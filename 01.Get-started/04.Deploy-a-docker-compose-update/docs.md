---
title: Deploy a Docker Compose update
taxonomy:
    category: docs
    label: tutorial
---


!!! This tutorial is not supported by the virtual device because it does not come with a package manager to install the needed dependencies.


In this tutorial, we will conduct a container update to a device using a
multi-container Docker composition with a Traefik gateway and a backend service
`whoami`. First we will create the update Artifact with a new Docker composition
and deploy it to the device. In the second part will show how update the Docker
images in the composition using binary delta to save size and data transfer
bandwidth.

In the example, we will observe Traefik as the primary container in the composition.
As a result the composition's naming and version will be heavily defined by the Traefik version. 
This makes sense because Traefik provides the primary functionality in the composition.
In deployments consisting of multiple containers without a clear primary, it can make sense to version the composition separate from the container. 


### Prerequisites

To get started using the Docker Compose Update Module, we need to prepare the
target devices for accepting the deployment and the workstation for creating the
deployment.

The tutorial assumes the usage of the Raspberry Pi with the reference OS image.
Please [prepare a Raspberry Pi device](../../01.Get-started/01.Preparation/01.Prepare-a-Raspberry-Pi-device/docs.md) if you haven't already.

Throughout the tutorial you will execute commands on the device.
You can use the [Remote terminal](../../09.Add-ons/50.Remote-Terminal/docs.md) to gain access to the shell of the device and execute the command.

The term [Update Module](../../03.Client-installation/05.Use-an-updatemodule/docs.md) will be used throughout the tutorial.
This is Mender mechanism to work with different types of updates, Docker Compose being one of them.
You don't need to know about this concept to complete get to a working example.


##### Installing the update module for docker compose 

! In this chapter the commands are executed on the **device** using the [Remote terminal](../../09.Add-ons/50.Remote-Terminal/docs.md)

Since you're using the [Raspberry Pi reference image](../../01.Get-started/01.Preparation/01.Prepare-a-Raspberry-Pi-device/docs.md)  Mender client is already present. 
You need to install the other external dependencies.

Become the root user on the device to simplify the install process:

``` bash
sudo su
```

Install the extra external dependencies on the device:

``` bash
printf "\n\nInstalling external dependencies \n\n" && \
apt-get install -y jq tree xdelta3 && \
printf "\n\nFeching docker install script \n\n" && \
curl -fsSL https://get.docker.com -o get-docker.sh && \
printf "\n\nExecuting docker install script \n\n" && \
sh get-docker.sh && \
printf "\n\nTesting docker \n\n" && \
docker ps && \
printf "\n\nSuccess \n\n"
```


With all the dependencies in place you can install the update module:

<!--AUTOVERSION: "app-update-module/%/"/ignore-->
```bash
printf "\n\nCreating the directory structure \n\n" && \
mkdir -p /usr/share/mender/modules/v3 && \
mkdir -p /usr/share/mender/app-modules/v1 && \
printf "\n\nDownloading and installing the app update module \n\n" && \
wget https://raw.githubusercontent.com/mendersoftware/app-update-module/1.1.0/src/app \
        -O /usr/share/mender/modules/v3/app && \
chmod +x /usr/share/mender/modules/v3/app && \
printf "\n\nDownloading and installing the docker compose update module \n\n" && \
wget https://raw.githubusercontent.com/mendersoftware/app-update-module/1.1.0/src/app-modules/docker-compose \
        -O /usr/share/mender/app-modules/v1/docker-compose \
        && chmod +x /usr/share/mender/app-modules/v1/docker-compose
printf "\n\nDownloading and installing the configuration files \n\n" && \
wget https://raw.githubusercontent.com/mendersoftware/app-update-module/1.1.0/conf/mender-app.conf \
        -O /etc/mender/mender-app.conf && \
wget https://raw.githubusercontent.com/mendersoftware/app-update-module/1.1.0/conf/mender-app-docker-compose.conf \
        -O /etc/mender/mender-app-docker-compose.conf && \
printf "\n\nSuccess \n\n"
```

##### Prepare the workstation

! In this chapter the commands are executed on the **workstation**

Install the external dependencies:

``` bash
sudo su
```

```bash
printf "\n\nInstalling external dependencies \n\n" && \
apt-get install -y xdelta3 && \
printf "\n\nSuccess  \n\n"
exit 
```

Run the following to verify:

<!--AUTOVERSION: "Xdelta version %"/ignore-->
``` bash
xdelta3 -h 
# Xdelta version 3.0.11, Copyright (C) 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015 Joshua MacDonald
# Xdelta comes with ABSOLUTELY NO WARRANTY.
# This is free software, and you are welcome to redistribute it
# under certain conditions; see "COPYING" for details.
# usage: xdelta3 [command/options] [input [output]]
# make patch:
# 
#   xdelta3.exe -e -s old_file new_file delta_file
```

