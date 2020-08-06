---
title: Provisioning a new device
taxonomy:
    category: docs
---

After [building a Mender Yocto Project image](../../05.System-updates-Yocto-Project/03.Build-for-demo/docs.md#building-the-image), you need to write the disk
image to the flash of the device.

Depending on the build configuration the disk image will have one of the following
suffixes: `sdimg`, `uefiimg`, `biosimg` or `gptimg`.

Sometimes the image is compressed in which case there may be an additional
`.gz`, `.xz` or `.zip` suffix. If the image is compressed, you need to
uncompress it first with one of the commands below:

```bash
# For gz compressed images.
gunzip <IMAGE-NAME>.img.gz

# For xz compressed images.
unxz <IMAGE-NAME>.img.xz

# For zip compressed images.
unzip <IMAGE-NAME>.img.zip
```

## Prerequisites


### A physical device to provision that uses SD cards

In this initial provisioning you will flash and overwrite everything
on the given device storage.

There are several methods to flash storage, and the simplest case is if your
device uses a SD card. Currently, this is the approach we assume you take here,
but the same disk image file can be used to flash any block device. See
[Flash memory types](../../05.System-updates-Yocto-Project/02.Board-integration/01.Partition-configuration/docs.md#flash-memory-types) for a clarification of
what is meant by block device in this context.


## Write the disk image to the SD card

!! Be careful! If you point to the wrong `<DEVICE>` when executing the command below, you risk overwriting your workstation's local or connected storage devices.

Assuming you are in the same directory as your disk image, you can write it to
the the SD card using the following command (`sdimg` is used as an example):

```bash
sudo dd if=<PATH-TO-IMAGE>.sdimg of=<DEVICE> bs=1M && sudo sync
```

This may take a few minutes, depending on the size of the image.

!!! &lt;DEVICE&gt; depends on where your SD card is placed. Normally this would be something like  `/dev/mmcblk0` or `/dev/sdb`.  If you are unsure how to find the correct device, the Raspberry Pi Foundation provides some nice references that can help you for [Linux](https://www.raspberrypi.org/documentation/installation/installing-images/linux.md?target=_blank), [Mac OSX](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md?target=_blank), [Windows](https://www.raspberrypi.org/documentation/installation/installing-images/windows.md?target=_blank).
