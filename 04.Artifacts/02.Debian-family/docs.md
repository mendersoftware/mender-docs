---
title: Building a Mender Debian image
taxonomy:
    category: docs
---

`mender-convert` can be used to convert existing disk images for use with
Mender. It will generate a new disk image with two rootfs partitions, install a
bootloader that supports booting either of the root partitions and install the
Mender client and its configuration.

The output of `mender-convert` is:
* The converted disk image described above ready to be flashed into an SD card.
* A Mender Artifact formatted update to be deployed remotely to devices running
  Mender through the Mender Server.
* An ext4 image of the modified filesystem for advanced users.

### Recommended workflow

The recommended workflow for using `mender-convert` is to rely on a *golden disk
image* that should be replicated in a robust way to many devices. The steps in
this workflow are:

1. Install a fresh OS to a device storage (typically an SD card)
2. Boot the device, log in, and make modifications in run-time, e.g. install
   packages, change configurations
3. Power off the device with the (now updated) golden image
4. Copy the contents of the golden image back to your workstation (e.g. using
   dd)
5. Generate a Mender Artifact and disk image from this golden image using
   `mender-convert` (continue reading for details)
6. Deploy the Artifact to all devices

Note that your golden device or SD card is not running Mender and is not
modified during deployments. It is simply the "source" for generating the
Artifacts that you deploy to the devices in the field.

In order to create another OTA update, the device with the golden image is
booted again, i.e. the steps from 2. and onwards are carried out again.

!!! `mender-convert` is currently tested on BeagleBone and Raspberry Pi3, using
official Debian or Raspbian images. The intention is to extend and test
`mender-convert` to cover more boards and OSes and finally make it
board-agnostic.

## Prerequisites

### Enough free disk space on your workstation

The amount of disk space needed depends on the size of your original raw disk image.
You should have at least **4 x the size of the raw disk image** available.
For example, if your raw disk image is 4 GB, you should have at least 16 GB free disk space on your workstation where you are running `mender-convert`.

### A golden raw disk image

As described in the workflow above, you need a raw disk image as input to `mender-convert`. This is the image that contains the root file system you want to deploy to many devices. Note that this must be a *complete disk image* (usually they have a `.img` suffix).

Board manufacturers typically provide a disk image for you to start with so you can download and use `mender-convert` directly on this image.

If you have made run-time modifications on your device and want to copy the image from an existing SD card, insert it into your workstation and run the following command:

```bash
dd if=<DEVICE> of=golden-image-1.img bs=1M conv=fdatasync
```

!!! Replace `<DEVICE>` with the location of your SD card. Normally this would be something like `/dev/mmcblk0` or `/dev/sdb`.


### Docker

#### Docker Engine 17.03

Follow the [documentation to install Docker
Engine](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/?target=_blank),
version **17.03 or later**.

##### Docker permissions

Invoking the docker commands may fail when the local user has insufficient
permissions to connect to the docker daemon. In Ubuntu 18.04, the user must be a
member of the `docker` group to be able to access it. Please check the
documentation for your host OS if you encounter connection issues with docker.

### Download mender-convert

Clone `mender-convert` from the official repository:

<!--AUTOVERSION: "-b % https://github.com/mendersoftware/mender-convert"/mender-convert-->
```bash
git clone -b master https://github.com/mendersoftware/mender-convert.git
```

## Build the mender-convert container image

Change directory to where you downloaded `mender-convert`:

```bash
cd mender-convert
```

Then, run the following command to build the container based on Ubuntu 18.04 with all required dependencies for `mender-convert`:

```bash
./docker-build
```

## Convert a raw disk image

Move your *golden disk image* into an input subdirectory:

```bash
mkdir -p input
mv <PATH_TO_MY_GOLDEN_IMAGE> input/golden-image-1.img
```

Then adjust to the correct paths below and run the conversion:

```bash
DEVICE_TYPE="raspberrypi3"
RAW_DISK_IMAGE="input/golden-image-1.img"

ARTIFACT_NAME="golden-image-1-mender-integ"
MENDER_DISK_IMAGE="golden-image-1-mender-integ.sdimg"
TENANT_TOKEN="<INSERT-TOKEN-FROM hosted Mender>"

./docker-mender-convert from-raw-disk-image                      \
            --raw-disk-image $RAW_DISK_IMAGE                     \
            --mender-disk-image $MENDER_DISK_IMAGE               \
            --device-type $DEVICE_TYPE                           \
            --artifact-name $ARTIFACT_NAME                       \
            --bootloader-toolchain arm-buildroot-linux-gnueabihf \
            --server-url "https://hosted.mender.io"              \
            --tenant-token $TENANT_TOKEN
```

!!! The conversion may take 10 minutes, depending on the resources available on your machine.

After a successful conversion, your images can be found in `output/`.

The above invocation will use configuration defaults for use with the Hosted
Mender in production environment. If on premise server is used, then adjust
`--server-url` accordingly, and replace `--tenant-token` option with
`--server-cert` option, specifying a valid path for the server certificate.

## Building for demo environment

If instead you wish to use the [Mender demo
environment](../../../getting-started/on-premise-installation), execute the
command with these parameters:

```
bash
DEVICE_TYPE="raspberrypi3"
RAW_DISK_IMAGE="input/golden-image-1.img"

ARTIFACT_NAME="golden-image-1-mender-integ"
MENDER_DISK_IMAGE="golden-image-1-mender-integ.sdimg"

DEMO_HOST_IP="192.168.10.2"

./docker-mender-convert from-raw-disk-image                      \
            --raw-disk-image $RAW_DISK_IMAGE                     \
            --mender-disk-image $MENDER_DISK_IMAGE               \
            --device-type $DEVICE_TYPE                           \
            --artifact-name $ARTIFACT_NAME                       \
            --bootloader-toolchain arm-buildroot-linux-gnueabihf \
            --demo                                               \
            --demo-host-ip $DEMO_HOST_IP
```
