---
title: Manual U-Boot integration
taxonomy:
    category: docs
---

In order to support rootfs rollback, Mender requires integration with
U-Boot. Normally this is handled automatically by the build process in Mender's
[meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank) layer.

If you need to integrate with U-Boot manually, this page explains how to do so
using your existing Yocto Project build environment.

# How to integrate with U-Boot

Mender provides special integration points for your existing boot code to hook
into so that Mender can be a part of the normal boot process. These integration
points, along with certain required U-Boot features and configuration options,
allow Mender to do safe, automatic updates of the device, with rollback support.

This normally requires patching of stock U-Boot versions, which is what the
automatic process does. But in this section we will do it manually, and the
necessary steps are described below.

If you are not sure whether your board is using automatic patching, you can
check it by executing this command:

```bash
bitbake -e u-boot | grep '^MENDER_UBOOT_AUTO_CONFIGURE='
```

The variable should be either 0 or 1, depending on whether automatic patching is
enabled or not. Note that the string `u-boot` may be different if you are using
a U-Boot fork with a different name.

A good starting point for manual patching, is to take the patch produced by the
automatic patcher and use that as a basis, since it will often be close to
complete, if not fully.

To extract the patch, execute the following bitbake command:

```bash
bitbake -c save_mender_auto_configured_patch u-boot
```

The command will tell you where the resulting patch can be found. As in the
previous command, the string `u-boot` may be different if you are using a U-Boot
fork with a different name.

## Disabling automatic patching

After acquiring the basis patch above, first thing you will need to do is to
disable the automatic patching. This can be done by adding a `u-boot_%.bbappend`
file to your layer (or a different name if you board is using a fork of U-Boot),
and inside it add:

```bash
MENDER_UBOOT_AUTO_CONFIGURE = "0"
```

## U-Boot features

A number of U-Boot features need to be enabled for Mender to work correctly, and
these should be enabled in the board support headers in U-Boot, under
`include/configs`.

1. `CONFIG_BOOTCOUNT_LIMIT`: This is required for rollback support to work. For
   example:

   ```c
   #define CONFIG_BOOTCOUNT_LIMIT
   ```

2. `CONFIG_BOOTCOUNT_ENV`: This will store the boot counter in the U-Boot
   environment. This means that other `CONFIG_BOOTCOUNT_` features should be
   turned off.

