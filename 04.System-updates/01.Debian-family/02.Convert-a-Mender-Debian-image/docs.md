---
title: Convert a Mender Debian image
taxonomy:
    category: docs
    label: guide
---

Use [`mender-convert`](https://github.com/mendersoftware/mender-convert) to
convert existing Debian disk images for use with Mender. This generates a new
disk image with two rootfs partitions and a data partition for persistent
configuration, installs a bootloader that supports booting either of the root
partitions and installs the Mender client and its configuration.

The output of `mender-convert` is:
* The converted disk image described above ready to be flashed into an SD card.
* A Mender Artifact to be deployed remotely to devices running Mender through
  the Mender Server.
* An ext4 image of the modified filesystem.

### Recommended workflow

The recommended workflow for using `mender-convert` is to have a Debian image
which you would like to have support robust OTA updates. The image output from
`mender-convert` is then replicated in a robust way to many devices. The steps
in this workflow are:

1. Download a Debian image, e.g. [Raspbian](https://downloads.raspberrypi.org/?target=_blank).
5. Generate a Mender Artifact and disk image from this image using
   `mender-convert` (continue reading for details).
6. Deploy the image to all devices.

!!! `mender-convert` is currently tested on BeagleBone, Raspberry Pi 3 and
!!! Raspberry Pi 4, using official Debian or Raspbian images. The goal is
!!! to extend and test `mender-convert` to cover more boards and OSes and
!!! finally make it board-agnostic.

## Prerequisites

### Enough free disk space on your workstation

The amount of disk space needed depends on the size of your original raw disk
image. You should have at least **4 x the size of the raw disk image**
available. For example, if your raw disk image is 4 GB, you should have at least
16 GB free disk space on your workstation where you are running
`mender-convert`.

### A Debian disk image

As described in the workflow above, you need a raw disk image as input to
`mender-convert`. This is the image that contains the root file system you want
to deploy to many devices. Note that this must be a *complete disk image*.

For Debian the possibilities include:
* [Raspbian](https://downloads.raspberrypi.org/?target=_blank)
* [Ubuntu](https://d1b0l86ne08fsf.cloudfront.net/mender-convert/images/Ubuntu-Bionic-x86-64.img.gz)

Or other Debian images. However, the above already have configurations for
`mender-convert` out of the box.


### Docker

#### Docker Engine 17.03

Follow the [documentation to install Docker
Engine](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/?target=_blank),
version **17.03 or later**. Also have a look at the [post-install
steps](https://docs.docker.com/engine/install/linux-postinstall/) to make sure
your system is up to date.

##### Docker permissions

Invoking the docker commands may fail when the local user has insufficient
permissions to connect to the docker daemon. In Ubuntu 18.04, the user must be a
member of the `docker` group to be able to access it. Please check the
documentation for your host OS if you encounter connection issues with docker.

### Download mender-convert

Clone `mender-convert` from the official repository:

<!--AUTOVERSION: "-b % https://github.com/mendersoftware/mender-convert"/mender-convert-->
```bash
git clone -b master https://github.com/mendersoftware/mender-convert.git
```

## Build the mender-convert container image

Change directory to where you downloaded `mender-convert`:

```bash
cd mender-convert
```

Then, run the following command to build the container with all required
dependencies for `mender-convert`:

```bash
./docker-build
```

## Configure the Mender client server configuration

The easiest, and most straight-forward way, is to integrate the client with
[hosted Mender](https://hosted.mender.io?target=_blank):

#### Using [hosted Mender](https://hosted.mender.io?target=_blank)
```bash
./scripts/bootstrap-rootfs-overlay-hosted-server.sh \
    --output-dir ${PWD}/rootfs_overlay_demo \
    --tenant-token "Paste token from https://hosted.mender.io/ui/#/settings/my-organization"
```

However, there are additional scripts in the `scripts/` directory to enable
working with a local demo server, or a production server.

## Convert the disk image

Move your *golden disk image* into an input subdirectory:

```bash
mkdir -p input
mv <PATH_TO_MY_IMAGE> input/debian-image.img
```

### Use the mender-convert container image

Run mender-convert from inside the container with your desired options, e.g.

```bash
MENDER_ARTIFACT_NAME=release-1 ./docker-mender-convert \
    --disk-image input/debian-image.img \
    --config configs/<board>_config \
    --overlay rootfs_overlay_demo/
```

Conversion takes 10-30 minutes, depending on the image size and resources
available. In the meantime can watch `work/convert.log` for progress and
diagnostics information.

After it is finished, you can find your images in the `deploy` directory on your
host machine.

## Customization

### Configuration Files

<!--AUTOVERSION: "blob/%/config"/mender-convert-->
The configuration files are a means to customize the conversion process for
`mender-convert`. In the `configs/` directory, there are customization scripts
which add support for board-specific configurations. A run of `mender-convert`
can include multiple configuration files, each one added with the `--config`
command-line option. The standard configuration which will always be included
can be found in the
[configs/mender_convert_config](https://github.com/mendersoftware/mender-convert/blob/master/configs/mender_convert_config)
file, and includes the defaults for the configuration options which the tool
supports.

!! Note: configuration files are evaluated in the order they are given on the command line, so that later ones can override settings from earlier ones.

### Example

An example application of using a configuration file can be enabling `lzma`
compression for the Raspberry Pi 3:

```bash
echo 'MENDER_ARTIFACT_COMPRESSION=lzma' >> configs/custom_config
```

Call `mender-convert` and provide your custom configuration file using the
`--config` option:

```bash
MENDER_ARTIFACT_NAME=release-1 ./mender-convert \
  --disk-image input/<image-to-convert.img> \
  --config configs/raspberrypi3_config \
  --config configs/custom_config
```

Configuration files are also a means to add customization that might be
necessary for specific devices or distributions. For more information please
visit the [Board-integration](../../../devices/debian-family)
section.


-------------------------------------------------------------------------------

## Hooks/Overrides

The `mender-convert` tool supports the addition of user *hooks* to override, or
add to some specific part of the modification process. Currently the supported hooks are:

| script                | Hook/Override    | Intended function |
|:---                   | :---             | :----             |
| mender-convert-modify |  platform_modify | Perform platform specific modifications |
| mender-convert-package|  platform_package | Perform platform specific package operations |
| some_included_config_file | mender_create_artifact | Override the creation of the Mender-Artifact through modifying the command which calls the `mender-artifact` tool. A good starting point is the standard function found in the standard configuration file *configs/mender_convert_config* |

These are added to the specific configuration file of choice.

#### Example

An example of overriding the `mender_create_artifact` hook is provided below.

Create a custom configuration file with a custom implementation of `mender_create_artifact`:

```bash
cat <<- EOF >> configs/custom_config
mender_create_artifact() {
  local -r device_type="${1}"
  local -r artifact_name="${2}"
  mender_artifact=deploy/${device_type}-${artifact_name}.mender
  log_info "Running custom implementation of the 'mender_create_artifact' hook"
  log_info "Writing Mender artifact to: ${mender_artifact}"
  log_info "This can take up to 20 minutes depending on which compression method is used"
  run_and_log_cmd "mender-artifact --compression ${MENDER_ARTIFACT_COMPRESSION} \
      write rootfs-image \
      --key <path/to/private-key> \
      --file work/rootfs.img \
      --output-path ${mender_artifact} \
      --artifact-name ${artifact_name} \
      --device-type ${device_type}"
}
EOF
```

Call `mender-convert` and provide your custom configuration file using the
`--config` option:

```bash
MENDER_ARTIFACT_NAME=release-1 ./mender-convert \
  --disk-image input/<image-to-convert.img> \
  --config configs/raspberrypi3_config \
  --config configs/custom_config
```
This should trigger the provided `mender_create_artifact` implementation in `configs/custom_config`

-------------------------------------------------------------------------------

## Rootfs-Overlays

The "rootfs-overlay" is a method for providing new and modified files to appear
in the output image without needing to modify the input image. Adding a file,
such as `/etc/mender/mender.conf`, to your "rootfs-overlay" will allow you
customize the files that are included in the output images.

### Example

One example of a overlay-rootfs addition can be found in the
`rootfs-overlay-demo` directory, which, after running the server setup script
(see [Using hosted Mender](../building-a-mender-debian-image#using-mender-professional))
contains:

```bash
rootfs_overlay_demo
└── etc
    ├── hosts
    └── mender
        ├── mender.conf
        └── server.crt
```

The files and folders shown above will become a part of the final file system
available to the device on boot

If the final image needs application configurations and additions, this is the
recommended way of doing it.

-------------------------------------------------------------------------------

## Configuration variables

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
[`IMAGE_ROOTFS_EXTRA_SPACE`](#image-rootfs-extra-space).

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

## MENDER_KERNEL_DEVICETREE 

> Value: kernel.dtb (default) 

Set the name of the kernel devicetree file.

## MENDER_USE_BMAP 

> Values: y/n (default) 

Enable/Disable the usage of bmap index in the generated image.


