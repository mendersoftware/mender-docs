---
title: Overview
taxonomy:
    category: docs
---


## Yocto Project release

Mender's meta layer, [meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank), has
several branches that map to given releases of the Yocto Project. However, note that Mender is
tested and maintained against the [**latest LTS branch of the Yocto
Project**](https://wiki.yoctoproject.org/wiki/Releases?target=_blank) only.

Older branches for the Yocto Project are still kept in
[meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank), but they might not work
seamlessly as they are not continuously tested by Mender. If you need support for older branches we
recommend posting your efforts and issues on [mender hub](https://hub.mender.io/c/board-integrations/6).
If you're interested in commercial support [read more here](https://mender.io/support-and-services/board-integration).



! For compatibility reasons, not all branches for the Yocto Project install the latest client by
! default. To make sure the latest client is installed, and you have access to all the latest
! features, see [the `PREFERRED_VERSION` setting when configuring the
! Yocto build](../03.Build-for-demo/docs.md#configuring-the-build).


## Device capacity

The client binaries are about 7 MB in size, or about 4 MB when debug symbols are
stripped (using the `strip` tool). This includes most of the dependencies for
the client, such as the http, TLS, and JSON libraries.

The client depends on the LZMA library for Artifact compression, which is
present in most Linux distributions, including those based on the Yocto Project.


## Bootloader support

To support atomic rootfs rollback, Mender integrates with the bootloader of the device. Currently
Mender supports [GRUB](https://www.gnu.org/software/grub/?target=_blank) and
[U-Boot](http://www.denx.de/wiki/U-Boot?target=_blank). Please see the [Yocto bootloader
support](../02.Board-integration/02.Bootloader-support/docs.md) for more information.


## Kernel support
While Mender itself does not have any specific kernel requirements beyond what a normal Linux kernel provides, it relies on systemd, which does have one such requirement: The `CONFIG_FHANDLE` feature must be enabled in the kernel. The symptom if this feature is unavailable is that systemd hangs during boot looking for device files.

If you [run the Mender Client in standalone mode](../../02.Overview/01.Introduction/docs.md#client-modes-of-operation), you can avoid this dependency by [disabling Mender as a system service](../05.Customize-Mender/docs.md#disabling-mender-as-a-system-service).


## Partition layout

In order to support robust rollback, Mender requires the device to have a certain partition layout.
At least four different partitions are needed:
* one boot partition, containing the U-Boot bootloader and its environment
* two partitions for storing the root filesystem and kernel. The kernel image file, zImage, and any device tree binary should be stored in directory `/boot`.
* one for persistent data

Mender marks one of the root filesystem partitions as *active*, making the partition the boot target.
The other, *inactive* partition, holds the previous root filesystem update. The client may either overwrite
the inactive partition on a new update or roll back if the active partition does not boot.
On a successful update, the partitions swaps roles.

The persistent data partition stores data requiring preservation through Operating System updates.

The following figure illustrates an example partition layout:

![Mender Client partition layout](mender_client_partition_layout.png)


## Correct clock

Certificate verification requires the device clock to be running correctly at all times.
Make sure to either have a reliable clock or use network time synchronization.
Note that the default setup of systemd will use network time
synchronization to maintain the clock in a running system. This may
take a few minutes to stabilize on system boot so it is possible
to have a few connection rejections from the server until this process
is complete and the time is correct. Please see [certificate troubleshooting](../../301.Troubleshoot/03.Mender-Client/docs.md#certificate-expired-or-not-yet-valid) for more information about the symptoms of this issue.

If your device does not have an active internet connection, then systemd
will be unable to configure the system time as it will be unable to connect
to the network time servers. In this case you will need to arrange other
methods to set a proper system time. Many standard Linux features can be
used for this. If your system includes a real-time clock chip, that will maintain the time
across power down situations and the network connectivity needs of systemd
will only be relevant on the system boots before the RTC is properly
initialized.

Note that on startup, the system initializes the time to the 
[Unix Epoch](https://en.wikipedia.org/wiki/Unix_time?target=_blank), before
either systemd or the RTC corrects it, which implies that the server rejects all
incoming TLS connections from the client until this happens.


## Unsupported build systems

Mender has official support for the Yocto build system and [binary OS images based on the Debian family](../../04.Operating-System-updates-Debian-family/chapter.md). It is possible to adapt to other build systems. Please see [this community post](https://hub.mender.io/t/mender-from-scratch?target=_blank) for a concrete description.


## Mender Hub community

For help from the community, as well as links to board integrations, visit [Mender
Hub](https://hub.mender.io/?target=_blank).
