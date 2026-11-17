---
title: Configuration
taxonomy:
    category: docs
---

This section summarizes the key configuration options for the Mender MCU client in ESP-IDF. The client is configured at build time with Kconfig options, which you set in `sdkconfig.defaults` with the `CONFIG_` prefix or with `idf.py menuconfig`.

## Kconfig options

The Mender MCU component makes Kconfig options available under **Component config → Mender client** in `idf.py menuconfig`. Each option has help text explaining its purpose. Below are the most important Kconfig settings:

* `MENDER_SERVER_HOST` – The Mender server's base URL. Defaults to hosted Mender US. For an on-premise server, set `CONFIG_MENDER_SERVER_HOST_ON_PREM=y` and the URL with `CONFIG_MENDER_SERVER_HOST="https://mender.mydomain.org"`.
* `MENDER_SERVER_TENANT_TOKEN` – The tenant token used to authenticate to a Mender server instance. You must set this to connect to the hosted Mender. It is a string provided by the Mender UI. Always treat the tenant token as a secret. If using an open-source Mender server, leave this blank or unset.
* `MENDER_DEVICE_TIER` – The [device tier](../../02.Overview/17.Device-tiers/docs.md) of the device, `micro` or `standard`. Defaults to `micro`. The tier also sets the default update poll and inventory refresh intervals.
* `MENDER_CLIENT_UPDATE_POLL_INTERVAL` – The interval in seconds between update checks. Short intervals like a couple of minutes or hours mean the device will receive updates quickly but use more network/power. Longer intervals conserve resources. Defaults to seven days on the `micro` tier and 30 minutes on `standard`.
* `MENDER_CLIENT_INVENTORY_REFRESH_INTERVAL` – The interval in seconds between inventory reports. Considering the inventory data is static in most cases (device ID, MAC address) it is recommended to send it to the server once every few days. Defaults to seven days on `micro` and eight hours on `standard`.
* `MENDER_DEVICE_TYPE` – The device type string reported by the client. By default, this is the ESP-IDF target, for example `esp32s3`. This must match one of the Compatible types specified in your Mender Artifacts as Mender ensures compatibility with the board and the software being deployed.
* `MENDER_ARTIFACT_NAME` – The name of the Mender Artifact the build generates from the application binary. Required unless you disable the Artifact generation with `MENDER_ARTIFACT_GENERATE`.
* `MENDER_LOG_LEVEL_DBG`, `MENDER_LOG_LEVEL_INF`, etc. – These control the log level of the Mender client's internal logging. Defaults to `MENDER_LOG_LEVEL_INF`.

## Certificates and TLS

The client verifies the server certificate with ESP-IDF's [certificate bundle](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/protocols/esp_crt_bundle.html?target=_blank), which works with hosted Mender. For a server with a self-signed certificate, add its CA certificate with `CONFIG_MBEDTLS_CUSTOM_CERTIFICATE_BUNDLE=y` and `CONFIG_MBEDTLS_CUSTOM_CERTIFICATE_BUNDLE_PATH`.
