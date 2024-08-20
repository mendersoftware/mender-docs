---
title: Deploy a Docker Compose update
taxonomy:
    category: docs
    label: tutorial
---


!!! This tutorial is not supported by the virtual device because it does not come
!!! with a package manager to install the needed dependencies.


In this tutorial, we will conduct a container update to a device using a
multi-container Docker composition with a Traefik gateway and a backend service
`whoami`. First we will create the update Artifact with a new Docker composition
and deploy it to the device. In the second part will show how update the Docker
images in the composition using binary delta to save size and data transfer
bandwidth.

In the example, we'll observe Traefik as the primary container in the composition.
As a result the composition's naming and version will be heavily defined by the Traefik version. 
This made sense because Traefik provides the primary functionality in the composition.
In deployments consisting of multiple containers without a clear primary, it can make sense to version the composition separate from the container. 


### Prerequisites

To get started using the Docker Compose Update Module, we need to prepare the
target devices for accepting the deployment and the workstation for creating the
deployment.

The tutorial assumes the usage of the Raspberry Pi with the reference OS image.
Please read [this section](../../../../01.Get-started/01.Preparation/01.Prepare-a-Raspberry-Pi-device/docs.md) of the Getting started to prepare the device.

Throughout the tutorial you'll be expected to execute commands on the device.
You can use the [Remote terminal](../../../../09.Add-ons/50.Remote-Terminal/docs.md) to gain access to the shell of the device and execute the command.


##### Installing dependencies on the devices

