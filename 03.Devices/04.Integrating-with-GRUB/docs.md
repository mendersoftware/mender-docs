---
title: Integrating with GRUB
taxonomy:
    category: docs
---

This section describes the Yocto configuration needed to integrate with the [GRUB bootloader](https://www.gnu.org/software/grub/?target=_blank), which is most commonly used on x86 based systems.

## Enabling GRUB

You can enable Mender integration with GRUB by turning on the `mender-grub` feature using `MENDER_FEATURES_ENABLE`. For instance, in your `local.conf`:

```
MENDER_FEATURES_ENABLE_append = " mender-grub"
```

!!! If the architecture is x86 or x86-64, and the `mender-full` class is inherited, then the `mender-grub` feature is already on by default. See [the documentation on features](../../artifacts/image-configuration/features) for more information.

## BIOS based systems

If using GRUB, Mender by default assumes that the system is using the UEFI boot standard. For systems using BIOS based booting, the `mender-bios` feature should also be enabled using `MENDER_FEATURES_ENABLE`.

!!! The `mender-bios` feature was introduced in the meta-mender sumo branch, corresponding to the Yocto Project 2.5 sumo release, and is not available in earlier branches.
