---
title: Convert a Mender Debian image
taxonomy:
    category: docs
---


The `mender-convert` utility can be used to convert existing disk images for use with
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
booted again, i.e. the steps from 2. onwards are carried out again.

!!! `mender-convert` is currently tested on BeagleBone, Raspberry Pi 3 and
!!! Raspberry Pi 4, using official Debian or Raspberry Pi OS images. The intention is
!!! to extend and test `mender-convert` to cover more boards and OSes.

## Prerequisites

### Enough free disk space on your workstation

The amount of disk space needed depends on the size of your original raw disk
image. You should have at least **4 x the size of the raw disk image**
available. For example, if your raw disk image is 4 GB, you should have at least
16 GB free disk space on your workstation where you are running
`mender-convert`.

### A golden raw disk image

As described in the workflow above, you need a raw disk image as input to
`mender-convert`. This is the image that contains the root file system you want
to deploy to many devices. Note that this must be a *complete disk image*.

Board manufacturers typically provide a disk image for you to start with so you
can download and use `mender-convert` directly on this image.

If you have made run-time modifications on your device and want to copy the
image from an existing SD card, insert it into your workstation and run the
following command:

```bash
dd if=<DEVICE> of=golden-image-1.img bs=1M conv=fdatasync
```

!!! Replace `<DEVICE>` with the location of your SD card. Normally this would be
something like `/dev/mmcblk0` or `/dev/sdb`.


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

Then, run the following command to build the container with all required
dependencies for `mender-convert`:

```bash
./docker-build
```

## Configure the Mender client server configuration

The easiest, and most straight-forward way, is to integrate the client with
[hosted Mender](https://hosted.mender.io?target=_blank):

#### Using [hosted Mender](https://hosted.mender.io?target=_blank)
```bash
./scripts/bootstrap-rootfs-overlay-hosted-server.sh \
    --output-dir ${PWD}/rootfs_overlay_demo \
    --tenant-token "Paste token from https://hosted.mender.io/ui/#/settings/my-organization"
```

However, there are additional scripts in the `scripts/` directory to enable
working with a local demo server, or a production server.

## Convert a raw disk image

Move your *golden disk image* into an input subdirectory:

```bash
mkdir -p input
mv <PATH_TO_MY_GOLDEN_IMAGE> input/golden-image-1.img
```

### Use the mender-convert container image

Run mender-convert from inside the container with your desired options, e.g.

```bash
MENDER_ARTIFACT_NAME=release-1 ./docker-mender-convert \
    --disk-image input/golden-image-1.img \
    --config configs/raspberrypi3_config \
    --overlay rootfs_overlay_demo/
```

Conversion will take 10-30 minutes, depending on image size and resources
available. In the meantime can watch `work/convert.log` for progress and
diagnostics information.

After it finishes, you can find your images in the `deploy` directory on your
host machine.