Before installing the Update Module on the device, you need to ensure that the following
dependencies are installed on the device:
 * [Mender client](../../../03.Client-installation/02.Install-with-Debian-package) (version >= 3.0)
 * [Docker Engine](https://docs.docker.com/engine/install/?target=_blank)
 * [Docker Compose](https://docs.docker.com/compose/install/?target=_blank) (version >= 2.0)
 * [`jq`](https://jqlang.github.io/jq/)
 * [`tree`](http://mama.indstate.edu/users/ice/tree/)
 * [`xdelta3`](https://github.com/jmacd/xdelta)


To verify the presence of the required dependencies, run the commands below on your device:
```bash
mender-update --version && \
  docker --version && \
  docker compose version && \
  jq --version && \
  tree --version && \
  xdelta3 -V
```

To install the Docker Compose Update Module, run the following commands on your device:
<!--AUTOVERSION: "app-update-module/%/"/ignore-->
```bash
# Install Application Update Module
sudo su
mkdir -p /usr/share/mender/modules/v3
wget https://raw.githubusercontent.com/mendersoftware/app-update-module/1.1.0/src/app \
        -O /usr/share/mender/modules/v3/app \
        && chmod +x /usr/share/mender/modules/v3/app
# Install Docker Compose module
mkdir -p /usr/share/mender/app-modules/v1
wget https://raw.githubusercontent.com/mendersoftware/app-update-module/1.1.0/src/app-modules/docker-compose \
        -O /usr/share/mender/app-modules/v1/docker-compose \
        && chmod +x /usr/share/mender/app-modules/v1/docker-compose
# Install the Configuration files
wget https://raw.githubusercontent.com/mendersoftware/app-update-module/1.1.0/conf/mender-app.conf \
        -O /etc/mender/mender-app.conf
wget https://raw.githubusercontent.com/mendersoftware/app-update-module/1.1.0/conf/mender-app-docker-compose.conf \
        -O /etc/mender/mender-app-docker-compose.conf
```

<!--AUTOVERSION: "app-update-module/blob/%/"/ignore-->

!!! The Docker Compose Update Module is a sub-module of the
!!! [Application Update Module](https://github.com/mendersoftware/app-update-module/blob/master/docs/README-submodule-api.md#applications-updates).
!!! That is why we install two Update Modules in the snippet above.

##### Prepare the workstation

To generate the update artifacts we'll need to install the `Application Update Artifact Generator`.
This tool has a dependency on [mender-artifact](../../../10.Downloads/docs.md#mender-artifact) (version >= 3.0).
Please follow the instructions to install [mender-artifact](../../../10.Downloads/docs.md#mender-artifact) on your workstation.

To verify the presence of the required dependencies, run the commands below on your device:
Please note that `app-gen` requires the presence of `mender-artifact` in PATH.

```bash
mender-artifact -h 
# Output
# NAME:
#    mender-artifact - interface for manipulating Mender artifacts
# 
# USAGE:
#    mender-artifact [--version][--help] <command> [<args>]
# ...
```


Next install the `app-gen` tool.
<!--AUTOVERSION: "app-update-module/%/"/ignore-->

```bash
mkdir docker-compose-evaluation
cd docker-compose-evaluation
wget https://raw.githubusercontent.com/mendersoftware/app-update-module/1.1.0/gen/app-gen \
        -O app-gen
chmod +x app-gen
```

Test the installation:

```bash
./app-gen
# Simple tool to generate Mender Artifact suitable for App Update Module
# 
# Usage: ./app-gen [options] [-- [options-for-mender-artifact] ]
# ...
```

!!! When integrating into the CI/CD pipelines, you might consider adding the `app-gen` to `PATH`. 


##### Workstation variables

The example snippets depend on some shared host variables.
Please ensure they are set for any host command you will be running.

If you're executing this on a single shell, you won't need to reset the variables.




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
VERSION="v2.9"
MANIFEST_DIR="manifests/$VERSION"

mkdir -p $MANIFEST_DIR

cat <<EOF > $MANIFEST_DIR/docker-compose.yaml
version: "3.3"
services:
  gateway:
    image: "traefik:$VERSION"
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
want to deploy to. 
In the following example, where we assume the device to be the Raspberry Pi,  we are deploying to is `linux/arm/v7` (`os/arch/variant`).

You can check more details regarding this notation in [Multi-platform images](https://docs.docker.com/build/building/multi-platform/) and [Architectures other than amd64](https://github.com/docker-library/official-images#architectures-other-than-amd64).

Run the command below to generate the update artifact:

```bash
ARTIFACT_NAME="traefik-composition"
DEVICE_TYPE="raspberrypi4"
PLATFORM="linux/arm/v7"

app-gen --artifact-name "$ARTIFACT_NAME-$VERSION" \
        --device-type "$DEVICE_TYPE" \
        --platform "$PLATFORM" \
        --application-name "$ARTIFACT_NAME" \
        --image docker.io/library/traefik:$VERSION \
        --image docker.io/traefik/whoami:latest \
        --orchestrator docker-compose \
        --manifests-dir $MANIFEST_DIR \
        --output-path "$ARTIFACT_NAME-$VERSION".mender \
        -- \
        --software-name="$ARTIFACT_NAME" \
        --software-version="$VERSION"
```

!!! For Raspberry pi 3 use  `DEVICE_TYPE="raspberrypi3"`
!!! All arguments after `--` are passed directly to `mender-artifact write module-image`. 


The generated artifact (`.mender` extension) is now ready to be deployed on the device. 


#### Deploy the Mender Artifact

Open your browser and navigate to the "Releases" column in the [Mender UI](https://hosted.mender.io/ui/releases) and upload your newly created artifact. 
Once uploaded, navigate to the "Devices" column and select your device and then click `Create a deployment for this device` in the `Device actions` in the bottom right corner. 
Select your newly created artifact and click `CREATE DEPLOYMENT`.

##### Verify your deployment

Once deployed, the device will start serving a simple server on port 8080. 
You can test the application by sending a request to path `/whoami` and the server will echo the request.

Open the Remote terminal from the Hosted Mender UI and run the following:

```bash
docker ps


# Output
#  CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS         PORTS                                   NAMES
#  3a27e70761b8   traefik:v2.9     "/entrypoint.sh --pr…"   9 minutes ago   Up 9 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   traefik-composition-gateway-1
#  01ca7e0e2f93   traefik/whoami   "/whoami"                9 minutes ago   Up 9 minutes   80/tcp                                  traefik-composition-whoami-1
```

If you get the similar output as above it shows that the containers on the device are running the correct versions.
Command below will test for functionality:


``` bash
curl http://localhost:8080/whoami

# Output:
# Hostname: d8ae8a9eca1c
# IP: 127.0.0.1
# IP: 172.19.0.3
# RemoteAddr: 172.19.0.2:58470
# GET /whoami HTTP/1.1
# Host: localhost:8080
# Accept: */*
# Accept-Encoding: gzip
# X-Forwarded-For: 172.19.0.1
# X-Forwarded-Host: localhost:8080
# X-Forwarded-Port: 8080
# X-Forwarded-Proto: http
# X-Forwarded-Server: c2c36ac1634b
# X-Real-Ip: 172.19.0.1
```


#### Update your composition using delta

! This section requires [xdelta3](https://github.com/jmacd/xdelta) to be
! installed on both your workstation and your device. Please make sure that
! this dependency is installed before proceeding.

Now that your Docker composition is running on the device, it is time to upgrade
the Traefik container to the next version. Create a new manifest directory and
bump gateway service to `traefik:v2.10`:

```bash
VERSION="v2.10"
MANIFEST_DIR="manifests/$VERSION"

mkdir -p $MANIFEST_DIR

cat <<EOF > $MANIFEST_DIR/docker-compose.yaml
version: "3.3"
services:
  gateway:
    image: "traefik:$VERSION"
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
image for the `whoami` service in the command below.

Proceed with creating the artifact:


```bash
ARTIFACT_NAME="traefik-composition"
DEVICE_TYPE="raspberrypi4"
PLATFORM="linux/arm/v7"
PREVIOUS_VERSION="v2.9"
NEW_VERSION="v2.10"

app-gen --artifact-name "$ARTIFACT_NAME-$VERSION" \
        --device-type "$DEVICE_TYPE" \
        --platform "$PLATFORM" \
        --application-name "$ARTIFACT_NAME" \
        --image docker.io/library/traefik:$PREVIOUS_VERSION,docker.io/library/traefik:$NEW_VERSION \
        --orchestrator docker-compose \
        --manifests-dir $MANIFEST_DIR \
        --output-path "$ARTIFACT_NAME-$VERSION".mender \
        --deep-delta \
        -- \
        --software-name "${ARTIFACT_NAME}" \
        --software-version="$VERSION" \
        --depends "rootfs-image.${ARTIFACT_NAME}.version:$PREVIOUS_VERSION"
```

In the above command we create a binary delta of the image to save bandwidth. 
That is why some parameters are different compared to the first version.

The `--image` argument now has two images listed.
This instructs the tool to create a delta to update form the previous to the new version.

The `--depends`  argument sets a [versioning constraints](../../09.Software-versioning/docs.md#application-updates-update-modules).
This ensures that the new artifact can only be installed on top of a specific version running on the device. 
This is a requirement for delta updates as they can only be applied to a specific base version.

The `--deep-delta` flag enables the delta feature of comparing individual layers of the composition and calculating delta between the each.
This gives a better compression ratio and is recommended as the default delta.


Upload the artifact to Hosted Mender and deploy it to the device.
Once complete open the Remote terminal from the Hosted Mender UI and run the following:

```bash
docker ps

# Output 
# CONTAINER ID   IMAGE            COMMAND                  CREATED          STATUS          PORTS                                   NAMES
# 0a81f8f74b30   traefik:v2.10    "/entrypoint.sh --pr…"   58 seconds ago   Up 55 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   traefik-composition-gateway-1
# 6cacafb1e9d3   traefik/whoami   "/whoami"                58 seconds ago   Up 55 seconds   80/tcp                                  traefik-composition-whoami-1
```

If you get the similar output as above it shows that the containers have been updated to the new versions. 


### Extra: what are the delta benefits?


The motivation for using the delta updates is to have a smaller artifact for the same effect.
This varies a lot depending on the amount of content change between the two versions.
The more the software is alike, the more the delta will save.

Let's compare how much saving the delta introduced in this case by creating a non-delta artifact for the new version.


```bash
ARTIFACT_NAME="traefik-composition"
DEVICE_TYPE="raspberrypi4"
PLATFORM="linux/arm/v7"
VERSION="v2.10"

app-gen --artifact-name "$ARTIFACT_NAME-$VERSION" \
        --device-type "$DEVICE_TYPE" \
        --platform "$PLATFORM" \
        --application-name "$ARTIFACT_NAME" \
        --image docker.io/library/traefik:$VERSION \
        --orchestrator docker-compose \
        --manifests-dir $MANIFEST_DIR \
        --output-path "NO-DELTA-${ARTIFACT_NAME}-${VERSION}".mender \
        -- \
        --software-name "${ARTIFACT_NAME}" \
        --software-version="$VERSION"
```


And compare the difference:

``` bash
du -h NO-DELTA-traefik-composition-v2.10.mender traefik-composition-v2.10.mender 
# Output: 
# 38M     NO-DELTA-traefik-composition-v2.10.mender
# 28M     traefik-composition-v2.10.mender
```

So in this case we're seeing a ~28% decrease in size.
