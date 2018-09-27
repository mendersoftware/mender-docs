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

  Please refer to [the Yocto Project Manual](http://www.yoctoproject.org/docs/latest/mega-manual/mega-manual.html#configuring-the-kernel) for how to use `menuconfig` to generate and save `defconfig` files for the kernel.

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

Most likely this is an issue in the upstream GRUB recipe from the Yocto Project
and it should be fixed in an upstream release or by
[Mender providing its own GRUB recipe](https://tracker.mender.io/browse/MEN-1961?target=_blank).
