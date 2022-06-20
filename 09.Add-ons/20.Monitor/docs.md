---
title: Monitor
taxonomy:
    category: docs
    label: user guide
---

!!!!! Requires the Mender Monitor add-on package.
!!!!! See [the Mender features page](https://mender.io/product/features?target=_blank)
!!!!! for an overview of all Mender plans and features.

The Mender Monitor add-on gives you instant visibility into issues
with your device fleet. In addition, it allows you to configure alerts
when certain parts of your infrastructure malfunction or need your attention.

To save bandwidth and support edge processing, Monitor is a fully
distributed solution, meaning that we send no data from the device
to the server unless triggered by an alert. Compared to classic approaches
of sending all the data about all the nodes to the server all the time,
this leads to massive bandwidth savings and allows instant local processing.

## Alerts

Each time a service is not running, or a log file contains a given pattern, or a
signal is received on a given D-Bus bus, all users who have access to the given
device on the Mender server receive an email notification. You can mute the
email notifications in the Mender Server settings.

There is one exception to the above rule: if a service goes up and down often
enough we consider it to be _flapping_. When we detect this, service subsystem
sends a _flapping alert_ and does not send anything else until the number of service
state changes per one `FLAPPING_INTERVAL` goes below `FLAPPING_COUNT_THRESHOLD`.
See the [advanced configuration](30.Advanced-configuration/docs.md) chapter
for more information about these settings.

## Architecture

The Monitor add-on consists of two parts: the API to the backend that allows
you to integrate with existing solutions, and a `mender-monitor`
systemd service which runs on the devices. When certain events occur,
the service sends alerts to the Mender Server. If you need more control,
or you want to customize your monitoring solution, you can use the set of
bash functions that compose the service directly from your scripts.

### Running and configuring

To start monitoring daemon, run the following command:

```bash
systemctl start mender-monitor
```

You can view the service's logs running the following command:

```bash
journalctl -u mender-monitor
```
