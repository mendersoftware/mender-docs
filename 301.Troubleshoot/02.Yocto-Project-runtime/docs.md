---
title: Yocto Project runtime
taxonomy:
    category: docs
---

<!--AUTOVERSION: "to % from"/ignore "GRUB % fails"/ignore-->
## Upgrading to scarthgap from GRUB 2.04 fails with disk not found

<!--AUTOVERSION: "like % used"/ignore "used in %"/ignore-->
Recent versions of `mke2fs` enable the `metadata_csum_seed` feature in ext4 filesystems by default,
which is not recognized by older GRUB versions, like 2.04 used in kirkstone. To be able to upgrade a
device with an affected GRUB, the feature needs to be removed from the new image.

To solve it, add to your `local.conf`:

```bash
EXTRA_IMAGECMD:ext4:append = " -O ^metadata_csum_seed"
```

<!--AUTOVERSION: "RelNotes/v%.txt"/ignore-->
See:
* Bug report: http://savannah.gnu.org/bugs/?56897
* Fix: https://git.savannah.gnu.org/cgit/grub.git/commit/?id=7fd5feff97c4b1f446f8fcf6d37aca0c64e7c763
* mke2fs release notes: https://git.kernel.org/pub/scm/fs/ext2/e2fsprogs.git/tree/doc/RelNotes/v1.47.0.txt


## Upgrading from mender-client 2.1 and earlier to newer versions fails "type_info provides values not yet supported"

If you generate an artifact with mender-artifact version 3.3 or newer and try to upgrade an older mender-client (2.1 or earlier), you may get a log line similar to this:

```bash
Mar 04 10:21:09 ifu-25 mender[14270]: time="2021-03-04T10:21:09Z" level=error msg="Fetching Artifact headers failed: installer: failed to read Artifact: type_info provides values not yet supported" module=state
```

