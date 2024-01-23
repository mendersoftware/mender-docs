---
title: Features
taxonomy:
    category: docs
---

When inheriting the `mender-full` or `mender-full-ubi` class in `local.conf`,
Mender provides a default set of features that covers a wide range of boards and
needs. However, sometimes it may be necessary to enable or disable certain
features depending on the needs of the particular build. Use
`MENDER_FEATURES_ENABLE` and `MENDER_FEATURES_DISABLE` variables to enable and
disable features provided by Mender.

To enable a feature, add this to your `local.conf`:

```bash
MENDER_FEATURES_ENABLE:append = " <FEATURE>"
```

To disable a feature, add this to your `local.conf`:

```bash
MENDER_FEATURES_DISABLE:append = " <FEATURE>"
```

!!! Note that the space inside the string is important in both of the above examples!


## List of features

Below is a list of the features that Mender provides, with descriptions.
Please note the following markers:

*internal*: feature is meant for internal use by the Mender team
only. The behaviour can be modified at any time.

*experimental*: feature is not undergoing regular QA.

* `mender-bios` - Enables booting of traditional BIOS based systems. Normally
  enabled together with `mender-grub`. Disabling this feature with `mender-grub`
  enabled will assume the booting process uses the UEFI standard.

<!--AUTOVERSION: "Yocto-5.0 \"%\" and later"/ignore-->
* `mender-client-install` - Enables a build that has Mender installed, with
  configuration. Note that this does not include the default Mender partition
  layout, use `mender-image` for that. Note that on
  Yocto-5.0 "scarthgap" and later, you need to use `mender-install` instead.

* `mender-growfs-data` - Enable dynamic resizing of the data filesystem through systemd-growfs

* `mender-grub` - Enables integration with the GRUB bootloader.

* `mender-image` - Enables a build that uses the Mender defined partition
  layout.

* `mender-image-bios` - Enables a build that provides a Mender partitioned image
  for use with traditional BIOS based systems (`.biosimg`). Enabling this
  feature requires enabling `mender-image` too.

* `mender-image-gpt` - Enables a build that provides a Mender partitioned image
  for use with BIOS GPT based systems (`.biosimg`). Enabling this feature
  requires enabling `mender-image` too.

* `mender-image-sd` - Enables a build that provides a Mender partitioned SD card
  image (`.sdimg`). Enabling this feature requires enabling `mender-image` too.

* `mender-image-ubi` - Enables a build that provides a Mender partitioned UBI
  image (`.ubimg`). Enabling this feature requires enabling `mender-image` too.

* `mender-image-uefi` - Enables a build that provides a Mender partitioned UEFI
  image (`.uefiimg`). Enabling this feature requires enabling `mender-image` too.

<!--AUTOVERSION: "Yocto-4.0 \"%\" and older"/ignore-->
* `mender-install` - Enables a build that has Mender installed, with
  configuration. Note that this does not include the default Mender partition
  layout, use `mender-image` for that. Note that on
  Yocto-4.0 "kirkstone" and older, you need to use `mender-client-install`
  instead.

* `mender-partuuid` - *experimental* - Enable usage of UUID as partition identifiers (GRUB only).

    You must set the UUID's for all parts in your environment, e.g

    ```bash
    # UUID's generated using the 'uuidgen -r' command
    MENDER_BOOT_PART = "/dev/disk/by-partuuid/9553c78a-bed1-40fe-9333-f7409e0585e5"
    MENDER_ROOTFS_PART_A = "/dev/disk/by-partuuid/cb8cc332-f5e3-4b53-a489-13d3a8dd5768"
    MENDER_ROOTFS_PART_B = "/dev/disk/by-partuuid/708798f3-4e9d-4338-bb69-bc92e0b51efb"
    MENDER_DATA_PART = "/dev/disk/by-partuuid/0965b52a-89bd-46c1-ac69-3b27fb6c2aae"
    ```

* `mender-partlabel` - *experimental* - Use PARTLABEL to avoid hardcoded drive device path.

* `mender-systemd` - Enables a Mender build that uses systemd. See also the
  section about [disabling Mender as a system
  service](../../05.Customize-Mender/docs.md#disabling-mender-as-a-system-service).

* `mender-systemd-boot` - *experimental* - Use Mender together with systemd-boot.

* `mender-efi-boot` - *internal* - Enabled by GRUB/systemd-boot to extend UEFI overlay recipes.

* `mender-ubi` - Enables Mender configuration files specifically for UBI images.

* `mender-uboot` - Enables integration with the U-Boot bootloader.

* `mender-persist-systemd-machine-id` - Enables setting up the systemd machine
  ID to be persistent across OTA updates.

* `mender-testing-enabled` - *internal* - Enable the testing/* layers and functionality.

## Default features

By default, no features are enabled, but it is common to include a top level
class in order to get some default features. Here is an example of how to enable
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
! Yocto releases prior to 2.6 (thud) used a different feature set by default.
! Use the following command to inspect features enabled for your build:
! `bitbake -e core-image-minimal | grep '^DISTRO_FEATURES='`
