---
title: Bootloader support
taxonomy:
    category: docs
---

This section describes the support level of the two bootloaders that Mender supports, [GRUB](https://www.gnu.org/software//?target=_blank) and [U-Boot](http://www.denx.de/wiki/U-Boot?target=_blank). It is assumed that Yocto is the build system used to build the device images.

Below is a table listing the bootloader support using various device types and Yocto Project releases. All versions of the Mender client software will work with either of the two bootloaders.

<!--AUTOVERSION: "Older than 2.4 (%)"/ignore "2.4 (%)"/ignore "2.5 (%)"/ignore "2.6 (%) and later"/ignore-->
| *Feature \ Yocto Project version*        | *Older than 2.4 (rocko)* | *2.4 (rocko)*       | *2.5 (sumo)* | *2.6 (thud) and later* |
|------------------------------------------|--------------------------|---------------------|--------------|------------------------|
| GRUB integration for ARM systems         | No                       | No                  | Yes          | Yes, default           |
| GRUB integration for Flash/UBI devices   | No                       | No                  | No           | No                     |
| GRUB integration for x86/UEFI systems    | No                       | Yes, default        | Yes, default | Yes, default           |
| GRUB integration for x86/BIOS systems    | No                       | No                  | Yes          | Yes                    |
| U-Boot integration for ARM systems       | Yes, default             | Yes, default        | Yes, default | Yes                    |
| U-Boot integration for Flash/UBI devices | Partial<sup>1</sup>      | Partial<sup>1</sup> | Yes          | Yes                    |

<!--AUTOVERSION: "% branch and older"/ignore-->
<sup>1</sup> Flash/UBI support is possible in the rocko branch and older, but it is a lot of manual work and not streamlined, which is why the support is marked as partial. We recommend moving to a more recent branch if possible.

## Which one to pick

If you are just starting out, we recommend trying [GRUB integration]() first, if possible. We recommend moving to [U-Boot integration]() only if integration with GRUB is not possible or unsuccessful.

The main technical reason for using GRUB rather than U-Boot is that GRUB requires no patching to work with Mender, whereas U-Boot does. For most users this will be the path of least resistance.
