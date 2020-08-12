---
title: GRUB
taxonomy:
    category: docs
---

This section describes the Yocto configuration needed to integrate with the [GRUB bootloader](https://www.gnu.org/software/grub/?target=_blank).

## Enabling GRUB

If GRUB integration is not already enabled, you can enable it by adding the snippet below to your build configuration. For instance, in your `local.conf`:

```
MENDER_FEATURES_ENABLE_append = " mender-grub mender-image-uefi"
MENDER_FEATURES_DISABLE_append = " mender-uboot mender-image-sd"
```

See [the documentation on features](../../../04.Image-customization/01.Features/docs.md) for more information.


## BIOS based systems

If using GRUB, Mender by default assumes that the system is using the UEFI boot standard. For systems using BIOS based booting, the `mender-bios` feature should also be enabled using `MENDER_FEATURES_ENABLE`.
