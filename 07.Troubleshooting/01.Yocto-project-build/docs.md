---
title: Yocto Project build
taxonomy:
    category: docs
---

##Your project is using a fork of U-Boot which conflicts with the U-Boot Mender uses

When [Building a Mender Yocto Project image](../../Artifacts/Building-Mender-Yocto-image) for your own project and device, you encounter a build error similar to the following:

```
ERROR: Multiple .bb files are due to be built which each provide u-boot (.../tisdk/sources/meta-variscite/recipes-bsp/u-boot/u-boot-var-som-am33.bb .../tisdk/sources/meta-ti/recipes-bsp/u-boot/u-boot_2014.07.bb).
 This usually means one provides something the other doesn't and should.
```

Mender needs to configure U-Boot in order to support robust rootfs rollback. If your project relies on a fork of U-Boot this needs to be integrated. For more information, see [Integrating with U-Boot](../../Devices/Integrating-with-U-Boot), in particular the section on [Forks of U-boot](../../Devices/Integrating-with-U-Boot#forks-of-u-boot).


## U-Boot and the Linux kernel do not agree about the indexes of storage devices

Sometimes it happens that U-Boot will refer to a storage device as `mmc 0`, whereas the Linux kernel will refer to the same device as `/dev/mmcblk1` (note the different index). In this case the Mender build system must be told explicitly about this disagreement. To do so, you can set the following two variables:

```
MENDER_UBOOT_STORAGE_INTERFACE = "mmc"
MENDER_UBOOT_STORAGE_DEVICE = "0"
```

which will set the index that U-Boot will use. All non-U-Boot references to the storage device, including the `root` argument passed by U-Boot to the Linux kernel when booting it, will keep using the `/dev/mmcblk1` variant derived from `MENDER_STORAGE_DEVICE` variables.


## Boot loader is missing from boot partition, but is required for my board

By default Mender does not add any boot loader files to the boot partition. If your board requires this you need to specify the files in the `IMAGE_BOOT_FILES` variable in the `machine.conf` file for your board. For example:

```
IMAGE_BOOT_FILES ?= "u-boot.bin MLO"
```

See the [Yocto Project documentation](http://www.yoctoproject.org/docs/latest/mega-manual/mega-manual.html?target=_blank#var-IMAGE_BOOT_FILES) for more information about the `IMAGE_BOOT_FILES` variable.


## Missing UBOOT_SUFFIX

The Yocto Project's `UBOOT_SUFFIX` variable is defined in [the U-Boot recipe](http://git.yoctoproject.org/cgit/cgit.cgi/poky/tree/meta/recipes-bsp/u-boot/u-boot.inc?target=_blank).
At the time of writing the default value is `bin`, but some versions of U-Boot use `img`.

This variable is used by meta-mender and should be available outside the U-Boot recipe.
However, if you encounter the following error during build, it was not expanded correctly.

```
 dd: failed to open 'build/tmp/deploy/images/gatewayr2/u-boot.': No such file or directory
```

This is most likely an issue with the Yocto Project's tools or recipes.
You can work around the problem by finding the correct value (e.g. `ls build/tmp/deploy/images/<MACHINE>/u-boot.*`) and adding a corresponding line similar to the following to your `local.conf`.

```
UBOOT_SUFFIX = "bin"
```


## U-Boot lacks support for Boot Count Limit

In order to support robust rootfs rollback, Mender depends on being able to tell the bootloader to roll back to the known-working rootfs if attempts to boot the updated rootfs fails a given number of times.
Currently, Mender uses the [Boot Count Limit](http://www.denx.de/wiki/view/DULG/UBootBootCountLimit?target=_blank) feature of U-Boot to achieve this.
If you see errors similar to the following during the Yocto Project build process, the U-Boot you are using most likely does not support this feature.

```
include/config_mender.h:34:3: error: #error CONFIG_BOOTCOUNT_ENV is required for Mender to work
```

There are two alternatives to resolve this issue. Either you can upgrade to U-Boot v2014.01 or newer, where Boot Count Limit was introduced, or you can patch your current U-Boot version to support this or a similar feature. Please see [Bootloader support](../../Devices/System-requirements#bootloader-support) for more information.
