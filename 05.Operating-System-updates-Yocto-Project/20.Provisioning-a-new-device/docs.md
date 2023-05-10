---
title: Provisioning a new device
taxonomy:
    category: docs
    label: tutorial
---

After [building a Mender Yocto Project image](../../05.Operating-System-updates-Yocto-Project/03.Build-for-demo/docs.md#building-the-image), you need to write the disk
image to the flash of the device. There are two ways to accomplish that:

1. Write the image to the storage directly
2. Boot from removable media and flash the image from there

Depending on the build configuration the disk image will have one of the
following suffixes: `sdimg`, `uefiimg`, `biosimg`, or `gptimg`. All disk images are
created by the `meta-mender` layer and by default contain four partitions
(boot, 2× rootfs, data). They are
meant to be written directly to the device storage.

! If booting from removable media in order to flash the image from there, be
! aware that booting with the image produced by meta-mender may not always work
! because Mender uses preconfigured storage locations. These will typically
! match the on-board storage, not the removable media. Use a standard,
! non-Mender configured image instead, and include the Mender image as a file.

If the image is compressed, you first need to decompress it first with one of
the commands below:

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
device uses a SD card. We will make this assumption here, but you can use the
same disk image for flashing any block device. See [Flash memory
types](../../05.Operating-System-updates-Yocto-Project/02.Board-integration/01.Partition-configuration/docs.md#flash-memory-types) 
for the definition of block device used here.



## Write the disk image to the SD card

!! Be careful! If you point to the wrong `<DEVICE>` when executing the command below, you risk overwriting your workstation's local or connected storage devices.

Assuming you are in the same directory as your disk image, you can write it to
the the SD card using the following command (`sdimg` is used as an example):

```bash
sudo dd if=<PATH-TO-IMAGE>.sdimg of=<DEVICE> bs=1M && sudo sync
```

This may take a few minutes, depending on the size of the image.

!!! &lt;DEVICE&gt; depends on what device name the Operating System assign to
!!! your SD-card. Normally, on Linux, the device is usually on the form
!!! `/dev/mmcblk[0-9]` or `/dev/sd[a-z]`. If you are unsure how to
!!! find the correct device, the Raspberry Pi Foundation provides some nice
!!! references that can help you for
!!! [Linux](https://www.raspberrypi.org/documentation/installation/installing-images/linux.md?target=_blank),
!!! [Mac OSX](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md?target=_blank),
!!! [Windows](https://www.raspberrypi.org/documentation/installation/installing-images/windows.md?target=_blank).
