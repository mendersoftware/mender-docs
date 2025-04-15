---
title: Microcontroller (preview)
taxonomy:
    category: docs
    label: tutorial
---

!! The feature is in preview and not recommended for production use.

We will walk through how to use a Zephyr-based microcontroller (MCU) with Mender and perform an OTA firmware update. We use the **Espressif ESP32-S3-DevKitC** development board running Zephyr as our reference implementation. By the end, you will have the device appearing in your Mender Server and deploy new firmware to it.

This guide assumes you are using **hosted Mender** as the Mender Server (you can sign up for a [free trial](https://hosted.mender.io/ui/signup?target=_blank) if you haven't already) and have the Zephyr development tools installed on your workstation (including the `west` tool and a toolchain for building Zephyr for ESP32).

!!! **Note:** This guide focuses on microcontroller devices (no Linux OS). If you want to update a Linux-based device (e.g. Raspberry Pi), refer to [this Get Started guide](https://docs.mender.io/get-started/preparation).

## Preview

MCU support is in **preview**, which means it's under active development. To ensure everything goes smoothly use the recommended version of Zephyr (v4.0 is recommended) and with the reference board ESP32-S3-DevKitC. Other Zephyr versions and [boards](https://github.com/mendersoftware/mender-mcu-integration?target=_blank&tab=readme-ov-file#build-the-project-for-other-boards) will work, but for first time testing we recommend using exactly these.

The Mender features available are basic full-image updates and sending inventory data; more advanced features (like delta updates, compressed artifacts, signed artifacts, advanced update controls using state scripts, etc.) are not supported on MCUs.

