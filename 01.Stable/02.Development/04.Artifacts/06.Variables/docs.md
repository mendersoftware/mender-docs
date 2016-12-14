---
title: Variables
taxonomy:
    category: docs
---

This section provides a reference of variables Mender use during the Yocto Project build process.
The variables are either specific to- and defined by Mender, as shown by the `MENDER_` prefix, or [defined by the Yocto Project](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html?target=_blank#ref-variables-glos) and used by Mender.


#### IMAGE_FSTYPES

Influences which file system type Mender will build for the rootfs partitions in the `.sdimg` file. Mender will pick the **first** of the file system types ext2/ext3/ext4 listed in this variable as the file system for rootfs in the generated `.sdimg` file. See [File system types](../../Devices/Partition-layout#file-system-types) for more information.


#### IMAGE_ROOTFS_SIZE

The allocated size of each of the two rootfs partitions. We recommend leaving some space in the initial rootfs partitions so that you allow your rootfs to grow over time as you deploy updates with Mender. See [Configuring the partition sizes](../../Devices/Partition-layout#configuring-the-partition-sizes) and [the Yocto Project documentation](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html?target=_blank#var-IMAGE_ROOTFS_SIZE) for more information.


#### MENDER_BOOT_PART

The partition Mender uses as the boot partition. See [More detailed storage configuration](../../Devices/Partition-layout#more-detailed-storage-configuration) for more information.


#### MENDER_BOOT_PART_SIZE_MB

The size of the boot partition in the generated `.sdimg` file. See [Configuring the partition sizes](../../Devices/Partition-layout#configuring-the-partition-sizes) for more information.


#### MENDER_DATA_PART

The partition Mender uses as the persistent data partition. See [More detailed storage configuration](../../Devices/Partition-layout#more-detailed-storage-configuration) for more information.


#### MENDER_DATA_PART_SIZE_MB

The size of the persistent data partition in the generated `.sdimg` file. See [Configuring the partition sizes](../../Devices/Partition-layout#configuring-the-partition-sizes) for more information.


#### MENDER_PARTITIONING_OVERHEAD_MB

A rough estimate of space lost due to partition alignment, expressed in MB. The
`.sdimg` build process will calculate that automatically using a simple
heuristic: `4 * MENDER_PARTITION_ALIGNMENT_MB` (accounts for boot partition, two
rootfs partitions and a data partition).


#### MENDER_PARTITION_ALIGNMENT_MB

Alignment of partitions used when building `.sdimg` image, expressed in MB.
Default value is `8`.


#### MENDER_ROOTFS_PART_A

The partition Mender uses as the first (A) rootfs partition. See [More detailed storage configuration](../../Devices/Partition-layout#more-detailed-storage-configuration) for more information.


#### MENDER_ROOTFS_PART_B

The partition Mender uses as the second (B) rootfs partition. See [More detailed storage configuration](../../Devices/Partition-layout#more-detailed-storage-configuration) for more information.


#### MENDER_STORAGE_DEVICE

The storage device holding all partitions (rootfs, boot, data) used by Mender. See [Configuring storage](../../Devices/Partition-layout#configuring-storage) for more information.


#### MENDER_STORAGE_TOTAL_SIZE_MB

Total size of the medium that mender `.sdimg` will be written to, expressed in
MB. The size of rootfs partition will be calculated automatically by subtracting
the sizes of boot (see [MENDER_BOOT_PART_SIZE_MB](#mender_boot_part_size_mb))
and data partitions (see [MENDER_DATA_PART_SIZE_MB](#mender_data_part_size_mb))
along with some predefined overhead
(see [MENDER_PARTITIONING_OVERHEAD_MB](#mender_partitioning_overhead_mb))).
Default value is `1024`.


#### MENDER_UBOOT_STORAGE_DEVICE

The storage device, as referred to by U-Boot (e.g. `1`). This variable can be used in cases where the Linux kernel and U-Boot refer to the same device with different names. See [U-Boot and the Linux kernel do not agree about the indexes of storage devices](../../Troubleshooting/Yocto-project-build#u-boot-and-the-linux-kernel-do-not-agree-about-the-indexes-of-st) for more information.


#### MENDER_UBOOT_STORAGE_INTERFACE

The storage interface, as referred to by U-Boot (e.g. `mmc`). This variable can be used in cases where the Linux kernel and U-Boot refer to the same device with different names. See [U-Boot and the Linux kernel do not agree about the indexes of storage devices](../../Troubleshooting/Yocto-project-build#u-boot-and-the-linux-kernel-do-not-agree-about-the-indexes-of-st) for more information.


#### SYSTEMD_AUTO_ENABLE_pn-mender

Controls whether to run Mender as a systemd service. See [Modes of operations](../../Architecture/overview#modes-of-operation) and [Build customizations](../../Artifacts/Build-customizations) for more information.
