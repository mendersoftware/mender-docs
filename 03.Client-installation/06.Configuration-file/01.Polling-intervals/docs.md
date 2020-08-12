---
title: Polling intervals
taxonomy:
    category: docs
---

For security reasons, the Mender client does not require any open ports on the embedded device.
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

But there is a trade-off; higher polling frequencies will result in more server load.
If many clients are connected to one server, a high frequency
will require more resources server-side to keep the environment responsive.

!!! If you are using the Mender client in demo mode, either by selecting it when running `mender setup`, or by using the [meta-mender-demo layer](../../../05.System-updates-Yocto-Project/03.Build-for-demo/docs.md), the Mender client has more aggressive polling intervals to simplify testing. The defaults noted above do not apply to demo mode and you will see extra network traffic in demo mode.


## Changing the parameters

Both parameters are stored in the configuration file `/etc/mender/mender.conf`:

```
{
  "UpdatePollIntervalSeconds": 1800,
  "InventoryPollIntervalSeconds": 28800,
…
}
```

