---
title: Modifying a disk image
taxonomy:
    category: docs
---

When provisioning a device, it is useful to modify the disk image (`.sdimg`)
before flashing it to SD cards in order to edit necessary configurations.
In order to do this we can discover the partition offsets within the disk image
and mount the individual partition file systems based on these offsets.

In the example below we will use a BeagleBone Black disk image (`mender-beaglebone.sdimg`),
but the procedure is the same for all disk images.

We start off by looking at information about the image with `fdisk`:

```
fdisk -l -u mender-beaglebone.sdimg
```

The output should look similar to the following:

```
Disk mender-beaglebone.sdimg: 1056 MB, 1056964608 bytes
4 heads, 32 sectors/track, 16128 cylinders, total 2064384 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x23737de7

                  Device Boot      Start         End      Blocks   Id  System
mender-beaglebone.sdimg1   *       49152       81919       16384    c  W95 FAT32 (LBA)
mender-beaglebone.sdimg2           81920      933887      425984   83  Linux
mender-beaglebone.sdimg3          933888     1785855      425984   83  Linux
mender-beaglebone.sdimg4         1802239     2064383      131072+   f  W95 Ext'd (LBA)
mender-beaglebone.sdimg5         1802240     2064383      131072   83  Linux
```

In this example there are four partitions (plus an extended partition). Please see
[Partition layout](../../Devices/Partition-layout) for a description of the
partitions Mender uses. The two Linux partitions in the middle, at device
`.sdimg2` and `.sdimg3`, are the two rootfs partitions.

First, we need to know the *sector size*. This is shown by the third line of the output,
in bold below:

> Units = sectors of 1 * 512 = **512** bytes

The second piece of information we need is the *start sector* of the partition we want to mount.
This is the second column in the output from `fdisk`. The start sector is shown in bold below for
our two rootfs partitions:

> mender-beaglebone.sdimg2           **81920**      933887      425984   83  Linux  
> mender-beaglebone.sdimg3          **933888**     1785855      425984   83  Linux  

In order to mount a partition we simply multiply the sector size and the start sector
and pass that to `mount`. You can use `bash` to do this calculation for you.
So in order to mount both the rootfs partitions in our example, we can run the following commands:

```
sudo mkdir /mnt/rootfs1 && sudo mkdir /mnt/rootfs2
```

```
sudo mount -o loop,offset=$((512*81920)) mender-beaglebone.sdimg /mnt/rootfs1
```

```
sudo mount -o loop,offset=$((512*933888)) mender-beaglebone.sdimg /mnt/rootfs2
```

Now you can modify the rootfs file systems in the paths `/mnt/rootfs1` and `/mnt/rootfs2`.
When finished, please remember to unmount so that the changes are written back to the
disk image, like the following:

```
sudo umount /mnt/rootfs1 && sudo umount /mnt/rootfs2
```

Optionally, you can also remove the created directories:

```
sudo rmdir /mnt/rootfs1 && sudo rmdir /mnt/rootfs2
```
