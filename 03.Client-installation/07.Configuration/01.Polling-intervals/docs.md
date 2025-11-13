---
title: Polling intervals
taxonomy:
    category: docs
---

For security reasons, the Mender Client does not require any open ports on the
embedded device. Therefore, all communication between the Mender Client and the
server is always initiated by the client and it is important to configure the
client so that the frequency of sending various requests to the server is
reasonable for a given setup.

There are two client configuration parameters that allow controlling the
frequency of communication between the client and the server:

* `UpdatePollIntervalSeconds` sets the frequency the client will send an update check request to the server.
Default value: 1800 seconds (30 minutes).

* `InventoryPollIntervalSeconds` sets the frequency for periodically sending [inventory data](../../04.Inventory/docs.md).
Inventory data is always sent after each boot of the device, and after a new update has been
correctly applied and committed by the device in addition to this periodic interval.
Default value: 28800 seconds (8 hours).

Note that `mender-auth`, one of the client components, does not connect on its own, but acts as a
proxy whenever `mender-update` needs to connect.


## How to choose right intervals

The Mender Client is more responsive with higher frequency intervals. Meaning
that the client inventory data updates more frequently. The client also polls
for updates at a smaller interval, leading to faster deployments.

But there is a trade-off; higher polling frequencies results in more server
load. If one server has many clients connected, a high frequency will require
more resources server-side to keep the environment responsive.

!!! If you are using the Mender Client in demo mode, either by selecting it when running `mender-setup`, or by using the [meta-mender-demo layer](../../../05.Operating-System-updates-Yocto-Project/03.Build-for-demo/docs.md), the Mender Client has more aggressive polling intervals to simplify testing. The defaults noted above do not apply to demo mode and you will see extra network traffic in demo mode.


## Changing the parameters

Both parameters are stored in the configuration file `/etc/mender/mender.conf`:

```
{
  "UpdatePollIntervalSeconds": 1800,
  "InventoryPollIntervalSeconds": 28800,
…
}
```

