---
title: Partition layout
taxonomy:
    category: docs
---

##Overview

In order to support robust rollback, Mender requires the device to have a certain partition layout.
At least four different partitions are needed:
* one boot partition, containing the U-Boot bootloader and its environment
* two partitions for storing the root filesystem and kernel. The kernel image file, zImage, and any device tree binary should be stored in directory /boot
* one for persistent data

One of the rootfs and kernel partitions will be marked as the *active* partition, from which the kernel and rootfs will be booted.
The other, called the *inactive* partition, will be used by the update mechanism to write the updated image.
After an update their roles are swapped.

The persistent data partition stores data that needs to be preserved through an update.

A sample partition layout is shown below:

![Mender client partition layout](mender_client_partition_layout.png)


##File system types

When [building a Mender Yocto Project image](../../Artifacts/Building-Mender-Yocto-image) the build output in `tmp/deploy/images/<MACHINE>` includes a binary rootfs file system image (e.g. with `.ext4` extension), as well as a complete disk image (with `.sdimg` extension). The binary rootfs file system images are used when deploying updates to the device, while the `.sdimg` image is typically used just once during initial device provisioning to flash the entire storage, and includes the partition layout and all partitions.

In general Mender does not have dependencies on a specific file system type, except NAND-flash (non-MMC) storage is not yet supported, but the version of U-Boot you are using must support the file system type used for rootfs because it needs to read the Linux kernel from the file system and start the Linux boot process.

The file system types Mender builds is based on your Yocto Project `IMAGE_FSTYPES` variable. As there is only one `.sdimg` file built, the rootfs file systems inside it will be the **first** `ext2`/`ext3`/`ext4` file system you have in the `IMAGE_FSTYPES` variable.


##Configuring storage

In order to select the storage device where the partitions are expected to be located on the device, `MENDER_STORAGE_DEVICE` should be set, either in `machine.conf` or in `local.conf`. The value should be the raw device containing the entire storage, not any single partition. For example:

```
MENDER_STORAGE_DEVICE = "/dev/mmcblk0"
```

! For memory card storage and some other types of storage, the default way to refer to partitions is to add a "p" and then the number of the partition (for example `/dev/mmcblk0p1`). If you're using a storage type which doesn't follow this scheme (for example `/dev/sda1`), then you also need to set `MENDER_STORAGE_DEVICE_BASE` to the correct value, such as `MENDER_STORAGE_DEVICE_BASE = "${MENDER_STORAGE_DEVICE}"`. The default is the value of `MENDER_STORAGE_DEVICE` plus a "p".


###More detailed storage configuration

If you need more fine grained control over which partitions Mender will use, you can set one or more the following variables to specific partition strings:

* `MENDER_BOOT_PART`
* `MENDER_DATA_PART`
* `MENDER_ROOTFS_PART_A`
* `MENDER_ROOTFS_PART_B`

For example:

```
MENDER_BOOT_PART = "${MENDER_STORAGE_DEVICE_BASE}1"
MENDER_DATA_PART = "${MENDER_STORAGE_DEVICE_BASE}5"
MENDER_ROOTFS_PART_A = "${MENDER_STORAGE_DEVICE_BASE}2"
MENDER_ROOTFS_PART_B = "${MENDER_STORAGE_DEVICE_BASE}3"
```

!! Note that the Mender image builder will not produce such images, so only set these variables if you're building partitioned images yourself, with a different layout than the default Mender layout (the example above reflects the default).


##Configuring the partition sizes

When [building a Mender Yocto Project image](../../Artifacts/Building-Mender-Yocto-image) Mender defines and uses certain OpenEmbedded variables which are used to define the sizes of the partitions. They are defined in `meta-mender` under `classes/mender-sdimg.bbclass`.

| Mount point | Purpose                                                 | Default size | Variable to configure size |
|-------------|---------------------------------------------------------|--------------|----------------------------|
| `/`         | Store the root filesystem and kernel.                   | N/A          | `IMAGE_ROOTFS_SIZE`        |
| `/uboot`    | Store the bootloader.                                   | 16 MB        | `SDIMG_BOOT_PART_SIZE_MB`  |
| `/data`     | Store persistent data, preserved during Mender updates. | 128 MB       | `SDIMG_DATA_PART_SIZE_MB`  |


You can override these default values in your `local.conf`.


##Preserving data and configuration across updates

As Mender does a full rootfs image update, care must be taken in where persistent data is stored. The contents of the partition mounted on `/data` is preserved across updates. In fact, the Mender client itself uses `/data/mender` as a backing to store data that needs to be kept across updates.

If you have data or configuration that you need to preserve across updates, the recommended approach is to create a symlink from where it gets written to somewhere within `/data/`. For example, if you have an application that writes to `/etc/application1`, then you can create a symlink `/etc/application1` -> `/data/application1` to ensure the data it writes is not lost during a Mender rootfs update.
