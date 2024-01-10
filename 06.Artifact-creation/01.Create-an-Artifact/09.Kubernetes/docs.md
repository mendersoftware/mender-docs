---
title: Tutorial: Kubernetes update
taxonomy:
    category: docs
    label: tutorial
---

In this tutorial, we will conduct a Kubernetes manifest based update to a device 
with a python application and PostgreSQL database. We will create the update
Artifact with a new manifest and deploy it to the device.

### Prerequisites

To get started using the Application Update Module for kubernetes-based applications
we need to perform certain configuration operations.

##### Prepare the devices
Before installing the Update Module on the **target device**, you need to install and configure
the following utilities on the device:
 * [Mender client](../../../03.Client-installation/02.Install-with-Debian-package) (version >= 3.0)
 * [`kubectl`](https://kubernetes.io/docs/tasks/tools/)
 * [`jq`](https://jqlang.github.io/jq/)
 * [`tree`](http://mama.indstate.edu/users/ice/tree/)
 * [`xdelta3`](https://github.com/jmacd/xdelta) (optional)

> To quickly verify the required dependencies are installed on your device, run
> the following commands:
> ```bash
> mender --version && \
>   kubectl version && \
>   jq --version && \
>   tree --version
> ```

We understand the existence of configured `kubectl` command as a proof that you have
configured kubernetes of any flavour, and we will not focus on the installation
but assume that kubectl presents a working interface to your cluster.

To install the Application Update Module and the Kubernetes submodule,
you need to run the following commands on your devices:
<!--AUTOVERSION: "app-update-module/%/"/ignore-->
```bash
# Install Application Update Module
mkdir -p /usr/share/mender/modules/v3
wget https://raw.githubusercontent.com/mendersoftware/app-update-module/1.0.0/src/app \
        -O /usr/share/mender/modules/v3/app \
        && chmod +x /usr/share/mender/modules/v3/app
# Install Kubernetes submodule
mkdir -p /usr/share/mender/app-modules/v1
wget https://raw.githubusercontent.com/mendersoftware/app-update-module/1.0.0/src/app-modules/k8s \
        -O /usr/share/mender/app-modules/v1/k8s \
        && chmod +x /usr/share/mender/app-modules/v1/k8s
# Install the Configuration files
wget https://raw.githubusercontent.com/mendersoftware/app-update-module/1.0.0/conf/mender-app.conf \
        -O /etc/mender/mender-app.conf
wget https://raw.githubusercontent.com/mendersoftware/app-update-module/1.0.0/conf/mender-app-k8s.conf \
        -O /etc/mender/mender-app-k8s.conf
```

<!--AUTOVERSION: "app-update-module/blob/%/"/ignore-->
!!! The Kubernetes Update Module is a sub-module of the
!!! [Application Update Module](https://github.com/mendersoftware/app-update-module/blob/master/docs/README-submodule-api.md#applications-updates).
!!! That is why we install two Update Modules in the snippet above.

##### Prepare the workstation
Once your devices are ready, return to your workstation and install the
Application Update Artifact Generator. First, make sure that you have
[mender-artifact](../../../10.Downloads/docs.md#mender-artifact) (version >= 3.0) installed
on your workstation, then install the Application Update Artifact Generator:
<!--AUTOVERSION: "app-update-module/%/"/ignore-->
```bash
BINDIR=$HOME/bin
mkdir -p $BINDIR
export PATH=$BINDIR:$PATH
wget https://raw.githubusercontent.com/mendersoftware/app-update-module/1.0.0/gen/app-gen \
        -O $BINDIR/app-gen
chmod +x $BINDIR/app-gen
```

### Create a deployment
The `app-gen` script we installed previously extends the
[mender-artifact](../../../10.Downloads/docs.md#mender-artifact) tool to create
Artifacts for container updates. We will use this tool to create a Mender
Artifact containing the Kubernetes manifest and the images used by
the composition.

#### Create the Mender artifact

In order to create a kubernetes-based application update module Mender artifact
we will prepare the following directory structure:

```shell
manifests/v1/
├── deployments
│   ├── app.yaml
│   └── postgres.yaml
├── secrets
│   └── secret-postgres.yaml
└── services
    └── service-postgres.yaml

4 directories, 4 files
```

And with the following contents:
```shell
==> manifests/v1/deployments/app.yaml <==
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: python-container
  template:
    metadata:
      labels:
        app: python-container
        tier: backend
    spec:
      containers:
        - name: python-container
          image: python:latest

==> manifests/v1/deployments/postgres.yaml <==
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: postgres-container
  template:
    metadata:
      labels:
        app: postgres-container
        tier: backend
    spec:
      containers:
        - name: postgres-container
          image: postgres:15.4
          env:
            - name: POSTGRES_USER
              valueFrom:
                secretKeyRef:
                  name: postgres-secret
                  key: user

            - name: POSTGRES_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: postgres-secret
                  key: password

            - name: POSTGRES_DB
              value: db0

          ports:
            - containerPort: 5432

==> manifests/v1/secrets/secret-postgres.yaml <==
apiVersion: v1
kind: Secret
metadata:
  name: postgres-secret
type: Opaque
data:
  user: dXNlcjA=
  password: bG9uZ3Bhc3N3b3Jk

==> manifests/v1/services/service-postgres.yaml <==
kind: Service
apiVersion: v1
metadata:
  name: postgres-service
spec:
  selector:
    app: postgres-container
  ports:
    - protocol: TCP
      port: 5432
      targetPort: 5432
```

To generate the artifact, we need to know the target platform of the devices we
want to deploy to. In the following example, we will assume the platform we are
deploying to is `linux/arm/v7` (`os/arch/variant`). You can check more details regarding
this notation in [Multi-platform images](https://docs.docker.com/build/building/multi-platform/) and
[Architectures other than amd64](https://github.com/docker-library/official-images#architectures-other-than-amd64).
```bash
ARTIFACT_NAME="myfirstcomposition"
DEVICE_TYPE="raspberrypi4"
PLATFORM="linux/arm/v7"
app-gen --artifact-name "$ARTIFACT_NAME" \
        --device-type "$DEVICE_TYPE" \
        --platform "$PLATFORM" \
        --application-name "$ARTIFACT_NAME" \
        --image docker.io/library/postgres:15.1 \
        --image docker.io/library/python:latest \
        --orchestrator k8s \
        --manifests-dir ./manifests/v1 \
        --output-path artifact.mender \
        -- \
        --software-name="$ARTIFACT_NAME" \
        --software-version="v1"
```

!!!!! All arguments after `--` are passed directly to `mender-artifact write
!!!!! module-image`. In the following example we will make use of
!!!!! [versioning constraints](../../09.Software-versioning/docs.md#application-updates-update-modules)
!!!!! to prevent deploying the wrong version to a device.

#### Deploy the Mender Artifact

The generated artifact is now ready to be deployed on the device. Open your
browser and navigate to the "Releases" column in [Hosted Mender
UI](https://hosted.mender.io/ui/releases) and upload your newly created
artifact. Once uploaded, navigate to the "Devices" column and select your device
and then click `Create a deployment for this device` in the `Device actions` in
the bottom right corner. Select your newly created artifact and click `CREATE
DEPLOYMENT`.

##### Verify your deployment

You can use the `kubectl` command on the device to verify that the pods are running:

```shell
 # kubectl get pods
NAME                                   READY   STATUS                   RESTARTS   AGE
python-deployment-567c5dbcbd-6k57l     1/1     Running                  0          20m
postgres-deployment-7b54fd68f9-8fkhj   1/1     Running                  0          20m
```
