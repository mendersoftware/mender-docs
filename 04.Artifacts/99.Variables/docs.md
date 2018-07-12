---
title: Variables
taxonomy:
    category: docs
---

This section provides a reference of variables Mender use during the Yocto Project build process.
The variables are either specific to- and defined by Mender, as shown by the `MENDER_` prefix, or [defined by the Yocto Project](http://www.yoctoproject.org/docs/latest/ref-manual/ref-manual.html?target=_blank#ref-variables-glos) and used by Mender.


#### ARTIFACTIMG_FSTYPE


Defines which file system type Mender will build for the rootfs partitions in the `.biosimg`, `.sdimg`, `.uefiimg` and the `.mender` file.  See [File system types](../../devices/partition-layout#file-system-types) for more information.


#### IMAGE_ROOTFS_SIZE

The size of the generated rootfs, expressed in kiB. This will be the size that is shipped in a `.mender` update. This variable is a standard Yocto Project variable and is influenced by several other factors. See [the Yocto Project documentation](http://www.yoctoproject.org/docs/latest/ref-manual/ref-manual.html?target=_blank#var-IMAGE_ROOTFS_SIZE) for more information.

Note that this variable has no effect when generating a complete disk image (any suffix ending in `img`), since in that case the size is determined automatically. See  [`MENDER_STORAGE_TOTAL_SIZE_MB`](#mender_storage_total_size_mb) for more information.


#### MENDER_ARTIFACT_EXTRA_ARGS

Flags added to this variable will be used as extra arguments to the `mender-artifact` tool when creating the `.mender` artifact. For example:

```
MENDER_ARTIFACT_EXTRA_ARGS_append = " -v 1"
```

The above example builds an artifact with the version 1 format.


#### MENDER_ARTIFACT_NAME

The name of the image or update that will be built. This is what the device will report that it is running, and different updates must have different names. This variable must be defined or the build will fail.


#### MENDER_ARTIFACT_SIGNING_KEY

Can be set to a private key which will be used to sign the update artifact. The default is empty, which means the artifact won't be signed.

The signature can also be added or changed outside the build process, by using the `mender-artifact` tool's `-k` option. For more information, see the section on [modifying Mender artifacts](../modifying-a-mender-artifact).


#### MENDER_ARTIFACT_VERIFY_KEY

If set, this will add the given public verification key to the client configuration, which means that the client will reject updates which are not signed by the corresponding private key (see [MENDER_ARTIFACT_SIGNING_KEY](#mender-artifact-signing-key)).

More specifically, it will add the key to the root filesystem under `/etc/mender/artifact-verify-key.pem`, and add a `ArtifactVerifyKey` entry to `mender.conf`, pointing to this key. Using `MENDER_ARTIFACT_VERIFY_KEY` is recommended when the key is hosted in a file external to the build system / Yocto Project layer.

An alternative way to specify a verification key is to include a file named `artifact-verify-key.pem` in `SRC_URI`. This is a better approach if the key is hosted inside a Yocto Project layer, as opposed to living externally on the local host somewhere. Otherwise it has the same effect as defining `MENDER_ARTIFACT_VERIFY_KEY`.

Note that you cannot both use `MENDER_ARTIFACT_VERIFY_KEY` and have `artifact-verify-key.pem` in `SRC_URI` at the same time.


#### MENDER_BOOT_PART

The partition Mender uses as the boot partition. See [More detailed storage configuration](../../devices/partition-layout#more-detailed-storage-configuration) for more information.


#### MENDER_BOOT_PART_FSTYPE

Filesystem type of boot partition. This configuration is only used in
fstab. Most filesystems can be auto detected, but some can not and hence this
variable exists to override the auto detection.


#### MENDER_BOOT_PART_SIZE_MB

The size of the boot partition in the generated `.biosimg`, `.sdimg` or `.uefiimg` file. See [Configuring the partition sizes](../../devices/partition-layout#configuring-the-partition-sizes) for more information.


#### MENDER_DATA_PART

The partition Mender uses as the persistent data partition. See [More detailed storage configuration](../../devices/partition-layout#more-detailed-storage-configuration) for more information.


#### MENDER_DATA_PART_DIR

!!! This variable and the associated method is obsolete in Yocto Project 2.5 sumo and later. Simply [using recipes](../../devices/partition-layout#deploying-files-to-the-persistent-data-partition) to put files in the `/data` partition is enough.

This variable is used to add files to the data partition of the Mender partitioned image. You will need to update your recipe file and your image file. The update to the recipe file ensures that the persistent files are deployed to a common location and the updates to the image file ensures that these files are included in the target image.

The changes needed in a particular recipe include inheriting the deploy class and ensuring that the persistent files are copied into the `DEPLOYDIR` for access by the image generation package.

```bash
inherit deploy
do_deploy() {
    install -d ${DEPLOYDIR}/persist
    install -m 0644 persistent.txt ${DEPLOYDIR}/persist
}
addtask do_deploy after do_compile before do_build
```

The changes to the image recipe will add the contents of `persist` directory to the `.sdimg` or `.uefiimg` file by setting the `MENDER_DATA_PART_DIR` variable.

```bash
MENDER_DATA_PART_DIR = "${DEPLOY_DIR_IMAGE}/persist"
```

!!! The current implementation has a limitation of only one occurrence of `MENDER_DATA_PART_DIR` containing one directory.

#### MENDER_DATA_PART_FSTYPE

Filesystem type of data partition. This configuration is only used in
fstab. Most filesystems can be auto detected, but some can not and hence this
variable exists to override the auto detection.


#### MENDER_DATA_PART_SIZE_MB

The size of the persistent data partition in the generated `.biosimg`, `.sdimg` or `.uefiimg` file. See [Configuring the partition sizes](../../devices/partition-layout#configuring-the-partition-sizes) for more information.


#### MENDER_DEMO_HOST_IP_ADDRESS

As the name indicates, this variable is only relevant if you are building Mender with the `meta-mender-demo` layer. If set to an IP address, this variable sets the hostname resolution of the API gateway and the storage proxy (`docker.mender.io` and `s3.docker.mender.io`) to that address. The default is empty, which reverts to querying DNS (but note that the Docker setup comes with its own DNS server).


#### MENDER_DEVICE_TYPE

A string that defines the type of device this image will be installed on. This variable is only relevant when building a complete partitioned image (any suffix ending in `img`). Once a device is flashed with this, it will not change, even if the device is updated.

It defaults to the value of `${MACHINE}`.


#### MENDER_DEVICE_TYPES_COMPATIBLE

A space separated string of device types that determine which types of devices this update is suitable for. This complements the `MENDER_DEVICE_TYPE` variable, and is only relevant when building a `.mender` update, not when building a partitioned image (any suffix ending in `img`).

It defaults to the value of `${MACHINE}`.


#### MENDER_FEATURES_DISABLE

Features appended to this variable will be disabled in the build. See [the
section on features](../image-configuration/features) for more information.


#### MENDER_FEATURES_ENABLE

Features appended to this variable will be enabled in the build. See [the
section on features](../image-configuration/features) for more information.


#### MENDER_IMAGE_BOOTLOADER_BOOTSECTOR_OFFSET

Together with `MENDER_IMAGE_BOOTLOADER_FILE`, this sets the offset where the bootloader should be placed, counting from the start of the storage medium. The offset is specified in units of 512-byte sectors. Obviously this needs to be non-zero, or the partition table itself would be overwritten.


#### MENDER_IMAGE_BOOTLOADER_FILE

Together with `MENDER_IMAGE_BOOTLOADER_BOOTSECTOR_OFFSET`, this specifies a file that you would like to write directly into the boot sector, in the intervening space between the partition table and the first partition.


#### MENDER_KERNEL_IMAGETYPE_FORCE

In certain build scenarios, the detection of kernel image type may not work
for specific boards.  This is usually caused by custom post-processing steps
required to generate the images bypassing the standard Yocto logic.  Setting
this variable will ensure that Mender packages the proper files in these
cases.


#### MENDER_MBR_BOOTLOADER_FILE

Specifies a first stage bootloader to flash to the very first sector of the storage device (Master Boot Record, or "MBR"), in the same sector as the partition table. This is often used on BIOS based systems and frequently in combination with [`MENDER_IMAGE_BOOTLOADER_FILE`](#mender_image_bootloader_file) to flash a second stage bootloader on a later sector on the same storage device. The bootloader is normally very short, usually shorter than the sector size itself, so that the partition table will also fit on the same sector. The size of the bootloader is specified with [`MENDER_MBR_BOOTLOADER_LENGTH`](#mender_mbr_bootloader_length).

The default depends on which features are enabled. If `mender-bios` and `mender-grub` are enabled, then the default is the GRUB first stage bootloader, otherwise the default is empty.


#### MENDER_MBR_BOOTLOADER_LENGTH

The number of bytes to flash into the Master Boot Record (MBR) using [`MENDER_MBR_BOOTLOADER_FILE`](#mender_mbr_bootloader_file).


#### MENDER_MTD_UBI_DEVICE_NAME

The MTD part name where UBI volumes are stored.

Defaults to `ubi` when `mender-ubi` feature is on and building a `.ubimg`, otherwise the default is empty.


#### MENDER_PARTITIONING_OVERHEAD_MB

A rough estimate of space lost due to partition alignment, expressed in MB. The
build process will calculate that automatically using a simple heuristic. See
the definition of `MENDER_PARTITIONING_OVERHEAD_MB` in
[meta-mender](https://github.com/mendersoftware/meta-mender) for details on the
calculation.


#### MENDER_PARTITION_ALIGNMENT_KB

Alignment of partitions used when building partitioned images, expressed in kiB.
Default value is `8192`.


#### MENDER_ROOTFS_PART_A

The partition Mender uses as the first (A) rootfs partition. See [More detailed storage configuration](../../devices/partition-layout#more-detailed-storage-configuration) for more information.


#### MENDER_ROOTFS_PART_A_NAME

Alternative name for `MENDER_ROOTFS_PART_A`. Used if you need two different references to `MENDER_ROOTFS_PART_A`.

Example:
```
# will only accept a UBI volume name (but we normally work with index numbers e.g. `mender_boot_part`)
ubifsmount ubi0:rootfsa
```

Defaults to the value of `${MENDER_ROOTFS_PART_A}` when building `.biosimg`, `.sdimg` or `.uefiimg`.

Defaults to `${MENDER_STORAGE_DEVICE}:rootfsa` when building `.ubimg`.


#### MENDER_ROOTFS_PART_B

The partition Mender uses as the second (B) rootfs partition. See [More detailed storage configuration](../../devices/partition-layout#more-detailed-storage-configuration) for more information.


#### MENDER_ROOTFS_PART_B_NAME

See [`MENDER_ROOTFS_PART_A_NAME`](#mender_rootfs_part_a_name)

Defaults to the value of `${MENDER_ROOTFS_PART_B}` when building `.biosimg`, `.sdimg` or `.uefiimg`.

Defaults to `${MENDER_STORAGE_DEVICE}:rootfsb` when building `.ubimg`.


#### MENDER_SERVER_URL

Variable to override the URL of the server for the client to connect to.
Default value is `https://docker.mender.io`


#### MENDER_STATE_SCRIPTS

Variable to override the location of state scripts. See
[MENDER_STATE_SCRIPTS_DIR](#mender-state-scripts-dir) for more information.


#### MENDER_STATE_SCRIPTS_DIR

Only usable inside recipes that inherit `mender-state-scripts`. Recipes can put
executable binaries or scripts into this location to have the scripts be
included as state scripts for the Mender artifact. This should be done inside
the `do_compile` task of a recipe.

If neither building nor other preprocessing is necessary then it is also
possible to list a source archive in `SRC_URI` that extracts directly into
`${PN}-${PV}/mender-state-scripts`, where `$PN` and `${PV}` are the usual
Bitbake values of recipe name and version, respectively.

And finally, it is possible to set `MENDER_STATE_SCRIPTS` (note the missing
`_DIR`) manually to a location containing state scripts, however it is
recommended to use one of the two above methods.

The three methods should not be mixed.


#### MENDER_STORAGE_DEVICE

The storage device holding all partitions (rootfs, boot, data) used by Mender. See [Configuring storage](../../devices/partition-layout#configuring-storage) for more information.


#### MENDER_STORAGE_TOTAL_SIZE_MB

Total size of the medium that mender partitioned images will be written to,
expressed in MB. The size of rootfs partition will be calculated automatically
by subtracting the sizes of boot (see
[MENDER_BOOT_PART_SIZE_MB](#mender_boot_part_size_mb)) and data partitions (see
[MENDER_DATA_PART_SIZE_MB](#mender_data_part_size_mb)) along with some
predefined overhead (see
[MENDER_PARTITIONING_OVERHEAD_MB](#mender_partitioning_overhead_mb))).  Default
value is `1024`.


#### MENDER_TENANT_TOKEN

Set this variable in `local.conf` in order to make the device recognize the organization to which it belongs. This option should always be set, except when running a custom Mender server installation with multitenancy module disabled.


#### MENDER_UBOOT_ENV_STORAGE_DEVICE_OFFSET

Specifies the offset from the start of the raw block storage where the U-Boot
environment should be stored, expressed in bytes. The default is equal to
`MENDER_PARTITION_ALIGNMENT_KB` (converted to bytes), and if the value is
overridden, it must also be aligned to `MENDER_PARTITION_ALIGNMENT_KB`.


#### MENDER_UBOOT_STORAGE_DEVICE

The storage device, as referred to by U-Boot (e.g. `1`). This variable can be used in cases where the Linux kernel and U-Boot refer to the same device with different names. See [U-Boot and the Linux kernel do not agree about the indexes of storage devices](../../troubleshooting/yocto-project-build#u-boot-and-the-linux-kernel-do-not-agree-about-the-indexes-of-st) for more information.


#### MENDER_UBOOT_STORAGE_INTERFACE

The storage interface, as referred to by U-Boot (e.g. `mmc`). This variable can be used in cases where the Linux kernel and U-Boot refer to the same device with different names. See [U-Boot and the Linux kernel do not agree about the indexes of storage devices](../../troubleshooting/yocto-project-build#u-boot-and-the-linux-kernel-do-not-agree-about-the-indexes-of-st) for more information.


#### SYSTEMD_AUTO_ENABLE_pn-mender

Controls whether to run Mender as a systemd service. See [Modes of operations](../../architecture/overview#modes-of-operation) and [Image configuration](../../artifacts/image-configuration) for more information.