3. `CONFIG_ENV_IS_IN_MMC`: This will store the U-Boot environment file on the
   memory card, before the first partition start. See
   [`MENDER_UBOOT_ENV_STORAGE_DEVICE_OFFSET`](../../../../99.Variables/docs.md#mender_uboot_env_storage_device_offset)
   for more information. Other `CONFIG_ENV_IS_IN_` features should be turned
   off.

4. `FAT_ENV_INTERFACE`, `FAT_ENV_DEVICE`, `FAT_ENV_PART` and
   `FAT_ENV_DEVICE_AND_PART` should be removed from the configuration if they
   are present. They will be automatically defined by Mender.


## Integration points

These are the current integration points:

1. `mender_setup`: This is an environment script that should be run at the very
   beginning of the boot process. It will not perform any boot steps, however it
   may modify, and potentially save, the U-Boot environment.

   For example, if your current `bootcmd` looks like this:

   ```bash
   bootcmd=run mmcboot
   ```

   it should be changed to:

   ```bash
   bootcmd=run mender_setup; run mmcboot
   ```

2. `mender_uboot_root`: This is an environment variable that contains the
   description of the device currently set to boot. Whenever a U-Boot command is
   issued that needs to access the current boot partition, this variable should
   be referenced.

   For example, if you have a script, `loadimage`, that loads the kernel from
   the file system, using `mmc` as the device and a `${bootpart}` variable
   reference as the partition to load from:

   ```bash
   loadimage=load mmc ${bootpart} ${loadaddr} ${bootdir}/${bootfile}
   ```

   it should be changed into:

   ```bash
   loadimage=load ${mender_uboot_root} ${loadaddr} ${bootdir}/${bootfile}
   ```

   Note that `mmc` is included in the `${mender_uboot_root}` string; it is a
   complete description of the device and partition to load from.

3. `mender_kernel_root`: This is essentially the same as the previous variable,
   but is a string tailored to the Linux kernel instead of U-Boot. This should
   be used as the `root` argument to the kernel. For example:

   ```bash
   bootargs=console=${console},${baudrate} root=${mmcroot}
   ```

   should be changed to:

   ```bash
   bootargs=console=${console},${baudrate} root=${mender_kernel_root}
   ```


## Optional integration points

This section describes integration steps that are not strictly necessary for
basic Mender functionality, but will improve functionality under certain
conditions.

1. `mender_altbootcmd`: This integration point is only needed if your setup is
   already making use of U-Boot's `altbootcmd` functionality. If not currently
   in use, this step can be skipped.

   If `altbootcmd` is being used, one first needs to disable Mender's built-in
   `altbootcmd`. To do this, the `MENDER_NO_DEFAULT_ALTBOOTCMD` define should be
   added to the board configuration header in U-Boot (inside
   `include/configs`).

   Then, at the beginning of `altbootcmd`, the call `run mender_altbootcmd`
   should be added. Like `mender_setup`, this will not perform any boot steps,
   but it may modify and potentially save the environment. Afterwards the
   `mender_uboot_root` and `mender_kernel_root` variables will refer to the
   correct partitions, taking into account the potential rollback that may
   happen because `altbootcmd` was called. After the desired alternate boot
   steps have been performed, one can either call `bootcmd` to perform a normal
   boot using the new partitions, or one can perform a different type of boot
   sequence and refer to the Mender variables directly.

2. `mender_try_to_recover`: It is recommended to add a call to this boot script
   right after the normal, disk based boot command for the board. Note that it
   should be added *before* other boot methods that are not considered a
   "normal" boot sequence for the board, such as network boots. The call will
   facilitate rollback in the event that a boot fails after an update, without
   reverting to alternative boot methods such as a network boot. For example,
   change:

   ```bash
   bootcmd=run mmcboot; run networkboot
   ```

   into:

   ```bash
   bootcmd=run mmcboot; run mender_try_to_recover; run networkboot
   ```

   If there is no update in progress, the script will do nothing and hence
   alternative boot methods will continue working.

   Note that if this integration point is not used, rollback will still work,
   but it may not activate until after a network boot has been attempted or the
   device has been rebooted through other means.

3. `mender_uboot_boot`, `mender_uboot_if`, `mender_uboot_dev`: These variables
   are not required by Mender, but can be used if, in the board boot code, you
   need access to:

   * the boot partition string (in U-Boot format, for example `mmc 0:1`):
     `mender_uboot_boot`

   * the storage device interface (in U-Boot format, for example `mmc`):
     `mender_uboot_if`

   * the storage device index (in U-Boot format, for example `0`):
     `mender_uboot_dev`


## Boot configuration

There are also a few other details that need to be in place for Mender to work.

### Location of kernel

In a Mender based configuration, the kernel is loaded from the rootfs partition,
not from the boot partition. This is in order to make a complete upgrade
possible, including the kernel. Usually, in a boot partition, the kernel is
stored in the root, but on a rootfs partition it is usually stored in
`/boot`. Therefore, paths that refer to the location of the kernel need to be
updated to point to this location. This is usually the case for the device tree
and initrd files as well, if the kernel has those. For instance:

```bash
uimage=uImage
fdt_file=uImage.dtb
```

should be changed to:

```bash
uimage=boot/uImage
fdt_file=boot/uImage.dtb
```

### Kernel loading method

Because the kernel and associated files are loaded from a rootfs partition, in
the majority of cases it will be an ext4 or ext3 partition. If the existing boot
code for the board uses the `fatload` command to load the kernel and/or any
associated files, it will need to be changed, since the rootfs is usually not a
FAT partition. We recommend that it is replaced simply with `load`, since it
will work in both cases, but it can also be replaced with either `ext2load` or
`ext4load` if desired.

### Size of boot environment file

In the bitbake recipe for `u-boot`, `BOOTENV_SIZE` should be set to the same
value that `CONFIG_ENV_SIZE` is set to in the board specific C header for U-Boot
(inside `u-boot/include/configs`). Which value exactly is board specific; the
important thing is that they are the same.

For example, in `u-boot/include/configs/myboard.h`:

```c
#define CONFIG_ENV_SIZE 0x20000
```

and in `recipes-bsp/u-boot/u-boot_%.bbappend`:

```bash
BOOTENV_SIZE = "0x20000"
```


## Practical example

<!--AUTOVERSION: "%-v2017.11"/ignore-->
For a real life example of a patch used to integrate with Mender, check out [the
patch for
BeagleBone](https://github.com/mendersoftware/meta-mender/blob/pyro-v2017.11/meta-mender-beaglebone/recipes-bsp/u-boot/patches/0001-BBB-Use-Mender-boot-code-for-selecting-boot-device-a.patch?target=_blank)
on github.com. This patch displays all of the steps required to patch the U-Boot
boot code for BeagleBone, including most of the steps described on this
page. Note that the patch is not kept up to date anymore after the automatic
patching capability was added, so it serves only as an example.
