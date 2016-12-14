---
title: Running Yocto Project image
taxonomy:
    category: docs
---

## Boot sequence fails with "Failed to mount /uboot" and "codepage cp437 not found"

This sometimes happens when using one of the minimal images from the Yocto Project, such as `core-image-minimal` or `core-image-full-cmdline`. These images do not include the `kernel-modules` package, which contains the kernel module with codepage 437. There are two ways this can be resolved:

* If you're compiling a custom kernel, it is recommended to set the kernel configuration option:

  ```
  CONFIG_NLS_CODEPAGE_437=y
  ```

  Please refer to [the Yocto Project Manual](http://www.yoctoproject.org/docs/latest/mega-manual/mega-manual.html#configuring-the-kernel) for how to use `menuconfig` to generate and save `defconfig` files for the kernel.

* If you're not building a custom kernel, you can add this line to your `local.conf` in order to include all the kernel modules in the image:

  ```
  IMAGE_INSTALL_append = " kernel-modules"
  ```

  This is an easier fix, but also requires more space in the image than the previous solution, since all modules will be included, not just the missing one.
