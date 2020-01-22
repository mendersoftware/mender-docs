---
title: Variables
taxonomy:
    category: docs
---

This section provides a reference of variables Mender use during the Yocto
Project build process. The variables are either specific to- and defined by
Mender, as shown by the `MENDER_` prefix, or [defined by the Yocto
Project](http://www.yoctoproject.org/docs/latest/ref-manual/ref-manual.html?target=_blank#ref-variables-glos)
and used by Mender.


#### ARTIFACTIMG_FSTYPE

> Value: `ext4` (default) / <filesystem type>

Defines which file system type Mender will build for the rootfs partitions in
the `.biosimg`, `.sdimg`, `.uefiimg` and the `.mender` file. See [File system
types](../../../devices/yocto-project/partition-configuration#file-system-types)
for more information.


#### ARTIFACTIMG_NAME

> Value: <any string> (defaults to the image name being built)

Overrides the default internal image name that mender will use to build the
`.mender` file with.


#### IMAGE_ROOTFS_SIZE

> Value: <size in KiB> (default calculated from several factors, see below)

The size of the generated rootfs, expressed in kiB. This will be the size that
is shipped in a `.mender` update. This variable is a standard Yocto Project
variable and is influenced by several other factors. See [the Yocto Project
documentation](http://www.yoctoproject.org/docs/latest/ref-manual/ref-manual.html?target=_blank#var-IMAGE_ROOTFS_SIZE)
for more information.

Note that this variable has no effect when generating a complete disk image (any
suffix ending in `img`), since in that case the size is determined
automatically. See
[`MENDER_STORAGE_TOTAL_SIZE_MB`](#mender_storage_total_size_mb) for more
information.

It is recommended not to set this variable, but instead set
`MENDER_STORAGE_TOTAL_SIZE_MB` and let this variable be set automatically from
that.


#### MENDER_ARTIFACT_EXTRA_ARGS

> Value: <mender artifact arguments> (default: empty)

Flags added to this variable will be used as extra arguments to the
`mender-artifact` tool when creating the `.mender` artifact. For example:

```
MENDER_ARTIFACT_EXTRA_ARGS_append = " -v 1"
```

The above example builds an artifact with the version 1 format.


#### MENDER_ARTIFACT_NAME

> Value: <name of artifact> (no default, must be set)

The name of the image or update that will be built. This is what the device will
report that it is running, and different updates must have different names. This
variable must be defined or the build will fail.


#### MENDER_ARTIFACT_SIGNING_KEY

> Value: <key used to sign artifact> (default: empty)

Can be set to a private key which will be used to sign the update artifact. The
default is empty, which means the artifact won't be signed.

The signature can also be added or changed outside the build process, by using
the `mender-artifact` tool's `-k` option. For more information, see [signing
Mender Artifacts](../../signing-and-verification#signing).


#### MENDER_ARTIFACT_VERIFY_KEY

> Value: <key used to verify artifact> (default: empty)

If set, this will add the given public verification key to the client
configuration, which means that the client will reject updates which are not
signed by the corresponding private key (see
[MENDER_ARTIFACT_SIGNING_KEY](#mender-artifact-signing-key)).

More specifically, it will add the key to the root filesystem under
`/etc/mender/artifact-verify-key.pem`, and add a `ArtifactVerifyKey` entry to
`mender.conf`, pointing to this key. Using `MENDER_ARTIFACT_VERIFY_KEY` is
recommended when the key is hosted in a file external to the build system /
Yocto Project layer.

An alternative way to specify a verification key is to include a file named
`artifact-verify-key.pem` in `SRC_URI`. This is a better approach if the key is
hosted inside a Yocto Project layer, as opposed to living externally on the
local host somewhere. Otherwise it has the same effect as defining
`MENDER_ARTIFACT_VERIFY_KEY`.

Note that you cannot both use `MENDER_ARTIFACT_VERIFY_KEY` and have
`artifact-verify-key.pem` in `SRC_URI` at the same time.


#### MENDER_BOOT_PART

> Value: <block device> (default: 1st partition on `MENDER_STORAGE_DEVICE`)

The partition Mender uses as the boot partition. See [More detailed storage
configuration](../../../devices/yocto-project/partition-configuration#more-detailed-storage-configuration)
for more information.


#### MENDER_BOOT_PART_FSTYPE

> Value: auto (default) / <filesystem type>

Filesystem type of boot partition. This configuration is only used in fstab.
Most filesystems can be auto detected, but some can not and hence this variable
exists to override the auto detection.


#### MENDER_BOOT_PART_SIZE_MB

> Value: 16 (default)

The size of the boot partition in the generated `.biosimg`, `.sdimg` or
`.uefiimg` file. See [Configuring the partition
sizes](../../../devices/yocto-project/partition-configuration#configuring-the-partition-sizes)
for more information.


#### MENDER_DATA_PART

> Value: <block device> (default: 4th partition on `MENDER_STORAGE_DEVICE`)

The partition Mender uses as the persistent data partition. See [More detailed
storage
configuration](../../../devices/yocto-project/partition-configuration#more-detailed-storage-configuration)
for more information.


#### MENDER_DATA_PART_DIR

> Value: <directory> (default: empty)

<!--AUTOVERSION: "Yocto Project 2.5 % and later"/ignore-->
!!! This variable and the associated method is obsolete in Yocto Project 2.5 sumo and later.
Simply [using recipes](../../../devices/yocto-project/partition-configuration#deploying-files-to-the-persistent-data-partition)
to put files in the `/data` partition is enough.

This variable is used to add files to the data partition of the Mender
partitioned image. You will need to update your recipe file and your image file.
The update to the recipe file ensures that the persistent files are deployed to
a common location and the updates to the image file ensures that these files are
included in the target image.

The changes needed in a particular recipe include inheriting the deploy class
and ensuring that the persistent files are copied into the `DEPLOYDIR` for
access by the image generation package.

```bash
inherit deploy
do_deploy() {
    install -d ${DEPLOYDIR}/persist
    install -m 0644 persistent.txt ${DEPLOYDIR}/persist
}
addtask do_deploy after do_compile before do_build
```

The changes to the image recipe will add the contents of `persist` directory to
the `.sdimg` or `.uefiimg` file by setting the `MENDER_DATA_PART_DIR` variable.

```bash
MENDER_DATA_PART_DIR = "${DEPLOY_DIR_IMAGE}/persist"
```

!!! The current implementation has a limitation of only one occurrence of
`MENDER_DATA_PART_DIR` containing one directory.

#### MENDER_DATA_PART_FSTYPE

> Value: auto (default) / <filesystem type>

Filesystem type of data partition. This configuration is only used in fstab.
Most filesystems can be auto detected, but some can not and hence this variable
exists to override the auto detection.


#### MENDER_DATA_PART_SIZE_MB

> Value: 128 (default)

The size of the persistent data partition in the generated `.biosimg`, `.sdimg`
or `.uefiimg` file. See [Configuring the partition
sizes](../../../devices/yocto-project/partition-configuration#configuring-the-partition-sizes)
for more information.


#### MENDER_DEMO_HOST_IP_ADDRESS

> Value: <IP address> (default: empty)

As the name indicates, this variable is only relevant if you are building Mender
with the `meta-mender-demo` layer. If set to an IP address, this variable sets
the hostname resolution of the API gateway and the storage proxy
(`docker.mender.io` and `s3.docker.mender.io`) to that address. The default is
empty, which reverts to querying DNS (but note that the Docker setup comes with
its own DNS server).


#### MENDER_DEVICE_TYPE

> Value: <any string> (default: value of `${MACHINE}`)

A string that defines the type of device this image will be installed on. This
variable is only relevant when building a complete partitioned image (any suffix
ending in `img`). Once a device is flashed with this, it will not change, even
if the device is updated.


#### MENDER_DEVICE_TYPES_COMPATIBLE

> Value: <strings> (default: value of `${MACHINE}`)

A space separated string of device types that determine which types of devices
this update is suitable for. This complements the `MENDER_DEVICE_TYPE` variable,
and is only relevant when building a `.mender` update, not when building a
partitioned image (any suffix ending in `img`).


#### MENDER_FEATURES_DISABLE

> Value: <mender features> (default: empty)

Features appended to this variable will be disabled in the build. See [the
section on features](../image-configuration/features) for more information.


#### MENDER_FEATURES_ENABLE

> Value: <mender features> (default: platform dependent)

Features appended to this variable will be enabled in the build. See [the
section on features](../image-configuration/features) for more information.


#### MENDER_GRUB_STORAGE_DEVICE

> Value: <GRUB storage device> (default: empty)

The storage device, as referred to by GRUB (e.g. `hd1`). This variable can be
used in cases where the Linux kernel and GRUB refer to the same device with
different names. See [The bootloader and the Linux kernel do not agree about the
indexes of storage
devices](../../../troubleshooting/yocto-project-build#the-bootloader-and-the-linux-kernel-do-not-agree-about-the-index)
for more information.

If the variable is empty, it is automatically deduced from
`MENDER_STORAGE_DEVICE`.


#### MENDER_IMAGE_BOOTLOADER_BOOTSECTOR_OFFSET

> Value: <sector number> (default: platform dependent)

Together with `MENDER_IMAGE_BOOTLOADER_FILE`, this sets the offset where the
bootloader should be placed, counting from the start of the storage medium. The
offset is specified in units of 512-byte sectors. Obviously this needs to be
non-zero, or the partition table itself would be overwritten.


#### MENDER_IMAGE_BOOTLOADER_FILE

> Value: <bootloader filename> (default: platform dependent)

Together with `MENDER_IMAGE_BOOTLOADER_BOOTSECTOR_OFFSET`, this specifies a file
that you would like to write directly into the boot sector, in the intervening
space between the partition table and the first partition.


#### MENDER_IS_ON_MTDID

> Value: <MTD ID> (default: first MTD ID in `MENDER_MTDIDS`)

This variable is only relevant if the [the `mender-ubi`
feature](../image-configuration/features#list-of-features) is enabled. The
variable should be set to the MTDID of the device that mender, and the root
filesystem in particular, resides on. This is set automatically in cases where
it's possible, but in some cases it must be set manually.

For example:

```
MENDER_MTDIDS = "nand0=20000000.flash"
MENDER_IS_ON_MTDID = "20000000.flash"
```

See also [`MENDER_MTDIDS`](#mender-mtdids).


#### MENDER_KERNEL_IMAGETYPE_FORCE

> Value: <kernel image type> (default: value of `KERNEL_IMAGETYPE`)

In certain build scenarios, the detection of kernel image type may not work for
specific boards. This is usually caused by custom post-processing steps required
to generate the images bypassing the standard Yocto logic. Setting this variable
will ensure that Mender packages the proper files in these cases.


#### MENDER_MBR_BOOTLOADER_FILE

> Value: <MBR bootloader filename> (default: platform dependent)

Specifies a first stage bootloader to flash to the very first sector of the
storage device (Master Boot Record, or "MBR"), in the same sector as the
partition table. This is often used on BIOS based systems and frequently in
combination with [`MENDER_IMAGE_BOOTLOADER_FILE`](#mender_image_bootloader_file)
to flash a second stage bootloader on a later sector on the same storage device.
The bootloader is normally very short, usually shorter than the sector size
itself, so that the partition table will also fit on the same sector. The size
of the bootloader is specified with
[`MENDER_MBR_BOOTLOADER_LENGTH`](#mender_mbr_bootloader_length).

The default depends on which features are enabled. If `mender-bios` and
`mender-grub` are enabled, then the default is the GRUB first stage bootloader,
otherwise the default is empty.


#### MENDER_MBR_BOOTLOADER_LENGTH

> Value: 446 (default)

The number of bytes to flash into the Master Boot Record (MBR) using
[`MENDER_MBR_BOOTLOADER_FILE`](#mender_mbr_bootloader_file).


#### MENDER_MTD_UBI_DEVICE_NAME

> Value: `ubi` (default)

The MTD part name where UBI volumes are stored.

Defaults to `ubi` when `mender-ubi` feature is on and building a `.ubimg`,
otherwise the default is empty.


#### MENDER_MTDIDS

> Value: <mtdids string> (no default, must be set if using UBI)

This variable is only relevant if the [the `mender-ubi`
feature](../image-configuration/features#list-of-features) is enabled, in which
case it is mandatory. It lists the MTDID assignments on the system, separated by
comma. For example:

```
MENDER_MTDIDS = "nand0=20000000.flash,nand1=30000000.flash"
```

If it has more than one entry, then [`MENDER_IS_ON_MTDID`](#mender-is-on-mtdid)
must be set too.


#### MENDER_MTDPARTS

> Value: <mtdparts string> (default calculated from several factors)

This variable is only relevant if the [the `mender-ubi`
feature](../image-configuration/features#list-of-features) is enabled. The
variable holds the MTDPARTS string for the Flash based device. This is set
automatically in cases where it's possible, but in some cases it must be set
manually. For example:

```
MENDER_MTDPARTS = "20000000.flash:1m(u-boot),-(ubi)"
```

Two volume names have special meaning to the Mender `mtdimg` image builder:
* `u-boot` - The image builder will place the bootloader specified in
  `MENDER_IMAGE_BOOTLOADER_FILE` into this volume, if it is specified. Can be
  omitted if the platform doesn't need it.
* `ubi` - The `ubimg` image (UBI image) will be put into this volume. The `ubi`
  volume should virtually always be present.

See also [`MENDER_MTDIDS`](#mender-mtdids).


#### MENDER_NAND_FLASH_PAGE_SIZE

> Value: 2048 (default)

This variable sets the page size, in bytes, of the NAND flash on the device, and
is used to calculate parameters for the UBI volumes.


#### MENDER_PARTITIONING_OVERHEAD_KB

> Value: <number> (default calculated from several factors)

A rough estimate of space lost due to partition alignment, expressed in KiB. The
build process will calculate that automatically using a simple heuristic. See
the definition of `MENDER_PARTITIONING_OVERHEAD_KB` in
[meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank) for
details on the calculation.


#### MENDER_PARTITION_ALIGNMENT

> Value: <number> (default: value of `MENDER_STORAGE_PEB_SIZE`)

Alignment of partitions used when building partitioned images, expressed in
bytes. Note that this is not always a whole number of KiB, particularly when the
storage device is a UBI volume.


#### MENDER_ROOTFS_PART_A

> Value: <block device> (default: 2nd partition on `MENDER_STORAGE_DEVICE`)

The partition Mender uses as the first (A) rootfs partition. See [More detailed
storage
configuration](../../../devices/yocto-project/partition-configuration#more-detailed-storage-configuration)
for more information.


#### MENDER_ROOTFS_PART_A_NAME

> Value: <name> (default: platform dependent)

Alternative name for `MENDER_ROOTFS_PART_A`. Used if you need two different
references to `MENDER_ROOTFS_PART_A`.

Example:
```
# will only accept a UBI volume name (but we normally work with index numbers e.g. `mender_boot_part`)
ubifsmount ubi0:rootfsa
```

Defaults to the value of `${MENDER_ROOTFS_PART_A}` when building `.biosimg`,
`.sdimg` or `.uefiimg`.

Defaults to `${MENDER_STORAGE_DEVICE}:rootfsa` when building `.ubimg`.


#### MENDER_ROOTFS_PART_B

> Value: <block device> (default: 3rd partition on `MENDER_STORAGE_DEVICE`)

The partition Mender uses as the second (B) rootfs partition. See [More detailed
storage
configuration](../../../devices/yocto-project/partition-configuration#more-detailed-storage-configuration)
for more information.


#### MENDER_ROOTFS_PART_B_NAME

> Value: <name> (default: platform dependent)

See [`MENDER_ROOTFS_PART_A_NAME`](#mender_rootfs_part_a_name)

Defaults to the value of `${MENDER_ROOTFS_PART_B}` when building `.biosimg`,
`.sdimg` or `.uefiimg`.

Defaults to `${MENDER_STORAGE_DEVICE}:rootfsb` when building `.ubimg`.


#### MENDER_SERVER_URL

> Value: `https://docker.mender.io` (default)

Variable to override the URL of the server for the client to connect to.


#### MENDER_STATE_SCRIPTS

> Value: `${S}/mender-state-scripts ${MENDER_STATE_SCRIPTS_DIR}` (default)

Variable to override the location of state scripts. See
[MENDER_STATE_SCRIPTS_DIR](#mender-state-scripts-dir) for more information.


#### MENDER_STATE_SCRIPTS_DIR

> Value: `${B}/mender-state-scripts` (default)

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

> Value: `/dev/mmcblk0` (default)

The storage device holding all partitions (rootfs, boot, data) used by Mender.
See [Configuring
storage](../../../devices/yocto-project/partition-configuration#configuring-storage)
for more information.


#### MENDER_STORAGE_PEB_SIZE

> Value: 8388608 (default)

Holds the size, in bytes, of the physical erase blocks (PEBs) on the Flash
device.


#### MENDER_STORAGE_TOTAL_SIZE_MB

> Value: 1024 (default)

Total size of the physical storage medium that mender partitioned images will be
written to, expressed in MiB. The size of rootfs partition will be calculated
automatically by subtracting the sizes of boot (see
[MENDER_BOOT_PART_SIZE_MB](#mender_boot_part_size_mb)) and data partitions (see
[MENDER_DATA_PART_SIZE_MB](#mender_data_part_size_mb)) along with some
predefined overhead (see
[MENDER_PARTITIONING_OVERHEAD_MB](#mender_partitioning_overhead_mb))). Default
value is `1024`.


#### MENDER_SWAP_PART_SIZE_MB

> Value: 0 (default)

<!--AUTOVERSION: "introduced in the Yocto Project 2.7 (%)"/ignore--> 
!!! This variable was introduced in the Yocto Project 2.7 (warrior) release.

The size of the optional swap partition in the generated `.biosimg`, `.sdimg` or
 `.uefiimg` file. By default no swap partition is created, setting this variable
 to a value greater than zero will add one after the other partitions.



#### MENDER_TENANT_TOKEN

> Value: <tenant token string> (default: empty)

Set this variable in `local.conf` in order to make the device recognize the
organization to which it belongs. This option should always be set, except when
running a custom Mender server installation with multitenancy module disabled.


#### MENDER_UBI_LEB_PEB_BLOCK_OVERHEAD

> Value: <number> (default: 128 for NOR Flash, `${MENDER_NAND_FLASH_PAGE_SIZE} *
> 2` for NAND Flash)

The overhead that each logical erase block (LEB) of the UBI device adds to the
physical erase block (PEB), in bytes. In other words, how many bytes are
"wasted" in each LEB. Usually set automatically, but can be overridden.


#### MENDER_UBI_LEB_SIZE

> Value: <number> (default: `${MENDER_STORAGE_PEB_SIZE} -
> ${MENDER_UBI_LEB_PEB_BLOCK_OVERHEAD}`)

The size of each logical erase block (LEB) on the UBI device, in bytes. Usually
set automatically from the various `MENDER_UBI_*_OVERHEAD` variables, but can be
overridden.


#### MENDER_UBI_TOTAL_BAD_PEB_OVERHEAD

> Value: <number> (default: 0 for NOR Flash, 20 per PEB block for NAND Flash)

Total overhead on the whole UBI device, in bytes, that is reserved for bad
physical erase blocks (PEBs). Usually zero for NOR Flash or [a variable
amount](http://linux-mtd.infradead.org/doc/ubi.html?target=_blank) for NAND
Flash.


#### MENDER_UBOOT_ENV_STORAGE_DEVICE_OFFSET

> Value: <number> (default: Value of `MENDER_PARTITION_ALIGNMENT`)

Specifies the offset from the start of the raw block storage where the U-Boot
environment should be stored, expressed in bytes. The default is equal to
`MENDER_PARTITION_ALIGNMENT_KB` (converted to bytes), and if the value is
overridden, it must also be aligned to `MENDER_PARTITION_ALIGNMENT_KB`.


#### MENDER_UBOOT_POST_SETUP_COMMANDS

> Value: <U-Boot command string> (default: empty)

A set of U-Boot commands to be executed at the end of the MENDER_SETUP code in
the MENDER_BOOTENV.


#### MENDER_UBOOT_PRE_SETUP_COMMANDS

> Value: <U-Boot command string> (default: empty)

A set of U-Boot commands to be executed at the beginning of the MENDER_SETUP
code in the MENDER_BOOTENV.


#### MENDER_UBOOT_STORAGE_DEVICE

> Value: <U-Boot storage device> (default: empty)

The storage device, as referred to by U-Boot (e.g. `1`). This variable can be
used in cases where the Linux kernel and U-Boot refer to the same device with
different names. See [The bootloader and the Linux kernel do not agree about the
indexes of storage
devices](../../../troubleshooting/yocto-project-build#the-bootloader-and-the-linux-kernel-do-not-agree-about-the-index)
for more information.

If the variable is empty, it is automatically deduced from
`MENDER_STORAGE_DEVICE`.


#### MENDER_UBOOT_STORAGE_INTERFACE

> Value: <U-Boot storage interface> (default: empty)

The storage interface, as referred to by U-Boot (e.g. `mmc`). This variable can
be used in cases where the Linux kernel and U-Boot refer to the same device with
different names. See [The bootloader and the Linux kernel do not agree about the
indexes of storage
devices](../../../troubleshooting/yocto-project-build#the-bootloader-and-the-linux-kernel-do-not-agree-about-the-index)
for more information.

If the variable is empty, it is automatically deduced from
`MENDER_STORAGE_DEVICE`.


#### SYSTEMD_AUTO_ENABLE_pn-mender

> Value: `enable` (default)

Controls whether to run Mender as a systemd service. See [Modes of
operations](../../../architecture/overview#modes-of-operation) and [Image
configuration](../image-configuration) for more information.

#### MENDER_EXTRA_PARTS

> Value: <Extra partitions list> (default: empty)

This variable is used to define extra partitions which will be added after data partition.
Format is like:
`MENDER_EXTRA_PARTS = "part1 part2"`
`MENDER_EXTRA_PARTS[part1] = "--fixed-size 1024M --label=static --fstype=ext4"`
`MENDER_EXTRA_PARTS[part2] = "--fixed-size 9G --label=update --fstype=vfat"`

where arguments are bypassed as is to wks file and used by  [wic tool](https://www.yoctoproject.org/docs/2.4.2/dev-manual/dev-manual.html#creating-partitioned-images-using-wic)
