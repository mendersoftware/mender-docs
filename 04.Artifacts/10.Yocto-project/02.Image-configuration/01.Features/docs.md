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

* `mender-ubi` - Enables Mender configuration files specifically for UBI images.

* `mender-systemd` - Enables a Mender build that uses systemd. See also the
  section about [disabling Mender as a system
  service](../docs.md#disabling-mender-as-a-system-service).

* `mender-uboot` - Enables integration with the U-Boot bootloader.

* `mender-growfs-data` - Enable dynamic resizing of the data filesystem through systemd-growfs


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
