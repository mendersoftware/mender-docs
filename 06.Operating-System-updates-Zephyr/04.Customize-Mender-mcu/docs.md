---
title: Operating System updates: Customize Mender MCU
taxonomy:
    category: docs
---

## Customize Mender MCU

You can customize the Mender MCU client's behavior on microcontrollers. However, Zephyr has no file system for configuration files, these settings are primarily configured at build time (Kconfig options) or by implementing code callbacks. Below are key areas you may want to adjust:

### Server URL and tenant token

By default, the Mender MCU client is configured to communicate with **hosted Mender**, which requires a Tenant Token for the device to authenticate to your account. The hosted Mender server URL and tenant token can be set via Kconfig options:

* `MENDER_SERVER_HOST` – the base URL of the Mender server. By default, this points to hosted Mender (e.g., "https://hosted.mender.io"). If you are using a self-hosted Mender server, change this to your server's URL​, like `CONFIG_MENDER_SERVER_HOST="https://mender.mydomain.org"`.
* `MENDER_SERVER_TENANT_TOKEN` – the authentication token associating the device with your Hosted Mender tenant (`CONFIG_MENDER_SERVER_TENANT_TOKEN="<your token here>"`). This must be set for devices connecting to the Hosted Mender​. You can obtain the token from your Hosted Mender account in the "My organization" menu and compile it into the firmware. If you are using an on-premises Mender server (Open Source or Enterprise), you can leave this token empty or unset as it is not used in non-multi-tenant servers.

### Certificates and TLS

All communication with the Mender server is done over HTTPS. The Mender MCU client uses Zephyr’s TLS API provided by MbedTLS for secure connections. This means the device needs to trust the server’s certificate:

* If connecting to Hosted Mender or a server with a certificate signed by a public CA, you should ensure the relevant **CA certificate** is present on the device. You can bundle the necessary CA cert (for Hosted Mender US instance, the DigiCert Global Root CA is needed, as Hosted Mender uses AWS CloudFront which is signed by DigiCert) into your firmware.
* If connecting to a server with a self-signed certificate, which is common for on-premise testing, you **must** provision that self-signed CA or cert on the device.

The Zephyr way to handle this is by using `tls_credentials_add()` to add the certificate to the TLS stack. Typically, you would:
* Include the PEM or DER formatted CA certificate in your project (for example, as a file that gets compiled into a C array). The integration example shows using CMake’s `generate_inc_file_for_target` to format a certificate file into a C array and embed it into the build​.
* At startup before the client connects, call `tls_credentials_add(TAG, TLS_CREDENTIAL_CA_CERTIFICATE, cert_data, cert_size)`, where TAG is an integer identifier. The Mender client by default looks for two possible tags: a primary and optionally a secondary CA certificate tag. These tags are configured via `CONFIG_MENDER_NET_CA_CERTIFICATE_TAG_PRIMARY` and `*_SECONDARY` in `Kconfig`.


The reference project uses two certificate slots, primary and secondary, to allow for cases where the Mender server might host the artifact download on a different domain (e.g., S3 storage) with a different certificate​. Make sure to enable Zephyr’s TLS support (`CONFIG_NET_SOCKETS_SOCKOPT_TLS=y`) and all required Mbed TLS options. You can check the integration’s prj.conf as an example. It sets a number of `CONFIG_MBEDTLS_*` options to ensure ECDSA, RSA, and required ciphers are enabled for TLS​.

### Polling intervals

Microcontroller devices often need to manage network usage and power, so Mender's polling intervals may need tuning:

* `MENDER_CLIENT_UPDATE_POLL_INTERVAL` – how often the client polls the server for deployment updates.
* `MENDER_CLIENT_INVENTORY_REFRESH_INTERVAL` – how often the client sends inventory data to the server. 


!!! Note: By default, these might be set to values suitable for demo purposes (30 seconds for update polling and 60 seconds for inventory refresh). For production deployments, however, the recommended settings are much longer – typically 1 day for update polling and 14 days for inventory refresh. Longer intervals help reduce power consumption and network load and are aligned with our fair usage policy. Running production devices with demo intervals (e.g., polling every 30 or 60 seconds) is considered unacceptable and may trigger rate limits. We strongly recommend that you adjust these intervals in your `prj.conf` or via menuconfig to ensure both optimal performance and compliance with fair usage standards.

### Device identity

Every Mender device has an identity, which consists of one or more attributes that uniquely identify it. In Mender MCU, you must implement the **identity callback** in code to return the device's identity string​. A common choice is to use a hardware identifier such as a MAC address, chip unique ID, or a combination of attributes. For instance, on an ESP32, you could retrieve and use the base MAC address, like `mac=AA:BB:CC:DD:EE:FF`. The identity is sent to the Mender Server for device authentication. By default, if you do not implement an identity callback, the device will not have an identity and thus cannot be uniquely recognized by the server – so this is a required part of integration. Typically, you will write a small function that populates a buffer with the ID string and register it with the Mender client before activation. The identity callback is created by calling `mender_get_identity_cb` which is defined in the [client API](https://github.com/mendersoftware/mender-mcu/blob/main/include/mender/client.h). This callback is then registered to the MCU client as a part of the callback structure passed to `mender_client_init()`. 

