---
title: System requirements
taxonomy:
    category: docs
---

##Yocto Project
Although it is possible to compile and install Mender independently, we have optimized the installation experience for those who build their Linux images using [Yocto Project](https://www.yoctoproject.org?target=_blank).

Mender's meta layer, [meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank), has several branches that map to given releases of the Yocto Project (e.g. krogoth). However, note that Mender is tested and maintained against the **latest branch of the Yocto Project** only (krogoth at the time of writing). Older branches for the Yocto Project are still kept in [meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank), but they might not work seamlessly as they are not continiously tested by Mender. We appreciate [community contributions](https://mender.io/community?target=_blank) to help maintain older branches! If you would like commercial support for a certain branch, please contact us at <contact@mender.io>.

##Device capacity
The client binaries, which are written in Go, are around 7 MiB in size. 

Our reference board, the [BeagleBone Black](http://beagleboard.org/bone?target=_blank), comes with a 1 GHz ARM Cortex-A8 processor, with 512 MiB of RAM. We use these boards in our continuous integration process.

##Bootloader support
To support atomic rootfs rollback, Mender integrates with the bootloader of the device. Currently Mender supports [U-Boot](http://www.denx.de/wiki/U-Boot?target=_blank).
As Mender relies on the `CONFIG_BOOTCOUNT_ENV` feature of U-Boot, which was [introduced in October 2013](http://lists.denx.de/pipermail/u-boot/2013-October/165484.html?target=_blank), Mender currently requires **U-Boot v2014.01 or newer**. If you have an older version of U-Boot, it should be straightforward to backport or implement this feature. Please [reach out on the Mender mailing list](https://groups.google.com/a/lists.mender.io/forum?target=_blank#!forum/mender).


Besides any special configuration to support the device, U-Boot needs to be compiled and used with the following features:

* [Boot Count Limit](http://www.denx.de/wiki/view/DULG/UBootBootCountLimit?target=_blank). It enables specific actions to be triggered when the boot process fails a certain amount of attempts.
* ext2/3/4 load support (specifically: the file system type of the rootfs). U-Boot needs this capability because the kernel will be stored there.

Support for modifying U-Boot variables from userspace is also required so that fw_printenv/fw_setenv utilities (from u-boot-fw-utils) are available in userspace. These utilities can be 
[compiled from U-Boot sources](http://www.denx.de/wiki/view/DULG/HowCanIAccessUBootEnvironmentVariablesInLinux?target=_blank) and are part of U-Boot.

Please see [Integrating with U-Boot](../Integrating-with-U-Boot) for more information.

##Kernel support
While Mender itself does not have any specific kernel requirements beyond what a normal Linux kernel provides, it relies on systemd, which does have one such requirement: The `CONFIG_FHANDLE` feature must be enabled in the kernel. The symptom if this feature is unavailable is that systemd hangs during boot looking for device files.

If you [run the Mender client in standalone mode](../../Architecture/overview#modes-of-operation), you can avoid this dependency by [disabling Mender as a system service](../../Artifacts/Build-customizations#disabling-mender-as-a-system-service) .

##Partition layout
Please see [Partition layout](../Partition-layout/).
