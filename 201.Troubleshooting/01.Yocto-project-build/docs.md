---
title: Yocto Project build
taxonomy:
    category: docs
---

##Your project is using a fork of U-Boot which conflicts with the U-Boot Mender uses

When [Building a Mender Yocto Project image](../../artifacts/building-mender-yocto-image) for your own project and device, you encounter a build error similar to the following:

```
ERROR: Multiple .bb files are due to be built which each provide u-boot (.../tisdk/sources/meta-variscite/recipes-bsp/u-boot/u-boot-var-som-am33.bb .../tisdk/sources/meta-ti/recipes-bsp/u-boot/u-boot_2014.07.bb).
 This usually means one provides something the other doesn't and should.
```

Mender needs to configure U-Boot in order to support robust rootfs rollback. If your project relies on a fork of U-Boot this needs to be integrated. For more information, see [Integrating with U-Boot](../../devices/integrating-with-u-boot), in particular the section on [Forks of U-boot](../../devices/integrating-with-u-boot#forks-of-u-boot).


## U-Boot and the Linux kernel do not agree about the indexes of storage devices

Sometimes it happens that U-Boot will refer to a storage device as `mmc 0`, whereas the Linux kernel will refer to the same device as `/dev/mmcblk1` (note the different index). In this case the Mender build system must be told explicitly about this disagreement. To do so, you can set the following two variables:

```bash
MENDER_UBOOT_STORAGE_INTERFACE = "mmc"
MENDER_UBOOT_STORAGE_DEVICE = "0"
```

which will set the index that U-Boot will use. All non-U-Boot references to the storage device, including the `root` argument passed by U-Boot to the Linux kernel when booting it, will keep using the `/dev/mmcblk1` variant derived from `MENDER_STORAGE_DEVICE` variables.


## Bootloader is missing from boot partition, but is required for my device

By default Mender does not add any bootloader files to the boot partition. If your device requires this you need to specify the files in the `IMAGE_BOOT_FILES` variable in the `machine.conf` file for your device. For example:

```bash
IMAGE_BOOT_FILES ?= "u-boot.bin MLO"
```

See the [Yocto Project documentation](http://www.yoctoproject.org/docs/latest/mega-manual/mega-manual.html?target=_blank#var-IMAGE_BOOT_FILES) for more information about the `IMAGE_BOOT_FILES` variable.


## U-Boot lacks support for Boot Count Limit

In order to support robust rootfs rollback, Mender depends on being able to tell the bootloader to roll back to the known-working rootfs if attempts to boot the updated rootfs fails a given number of times.
Currently, Mender uses the [Boot Count Limit](http://www.denx.de/wiki/view/DULG/UBootBootCountLimit?target=_blank) feature of U-Boot to achieve this.
If you see errors similar to the following during the Yocto Project build process, the U-Boot you are using most likely does not support this feature.

```bash
include/config_mender.h:34:3: error: #error CONFIG_BOOTCOUNT_ENV is required for Mender to work
```

There are two alternatives to resolve this issue. Either you can upgrade to U-Boot v2014.07 or newer, where Boot Count Limit was introduced, or you can patch your current U-Boot version to support this or a similar feature. Please see [Bootloader support](../../devices/system-requirements#bootloader-support) for more information.

## The build produces an error message "__populate_fs: Could not allocate block in ext2 filesystem while writing file..."

This is most likely because you are producing an image that has a lot of small files, so many that the filesystem runs out of blocks, even if there is enough space when counting bytes. There are several ways this can be remedied:

* Check if you have `dbg-pkgs` set in `IMAGE_FEATURES` or `EXTRA_IMAGE_FEATURES`. This will cause debug packages to be included in the image, which typically contain a lot of small files. If you don't need the debug information, this feature can be disabled.

* Increase the size of the image by increasing the value in `MENDER_STORAGE_TOTAL_SIZE_MB` (see description in [Variables](../../artifacts/variables#mender_storage_total_size_mb)), which will also increase the number of blocks. However, note that unless it is increased greatly, this will still give you a filesystem which is fairly close to the block limit, so the problem could happen during production instead, if the device writes enough files.

* Decrease the size of each block. This can be done by setting `EXTRA_IMAGECMD_ext4 = " -b 1024"` in `local.conf`. The default is 4096, and must be a power of 1024.
