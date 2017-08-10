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

As an example, to illustrate potential pain points we will use a Versatile
Express CortexA9x4 board, emulated under QEMU (`vexpress-a9` target). The board
comes with 128MB of CFI NOR flash, provided in form of 2 * 64MB dies. Respective
details may slightly differ for NAND flash or SPI NOR flash devices.

### Mender

The Mender Yocto layer comes with support for the following raw flash boards in
the main tree:

* [Toradex Colibri VF50/VF61 `meta-mender-toradex-nxp`](https://github.com/mendersoftware/meta-mender/tree/master/meta-mender-toradex-nxp)
* [vexpress-a9 emulated by QEMU `meta-mender-qemu`](https://github.com/mendersoftware/meta-mender/tree/master/meta-mender-qemu)

Both layers provide a set of patches based on their respective upstream U-Boot
sources and can be used as a reference when implementing your raw flash based
machine.

### QEMU

It is possible to build a Yocto image and inspect all the details of Mender
integration by adding the `meta-mender-qemu` layer to the build. The layer
defines a `vexpress-qemu-flash` machine and includes all necessary pieces to
enable MTD and UBI support.

!! In order to test raw flash support under QEMU, a QEMU version >= 2.9 is required (see the output of `qemu-system-arm --version` command). Earlier versions contain a bug in CFI flash support that renders flash support on `vexpress-a9` unusable. 

Add the following to `local.conf` and run `bitbake core-image-minimal`:

```bash
INHERIT += "mender-full-ubi"

...

MACHINE = "vexpress-qemu-flash"

```

A successful build will produce a `vexpress-nor` image in `${DEPLOYDIR}`:

```bash
$ ls -shLl tmp/deploy/images/vexpress-qemu-flash/core-image-minimal-vexpress-qemu-flash.vexpress-nor
129M -rw-r--r-- 2 user user 129M 07-18 15:34 tmp/deploy/images/vexpress-qemu-flash/core-image-minimal-vexpress-qemu-flash.vexpress-nor
```

A `vexpress-nor` image is a tar file that contains an image for each of the `nor`
'drives' emulated by QEMU.

The image can be run by calling a `mender-qemu` helper script provided in
`meta-mender-qemu` layer:

```bash
QEMU_SYSTEM_ARM=$HOME/qemu-install/bin/qemu-system-arm \
VEXPRESS_IMG=tmp/deploy/images/vexpress-qemu-flash/core-image-minimal-vexpress-qemu-flash.vexpress-nor \
MACHINE=vexpress-qemu-flash \
    ../meta-mender/meta-mender-qemu/scripts/mender-qemu
```

!!! The `QEMU_SYSTEM_ARM` environment variable can be used to provide a path to `qemu-system-arm` binary. When empty or not defined, the script will call `qemu-system-arm` available in your `$PATH`.

### Raw flash devices, partitioning

Using raw flash devices under Linux is more complicated compared to typical
block devices such as hard disks or eMMC flash. Block devices typically come
with a partition table, using either the MBR or GPT formats, that enables
discovery and identification of existing partitions. In the case of raw flash
devices, no partition tables are in use. Instead, the kernel must be informed
about existing partitions, their start locations and sizes. This can achieved
using a number of different methods:

* machine configuration via `arch/<ARCH>/mach-<MACH>` (deprecated)
* kernel command line ([drivers/mtd/cmdlinepart.c](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/mtd/cmdlinepart.c)) typically set up by bootloader
* device tree ([DTS MTD bindings](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/Documentation/devicetree/bindings/mtd/partition.txt))

Raw flash boards currently supported by Mender use the kernel command line to pass
information about MTD partitions.

Using `vexpress-a9` QEMU target as an example, the flash area is partitioned like this:

* 1MB - U-Boot, partition name `u-boot`
* 1MB - U-Boot environment (main + redundant), partition name `u-boot-env`
* remaining space (126MB) - UBI, partition name `ubi`

Having enabled `CONFIG_CMD_MTDPARTS` in U-Boot we can see the following output
after issuing the `mtdparts` command at U-Boot prompt:

```
=> mtdparts 

device nor2 <40000000.flash>, # parts = 3
 #: name                size            offset          mask_flags
 0: u-boot              0x00100000      0x00000000      1
 1: u-boot-env          0x00100000      0x00100000      0
 2: ubi                 0x07e00000      0x00200000      0

active partition: nor2,0 - (u-boot) 0x00100000 @ 0x00000000

defaults:
mtdids  : nor2=40000000.flash
mtdparts: mtdparts=40000000.flash:1m(u-boot)ro,1m(u-boot-env),-(ubi)
```

Note that the `mtdparts` command line argument is using the same device name as
produced by board devicetree bindings.

Booting the kernel, the following log listing MTD partitions will be visible:

```bash
[    0.844595] Concatenating MTD devices:
[    0.844712] (0): "40000000.flash"
[    0.844814] (1): "40000000.flash"
[    0.844891] into device "40000000.flash"
[    0.845949] 3 cmdlinepart partitions found on MTD device 40000000.flash
[    0.846161] Creating 3 MTD partitions on "40000000.flash":
[    0.846579] 0x000000000000-0x000000100000 : "u-boot"
[    0.852186] 0x000000100000-0x000000200000 : "u-boot-env"
[    0.855636] 0x000000200000-0x000008000000 : "ubi"
```

MTD partitions can be viewed in the running system by inspecting `/proc/mtd`:

```bash
root@vexpress-qemu-flash:~# cat /proc/mtd 
dev:    size   erasesize  name
mtd0: 00100000 00040000 "u-boot"
mtd1: 00100000 00040000 "u-boot-env"
mtd2: 07e00000 00040000 "ubi"
```

### UBI and UBI File System

The `ubinize` and `mkfs.ubifs` arguments are a little complicated to get right.
One can use `mtdinfo` in a running system to obtain a set a reasonable defaults.
Using the `vexpress-a9` QEMU target as an example:

```bash
root@vexpress-qemu-flash:~# mtdinfo -u /dev/mtd2
mtd2
Name:                           ubi
Type:                           nor
Eraseblock size:                262144 bytes, 256.0 KiB
Amount of eraseblocks:          504 (132120576 bytes, 126.0 MiB)
Minimum input/output unit size: 1 byte
Sub-page size:                  1 byte
Character device major/minor:   90:4
Bad blocks are allowed:         false
Device is writable:             true
Default UBI VID header offset:  64
Default UBI data offset:        128
Default UBI LEB size:           262016 bytes, 255.9 KiB
Maximum UBI volumes count:      128
```

Note that these settings will generally be different depending on the type of
flash memory.

Once determined, the parameters for `mkfs.ubifs` and `ubinize` must be set in
the Yocto configuration using `MKUBIFS_ARGS` and `UBINIZE_ARGS` variables
respectively. Since these parameters are a specific for given board, it is
possible they may already be set by a corresponding machine configuration.

## U-Boot

To enable UBI support in U-Boot and integrate it with the kernel you will need
to enable at least these configuration options in U-Boot:

* `CONFIG_CMD_UBI`
* `CONFIG_CMD_UBIFS`
* `CONFIG_MTD_DEVICE`
* `CONFIG_MTD_PARTITIONS`
* `CONFIG_CMD_MTDPARTS`
* `CONFIG_LZO`

Optionally, to match the kernel configuration, you may need to set
`CONFIG_MTD_CONCAT` to enable automatic concatenation of neighboring flash
devices into a single one.

Using `vexpress-a9` as an example, a minimal boot script is then:

```bash
"kernel_addr_r=0x60100000\0"           \
"fdt_addr_r=0x60000000\0"              \
"fdtfile=vexpress-v2p-ca9.dtb\0"       \
"mtdparts=40000000.flash:1m(u-boot)ro,1m(u-boot-env)ro,-(ubi)\0" \
"ubiargs=ubi.mtd=2 root=ubi0:rootfs rootfstype=ubifs ubi.fm_autoconvert=1\0" \
"ubiboot=" \
	"echo Booting from NOR...; "                              \
	"ubi part ubi && "                                        \
	"ubifsmount ubi0:rootfs && "                              \
	"ubifsload ${kernel_addr_r} /boot/zImage && "             \
	"ubifsload ${fdt_addr_r} /boot/${fdtfile} && "            \
    "setenv bootargs ${mtdparts} ${ubiargs} ${defargs} && "   \
	"bootz ${kernel_addr_r} - ${fdt_addr_r}\0"
```

The script:

1. Attaches UBI partition using `ubi` device defined by `mtdparts`, creating
   the `ubi0` device.
2. Mounts the UBIFS volume `rootfs` from `ubi0`.
3. Loads `zImage` at kernel load address 0x60100000 (start of RAM + 1MB offset).
4. Loads flattened device tree at 0x60000000 (start of RAM).
5. Updates `bootargs` to include:
   1. `mtdparts` - MTD partitions, locations, sizes and naming.
   2. `ubiargs` - MTD device carrying UBI, root file system location contents on `ubi0:rootfs` volume and sets rootfs type to UBIFS.
   3. `defargs` - additional default arguments, such as console, panic settings and similar.
6. Loads the kernel.


## Integrating Mender

To enable UBI support, inherit the `mender-full-ubi` class in your `local.conf`
and take a look at the various UBI related variables in
`mender-install-ubi.bbclass`. 

Mender support will create a UBI image file (`ubimg` in `${DEPLOYDIR}/images`)
including the following volumes:

* `rootfsa` - contents of root filesystem A
* `rootfsb` - contents of root filesystem B
* `data` - contents of data partition

The `ubimg` image file can be used for populating the UBI partition with
the `ubiformat` tool.

By default a `*.ubifs` root filesystem image will be used when generating a Mender artifact.

### meta-mender integration

By inheriting [`mender-install-ubi`](https://github.com/mendersoftware/meta-mender/blob/master/meta-mender-core/classes/mender-install-ubi.bbclass) (included
in `mender-full-ubi`) the following configuration settings will be set
automatically:

* `MENDER_STORAGE_DEVICE` - defaults to `ubi0`
* `MENDER_ROOTFS_PART_A` - defaults to `ubi0_0`
* `MENDER_ROOTFS_PART_B` - defaults to `ubi0_1`
* `MENDER_ROOTFS_PART_A_NAME` and `MENDER_ROOTFS_PART_B_NAME` - defaulting to
  `ubi0:rootfsa` and `ubi0:rootfsb`

Also, you will need to set the following configuration options:

* `MENDER_STORAGE_TOTAL_SIZE_MB` - size of your flash
* `MENDER_DATA_PART_SIZE_MB` - desired size of data partition
* `MENDER_PARTITION_ALIGNMENT_KB` - partition alignment, set to match erase block size

When using UBI you may need to set `MENDER_STORAGE_RESERVED_RAW_SPACE` to
account for space lost to UBI metadata. 

These settings affect the calculated rootfs size.

!!! Note that the calculated rootfs size (i.e. volume size) is different from the actual amount of data that can be stored in rootfs. The difference is caused by compression. To set an upper boundary on the amount of rootfs data, you can define `IMAGE_ROOTFS_MAXSIZE`.

### U-Boot integration

For U-Boot, on top of options listed in [U-Boot](#u-boot) you will need to
enable the options required by Mender listed
in [U-Boot integration](../integrating-with-u-boot#u-boot-features).

The U-Boot boot process remains very much the same as described
in [integration points](../integrating-with-u-boot#integration-points) with the
addition of a call to `mender_setup` script (using `vexpress-a9` as an example):

```bash
"set_ubiargs=setenv ubiargs ubi.mtd=${mender_mtd_ubi_dev_name} "      \
             "root=${mender_kernel_root} rootfstype=ubifs ubi.fm_autoconvert=1\0"  \
"ubiboot=" \
	"echo Booting from NOR...; "                              \
	"run mender_setup; "                                      \
	"run set_ubiargs; "                                       \
	"ubi part ${mender_mtd_ubi_dev_name} && "                 \
	"ubifsload ${kernel_addr_r} /boot/zImage && "             \
    ...
```

Note that U-Boot places some constraints on parameter expansion, for this reason
the parameter `ubiargs` is no longer set by default environment. Instead it is
set by the intermediate `set_ubiargs` script.