Example of adding device identity:

```C
static mender_identity_t mender_identity = { .name = "mac", .value = "AA:BB:CC:DD:EE:FF"};

mender_err_t
mender_get_identity_cb(const mender_identity_t **identity) {
    if (NULL != identity) {
        *identity = &mender_identity;
        return MENDER_OK;
    }
    return MENDER_FAIL;
}

// Set up Mender client callbacks.
// Other callbacks (for networking, inventory, etc.) should be set as needed.
mender_client_callbacks_t mender_callbacks = {
    .get_identity = mender_get_identity_cb,
    // .network_connect = ...,
    // .restart = ...,
    // etc.
};

void setup_mender_client(void) {
    // Register your callbacks when initializing the Mender client.
    mender_client_init(&mender_client_config, &mender_callbacks);
}
```

More examples can be found inside the [mender-mcu-integration project](https://github.com/mendersoftware/mender-mcu-integration). 

### Inventory

Inventory data is additional information about the device that is reported to the Mender server such as device type, firmware version, hardware revision, etc. It is provided as key-value pairs which can be arbitrarily named. On Linux, inventory data is provided by executable scripts. On Zephyr, you can set up inventory data by constructing key-value pairs and passing them to the client with a callback. You can add an inventory callback by calling `mender_inventory_add_callback`, which is defined in the [inventory API](https://github.com/mendersoftware/mender-mcu/blob/main/include/mender/inventory.h). Callbacks and inventory data are either persistent or dynamic. Persistent data is only queried using the respective callback once, dynamic data is queried with the respective callback at every inventory refresh interval.

Example of adding a persistent callback:

```C
static mender_err_t
persistent_inventory_cb(mender_keystore_t **keystore, uint8_t *keystore_len) {
    static mender_keystore_t inventory[] = { { .name = "Name", .value = "Example value" } };
    *keystore = inventory;
    *keystore_len = 1;
    return MENDER_OK;
}

mender_inventory_add_callback(persistent_inventory_cb, true /* persistent */);
```

This registers one inventory item that the client will send on its inventory update together with some built-in inventory data​. In the example above, `mender_inventory_set()` is called with a static array of items; you could also build this dynamically (e.g., by reading system info). More examples can be found inside the [mender-mcu-integration project](https://github.com/mendersoftware/mender-mcu-integration). 

### Update Module (zephyr-image)

On the Mender Client, Update Modules are external executables or scripts that the Mender Client invokes to install a  specific update type like a Debian package or a container. The Mender MCU client models the Update Modules API. Refer to the [Update Modules chapter in Mender Docs](https://docs.mender.io/artifact-creation/create-a-custom-update-module) for an introduction. In Mender MCU an Update Module is implemented as a set of C callback functions integrated directly into the firmware. This design makes update handling efficient on resource-constrained devices, while still following the standard Mender Update Module workflow (Download, Install, Reboot, Commit, etc.) behind the scenes.

By default, the **zephyr-image Update Module** is compiled in​. This module knows how to handle a Zephyr application binary: writing it to the secondary slot and coordinating with MCUboot for the swap. You do not need to modify this for Zephyr firmware updates on MCUboot integrated Zephyr boards.

#### Custom Update Modules for Special Use Cases

The zephyr-image module covers the standard Zephyr and MCUboot update scenario. Still, Mender’s Update Module framework allows you to implement custom Update Modules to handle other use cases as needed. In Mender MCU, writing a custom module means coding a new set of C callback functions to perform whatever update logic you require and to register that module with the client. A typical use case is if you need to support a different bootloader than MCUboot for your board, or to update a separate MCU or CPU connected to your Zephyr device.

Implementing a custom Update Module involves defining the handler functions for the relevant update states and integrating them into the Mender client. It’s often helpful to use the zephyr-image module’s implementation as a reference – its source code is available in the [Mender MCU repository](https://github.com/mendersoftware/mender-mcu)​ for inspiration and to understand how each state is handled. By following the same patterns, you can tailor a custom Update Module to your device’s needs. You can also look at the dummy Noop Update Module in Mender MCU integration repository to get the barebones of an Update Module that does nothing and implement the states that are required for your update process. Remember to consult the Update Modules chapter for guidance on the expected state flow and behaviors for custom modules​.

### Other settings and callbacks

The Mender MCU client offers additional callbacks and settings:
* **Network connect/release callbacks**: If your device's network interface is not always on, you can provide callbacks to bring it up before an update check and bring it down after​. For instance, a device could power on a modem only when needed. If not required, these can be set to NULL (assuming the network is always available).
* **Reboot (restart) callback**: You can supply a callback that triggers a device reset. If needed, the client may call this to reboot the device after an update is installed​. Often, you can simply use Zephyr's `sys_reboot()` in this callback.
* **Authentication keys**: The Mender client will store its authentication keys and update state in flash. Ensure your Zephyr storage settings (such as enabling NVS or file storage if needed) are compatible. The client manages the specifics internally – on the first run, it generates a device key pair and persists the private key for future authentication.

In summary, customization is done by setting the appropriate **Kconfig options** for build-time configuration and implementing **C callbacks** for runtime behavior. In the next section, we list the essential configuration options and variables available.
