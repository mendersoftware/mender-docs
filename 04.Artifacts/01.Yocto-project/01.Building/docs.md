---
title: Building a Mender Yocto Project image
taxonomy:
    category: docs
---

This document outlines the steps needed to build a [Yocto Project](https://www.yoctoproject.org/?target=_blank) image for a device.
The build output will most notably include:
* a disk image that can be flashed to the device storage during initial provisioning
* an Artifact containing rootfs filesystem image file that Mender can deploy to your provisioned device, it has suffix `.mender`

!!! If you do not want to build your own images for testing purposes, the [Getting started](../../../getting-started) tutorials provide links to several [demo images](../../../getting-started/download-test-images).

## What is *meta-mender*?

[meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank) is a set of layers that enable the creation of a Yocto Project image where the Mender client is part of the image. With Mender installed and configured on the image, you can deploy image updates and benefit from features like automatic roll-back, remote management, logging and reporting.

Inside *meta-mender* there are several layers. The most important one is *meta-mender-core*, which is required by all builds that use Mender. *meta-mender-core* takes care of:

* Cross-compiling Mender for ARM devices
* [Partitioning the image correctly](../../../devices/yocto-project/partition-configuration)
* [Setting up the U-Boot bootloader to support Mender](../../../devices/yocto-project/bootloader-support/u-boot)

Each one of these steps can be configured further, see the linked sections for more details.

The other layers in *meta-mender* provide support for specific boards used in Mender testing.

## What is *meta-mender-community*?

[meta-mender-community](https://github.com/mendersoftware/meta-mender-community?target=_blank) is a set of layers containing board-specific settings for Mender integration.

!!! For general information about getting started with Yocto Project, it is recommended to read the [Yocto Project Quick Start guide](http://www.yoctoproject.org/docs/2.4/yocto-project-qs/yocto-project-qs.html?target=_blank).


## Prerequisites

### Board integrated with Mender

Mender needs to integrate with your board, most notably with the boot process.
Although the integration is automated for most boards, please see
[Board integration](../../../devices) for general requirements and
adjustment you might need to make before building.

Check out the board integrations at [Mender Hub](https://hub.mender.io?target=_blank) to see if your board is
already integrated.
If you encounter any issues and want to save time, you can use
the [Mender professional services to integrate your board](https://mender.io/product/board-support?target=_blank).


### Correct clock on device

Make sure that the clock is set correctly on your devices. Otherwise certificate verification will become unreliable
and **the Mender client can likely not connect to the Mender server**.
See [certificate troubleshooting](../../../troubleshooting/mender-client#certificate-expired-or-not-yet-valid) for more information.


## Yocto Project

Full details for building the Yocto project for your board are available at the Mender Hub. The tested reference platforms for Mender are available at the following:
* [Raspberry Pi 3 Model B/B+](https://hub.mender.io/t/raspberry-pi-3-model-b-b/57)
* [BeagleBone Black](https://hub.mender.io/t/beaglebone-black/83)
* [QEMU](https://hub.mender.io/t/qemu-the-fast-processor-emulator/420)

!!! Note that the Yocto Project also depends on some [development tools to be in place](http://www.yoctoproject.org/docs/2.4/yocto-project-qs/yocto-project-qs.html?target=_blank#packages).

! The `meta-mender-demo` layer, which is included in the integrations available at [Mender Hub](https://hub.mender.io?target=_blank), is not appropriate if you are building for production devices. Please go to the section about [building for production](../building-for-production) to see the difference between demo builds and production builds.

If you encounter any issues, please see [Board integration](../../../devices)
for general requirements and adjustments you might need to enable your board to
support Mender.

### Configuring the build

!!! The configuration from [Mender Hub](https://hub.mender.io?target=_blank) will create a build that runs the Mender client in managed mode, as a `systemd` service. It is also possible to [run Mender standalone from the command-line or a custom script](../../../architecture/overview#modes-of-operation). See the [section on customizations](../image-configuration#disabling-mender-as-a-system-service) for steps to disable the `systemd` integration.


The following settings will be present in the default `conf/local.conf` after running the steps from [Mender Hub[(https://hub.mender.io?target=_blank). These are likely to need customization for your setup.

<!--AUTOVERSION: "Mender %"/mender "releases % and older"/ignore-->
```bash
# The name of the disk image and Artifact that will be built.
# This is what the device will report that it is running, and different updates must have different names
# because Mender will skip installation of an Artifact if it is already installed.
MENDER_ARTIFACT_NAME = "release-1"

# The version of Mender to build. This needs to match an existing recipe in the meta-mender repository.
#
# Given your Yocto Project version, see which versions of Mender you can currently build here:
# https://docs.mender.io/architecture/compatibility#mender-client-and-yocto-project-version
#
# Given a Mender client version, see the corresponding version of the mender-artifact utility:
# https://docs.mender.io/architecture/compatibility#mender-clientserver-and-artifact-format
#
# Note that by default this will select the latest released version of the tools.
# If you need an earlier version, please uncomment the following and set to the
# required version.
#
# PREFERRED_VERSION_pn-mender = "1.1.%"
# PREFERRED_VERSION_pn-mender-artifact = "2.0.%"
# PREFERRED_VERSION_pn-mender-artifact-native = "2.0.%"

ARTIFACTIMG_FSTYPE = "ext4"

# Build for Hosted Mender
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
# https://docs.mender.io/getting-started/create-a-test-environment
#
# Uncomment below and update IP address to match the machine running the
# Mender demo server
#MENDER_DEMO_HOST_IP_ADDRESS = "192.168.0.100"

# Build for Mender production setup (on-prem)
#
# https://docs.mender.io/artifacts/building-for-production
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

!!! The size of the disk image (`.sdimg`) should match the total size of your storage so you do not leave unused space; see [the variable MENDER_STORAGE_TOTAL_SIZE_MB](../variables#mender_storage_total_size_mb) for more information. Mender selects the file system type it builds into the disk image, which is used for initial flash provisioning, based on the `ARTIFACTIMG_FSTYPE` variable. See the [section on file system types](../../../devices/yocto-project/partition-configuration#file-system-types) for more information.

!!! If you are building for **Hosted Mender**, make sure to set `MENDER_SERVER_URL` and `MENDER_TENANT_TOKEN` (see the comments above).

!!! If you would like to use a read-only root file system, please see the section on [configuring the image for read-only rootfs](../../yocto-project/image-configuration#configuring-the-image-for-read-only-rootfs).
