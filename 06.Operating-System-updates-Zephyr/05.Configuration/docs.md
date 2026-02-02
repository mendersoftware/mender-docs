---
title: Configuration
taxonomy:
    category: docs
---


This section summarizes the key configuration options for the Mender MCU client in Zephyr. There are two categories of configuration: compile-time options (Kconfig) which you set before building your firmware, and runtime variables or values which the device determines during operation (often via callbacks or code). Most of the client behavior is controlled via Kconfig options in Zephyr's menuconfig system.

## Kconfig options

Integration of mender-mcu as a Zephyr module makes Kconfig options available under **Modules → mender-mcu** in west menuconfig. These options allow you to configure server connectivity, authentication, and client behavior. Below are the most important Kconfig settings:

* `MENDER_MCU_CLIENT` – Main switch to include the Mender client in the build. Set this to y to enable Mender OTA functionality. If not set, none of the client code is included.
* `MENDER_SERVER_HOST` – The Mender server's base URL. Defaults to the hosted Mender endpoint. Set this to your server's address if not using hosted Mender. Note that this should be the **host URL** without any API path.
* `MENDER_SERVER_TENANT_TOKEN` – The tenant token used to authenticate to a Mender server instance. You must set this to connect to the hosted Mender. It is a string provided by the Mender UI. If using an open-source Mender server, leave this blank or unset.
* `MENDER_CLIENT_UPDATE_POLL_INTERVAL` – The interval in seconds between update checks​. Short intervals like a couple of minutes or hours mean the device will receive updates quickly but use more network/power. Longer intervals conserve resources. Recommended default for production use is once every seven days.
* `MENDER_CLIENT_INVENTORY_REFRESH_INTERVAL` – The Interval in seconds between inventory reports​. You can adjust this based on how frequently you want the device to report its information. Omitting it or leaving the default uses a sensible value, e.g., every few days. Considering the inventory data is static in most cases (device ID, MAC address) it is recommended to send it to the server once every few days (the recommended default for production is seven days).
* `MENDER_DEVICE_TYPE` – The device type string reported by the client. By default, this is derived from Zephyr's board name at build time​. For example, if you build for `esp32s3_devkitc/esp32s3/procpu`, the device will report `esp32s3_devkitc` as its type. This must match the device type specified in your Mender Artifacts as Mender ensures compatibility with the board and the software being deployed. It's recommended to leave this as the default unless you have a specific reason to override it.
* `MENDER_LOG_LEVEL_DBG`, `MENDER_LOG_LEVEL_INF`, etc. – These control the log level of the Mender client's internal logging. Only one of these should be set to y: e.g., `MENDER_LOG_LEVEL_INF` for informational logs or `MENDER_LOG_LEVEL_DBG` for debug logs which is very verbose. If none is set, a default will be used. In development, `DBG` is helpful; in production, `INF` or even higher (`WARN`) might be preferred to reduce log noise​.


To view all available options with descriptions, run `west build -t menuconfig` and navigate to *Modules → mender-mcu*. Each option has help text explaining its purpose. Generally, the defaults are sane for a basic setup such as pointing to a hosted Mender server, but when using hosted Mender or Mender Enterprise on-premises you must at minimum set the Tenant token. For an on-premise installation you need to set the Server URL.

## Variables (runtime)

At runtime, the MCU client does not use a traditional configuration file, but there are a few **variables/values determined at runtime** that you should be aware of:
* **Device identity:** the identity callback in your device’s code determines its unique identity. Ensure that whatever variable or hardware ID you use (e.g., a MAC address stored in a register) is available and stable across reboots. This identity value is sent to the server upon authentication. For example, the identity might be computed and stored in a static buffer each time the device boots and registers.
* **Inventory data:** Inventory key-value pairs can be considered runtime variables. Your application might set these at boot or update them over time. For instance, you might periodically update network information, or device configuration such as location or time zone inventory values. The client will include the current values of all inventory variables on each inventory refresh interval.
* **Authentication keys:** For authentication, the device requires a private key and corresponding certificate or JWT. While the client can auto-generate these keys on first connection to the Mender server it is recommended that you provision the keys, e.g. at the factory, and supply them using Mender’s API. Note that authentication keys, whether generated or provided, persist between updates and are stored in non-volatile storage on the device, usually in internal flash. The location is determined by the Mender client's storage settings (which might use Zephyr's NVS or settings subsystem under the hood). If you need to reset a device's identity or force re-authentication, you might have to wipe this storage, for example, by erasing certain flash pages.
* **Networking status:** If you provide network connect/disconnect callbacks, the availability of the network becomes a runtime state variable. The client will call your connect callback before attempting to reach the server. Ensure that whatever flags or variables you use to track network readiness are correctly handled. For example, if using a modem, a global or static variable might track if the modem is powered on, and your callback would set it and initiate a connection.

In summary, most of the "variables" for Mender on microcontrollers are either compiled in or maintained by the client internally. Unlike Linux, you won't edit config files at runtime. Still, you should design your firmware to supply the needed data, mainly identity/inventory, and handle dynamic conditions like network up/down via the callback system. Once the device is running, any changes to its configuration such as pointing to a different server or changing poll intervals would require building and flashing a new firmware with the new settings. This can be done via Mender as an update.
