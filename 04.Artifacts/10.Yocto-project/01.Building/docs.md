---
title: Building a Mender Yocto Project image
taxonomy:
    category: docs
---

This document outlines the steps needed to build a [Yocto Project](https://www.yoctoproject.org/?target=_blank) image for a device.
The build output will most notably include:
* a disk image that can be flashed to the device storage during initial provisioning
* an Artifact containing rootfs filesystem image file that Mender can deploy to your provisioned device, it has suffix `.mender`

!!! If you do not want to build your own images for testing purposes, the [Get started](../../../01.Get-started/chapter.md) tutorials provide links to several [prebuilt images](../../../08.Downloads/docs.md#disk-images).

## What is *meta-mender*?

[meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank) is a set of layers that enable the creation of a Yocto Project image where the Mender client is part of the image. With Mender installed and configured on the image, you can deploy image updates and benefit from features like automatic roll-back, remote management, logging and reporting.

Inside *meta-mender* there are several layers. The most important one is *meta-mender-core*, which is required by all builds that use Mender. *meta-mender-core* takes care of:

* Cross-compiling Mender for ARM devices
* [Partitioning the image correctly](../../../03.Devices/02.Yocto-project/01.Partition-configuration/docs.md)
* [Setting up the U-Boot bootloader to support Mender](../../../03.Devices/02.Yocto-project/02.Bootloader-support/02.U-Boot/docs.md)

Each one of these steps can be configured further, see the linked sections for more details.

The other layers in *meta-mender* provide support for specific boards used in Mender testing.

## What is *meta-mender-community*?

[meta-mender-community](https://github.com/mendersoftware/meta-mender-community?target=_blank) is a set of layers containing board-specific settings for Mender integration.

!!! For general information about getting started with Yocto Project, it is recommended to read the [Yocto Project Quick Start tutorial](http://www.yoctoproject.org/docs/2.4/yocto-project-qs/yocto-project-qs.html?target=_blank).


## Prerequisites

### Board integrated with Mender

Mender needs to integrate with your board, most notably with the boot process.
Although the integration is automated for most boards, please see
[Board integration](../../../03.Devices/chapter.md) for general requirements and
adjustment you might need to make before building.

Check out the board integrations at [Mender Hub](https://hub.mender.io?target=_blank) to see if your board is
already integrated.
If you encounter any issues and want to save time, you can use
the [Mender Consulting services to integrate your board](https://mender.io/support-and-services/board-integration?target=_blank).


### Correct clock on device

Make sure that the clock is set correctly on your devices. Otherwise certificate verification will become unreliable
and **the Mender client can likely not connect to the Mender server**.
See [certificate troubleshooting](../../../201.Troubleshooting/03.Mender-Client/docs.md#certificate-expired-or-not-yet-valid) for more information.


## Yocto Project

### Starting from scratch

Full details for building the Yocto project for your board are available at Mender Hub. The tested reference platforms for Mender are available at the following:
* [Raspberry Pi 3 Model B/B+](https://hub.mender.io/t/raspberry-pi-3-model-b-b/57)
* [Raspberry Pi 4 Model B](https://hub.mender.io/t/raspberry-pi-4-model-b/889)
* [BeagleBone Black](https://hub.mender.io/t/beaglebone-black/83)
* [QEMU](https://hub.mender.io/t/qemu-the-fast-processor-emulator/420)

!!! Note that the Yocto Project also depends on some [development tools to be in place](http://www.yoctoproject.org/docs/2.4/yocto-project-qs/yocto-project-qs.html?target=_blank#packages).

! The `meta-mender-demo` layer, which is included in the integrations available at [Mender Hub](https://hub.mender.io?target=_blank), is not appropriate if you are building for production devices. Please go to the section about [building for production](../03.Building-for-production/docs.md) to see the difference between demo builds and production builds.

If you encounter any issues, please see [Board integration](../../../03.Devices/chapter.md)
for general requirements and adjustments you might need to enable your board to
support Mender.

#### Configuring the build

!!! The configuration from [Mender Hub](https://hub.mender.io?target=_blank) will create a build that runs the Mender client in managed mode, as a `systemd` service. It is also possible to [run Mender standalone from the command-line or a custom script](../../../02.Overview/01.Introduction/docs.md#client-modes-of-operation). See the [section on customizations](../02.Image-configuration/docs.md#disabling-mender-as-a-system-service) for steps to disable the `systemd` integration.

The following settings will be present in the default `conf/local.conf` after running the steps from [Mender Hub](https://hub.mender.io?target=_blank). These are likely to need customization for your setup.

<!--AUTOVERSION: "Mender %"/mender "releases % and older"/ignore "PREFERRED_VERSION_pn-mender = \"%\""/mender "PREFERRED_VERSION_pn-mender-artifact = \"%\""/mender-artifact "PREFERRED_VERSION_pn-mender-artifact-native = \"%\""/mender-artifact-->
```bash
# The name of the disk image and Artifact that will be built.
# This is what the device will report that it is running, and different updates must have different names
# because Mender will skip installation of an Artifact if it is already installed.
MENDER_ARTIFACT_NAME = "release-1"

# The version of Mender to build. This needs to match an existing recipe in the meta-mender repository.
#
# Given your Yocto Project version, see which versions of Mender you can currently build here:
# https://docs.mender.io/overview/compatibility#mender-client-and-yocto-project-version
#
# Given a Mender client version, see the corresponding version of the mender-artifact utility:
# https://docs.mender.io/overview/compatibility#mender-clientserver-and-artifact-format
#
# Note that by default this will select the latest released version of the tools.
# If you need an earlier version, please uncomment the following and set to the
# required version.
#
# PREFERRED_VERSION_pn-mender = "2.1.2"
# PREFERRED_VERSION_pn-mender-artifact = "3.2.1"
# PREFERRED_VERSION_pn-mender-artifact-native = "3.2.1"

ARTIFACTIMG_FSTYPE = "ext4"

# Build for hosted Mender
#
# To get your tenant token:
#    - log in to https://hosted.mender.io
#    - click your email at the top right and then "My organization"
#    - press the "COPY TO CLIPBOARD"
#    - assign content of clipboard to MENDER_TENANT_TOKEN
#
#MENDER_SERVER_URL = "https://hosted.mender.io"
#MENDER_TENANT_TOKEN = ""

# Build for Mender demo server
#
# https://docs.mender.io/administration/demo-installation
#
# Uncomment below and update IP address to match the machine running the
# Mender demo server
#MENDER_DEMO_HOST_IP_ADDRESS = "192.168.0.100"

# Build for Mender production setup (on-prem)
#
# https://docs.mender.io/administration/production-installation
#
# Uncomment below and update the URL to match your configured domain
# name and provide the path to the generated server.crt file.
#
# Note that a custom server.crt file is only necessary if you are using
# self-signed certificates.
#
# NOTE! It is recommend that you provide below information in your custom
# Yocto layer and this is only for demo purposes. See linked documentation
# for additional information.
#MENDER_SERVER_URL = "https://docker.mender.io"
#FILESEXTRAPATHS_prepend_pn-mender := "<DIRECTORY-CONTAINING-server.crt>:"
#SRC_URI_append_pn-mender = " file://server.crt"
```

!!! The size of the disk image (`.sdimg`) should match the total size of your storage so you do not leave unused space; see [the variable MENDER_STORAGE_TOTAL_SIZE_MB](../99.Variables/docs.md#mender_storage_total_size_mb) for more information. Mender selects the file system type it builds into the disk image, which is used for initial flash provisioning, based on the `ARTIFACTIMG_FSTYPE` variable. See the [section on file system types](../../../03.Devices/02.Yocto-project/01.Partition-configuration/docs.md#file-system-types) for more information.

!!! If you are building for **[hosted Mender](https://hosted.mender.io?target=_blank)**, make sure to set `MENDER_SERVER_URL` and `MENDER_TENANT_TOKEN` (see the comments above).

!!! If you would like to use a read-only root file system, please see the section on [configuring the image for read-only rootfs](../../10.Yocto-project/02.Image-configuration/docs.md#configuring-the-image-for-read-only-rootfs).

### Adding meta-mender to existing Yocto Project environment

If you have an existing Yocto Project environment and want to add Mender to that, you will need to add the required meta layers to your build environment. The instructions
here are the basic steps needed to do this however your actual setup may require different mechanisms such as the [Google repo tool](https://gerrit.googlesource.com/git-repo/).

Please make sure you are standing in the directory where `poky` resides,
i.e. the top level of the Yocto Project build tree, and run these commands:

<!--AUTOVERSION: "-b % git://github.com/mendersoftware/meta-mender"/meta-mender-->
```bash
git clone -b master git://github.com/mendersoftware/meta-mender
```

<!--AUTOVERSION: "the HEAD of the % branch"/meta-mender-->
Note that this command checks out the HEAD of the master branch and is not a specific tagged release. The [Yocto project release schedule](https://wiki.yoctoproject.org/wiki/Releases) differs from the Mender release schedule so even though you may be using a specific release of Mender, you will still need to take further steps if you want to use a tagged release of the Yocto project.

Next, initialize the build environment:

```bash
source oe-init-build-env
```

This creates a build directory with the default name, `build`, and makes it the
current working directory.

Then, add the Mender layers into your project:

```bash
bitbake-layers add-layer ../meta-mender/meta-mender-core
```

! The `meta-mender-demo` layer (below) is not appropriate if you are building for production devices. Please go to the section about [building for production](../03.Building-for-production/docs.md) to see the difference between demo builds and production builds.

```bash
bitbake-layers add-layer ../meta-mender/meta-mender-demo
```

#### Configuring the build

!!! The configuration in `conf/local.conf` below will create a build that runs the Mender client in managed mode, as a `systemd` service. It is also possible to [run Mender standalone from the command-line or a custom script](../../../02.Overview/01.Introduction/docs.md#client-modes-of-operation). See the [section on customizations](../02.Image-configuration/docs.md#disabling-mender-as-a-system-service) for steps to disable the `systemd` integration.

Add these lines to the start of your `conf/local.conf`:

<!--AUTOVERSION: "Mender %"/mender "releases % and older"/ignore "PREFERRED_VERSION_pn-mender = \"%\""/mender "PREFERRED_VERSION_pn-mender-artifact = \"%\""/mender-artifact "PREFERRED_VERSION_pn-mender-artifact-native = \"%\""/mender-artifact-->
```bash
# The name of the disk image and Artifact that will be built.
# This is what the device will report that it is running, and different updates must have different names
# because Mender will skip installation of an Artifact if it is already installed.
MENDER_ARTIFACT_NAME = "release-1"

INHERIT += "mender-full"

# A MACHINE integrated with Mender.
# raspberrypi3, raspberrypi4, beaglebone-yocto, vexpress-qemu and qemux86-64 are reference boards
MACHINE = "<YOUR-MACHINE>"

# The version of Mender to build. This needs to match an existing recipe in the meta-mender repository.
#
# Given your Yocto Project version, see which versions of Mender you can currently build here:
# https://docs.mender.io/overview/compatibility#mender-client-and-yocto-project-version
#
# Given a Mender client version, see the corresponding version of the mender-artifact utility:
# https://docs.mender.io/overview/compatibility#mender-clientserver-and-artifact-format
#
# Note that by default this will select the latest released version of the tools.
# If you need an earlier version, please uncomment the following and set to the
# required version.
#
# PREFERRED_VERSION_pn-mender = "2.1.2"
# PREFERRED_VERSION_pn-mender-artifact = "3.2.1"
# PREFERRED_VERSION_pn-mender-artifact-native = "3.2.1"

# The following settings to enable systemd are needed for all Yocto
# releases sumo and older.  Newer releases have these settings conditionally
# based on the MENDER_FEATURES settings and the inherit of mender-full above.
DISTRO_FEATURES_append = " systemd"
VIRTUAL-RUNTIME_init_manager = "systemd"
DISTRO_FEATURES_BACKFILL_CONSIDERED = "sysvinit"
VIRTUAL-RUNTIME_initscripts = ""

ARTIFACTIMG_FSTYPE = "ext4"

# Build for hosted Mender
#
# To get your tenant token:
#    - log in to https://hosted.mender.io
#    - click your email at the top right and then "My organization"
#    - press the "COPY TO CLIPBOARD"
#    - assign content of clipboard to MENDER_TENANT_TOKEN
#
#MENDER_SERVER_URL = "https://hosted.mender.io"
#MENDER_TENANT_TOKEN = ""

# Build for Mender demo server
#
# https://docs.mender.io/administration/demo-installation
#
# Uncomment below and update IP address to match the machine running the
# Mender demo server
#MENDER_DEMO_HOST_IP_ADDRESS = "192.168.0.100"

# Build for Mender production setup (on-prem)
#
# https://docs.mender.io/administration/production-installation
#
# Uncomment below and update the URL to match your configured domain
# name and provide the path to the generated server.crt file.
#
# Note that a custom server.crt file is only necessary if you are using
# self-signed certificates.
#
# NOTE! It is recommend that you provide below information in your custom
# Yocto layer and this is only for demo purposes. See linked documentation
# for additional information.
#MENDER_SERVER_URL = "https://docker.mender.io"
#FILESEXTRAPATHS_prepend_pn-mender := "<DIRECTORY-CONTAINING-server.crt>:"
#SRC_URI_append_pn-mender = " file://server.crt"
```

!!! The size of the disk image (`.sdimg`) should match the total size of your storage so you do not leave unused space; see [the variable MENDER_STORAGE_TOTAL_SIZE_MB](../99.Variables/docs.md#mender_storage_total_size_mb) for more information. Mender selects the file system type it builds into the disk image, which is used for initial flash provisioning, based on the `ARTIFACTIMG_FSTYPE` variable. See the [section on file system types](../../../03.Devices/02.Yocto-project/01.Partition-configuration/docs.md#file-system-types) for more information.

!!! If you are building for **[hosted Mender](https://hosted.mender.io?target=_blank)**, make sure to set `MENDER_SERVER_URL` and `MENDER_TENANT_TOKEN` (see the comments above).

!!! If you would like to use a read-only root file system, please see the section on [configuring the image for read-only rootfs](../../10.Yocto-project/02.Image-configuration/docs.md#configuring-the-image-for-read-only-rootfs).

#### Building the image

Once all the configuration steps are done, build an image with bitbake:

```bash
bitbake <YOUR-TARGET>
```

Replace `<YOUR-TARGET>` with the desired target or image name, e.g. `core-image-full-cmdline`.

!!! The first time you build a Yocto Project image, the build process can take several hours. The successive builds will only take a few minutes, so please be patient this first time.


#### Using the build output

After a successful build, the images and build artifacts are placed in `tmp/deploy/images/<YOUR-MACHINE>/`.

There is one Mender disk image, which will have one of the following suffixes:

  * `.uefiimg` if the system boots using the UEFI standard (x86 with UEFI or ARM with U-Boot and UEFI emulation) and GRUB bootloader
  * `.sdimg` if the system is an ARM system and boots using U-Boot (without UEFI emulation)
  * `.biosimg` if the system is an x86 system and boots using the traditional BIOS and GRUB bootloader

!!! Please consult the [bootloader support section](../../../03.Devices/02.Yocto-project/02.Bootloader-support/docs.md) for information on which boot method is typically used in each build configuration.

This disk image is used to provision the device storage for devices without
Mender running already. Please proceed to [Provisioning a new device](../../20.Provisioning-a-new-device/docs.md)
for steps to do this.

On the other hand, if you already have Mender running on your device and want to deploy a rootfs update
using this build, you should use the [Mender Artifact](../../../02.Overview/02.Artifact/docs.md) files,
which have `.mender` suffix.

!!! If you built for one of the virtual Mender reference boards (`qemux86-64` or `vexpress-qemu`), you can start up your newly built image with the script in `../meta-mender/meta-mender-qemu/scripts/mender-qemu` and log in as *root* without password.
