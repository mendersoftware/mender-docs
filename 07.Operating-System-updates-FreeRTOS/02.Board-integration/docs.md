---
title: Board integration
taxonomy:
    category: docs
---

To use Mender with an ESP-IDF based MCU, you need to integrate the Mender MCU client into your ESP-IDF project and ensure the flash is large enough to hold two firmware partitions. Those are called A and B, or active and inactive.

**ESP-IDF project setup:** Mender provides the mender-mcu repository, which you add to your ESP-IDF project as a component. For example, in `main/idf_component.yml`, add:

```yaml
dependencies:
  mender-mcu:
    git: https://github.com/mendersoftware/mender-mcu.git
    version: main
```

* The ESP-IDF component manager fetches the Mender MCU client on the next `idf.py build` or `idf.py update-dependencies`.
* **Partitions:** Define a custom partition table with an `otadata` partition, two OTA app partitions (`ota_0` and `ota_1`), a `mender` NVS partition for persistent Mender data, and a `mender_logs` partition for deployment logs. For example, the reference application uses this `partitions_mender.csv`:

```
# Name, Type, SubType, Offset, Size, Flags
nvs         ,data ,nvs, 0x9000 ,24K,
otadata     ,data ,ota,        ,0x2000,
mender      ,data ,nvs,        ,32K,
mender_logs ,data ,undefined,  ,8K,
ota_0       ,app  ,ota_0,      ,1536K,
ota_1       ,app  ,ota_1,      ,1536K,
```

**Build configuration:** Set the flash size, the partition table, and the Mender options in your `sdkconfig.defaults`. If your project already has an `sdkconfig`, delete it so these values are applied. For hosted Mender or Mender Enterprise on-premise, you must additionally provide the **Mender Server Tenant token**. For Mender Open Source on-premise Server, adjust the server address and tenant token as required. For example:

```bash
# 8 MB flash on the ESP32-S3-DevKitC
CONFIG_ESPTOOLPY_FLASHSIZE_8MB=y
CONFIG_PARTITION_TABLE_CUSTOM=y
CONFIG_PARTITION_TABLE_CUSTOM_FILENAME="partitions_mender.csv"

CONFIG_MENDER_ARTIFACT_NAME="release-1"
CONFIG_MENDER_SERVER_TENANT_TOKEN="YOUR-TENANT-TOKEN"
# if using a self-hosted Mender server
# CONFIG_MENDER_SERVER_HOST_ON_PREM=y
# CONFIG_MENDER_SERVER_HOST="https://my.mender.server"
```

* We will cover configuration options in detail on the [Configuration](../04.Configuration/docs.md) page. You must also ensure networking is enabled such as WiFi including credentials or Ethernet so that the device can reach the Mender server.

**Client initialization:** The Mender client API requires two callbacks in your application code: an **identity callback** that returns a unique identifier for the device such as a MAC address, for example from `esp_read_mac()`, and a **restart callback** that calls `esp_restart()`. Register the esp-ota Update Module with `mender_esp_ota_register_update_module()` before activating the client. The client API is the same as on Zephyr, see [Customize Mender MCU](../../06.Operating-System-updates-Zephyr/04.Customize-Mender-mcu/docs.md) and the [reference application](https://github.com/mendersoftware/mender-mcu-integration/blob/esp-idf/main/main.c?target=_blank).

`idf.py build` also generates the Mender Artifact `build/<project name>.mender`, which you upload to the Mender Server to deploy it.
