---
title: Bootloader support (ESP-IDF bootloader)
taxonomy:
    category: docs
---

## Bootloader support (ESP-IDF bootloader)

With the esp-ota Update Module, Mender leverages ESP-IDF's [OTA mechanism](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/ota.html?target=_blank) and bootloader to enable atomic updates on microcontrollers. The device has two OTA app partitions: the active partition holds the currently running image, and the inactive partition receives the update. When an update is deployed, the new firmware is written into the inactive partition and set as the boot partition. If the new firmware fails to boot or isn't confirmed as valid, the bootloader reverts to the previous image to ensure the device recovers and is not bricked.

For Mender's ESP-IDF integration:
* **Enabling rollback:** The esp-ota Update Module (`MENDER_ESP_OTA_UPDATE_MODULE`, enabled by default) automatically enables the bootloader's rollback support (`BOOTLOADER_APP_ROLLBACK_ENABLE`).
* **Partition requirements:** The partition table must have an `otadata` partition and two OTA app partitions, `ota_0` and `ota_1`. See [Board integration](../02.Board-integration/docs.md).
* **Automatic rollback:** The Mender MCU client and the bootloader work together to implement rollback. On the first boot of a new image, the bootloader marks it as pending verification. The Mender client then confirms the update once it has started up successfully. If the new firmware does not report success, for example if it crashes or doesn't run the Mender client, the bootloader will revert to the old image upon reboot.
