---
title: Overview
taxonomy:
    category: docs
    label: reference
---

Mender has official support for binary-OS images based on Debian. The general
approach for using such an image with Mender is through
[Mender-convert](https://github.com/mendersoftware/mender-convert), which is a
tool to automatically add Mender to a binary-OS image. For more information,
have a look at
[Mender-Hub](https://hub.mender.io/c/board-integrations/debian-family/11) for
the specific boards that have already been integrated.


# General requirements

## Device capacity

The client binaries are about 7 MB in size, or about 4 MB when debug symbols are
stripped (using the `strip` tool). This includes most of the dependencies for
the client, such as the http, TLS, and JSON libraries.

The client depends on the LZMA library for Artifact compression, which is
present in most Linux distributions, including those based on the Debian family.

## Bootloader support

To support atomic rootfs rollback, Mender integrates with the bootloader of the
device. Currently Mender supports
[GRUB](https://www.gnu.org/software/grub/?target=_blank) and
[U-Boot](http://www.denx.de/wiki/U-Boot?target=_blank). The bootloader
installation, features and requirements vary depending on the target OS in use.
Please see the [Debian bootloader support](../debian-family#bootloader-support)
for more information.

## Kernel support

While Mender itself does not have any specific kernel requirements beyond what a
normal Linux kernel provides, it relies on systemd, which does have one such
requirement: The `CONFIG_FHANDLE` feature enabled in the kernel. If this feature
is unavailable systemd hangs during boot looking for device files.

If you [run the Mender client in standalone
mode](../../overview/overview#modes-of-operation), you can avoid this
dependency by [disabling Mender as a system
service](../../system-updates/yocto-project/image-customization#disabling-mender-as-a-system-service).

## Partition layout

In order to support robust rollback, Mender requires the device to have a
certain partition layout. Mender needs at least four different partitions:
* One boot partition, containing the U-Boot bootloader and its environment.
* Two partitions for storing the root file system and kernel. The kernel image
  file, zImage, and any device tree binary are in the /boot directory.
* One for persistent data.

One of the rootfs and kernel partitions is the *active* partition, from which
the kernel and rootfs boots. The other is the *inactive* partition. The update
mechanism uses this to write the updated image to. An update swaps their roles.

Data that requires preservation across updates are located on the persistent
data partition. 

Below is a sample partition layout:

![Mender client partition layout](mender_client_partition_layout.png)

## Correct clock

Certificate verification requires the device clock to be running correctly at
all times. Make sure to either have a reliable clock or use network time
synchronization. Note that the default setup of systemd will use network time
synchronization to maintain the clock in a running system. This may take a few
minutes to stabilize on system boot so it is possible to have a few connection
rejections from the server until this process is complete and the time is
correct. Please see [certificate
troubleshooting](../../troubleshooting/mender-client#certificate-expired-or-not-yet-valid)
for more information about the symptoms of this issue.

If your device does not have an active internet connection, then systemd will be
unable to configure the system time as it will be unable to connect to the
network time servers. In this case you will need to arrange other methods to set
a proper system time. Many standard Linux features can are available for this.
If your system includes a real-time clock chip, that will maintain the time
across power down situations and the network connectivity needs of systemd will
only be relevant on the system boots before the RTC is properly initialized.

Before the time is set properly, either by systemd or the RTC, the time will
default to the [Unix
Epoch](https://en.wikipedia.org/wiki/Unix_time?target=_blank). Note that the
Mender client connections gets rejected by the server until this situation is
resolved.

### Unsupported build systems

Mender has official support binary OS images based on the Debian family. It is
possible to adapt to other build systems. Please see [this blog
post](https://mender.io/blog/porting-mender-to-a-non-yocto-build-system?target=_blank)
for an example (note that some of Mender's needs may have changed since the blog
post was made).
