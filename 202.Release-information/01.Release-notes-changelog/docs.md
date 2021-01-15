---
title: Release notes & changelog
taxonomy:
    category: docs
shortcode-core:
    active: false
---

## meta-mender sumo-v2018.11.2

_Released 11.16.2018_

#### meta-mender (sumo-v2018.11.2)

New changes in meta-mender since sumo-v2018.11:

* Add mender 1.7.0b1 recipe.
* Add mender-artifact 2.4.0b1 recipe.


## meta-mender sumo-v2018.11

_Released 11.12.2018_

#### meta-mender (sumo-v2018.11)

New changes in meta-mender since sumo-v2018.10:

* QEMU: Always try to run with KVM enabled, only fall back to emulation.


## meta-mender sumo-v2018.10

_Released 10.03.2018_

#### meta-mender (sumo-v2018.10)

New changes in meta-mender since sumo-v2018.09:

* Make sure mtdimg is not truncated, but has its full length.
* Add specific patches for u-boot-toradex_2016.11.
  ([MEN-1849](https://tracker.mender.io/browse/MEN-1849))
* Fix incorrect Flash bad PEB calculation which led to wrong total image size.
  ([MEN-1849](https://tracker.mender.io/browse/MEN-1849))
* Make mkfs.ubifs and ubinize arguments a bit more customizable.
  The new variables `MENDER_FLASH_MINIMUM_IO_UNIT` and
  `MENDER_MAXIMUM_LEB_COUNT` have been introduced, which maps directly
  to the corresponding arguments of the two tools.
* Fix inability to patch old u-boot variants of MTDPARTS and
  MTDIDS correctly.
  ([MEN-1849](https://tracker.mender.io/browse/MEN-1849))
* Fix confusing warning flood when MENDER_MTDIDS is unset in a UBI build.


## meta-mender sumo-v2018.09

_Released 09.13.2018_

#### meta-mender (sumo-v2018.09)

New changes in meta-mender since sumo-v2018.08:

* Fix regression in QEMU launching after changing image name in 897195ddc3f.
* GRUB: Pass kernel arguments from bootargs variable instead of hard-coded.
  This allows it to be overridden or modified by adding a script snippet
  which sets the variable.
  Also log kernel messages to both screen and serial port by default,
  and have systemd log to serial port (last "console" argument,
  apparently it cannot log to both).
* Introduce support for a standardized boot method on ARM
  using UEFI and GRUB. The UEFI boot standard is fully supported on ARM
  in theory, but few board manufacturers implement it in practice.
  Therefore U-Boot is still utilized, but acts only as a UEFI loader,
  and hence no U-Boot integration is needed. All boot scripts are then
  handled by GRUB, which needs no patching.
  ([MEN-1595](https://tracker.mender.io/browse/MEN-1595), [MEN-1659](https://tracker.mender.io/browse/MEN-1659))
* Auto-select correct `MENDER_STORAGE_DEVICE_BASE` scheme.
  This should rarely need to be set by anyone anymore.
* Add some debug functionality to GRUB booting process.
  To use it, enable either or both of `debug-log` and `debug-pause` in
  `PACKAGECONFIG` for `grub-mender-grubenv`. The former enables debug
  logging in GRUB, which can be tweaked further by setting the
  `DEBUG_LOG_CATEGORY` variable. The latter pauses the boot process at
  strategic points during the boot, so that screen output can be
  captured before it is cleared or scrolls by.
* GRUB: Fix error about devicetree command not being found.
* Images partitioned with GPT or MS-DOS partition tables are
  now padded up to the nearest alignment specified in
  `MENDER_PARTITION_ALIGNMENT`. Previously the last block might be
  shorter.
* Fix build error when using GRUB and /dev/mmcblk storage device.
* Fix build error when using any hard-drive besides sda/hda, such as sdb.
* Fix `IMAGE_ROOTFS_EXCLUDE_PATH` failing when listing a non-existent path.
* Fix `MENDER_GRUB_STORAGE_DEVICE` variable not being respected.
  ([MEN-2048](https://tracker.mender.io/browse/MEN-2048))
* Allow disabling auto-generated /etc/fstab
* Boot script recipe for demoing OTA updates
* mender: Allow overrides for MENDER_STORAGE_TOTAL_SIZE_MB_DEFAULT.
* mender-uboot: Use hex for dev/part numbers in U-Boot.
* Add mender 1.5.1 recipe.
* Add mender 1.6.0 recipe.
* Add mender-artifact 2.3.0 recipe.


## Mender 1.5.1

_Released 09.18.2018_

#### gui (1.5.1)

New changes in gui since 1.5.0:

* Bugfix - show decommissioned devices in deployment reports
* Bugfix - show decommissioned devices in deployment reports

#### integration (1.5.1)

New changes in integration since 1.5.0:

* test_security.py: Ignore return code of grep.
* Upgrade gui to 1.5.1.
* Upgrade inventory to 1.4.1.
* Upgrade mender to 1.5.1.
* Upgrade mender-cli to 1.0.1.

#### mender (1.5.1)

New changes in mender since 1.5.0:

* FIX: Enabling compiling ppc64le
* Fix active partition detection when using non-native
  filesystems.


## meta-mender sumo-v2018.08

_Released 08.03.2018_

#### meta-mender (sumo-v2018.08)

New changes in meta-mender since sumo-v2018.07:

* Add mender 1.6.0b1 and mender-artifact 2.3.0b1 recipes.
* Fixed support for raspberrypi3-64 and aarch64
* Fix incorrect license tag for mender-artifact recipe.
  Little practical difference, since they are all permissive licenses.
* mender-uboot: Allow multi-digit partition/device nums.
* Fix license checksum sometimes failing in
  `u-boot-fw-utils-mender-auto-provided` recipe when U-Boot fork has a
  slightly different README file.


## meta-mender sumo-v2018.07

_Released 07.12.2018_

#### meta-mender (sumo-v2018.07)
* Warn when mender.conf settings conflict with Bitbake variables.
* Make sure that new-style "enp" network devices get DHCP address in demo.
* Delete all components from pre-1.3 Mender releases.
  All pre-1.3 releases are EOL.
* Rename IMAGE_BOOTLOADER* variables to MENDER_IMAGE_BOOTLOADER*.
* Fix lockfile error due to using system lock directory.
* Licence checksum updated in mender-artifact
* mender: Allow for forcing a specific KERNEL_IMAGETYPE.
* mender-uboot: Add MENDER_UBOOT_POST_SETUP_COMMANDS config point.
* Fix occasional inode corruption issue when re-launching a
  previously launched and saved QEMU image.
* QEMU: Limit client setup steps to run on first boot only.
* mender-qemu: increase qemu memory size to 256MiB.
* Let colibri-imx7 and vf boards be handled by automatic patching.
* Fixed issue with build due to unknown image linux-firmware-raspbian-bcm43430
* Fix mender not building if build and host architecture is the same.
* meta-mender-orangepi: Fix up u-boot
* Fix Linux kernel hanging when loaded via U-Boot/UEFI/GRUB
  on vexpress-qemu*.
  ([MEN-1657](https://tracker.mender.io/browse/MEN-1657))
* Add mender-1.3.1 and mender-artifact-2.1.2 recipes.
* Implement `IMAGE_ROOTFS_EXCLUDE_PATH` support. It works the
  following way: It contains a space separated list of directories,
  relative to the rootfs root (no beginning slash), and any directory
  specified will be omitted from the rootfs. If the directory ends in a
  slash, only the contents will be omitted, not the directory itself
  (useful for mount points). One can then set
  `do_image_<imagetype>[respect_exclude_path] = "1"` for certain image
  builders to prevent the exclusion and then add them back as separate
  partitions there.
* Support for `MENDER_DATA_PART_DIR` has been removed. Use
  recipe files to add files directly to the `/data` directory instead.
* mender: Create bmap files.
* tests: Filter out the data partition as the latest build artifact.
* example-state-scripts: Explicitly return 0 from scripts.
* uboot_auto_patch: Simplify definition placement at the expense of beauty.
  The resulting patch is uglier because the definitions go into a cross
  platform section which is not appropriate for upstream submission. But
  it does fix the case where unwanted ifdefs were "hiding" the added
  definitions.
* rpi_0_w: Setup Mender required defconfigs
* Implement GRUB and x86-64 support.
  ([MEN-1430](https://tracker.mender.io/browse/MEN-1430), [MEN-1432](https://tracker.mender.io/browse/MEN-1432), [MEN-1433](https://tracker.mender.io/browse/MEN-1433), [MEN-1434](https://tracker.mender.io/browse/MEN-1434), [MEN-1435](https://tracker.mender.io/browse/MEN-1435), [MEN-1436](https://tracker.mender.io/browse/MEN-1436))
* Implement qemux86-64 machine target.
  ([MEN-1430](https://tracker.mender.io/browse/MEN-1430), [MEN-1432](https://tracker.mender.io/browse/MEN-1432), [MEN-1433](https://tracker.mender.io/browse/MEN-1433), [MEN-1434](https://tracker.mender.io/browse/MEN-1434), [MEN-1435](https://tracker.mender.io/browse/MEN-1435), [MEN-1436](https://tracker.mender.io/browse/MEN-1436))
* mender: Conditionally add /uboot mount only for SDCards.
* Increased the demo mender-retry-polling interval
  ([MEN-1006](https://tracker.mender.io/browse/MEN-1006))
* meta-mender-toradex-nxp: Adapt colibri-imx7-mender to U-Boot autopatching
* Fix 'depends upon non-existent task' error in U-Boot recipes without auto patching.
* Use timedatectl, if available, to determine with time is synchronized.
* mender upgraded to 1.4.0.
* mender-artifact upgraded to 2.2.0.
* mender-qemu: More robust detection of MACHINE setting.
* beaglebone: Rename to beaglebone-yocto.
* Add mtdimg image type.
  The mtdimg type is an image type meant to be flashed to the entire
  Flash device, unlike the ubimg, which should only be flashed to the
  ubi area of the mtd device. Either one can be used depending on need.
  vexpress-nor image, used in QEMU, was also changed to take advantage
  of the new mtdimg image.
  ([MEN-1597](https://tracker.mender.io/browse/MEN-1597))
* Add LAYERSERIES_COMPAT settings to all Mender layers.
* Replace `MENDER_PARTITION_ALIGNMENT_KB` with
  `MENDER_PARTITION_ALIGNMENT`, which is in bytes.
* Rename `MENDER_STORAGE_RESERVED_RAW_SPACE` to
  `MENDER_RESERVED_SPACE_BOOTLOADER_DATA`, to better reflect what it is
  used for.
* Enable wifi in the raspberry-pi demo image by default.
  ([MEN-1804](https://tracker.mender.io/browse/MEN-1804))
* mender: Only create vfat boot partition if size is non-zero
* meta-mender-toradex-nxp: increase layer priority to 91
* Fix creating ubifs image.
* tests: Respect user set SSTATE_DIR and DL_DIR variables.
* Make sure auto provided fw-utils use virtual/bootloader setting if present.
* QEMU: Raise systemd service timeout so that it boots properly on slow hosts.
* Fix fstab sometimes not containing boot partition entry.
* Fix build error if `IMAGE_FSTYPES` contains the same entry more than once.
* Implement x86 BIOS support together with GRUB.
  It can be enabled by inheriting the `mender-full-bios` class, or by
  enabling the `mender-grub` and `mender-bios` features using
  `MENDER_FEATURES_ENABLE`.
  ([MEN-1845](https://tracker.mender.io/browse/MEN-1845))
* Client container init scripts are modified to accept MAC address for qemu through env var, `RANDOM_MAC`.
* added layer dependency on mender layer
* uboot_auto_configure: Fail immediately if a define cannot be added.
  Better than failing later at runtime, where the problem is much harder
  to debug.
* Warn on unused MENDER_.* variables
  ([MEN-1603](https://tracker.mender.io/browse/MEN-1603))
* uboot_auto_patch: Switch kernel address from `kernel_addr_r` to `loadaddr`.
* Remove unused IMAGE_UENV_TXT_FILE variable.
* Add U-Boot auto patching support for Flash based devices.
  The autopatcher will use UBI as storage medium for both the
  filesystems and the U-Boot environment. Mender requires a minimum of
  configuration: the `MENDER_MTDIDS` needs to be set for the board, and
  will normally go in the `conf/machine/<MACHINE>.conf` file for the
  board in question. See documentation for variables `MENDER_MTDIDS`,
  `MENDER_IS_IN_MTDID` and `MENDER_MTDPARTS` for more information.
  ([MEN-1597](https://tracker.mender.io/browse/MEN-1597))
* Partition alignment (`MENDER_PARTITION_ALIGNMENT`) on Flash
  devices using UBI is now aligned to the UBI LEB size, which in general
  is not a multiple of KiB.
  ([MEN-1597](https://tracker.mender.io/browse/MEN-1597))
* Add Mender 1.4.1 recipe.
* Clear IMAGE_NAME_SUFFIX for all image types.
* Fix "No rule to make target 'envtools'" error in some U-Boot builds.
* Pregenerate SSH keys for all QEMU images.
* Since the "beaglebone" machine name has changed in upstream
  to "beaglebone-yocto", add "beaglebone" to the
  `MENDER_DEVICE_TYPES_COMPATIBLE` default, so that older devices can
  upgrade even if they have the old device type.
* mender: Copy data partition images to the deploy dir.
* mender: Append to fstab rather than replacing it.
* Fix failed uboot.env install when mender-uboot feature is disabled.
* tests: Also check ARTIFACTIMG_FSTYPE for compatible images.
* uboot_auto_patch: Update to support U-Boot v2018.05.
* uboot_auto_patch: Add support for new Kconfig based
  defines.
* mender-uboot: Add MENDER_UBOOT_PRE_SETUP_COMMANDS config point.
* Add Mender 1.5.0 Beta recipe.
* Add mender-1.4.0b1 and mender-artifact-2.2.0b1 recipes.
* Add 'dataimg' as an image type.
  It contains the data partition filesystem which is normally part of
  the complete partitioned image. To enable it, add `dataimg` to
  `IMAGE_FSTYPES`.
  ([MEN-1879](https://tracker.mender.io/browse/MEN-1879))
* mender: Use only the basename to load DTBs.
* Add Mender 1.5.0 recipe.
* Document SDIMG_ROOTFS_TYPE settings for Raspberry Pi.
* Change rootfs size calculation so it takes alignment into account.
  This should fix a few corner cases, where the filesystems may all fit
  in terms of bytes, but still would not actually fit because of
  partition alignment.
* Added new state script to wait for time sync to complete.
* Drop creation of `authtentoken` file, which is unneeded now.
* Added basic support for orangepi boards
* mender: Cleanup IMAGE_FSTYPES.
* uboot_auto_configure: Handle tabs in defines correctly.


## meta-mender rocko-v2018.07

_Released 07.10.2018_

#### meta-mender (rocko-v2018.07)
* Clear IMAGE_NAME_SUFFIX for all image types.
* Use timedatectl, if available, to determine with time is synchronized.
* Change rootfs size calculation so it takes alignment into account.
  This should fix a few corner cases, where the filesystems may all fit
  in terms of bytes, but still would not actually fit because of
  partition alignment.
  Backported to Morty. MENDER_PARTITION_ALIGNMENT_KB instead
  of MENDER_PARTITION_ALIGNMENT.
* Fix Linux kernel hanging when loaded via U-Boot/UEFI/GRUB
  on vexpress-qemu*.
  ([MEN-1657](https://tracker.mender.io/browse/MEN-1657))
* Fix occasional inode corruption issue when re-launching a
  previously launched and saved QEMU image.
* QEMU: Limit client setup steps to run on first boot only.
* tests: Filter out the data partition as the latest build artifact.
* Licence checksum updated in mender-artifact
* Fixed issue with build due to unknown image linux-firmware-raspbian-bcm43430
* tests: Respect user set SSTATE_DIR and DL_DIR variables.
* Warn when mender.conf settings conflict with Bitbake variables.
* example-state-scripts: Explicitly return 0 from scripts.
* Client container init scripts are modified to accept MAC address for qemu through env var, `RANDOM_MAC`.
* tests: Also check ARTIFACTIMG_FSTYPE for compatible images.
* meta-mender-core: Clean spaces out of UBOOT_MACHINE.


## meta-mender rocko-v2018.06

_Released 06.05.2018_

#### meta-mender rocko-v2018.06
* Add Mender 1.5.0 recipe.
* Add Mender 1.4.1 recipe.
* Enable wifi in the raspberry-pi demo image by default.
  ([MEN-1804](https://tracker.mender.io/browse/MEN-1804))


## Mender v1.5.0

_Released 06.07.2018_

#### integration (1.5.0)
* Add mender-cli as a versioned repository under the Mender umbrella.
* Upgrade deployments to 1.5.0.
* Upgrade deviceadm to 1.4.0.
* Upgrade deviceauth to 1.5.0.
* Upgrade gui to 1.5.0.
* Upgrade inventory to 1.4.0.
* Upgrade mender to 1.5.0.
* Upgrade mender-api-gateway-docker to 1.5.0.
* Add mender-cli 1.0.0.
* Add mender-conductor 1.0.0.
* Add mender-conductor-enterprise 1.0.0.
* Upgrade useradm to 1.5.0.

#### mender (1.5.0)
* FIXED: HTTP error 401 is not handled by all states
  ([MEN-1854](https://tracker.mender.io/browse/MEN-1854))
* Mender client key generator script


## Mender v1.4.2

_Released 06.07.2018_

#### gui (1.4.1)
* Fix elusive bug which sometimes caused GUI to restart over
  and over due to not finding uglifyjs.

#### integration (1.4.2)
* Upgrade gui to 1.4.1.


## Mender v1.4.1

_Released 06.04.2018_

#### integration (1.4.1)
* Switched to using Intel x86_64 hardware accelerated client
  instead of ARM emulator.
* Add --kvm option to demo scripts to run client VM hardware accelerated.
* Switch default client container type to qemux86-64.
* Upgrade mender to 1.4.1.

#### mender (1.4.1)
* FIXED: Log writes not flushed from memory
  ([MEN-1726](https://tracker.mender.io/browse/MEN-1726))
* Regenerate keys on all key errors, not just when keys are missing.
  ([MEN-1823](https://tracker.mender.io/browse/MEN-1823))
* Mender client key generator script


## meta-mender rocko-v2018.05

_Released 05.09.2018_

## meta-mender rocko-v2018.05
* mender: Copy data partition images to the deploy dir.
* Fix mender not building if build and host architecture is the same.
* Increased the demo mender-retry-polling interval
  ([MEN-1006](https://tracker.mender.io/browse/MEN-1006))
* Fix failed uboot.env install when mender-uboot feature is disabled.
* Implement GRUB and x86-64 support.
  ([MEN-1430](https://tracker.mender.io/browse/MEN-1430), [MEN-1432](https://tracker.mender.io/browse/MEN-1432), [MEN-1433](https://tracker.mender.io/browse/MEN-1433), [MEN-1434](https://tracker.mender.io/browse/MEN-1434), [MEN-1435](https://tracker.mender.io/browse/MEN-1435), [MEN-1436](https://tracker.mender.io/browse/MEN-1436))
* Implement qemux86-64 machine target.
  ([MEN-1430](https://tracker.mender.io/browse/MEN-1430), [MEN-1432](https://tracker.mender.io/browse/MEN-1432), [MEN-1433](https://tracker.mender.io/browse/MEN-1433), [MEN-1434](https://tracker.mender.io/browse/MEN-1434), [MEN-1435](https://tracker.mender.io/browse/MEN-1435), [MEN-1436](https://tracker.mender.io/browse/MEN-1436))
* Make sure auto provided fw-utils use virtual/bootloader setting if present.
* Add Mender 1.5.0 Beta recipe.
* mender: Use only the basename to load DTBs.
* mender: Conditionally add /uboot mount only for SDCards.
* Make sure that new-style "enp" network devices get DHCP address in demo.
* mender: Allow for forcing a specific KERNEL_IMAGETYPE.
* Remove unused IMAGE_UENV_TXT_FILE variable.


## Mender v1.5.0b1

_Released 05.15.2018_

#### deployments (1.5.0b1)
* display number of devices targeted when listing deployments
* possible to upload artifacts to specific tenant via internal API
  ([MEN-1775](https://tracker.mender.io/browse/MEN-1775))
* add ability to filter on deployment creation timestamps

#### deviceauth (1.5.0b1)
* trigger device provisioning workflow only if the device is not currently accepted
* device count endpoint handles preauthorized devices
* moved to globalsign/mgo

#### gui (1.5.0b1)
* Fix bug where recent deployment stats were being called repeatedly on dashboard
* Display version in UI
* Redesign Devices sections, added Rejected devices tab
* Display a dialog after first deployment as part of onboarding
* Move main navigation to be left aligned

#### integration (1.5.0b1)
* Switched to using Intel x86_64 hardware accelerated client
  instead of ARM emulator.
* Make the integration version available to the UI
  ([MEN-1767](https://tracker.mender.io/browse/MEN-1767))
* mender-conductor container is now based on
  github.com/mendersoftware/mender-conductor repository.
* Add --kvm option to demo scripts to run client VM hardware accelerated.
* Introduce optional mender-conductor container based on
  github.com/mendersoftware/mender-conductor-enterprise, for Enterprise
  installations.
* migrate to setup with mender-conductor-enterprise image
* Switch default client container type to qemux86-64.
* Upgrade deployments to 1.5.0b1.
* Upgrade deviceadm to 1.4.0b1.
* Upgrade deviceauth to 1.5.0b1.
* Upgrade gui to 1.5.0b1.
* Upgrade inventory to 1.4.0b1.
* Upgrade mender to 1.5.0b1.
* Upgrade mender-api-gateway-docker to 1.5.0b1.
* Add mender-conductor 1.0.0b1.
* Add mender-conductor-enterprise 1.0.0b1.
* Upgrade useradm to 1.5.0b1.
* migrate to setup with mender-conductor image

#### mender (1.5.0b1)
* Regenerate keys on all key errors, not just when keys are missing.
  ([MEN-1823](https://tracker.mender.io/browse/MEN-1823))
* cli: New client option to show installed artifact name
  ([MEN-1806](https://tracker.mender.io/browse/MEN-1806))
* Spontaneous-reboot hardening of the client
  ([MEN-1187](https://tracker.mender.io/browse/MEN-1187))
* FIXED: Log writes not flushed from memory
  ([MEN-1726](https://tracker.mender.io/browse/MEN-1726))
* Allow multiple digit partition numbers.
* log request-id in case of bad API requests
  ([MEN-1738](https://tracker.mender.io/browse/MEN-1738))
* Abort upgrade if artifact name is not retrievable from artifact_info
  ([MEN-1824](https://tracker.mender.io/browse/MEN-1824))

#### mender-api-gateway-docker (1.5.0b1)
* Allow cross-origin requests from hostnames listed in ALLOWED_HOSTS
* When a client exceeds its rate limit gateway returns 429 (Too
  Many Requests) instead of 503 (Service Temporarily Unavailable)

#### useradm (1.5.0b1)
* New internal endpoint for deleting authentication tokens.


## Mender v1.4.0

_Released 03.20.2018_

#### integration (1.4.0)
* Upgrade deployments to 1.4.0.
* Upgrade deviceadm to 1.3.0.
* Upgrade deviceauth to 1.4.0.
* Upgrade gui to 1.4.0.
* Upgrade inventory to 1.3.0.
* Upgrade mender to 1.4.0.
* Upgrade mender-api-gateway-docker to 1.4.0.
* Upgrade mender-artifact to 2.2.0.
* Upgrade useradm to 1.4.0.

#### mender (1.4.0)
* Allow multiple digit partition numbers.


## meta-mender rocko-v2018.03

_Released 03.19.2018_

#### meta-mender rocko-v2018.03
* mender upgraded to 1.4.0.
* mender-artifact upgraded to 2.2.0.
* Document SDIMG_ROOTFS_TYPE settings for Raspberry Pi.
* Fix creating ubifs image.
* mender-qemu: increase qemu memory size to 256MiB.
* meta-mender-toradex-nxp: increase layer priority to 91


## meta-mender rocko-v2018.02

_Released 02.02.2018_

#### meta-mender rocko-v2018.02
* mender: Append to fstab rather than replacing it.
* Add mender-1.4.0b1 and mender-artifact-2.2.0b1 recipes.
* Fix 'depends upon non-existent task' error in U-Boot recipes without auto patching.
* Add mender-1.3.1 and mender-artifact-2.1.2 recipes.
* QEMU: Raise systemd service timeout so that it boots properly on slow hosts.
* Added new state script to wait for time sync to complete.
* Fix "No rule to make target 'envtools'" error in some U-Boot builds.
* Pregenerate SSH keys for all QEMU images.


## Mender v1.4.0b1

_Released 02.09.2018_

#### deployments (1.4.0b1)
* updated aws-go-sdk to v1.12.27
* delete artifact from storage if parsing failed

#### deviceadm (1.3.0b1)
* PUT /devices/{id}/status (internal)

#### gui (1.4.0b1)
* Add checkbox option to remain logged in
* add progress bar for individual devices updates
  ([MEN-1558](https://tracker.mender.io/browse/MEN-1558))
* make it possible to decommission a device that has never sent inventory
* add request ID to snackbar
* Added deployments in progress to header bar
* Add Device notifications to top bar
* Fix for showing incorrect device IDs
  ([MEN-1536](https://tracker.mender.io/browse/MEN-1536))

#### integration (1.4.0b1)
* Upgrade Conductor to 1.8.1
* replace dynomite with redis
* fix http 404 on decommissioning
* Update integration version references to 1.4.x.
* Upgrade deployments to 1.4.0b1.
* Upgrade deviceadm to 1.3.0b1.
* Upgrade deviceauth to 1.4.0b1.
* Upgrade gui to 1.4.0b1.
* Upgrade inventory to 1.3.0b1.
* Upgrade mender to 1.4.0b1.
* Upgrade mender-api-gateway-docker to 1.4.0b1.
* Upgrade mender-artifact to 2.2.0b1.
* Upgrade useradm to 1.4.0b1.
* replace dynomite with redis

#### inventory (1.3.0b1)
* Get all devices in a group with a single api-call.
  ([MEN-811](https://tracker.mender.io/browse/MEN-811))

#### mender (1.4.0b1)
* Report update status for scripts and states
  ([MEN-1015](https://tracker.mender.io/browse/MEN-1015))
* Print detailed logs about authorization errors.
  ([MEN-1660](https://tracker.mender.io/browse/MEN-1660), [MEN-1661](https://tracker.mender.io/browse/MEN-1661))
* mender-device-identity: Check if file exists before reading
  Mender on orangepi fails to run because identity script exit with error like:
  /usr/share/mender/identity/mender-device-identity
  cat: can't open '/sys/class/net/bonding_masters/type': Not a directory
  Add check before reading type to avoid problems.
* Remove trailing slash from server URL configuration.
  ([MEN-1620](https://tracker.mender.io/browse/MEN-1620))

#### mender-artifact (2.2.0b1)
* Fix ECDSA failures while signing and verifying artifact.
  ([MEN-1470](https://tracker.mender.io/browse/MEN-1470))
* Fix broken header checksum verification.
  ([MEN-1412](https://tracker.mender.io/browse/MEN-1412))
* Add modify existing images and artifacts functionality.
  ([MEN-1213](https://tracker.mender.io/browse/MEN-1213))
* Artifact version 3 format documentation
  ([MEN-1667](https://tracker.mender.io/browse/MEN-1667))
* Mender-Artifact now returns an error code to the os on cli errors
  ([MEN-1328](https://tracker.mender.io/browse/MEN-1328))
* mender-artifact now fails with whitespace in the artifact-name
  ([MEN-1355](https://tracker.mender.io/browse/MEN-1355))

#### mender-api-gateway-docker (1.4.0b1)
* reload-when-hosts-changed: silence cmp output
* From now on it is possible to set rate limit per IP address
  for the API using environment variables.
  There are two variables:
  RATE_LIMIT_GLOBAL_RATE=limit - number of request per second
  RATE_LIMIT_GLOBAL_BURST=burst - burst parameter defines
  how many requests a client can make in excess
  of the rate specified by the limit.
  Both parameters, limit and burst, should be numbers.
* entrypoint: include mender-gui in monitored DNS names


## meta-mender rocko-v2018.01

_Released 01.04.2018_

* meta-mender-core: Allow dtbos in KERNEL_DEVICETREE

## meta-mender rocko-v2017.12

_Released 12.20.2017_

* mender-artifact: Fix build failure due to poky golang source directory changes.
* Catch up with latest poky U-Boot v2017.05.
* Fix build failure after poky switched to checking out Go
  sources under the full GOPATH.
* rpi-u-boot-scr: Switch to boot.cmd.in style recipe.
* sato: Set NETWORK_MANAGER to systemd.
* Update example-state-scripts to use standard logging.
* Add Mender 1.3.0b1 recipe.
* Work around bug in libpseudo regarding file owners on data partition.
* Add machine configuration for Mender on colibri-imx7
* u-boot: update mender_boot_part_name when mender_boot_part changes
* Remove meta-mender-beaglebone layer. This layer is not
  needed anymore for compiling for Beaglebone and should be removed from
  all build configurations.
  ([MEN-1387](https://tracker.mender.io/browse/MEN-1387))
* Add example recipe to show how to deploy files into Mender persistent data partition
* mender-artifact: Fix build failure due to poky golang support changes.
* meta-mender-raspberrypi: increase layer priority to 10
* Fix bug where MENDER_DEVICE_TYPES_COMPATIBLE would only accept one entry.
* mender: Adjust patches for U-Boot v2017.09
* mender: Use GO environment variable to launch the compiler
* Implement heuristic automatic patching of U-Boot.
  It can be turned on and off by setting `MENDER_UBOOT_AUTO_CONFIGURE`
  to `1` and `0`, respectively, in a `u-boot.bbappend` file. It is on by
  default. If the automatic patching is unsuccessful, there is a special
  bitbake target that can be used to extract the generated patch and use
  it as a basis for a manual patch. It can be invoked with `bitbake -c
  save_mender_auto_configured_patch <u-boot-recipe>`, where
  `<u-boot-recipe>` is either `u-boot` or the fork of U-Boot that your
  board uses. ([MEN-1387](https://tracker.mender.io/browse/MEN-1387))
* Bump mender and mender-artifact to version 1.1.0 and 2.0.0, respectively.
* Remove recipes for Mender 1.0.x series.
* Add Mender 1.3.0 build recipe.


## meta-mender pyro-v2017.12

_Released 12.20.2017_

* Fix bug where MENDER_DEVICE_TYPES_COMPATIBLE would only accept one entry.
* Add Mender 1.3.0 build recipe.
* u-boot: update mender_boot_part_name when mender_boot_part changes
* Update example-state-scripts to use standard logging.
* meta-mender-raspberrypi: increase layer priority to 10
* sato: Set NETWORK_MANAGER to systemd.
* Add machine configuration for Mender on colibri-imx7


## Mender v1.3.0

_Released 12.21.2017_

#### integration (1.3.0)
* Upgrade deployments to 1.3.0.
* Upgrade deviceadm to 1.2.0.
* Upgrade deviceauth to 1.3.0.
* Upgrade gui to 1.3.0.
* Upgrade inventory to 1.2.0.
* Upgrade mender to 1.3.0.
* Upgrade mender-api-gateway-docker to 1.3.0.
* Upgrade useradm to 1.3.0.

#### mender (1.3.0)
* Remove trailing slash from server URL configuration.
  ([MEN-1620](https://tracker.mender.io/browse/MEN-1620))


## meta-mender pyro-v2017.11

_Released 11.14.2017_

* Add Mender 1.3.0b1 recipe.
* Upstream image has grown significantly, increase to 608MB sdimg.
  The noticeably non-round number is to make sure the calculated rootfs
  size is divisible by the partition alignment.


## Mender v1.3.0b1

_Released 11.14.2017_

#### deployments (1.3.0b1)
* docs: dump expire parameter from artifact download endpoint
* deployments/controller: handle substate field in device status updates
* images: make artifact download links valid for 15 minutes only
* deployments: descending sort by created time when listing deployments
* deployments/controller: status report substate field length limited to 200 characters
* Additional MongoDB configuration options: mongo_ssl, mongo_ssl_skipverify, mongo_username, mongo_password
* docs/management: return device state and substate in device deployment info
* limits: add GET /limits/storage management endpoint
* deployments: make artifact download links valid for 1 hour only
* Prevent artifacts with invalid checksums from
  being uploaded to the server.
  ([MEN-1412](https://tracker.mender.io/browse/MEN-1412))
* docs/internal: spec for GET /tenants/:id/limits/storage
* Additional MongoDB configuration options: mongo_ssl, mongo…
* docs: document that expire on /artifacts/{id}/download is silently ignored
* POST /api/v1/internal/tenants ep
* docs/devices: add optional substate field in status ported

#### deviceadm (1.2.0b1)
* middleware: accommodate changes in request{id,log} middleware and enable request logger update
* Additional MongoDB configuration options: mongo_ssl, mongo_ssl_skipverify, mongo_username, mongo_password
* Additional MongoDB configuration options: mongo_ssl, mongo…
* store/mongo: move single tenant migration to separate func
* main: add 'migrate [--tenant=<tenant ID>]' command

#### deviceauth (1.3.0b1)
* GET /devices/count?status endpoint
* devauth: only one accepted authset
  When accepting an auth set, reject all other accepted auth sets of a particular
  device. This way we make sure that only one auth set is accepted at a time. In
  case when key rotation is used, old key cannot be used to obtain the token.
  ([MEN-1417](https://tracker.mender.io/browse/MEN-1417))
* store/mongo: properly setup context for migrations in multi tenant
* api/http: support for internal endpoint for setting per-tenant limits
  Add support for PUT operation on a new internal endpoint
  `/api/internal/v1/devauth/tenant/:id/limits/:name`. The endpoint is used for
  setting per tenant limits.
* store/mongo: make UpdateAuthSet() operate on multiple auth sets
* store, store/mongo: add collection for keeping 'Limits'
* devauth: ignore store.ErrAuthSetNotFound when rejecting auth sets during accept
* devauth: set Authorization field in  device decommissioning requests
* devauth: support for saving per-tenant limits
* devauth: log a message when the token is does not have a mender.device claim
* docs: include Authorization header in spec of authset status PUT endpoint
* Additional MongoDB configuration options: mongo_ssl, mongo_ssl_skipverify, mongo_username, mongo_password
* migrate --tenant=... cli
* store/mongo: raise store.ErrAuthSetNotFound when no auth sets were updated
* model: add Limit wrapper, add predefined limit name - max_device_count
* jwt: add mender.device claim, type bool, defaults to false
* docs/internal: remove 404 status on PUT /tenant/:id/limits/max-device-count
* middleware: repacking of logger and request ID to context is no longer needed
* docs: add spec for GET /limits/max_devices
* devauth: set and verify mender.device claim
  Device tokens given out by deviceauth service will now have 'mender.device'
  claim set to true. Tokens without the claim will fail verification and will be
  rejected. Device is expected to request a new token.
* client/orchestrator: pass 'authorization' parameter in device decommission request

#### gui (1.3.0b1)
* Fix logout issues, only timeout user when inactive
* Fix for showing incorrect device IDs
  ([MEN-1536](https://tracker.mender.io/browse/MEN-1536))
* Added onboarding helptips that toggle on/off per user
* Added API connection error messaging and timeouts to Deployments tab
* Added API timeouts and disconnection error retry messages to devices and artifacts tabs
* disable decommissioning button while request is in progress
* API connection error and retry for deployments on dashboard

#### integration (1.3.0b1)
* compose, template: set mender-inventory command to `server --automigrate`
  Ensure that inventory service starts in daemon mode and automatically applies DB
  migrations.
* Fix Missing restart policy for some containers in
  docker-compose setup.
  ([MEN-1556](https://tracker.mender.io/browse/MEN-1556))
* Update conductor to 1.7.7
* allow access to https://localhost in test environment
* Update conductor to 1.7.7
* Upgrade deployments to 1.3.0b1.
* Upgrade deviceadm to 1.2.0b1.
* Upgrade deviceauth to 1.3.0b1.
* Upgrade gui to 1.3.0b1.
* Upgrade inventory to 1.2.0b1.
* Upgrade mender to 1.3.0b1.
* Upgrade mender-api-gateway-docker to 1.3.0b1.
* Upgrade useradm to 1.3.0b1.
* conductor: include Authorization header in decommissioning workflow

#### inventory (1.2.0b1)
* main: add server [--automigrate] command, drop previous command line flags
  Command line invocation and parameters are changed. See --help output for
  details.
  `server` subcommand will start the services in 'daemon' mode (sans the forking
  part). Optional `--automigrate` argument enables automatic DB migration,
  otherwise then a migration is needed the service will exit logging an error.
* Additional MongoDB configuration options: mongo_ssl, mongo_ssl_skipverify, mongo_username, mongo_password
* main: add 'migrate [--tenant=<tenant ID>]' command
* middleware: accommodate changes in request{id,log} middleware and enable request logger update
* dockerfile: update entrypoint to match currently supported command line arguments
* Additional MongoDB configuration options: mongo_ssl, mongo…

#### mender (1.3.0b1)
* Mender now logs whatever a state-script outputs to stderr
  ([MEN-1349](https://tracker.mender.io/browse/MEN-1349))
* mender-device-identity: only collect MAC from ARPHRD_ETHER types
* Fix 'unexpected EOF' error when downloading large updates.
  ([MEN-1511](https://tracker.mender.io/browse/MEN-1511))
* Implement ability for client to resume a download from
  where it left off if the connection is broken.
  ([MEN-1511](https://tracker.mender.io/browse/MEN-1511))
* Improve error messages for state scripts errors.
  Rely on the full error description instead of just the error code.
* Fix compile for ARM64.
* set return code = 2, when there is nothing to commit
* Added retry-later functionality on top of the state-script functionality
* Correctly fail state script execution if stderr can not be opened.
  It would not be impossible to continue execution in this case, but it
  is bad to lose log output, and not being able to open stderr is a
  pretty uncommon case that might indicate a more serious issue like
  resource starvation.

#### mender-api-gateway-docker (1.3.0b1)
* Introduce static content caching for /ui routing.
* Make browser side UI caching configurable though CACHE_UI env. Disabled by default.
* Include request time in gateway access logs.
* nginx: separate HTTP and HTTPS server scopes, redirect all HTTP requests to HTTPS
* nginx: align gateway URLs with useradm API
* Introduce static content caching for /ui routing.
* deployments service routing
* gateway dns cache reloading for improved recovery from service restarts
  ([MEN-1227](https://tracker.mender.io/browse/MEN-1227))
* Include request time in gateway access logs.

#### useradm (1.3.0b1)
* docs: add undocumented X-Original-URI, X-Original-Method on internal /auth/verify
* store/mongo: TenantDataStore uses a store with automigrations enabled
* commands: add 'migrate [--tenant=<id>]' command
* middleware: accommodate changes in request{id,log} middleware and enable request logger update
* jwt: add mender.user claim, bool
  Add 'mender.user' claim to tokens given out bu useradm. The claim indicates that
  the token is assigned to a user and a 'sub' claim corresponds to user ID.
* store/mongo: With*() helpers return a new instance of store with correct property modified
* docs: spec for an endpoint for setting up tenants
* commands: propagate new user to tenantadm
  ([MEN-1311](https://tracker.mender.io/browse/MEN-1311))
* store/mongo: move migration of single tenant to separate func
* api/http: update internal URLs, align them with API URL schema
  Internal URLs are now available with /api/internal/v1/useradm/ prefix
* store: introduce tenant keeper
* docs: align internal URLs with API URL scheme
* useradm: add mender.user claim to given out tokens
  Append 'mender.user' claim to all given out tokens. All tokens that do not have
  this claim will fail verification and be rejected forcing the user to log in again.
* set correct header when sending token
* useradm: add CreateTenant operation
* api/http: add endpoint for creating tenants


## Mender v1.2.2

_Released 11.14.2017_

#### deployments (1.2.2)
* deployments: descending sort by created time when listing deployments

#### integration (1.2.2)
* Upgrade deployments to 1.2.2.
* Upgrade gui to 1.2.1.
* Upgrade mender-api-gateway-docker to 1.2.1.
* Fix Missing restart policy for some containers in
  docker-compose setup.
  ([MEN-1556](https://tracker.mender.io/browse/MEN-1556))

#### mender-api-gateway-docker (1.2.1)
* nginx: separate HTTP and HTTPS server scopes, redirect all HTTP requests to HTTPS


## Mender v1.2.1

_Released 10.02.2017_

#### deployments (1.2.1)
* Prevent artifacts with invalid checksums from
  being uploaded to the server.
  ([MEN-1412](https://tracker.mender.io/browse/MEN-1412))

#### integration (1.2.1)
* Upgrade deployments to 1.2.1.
* Upgrade mender to 1.2.1.
* Upgrade mender-artifact to 2.1.1.

#### mender (1.2.1)
* Improve error messages for state scripts errors.
  Rely on the full error description instead of just the error code.
* Fix checksum not being verified for headers, only
  payload. ([MEN-1412](https://tracker.mender.io/browse/MEN-1412))

#### mender-artifact (2.1.1)
* Fix broken header checksum verification.
  ([MEN-1412](https://tracker.mender.io/browse/MEN-1412))


## Mender v1.2.0

_Released 09.05.2017_

#### deployments (1.2.0)
* Deployment creation process changed. From now on artifacts are
  assigned to device deployments on update request handling.
* Return 422 - Unprocessable Entity on attempt of creating deployment without artifacts
* Deployments no longer require inventory to create deployments.
* New optional array field: 'artifacts' in deployment object returned by API containing list of artifact ids used by deployment.

#### deviceauth (1.2.0)
* Introduce 'server' subcommand that is also default command. Supports '--automigrate' parameter to enable automatic database version migration on startup.
* Increase orchestrater request timeout to 30s

#### gui (1.2.0)
* Bugfix for multiplying GET devices requests
* Add ‘create user’ functionality
* Change root API url to docker.mender.io
* Removed user creation UI incl password strength check (#231)
* Added user management edit functionality
* Updated node modules
* Remove shortened device IDs, now useless due to incremental SHAs
* create deployment from single device ([MEN-1233](https://tracker.mender.io/browse/MEN-1233))
* Allow user to remove artifacts via the GUI
* Added self user management

#### integration (1.2.0)
* Move interactive flags for client container to main docker file.
  Makes it available for debugging on all client containers, not just
  dev containers.
* allow access to https://localhost in test environment

#### mender (1.2.0)
* Refactored all store implementations into /store
* Improve error message when manifest field/file cannot be read.
* Fixed format check to conform to the expected artifact-file-format
  ([MEN-1289](https://tracker.mender.io/browse/MEN-1289))
* installer: improve incompatible image error message
* Client will not run state scripts from cmd-line except when forced.
  ([MEN-1235](https://tracker.mender.io/browse/MEN-1235))
* Fixed behaviour when no sys-cert is available on the system.
  ([MEN-1151](https://tracker.mender.io/browse/MEN-1151))
* Mender now logs whatever a state-script outputs to stderr
  ([MEN-1349](https://tracker.mender.io/browse/MEN-1349))
* Fix misleading version being displayed for non-tagged builds.
  ([MEN-1178](https://tracker.mender.io/browse/MEN-1178))
* Changed the errormessage to more closely reflect the issue.
  ([MEN-1215](https://tracker.mender.io/browse/MEN-1215))
* Removed the DeviceKey option in menderConfig.
* Fix - Now throws an error when committing nothing.
  ([MEN-505](https://tracker.mender.io/browse/MEN-505))
* Introduction of state script feature. State scripts can be
  used to execute scripts at various stages of Mender's execution. See
  documentation for more information.
* Introduce experimental support for writing to UBI volumes
* Logs an error when device_type file not found.
  ([MEN-505](https://tracker.mender.io/browse/MEN-505))
* remove no longer referenced client certificate code

#### mender-api-gateway-docker (1.2.0)
* Return additional headers for improved security: X-XSS-Protection, Cache-Control, Pragma. ([MEN-1316](https://tracker.mender.io/browse/MEN-1316))
* Validate Origin header if present. ([MEN-1287](https://tracker.mender.io/browse/MEN-1287))
* Add a configurable Host whitelist to gateway configuration, denying requests with unknown Hosts. Configured through ALLOWED_HOSTS env var on gateway startup. ([MEN-1262](https://tracker.mender.io/browse/MEN-1262))

#### mender-artifact (2.1.0)
* Sign existing artifacts using mender-artifact CLI
  ([MEN-1220](https://tracker.mender.io/browse/MEN-1220))
* Improve error message when private signing key can't be loaded.
* Fix misleading version being displayed for non-tagged builds.
  ([MEN-1178](https://tracker.mender.io/browse/MEN-1178))
* Mender-Artifact now returns an error code to the os on cli errors
  ([MEN-1328](https://tracker.mender.io/browse/MEN-1328))
* mender-artifact now fails with whitespace in the artifact-name
  ([MEN-1355](https://tracker.mender.io/browse/MEN-1355))

#### useradm (1.2.0)
* Improve log messages when opening connection to MongoDB.
* Additional MongoDB configuration options: mongo_ssl, mongo_ssl_skipverify, mongo_username, mongo_password
* Remove 'initial user' login logic, including 'POST /users/initial' API. Now initial user need to be created by administrator using cli ([MEN-1034](https://tracker.mender.io/browse/MEN-1034))
* New cli subcommand for creating users: 'useradm create-user. ([MEN-1034](https://tracker.mender.io/browse/MEN-1034))
* New API for listing users: 'GET https://localhost/api/management/v1/useradm/users' and 'GET https://localhost/api/management/v1/useradm/users/:userid'
* New API for creating additional users: 'POST https://localhost/api/management/v1/useradm/users'
* New API for editing user email and password: 'PUT https://localhost/api/management/v1/useradm/users/:userid'
* New API for removing user: 'DELETE https://localhost/api/management/v1/useradm/users/:userid'


## Mender v1.1.0

_Released 06.16.2017_

#### gui

* Remove shortened device IDs, now useless due to incremental SHAs
* Fix for [MEN-1233](https://tracker.mender.io/browse/MEN-1233) - create deployment from single device

#### mender

* Fix misleading version being displayed for non-tagged builds. ([MEN-1178](https://tracker.mender.io/browse/MEN-1178))


## Mender v1.1.0 Beta 1

_Released 05.24.2017_

#### deployments
* Increase file upload request validity when pushing artifact to remote file storage.
* Update artifact handling reflecting changes in mender-artifact.
* Support for signed images introduced, but with no signature
  verification yet. ([MEN-1022](https://tracker.mender.io/browse/MEN-1022))
* Add device decommissioning support in the deployments service.
* Update artifact description when updating artifact data.
* images/s3: unmarshal S3 errors when uploading image
* Artifact upload error handling fixed.
* Update artifact description when updating artifact data. ([MEN-1093](https://tracker.mender.io/browse/MEN-1093))
* travis: bump required Go version to 1.8

#### deviceadm
* Support for listing device authentication data sets with device ID
  filter using GET /devices?device_id=<devid>

#### deviceauth
* New feature: decommissioning device
* devauth: improve logging when rejecting or giving out tokens
* Decommission device endpoint implemented (without
  decommission job submit).
* api/management: management API is publicly available, update misleading description
* api: add tenant_token as an optional attribute in authentication request

#### gui
* Artifact signed field and improvements ([MEN-230](https://tracker.mender.io/browse/MEN-230))
* Bugfix: hide placeholder when past deployments is not empty ([MEN-229](https://tracker.mender.io/browse/MEN-229))
* Device blocking & decommissioning ([MEN-226](https://tracker.mender.io/browse/MEN-226))
* Implement pagination UI on pending & in progress deployment lists ([MEN-222](https://tracker.mender.io/browse/MEN-222))

#### integration
* Upgrade all server components to 1.1 series
* Upgrade client to 1.1
* Upgrade mender-artifact to 2.0

#### inventory
* No changes

#### mender-api-gateway-docker
* nginx: log and pass X-MEN-RequestID

#### mender-artifact
* Switch default artifact format version to 2. ([MEN-1183](https://tracker.mender.io/browse/MEN-1183))
* Add CLI support for signing and verifying images.
* Add implementation of RSA and ECDSA signatures.
* Fix returning and printing errors form artifact library.
* Fix overwriting artifact if new one is invalid.
* Add basic signing functionality and rewrite the library.

#### mender
* Add support for using signed mender-artifact library.
* Add support for verifying artifact signature. ([MEN-1020](https://tracker.mender.io/browse/MEN-1020))

#### useradm
* Added `create-user` and `server` commands to useradm. Running
  `useradm server` will start useradm service (just like running `useradm` did),
  also if no command is passed `server` is used a default. `create-user` will add
  given user to DB. Examples: `useradm create-user --username foo@bar.com
  --password foobarbarbar` (creates a user with username foo@bar.com and password
  foobar...), `useradm create-user --username foo@bar.com` (same as before, but
  password is read from terminal). See `--help` for details.


## Mender v1.0.1
_Released 04.05.2017_

### Notable changes

#### deployments

* Update artifact description when updating artifact data. (MEN-1093)
* Fix log flag not being set for device deployment after log been uploaded.
  (MEN-1078)

#### gui

* Bugfix: open correct deployment report dialog from dashboard
* Update node modules, add drag+drop artifact, allow edit
  artifact description
* Move user token from local storage to cookie, add react-cookie module (#217)
* Update node modules, add drag+drop & cookie functionality (#219)
* Replace artifact upload dialog with drag-and-drop
* Remove cookie when receiving unauthorized response
* Edit artifact description in UI

#### mender

* Fix bug that caused the update not to be retried after failing during
  previous attempt (#193)

---

## Mender v1.0.0 
_Released 02.20.2017_

---
