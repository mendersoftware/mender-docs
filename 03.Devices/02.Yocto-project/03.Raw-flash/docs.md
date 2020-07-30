
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
next example section]().


### Raw flash storage

The Mender Yocto layer comes with support for auto-configuring most aspects of
the Flash specific components, including partitioning and the U-Boot
bootloader. Some configuration values need to be set, however, and they are
described below.

For more information about these or other variables that affect a Flash build,
see [the Variables section](../../../04.Artifacts/10.Yocto-project/99.Variables/docs.md).


#### MENDER_MTDIDS

The MTDID string is required, and describes the Flash type and the location it
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


#### MENDER_MTDPARTS

The MTDPARTS string expresses the MTD partitions that are present on the
device. If it is not provided, Mender will provide a default one which contains
only a `u-boot` entry and the `ubi` section, but the string often needs to be
manually specified to match the layout expectations of the device.

```bash
# Example of string that Mender itself provides:
MENDER_MTDPARTS = "40000000.flash:512k(u-boot),-(ubi)"

# Example of a custom string (this one is for the Toradex Colibri board):
MENDER_MTDPARTS = "gpmi-nand:512k(mx7-bcb),1536k(u-boot1)ro,1536k(u-boot2)ro,512k(u-boot-env),-(ubi)"
```

The `MENDER_MTDPARTS` variable has an impact on the `mtdimg` image type that
Mender produces. Normally it tries to produce an image which contains the U-Boot
boot code inside the `u-boot` partition (actually the file specified in the
`MENDER_IMAGE_BOOTLOADER_FILE` variable), and the `ubimg` inside the `ubi`
partition. For custom strings it may not be able to put things in the right
places, ant it may be preferable to turn this image type off, and use the
`ubimg` instead:

```bash
IMAGE_FSTYPES_remove = "mtdimg"
```

See also [image types](#image-types) below for more information about the
different image types for Flash.

If you don't know what value the `MENDER_MTDPARTS` string should have, like
`CONFIG_MTDIDS` a good place to look is the U-Boot source code, particularly the
value of `CONFIG_MTDPARTS_DEFAULT` for the particular board.


#### Physical erase block (PEB) size

Mender needs to know what the physical erase block size of the Flash store
is. It can be set using the following variable:

```bash
# PEB size of 128KiB, a common size.
MENDER_STORAGE_PEB_SIZE = "131072"
```

If you don't what it is it can be found by running this command on the
board. This assumes that you have a working image installed on the board, and
that the `mtdinfo` tool is available.

```bash
mtdinfo -a | grep -i 'eraseblock size:' |sort -u
```


#### Bootloader

This is only relevant if you are using [the `mtdimg` image
type](#image-types). If you need to flash a bootloader into the `u-boot` MTD
partition, it should be specified as a bare filename, like this:

```bash
MENDER_IMAGE_BOOTLOADER_FILE = "u-boot.bin"
```


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
identified from its ["mtdparts" string (`MENDER_MTDPARTS`)](#mender_mtdparts).

#### mtdimg

A raw flash image for MTD devices that contains the `ubimg` as well as other
components specified in the [`MENDER_MTDPARTS` variable](#mender_mtdparts).

This image can be flashed directly to a raw Flash device.
