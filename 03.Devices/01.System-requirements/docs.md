---
title: System requirements
taxonomy:
    category: docs
---

##Yocto Project
Although it is possible to compile and install Mender independently, we have optimized the installation experience for those who build their Linux images using [Yocto Project](https://www.yoctoproject.org?target=_blank).

Mender's meta layer, [meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank), has several branches that map to given releases of the Yocto Project. However, note that Mender is tested and maintained against the **latest release branch of the Yocto Project** only. Older branches for the Yocto Project are still kept in [meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank), but they might not work seamlessly as they are not continuously tested by Mender. We appreciate [community contributions](https://mender.io/community?target=_blank) to help maintain older branches!

### Other build systems

Mender has no official support for other build systems. However, by following the right steps, it is possible to adapt other build systems to Mender's needs. Please see [this blog post](https://mender.io/blog/porting-mender-to-a-non-yocto-build-system) for an example (note that some of Mender's needs may have changed since the blog post was made).

##Device capacity
The client binaries, which are written in Go, are around 7 MiB in size. 

Our physical reference device, the [BeagleBone Black](https://beagleboard.org/black?target=_blank), comes with a 1 GHz ARM Cortex-A8 processor, with 512 MiB of RAM. Mender also has a virtual QEMU-based reference device using the `vexpress-qemu` machine type. We use both these devices in our continuous integration process so they are well supported.

##Bootloader support
To support atomic rootfs rollback, Mender integrates with the bootloader of the device. Currently Mender supports [U-Boot](http://www.denx.de/wiki/U-Boot?target=_blank).
As Mender relies on the `CONFIG_BOOTCOUNT_ENV` feature of U-Boot, which was [introduced in October 2013](http://lists.denx.de/pipermail/u-boot/2013-October/165484.html?target=_blank), Mender currently recommends **U-Boot v2014.07 or newer**. If you have an older version of U-Boot, it is possible to apply some extra patches to make this work. Please see the section about [U-Boot versions without BOOTLIMIT support](../integrating-with-u-Boot/u-boot-versions-without-BOOTLIMIT-support) for more information.


Besides any special configuration to support the device, U-Boot needs to be compiled and used with the following features:

* [Boot Count Limit](http://www.denx.de/wiki/view/DULG/UBootBootCountLimit?target=_blank). It enables specific actions to be triggered when the boot process fails a certain amount of attempts.
* ext2/3/4 load support (specifically: the file system type of the rootfs). U-Boot needs this capability because the kernel will be stored there.

Support for modifying U-Boot variables from user space is also required so that fw_printenv/fw_setenv utilities (from u-boot-fw-utils) are available in user space. These utilities can be 
[compiled from U-Boot sources](http://www.denx.de/wiki/view/DULG/HowCanIAccessUBootEnvironmentVariablesInLinux?target=_blank) and are part of U-Boot.

Please see [Integrating with U-Boot](../integrating-with-u-boot) for more information.

##Kernel support
While Mender itself does not have any specific kernel requirements beyond what a normal Linux kernel provides, it relies on systemd, which does have one such requirement: The `CONFIG_FHANDLE` feature must be enabled in the kernel. The symptom if this feature is unavailable is that systemd hangs during boot looking for device files.

If you [run the Mender client in standalone mode](../../architecture/overview#modes-of-operation), you can avoid this dependency by [disabling Mender as a system service](../../artifacts/image-configuration#disabling-mender-as-a-system-service) .

##Partition layout
Please see [Partition layout](../partition-layout/).

##Correct clock
Certificate verification requires the device clock to be running correctly at all times.
Make sure to either have a reliable clock or use network time synchronization.
Please see [certificate troubleshooting](../../troubleshooting/mender-client#certificate-expired-or-not-yet-valid) for more information about the symptoms of this issue.
