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


## A U-Boot component is failing to compile, and it compiles without Mender

This may be an indication that Mender's automatic U-Boot patching has failed for the particular board that's being built for, and a manual patch may be required. For information on how to create such a patch, go to the [Manual U-Boot integration section](../../devices/integrating-with-u-boot/manual-u-boot-integration).


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

* Decrease the size of each block. This can be done by setting `EXTRA_IMAGECMD_ext4 = " -b 1024"` in `local.conf`. The default is 4096, it must be a power of 2, and it must not be smaller than 1024.


## I get a build error "fw_printenv: File format not recognized"

The symptom is an error message similar to this:

```
ERROR: u-boot-fw-utils-mender-auto-provided-1.0-r0 do_package: objcopy failed with exit code 1 (cmd was 'arm-poky-linux-gnueabi-objcopy' --only-keep-debug '/home/user/poky/build/tmp/work/cortexa7hf-neon-poky-linux-gnueabi/u-boot-fw-utils-mender-auto-provided/1.0-r0/package/sbin/fw_printenv' '/home/user/poky/build/tmp/work/cortexa7hf-neon-poky-linux-gnueabi/u-boot-fw-utils-mender-auto-provided/1.0-r0/package/sbin/.debug/fw_printenv'):
arm-poky-linux-gnueabi-objcopy:/home/user/poky/build/tmp/work/cortexa7hf-neon-poky-linux-gnueabi/u-boot-fw-utils-mender-auto-provided/1.0-r0/package/sbin/fw_printenv: File format not recognized
ERROR: u-boot-fw-utils-mender-auto-provided-1.0-r0 do_package: Function failed: split_and_strip_files
ERROR: Logfile of failure stored in: /home/user/poky/build/tmp/work/cortexa7hf-neon-poky-linux-gnueabi/u-boot-fw-utils-mender-auto-provided/1.0-r0/temp/log.do_package.15130
ERROR: Task (/home/user/poky/meta-mender/meta-mender-core/recipes-bsp/u-boot/u-boot-fw-utils-mender-auto-provided_1.0.bb:do_package) failed with exit code '1'
```

This is a known bug in U-Boot versions prior to v2017.05. If you get this error, the auto-provided recipe won't work, so you will have to carry out the steps in [the u-boot-fw-utils guide](../../devices/integrating-with-u-boot/manual-u-boot-integration#u-boot-fw-utils). Note that only the section under "u-boot-fw-utils" is necessary, the other sections on the same page, such as `MENDER_UBOOT_AUTO_CONFIGURE = "0"`, should not be necessary to carry out unless you have other reasons to do so.


## I get a build error if I am using PREFERRED_PROVIDER_virtual/bootloader instead of PREFERRED_PROVIDER_u-boot

The symptom is an error message similar to this:

```
ERROR: Nothing PROVIDES 'u-boot'
u-boot was skipped: PREFERRED_PROVIDER_virtual/bootloader set to u-boot-rockchip, not u-boot
ERROR: Required build target 'core-image-base' has no buildable providers.
Missing or unbuildable dependency chain was: ['core-image-base', 'u-boot']
```

This error stems from the fact that custom u-boot fork recipes are missing hard dependency required by mender recipes. If you get this error you need to add following lines to your custom u-boot fork recipe:

```
PROVIDES += "u-boot"
RPROVIDES_${PN} = "u-boot"
```

Detailed explanation how to do it you can find in [Integrating with U-Boot](../../devices/integrating-with-u-boot) section.