<!--AUTOVERSION: "mender-client %"/ignore-->
It is because mender-client 2.1.0 does not support the newer `rootfs-image.checksum` feature. See [MEN-2956](https://northerntech.atlassian.net/browse/MEN-2956?target=_blank)

To solve it, use the `--no-checksum-provide` flag when creating the artifact. In Yocto you can add this argument to the MENDER_ARTIFACT_EXTRA_ARGS variable.

```bash
MENDER_ARTIFACT_EXTRA_ARGS = "--no-checksum-provide"
```

You will likely then run into another error described above. If so, you can just chose to generate a `v2` artifact and that solves the `--no-checksum-provide` problem as well.

See [here](https://hub.mender.io/t/update-fails/3300?target=_blank) and [here](https://hub.mender.io/t/error-fetching-artifact-headers-failed-installer-failed-to-read-artifact-type-info-provides-values-not-yet-supported/2774?target=_blank) for more discussion on Mender Hub.


## Boot sequence fails with "Failed to mount /uboot" and "codepage cp437 not found"

This sometimes happens when using one of the minimal images from the Yocto Project, such as `core-image-minimal` or `core-image-full-cmdline`. These images do not include the `kernel-modules` package, which contains the kernel module with codepage 437. There are two ways this can be resolved:

* If you're compiling a custom kernel, it is recommended to set the kernel configuration option:

  ```bash
  CONFIG_NLS_CODEPAGE_437=y
  ```

  Please refer to [the Yocto Project Manual](https://docs.yoctoproject.org/kernel-dev/common.html?target=_blank#configuring-the-kernel) for how to use `menuconfig` to generate and save `defconfig` files for the kernel.

* If you're not building a custom kernel, you can add this line to your `local.conf` in order to include all the kernel modules in the image:

  ```bash
  IMAGE_INSTALL:append = " kernel-modules"
  ```

  This is an easier fix, but also requires more space in the image than the previous solution, since all modules will be included, not just the missing one.


## System stops at U-Boot prompt

There are reports of some systems having trouble running the U-Boot boot commands and getting stuck at the U-Boot prompt. This has, notably, been reported to
happen on the Raspberry Pi family of boards with certain serial port adapters. In the failing scenario, it is believed that the serial port adapter is electrically
noisy resulting in spurious data on the console that is interpreted by U-Boot as the user intentionally interrupting the boot process. It is unclear which
brands of serial port adapters cause this issue or if certain boards are more susceptible than others.

If you are experiencing this issue, there are several proposed workarounds that you should try:

* Disable the serial console by editing config.txt.  With Yocto builds you can set the following in your local.conf to disable this:

  ```bash
  ENABLE_UART = "0"
  ```

* Change the U-Boot configuration to disable the UART for console input. Adding the following to the U-Boot environment has been reported to address this
in some situations:

  ```bash
  setenv stdout lcd
  setenv stderr lcd
  setenv stdin usbkbd
  ```

* Modify the U-Boot code to require a different key sequence to interrupt the boot. Some tweaking of the following settings in the U-Boot code may
help here:

  ```bash
  #define CONFIG_AUTOBOOT_KEYED
  #define CONFIG_AUTOBOOT_PROMPT \
      "\nRPi - booting... stop with ENTER\n"
  #define CONFIG_AUTOBOOT_DELAY_STR "\r"
  #define CONFIG_AUTOBOOT_DELAY_STR2 "\n"
  ```

<!--AUTOVERSION: "older meta-mender branch to the % branch"/ignore-->
## I moved from an older meta-mender branch to the thud branch and suddenly my image is just a few MiB too small

This is a typical symptom:

```
error: update (952107008 bytes) is larger than the size of device /dev/mmcblk0p3 (947912704 bytes)
```

<!--AUTOVERSION: "optimization to the % branch"/ignore-->
This is because of an optimization to the thud branch which uses more of the
available space in the `sdimg` and `uefiimg` images. However, it also means that
if the device was provisioned with an older image, the new update will be just
slightly too big for the old partition to hold it.

To revert to the old size calculation, add this to your build configuration
(`machine.conf` or `local.conf` are good places):

```
MENDER_PARTITIONING_OVERHEAD_KB = "${@eval('(int((${MENDER_PARTITION_ALIGNMENT} - 1) / 1024) + 1) * 4')}"
```


## Poor performance when loading images from U-boot

On certain devices you might get poor performance when trying to load the Linux kernel image from the root filesystem, and it can look like this:

```
u-boot=> ext4load ${mender_uboot_root} /boot/${image}
23065088 bytes read in 79537 ms (282.2 KiB/s)
```

This seems to be more common on `aarch64` devices, that is 64-bit ARM.

The root cause of this issue is that U-Boot's `ext4` support does not handle extents very well. When a file gets large enough, extent index blocks will get created for it, and that leads to exercising a very slow code path. This has been fixed in upstream U-boot with this [patch](https://github.com/u-boot/u-boot/commit/d5aee659f217746395ff58adf3a863627ff02ec1?target=_blank), but at the time of writing, this is not included in any released U-boot versions and the first version to contain this fix will be 2019.07.

There are a couple of workarounds,

1. Backport the upstream [patch](https://github.com/u-boot/u-boot/commit/d5aee659f217746395ff58adf3a863627ff02ec1?target=_blank) to the U-boot version you are using or update U-boot to to a version that includes the mentioned patch.
2. Use a different filesystem, e.g `ext3` which does not support `extents` and does not suffer from this limitation.
    - In Yocto you can change filesystem type by setting `ARTIFACTIMG_FSTYPE = "ext3"` in your `local.conf` or other appropriate location
3. Disable `extents` feature on `ext4` filesystem
    - In Yocto you can add `EXTRA_IMAGECMD:ext4 = "-O ^extent"` in your `local.conf` or other appropriate location.
    - Above is equivalent to running `mkfs.ext4 -O ^extent` if you are using something other then Yocto to generate your filesystem images

Additional background information can be found in these threads:

- [uboot ext4load is very slow to read the kernel image into memory](https://community.nxp.com/thread/472241?target=_blank)
- [u-boot: eMMC transfer speed significantly slower than stock u-boot on Tegra186](https://github.com/madisongh/meta-tegra/issues/42?target=_blank)
- [Mender 1.7 - Standalone mode - Kernel read time get difference before and after mender update](https://hub.mender.io/t/mender-1-7-standalone-mode-kernel-read-time-get-difference-before-and-after-mender-update?target=_blank)


<!--AUTOVERSION: "from `%` to `%` on"/ignore -->
### Deploying an update from `dunfell` to `kirkstone` on Raspberry Pi blocks forever with `Waiting for root device /dev/mmcblk0p3...`

Raspberry Pi boards have a set of boot firmware files (including Device Tree Blob files) that are
located on the boot partition, and these files are not updated when you perform an update of the
root filesystem where the kernel lives.

Occasionally, changes to the Raspberry Pi software stack require that these files are updated.
Between the Linux kernel and the boot firmware, version interdependencies exist which need to be
taken care of. Therefore, to update the Linux kernel, you must also update the boot firmware files.

<!--AUTOVERSION: "between `%` and `%` yocto"/ignore -->
This is what has happened between `dunfell` and `kirkstone` yocto releases for Raspberry Pi 3B
(other boards might have been affected too).

Mender provides a recipe to include a state script in the Artifact that will copy the firmware
files into the boot during the Artifact install. Enable it by adding the following to e.g
`local.conf`:

```
INHERIT += "rpi-update-firmware"
```

You can override the script customizing what files to update, e.g only DTB files. See
[mendersoftware/meta-mender@5abe2e7](https://github.com/mendersoftware/meta-mender/commit/5abe2e7b1f85b3482cb53b747ae9ced3f20a3e73) for more details.

!! Updating the boot firmware files can not be done atomically and the files cannot be rolled back
!! even though a rootfs rollback is performed. In conclusion, this is a risky operation which could
!! brick your device. We recommend using this workaround only once when upgrading between Yocto
!! releases, and not for every update henceforth.

!! When removing `INHERIT += "rpi-update-firmware"` from your `local.conf`, you need to to clear the
!! `tmp` directory of the Yocto build or call
!! `bitbake -c clean update-firmware-state-script <your-image-name>` before building a new image to
!! successfully remove the state script from the next Artifact.
