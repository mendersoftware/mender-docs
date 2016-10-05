---
title: Building a Mender Yocto Project image
taxonomy:
    category: docs
---

This document outlines the steps needed to build a [Yocto Project](https://www.yoctoproject.org/?target=_blank) image containing a testable version of the Mender client for both QEMU and BeagleBone Black.

!!! If you do not want to build your own images for testing purposes, the [Getting started](../../Getting-started) tutorials provide links to several demo images, both for QEMU and BeagleBone Black.

## What is *meta-mender*?

[meta-mender](https://github.com/mendersoftware/meta-mender) is a layer that enables the creation of a Yocto Project image where the Mender client is part of the image. With Mender installed and configured on the image, you can deploy image updates and benefit from features like automatic roll-back, remote management, logging and reporting. The *meta-mender* layer contains all the recipes required to build the Mender Go binary and configure the Yocto Project image.

The *meta-mender* layer takes care of:

* Cross-compiling Mender for ARM devices using Go 1.6.
* [Partitioning the image correctly](../../Devices/Partition-layout).
* [Setting up the U-Boot bootloader to support Mender](../../Devices/Integrating-with-U-Boot).

Each one of these steps can be configured further, see the linked sections for more details.

Detailed instructions and recipes needed for building a self-contained image follow.

!!! For general information about getting started with Yocto Project, it is recommended to read the [Yocto Project Quick Start guide](http://www.yoctoproject.org/docs/2.1/yocto-project-qs/yocto-project-qs.html).

##Dependencies

! We use the Yocto Project's **krogoth** branch below. *Building meta-mender on other releases of the Yocto Project will likely not work seamlessly.* `meta-mender` has other branches like [daisy](https://github.com/mendersoftware/meta-mender/tree/daisy), but these branches are no longer maintained by Mender developers.

The *meta-mender* layer depends on the following repositories:

```
URI: git://git.yoctoproject.org/poky
branch: krogoth

URI: git://github.com/mendersoftware/meta-mender
branch: krogoth

URI: git://github.com/mem/oe-meta-go
branch: master
```

## Pre-configuration

First, we need to clone the latest Yocto Project source:

```
git clone -b krogoth git://git.yoctoproject.org/poky
```

Having done that, we can clone the meta-mender and oe-meta-go layers into the top level
of the Yocto Project build tree (in directory poky):

```
cd poky
```
```
git clone -b krogoth git://github.com/mendersoftware/meta-mender
```
```
git clone git://github.com/mem/oe-meta-go
```


Next, we initialize the build environment:

```
source oe-init-build-env
```

This creates a build directory with the default name, ```build```, and makes it the
current working directory.


## Yocto Project configuration

We need to incorporate the two layers, meta-mender and oe-meta-go, into
our project:

```
bitbake-layers add-layer ../meta-mender
```
```
bitbake-layers add-layer ../oe-meta-go
```

!!! The configuration in `conf/local.conf` below will create a build that runs the Mender client in managed mode, as a `systemd` service. It is also possible to [run Mender standalone from the command-line or a custom script](../../Architecture/overview#modes-of-operation). See the [section on customizations](../Customizations#disabling-mender-as-a-system-service) for steps to disable the `systemd` integration.

We can generate a mender test build for one of two machines: a target emulated
by QEMU or a BeagelBone Black.

For QEMU, add these lines to the start of ```conf/local.conf```:

```
INHERIT += "mender-full"
MACHINE = "vexpress-qemu"
DISTRO_FEATURES_append = " systemd"
VIRTUAL-RUNTIME_init_manager = "systemd"
DISTRO_FEATURES_BACKFILL_CONSIDERED = "sysvinit"
VIRTUAL-RUNTIME_initscripts = ""
```

For the BeagleBone Black, add these lines:

```
INHERIT += "mender-full"
MACHINE = "beaglebone"
DISTRO_FEATURES_append = " systemd"
VIRTUAL-RUNTIME_init_manager = "systemd"
DISTRO_FEATURES_BACKFILL_CONSIDERED = "sysvinit"
VIRTUAL-RUNTIME_initscripts = ""
```

! Note that Mender automatically selects the file system types it builds based on the `IMAGE_FSTYPES` variable. See the [section on file system types](../../Devices/Partition-layout#file-system-types) for more information.

!!! It is suggested to also add ```INHERIT += "rm_work"``` to ```conf/local.conf``` in order to conserve disk space during the build.

## Building the image

### For QEMU

Once all the configuration steps are done, the image can be built like this:

```
bitbake core-image-full-cmdline
```

This will build the `core-image-full-cmdline` image type, but it is also possible to
build other image types.

!!! The first time you build a Yocto Project image, the build process can take several hours. The successive builds will only take a few minutes, so please be patient this first time. 

After a successful build, the images and build artifacts are placed in `tmp/deploy/images/vexpress-qemu/`. There is a helper script that starts up our newly built image which can be run with:

```
../meta-mender/scripts/mender-qemu
```

You can log in as *root* without password. To test how to deploy a rootfs update in QEMU, please read [Getting started - Your first update on QEMU](../../Getting-started/Your-first-update-on-qemu#serve-a-rootfs-image-for-the-qemu-machine). Optionally, if you want to modify the rootfs image prior to deploying it, see [Modifying a rootfs image](../Modifying-a-rootfs-image).

### For BeagleBone Black

In order to build an image that can be run on BeagleBone Black, the following
command should be used:

```
bitbake core-image-base
```

The reason the ```core-image-base``` image is built is the simplicity of the booting
and testing process. With the base image, all needed boot and configuration files
are created by Yocto Project and copied to appropriate locations in the boot partition
and the root file system. For more information the about differences with
image types on the BeagleBone Black please see [the official Yocto Project BeagleBone support
page](https://www.yoctoproject.org/downloads/bsps/krogoth21/beaglebone).

Like for QEMU, please be aware that your first Yocto Project build can take several hours.

After a successful build, the images and build artifacts are placed in `tmp/deploy/images/beaglebone/`. To write your new image to the SD card and test how to deploy a rootfs update on BeagleBone Black, please read [Getting started - Your first update on BeagleBone Black](../../Getting-started/Your-first-update-on-BeagleBone#write-the-disk-image-to-the-sd-card). Optionally, if you want to modify the rootfs image prior to deploying it, see [Modifying a rootfs image](../Modifying-a-rootfs-image).
