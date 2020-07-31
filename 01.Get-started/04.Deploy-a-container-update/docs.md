---
title: Deploy a container update
taxonomy:
    category: docs
---

!!! This tutorial is not supported by the virtual device because it does not come
!!! with a package manager to install the needed dependencies.

This tutorial will walk you trough how to deploy Docker container updates with
Mender. We will be using the
[Docker Update Module](https://hub.mender.io/t/docker/324?target=blank) which
allows you to specify a list of container images and their versions in a
[Mender Artifact](../../02.Overview/02.Artifact/docs.md) which
can later be deployed to your device using the hosted Mender server.

## Prerequisites

To follow this tutorial, you will need to install:

* [Docker Engine](https://docs.docker.com/engine/install?target=_blank) on your
workstation.

It is also assumed that you have completed the following tutorials:

* [Prepare a Raspberry Pi device](../01.Preparation/01.Prepare-a-Raspberry-Pi-device/docs.md)
* [Deploy an application update](../02.Deploy-an-application-update/docs.md)

## Step 1 - Install Docker Engine on your Raspberry Pi

Log in to your Raspberry Pi and run the commands outlined below.

The [Docker Update Module](https://hub.mender.io/t/docker/324?target=blank) has
a dependency on the `jq` utility, run the following command to install it:

```bash
sudo apt-get install jq
```

Download the Docker install script:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
```

Execute the Docker install script:

```bash
sudo sh get-docker.sh
```

Once the installation script has finished, verify that you can run the
`sudo docker images` command.

You will get similar output to below:


>```bash
>pi@raspberrypi:~$ sudo docker images
>REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
>```

As you can see, there are no Docker images on the device. In the next step we
will generate a
[Mender Artifact](../../02.Overview/02.Artifact/docs.md) which will
download an image.

### Step 2 - Download the mender-artifact utility on your workstation

Prepare destination directory:

```bash
mkdir -p ${HOME}/bin
```

Download the `mender-artifact` binary

<!--AUTOVERSION: "mender-artifact/%/"/mender-artifact -->
```bash
wget https://d1b0l86ne08fsf.cloudfront.net/mender-artifact/master/linux/mender-artifact -O ${HOME}/bin/mender-artifact
```

Make the `mender-artifact` binary executable:

```bash
chmod +x "${HOME}/bin/mender-artifact"
```

Add `${HOME}/bin` to `PATH`:

```bash
export PATH="${PATH}:${HOME}/bin"
```

!!! Add above to `~/.bashrc` or equivalent to make it persistent across multiple
!!! terminal sessions.


## Step 3 - Prepare a Mender Artifact on your workstation

Prepare a workspace and change directory to it:

```bash
mkdir "${HOME}/mender-docker" && cd "${HOME}/mender-docker"
```

Download the `docker-artifact-gen` utility script:

<!--AUTOVERSION: "mender/%"/mender-->
```bash
wget https://raw.githubusercontent.com/mendersoftware/mender/master/support/modules-artifact-gen/docker-artifact-gen
```

Make `docker-artifact-gen` executable:

```bash
chmod +x docker-artifact-gen
```

Set the target device type:

```bash
DEVICE_TYPE="raspberrypi4"
```

!!! Change `raspberrypi4` to `raspberrypi3` if you are using a Raspberry Pi 3


Generate a Mender Artifact that will deploy the `hello-world` Docker container image:

```bash
./docker-artifact-gen \
    -n "hello-world-container-update" \
    -t "${DEVICE_TYPE}" \
    -o "hello-world-container-update.mender" \
    "hello-world"
```

!!! [hello-world](https://hub.docker.com/_/hello-world?target=_blank) is the name of the Docker
!!! image that we want to download on the device when we deploy the generated
!!! [Mender Artifact](../../02.Overview/02.Artifact/docs.md)

## Step 3 - Deploy the Docker update

Upload the file `hello-world-container-update.mender` from the previous step
to the hosted Mender. Go to the **RELEASES** tab in the UI and upload it.

Once uploaded, click **CREATE DEPLOYMENT WITH THIS RELEASE** in order to deploy
it to your device.

If the deployment of `hello-world-container-update.mender` is successful, you
will see that there is a image downloaded on the device:

>```bash
>pi@raspberrypi:~$ sudo docker images
>REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
>hello-world         <none>              851163c78e4a        4 months ago        4.85kB
>```

The [Docker Update Module](https://hub.mender.io/t/docker/324?target=blank) will
download the specified images from e.g https://hub.docker.io. It will not
stop or start the images. This is a reference module, intended  as a starting
point to develop your own Docker container update strategy.

The [Kubernetes Update Module](https://hub.mender.io/t/kubernetes/1939?target=_blank) is very
similar and instead allows deployment of Kubernetes manifesto files.

You can explore other types of updates available by extending the Mender client
in the
[Update Modules category in the Mender Hub community platform](https://hub.mender.io/c/update-modules/13?target=_blank).
