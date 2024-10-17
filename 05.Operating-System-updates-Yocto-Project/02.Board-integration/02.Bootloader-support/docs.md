---
title: Bootloader support
taxonomy:
    category: docs
---

This section describes the support level of the two bootloaders that Mender supports, [GRUB](https://www.gnu.org/software//?target=_blank) and [U-Boot](http://www.denx.de/wiki/U-Boot?target=_blank).

By default, Mender uses GRUB to boot, and this is the recommended bootloader to use, even on platforms that ordinarily use U-Boot. However, U-Boot can be used in cases where using GRUB is not possible or unsuccessful.

!!! On platforms using [Raw flash](../03.Raw-flash/docs.md) (UBI), it is only possible to use U-Boot.

The main technical reason for using GRUB rather than U-Boot is that GRUB requires no patching to work with Mender, whereas U-Boot does. For most users this will be the path of least resistance.

Please see the sub sections for [GRUB](01.GRUB/docs.md) and [U-Boot](02.U-Boot/docs.md) for more details.

## Compatibility

Below is a table listing the bootloader support using various device types. All versions of the Mender Client software, as well as the rootfs-image update modules, will work with either of the two bootloaders.

| *Feature*                                | *Supported*  |
|------------------------------------------|--------------|
| GRUB integration for ARM systems         | Yes, default |
| GRUB integration for Flash/UBI devices   | No           |
| GRUB integration for x86/UEFI systems    | Yes, default |
| GRUB integration for x86/BIOS systems    | Yes          |
| U-Boot integration for ARM systems       | Yes          |
| U-Boot integration for Flash/UBI devices | Yes          |
