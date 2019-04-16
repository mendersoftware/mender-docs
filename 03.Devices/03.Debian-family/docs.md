---
title: Debian family
taxonomy:
    category: docs
---

This page describes the requirements for Mender when integrated with the Debian
family target OS images such as [Debian](https://www.debian.org/?target=_blank),
[Ubuntu](https://www.ubuntu.com/?target=_blank) and
[Raspbian](https://www.raspberrypi.org/downloads/raspbian/?target=_blank).

For these devices, `mender-convert` is used to perform Mender integration.

`mender-convert` will take care of the full integration, which includes:
* Modification of the original partition layout to fulfill Mender needs
* Integration with a compatible bootloader (see below for details)
* Install the Mender client and its configuration into the image.

##Bootloader support

### GRUB

[mender-convert](https://github.com/mendersoftware/mender-convert?target=_blank)
builds GRUB as second stage bootloader for Debian on Beaglebone. It is built
from the [official
repository](https://www.gnu.org/software/grub/grub-download.html?target=_blank).
Mender does not require any patches for GRUB and should be built with EFI
platform support.

### U-Boot

[mender-convert](https://github.com/mendersoftware/mender-convert?target=_blank)
provides for building and installing [patched
U-Boot](https://github.com/mendersoftware/uboot-mender?target=_blank) for
Raspbian. Currently only a patched U-Boot is supported by Mender on Raspberry Pi
3.

## Mender integration

The procedure to be followed to integrate Mender is the same as for to create a
Mender Artifact for Debian family OSes. Refer to [Debian family Artifact
creation](../../artifacts/debian-family) for step by step instructions.
