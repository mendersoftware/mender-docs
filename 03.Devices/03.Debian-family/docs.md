---
title: Debian family
taxonomy:
    category: docs
---

This page describes the requirements for Mender when integrated with the Debian
family target OS images such as [Debian](https://www.debian.org/?target=_blank),
[Ubuntu](https://www.ubuntu.com/?target=_blank) and
[Raspberry Pi OS](https://www.raspberrypi.org/downloads/raspberry-pi-os/?target=_blank).

For these devices, `mender-convert` is used to perform the Mender integration,
and this case a Mender integration covers the following:

* Modification of the original partition layout to fulfill Mender's needs to
  perform rootfs image updates.
* Integration with a compatible bootloader (see below for details).
* Install the Mender client and its configuration into the image.

`mender-convert` is designed with the following goals in mind:

* It should be easy to extend the tool to support other boards or distributions
   ** We should not compile code (rely on pre-built binaries)
* The tool shall not be designed around specific hardware/platform types
* The tool should be able to convert images without knowing anything about the
  hardware/platform.
* Platform specific code shall be provided trough *hooks*, and are not part of
  the core `mender-convert` code.

## Default bootloader integration

The default bootloader integration relies on GRUB for both ARM and x86 based
system. In the ARM case it is expected that the U-Boot bootloader loads
GRUB as an EFI application payload.

If you are trying to integrate a new board you should always start out with
the following command:

```bash
MENDER_ARTIFACT_NAME=release-1 ./docker-mender-convert \
    --disk-image <path to your input disk image>
```

`mender-convert` will probe the input image for details about the target
platform and take actions based on this information. With some luck, this is
all that you need to integrate a new device with an unsupported OS.

### Common customizations

In many cases it will be required to provide a [custom configuration
file](../../04.Artifacts/15.Debian-family/02.image-configuration/docs.md#configuration-files)
to provide details that cannot be determined at probe time. Common configuration
variables are:

- `MENDER_STORAGE_DEVICE` - This is the name of your storage medium device in
   the Linux kernel, e.g `/dev/sda` or `/dev/mmcblk0`.

You need to look up this information based the input disk image and OS you are
using. E.g. try booting the image and check the output of `mount` command to see
which device is mounted at `/`.

Example:

> ```bash
> mount
> /dev/mmcblk1p2 on / type ext4 (rw,relatime)
> ```

The above would translate to `MENDER_STORAGE_DEVICE = "/dev/mmcblk1p"`.

!!! Note that the trailing partition index number is not included, only the
!!! device is

!!! The default value of `MENDER_STORAGE_DEVICE` is `/dev/mmcblk0p`


- `MENDER_KERNEL_DEVICETREE` - This variable applies to ARM devices and should
   specify the name of the DTB used for your particular device. It will look for
   the name specified here in the `/boot` directory of the root filesystem. This
   is very hard to "probe" as many vendors ship multiple DTB files, and possibly
   in different locations so there is not enough information to determine which
   one is for your specific board.

## Other Mender customizations

Note that configuring features such as
[identity](../../05.Client-configuration/03.Identity/docs.md) and
[inventory]((../../05.Client-configuration/03.Identity/docs.md) rely on placing
additional files into the target filesystem.  With `mender-convert`,
these modifications should _not_ be done in the input images since
they will be overwritten by `mender-convert`.  The proper mechanism to
support updates like these, is to add them as files in your rootfs
overlay.

Similarly adding
[root file system state scripts](../../06.Artifact-creation/04.State-scripts/docs.md#root-file-system-and-artifact-scripts)
should be done using the `mender-convert` rootfs overlay.

## Fall back to U-Boot integration on ARM

On some ARM devices it will not be possible to run GRUB. In that case the
integration needs to provide a standalone U-Boot integration, which is a more
involved process. The following is an overview of this process:

<!--AUTOVERSION: "mender-convert-integration-scripts/blob/%"/ignore-->
1. Patch the U-Boot source code with the Mender integration patches
    - This process is described
      [here](https://hub.mender.io/t/mender-from-scratch/391), under the U-Boot
      section.
2. Compile the U-Boot binary and U-Boot `env` tools
    - Reference of the build and packaging process can be found
      [here](https://github.com/mendersoftware/mender-convert-integration-scripts/blob/master/build-uboot-rpi.sh)
3. Upload the pre-built U-Boot integration binaries to a convenient location
4. Provide a custom `mender-convert` configuration file with content similar to
   the following:

```bash
# This will disable the default GRUB integration
MENDER_GRUB_EFI_INTEGRATION=n

# This is only useful when using the default GRUB integration
MENDER_COPY_BOOT_GAP=n

CUSTOM_BINARIES_URL="<URL to archive containing integration binaries>"
CUSTOM_BINARIES="<name of the downloaded archive containing integration binaries>"

function platform_modify() {
  mkdir -p work/custom

  run_and_log_cmd "wget -Nq ${CUSTOM_BINARIES_URL} -P work/custom"
  run_and_log_cmd "tar xvf work/custom/${CUSTOM_BINARIES} -C work/custom"

  # Install custom boot.scr with Mender integration
  run_and_log_cmd "sudo cp work/custom/boot.scr work/boot"

  # Install custom 'fw_setenv/fw_getenv configuration' file
  run_and_log_cmd "sudo cp work/custom/fw_env.config work/rootfs/etc/"

  # Do any other platform specific changes here
}

function platform_package() {
  log_info "Embedding bootloader in disk image"

  # NOTE! This step is highly platform specific, and you need to figure out
  # at what address the bootloader binary needs to be flashed.
  run_and_log_cmd "dd if=work/custom/u-boot.bin of=${sdimg_path} \
     seek=64 conv=notrunc status=none"
}
```

Then execute:

```bash
MENDER_ARTIFACT_NAME=release-1 ./docker-mender-convert \
    --disk-image <path to your input disk image> \
    --config <path to custom configuration file>
```

<!--AUTOVERSION: "mender-convert/blob/%/configs"/mender-convert -->
Refer to the following device integrations for more details regarding standalone U-Boot integration:
    - Raspberry Pi 3
      - [configs/raspberrypi_config](https://github.com/mendersoftware/mender-convert/blob/master/configs/raspberrypi_config)
      - [configs/raspberrypi3_config](https://github.com/mendersoftware/mender-convert/blob/master/configs/raspberrypi3_config)
    - Raspberry Pi 4
      - [configs/raspberrypi_config](https://github.com/mendersoftware/mender-convert/blob/master/configs/raspberrypi_config)
      - [configs/raspberrypi4_config](https://github.com/mendersoftware/mender-convert/blob/master/configs/raspberrypi4_config)
    - Beaglebone Black
      - [configs/beaglebone_black_base_config](https://github.com/mendersoftware/mender-convert/blob/master/configs/beaglebone_black_base_config)
      - [configs/beaglebone_black_debian_sdcard_config](https://github.com/mendersoftware/mender-convert/blob/master/configs/beaglebone_black_debian_sdcard_config)
