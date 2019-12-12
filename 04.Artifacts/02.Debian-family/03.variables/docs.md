---
title: Variables
taxonomy:
    category: docs
---

This section provides an overview of the variables that `mender-convert` uses
during the conversion process.

You can override any option specified here by providing your own configuration
file using the '--config' argument.


#### MENDER_COMPRESS_DISK_IMAGE

> Values: y(default)/n

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

## MENDER_KERNEL_DEVICETREE 

> Value: kernel.dtb (default) 

Set the name of the kernel devicetree file.

## MENDER_USE_BMAP 

> Values: y/n (default) 

Enable/Disable the usage of bmap index in the generated image.


