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

### Optimizing for unstable networks

In environments with frequent network interruptions, remote terminal sessions may occasionally fail to close cleanly on the device. This can lead to "ghost" sessions that consume the session limit and block new connections.

To improve reliability, we recommend the following configuration in `/etc/mender/mender-connect.conf`:

*   `Sessions.ExpireAfterIdle`: Set to `600` (10 minutes) to automatically close sessions after inactivity.
*   `Sessions.StopExpired`: Set to `true` to enable the cleanup of idle or expired sessions.
*   `Sessions.MaxPerUser`: Consider increasing this to `2` or `4` to provide a buffer for users whose previous sessions didn't close cleanly.

For more details, see the [configuration of mender-connect](../../90.Mender-Connect/docs.md#configuration).

!!! Note: Starting with version 3.0, `mender-connect` will adopt more proactive defaults to improve out-of-the-box reliability:
!!! *   `ExpireAfterIdle` will default to **600 seconds** (previously `0`/disabled).
!!! *   `StopExpired` will default to **true** (previously `false`).


## Remote terminal sometimes not working

If you notice that remote terminal isn't available at one time, but is after checking again after a few minutes, this is the autoheal mechanism of the remote terminal in action.

There is a hardcoded, 60 second, websocket ping timeout used to maintain a notion of a connection.
As soon as that times out, the remote terminal will close the current connection and attempt to create a new to reestablish the communication with the server.
