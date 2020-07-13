---
title: Provision a new device
taxonomy:
    category: docs
---

After you have obtained a Mender disk image, the image needs to be written to the storage of the
device.

## Prerequisites

### A disk image for the device storage

You need an image file to flash to the entire storage of the device. This section assumes that you
already have one. If not, please go back to [the overview](../overview) to find the best approach
for you.

Image files end with the three letters `img`, but not necessarily only those three letters. Common
suffixes are `.img`, `.uefiimg` and `.sdimg`. Sometimes the image is compressed in which case there
may be an additional `.gz`, `.xz` or `.zip` suffix. If the image is compressed, you need to
uncompress it first with one of the commands below:

```bash
# For gz compressed images.
gunzip <IMAGE-NAME>.img.gz

# For xz compressed images.
unxz <IMAGE-NAME>.img.xz

# For zip compressed images.
unzip <IMAGE-NAME>.img.zip
```


### A physical device to provision that uses SD cards

In this initial provisioning you will flash and overwrite everything on the given device storage.

There are several methods to flash storage, and the simplest case is if your device uses a SD
card. Currently, this is the approach we assume you take here, but the image file can be used to
flash any block device. See [Flash memory
types](../../03.Devices/02.Yocto-project/01.Partition-configuration/docs.md#flash-memory-types) for
a clarification of what is meant by block device in this context.


## Write the disk image to the SD card

!! Be careful! If you point to the wrong `<DEVICE>` when executing the command below, you risk
!! overwriting your workstation's local or connected storage devices.

You can write the image to the SD card using the following command:

```bash
sudo dd if=<PATH-TO-IMAGE>.img of=<DEVICE> bs=4M && sync
```

`<DEVICE>` depends on where your SD card is placed. Normally this would be something like
`/dev/mmcblk0` or `/dev/sdb`.  If you are unsure how to find the correct device, the Raspberry Pi
Foundation provides some nice references that can help you for
[Linux](https://www.raspberrypi.org/documentation/installation/installing-images/linux.md?target=_blank),
[Mac
OSX](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md?target=_blank)
and
[Windows](https://www.raspberrypi.org/documentation/installation/installing-images/windows.md?target=_blank).

The flashing may take a few minutes, depending on the size of the image.

!!! **Tip:** Many versions of `dd` support adding the `oflag=sync status=progress` arguments to get
!!! progress information during the flashing. To try it out, use the command `sudo dd
!!! if=<PATH-TO-IMAGE>.img of=<DEVICE> bs=4M oflag=sync status=progress` instead of the command
!!! above. Not all versions of `dd` support these arguments.
