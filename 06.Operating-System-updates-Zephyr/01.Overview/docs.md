---
title: Operating System updates: Overview
taxonomy:
    category: docs
---

!! This section is a preview of Mender's support for microcontroller devices running the Zephyr RTOS. It is not yet recommended for production use. Also, expect the APIs and configurations to evolve as the integration matures.

## Overview

Mender enables robust **firmware updates** on resource-constrained devices by integrating with the Zephyr real-time operating system and the MCUboot bootloader. This allows microcontroller units (MCUs) to perform atomic, **fail-safe OTA updates** with automatic rollback on failure, similar to Mender's updates for Linux devices.

<!--AUTOVERSION: "supports **Zephyr %** on boards"/ignore -->
Mender's microcontroller client (*Mender MCU* or *mender-mcu*) runs as part of the Zephyr application firmware. It communicates with the Mender server to report device inventory and identity, checks for available updates, downloads new firmware, and coordinates with MCUboot to install updates safely. The reference implementation supports **Zephyr 4.0.0** on boards that use MCUboot as a bootloader, with Espressif's **ESP32-S3-DevKitC** as the reference board.

This section describes integrating Mender into a Zephyr-based MCU project for full firmware image updates. The high-level components for a Mender-enabled microcontroller device are:
* **Bootloader (MCUboot)**: The device boots via MCUboot, which manages two firmware slots (active and inactive) for A/B updates. MCUboot verifies images and can swap them to a new image and revert them if needed.
* **Mender MCU client**: Runs within the Zephyr application. It periodically connects to the Mender Server to report its current software version and check for updates.
* **Mender Artifacts**: Firmware updates are packaged as Mender Artifacts of type zephyr-image containing the new application binary. These are uploaded to the server and deployed to devices.
