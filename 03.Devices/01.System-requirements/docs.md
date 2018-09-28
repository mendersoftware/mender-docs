---
title: System requirements
taxonomy:
    category: docs
---

!!! Mender has four reference boards already integrated: [Raspberry Pi 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b?target=_blank), [BeagleBone Black](https://beagleboard.org/black?target=_blank) and two virtual devices (`qemux86-64` and `vexpress-qemu`). If you would like assistance supporting your device and OS, please refer to the [commercial device support offering](https://mender.io/product/board-support?target=_blank).

##Device capacity
The client binaries are about 7 MB in size, or about 4 MB when debug symbols are stripped (using the `strip` tool). This includes all dependencies for the client, such as the http, TLS, and JSON libraries.

##Bootloader support
To support atomic rootfs rollback, Mender integrates with the bootloader of the device. Currently Mender supports [GRUB](https://www.gnu.org/software/grub/?target=_blank) and [U-Boot](http://www.denx.de/wiki/U-Boot?target=_blank). See [Yocto bootloader support](yocto/bootloader-support) or [Debian bootloader support](debian-family/bootloader-support) for more information.

##Kernel support
While Mender itself does not have any specific kernel requirements beyond what a normal Linux kernel provides, it relies on systemd, which does have one such requirement: The `CONFIG_FHANDLE` feature must be enabled in the kernel. The symptom if this feature is unavailable is that systemd hangs during boot looking for device files.

If you [run the Mender client in standalone mode](../../architecture/overview#modes-of-operation), you can avoid this dependency by [disabling Mender as a system service](../../artifacts/image-configuration#disabling-mender-as-a-system-service) .

##Partition layout
Please see [Partition layout](../partition-layout/).

##Correct clock
Certificate verification requires the device clock to be running correctly at all times.
Make sure to either have a reliable clock or use network time synchronization.
Note that the default setup of systemd will use network time
synchronization to maintain the clock in a running system. This may
take a few minutes to stabilize on system boot so it is possible
to have a few connection rejections from the server until this process
is complete and the time is correct. Please see [certificate troubleshooting](../../troubleshooting/mender-client#certificate-expired-or-not-yet-valid) for more information about the symptoms of this issue.

If your device does not have an active internet connection, then systemd
will be unable to configure the system time as it will be unable to connect
to the network time servers. In this case you will need to arrange other
methods to set a proper system time. Many standard Linux features can be
used for this. If your system includes a real-time clock chip, that will maintain the time
across power down situations and the network connectivity needs of systemd
will only be relevant on the system boots before the RTC is properly
initialized.

Before the time is set properly, either by systemd or the RTC, the time will
default to the [Unix Epoch](https://en.wikipedia.org/wiki/Unix_time).  Note
that the Mender client connections will be rejected by the server until this
situation is resolved.
