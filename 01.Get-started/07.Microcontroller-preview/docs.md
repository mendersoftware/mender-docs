---
title: Microcontroller
taxonomy:
    category: docs
    label: tutorial
---

We will walk through how to use a Zephyr-based microcontroller (MCU) with Mender and perform an OTA firmware update. We use the **Espressif ESP32-S3-DevKitC** development board running Zephyr 4.2 as our reference implementation. By the end, you will have the device appearing in your Mender Server and deploy new firmware to it.

MCU devices use the **micro device tier** in Mender, which is optimized for resource-constrained devices. The micro tier has longer default polling intervals (1 day for updates, 14 days for inventory) and smaller artifact size limits compared to standard tier Linux devices. See [Device tiers](../../02.Overview/17.Device-tiers/docs.md) for more information.

This guide assumes you are using **hosted Mender** as the Mender Server (you can sign up for a [free trial](https://hosted.mender.io/ui/signup?target=_blank) if you haven't already) and have the Zephyr development tools installed on your workstation (including the `west` tool and a toolchain for building Zephyr for ESP32).

!!! **Note:** This guide focuses on microcontroller devices (micro tier, no Linux OS). If you want to update a Linux-based device (standard tier, e.g. Raspberry Pi), refer to [this Get Started guide](https://docs.mender.io/get-started/preparation).

The Mender features available are basic full-image updates and sending inventory data; more advanced features (like delta updates, compressed artifacts, signed artifacts, advanced update controls using state scripts, etc.) are not supported on MCUs.