You also need to need to install [mender-artifact](../../10.Downloads/docs.md#mender-artifact) (version >= 3.0) on your workstation.
This isn't installable through a copy code snippet.
Please follow the instructions to install [mender-artifact](../../10.Downloads/docs.md#mender-artifact) on your workstation.

To verify the successful install, run the commands below:

```bash
mender-artifact -h 
# Output
# NAME:
#    mender-artifact - interface for manipulating Mender Artifacts
# 
# USAGE:
#    mender-artifact [--version][--help] <command> [<args>]
# ...
```

Next install the `app-gen` tool.
This is the tool we will use to generate the artifacts.

<!--AUTOVERSION: "app-update-module/%/"/ignore-->
```bash
printf "\n\nCreating the directory structure \n\n" && \
mkdir docker-compose-evaluation && \
printf "\n\nDownloading and installing the docker compose generator tool \n\n" && \
cd docker-compose-evaluation && \
wget https://raw.githubusercontent.com/mendersoftware/app-update-module/1.1.0/gen/app-gen \
        -O app-gen && \
chmod +x app-gen && \
printf "\n\nSuccess \n\n"
```

Test the installation:

```bash
./app-gen
# Simple tool to generate Mender Artifact suitable for App Update Module
# 
# Usage: ./app-gen [options] [-- [options-for-mender-artifact] ]
# ...
```


### Create a deployment

! In this chapter the commands are executed on the **workstation**

The `app-gen` script we installed previously extends the
[mender-artifact](../../10.Downloads/docs.md#mender-artifact) tool to create
Artifacts for container updates. We will use this tool to create a Mender
Artifact containing the Docker Compose manifest and the Docker images used by
the composition. Including the Docker images is optional, excluding the images
will make the devices try to pull the images from the Docker registry.

#### Create the Mender Artifact

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

To generate the Artifact, we need to know the target platform of the devices we want to deploy to. 
In this tutorial the device is a Raspberry Pi so it's set to `linux/arm/v7` (`os/arch/variant`).

!!! You can check more details regarding this notation in [Multi-platform images](https://docs.docker.com/build/building/multi-platform/) and [Architectures other than amd64](https://github.com/docker-library/official-images#architectures-other-than-amd64).

Run the command below to generate the update Artifact:

```bash
ARTIFACT_NAME="traefik-composition"

app-gen --artifact-name "$ARTIFACT_NAME-$VERSION" \
        --device-type "raspberrypi4" \
        --device-type "raspberrypi3" \
        --platform "linux/arm/v7" \
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

The generated Artifact (`.mender` extension) is now ready to be deployed on the device. 

Open your browser and navigate to the "Releases" column in the [Mender UI](https://hosted.mender.io/ui/releases) and upload your newly created Artifact. 
Once uploaded, navigate to the "Devices" column and select your device and then click `Create a deployment for this device` in the `Device actions` in the bottom right corner. 
Select your newly created Artifact and click `CREATE DEPLOYMENT`.

##### Verify your deployment

! In this chapter the commands are executed on the **device** using the [Remote terminal](../../09.Add-ons/50.Remote-Terminal/docs.md)

Once deployed, the device will start serving a simple server on port 8080. 
You can test the application by sending a request to path `/whoami` and the server will echo the request.


```bash
docker ps


# Output
#  CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS         PORTS                                   NAMES
#  3a27e70761b8   traefik:v2.9     "/entrypoint.sh --pr…"   9 minutes ago   Up 9 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   traefik-composition-gateway-1
#  01ca7e0e2f93   traefik/whoami   "/whoami"                9 minutes ago   Up 9 minutes   80/tcp                                  traefik-composition-whoami-1
```

If you get the similar output as above it shows that the containers on the device are running the correct versions.
Run the following command to verify it works:

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

! In this chapter the commands are executed on the **workstation**

Now that your Docker composition is running on the device, it is time to upgrade
the Traefik container to the next version. Create a new manifest directory and
update the gateway service to `traefik:v2.10`:

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

Proceed with creating the Artifact:


```bash
ARTIFACT_NAME="traefik-composition"
PREVIOUS_VERSION="v2.9"
NEW_VERSION="v2.10"

app-gen --artifact-name "$ARTIFACT_NAME-$VERSION" \
        --device-type "raspberrypi4" \
        --device-type "raspberrypi3" \
        --platform "linux/arm/v7" \
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

The `--depends`  argument sets a [versioning constraints](../../06.Artifact-creation/09.Software-versioning/docs.md#application-updates-update-modules).
This ensures that the new Artifact can only be installed on top of a specific version running on the device. 
This is a requirement for delta updates as they can only be applied to a specific base version.

The `--deep-delta` flag enables the delta feature of comparing individual layers of the composition and calculating delta between the each.
This gives a better compression ratio and is recommended as the default delta.


Upload the Artifact to Hosted Mender and deploy it to the device.

#### Verify the update on the device

! In this chapter the commands are executed on the device using the [Remote terminal](../../09.Add-ons/50.Remote-Terminal/docs.md)

```bash
docker ps

# Output 
# CONTAINER ID   IMAGE            COMMAND                  CREATED          STATUS          PORTS                                   NAMES
# 0a81f8f74b30   traefik:v2.10    "/entrypoint.sh --pr…"   58 seconds ago   Up 55 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   traefik-composition-gateway-1
# 6cacafb1e9d3   traefik/whoami   "/whoami"                58 seconds ago   Up 55 seconds   80/tcp                                  traefik-composition-whoami-1
```

If you get the similar output as above it shows that the containers have been updated to the new versions. 


### Benefits of Delta Updates

! In this chapter the commands are executed on the **workstation**

The motivation for using the delta updates is to have a smaller Artifact for the same effect.
This varies a lot depending on the amount of content change between the two versions.
The more the software is alike, the more the delta will save.

Let's compare how much saving the delta introduced in this case by creating a non-delta Artifact for the new version.


```bash
ARTIFACT_NAME="traefik-composition"
VERSION="v2.10"

app-gen --artifact-name "$ARTIFACT_NAME-$VERSION" \
        --device-type "raspberrypi4" \
        --device-type "raspberrypi3" \
        --platform "linux/arm/v7" \
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

So in this case we are seeing a ~28% decrease in size, though the size savings of deltas vary depending on the changes between Artifacts and can go up to 90% in some cases.
