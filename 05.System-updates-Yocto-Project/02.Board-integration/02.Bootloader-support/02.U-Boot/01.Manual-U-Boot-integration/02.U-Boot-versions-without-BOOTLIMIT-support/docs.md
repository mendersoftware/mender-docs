---
title: Experimental: U-Boot versions without BOOTLIMIT support
taxonomy:
    category: docs
---

Some older versions of U-Boot do not have support for the BOOTLIMIT feature,
which Mender depends on. In this experimental section we provide a way to work
around this missing feature by using custom boot code to simulate the
feature. It is equivalent in terms of functionality and robustness.

This section assumes that you are using a [custom fork of
U-Boot](../../docs.md#forks-of-u-boot).

## The cross platform part

The cross platform bit is actually quite easy, just need to enable the patch for
Mender's generic boot code that we already provide. Add this to your
`u-boot-my-fork.bb` or `u-boot-my-fork.bbappend` file (adjust paths as
necessary):

```bash
FILESEXTRAPATHS_prepend := "${THISDIR}/../../../meta-mender-core/recipes-bsp/u-boot/patches/experimental:"
SRC_URI_append = " file://0001-Generic-bootlimit-patch-without-U-Boot-boot-counter-.patch"
```

## The board specific part

The board specific part will need customizations specific to your board, but the
changes are relatively simple.

1. The first thing you need to do is to make sure that the board supports the
   `setexpr` command in the U-Boot scripting language. This will need the
   `CONFIG_CMD_SETEXPR` define to be set inside the board configuration in
   `include/configs`.

2. Second, any existing `CONFIG_BOOTCOUNT_LIMIT` and/or `CONFIG_BOOTCOUNT_ENV`
   defines in the configuration must be removed.

<!--AUTOVERSION: "meta-mender/blob/%"/ignore -->
For an example, take a look at [the patch provided for the `vexpress-qemu`
`MACHINE`
type](https://github.com/mendersoftware/meta-mender/blob/master/meta-mender-qemu/recipes-bsp/u-boot/patches/experimental/0002-Enable-custom-bootlimit-code-for-vexpress-qemu.patch?target=_blank).
You can try this patch by adding this to your `u-boot-my-fork.bb` or
`u-boot-my-fork.bbappend` file:

```bash
FILESEXTRAPATHS_prepend := "${THISDIR}/../../../meta-mender-qemu/recipes-bsp/u-boot/patches/experimental:"
SRC_URI_append_vexpress-qemu = " file://0002-Enable-custom-bootlimit-code-for-vexpress-qemu.patch"
```

Obviously this will require using the `vexpress-qemu` `MACHINE` type; it will
not work on another board.
