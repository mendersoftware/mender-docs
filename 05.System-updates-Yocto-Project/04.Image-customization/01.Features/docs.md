---
title: Features
taxonomy:
    category: docs
---

When inheriting the `mender-full` or `mender-full-ubi` class in `local.conf`,
Mender provides a default set of features that covers a wide range of boards and
needs. However, sometimes it may be necessary to enable or disable certain
features depending on the needs for the particular build. This can be done
using the `MENDER_FEATURES_ENABLE` and `MENDER_FEATURES_DISABLE` variables.

To enable a feature, add this to your `local.conf`:

```bash
MENDER_FEATURES_ENABLE_append = " <FEATURE>"
```

To disable a feature, add this to your `local.conf`:

```bash
MENDER_FEATURES_DISABLE_append = " <FEATURE>"
```

!!! Note that the space inside the string is important in both of the above examples!


## List of features

Below is a list of the features that Mender provides, with descriptions:

* `mender-bios` - Enables booting of traditional BIOS based systems. Normally
  enabled together with `mender-grub`. If `mender-grub` is enabled, but
  `mender-bios` is disabled, then it is assumed that the booting process uses
  the UEFI standard.

* `mender-growfs-data` - Enable dynamic resizing of the data filesystem through systemd-growfs

* `mender-grub` - Enables integration with the GRUB bootloader.

* `mender-image` - Enables a build that uses the Mender defined partition
  layout.

* `mender-image-bios` - Enables a build that provides a Mender partitioned image
  for use with traditional BIOS based systems (`.biosimg`). If this is enabled
  then `mender-image` needs to be enabled too.

* `mender-image-sd` - Enables a build that provides a Mender partitioned SD card
  image (`.sdimg`). If this is enabled then `mender-image` needs to be enabled
  too.

* `mender-image-ubi` - Enables a build that provides a Mender partitioned UBI
  image (`.ubimg`). If this is enabled then `mender-image` needs to be enabled
  too.

* `mender-image-uefi` - Enables a build that provides a Mender partitioned UEFI
  image (`.uefiimg`). If this is enabled then `mender-image` needs to be enabled
  too.

* `mender-install` - Enables a build that has Mender installed, with
  configuration. Note that this does not include the default Mender partition
  layout, use `mender-image` for that.

* `mender-partuuid` - Enable usage of UUID as partition identifiers (GRUB only).

    You must set the UUID's for all parts in your environment, e.g

    ```bash
    # UUID's generated using the 'uuidgen -r' command
    MENDER_BOOT_PART = "/dev/disk/by-partuuid/9553c78a-bed1-40fe-9333-f7409e0585e5"
    MENDER_ROOTFS_PART_A = "/dev/disk/by-partuuid/cb8cc332-f5e3-4b53-a489-13d3a8dd5768"
    MENDER_ROOTFS_PART_B = "/dev/disk/by-partuuid/708798f3-4e9d-4338-bb69-bc92e0b51efb"
    MENDER_DATA_PART = "/dev/disk/by-partuuid/0965b52a-89bd-46c1-ac69-3b27fb6c2aae"
    ```

* `mender-systemd` - Enables a Mender build that uses systemd. See also the
  section about [disabling Mender as a system
  service](../docs.md#disabling-mender-as-a-system-service).

* `mender-ubi` - Enables Mender configuration files specifically for UBI images.

* `mender-uboot` - Enables integration with the U-Boot bootloader.


## Default features

By default, no features are enabled, but it is common to include a top level
class in order to get some default features. Her is an example of how to enable
such a class in `local.conf`:

```bash
INHERIT += "mender-full"
```

The currently available classes are:

* `mender-full`: Enables the most common features for Mender, which are:
    * `mender-image`
    * `mender-install`
    * `mender-systemd`
    * `mender-image-uefi`
    * `mender-grub`
    * `mender-growfs-data`

* `mender-full-ubi`: Enables the most common features for UBI based Mender
  installations, which are:
    * `mender-image`
    * `mender-image-ubi`
    * `mender-install`
    * `mender-systemd`
    * `mender-ubi`
    * `mender-uboot`
    * `mender-growfs-data`

<!--AUTOVERSION: "Yocto releases prior to 2.6 (%)"/ignore-->
! Yocto releases prior to 2.6 (thud) used a different feature set by default. Use the following command to check exactly which features are enabled: `bitbake -e core-image-minimal | grep '^DISTRO_FEATURES='`
