---
title: Building a Mender Yocto image
taxonomy:
    category: docs
---

This document outlines the steps needed to build a [Yocto](https://www.yoctoproject.org/?target=_blank) image containing a testable version of the Mender client for both QEMU and BeagleBone.

## What is *meta-mender*?

*meta-mender* is a layer that enables the creation of a Yocto image where the Mender client is part of the image. With Mender installed on the image, you can deploy image updates and benefit from features like automatic roll-back, remote management, phased roll-outs, logging, reporting, etc.

The *meta-mender* layer contains all the recipes required to build the Mender Go binary as a part of the Yocto image. It currently supports cross-compiling Mender for ARM devices using Go 1.6.

As Mender is a framework, not just a standalone application, it requires the
[bootloader and partition layout](../../Getting-started/System-requirements#device-partitioning) set up in a specific way. That's why it is
recommended to use Yocto for building a complete image containing all the required
dependencies and configuration.

Detailed instructions and recipes needed for building a self-containing image follows.

##Dependencies

*meta-mender* depends on the following repositories:

```
  URI: git://git.yoctoproject.org/poky
  branch: master or jethro

  URI: git://github.com/mendersoftware/meta-mender
  branch: master

  URI: git://github.com/mem/oe-meta-go
  branch: master
```

!!! For internal purposes, Yocto images for QEMU and BeagleBone are built daily using the master branches. For testing, please feel free to download these images [here](https://goo.gl/mmJoxs?target=_blank).


## 1. Get Yocto and neccessary layers

We first need to clone Yocto sources from:

```
$ git clone -b <branch-name> git://git.yoctoproject.org/git/poky
```

Next, clone the rest of the required dependencies into the top level
of the Yocto build tree (usually yocto/poky). These are the Mender layer and the 
OpenEmbedded layer for the Go programming language:

```
$git clone git://github.com/mendersoftware/meta-mender
$git clone git://github.com/mem/oe-meta-go
```

##2. Create build environment


To build a Yocto image, we need to run a setup scipt to create the build directory for Yocto and set build environment:

```
    $ source oe-init-build-env
```

This should create the build environment and build directory, and running the
command should change the current directory to the build directory. In this
document, we assume that the name of the build directory is `build`.


##3. Set Yocto build configuration


The layers used for building the image need to be included.  In order to do so,
edit `conf/bblayers.conf` and make sure that `BBLAYERS` looks like the
following:

```
    BBLAYERS ?= " \
      <YOCTO-INSTALL-DIR>/yocto/poky/meta \
      <YOCTO-INSTALL-DIR>/yocto/poky/meta-yocto \
      <YOCTO-INSTALL-DIR>/yocto/poky/meta-yocto-bsp \
      <YOCTO-INSTALL-DIR>/yocto/poky/meta-mender \
      <YOCTO-INSTALL-DIR>/yocto/poky/oe-meta-go \
      "
```

In order to support building Mender, the following changes are needed in the
```conf/local.conf``` file:

for building the image that will be run on the QEMU machine:

```
    INHERIT += "mender-install"
    MACHINE ??= "vexpress-qemu"
```

Or for building the image supported by Beaglebone Black boards:

```
    INHERIT += "mender-install"
    MACHINE ??= "beaglebone"
```
##4. Building the image

### For QEMU

Once all the configuration steps are done, the image can be built like this:

```
    $ bitbake core-image-full-cmdline
```

This will build the `core-image-full-cmdline` image type. It is possible to
build other image types. Depending on how powerful your build machine is, the first time you build a Yocto image, the build process can take up to several hours. Luckily, the successive builds will only take a few minutes, so please be patient this first time. 

**Congratulations!** At the end of a successful build, you have an image with Mender installed that can be tested in QEMU.  The images
and build artifacts are placed in `tmp/deploy/images/vexpress-qemu/`. The
directory should contain a file named
```core-image-full-cmdline-vexpress-qemu.sdimg```, which is an image that
contains a boot partition and two other partitions, each with the kernel and
rootfs.

To test how to make an update on QEMU, please read [Getting started - Your first update on Qemu](../../Getting-started/Your-first-update-on-qemu).

For more information about getting started with Yocto, it is recommended to read
the [Yocto Project Quick Start
guide](http://www.yoctoproject.org/docs/2.0/yocto-project-qs/yocto-project-qs.html?target=_blank).


### For BeagleBone Black

In order to build an image that can be run on BeagleBone Black, the following
command should be used:

```
    $ bitbake core-image-base
```

The reason why the base image is built is for simplicity of the later booting
and testing process. With the base image, all the required boot and configuration files
are created by Yocto and copied to appropriate locations in the boot partition
and the root file system.

Like for QEMU, please be aware that your first Yocto build can take a very long time  (around two hours on a powerful machine).

To test how to make an update on BeagleBone, please read [Getting started - Your first update on BeagleBone](../../Getting-started/Your-first-update-on-BeagleBone).


For more information about differences while using
different image types please see [official Yocto BeagleBone support
page](https://www.yoctoproject.org/downloads/bsps/daisy16/beaglebone).

