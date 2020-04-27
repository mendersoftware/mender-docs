---
title: Provisioning a new device
taxonomy:
    category: docs
---

After downloading one of the Mender demo images,
[building a Mender Yocto Project image](../yocto-project/building) or [converting existing debian images](../debian-family)
for the first time, you need to write the storage image to
the flash of the device.

!!! The Mender `sdimg` generator, which is part of [meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank), generates disk images with exactly four partitions: one boot, two rootfs and one data partition. It is intended as a reference implementation for testing and simple production use. For more advanced use cases, please refer to your board's tools for generating disk images and flashing storage, such as `imx-loader`, `mfg-tool`, and `tegrarcm`.

## Prerequisites

### A disk image for the device storage

You need an image file to flash to the entire storage of the
device. `meta-mender-core` creates these files with a `.sdimg`
suffix, so they are easy to recognize. This file contains
all the partitions of the given storage device, as
described in [Partition layout](../../devices/general-system-requirements#partition-layout).


### A physical device to provision that uses SD cards

In this initial provisioning you will flash and overwrite everything
on the given device storage.

There are several methods to flash storage, and the simplest
case is if your device uses a SD card. Currently, this is the approach
we assume you take here, but the same `.sdimg` file can be used
to flash any block device. See
[Flash memory types](../../devices/yocto-project/partition-configuration#flash-memory-types)
for a clarification of what is meant by block device in this context.


## Write the disk image to the SD card

!! Be careful! If you point to the wrong `<DEVICE>` when executing the command below, you risk overwriting your workstation's local or connected storage devices.

Assuming you are in the same directory as your `.sdimg`, you can write the sdimg to the SD card using the following command:

```bash
sudo dd if=<PATH-TO-IMAGE>.sdimg of=<DEVICE> bs=1M && sudo sync
```

This may take a few minutes, depending on the size of the image.

!!! &lt;DEVICE&gt; depends on where your SD card is placed. Normally this would be something like  `/dev/mmcblk0` or `/dev/sdb`.  If you are unsure how to find the correct device, the Raspberry Pi Foundation provides some nice references that can help you for [Linux](https://www.raspberrypi.org/documentation/installation/installing-images/linux.md?target=_blank), [Mac OSX](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md?target=_blank), [Windows](https://www.raspberrypi.org/documentation/installation/installing-images/windows.md?target=_blank).
