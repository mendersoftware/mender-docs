---
title: Overview
taxonomy:
    category: docs
---


<!--AUTOVERSION: "mender-convert version %"/mender-convert-->
<!-- See MEN-4983 -->
!! Be careful when running `apt upgrade` on a device with Mender Operating System updates enabled. Integration
!! with `apt upgrade` (through the `grub.d` framework) is only implemented for x86 as of
!! mender-convert version 4.2.0. For ARM and other non-x86 architectures, always update single
!! applications only, because running `apt upgrade` may brick your device!. If you need to run `apt
!! upgrade`, do it on a pristine system without Mender installed, and then [convert it to a Mender
!! image](../../04.Operating-System-updates-Debian-family/02.Convert-a-Mender-Debian-image/docs.md)
!! afterwards. We may lift this restriction in the future.


## General requirements

Below are a number of general requirements for using Mender.


### Device capacity

The client binaries are about 7 MB in size, or about 4 MB when debug symbols are
stripped (using the `strip` tool). This includes most of the dependencies for
the client, such as the http, TLS, and JSON libraries.

The client depends on the LZMA library for Artifact compression, which is
present in most Linux distributions, including those based on the Debian family.


### Bootloader support

To support atomic rootfs rollback, Mender integrates with the bootloader of the device. Currently
Mender supports [GRUB](https://www.gnu.org/software/grub/?target=_blank) and
[U-Boot](http://www.denx.de/wiki/U-Boot?target=_blank). Some boards may require a board integration;
visit [Mender Hub](https://hub.mender.io/?target=_blank) to find board integrations that community
members have submitted. If no board integration is available for your board, we recommend you
try it without any integration, as GRUB may work without additional configuration on both ARM and x86.


### Partition layout

In order to support robust rollback, Mender requires the device to have a certain partition layout.
You need at least four different partitions:
* one boot partition, containing the U-Boot bootloader and its environment
* two partitions for storing the root filesystem and kernel. The kernel image file, zImage, and any device tree binary should go into the `/boot` directory.
* one for persistent data

One of the rootfs and kernel partitions will be the *active* partition, from which the kernel and rootfs will boot.
The other, called the *inactive* partition, will be used by the update mechanism to write the updated image.
After an update they switch roles.

The persistent data partition stores data that must persist through an update.

Below is a sample partition layout:

![Mender client partition layout](mender_client_partition_layout.png)


### Correct clock

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

Before the time is set properly, either by systemd or the RTC, the time will
default to the [Unix Epoch](https://en.wikipedia.org/wiki/Unix_time?target=_blank). Note
that the Mender Server will reject client connections until this
situation is resolved.


### Unsupported build systems

Mender has official support for [the Yocto Project build system](../../05.Operating-System-updates-Yocto-Project/chapter.md) and [binary OS images based on the Debian family](../chapter.md). It is possible to adapt to other build systems. Please see [this community post](https://hub.mender.io/t/mender-from-scratch?target=_blank) for a concrete description.


## Mender Hub community

For help from the community, as well as links to board integrations, visit [Mender
Hub](https://hub.mender.io/?target=_blank).
