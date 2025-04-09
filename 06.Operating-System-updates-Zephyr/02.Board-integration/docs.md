---
title: Operating System updates: Board integration
taxonomy:
    category: docs
---

## Board integration

To use Mender with a Zephyr-based MCU, you need to integrate the Mender MCU client into your Zephyr project and ensure the board supports the required bootloader and partition layout:
* **Bootloader:** the board must be compatible with MCUboot. You can check the integration requirements at [https://docs.mcuboot.com/readme-zephyr.html](https://docs.mcuboot.com/readme-zephyr.html)
* **Storage:** the board's storage must be large enough and configured to hold two firmware partitions. Those are called A and B, or active and inactive.

**Zephyr project setup:** Mender provides the mender-mcu repository, which you add to your Zephyr **west workspace** as a module. In your west manifest file, include the Mender MCU project. For example, in west.yml, add:

```bash
manifest:
  projects:
    - name: mender-mcu
      url: https://github.com/mendersoftware/mender-mcu
      revision: main
      path: modules/mender-mcu
      import: true
```

* After running `west update`​ it will fetch the Mender MCU client code and Kconfig definitions into your Zephyr workspace​. The Mender client module becomes available to your application after updating the west workspace (west update).  
* **MCUboot and partitions:** Enable MCUboot as the bootloader for your application. In Zephyr, this is typically done by setting `CONFIG_BOOTLOADER_MCUBOOT=y` in your project configuration. Ensure the board's device tree defines the required flash partitions: a bootloader partition, a **slot0** (active) partition for the running image, and a **slot1** (inactive) partition for the incoming update​. Scratch partitions are not used in this integration, as the swap-using-scratch algorithm is not recommended​. Many Zephyr boards already have these partitions defined when MCUboot is enabled. If using Zephyr's **System Build (sysbuild)**, you can build MCUboot and your application together in one step (this is the approach used in Mender's reference application).

**Build configuration:** Set the necessary Kconfig options to include the Mender MCU client in your `prj.conf` or configuration fragment. To enable the MCU client add `CONFIG_MENDER_MCU_CLIENT=y`. For hosted Mender or Mender Enterprise on-premise, you must additionally provide the **Mender Server Tenant token**. For Mender Open Source on-premise Server, adjust the server address and tenant token as required. For example:

```bash
CONFIG_MENDER_MCU_CLIENT=y  
CONFIG_MENDER_SERVER_TENANT_TOKEN="YOUR-TENANT-TOKEN"  
# if using a self-hosted Mender server  
# CONFIG_MENDER_SERVER_HOST="https://my.mender.server"
```

* We will cover configuration options in detail below. You must also ensure networking is enabled such as WiFi including credentials or Ethernet so that the device can reach the Mender server.
* **Application changes:** The Mender client API requires a number of callbacks to be implemented in your application code. Notably, you need to provide an **identity callback** that returns a unique identifier for the device such as a MAC address or chip serial​, and **inventory data** (key-value attributes) to be sent to the server. In most cases, you can use Zephyr's APIs to get a unique ID, for example, `net_if_get_link_addr` to retrieve a MAC for a network interface, and use that as the device identity.
