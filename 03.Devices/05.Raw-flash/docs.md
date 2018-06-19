---
title: Raw flash
taxonomy:
    category: docs
---

This chapter introduces the technical details of raw flash support in Mender.

## Overview

Support for raw flash memory under Linux is in general more complicated than
working with block devices. It is advised to have a fully working bootloader,
kernel and rootfs before introducing Mender.

The Mender Yocto layer comes with support for the following raw flash boards in
the main tree:

* Toradex Colibri VF50/VF61 `meta-mender-toradex-nxp`
* vexpress-a9 emulated by QEMU `meta-mender-qemu`

Both layers provide a set of patches based on their respective upstream U-Boot
sources and can be used as a reference when implementing your raw flash based
machine.

As an example, to illustrate potential pain points we will use a Versatile
Express CortexA9x4 board, emulated under QEMU (`vexpress-a9` target). See [the
next example section](example-qemu).


### Raw flash storage

The Mender Yocto layer comes with support for auto-configuring most aspects of
the Flash specific components, including partitioning and the U-Boot
bootloader. But there is at least one piece of information that must be
supplied: The MTDID string, which describes the Flash type and the location it
has in the device's memory. For example:

```
MENDER_MTDIDS = "nor0=40000000.flash"
```

Having one entry will allow the Mender Yocto layer to deduce the proper storage
parameters and partition layout. If the device has more than one unit of Flash
storage, it is possible to add more than one entry, separated by comma; in this
case you will also need to set `MENDER_IS_ON_MTDID` to the Flash device that you
want Mender to reside on and update. For example:

```
MENDER_MTDIDS = "nand0=40000000.flash,nand1=60000000.flash"
MENDER_IS_ON_MTDID = "60000000.flash"
```

Note that currently Mender only supports running on, and updating, one Flash
storage device, but you can have more Flash storage devices inside one system
outside of Mender's control.

Please refer to the documentation for your device to find out what value to put
in `MENDER_MTDIDS`. If in doubt, a good place to look is the U-Boot source code
for the board, specifically the value of `CONFIG_MTDIDS_DEFAULT`.

For more information about variables that affect a Flash build, see [the
Variables section](../../artifacts/variables).


### Image types

There are three relevant image types that can be built when using raw flash.
They can be enabled by adding them to the `IMAGE_FSTYPES` Yocto variable.

#### ubifs

A UBI filesystem that contains the root filesystem. The data filesystem is also
built using the same filesystem type.

#### ubimg

A UBI image that contains multiple UBI volumes, at minimum including two root
filesystem volumes and one data volume. It will also normally contain two
volumes to store two redundant copies of U-Boot's environment data.

This image can be flashed to an MTD device into its "ubi" partition, as
identified from its "mtdparts" string (`MENDER_MTDPARTS`).

#### mtdimg

A raw flash image for MTD devices that contains the `ubimg` as well as other
components specified in the `MENDER_MTDPARTS` variable.

This image can be flashed directly to a raw Flash device.
