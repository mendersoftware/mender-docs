---
title: Variables
taxonomy:
    category: docs
---

This section provides an overview of the variables that `mender-convert` uses
during the conversion process.

You can override any option specified here by providing your own configuration
file using the '--config' argument.


#### IMAGE_ROOTFS_SIZE

> Value: 0 (default)

The size of each of the two rootfs filesystems, in KiB. If this is 0,
mender-convert will use the size of the filesystem content as a basis. If the
value is -1, mender-convert will use the maximum size that will fit inside the
created partition. The size is further modified by `IMAGE_ROOTFS_EXTRA_SPACE`
and `IMAGE_OVERHEAD_FACTOR`.

This variable directly mirrors the variable from the Yocto Project, which is why
it is missing a "MENDER_" prefix.


#### IMAGE_ROOTFS_EXTRA_SPACE

> Value: 0 (default)

The amount of extra free space requested on the rootfs, in KiB. This is added to
the value of `IMAGE_ROOTFS_SIZE`. The size is further modified by
`IMAGE_OVERHEAD_FACTOR`.

Note that due to reserved space for the root user on the filesystem, "df" may
report a significantly lower number than requested. A more accurate number can
be fetched using for example `dumpe2fs` and looking for the `Free blocks` field,
but even this value is usually going to be lower than requested due to meta data
on the filesystem.

This variable directly mirrors the variable from the Yocto Project, which is why
it is missing a "MENDER_" prefix.


#### IMAGE_OVERHEAD_FACTOR

> Value: 1.5 (default)

This factor is multiplied by the used space value for the generated rootfs, and
if the result is larger than `IMAGE_ROOTFS_SIZE + IMAGE_ROOTFS_EXTRA_SPACE`, it
will be used as the size of the rootfs instead of the other two variables.

The actual free space will usually be lower than requested. See comment for
[`IMAGE_ROOTFS_EXTRA_SPACE`](#image_rootfs_extra_space).

This variable directly mirrors the variable from the Yocto Project, which is
why it is missing a "MENDER_" prefix.


#### MENDER_COMPRESS_DISK_IMAGE

> Values: gzip(default)/lzma/none

This is useful when you have large disk images, compressing them makes it easier
to transfer them between a build server and a local machine, and saves space.


#### MENDER_ARTIFACT_COMPRESSION 

> Values: gzip(default)/lzma/none 

The compression algorithm to use when generating the Artifact. In general LZMA
will produce a smaller Mender Artifact (2-3x) but will significantly increase
time spent generating the Mender Artifact (10x).


#### MENDER_ENABLE_SYSTEMD 

> Values: y(default)/n 

If you want the Mender client to operate in managed mode and connect to a
server, then this should be enabled. If you are not interested connecting to a
server and will only be running standalone mode updates, then you can safely
disable this.

#### MENDER_DATA_PART_FSTAB_OPTS

> Values: defaults/<fstab specific options>

Options passed on to fstab.


#### MENDER_DATA_PART_GROWFS

> Values: y(default)/n 

Enable/Disable automatically growing the filesystem to fill the physical storage device.

## MENDER_ARTIFACT_NAME 

> Value: <release-name>

Explicitly set the name of the generated update Artifact. Required for the
conversion to succeed. However, should be specified on the command line, and not
in the configuration.

## MENDER_DEVICE_TYPE 

> Value: <device-type> 

Set the device type specified by the Artifact. If left empty it will default to
the value of '/etc/hostname'.

## MENDER_STORAGE_TOTAL_SIZE_MB

> Value: 8192 (default) 

The size of the storage medium of the device.

## MENDER_BOOT_PART_SIZE_MB 

> Value: 40 (default) 

The size of the boot partition.

## MENDER_DATA_PART_SIZE_MB 

> Value: 128 (default) 

The size of the Mender data partition.

## MENDER_PARTITION_ALIGNMENT 

> Value: 8388608 ( 8MB, default) 

The partition alignment expressed in bytes.

## MENDER_CLIENT_VERSION 

<!--AUTOVERSION: "Value: %"/ignore-->
> Value: master (default) 

The version of the Mender client to include in the update.

## MENDER_STORAGE_URL 

> Value: https://d1b0l86ne08fsf.cloudfront.net (default) 

The source of the binaries employed by the `Mender-convert` tool.

## MENDER_GITHUB_ORG 

> Value: https://github.com/mendersoftware (default) 

The URL prefix for looking up the mendersoftware dependencies.

## MENDER_STORAGE_DEVICE 

> Value: /dev/mmcblk0p (default) 

Set the device file corresponding to the root filesystem partitions.

## MENDER_BOOT_PART_INDEX 

> Value: 1 (default)  

Set the default index for the boot partition.

## MENDER_ROOTFS_PART_A_INDEX 

> Value: 2 (default) 

Set the default index of the rootfs part-A partition.

## MENDER_ROOTFS_PART_B_INDEX 

> Value: 3 (default) 

Set the default index of the rootfs part-B partition.

## MENDER_DATA_PART_INDEX 

> Value: 4 (default) 

Set the index of the data partition.


## MENDER_ENABLE_PARTUUID

> Values: y/n(default)

This option enables the use of partuuid's as partition block device references. The variables `MENDER_BOOT_PART`, `MENDER_ROOTFS_PART_A`, `MENDER_ROOTFS_PART_B` and `MENDER_DATA_PART` should also be set in conjunction with this variable to ensure reproducible builds with the same part-uuids.




## MENDER_BOOT_PART

> Value:

This option allows fine grained control of the boot partition device path and overrides `MENDER_STORAGE_DEVICE` and `MENDER_BOOT_PART_INDEX` settings. If part-uuid is used then you will need to also enable `MENDER_ENABLE_PARTUUID`

Examples: 
```
/dev/sda1
/dev/disk/by-partuuid/26445670-f37c-408b-be2c-3ef419866620
/dev/disk/by-partuuid/26445670-01
```

## MENDER_ROOTFS_PART_A

> Value:

This option allows fine grained control of the first (A) rootfs partition device path and overrides `MENDER_STORAGE_DEVICE` and `MENDER_ROOTFS_PART_A_INDEX` settings. If part-uuid is used then you will need to also enable `MENDER_ENABLE_PARTUUID`

Examples: 
```
/dev/sda2
/dev/disk/by-partuuid/26445670-f37c-408b-be2c-3ef419866621
/dev/disk/by-partuuid/26445670-02
```

## MENDER_ROOTFS_PART_B

> Value:

This option allows fine grained control of the first (B) rootfs partition device path and overrides `MENDER_STORAGE_DEVICE` and `MENDER_ROOTFS_PART_B_INDEX` settings. If part-uuid is used then you will need to also enable `MENDER_ENABLE_PARTUUID`

Examples: 
```
/dev/sda3
/dev/disk/by-partuuid/26445670-f37c-408b-be2c-3ef419866622
/dev/disk/by-partuuid/26445670-03
```

## MENDER_DATA_PART

> Value:

This option allows fine grained control of the data partition device path and overrides `MENDER_STORAGE_DEVICE` and `MENDER_DATA_PART_INDEX` settings. If part-uuid is used then you will need to also enable `MENDER_ENABLE_PARTUUID`

Examples: 
```
/dev/sda4
/dev/disk/by-partuuid/26445670-f37c-408b-be2c-3ef419866623
/dev/disk/by-partuuid/26445670-04
```

## MENDER_KERNEL_DEVICETREE 

> Value: kernel.dtb (default) 

Set the name of the kernel devicetree file.

## MENDER_USE_BMAP 

> Values: y/n (default) 

Enable/Disable the usage of bmap index in the generated image.


