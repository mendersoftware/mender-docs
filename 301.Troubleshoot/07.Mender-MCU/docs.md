---
title: Mender MCU
taxonomy:
    category: docs
---

## Mender MCU debugging tips and known limitations

Developing embedded systems with OTA can be complex. This section provides some tips for debugging issues that may arise and notes a few known limitations or things to keep in mind when using Mender MCU with Zephyr.

### Debugging tips

* **Enable debug logs:** If you suspect something is wrong in the client's behavior, enable `CONFIG_MENDER_LOG_LEVEL_DBG=y` to get verbose logging from the Mender client. This will show state transitions, server responses, etc., which is invaluable for troubleshooting.
* **Serial console is your friend:** Always monitor the serial output during testing. It will show you if the device is stuck, rebooting unexpectedly, or if any assertion/exception happens in Zephyr. If the device seems to reboot in a loop, check if MCUboot might be reverting an update (maybe the app didn't confirm in time).
* **Use a debugger:** Zephyr supports GDB debugging via the west attach command for many boards. For example, on an nRF52840 DK, you can attach GDB to the running firmware even after it reboots into a new image. This can help catch issues in the application or in how the Mender client is integrated.
* **Check the Mender server logs/UI:** The server will show if a device is rejecting authentication while being in pending state or due to an incorrect tenant token or if deployments fail to deliver. In hosted Mender, you can see deployment logs, including messages the client sent (like error codes).
* **Networking issues:** If your device isn't appearing on the server, ensure it has network connectivity. Use ping or other diagnostics if your Zephyr app can support it. Make sure the WiFi or Ethernet came up and got an IP. Zephyr's logging for networking (enable `CONFIG_NET_LOG`, etc.) can help. Also, verify DNS – by default, the client will resolve the server hostname. If DNS isn't working (common issue if not configured), you might use an IP or ensure a DNS server is set.
* **Artifact formatting issues:** You can inspect a `.mender` artifact with a `mender-artifact read artifact.mender` to verify its contents (type, checksum, etc.). If the device fails to install it, check that it's uncompressed and of the correct type.

### Known limitations and considerations

* **Work in progress status:** The Mender MCU client for Zephyr is new and under active development​. Some features of the full Mender client are unavailable or unstable in the MCU version. Expect changes and improvements in upcoming releases.
* **No delta updates:** Mender's binary delta update feature (which exists for Linux images) is not applicable here. Each update will transfer the whole firmware image.
* **No Artifact compression:** The Mender MCU client does not support artifact compression. Artifacts must be created with `--compression none`.
* **No Artifact signatures:** Verifying signed Artifacts is not supported. Note that when using MCUBoot the payload itself is cryptographically signed and verified later by the MCUBoot boot process.
* **Connection stability:** The client relies on a stable TCP/IP connection to download artifacts. If your network is unreliable, the update could fail during the process.
* **Community support:** As this is a new integration, community resources (forums on [Mender Hub](https://hub.mender.io/) or [Jira tickets](https://northerntech.atlassian.net/jira)) are valuable if you encounter problems. Don't hesitate to use them. The reference repository README provides up-to-date info and troubleshooting tips from developers.