---
title: Running Yocto Project image
taxonomy:
    category: docs
---

## Boot sequence fails with "Failed to mount /uboot" and "codepage cp437 not found"

This sometimes happens when using one of the minimal images from the Yocto Project, such as `core-image-minimal` or `core-image-full-cmdline`. These images do not include the `kernel-modules` package, which contains the kernel module with codepage 437. There are two ways this can be resolved:

* If you're compiling a custom kernel, it is recommended to set the kernel configuration option:

  ```bash
  CONFIG_NLS_CODEPAGE_437=y
  ```

  Please refer to [the Yocto Project Manual](http://www.yoctoproject.org/docs/latest/mega-manual/mega-manual.html?target=_blank#configuring-the-kernel) for how to use `menuconfig` to generate and save `defconfig` files for the kernel.

* If you're not building a custom kernel, you can add this line to your `local.conf` in order to include all the kernel modules in the image:

  ```bash
  IMAGE_INSTALL_append = " kernel-modules"
  ```

  This is an easier fix, but also requires more space in the image than the previous solution, since all modules will be included, not just the missing one.

## System stops at U-Boot prompt

There are reports of some systems having trouble running the U-Boot boot commands and getting stuck at the U-Boot prompt. This has, notably, been reported to
happen on the Raspberry Pi family of boards with certain serial port adapters. In the failing scenario, it is believed that the serial port adapter is electrically
noisy resulting in spurious data on the console that is interpreted by U-Boot as the user intentionally interrupting the boot process. It is unclear which
brands of serial port adapters cause this issue or if certain boards are more susceptible than others.

If you are experiencing this issue, there are several proposed workarounds that you should try:

* Disable the serial console by editing config.txt.  With Yocto builds you can set the following in your local.conf to disable this:

  ```bash
  ENABLE_UART = "0"
  ```

* Change the U-Boot configuration to disable the UART for console input. Adding the following to the U-Boot environment has been reported to address this
in some situations:

  ```bash
  setenv stdout lcd
  setenv stderr lcd
  setenv stdin usbkbd
  ```

* Modify the U-Boot code to require a different key sequence to interrupt the boot. Some tweaking of the following settings in the U-Boot code may
help here:

  ```bash
  #define CONFIG_AUTOBOOT_KEYED
  #define CONFIG_AUTOBOOT_PROMPT \
      "\nRPi - booting... stop with ENTER\n"
  #define CONFIG_AUTOBOOT_DELAY_STR "\r"
  #define CONFIG_AUTOBOOT_DELAY_STR2 "\n"
  ```


## GRUB prints error: no such device: ((hd0,gpt1)/EFI/BOOT)/EFI/BOOT/grub.cfg.

When using GRUB as an intermediate bootloader in a Yocto Project build,
the above error is printed, possibly with a different device than `(hd0,gpt1)`.

This error message is usually harmless and only a cosmetic issue,
as GRUB will fall back to the correct location of its configuration file.

<!--AUTOVERSION: "`%` (and newer)"/ignore-->
The issue is resolved in `thud` (and newer) branches of  meta-mender.
See [issue MEN-1961](https://tracker.mender.io/browse/MEN-1961?target=_blank) for more information.


<!--AUTOVERSION: "older meta-mender branch to the % branch"/ignore-->
## I moved from an older meta-mender branch to the thud branch and suddenly my image is just a few MiB too small

This is a typical symptom:

```
error: update (952107008 bytes) is larger than the size of device /dev/mmcblk0p3 (947912704 bytes)
```

<!--AUTOVERSION: "optimization to the % branch"/ignore-->
This is because of an optimization to the thud branch which uses more of the
available space in the `sdimg` and `uefiimg` images. However, it also means that
if the device was provisioned with an older image, the new update will be just
slightly too big for the old partition to hold it.

To revert to the old size calculation, add this to your build configuration
(`machine.conf` or `local.conf` are good places):

```
MENDER_PARTITIONING_OVERHEAD_KB = "${@eval('(int((${MENDER_PARTITION_ALIGNMENT} - 1) / 1024) + 1) * 4')}"
```

## Poor performance when loading images from U-boot

On certain devices you might get poor performance when trying to load the Linux kernel image from the root filesystem, and it can look like this:

```
u-boot=> ext4load ${mender_uboot_root} /boot/${image}
23065088 bytes read in 79537 ms (282.2 KiB/s)
```

This seems to be more common on `aarch64` devices, that is 64-bit ARM.

The root cause of this issue is that U-Boot's `ext4` support does not handle extents very well. When a file gets large enough, extent index blocks will get created for it, and that leads to exercising a very slow code path. This has been fixed in upstream U-boot with this [patch](http://git.denx.de/?p=u-boot.git;a=commit;h=d5aee659f217746395ff58adf3a863627ff02ec1), but at the time of writing, this is not included in any released U-boot versions and the first version to contain this fix will be 2019.07.

There are a couple of workarounds,

1. Backport the upstream [patch](http://git.denx.de/?p=u-boot.git;a=commit;h=d5aee659f217746395ff58adf3a863627ff02ec1) to the U-boot version you are using or update U-boot to to a version that includes the mentioned patch.

2. Use a different filesystem, e.g `ext3` which does not support `extents` and does not suffer from this limitation.
    - In Yocto you can change filesystem type by setting `ARTIFACTIMG_FSTYPE = "ext3"` in your `local.conf` or other appropriate location

3. Disable `extents` feature on `ext4` filesystem
    - In Yocto you can add `EXTRA_IMAGECMD_ext4 = "-O ^extent"` in your `local.conf` or other appropriate location.
    - Above is equivalent to running `mkfs.ext4 -O ^extent` if you are using something other then Yocto to generate your filesystem images

Additional background information can be found in these threads:

- https://community.nxp.com/thread/472241
- https://github.com/madisongh/meta-tegra/issues/42
- https://hub.mender.io/t/mender-1-7-standalone-mode-kernel-read-time-get-difference-before-and-after-mender-update
