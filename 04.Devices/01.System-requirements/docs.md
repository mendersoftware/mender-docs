---
title: System requirements
taxonomy:
    category: docs
---

##Yocto Project
Although it is possible to compile and install Mender independently, we have optimized the installation experience for those who build their Linux images using [Yocto Project](https://www.yoctoproject.org?target=_blank).

Mender's meta layer, [meta-mender](https://github.com/mendersoftware/meta-mender), has several branches that map to given releases of the Yocto Project (e.g. krogoth). However, note that Mender is tested and maintained against the **latest branch of the Yocto Project** only (krogoth at the time of writing). Older branches for the Yocto Project are still kept in [meta-mender](https://github.com/mendersoftware/meta-mender), but they might not work seamlessly as they are not continiously tested by Mender. We appreciate [community contributions](https://mender.io/community) to help maintain older branches! If you would like commercial support for a certain branch, please contact us at <contact@mender.io>.

##Device capacity
The client binaries, which are written in Go, are around 7 MiB in size. 

Our reference board, the [BeagleBone Black](http://beagleboard.org/bone?target=_blank), comes with a 1 GHz ARM Cortex-A8 processor, with 512 MiB of RAM. We use these boards in our continuous integration process.

##Bootloader support
Mender integrates with the bootloader of the device. Currently we support the popular [U-Boot](http://www.denx.de/wiki/view/DULG/UBootBootCountLimit?target=_blank). Besides any special configuration to support the device, U-Boot needs to be compiled and used with the following features:

* [Boot Count Limit](http://www.denx.de/wiki/view/DULG/UBootBootCountLimit?target=_blank). It enables specific actions to be triggered when the boot process fails a certain amount of attempts.
* ext2/3/4 load support (specifically: the file system type of the rootfs). U-Boot needs this capability because the kernel will be stored there.

Support for modifying U-Boot variables from userspace is also required so that fw_printenv/fw_setenv utilities are available in userspace. These utilities can be 
[compiled from U-Boot sources](http://www.denx.de/wiki/view/DULG/HowCanIAccessUBootEnvironmentVariablesInLinux?target=_blank) and are part of U-Boot.

Please see [Integrating with U-Boot](../Integrating-with-U-Boot) for more information.

##Kernel support
While Mender itself does not have any specific kernel requirements beyond what a normal Linux kernel provides, it relies on systemd, which does have one such requirement: The `CONFIG_FHANDLE` feature must be enabled in the kernel. The symptom if this feature is unavailable is that systemd hangs during boot looking for device files.

If you solely want to run Mender manually, you can avoid this dependecy by [disabling Mender as a system service](../Customizations#disabling-mender-as-a-system-service) .

##Partition layout
Please see [Partition layout](../Partition-layout/).
