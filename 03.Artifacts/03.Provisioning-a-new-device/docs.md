---
title: Provisioning a new device
taxonomy:
    category: docs
---

After downloading one of the Mender demo images or
[Building a Mender Yocto Project image](../Building-Mender-Yocto-image)
for the first time, you need to write the storage image to
the flash of the device.


## Prerequisites

### A disk image for the device storage

You need an image file to flash to the entire storage of the
device. `meta-mender` creates these files with a `.sdimg`
suffix, so they are easy to recognize. This file contains
all the partitions of the given storage device, as
described in [Partition layout](../../Devices/Partition-layout).


### A physical device to provision that uses SD cards

In this initial provisioning you will flash and overwrite everything
on the given device storage.

There are several methods to flash storage, and the simplest
case is if your device uses a SD card. Currently, this is the approach
we assume you take here, but the same `.sdimg` file can be used
to flash any block device. See
[Flash memory types](../../Devices/Partition-layout#flash-memory-types)
for a clarification of what is meant by block device in this context.


## Write the disk image to the SD card

!! Be careful! If you point to the wrong `<DEVICE>` when executing the command below, you risk overwriting your workstation's local or connected storage devices.

Assuming you are in the same directory as your `.sdimg`, you can write the sdimg to the SD card using the following command:

```
sudo dd if=<PATH-TO-IMAGE>.sdimg of=<DEVICE> bs=1M && sudo sync
```

!!! &lt;DEVICE&gt; depends on where your SD card is placed. Normally this would be something like  `/dev/mmcblk0` or `/dev/sdb`.  If you are unsure how to find the correct device, the Raspberry PI Foundation provide some nice references that can help you for [Linux](https://www.raspberrypi.org/documentation/installation/installing-images/linux.md?target=_blank), [Mac OSX](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md?target=_blank), [Windows](https://www.raspberrypi.org/documentation/installation/installing-images/windows.md?target=_blank).
