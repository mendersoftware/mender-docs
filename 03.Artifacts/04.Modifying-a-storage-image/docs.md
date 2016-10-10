---
title: Modifying a storage image
taxonomy:
    category: docs
---

When provisioning a device, it is useful to modify the storage image (`.sdimg`)
before flashing it to SD cards in order to edit necessary configurations.
In order to do this we can discover the partition offsets within the storage image
and mount the individual partition file systems based on these offsets.

In the example below we will use a BeagleBone Black storage image (`core-image-base-beaglebone.sdimg`),
but the procedure is the same for all storage images.

We start off by looking at information about the image with `fdisk`:

```
fdisk -l -u core-image-base-beaglebone.sdimg
```

The output should look similar to the following:

```
Disk core-image-base-beaglebone.sdimg: 444 MB, 444597248 bytes
4 heads, 32 sectors/track, 6784 cylinders, total 868354 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x4b5fa790

                           Device Boot      Start         End      Blocks   Id  System
core-image-base-beaglebone.sdimg1   *       16384       49151       16384    c  W95 FAT32 (LBA)
core-image-base-beaglebone.sdimg2           49152      316421      133635   83  Linux
core-image-base-beaglebone.sdimg3          327680      594949      133635   83  Linux
core-image-base-beaglebone.sdimg4          606207      868351      131072+   f  W95 Ext'd (LBA)
core-image-base-beaglebone.sdimg5          606208      868351      131072   83  Linux
```

In this example there are four partitions (plus an exteded partition). Please see
[Partition layout](../../Devices/Partition-layout) for a description of the
partitions Mender uses. The two Linux partitions in the middle, at device
`.sdimg2` and `.sdimg3`, are the two rootfs partitions.

First, we need to know the *sector size*. This is shown by the third line of the output:

> Units = sectors of 1 * 512 = **512** bytes

The second piece of information we need is the *start sector* of the partition we want to mount.
This is the second column in the output from `fdisk`. The start sector in bold below for
our two rootfs partitions:

> core-image-base-beaglebone.sdimg2           **49152**      316421      133635   83  Linux  
> core-image-base-beaglebone.sdimg3          **327680**      594949      133635   83  Linux  

In order to mount a partition we simply multiply the sector size and the start sector
and pass that to `mount`. You can use `bash` to do this calculation for you.
So in order to mount both the rootfs partitions in our example, we can run the following commands:

```
sudo mkdir /mnt/rootfs1 && sudo mkdir /mnt/rootfs2
```

```
sudo mount -o loop,offset=$((512*49152)) core-image-base-beaglebone.sdimg /mnt/rootfs1
```

```
sudo mount -o loop,offset=$((512*327680)) core-image-base-beaglebone.sdimg /mnt/rootfs2
```

Now you can modify the rootfs file systems in the paths `/mnt/rootfs1` and `/mnt/rootfs2`.
When finished, please remember to unmount so that the changes are written back to the
storage image, like the following:

```
sudo umount /mnt/rootfs1 && sudo umount /mnt/rootfs2
```

Optionally, you can also remove the created directories:

```
sudo rmdir /mnt/rootfs1 && sudo rmdir /mnt/rootfs2
```
