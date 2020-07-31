---
title: Yocto Project build
taxonomy:
    category: docs
---

##Your project is using a fork of U-Boot which conflicts with the U-Boot Mender uses

When [Building a Mender Yocto Project image](../../04.Artifacts/10.Yocto-project/01.Building/docs.md) for your own project and device, you encounter a build error similar to the following:

```
ERROR: Multiple .bb files are due to be built which each provide u-boot (.../tisdk/sources/meta-variscite/recipes-bsp/u-boot/u-boot-var-som-am33.bb .../tisdk/sources/meta-ti/recipes-bsp/u-boot/u-boot_2014.07.bb).
 This usually means one provides something the other doesn't and should.
```

Mender needs to configure U-Boot in order to support robust rootfs rollback. If your project relies on a fork of U-Boot this needs to be integrated. For more information, see [Integrating with U-Boot](../../03.Devices/02.Yocto-project/02.Bootloader-support/02.U-Boot/docs.md), in particular the section on [Forks of U-boot](../../03.Devices/02.Yocto-project/02.Bootloader-support/02.U-Boot/docs.md#forks-of-u-boot).


## A U-Boot component is failing to compile, and it compiles without Mender

This may be an indication that Mender's automatic U-Boot patching has failed for the particular board that's being built for, and a manual patch may be required. For information on how to create such a patch, go to the [Manual U-Boot integration section](../../03.Devices/02.Yocto-project/02.Bootloader-support/02.U-Boot/01.Manual-U-Boot-integration/docs.md).


## The bootloader and the Linux kernel do not agree about the indexes of storage devices

Sometimes it happens that U-Boot will refer to a storage device as `hd0` or `mmc 0`, respectively, whereas the Linux kernel will refer to the same device as `/dev/mmcblk1` (note the different index). In this case the Mender build system must be told explicitly about this disagreement. To do so, you can add the following to the build configuration:

```bash
# For U-Boot
MENDER_UBOOT_STORAGE_INTERFACE = "mmc"
MENDER_UBOOT_STORAGE_DEVICE = "0"
```

which will set the index that the bootloaders will use. All Linux references to the storage device, including the `root` argument passed by the bootloader to the Linux kernel when booting it, will keep using the `/dev/mmcblk1` variant derived from `MENDER_STORAGE_DEVICE` variables.


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

There are two alternatives to resolve this issue. Either you can upgrade to U-Boot v2014.07 or newer, where Boot Count Limit was introduced, or you can patch your current U-Boot version to support this or a similar feature. Please see [Bootloader support](../../03.Devices/01.General-system-requirements/docs.md#bootloader-support) for more information.

## The build produces an error message "__populate_fs: Could not allocate block in ext2 filesystem while writing file..."

This is most likely because you are producing an image that has a lot of small files, so many that the filesystem runs out of blocks, even if there is enough space when counting bytes. There are several ways this can be remedied:

* Check if you have `dbg-pkgs` set in `IMAGE_FEATURES` or `EXTRA_IMAGE_FEATURES`. This will cause debug packages to be included in the image, which typically contain a lot of small files. If you don't need the debug information, this feature can be disabled.

* Increase the size of the image by increasing the value in `MENDER_STORAGE_TOTAL_SIZE_MB` (see description in [Variables](../../04.Artifacts/10.Yocto-project/99.Variables/docs.md#mender_storage_total_size_mb)), which will also increase the number of blocks. However, note that unless it is increased greatly, this will still give you a filesystem which is fairly close to the block limit, so the problem could happen during production instead, if the device writes enough files.

* Decrease the size of each block. This can be done by setting `EXTRA_IMAGECMD_ext4 = " -b 1024"` in `local.conf`. The default is 4096, it must be a power of 2, and it must not be smaller than 1024.


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

Detailed explanation how to do it you can find in [Integrating with U-Boot](../../03.Devices/02.Yocto-project/02.Bootloader-support/02.U-Boot/docs.md) section.


## I'm using Flash/UBI setup and getting the message that `BOOTENV_SIZE` is too big to fit two copies inside `MENDER_RESERVED_SPACE_BOOTLOADER_DATA` with proper alignment, but my Flash size should be big enough

The message may look something like this:

```
ERROR: u-boot-toradex-2016.11+gitAUTOINC+087e95a2dc-r0 do_provide_mender_defines: BOOTENV_SIZE (0x20000) is too big to fit two copies inside MENDER_RESERVED_SPACE_BOOTLOADER_DATA (253952) with proper alignment. Please either: 1. Increase MENDER_RESERVED_SPACE_BOOTLOADER_DATA manually and make sure it is an *even* multiple of MENDER_PARTITION_ALIGNMENT. -or- 2. Decrease BOOTENV_SIZE in the U-Boot recipe so that it can fit two copies inside MENDER_RESERVED_SPACE_BOOTLOADER_DATA.
ERROR: u-boot-toradex-2016.11+gitAUTOINC+087e95a2dc-r0 do_provide_mender_defines: Function failed: do_provide_mender_defines (log file is located at /home/user/poky/build/colibri-imx7-mender/tmp/work/colibri_imx7_mender-poky-linux-gnueabi/u-boot-toradex/2016.11+gitAUTOINC+087e95a2dc-r0/temp/log.do_provide_mender_defines.22000)
ERROR: Logfile of failure stored in: /home/user/poky/build/colibri-imx7-mender/tmp/work/colibri_imx7_mender-poky-linux-gnueabi/u-boot-toradex/2016.11+gitAUTOINC+087e95a2dc-r0/temp/log.do_provide_mender_defines.22000
ERROR: Task (/home/user/poky/src/meta-freescale-3rdparty/recipes-bsp/u-boot/u-boot-toradex_2016.11.bb:do_provide_mender_defines) failed with exit code '1'
```

The problem is that the U-Boot environment that Mender uses is written to a UBI volume, not to pure Flash memory, and UBI block sizes (LEB sizes) are smaller than physical Flash block sizes (PEB sizes). UBI uses these extra bytes for its own purposes, so they are not available for storage. Therefore the U-Boot environment must be adjusted to fit inside Mender's UBI volume if it fit exactly into physical sectors before introducing Mender.

There are two simple ways to fix the problem; which one should be used depends on the situation.

1. Decrease the `BOOTENV_SIZE` variable, so that it's no longer too big to fit two copies. This is generally the recommended solution unless you really need `BOOTENV_SIZE` size to be a certain size.

2. Multiply `MENDER_RESERVED_SPACE_BOOTLOADER_DATA`, whose value you can see in the error message, by some even value, like 2, and set that in the configuration for the board.

!! In the UBI case, `MENDER_RESERVED_SPACE_BOOTLOADER_DATA` is generally *not* a power two, so watch out for this. It should be an even multiple of `MENDER_PARTITION_ALIGNMENT`, which is itself defined from `MENDER_UBI_LEB_SIZE`, both of which you can get by running `bitbake -e core-image-minimal | egrep '^(MENDER_UBI_LEB_SIZE|MENDER_PARTITION_ALIGNMENT)='`.


## do_mender_uboot_auto_configure fails when executing `tools/env/fw_printenv -l fw_printenv.lock`

Typical symptoms is that there is some output similar to this:

```
+ tools/env/fw_printenv -l fw_printenv.lock
*** buffer overflow detected ***: tools/env/fw_printenv terminated
======= Backtrace: =========
/lib/x86_64-linux-gnu/libc.so.6(+0x777e5)[0x7fee9e46e7e5]
/lib/x86_64-linux-gnu/libc.so.6(__fortify_fail+0x5c)[0x7fee9e51015c]
/lib/x86_64-linux-gnu/libc.so.6(+0x117160)[0x7fee9e50e160]
/lib/x86_64-linux-gnu/libc.so.6(+0x1166c9)[0x7fee9e50d6c9]
/lib/x86_64-linux-gnu/libc.so.6(_IO_default_xsputn+0x80)[0x7fee9e4726b0]
/lib/x86_64-linux-gnu/libc.so.6(_IO_vfprintf+0x7bd)[0x7fee9e44492d]
/lib/x86_64-linux-gnu/libc.so.6(__vsprintf_chk+0x84)[0x7fee9e50d754]
/lib/x86_64-linux-gnu/libc.so.6(__sprintf_chk+0x7d)[0x7fee9e50d6ad]
tools/env/fw_printenv[0x4012ca]
/lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xf0)[0x7fee9e417830]
tools/env/fw_printenv[0x4014b9]
======= Memory map: ========
00400000-00407000 r-xp 00000000 08:01 8197150                            /home/user/poky/build-vexpress-qemu/tmp/work/vexpress_qemu-poky-linux-gnueabi/u-boot/1_2018.01-r0/tmp-src/tools/env/fw_printenv
00606000-00607000 r--p 00006000 08:01 8197150                            /home/user/poky/build-vexpress-qemu/tmp/work/vexpress_qemu-poky-linux-gnueabi/u-boot/1_2018.01-r0/tmp-src/tools/env/fw_printenv
00607000-00609000 rw-p 00007000 08:01 8197150                            /home/user/poky/build-vexpress-qemu/tmp/work/vexpress_qemu-poky-linux-gnueabi/u-boot/1_2018.01-r0/tmp-src/tools/env/fw_printenv
01456000-01477000 rw-p 00000000 00:00 0                                  [heap]
7fee9e1e1000-7fee9e1f7000 r-xp 00000000 08:01 1961                       /lib/x86_64-linux-gnu/libgcc_s.so.1
7fee9e1f7000-7fee9e3f6000 ---p 00016000 08:01 1961                       /lib/x86_64-linux-gnu/libgcc_s.so.1
7fee9e3f6000-7fee9e3f7000 rw-p 00015000 08:01 1961                       /lib/x86_64-linux-gnu/libgcc_s.so.1
7fee9e3f7000-7fee9e5b7000 r-xp 00000000 08:01 1967                       /lib/x86_64-linux-gnu/libc-2.23.so
7fee9e5b7000-7fee9e7b7000 ---p 001c0000 08:01 1967                       /lib/x86_64-linux-gnu/libc-2.23.so
7fee9e7b7000-7fee9e7bb000 r--p 001c0000 08:01 1967                       /lib/x86_64-linux-gnu/libc-2.23.so
7fee9e7bb000-7fee9e7bd000 rw-p 001c4000 08:01 1967                       /lib/x86_64-linux-gnu/libc-2.23.so
7fee9e7bd000-7fee9e7c1000 rw-p 00000000 00:00 0
7fee9e7c1000-7fee9e7e7000 r-xp 00000000 08:01 1965                       /lib/x86_64-linux-gnu/ld-2.23.so
7fee9e9d9000-7fee9e9dc000 rw-p 00000000 00:00 0
7fee9e9e5000-7fee9e9e6000 rw-p 00000000 00:00 0
7fee9e9e6000-7fee9e9e7000 r--p 00025000 08:01 1965                       /lib/x86_64-linux-gnu/ld-2.23.so
7fee9e9e7000-7fee9e9e8000 rw-p 00026000 08:01 1965                       /lib/x86_64-linux-gnu/ld-2.23.so
7fee9e9e8000-7fee9e9e9000 rw-p 00000000 00:00 0
7ffd719dc000-7ffd719ff000 rw-p 00000000 00:00 0                          [stack]
7ffd71a73000-7ffd71a76000 r--p 00000000 00:00 0                          [vvar]
7ffd71a76000-7ffd71a78000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]
./uboot_auto_configure.sh: line 120:  3631 Aborted                 (core dumped) tools/env/fw_printenv -l fw_printenv.lock > "$TMP_DIR/compiled-environment.txt"
WARNING: exit code 134 from a shell command.
ERROR: Function failed: do_mender_uboot_auto_configure (log file is located at /home/user/poky/build-vexpress-qemu/tmp/work/vexpress_qemu-poky-linux-gnueabi/u-boot/1_2018.01-r0/temp/log.do_mender_uboot_auto_configure.29863)
```

This is a known bug in U-Boot versions prior to v2018.05. If you hit this you will need to include [this patch](https://raw.githubusercontent.com/mendersoftware/meta-mender/27f9e8dabf461d59dec4d94bd93d6b7207be0040/meta-mender-core/recipes-bsp/u-boot/patches/0005-fw_env_main.c-Fix-incorrect-size-for-malloc-ed-strin.patch?target=_blank) in your U-Boot sources. After adding the patch file to your layer, in your U-Boot `.bb` or `.bbappend` file, add the following:

```
SRC_URI_append = " file://0005-fw_env_main.c-Fix-incorrect-size-for-malloc-ed-strin.patch"
```


## I'm trying to integrate with GRUB on an ARM board, but I only see U-Boot loading and never GRUB

Unlike x86, ARM based boards usually do not implement [the UEFI boot standard](https://en.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface?target=_blank). Therefore, on ARM, U-Boot is used as a first stage bootloader which provides a UEFI loader, and this is then used to boot GRUB using the UEFI boot standard. For a large number of boards out there, this works out of the box.

!!! Do not confuse the usage of "U-Boot as a first stage bootloader" with "U-Boot integration". "GRUB integration" still means that GRUB is used for all integration with the Mender client.

However, some boards do not call `distro_bootcmd` as part of their U-Boot startup script, and in this case the approach will not work. A typical symptom is that the U-Boot bootloader skips loading of GRUB entirely and goes directly to loading the kernel. If this happens to you, you have two choices:

1. Change the bootscript to call `distro_bootcmd` by patching U-Boot
2. Abandon GRUB integration and attempt [U-Boot integration](../../03.Devices/02.Yocto-project/02.Bootloader-support/02.U-Boot/docs.md) instead


## My device ends up at the GRUB prompt and all error and debug messages are lost because it clears the screen

This is a common problem when trying to debug boot problems with GRUB. meta-mender provides an option to pause the boot process to see the messages before they disappear. To enable it, add this to `local.conf`:

```
PACKAGECONFIG_append_pn-grub-mender-grubenv = " debug-pause"
```

This option should be removed before moving to production.

There is also an option, `debug-log`, to put GRUB in debug mode, where it will print a lot of debugging output.


## The firmware in my device looks for certain files on the first partition of the device, and this does not work while attempting GRUB integration

By default, meta-mender will produce a UEFI image (`uefiimg`) when integrating with GRUB. However, some older firmware may not recognize the [GPT partition table](https://en.wikipedia.org/wiki/GUID_Partition_Table?target=_blank) which is used on UEFI images. If so, the image can be switched to an [MBR partition table](https://en.wikipedia.org/wiki/Master_boot_record?target=_blank) image (`sdimg`) by adding the snippet below to the build configuration:

```
MENDER_FEATURES_ENABLE_append = " mender-image-sd"
MENDER_FEATURES_DISABLE_append = " mender-image-uefi"
```

<!--AUTOVERSION: "When I update Yocto version from % to %"/ignore-->
## When I update Yocto version from rocko to sumo U-boot patches do not apply

This is what the error message might look like.

```
ERROR: u-boot-custom-2017.03-r0 do_patch: Command Error: 'quilt --quiltrc /home/user/git/poky/build/tmp/work/imx6ullevk-poky-linux-gnueabi/u-boot-custom/2017.03-r0/recipe-sysroot-native/etc/quiltrc push' exited with 0  Output:
Applying patch 0006-env-Kconfig-Add-descriptions-so-environment-options-.patch
can't find file to patch at input line 19
Perhaps you used the wrong -p or --strip option?
The text leading up to this was:
--------------------------
|From f083052dd16a09c51a9426aa008b0c20878a7c30 Mon Sep 17 00:00:00 2001
|From: Kristian Amlie <kristian.amlie@northern.tech>
|Date: Mon, 23 Apr 2018 23:10:33 +0200
|Subject: [PATCH 6/6] env/Kconfig: Add descriptions so environment options can
| be modified.
|
|Without a description they always revert to their defaults regardless
|of what is in the defconfig file.
|
|Signed-off-by: Kristian Amlie <kristian.amlie@northern.tech>
|---
| env/Kconfig | 4 ++--
| 1 file changed, 2 insertions(+), 2 deletions(-)
|
|diff --git a/env/Kconfig b/env/Kconfig
|index bef6e89..f8d5ddb 100644
|--- a/env/Kconfig
|+++ b/env/Kconfig
--------------------------
No file to patch.  Skipping patch.
2 out of 2 hunks ignored
Patch 0006-env-Kconfig-Add-descriptions-so-environment-options-.patch does not apply (enforce with -f)
ERROR: u-boot-custom-2017.03-r0 do_patch: Function failed: patch_do_patch
ERROR: Logfile of failure stored in: /home/user/git/poky/build/tmp/work/imx6ullevk-poky-linux-gnueabi/u-boot-custom/2017.03-r0/temp/log.do_patch.30239
ERROR: Task (/home/user/git/poky/meta-freescale/recipes-bsp/u-boot/u-boot-custom_2017.03.bb:do_patch) failed with exit code '1'
NOTE: Tasks Summary: Attempted 1428 tasks of which 458 didn't need to be rerun and 1 failed.
```

<!--AUTOVERSION: "U-Boot version used in % by upstream Yocto"/ignore-->
This is because the U-Boot version used in sumo by upstream Yocto is v2018.01,
and the u-boot-custom version is v2017.03. It is safe to simply remove  this
patch, since I it fixes a problem that was introduced after v2017.03.

Just add this to your u-boot bbappend file:

```
SRC_URI_remove =
"0006-env-Kconfig-Add-descriptions-so-environment-options-.patch"
```


## Bitbake produces a warning that it doesn't know how to flash an mtdparts section

An example of the type of warning is this:

```
WARNING: core-image-full-cmdline-1.0-r0 do_image_mtdimg: Don't know how to flash mtdparts 'u-boot1'. Filling with zeros.
```

This can happen if `MENDER_MTDPARTS` has been set manually, and contains volumes
that Mender doesn't know how to handle. In most cases this means that the
`mtdimg` is not usable, since it will not contain what is expected by the
platform. Under these circumstances it should be turned off, and either the
`ubimg` should be used directly, or you need to produce an `mtdimg` by different
means.

```bash
IMAGE_FSTYPES_remove = "mtdimg"
```

Alternatively, if appropriate, you can remove the manually set `MENDER_MTDPARTS`
variable, and let Mender set it automatically, but you will then get a generic
`mtdimg` which may not work on the platform in question. Please refer to [the
Raw Flash section](../../03.Devices/02.Yocto-project/03.Raw-flash/docs.md) for more information.

## After updating, the RootfsPartA and RootfsPartB are missing from `/etc/mender/mender.conf`

This may be due to a new feature added in `release 1.8`. From this release onwards, the `mender.conf` file will be split
into a persistent file (/data/mender/mender.conf) and a transient file (/etc/mender/mender.conf) each of which will hold
separate settings. By default, `RootfsPartA` and `RootfsPartB` are stored in the persistent configuration file, this can
be controlled by setting the `MENDER_PERSISTENT_CONFIGURATION_VARS` to whichever configuration variables you would like
to be persistent for your device in your `local.conf` file like so:
```bash
MENDER_PERSISTENT_CONFIGURATION_VARS = "RootfsPartA RootfsPartB"
```
For users still on the old setup, there is a `state-script` available that will
help migrate a device from the old setup to the new one. This is enabled by adding
```bash
IMAGE_INSTALL_append = " mender-migrate-configuration"
```
to your `local.conf` file.

## I get a build error "Disk Requirements: At least xxx more space needed on the / filesystem." or "The rootfs size xxx(K) overrides IMAGE_ROOTFS_MAXSIZE: xxx(K)"

This indicates that the size declared for the full Mender image is too small to contain all files in the root filesystem.

Increase the size of the image by increasing the value in `MENDER_STORAGE_TOTAL_SIZE_MB` (see description in [Variables](../../04.Artifacts/10.Yocto-project/99.Variables/docs.md#mender_storage_total_size_mb)).

## Conflict between u-boot and grub-efi versions

A typical error message for this condition is:

<!--AUTOVERSION: "mender-%-r0.cortexa8hf_neon"/mender-->
```
Error:
 Problem: package grub-efi-mender-precompiled-2.04-r0.cortexa8hf_neon requires u-boot, but none of the providers can be installed
  - package grub-efi-mender-precompiled-2.04-r0.cortexa8hf_neon conflicts with u-boot <= 1:2019.07 provided by u-boot-fork-1:2019.07-r0.beaglebone_yocto
  - package mender-master-r0.cortexa8hf_neon requires grub-editenv, but none of the providers can be installed
  - conflicting requests
```

There are several possible resolutions to this problem:

1. If your u-boot version is older than (and not equal) to 2018.11, you can suppress the message by adding this to `local.conf`:
   ```
   RCONFLICTS_remove = "u-boot (<= 1:2019.07)"
   ```
   Note that `u-boot` needs to be replaced with a different name if you are using a U-Boot fork. The name should be visible the error message from earlier (look for `u-boot-fork` in the example message above). You can *try* this fix even if you U-Boot version is equal to or higher than 2018.11, but most likely the board will not boot, because the 2018.11 &lt;-&gt; 2019.07 version range has known problems in the UEFI loader.

2. See if you can use an updated version recipe for your fork of U-Boot, for example by fetching the latest Yocto branch for the layer that contains the U-Boot fork.

3. Avoid UEFI altogether by switching off the `mender-grub` feature. This will require you to use [U-Boot integration](../../03.Devices/02.Yocto-project/02.Bootloader-support/02.U-Boot/docs.md) instead.
