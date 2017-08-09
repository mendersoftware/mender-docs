---
title: Building a Mender Yocto Project image
taxonomy:
    category: docs
---

This document outlines the steps needed to build a [Yocto Project](https://www.yoctoproject.org/?target=_blank) image for a device.
The build output will most notably include:
* a file that can be flashed to the device storage during initial provisioning, it has suffix `.sdimg`
* an Artifact containing rootfs filesystem image file that Mender can deploy to your provisioned device, it has suffix `.mender`

Mender has two [reference devices](../../getting-started/what-is-mender#mender-reference-devices): a virtual QEMU device for testing without the need for hardware, and the BeagleBone Black.
Building for these devices is well tested with Mender. If you are building for your own device
please see [Device integration](../../devices) for general requirements and adjustments you might need
to enable your device to support atomic image-based deployments with rollback.

!!! If you do not want to build your own images for testing purposes, the [Getting started](../../getting-started) tutorials provide links to several demo images, both for QEMU and BeagleBone Black.

## What is *meta-mender*?

[meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank) is a set of layers that enable the creation of a Yocto Project image where the Mender client is part of the image. With Mender installed and configured on the image, you can deploy image updates and benefit from features like automatic roll-back, remote management, logging and reporting. The *meta-mender* layers contain all the recipes required to build the Mender Go binary and configure the Yocto Project image.

Inside *meta-mender* there are several layers. The most important one is *meta-mender-core*, which is required by all builds that use Mender. *meta-mender-core* takes care of:

* Cross-compiling Mender for ARM devices
* [Partitioning the image correctly](../../devices/partition-layout)
* [Setting up the U-Boot bootloader to support Mender](../../devices/integrating-with-u-boot)

Each one of these steps can be configured further, see the linked sections for more details.

The other layers in *meta-mender* provide support for specific boards.

!!! For general information about getting started with Yocto Project, it is recommended to read the [Yocto Project Quick Start guide](http://www.yoctoproject.org/docs/2.2/yocto-project-qs/yocto-project-qs.html?target=_blank).


## Prerequisites

! We use the Yocto Project's **master** branch below. *Building meta-mender on other releases of the Yocto Project will likely not work seamlessly.* We use the `master` branch in `meta-mender`, which builds a latest release of Mender for the bleeding edge Yocto Project revision. `meta-mender` also has other branches like [daisy](https://github.com/mendersoftware/meta-mender/tree/daisy?target=_blank) that correspond to Yocto Project releases , but these branches are no longer maintained by Mender developers. Please reach out on the [Mender community mailing list](https://groups.google.com/a/lists.mender.io/forum?target=_blank#!forum/mender) if you would like help with getting Mender to work on other versions of the Yocto Project.

!!! The meta-mender-demo layer, which is used below, and the webserver, are bundled with a default demo certificate and key. If you are intending on using Mender in production, you must generate your own certificate using OpenSSL. Please see the certificate section [for the server](../../administration/certificates-and-keys) and [for the client](../building-for-production/#certificates) for more information.

The required meta layers are found in the following repositories:

```
URI: git://git.yoctoproject.org/poky
branch: master

URI: git://github.com/mendersoftware/meta-mender
branch: master
```

A Yocto Project poky environment is required. If you already have 
this in your build environment, please open a terminal, go to the `poky`
directory and skip to [Adding the meta layers](#adding-the-meta-layers).


On the other hand, if you want to start from a *clean Yocto Project environment*,
you need to clone the latest poky and go into the directory:

```bash
git clone -b master git://git.yoctoproject.org/poky
```

```bash
cd poky
```

!!! Note that the Yocto Project also depends on some [development tools to be in place](http://www.yoctoproject.org/docs/2.2/yocto-project-qs/yocto-project-qs.html?target=_blank#packages).

! Please make sure that the clock is set correctly on your devices. Otherwise certificate verification will become unreliable. See [certificate troubleshooting](../../troubleshooting/mender-client#certificate-expired-or-not-yet-valid) for more information.

## Adding the meta layers

We will now add the required meta layers to our build environment.
Please make sure you are standing in the directory where `poky` resides,
i.e. the top level of the Yocto Project build tree, and run these commands:

```bash
git clone -b master git://github.com/mendersoftware/meta-mender
```

Next, we initialize the build environment:

```bash
source oe-init-build-env
```

This creates a build directory with the default name, `build`, and makes it the
current working directory.

We then need to incorporate the two layers, meta-mender-core and
meta-mender-demo, into our project:

```bash
bitbake-layers add-layer ../meta-mender/meta-mender-core
bitbake-layers add-layer ../meta-mender/meta-mender-demo
```

! The `meta-mender-demo` layer is not appropriate if you are building for production devices. Please go to the section about [building for production](../building-for-production) to see the difference between demo builds and production builds.

Finally, you need to incorporate the layer specific to your board. Mender currently comes with two supported boards: vexpress-qemu and beaglebone, residing in `meta-mender/meta-mender-qemu` and `meta-mender/meta-mender-beaglebone`, respectively. Other boards may also exist that are contributed by the community, or you may need to create a board specific layer yourself for your particular hardware.

If you wish to test using the QEMU emulator, run the following:

```bash
bitbake-layers add-layer ../meta-mender/meta-mender-qemu
```

At this point, all the layers required for Mender should be
part of your Yocto Project build environment.


## Configuring the build

!!! The configuration in `local.conf` below will create a build that runs the Mender client in managed mode, as a `systemd` service. It is also possible to [run Mender standalone from the command-line or a custom script](../../architecture/overview#modes-of-operation). See the [section on customizations](../image-configuration#disabling-mender-as-a-system-service) for steps to disable the `systemd` integration.

Add these lines to the start of your `local.conf`:

```bash
MENDER_ARTIFACT_NAME = "release-1"

INHERIT += "mender-full"

MACHINE = "<YOUR-MACHINE>"

DISTRO_FEATURES_append = " systemd"
VIRTUAL-RUNTIME_init_manager = "systemd"
DISTRO_FEATURES_BACKFILL_CONSIDERED = "sysvinit"
VIRTUAL-RUNTIME_initscripts = ""

IMAGE_FSTYPES = "ext4"
```

`MENDER_ARTIFACT_NAME` is name of the image or update that will be built. This is what the device will report that it is running, and different updates must have different names because Mender will skip installation of an artifact if it is already installed.

Please replace `<YOUR-MACHINE>` with the correct machine for your device.

! The machine `<YOUR-MACHINE>` needs to be integrated with Mender before it will work correctly; most notably U-Boot needs the required features and integration. Please see [Device integration](../../devices) for more information. If you are building for a Mender [reference device](../../getting-started/what-is-mender#mender-reference-devices), you can use `vexpress-qemu` or `beaglebone`. 

!!! The size of the disk image (`.sdimg`) should match the total size of your storage so you do not leave unused space; see [the variable MENDER_STORAGE_TOTAL_SIZE_MB](../variables#mender_storage_total_size_mb) for more information. Mender automatically selects the file system types it builds into the disk image, which is used for initial flash provisioning, based on the `IMAGE_FSTYPES` variable. See the [section on file system types](../../devices/partition-layout#file-system-types) for more information.

!!! It is suggested to add `INHERIT += "rm_work"` to `local.conf` in order to conserve disk space during the build.


## Building the image

Once all the configuration steps are done, an image can be built with bitbake:

```bash
bitbake <YOUR-TARGET>
```

!!! Please replace `<YOUR-TARGET>` with the desired target or image name. If you are building for `vexpress-qemu`, set the target to `core-image-full-cmdline`. If you are building for the `beaglebone`, set the target to `core-image-base`. For more information about the differences with image types on the BeagleBone Black please see [the official Yocto Project BeagleBone support page](https://www.yoctoproject.org/downloads/bsps/morty22/beaglebone?target=_blank).

!!! The first time you build a Yocto Project image, the build process can take several hours. The successive builds will only take a few minutes, so please be patient this first time.


## Using the build output

After a successful build, the images and build artifacts are placed in `tmp/deploy/images/<YOUR-MACHINE>/`.

The files with suffix `.sdimg` are used to provision the device storage for devices without
Mender running already. Please proceed to [Provisioning a new device](../provisioning-a-new-device)
for steps to do this.

On the other hand, if you already have Mender running on your device and want to deploy a rootfs update
using this build, you should use the [Mender Artifact](../../architecture/mender-artifacts) files,
which have `.mender` suffix. You can either deploy this Artifact in managed mode with
the Mender server as described in [Deploy to physical devices](../../getting-started/deploy-to-physical-devices)
or by using the Mender client only in [Standalone deployments](../../getting-started/standalone-deployments).

!!! If you built for the Mender reference device `vexpress-qemu`, you can start up your newly built image with the script in `../meta-mender/meta-mender-qemu/scripts/mender-qemu` and log in as *root* without password.
