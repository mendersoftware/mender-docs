---
title: Operating System updates: Bootloader support (MCUBoot)
taxonomy:
    category: docs
---

## Bootloader support (MCUBoot)

With the zephyr-image Update Module, Mender leverages MCUboot to enable atomic updates on microcontrollers. MCUboot manages two firmware slots: the active slot holds the currently running image, and the inactive slot contains the new update. When an update is deployed, the new firmware is written into the inactive slot, and on reboot, MCUboot swaps the images by placing the new firmware inside the active slot. If the new firmware fails to boot or isn’t confirmed as valid, MCUboot reverts to the previous image to ensure  the device recovers and is not bricked. Note that this mechanism applies when using the zephyr-image Update Module; Mender can work with other bootloaders, provided you implement the corresponding Update Module yourself.

For Mender's Zephyr integration:
* **Enabling MCUboot:** In your Zephyr project configuration, enable the MCUboot bootloader (`CONFIG_BOOTLOADER_MCUBOOT`). This will include the MCUboot build as part of the application (or require you to build MCUboot separately and flash it to the bootloader partition). The Mender reference integration uses Zephyr's *sysbuild* to build MCUboot alongside the application​, simplifying the process.
* **Partition requirements:** Verify that your board's devicetree has the required partitions. You should have:  
  * A `boot_partition` for MCUboot itself.
  * A `slot0_partition` for the primary image.
  * A `slot1_partition` for the secondary image.
  * A `storage_partition` for persistent Mender data. It is recommended to have a separate `mender_partition` but a generic `storage_partition` can be used.
  * **There should be no scratch partition** since the integration uses the **swap without scratch** method which requires contiguous slots and avoids needing a separate scratch area​. Make sure `CONFIG_MCUBOOT_SWAP_USING_SCRATCH` is **disabled** (`MCUBOOT_SWAP_USING_SCRATCH=n`; the default in most cases).
* **Automatic rollback:** The Mender MCU client and MCUboot work together to implement rollback. On the first boot of a new image, MCUboot will mark it as a temporary image. The Mender client then confirms the update by marking the image as permanent once it has started up successfully. If the new firmware does not report success, for example if it crashes or doesn't run the Mender client, MCUboot will revert to the old image upon reboot. This behavior gives similar robustness to Mender's dual rootfs updates on Linux.
