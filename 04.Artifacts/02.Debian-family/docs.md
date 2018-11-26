---
title: Building a Mender Debian image
taxonomy:
    category: docs
---

The `mender-convert` utility can be used to convert existing disk images for use with Mender. It will generate a new disk image with two rootfs partitions, install a bootloader that supports booting either of the root partitions and install the Mender client and its configuration.

A typical workflow for using `mender-convert` is to rely on a *golden disk image* that should be replicated in a robust way to many devices. The steps in this workflow are:

1. Install a fresh OS to a device storage
2. Boot the device
3. Make modifications in run-time, e.g. install packages, change configurations
4. Power off the device with the (now updated) golden image
5. Generate a Mender Artifact and disk image from this golden image using `mender-convert`
6. Deploy the Artifact to all devices

In order to create another OTA update, the device with the golden image is booted again, i.e. the steps from 2. and onwards are carried out again.

!!! `mender-convert` is currently tested on BeagleBone and Raspberry Pi3, using official Debian or Raspbian images. The intention is to extend and test the utility to cover more boards and OSes and finally make it board-agnostic.

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


### A Mender client for your device

You need a Mender client binary compiled for your target device.
See [cross-compiling Mender client](../../client-configuration/cross-compiling) for steps how to compile one.


### Dependencies for mender-convert

If you are using Ubuntu 18.04, install the dependencies by running the following command:

```bash
sudo apt install kpartx bison flex mtools parted mtd-utils e2fsprogs u-boot-tools pigz device-tree-compiler autoconf autotools-dev libtool pkg-config python
```

Disable sanity checks made by Mtools commands. These checks reject copy/paste operations on converted disk images.
```bash
echo "mtools_skip_check=1" >> ${HOME}/.mtoolsrc
```
<!--AUTOVERSION: "version %"/ignore-->
If you want to convert RaspberryPi3 raw disk image, you need to install GCC ARM toolchain in version 6.3.1 to meet U-Boot build requirements. You can download it from here:
<!--AUTOVERSION: "linaro-%"/ignore-->
```bash
wget -nc -q http://releases.linaro.org/components/toolchain/binaries/6.3-2017.05/arm-linux-gnueabihf/gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf.tar.xz
```
Next, unpack it:
<!--AUTOVERSION: "linaro-%"/ignore-->
```bash
tar -xJf gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf.tar.xz
```
Finally, add toolchain to `PATH`:
<!--AUTOVERSION: "linaro-%"/ignore-->
```bash
PATH=$PATH:$(pwd)/gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf/bin
```

#### Install mender-artifact

`mender-convert` also depends on `mender-artifact`.
Please follow [the documentation on mender-artifact](../modifying-a-mender-artifact#mender-artifact) and install it.


### Download mender-convert

Clone `mender-convert` from the official repository:

```bash
git clone https://github.com/mendersoftware/mender-convert.git
```


## Convert a raw disk image

Change directory to where you downloaded `mender-convert`:

```bash
cd mender-convert
```

Then adjust to the correct paths below and run the conversion:

```bash
./mender-convert from-raw-disk-image                        \
            --raw-disk-image <PATH-TO-RAW-DISK-IMAGE>       \
            --mender-disk-image golden-image-1.sdimg        \
            --device-type <beaglebone | raspberrypi3>       \
            --mender-client <PATH-TO-MENDER-CLIENT-BINARY>  \
            --artifact-name golden-image-1                  \
            --bootloader-toolchain arm-linux-gnueabihf      \
            --demo-host-ip <IP-OF-DEMO-SERVER> --keep
```

!!! The conversion may take 10 minutes, depending on the resources available on your machine.

After a successful conversion, your images can be found in `outputs/`.

The above invocation will use configuration defaults for use with the [Mender demo environment](../../../getting-started/create-a-test-environment).


## Building for production

In a production environment, we should not use the ``--demo-host-ip` option, but rather one or more of the following:

```bash
--tenant-token <name of token for hosted.mender.io service>
--server-url <url to production server>
--server-cert <file path to the certificate>
```
