---
title: Example: QEMU
taxonomy:
    category: docs
    label: tutorial
---

## QEMU

As an example, to illustrate potential pain points we will use a Versatile
Express CortexA9x4 board, emulated under QEMU (`vexpress-a9` target). The board
comes with 128MB of CFI NOR flash, provided in form of 2 * 64MB dies. Respective
details may slightly differ for NAND flash or SPI NOR flash devices.

It is possible to build a Yocto image and inspect all the details of Mender
integration by adding the `meta-mender-qemu` layer to the build. The layer
defines a `vexpress-qemu-flash` machine and includes all necessary pieces to
enable MTD and UBI support.

!! Testing raw flash support under QEMU requires version >= 2.9 (see the output
!! of `qemu-system-arm --version` command). Earlier versions contain a bug in
!! CFI flash support that renders flash support on `vexpress-a9` unusable. 

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

!!! A `vexpress-nor` image is a tar file that contains an image for each of the
!!! `nor` 'drives' emulated by QEMU. It is specific to QEMU and will not
!!! generally be used for other devices, which will usually use either `ubimg`
!!! or `mtdimg`.

The image can be run by calling a `mender-qemu` helper script provided in
`meta-mender-qemu` layer:

```bash
QEMU_SYSTEM_ARM=$HOME/qemu-install/bin/qemu-system-arm \
DISK_IMG=tmp/deploy/images/vexpress-qemu-flash/core-image-minimal-vexpress-qemu-flash.vexpress-nor \
MACHINE=vexpress-qemu-flash \
    ../meta-mender/meta-mender-qemu/scripts/mender-qemu
```

!!! The `QEMU_SYSTEM_ARM` environment variable can optionally provide a path to
!!! `qemu-system-arm` binary used by the script. When empty or not defined, the
!!! script will call `qemu-system-arm` available in your `$PATH`.
