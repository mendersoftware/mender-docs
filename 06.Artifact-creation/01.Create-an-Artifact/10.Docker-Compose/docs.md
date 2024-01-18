---
title: Tutorial: Docker Compose update
taxonomy:
    category: docs
    label: tutorial
---

In this tutorial, we will conduct a container update to a device using a
multi-container Docker composition with a Traefik gateway and a backend service
`whoami`. First we will create the update Artifact with a new Docker composition
and deploy it to the device. In the second part will show how update the Docker
images in the composition using binary delta to save size and data transfer
bandwidth.

### Prerequesites

To get started using the Docker Compose Update Module, we need to prepare the
target devices for accepting the deployment and the workstation for creating the
deployment.

##### Prepare the devices
Before installing the Update Module on the **target device**, you need to ensure that the following
dependencies are installed on the device:
 * [Mender client](../../../03.Client-installation/02.Install-with-Debian-package) (version >= 3.0)
 * [Docker Engine](https://docs.docker.com/engine/install/?target=_blank)
 * [Docker Compose](https://docs.docker.com/compose/install/?target=_blank) (version >= 2.0)
 * [`jq`](https://jqlang.github.io/jq/)
 * [`tree`](http://mama.indstate.edu/users/ice/tree/)
 * [`xdelta3`](https://github.com/jmacd/xdelta)

> To quickly verify the required dependencies are installed on your device, run
> the following commands:
> ```bash
> mender-update --version && \
>   docker --version && \
>   docker compose version && \
>   jq --version && \
>   tree --version && \
>   xdelta3 -V &&
> ```

To install the Docker Compose Update Module, run the following commands on your
devices:
<!--AUTOVERSION: "app-update-module/%/"/ignore-->
```bash
# Install Application Update Module
mkdir -p /usr/share/mender/modules/v3
wget https://raw.githubusercontent.com/mendersoftware/app-update-module/1.0.0/src/app \
        -O /usr/share/mender/modules/v3/app \
        && chmod +x /usr/share/mender/modules/v3/app
# Install Docker Compose module
mkdir -p /usr/share/mender/app-modules/v1
wget https://raw.githubusercontent.com/mendersoftware/app-update-module/1.0.0/src/app-modules/docker-compose \
        -O /usr/share/mender/app-modules/v1/docker-compose \
        && chmod +x /usr/share/mender/app-modules/v1/docker-compose
# Install the Configuration files
wget https://raw.githubusercontent.com/mendersoftware/app-update-module/1.0.0/conf/mender-app.conf \
        -O /etc/mender/mender-app.conf
wget https://raw.githubusercontent.com/mendersoftware/app-update-module/1.0.0/conf/mender-app-docker-compose.conf \
        -O /etc/mender/mender-app-docker-compose.conf
```

<!--AUTOVERSION: "app-update-module/blob/%/"/ignore-->
!!! The Docker Compose Update Module is a sub-module of the
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
Artifact containing the Docker Compose manifest and the Docker images used by
the composition. Including the Docker images is optional, excluding the images
will make the devices try to pull the images from the Docker registry.

#### Create the Mender artifact
Begin by creating the manifest on your workstation and saving it in a separate
directory:
```bash
mkdir -p manifests/v1
cat <<EOF > manifests/v1/docker-compose.yaml
version: "3.3"
services:
  gateway:
    image: "traefik:v2.9"
    command:
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--entrypoints.web.address=:80"
    ports:
      - "8080:80"
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock:ro"
  whoami:
    image: "traefik/whoami"
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.whoami.rule=Path(\`/whoami\`)"
      - "traefik.http.routers.whoami.entrypoints=web"
EOF
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
        --image docker.io/library/traefik:v2.9 \
        --image docker.io/traefik/whoami:latest \
        --orchestrator docker-compose \
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

Once deployed, the device will start serving a simple server on port 8080. You
can test the application by sending a request to path `/whoami` and the server
will echo the request.
To this end, we will leverage the Troubleshoot add-on and start a port-forward
session using the [mender-cli](../../../10.Downloads/docs.md#mender-cli).
```bash
mender-cli port-forward <device_id> 8080:8080
```
!!!!! Note that `device_id` should be replaced with the ID of the device (i.e `1bfcf943-4378-4a4f-bc88-0b4c86cdcc74`).

```bash
curl http://localhost:8080/whoami
```
> ```bash
> Hostname: d8ae8a9eca1c
> IP: 127.0.0.1
> IP: 172.19.0.3
> RemoteAddr: 172.19.0.2:58470
> GET /whoami HTTP/1.1
> Host: localhost:8080
> Accept: */*
> Accept-Encoding: gzip
> X-Forwarded-For: 172.19.0.1
> X-Forwarded-Host: localhost:8080
> X-Forwarded-Port: 8080
> X-Forwarded-Proto: http
> X-Forwarded-Server: c2c36ac1634b
> X-Real-Ip: 172.19.0.1
> ```


#### Update your composition using delta

! This section requires [xdelta3](https://github.com/jmacd/xdelta) to be
! installed on both your workstation and your device. Please make sure that
! this dependency is installed before proceeding.

Now that your Docker composition is running on the device, it is time to upgrade
the Traefik container to the next version. Create a new manifest directory and
bump gateway service to `traefik:v2.10`:
```bash
mkdir -p manifests/v2
cat <<EOF > manifests/v2/docker-compose.yaml
version: "3.3"
services:
  gateway:
    image: "traefik:v2.10"
    command:
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--entrypoints.web.address=:80"
    ports:
      - "8080:80"
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock:ro"
  whoami:
    image: "traefik/whoami"
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.whoami.rule=Path(\`/whoami\`)"
      - "traefik.http.routers.whoami.entrypoints=web"
EOF
```

Since we are only upgrading the Traefik service, we do not need to include the
image for the `whoami` service since this was provided by the last deployment.
And, to save bandwidth we will create a binary delta of the image for the
gateway service.

```bash
app-gen --artifact-name "${ARTIFACT_NAME}-v2" \
        --device-type "$DEVICE_TYPE" \
        --platform "$PLATFORM" \
        --application-name "$ARTIFACT_NAME" \
        --image docker.io/library/traefik:v2.9,docker.io/library/traefik:v2.10 \
        --orchestrator docker-compose \
        --manifests-dir ./manifests/v2 \
        --output-path artifact-v2.mender \
        --deep-delta \
        -- \
        --software-name "${ARTIFACT_NAME}" \
        --software-version "v2" \
        --depends "rootfs-image.${ARTIFACT_NAME}.version:v1"
```

!!!!! The last argument to `app-gen` ensures that the artifact is only
!!!!! installed if `v1` is installed.

The `--deep-delta` flag enables the delta feature which creates a binary delta
between the container images provided by the `--image` flag. Note that the
`--image` flag needs two inputs to be able to compute the delta. After
generating the artifact, upload the artifact to the Mender server and deploy it
to your device.

Congratulations! You successfully upgraded a component on your device. Continue
reading to learn more about advanced use-cases such as [custom update
modules](../../08.Create-a-custom-Update-Module)) and [software
versioning](../../09.Software-versioning).
