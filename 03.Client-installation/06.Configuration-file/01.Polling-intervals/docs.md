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

* `InventoryPollIntervalSeconds` sets the frequency for periodically sending [inventory data](../../04.Inventory/docs.md).
Inventory data is always sent after each boot of the device, and after a new update has been
correctly applied and committed by the device in addition to this periodic interval.
Default value: 28800 seconds (8 hours).

## How to choose right intervals

The higher the frequency is (i.e. the lower the configuration value), the sooner the server will
be updated with the client inventory data and the client will poll the update install request faster
so updates can be deployed more quickly.

But there is a trade-off, as the higher frequency is, the more load server will receive.
If many clients are connected to one server, a high frequency
will require more resources server-side to keep the environment responsive.

!!! If you are using the Mender client in demo mode, either by selecting it when running `mender setup`, or by using one of the [prebuilt Yocto images](../../../08.Downloads/docs.md#disk-images) and set up with the [demo layer](../../../04.Artifacts/10.Yocto-project/01.Building/docs.md#adding-meta-mender-to-existing-yocto-project-environment), the Mender client has more aggressive polling intervals to simplify testing. The defaults noted above does not apply to demo mode and you will see extra network traffic in demo mode.


## Changing the parameters

Both parameters are stored in the configuration file `/etc/mender/mender.conf`:

```
{
  "UpdatePollIntervalSeconds": 1800,
  "InventoryPollIntervalSeconds": 28800,
...
```

Before building an image as described in [Building Mender Yocto
image](../../../04.Artifacts/10.Yocto-project/01.Building/docs.md), you can adjust these configuration settings
either [using a custom configuration file](..), or [using Yocto
variables](../../../04.Artifacts/10.Yocto-project/02.Image-configuration/docs.md#configuring-polling-intervals).

If you have already built an Artifact containing the rootfs, have a look at
[modifying a configuration in a Mender Artifact](../../../04.Artifacts/25.Modifying-a-Mender-Artifact/docs.md#modifying-a-configuration-file).
