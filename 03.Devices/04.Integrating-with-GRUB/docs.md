---
title: Integrating with GRUB
taxonomy:
    category: docs
---

This section describes the Yocto configuration needed to integrate with the [GRUB bootloader](https://www.gnu.org/software/grub/?target=_blank).

# Requirements

In order to integrate with GRUB, your system must boot using the UEFI standard. The traditional BIOS based boot procedure is not supported.

# Enabling GRUB

You can enable Mender integration with GRUB by turning on the `mender-grub` feature using `MENDER_FEATURES_ENABLE`. For instance, in your `local.conf`:

```
MENDER_FEATURES_ENABLE_append = " mender-grub"
```

!!! If the architecture is x86 or x86-64, and the `mender-full` class is inherited, then the `mender-grub` feature is already on by default. See [the documentation on features](../../artifacts/image-configuration/features) for more information.
