---
title: Polling intervals
taxonomy:
    category: docs
---

For security reasons, the Mender client does not require any open ports at the embedded device.
Therefore, all communication between the Mender client and the server is always initiated by the client and
it is important to configure the client so that the frequency of sending various requests to the server is
reasonable for a given setup.

There are two client configuration parameters that allow controlling the frequency of communication between
the client and the server:

* `UpdatePollIntervalSeconds` sets the frequency the client will send an update check request to the server.
Default value: 1800 seconds (30 minutes).

* `InventoryPollIntervalSeconds` sets the frequency for periodically sending [inventory data](../../inventory).
Inventory data is always sent after each boot of the device, and after a new update has been
correctly applied and committed by the device in addition to this periodic interval.
Default value: 86400 seconds (one day). 

## How to choose right intervals

The higher the frequency is (i.e. the lower the configuration value), the sooner the server will
be updated with the client inventory data and the client will poll the update install request faster
so updates can be deployed more quickly.

But there is a trade-off, as the higher frequency is, the more load server will receive.
If many clients are connected to one server, a high frequency
will require more resources server-side to keep the environment responsive.

!!! When in demo mode, which is used in the [prebuilt images](../../../getting-started/download-test-images) and set up with the [demo layer](../../../artifacts/yocto-project/building#adding-the-meta-layers), the Mender client has more aggressive polling intervals to simplify testing. The defaults noted above does not apply to demo mode and you will see extra network traffic in demo mode.


## Changing the parameters

Both parameters are stored in the configuration file `/etc/mender/mender.conf`:

```
{
  "UpdatePollIntervalSeconds": 1800,
  "InventoryPollIntervalSeconds": 86400,
...
```

Before building an image as described in [Building Mender Yocto
image](../../../artifacts/building-mender-yocto-image), you can adjust these configuration settings
either [using a custom configuration file](..), or [using Yocto
variables](../../../artifacts/image-configuration#configuring-polling-intervals).

If you have already built an Artifact containing the rootfs, have a look at
[modifying a configuration in a Mender Artifact](../../../artifacts/modifying-a-mender-artifact#modifying-a-configuration-file).
