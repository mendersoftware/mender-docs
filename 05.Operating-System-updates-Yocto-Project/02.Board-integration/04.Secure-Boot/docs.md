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

Secure Boot is architecturally independent of Mender. We recommend implementing
and verifying Secure Boot on your platform before integrating the Mender update
process.

While Mender does not provide pre-validated configurations for specific Secure
Boot implementations (e.g., custom U-Boot signatures), there are no known
architectural limitations. If your bootloader and kernel are correctly signed,
Mender’s update mechanism will function as intended.

The primary consideration is your build system. Because Secure Boot signatures
are embedded within the binaries, the Mender Client will deploy them regardless
of their signature status. However, your image-building process must be
configured to sign all artifacts that Mender introduces into the boot chain.
Please note that while the Mender Client is compatible with Secure Boot, not all
Mender image-building tools support automated signing out of the box.

For the Yocto family of operating system images,
[meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank) is the Yocto layer used
to enable building of Mender compatible dual rootfs images. For the most part, signing for Secure
Boot compliant images happens independently from Mender, and Mender will just use the signed
components without "getting in the way" of Secure Boot.

However, some things are worth noting regarding the current implementation:

* For ARM systems that use [GRUB integration](../02.Bootloader-support/01.GRUB) (the default):

    * If the system previously used U-Boot only, then Mender's Yocto layer introduces either the
      `grub-efi` or `grub-efi-mender-precompiled` recipe into the build. Make sure that the binary
      produced in either of these recipes is
      signed.

    * On ARM, U-Boot is usually used as a UEFI provider which loads GRUB. U-Boot therefore needs to
      have UEFI Secure Boot built in (`CONFIG_EFI_SECURE_BOOT` build option).
