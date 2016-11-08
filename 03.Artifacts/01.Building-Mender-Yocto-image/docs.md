---
title: Building a Mender Yocto Project image
taxonomy:
    category: docs
---

This document outlines the steps needed to build a [Yocto Project](https://www.yoctoproject.org/?target=_blank) image for a device.
The build output will most notably include:
* a file that can be flashed to the device storage during initial provisioning, it has suffix `.sdimg`
* a rootfs filesystem image file that Mender can deploy to your provisioned device, it normally has suffix `.ext4`, but this depends on the file system type you build

Mender uses a virtual QEMU device for testing without the need for hardware, and the BeagleBone Black as the reference hardware platform.
Building for these devices is well tested with Mender. If you are building for your own device
please see [Device integration](../../Devices) for general requirements and adjustments you might need
to enable your device to support atomic image-based deployments with rollback.

!!! If you do not want to build your own images for testing purposes, the [Getting started](../../Getting-started) tutorials provide links to several demo images, both for QEMU and BeagleBone Black.

## What is *meta-mender*?

[meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank) is a layer that enables the creation of a Yocto Project image where the Mender client is part of the image. With Mender installed and configured on the image, you can deploy image updates and benefit from features like automatic roll-back, remote management, logging and reporting. The *meta-mender* layer contains all the recipes required to build the Mender Go binary and configure the Yocto Project image.

The *meta-mender* layer takes care of:

* Cross-compiling Mender for ARM devices using Go 1.6.
* [Partitioning the image correctly](../../Devices/Partition-layout).
* [Setting up the U-Boot bootloader to support Mender](../../Devices/Integrating-with-U-Boot).

Each one of these steps can be configured further, see the linked sections for more details.

Detailed instructions and recipes needed for building a self-contained image follow.

!!! For general information about getting started with Yocto Project, it is recommended to read the [Yocto Project Quick Start guide](http://www.yoctoproject.org/docs/2.1/yocto-project-qs/yocto-project-qs.html?target=_blank).

## Prerequisites

! We use the Yocto Project's **krogoth** branch below. *Building meta-mender on other releases of the Yocto Project will likely not work seamlessly.* `meta-mender` has other branches like [daisy](https://github.com/mendersoftware/meta-mender/tree/daisy?target=_blank), but these branches are no longer maintained by Mender developers. Please reach out on the [Mender community mailing list](https://groups.google.com/a/lists.mender.io/forum?target=_blank#!forum/mender) if you would like help with getting Mender to work on other versions of the Yocto Project.


!!! The meta-mender layer and the web-server are bundled with a default certificate and key. If you are intending on using Mender in production, it is highly recommend to generate your own certificate using OpenSSL (`openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256`), and replacing the [server certificate](https://github.com/mendersoftware/meta-mender/tree/master/recipes-mender/mender/files) found in the meta-mender layer, and [server certificate and key](https://github.com/mendersoftware/mender-api-gateway-docker/tree/master/cert) in the nginx gateway.

The required meta layers are found in the following repositories:

```
URI: git://git.yoctoproject.org/poky
branch: krogoth

URI: git://github.com/mendersoftware/meta-mender
branch: krogoth

URI: git://github.com/mem/oe-meta-go
branch: master
```

A Yocto Project poky environment is required. If you already have 
this in your build environment, please open a terminal, go to the `poky`
directory and skip to [Adding the meta layers](#adding-the-meta-layers).


On the other hand, if you want to start from a clean environment,
you need to clone the latest poky and go into the directory:

```
git clone -b krogoth git://git.yoctoproject.org/poky
```

```
cd poky
```

## Adding the meta layers

We will now add the required meta layers to our build environment.
Please make sure you are standing in the directory where `poky` resides,
i.e. the top level of the Yocto Project build tree, and run these commands:

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

We then need to incorporate the two layers, meta-mender and oe-meta-go, into
our project:

```
bitbake-layers add-layer ../meta-mender
```
```
bitbake-layers add-layer ../oe-meta-go
```

At this point, all the layers required for Mender should be
part of your Yocto Project build environment.


## Configuring the build

!!! The configuration in `conf/local.conf` below will create a build that runs the Mender client in managed mode, as a `systemd` service. It is also possible to [run Mender standalone from the command-line or a custom script](../../Architecture/overview#modes-of-operation). See the [section on customizations](../Build-customizations#disabling-mender-as-a-system-service) for steps to disable the `systemd` integration.

Add these lines to the start of your `conf/local.conf`:

```
INHERIT += "mender-full"
MACHINE = "<YOUR-MACHINE>"
DISTRO_FEATURES_append = " systemd"
VIRTUAL-RUNTIME_init_manager = "systemd"
DISTRO_FEATURES_BACKFILL_CONSIDERED = "sysvinit"
VIRTUAL-RUNTIME_initscripts = ""
IMAGE_FSTYPES = "ext4"
```

Please replace `<YOUR-MACHINE>` with the correct machine for your device.

! The machine `<YOUR-MACHINE>` needs to be integrated with Mender before it will work correctly; most notably U-Boot needs the required features and integration. Please see [Device integration](../../Devices) for more information. If you are building for a Mender reference platform, you can use `vexpress-qemu` or `beaglebone`. 

!!! Mender automatically selects the file system types it builds into the disk image (`.sdimg`), which is used for initial flash provisioning, based on the `IMAGE_FSTYPES` variable. See the [section on file system types](../../Devices/Partition-layout#file-system-types) for more information.

!!! It is suggested to add ```INHERIT += "rm_work"``` to ```conf/local.conf``` in order to conserve disk space during the build.


## Building the image

Once all the configuration steps are done, an image can be built with bitbake:

```
bitbake <YOUR-TARGET>
```

!!! Please replace `<YOUR-TARGET>` with the desired target or image name. If you are building for a vexpress-qemu, set the target to `core-image-full-cmdline`. If you are building for the `beaglebone`, set the target to `core-image-base`. For more information about the differences with image types on the BeagleBone Black please see [the official Yocto Project BeagleBone support page](https://www.yoctoproject.org/downloads/bsps/krogoth21/beaglebone?target=_blank).

!!! The first time you build a Yocto Project image, the build process can take several hours. The successive builds will only take a few minutes, so please be patient this first time.


## Using the build output

After a successful build, the images and build artifacts are placed in `tmp/deploy/images/<YOUR-MACHINE>/`
(as set in `conf/local.conf`).

The files with suffix `.sdimg` are used to provision the device storage for devices without
Mender running already. Please proceed to [Provisioning a new device](../Provisioning-a-new-device)
for steps to do this.

On the other hand, if you already have Mender running on your device and want to deploy a rootfs update
using this build, you should use files with the suffix of your selected filesystem
(as set in `IMAGE_FSTYPES`), for example `.ext4`. You can either deploy this rootfs
image in managed mode with the Mender server as described in [Deploy to physical devices](../../Getting-started/Deploy-to-physical-devices)
or by using the Mender client only in [Standalone deployments](../../Getting-started/Standalone-deployments).

!!! If you built for the Mender reference platform `vexpress-qemu`, you can start up your newly built image with the script in `../meta-mender/scripts/mender-qemu` and log in as *root* without password.
