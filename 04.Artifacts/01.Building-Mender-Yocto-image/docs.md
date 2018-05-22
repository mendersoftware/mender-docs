---
title: Building a Mender Yocto Project image
taxonomy:
    category: docs
---

This document outlines the steps needed to build a [Yocto Project](https://www.yoctoproject.org/?target=_blank) image for a device.
The build output will most notably include:
* a file that can be flashed to the device storage during initial provisioning. It contains a `.uefiimg` suffix if UEFI partition layout is used (usually together with GRUB), and a `.sdimg` suffix if not (usually together with U-Boot).
* an Artifact containing rootfs filesystem image file that Mender can deploy to your provisioned device, it has suffix `.mender`

!!! If you do not want to build your own images for testing purposes, the [Getting started](../../getting-started) tutorials provide links to several [demo images](../../getting-started/download-test-images).

## What is *meta-mender*?

[meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank) is a set of layers that enable the creation of a Yocto Project image where the Mender client is part of the image. With Mender installed and configured on the image, you can deploy image updates and benefit from features like automatic roll-back, remote management, logging and reporting.

Inside *meta-mender* there are several layers. The most important one is *meta-mender-core*, which is required by all builds that use Mender. *meta-mender-core* takes care of:

* Cross-compiling Mender for ARM devices
* [Partitioning the image correctly](../../devices/partition-layout)
* [Setting up the U-Boot bootloader to support Mender](../../devices/integrating-with-u-boot)

Each one of these steps can be configured further, see the linked sections for more details.

The other layers in *meta-mender* provide support for specific boards.

!!! For general information about getting started with Yocto Project, it is recommended to read the [Yocto Project Quick Start guide](http://www.yoctoproject.org/docs/2.3/yocto-project-qs/yocto-project-qs.html?target=_blank).


## Prerequisites

### Device integrated with Mender

Before building for your device with Mender, Mender needs to
be integrated with your device (most notably with U-Boot). This
integration enables robust and atomic rollbacks with Mender.
The following reference devices are already integrated with Mender,
so if you are building for one of these you do not need to do any integration:

* [Raspberry Pi 3](https://github.com/mendersoftware/meta-mender/tree/rocko/meta-mender-raspberrypi?target=_blank) (other revisions are also likely to work)
* BeagleBone Black (no board specific layer needed)
* [Virtual device (vexpress-qemu)](https://github.com/mendersoftware/meta-mender/tree/rocko/meta-mender-qemu?target=_blank)

If you are building for a different device, please see [Device integration](../../devices)
for general requirements and adjustments you might need to enable your device
to support atomic image-based deployments with rollback.
There might already be similar devices you can use as a starting point in
the [meta-mender repository](https://github.com/mendersoftware/meta-mender?target=_blank).

If you want to save time, you can use our [professional services to integrate your device with Mender](https://mender.io/product/board-support?target=_blank).


### Correct clock on device

Make sure that the clock is set correctly on your devices. Otherwise certificate verification will become unreliable
and **the Mender client can likely not connect to the Mender server**.
See [certificate troubleshooting](../../troubleshooting/mender-client#certificate-expired-or-not-yet-valid) for more information.


### Yocto Project

! We use the **rocko** branch of the Yocto Project and `meta-mender` below. *Building meta-mender on other releases of the Yocto Project will likely not work seamlessly.* `meta-mender` also has other branches like [daisy](https://github.com/mendersoftware/meta-mender/tree/daisy?target=_blank) that correspond to Yocto Project releases, but these branches are no longer maintained by Mender developers. We offer professional services to to implement and support other branches over time, please take a look at the [Mender professional services offering](https://mender.io/product/professional-services?target=_blank).

A Yocto Project poky environment is required. If you already have 
this in your build environment, please open a terminal, go to the `poky`
directory and skip to [Adding the meta layers](#adding-the-meta-layers).


On the other hand, if you want to start from a *clean Yocto Project environment*,
you need to clone the latest poky and go into the directory:

```bash
git clone -b rocko git://git.yoctoproject.org/poky
```

```bash
cd poky
```

!!! Note that the Yocto Project also depends on some [development tools to be in place](http://www.yoctoproject.org/docs/2.3/yocto-project-qs/yocto-project-qs.html?target=_blank#packages).



## Adding the meta layers

We will now add the required meta layers to our build environment.
Please make sure you are standing in the directory where `poky` resides,
i.e. the top level of the Yocto Project build tree, and run these commands:

```bash
git clone -b rocko git://github.com/mendersoftware/meta-mender
```

Next, we initialize the build environment:

```bash
source oe-init-build-env
```

This creates a build directory with the default name, `build`, and makes it the
current working directory.

We then need to add the Mender layers into our project:

```bash
bitbake-layers add-layer ../meta-mender/meta-mender-core
```

! The `meta-mender-demo` layer (below) is not appropriate if you are building for production devices. Please go to the section about [building for production](../building-for-production) to see the difference between demo builds and production builds.

```bash
bitbake-layers add-layer ../meta-mender/meta-mender-demo
```

Finally, add the **Mender layer specific to your board**.
Mender currently comes with three reference devices
that you can build for (only add one of these):

* Raspberry Pi 3 (other revisions might also work): `bitbake-layers add-layer ../meta-mender/meta-mender-raspberrypi` (depends on `meta-raspberrypi`)
* BeagleBone Black: No board specific layer needed
* Virtual device: `bitbake-layers add-layer ../meta-mender/meta-mender-qemu`

Other devices may have community support,
either in [meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank) or other repositories.
If you are building for a different device, please see [Device integration](../../devices)
for general requirements and adjustments you might need to enable your device
to support Mender.

At this point, all the layers required for Mender should be
part of your Yocto Project build environment.


## Configuring the build

!!! The configuration in `conf/local.conf` below will create a build that runs the Mender client in managed mode, as a `systemd` service. It is also possible to [run Mender standalone from the command-line or a custom script](../../architecture/overview#modes-of-operation). See the [section on customizations](../image-configuration#disabling-mender-as-a-system-service) for steps to disable the `systemd` integration.

Add these lines to the start of your `conf/local.conf`:

```bash
# The name of the disk image and Artifact that will be built.
# This is what the device will report that it is running, and different updates must have different names
# because Mender will skip installation of an Artifact if it is already installed.
MENDER_ARTIFACT_NAME = "release-1"

INHERIT += "mender-full"

# A MACHINE integrated with Mender.
# raspberrypi3, beaglebone, and vexpress-qemu are reference devices
MACHINE = "<YOUR-MACHINE>"

# For Raspberry Pi, uncomment the following block:
# RPI_USE_U_BOOT = "1"
# MENDER_PARTITION_ALIGNMENT_KB = "4096"
# MENDER_BOOT_PART_SIZE_MB = "40"
# IMAGE_INSTALL_append = " kernel-image kernel-devicetree"
# IMAGE_FSTYPES_remove += " rpi-sdimg"
#
# Lines below not needed for Yocto Rocko (2.4) or newer.
# IMAGE_BOOT_FILES_append = " boot.scr u-boot.bin;${SDIMG_KERNELIMAGE}"
# KERNEL_IMAGETYPE = "uImage"

# The version of Mender to build. This needs to match an existing recipe in the meta-mender repository.
#
# Given your Yocto Project version, see which versions of Mender you can currently build here:
# https://docs.mender.io/architecture/compatibility#mender-client-and-yocto-project-version
#
# Given a Mender client version, see the corresponding version of the mender-artifact utility:
# https://docs.mender.io/architecture/compatibility#mender-client-and-artifact-format
#
# Note that by default this will select the latest released version of the tools.
# If you need an earlier version, please uncomment the following and set to the
# required version.
#
# PREFERRED_VERSION_pn-mender = "1.1.%"
# PREFERRED_VERSION_pn-mender-artifact = "2.0.%"
# PREFERRED_VERSION_pn-mender-artifact-native = "2.0.%"

# Build for Hosted Mender
# To get your tenant token, log in to https://hosted.mender.io,
# click your email at the top right and then "My organization".
# Remember to remove the meta-mender-demo layer (if you have added it).
# We recommend Mender 1.4.0 and Yocto Project's rocko or later for Hosted Mender.
#
# MENDER_SERVER_URL = "https://hosted.mender.io"
# MENDER_TENANT_TOKEN = "<YOUR-HOSTED-MENDER-TENANT-TOKEN>"

DISTRO_FEATURES_append = " systemd"
VIRTUAL-RUNTIME_init_manager = "systemd"
DISTRO_FEATURES_BACKFILL_CONSIDERED = "sysvinit"
VIRTUAL-RUNTIME_initscripts = ""

IMAGE_FSTYPES = "ext4"
```

!!! The size of the disk image (`.sdimg`) should match the total size of your storage so you do not leave unused space; see [the variable MENDER_STORAGE_TOTAL_SIZE_MB](../variables#mender_storage_total_size_mb) for more information. Mender automatically selects the file system types it builds into the disk image, which is used for initial flash provisioning, based on the `IMAGE_FSTYPES` variable. See the [section on file system types](../../devices/partition-layout#file-system-types) for more information.

!!! If you are building for **Hosted Mender**, make sure to set `MENDER_SERVER_URL` and `MENDER_TENANT_TOKEN` (see the comments above).

!!! If you would like to use a read-only root file system, please see the section on [configuring the image for read-only rootfs](../image-configuration#configuring-the-image-for-read-only-rootfs).



## Building the image

Once all the configuration steps are done, build an image with bitbake:

```bash
bitbake <YOUR-TARGET>
```

Replace `<YOUR-TARGET>` with the desired target or image name, e.g. `core-image-full-cmdline`.

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
or by using the Mender client only in [Standalone deployments](../../architecture/standalone-deployments).

!!! If you built for the virtual Mender reference device (`vexpress-qemu`), you can start up your newly built image with the script in `../meta-mender/meta-mender-qemu/scripts/mender-qemu` and log in as *root* without password.
