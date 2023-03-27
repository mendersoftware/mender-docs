---
title: Troubleshooting Remote Terminal
taxonomy:
    category: docs
---


## Obtaining mender-connect logs

You usually need logs in order to diagnose an issue.

The `mender-connect` by default logs to the system log using `systemd`, so the easiest way to retrieve logs
is to run the following command:

```
journalctl -u mender-connect
```


## Too many open sessions

When attempting to connect with Remote Terminal to a device,
e.g. via the Mender web UI, you get the following error:

```
Error: user has too many open sessions
```

The Remote Terminal feature by default allows
one open session to the device at the time, for each user account of the Mender Server.
Since the limit is per user account, other users of your Mender Server may
still be able to log in to the device.

If you get the above error, make sure you do not have too many browser tabs or CLI windows
with an open Remote Terminal session to the device.

You can increase this limit if you wish. See the [configuration of mender-connect](../../90.Mender-Connect/docs.md#configuration),
in particular the `Sessions.MaxPerUser` setting. Also note the `Sessions.ExpireAfterIdle`
setting, which allows you to set a timeout for sessions.
