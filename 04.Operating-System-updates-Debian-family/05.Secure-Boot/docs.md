---
title: Secure Boot
taxonomy:
    category: docs
---

## Introduction

[Secure Boot](https://en.wikipedia.org/wiki/UEFI#Secure_Boot?target=_blank) is a service offered by
the [UEFI boot firmware](https://en.wikipedia.org/wiki/UEFI?target=_blank) which verifies that all
executable code loaded during the boot process is
signed by a trusted key. This ensures that none of
the privileged software on the device has been
tampered with. In a Linux system, this encompasses
the boot loader, the kernel, and device drivers.

! Note that Secure Boot does not provide filesystem integrity, only boot loader, kernel and device
! driver (kernel module) integrity. If you are interested in filesystem integrity checking, the
! [dm-verity](https://www.kernel.org/doc/html/latest/admin-guide/device-mapper/verity.html?target=_blank)
! framework may be what you are looking for.

## Support

The signatures used by Secure Boot are embedded in the binary files themselves, and as such, are
largely independent of the Mender Client; it will just deploy whatever files the update contains,
with or without Secure Boot signatures. This means that in general, if a system was Secure Boot
compliant before introducing the Mender Client, it will keep being compliant after introducing it.

However, how you build the image affects whether it is Secure Boot compliant or not. Although the
Mender Client supports Secure Boot, not all of Mender's image building facilities do.

For the Debian family of operating system images,
[mender-convert](https://github.com/mendersoftware/mender-convert?target=_blank) is the tool used to
convert an upstream image to a Mender compatible dual rootfs image. Certain criteria need to be
met for this conversion to support Secure Boot.

* The architecture must be x86 (either 32-bit or 64-bit)
* The system must boot using UEFI.
* The `MENDER_GRUB_D_INTEGRATION` feature must be
  enabled in the mender-convert
  configuration. Normally this is auto-detected, but you can force it on by setting
  `MENDER_GRUB_D_INTEGRATION=y` somewhere in [the
  configuration](../02.Convert-a-Mender-Debian-image/01.Customization).
* Image must already be Secure Boot compliant. See [signing](#signing) below.
* The `grub-efi-amd64-signed` and `shim-signed` packages must be
  installed prior to the conversion.

## Signing

Mender-convert only supports images that are already Secure Boot compliant before the conversion,
and this requires that all relevant files are already signed. Upstream Debian and Ubuntu images are
already Secure Boot compliant when you download them, so no they need no further action to be
employed. However, sometimes it can be desirable to use custom keys to sign the image. See the table
below for some important security properties of each approach.

| **Property**                                                                          | **OS vendor keys** | **Custom keys** |
|---------------------------------------------------------------------------------------|--------------------|-----------------|
| Protects against [rootkits](https://en.wikipedia.org/wiki/Rootkit?target=_blank)      | ✔                  | ✔               |
| Prevents installation of different kernel and module versions from the same OS vendor | ✘                  | ✔               |
| Prevents installation of custom-built (hacked) kernels and modules                    | ✔                  | ✔               |
| Works with standard UEFI firmware keys<sup>1</sup>                                    | ✔                  | ✘               |

!!! <sup>1</sup> Most computers come with Microsoft's Root public key installed in the UEFI
!!! firmware. With custom keys, there needs to be a process in place during provisioning of each
!!! device, to remove this key and install a custom key in its place.

### Custom keys

To use custom keys, consider following something like [Ubuntu's "How to sign things for Secure
Boot" guide](https://ubuntu.com/blog/how-to-sign-things-for-secure-boot).

!! If you start with a pre-built image and follow above the guide to sign various components, it is
!! **very important** that you build the shim, GRUB, Linux kernel, and Linux kernel modules from
!! scratch! Using existing pre-built components from upstream vendors will result in an **insecure**
!! system, and you will not gain the additional security properties listed above.

Note that Secure Boot compliance is a complex field, and Northern.tech can not guarantee that the
guide above will result in a secure system. Consider employing a domain expert on Secure Boot and
have them validate the image building and signing process.
