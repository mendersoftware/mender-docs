---
title: Overview
taxonomy:
    category: docs
---

!! This section is a preview of Mender's support for microcontroller devices running FreeRTOS with ESP-IDF. It is not yet recommended for production use. Also, expect the APIs and configurations to evolve as the integration matures.

## Overview

Mender enables robust **firmware updates** on resource-constrained devices by integrating with Espressif's ESP-IDF framework, which is based on FreeRTOS, and the ESP-IDF bootloader. This allows microcontroller units (MCUs) to perform atomic, **fail-safe OTA updates** with automatic rollback on failure, similar to Mender's updates for Linux devices.

<!--AUTOVERSION: "supports **ESP-IDF %**"/ignore -->
Mender's microcontroller client (*Mender MCU* or *mender-mcu*) runs as part of the ESP-IDF application firmware. It communicates with the Mender server to report device inventory and identity, checks for available updates, downloads new firmware, and uses ESP-IDF's OTA mechanism to install updates safely. The reference implementation supports **ESP-IDF 6.0**, with Espressif's **ESP32-S3-DevKitC** as the reference board.

This section describes integrating Mender into an ESP-IDF project for full firmware image updates. The high-level components for a Mender-enabled microcontroller device are:
* **Bootloader (ESP-IDF bootloader)**: The device boots via the ESP-IDF bootloader, which manages two OTA app partitions (active and inactive) for A/B updates. The bootloader reverts to the previous image if the new one is not confirmed.
* **Mender MCU client**: Runs within your ESP-IDF application. It periodically connects to the Mender Server to report its current software version and check for updates.
* **Mender Artifacts**: Firmware updates are packaged as Mender Artifacts of type `esp-ota` containing the new application binary. These are uploaded to the server and deployed to devices.
