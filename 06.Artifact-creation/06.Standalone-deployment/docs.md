---
title: Standalone deployment
taxonomy:
    category: docs
    label: reference
---

This document will show how *standalone* deployments work with Mender,
where no Mender server is used and the deployments are triggered at the
device, either manually in the terminal or by custom scripts. This can be useful in order
to deploy updates to devices which do not have network connectivity or
are updated through external storage like a USB stick.

For an explanation of the difference between *managed* and *standalone* deployments, please see
[Modes of operation](../../02.Overview/01.Introduction/docs.md#client-modes-of-operation).

!!! Note that [state scripts](../../04.Artifacts/50.State-scripts/docs.md) work slightly differently in standalone mode, see [state scripts and standalone mode](../../04.Artifacts/50.State-scripts/docs.md#standalone-mode) for more information.

## Setting Mender up for standalone mode

If you would like to run Mender in *standalone* mode, you
must make sure that the Mender client does *not run as a daemon*. In most cases this
will entail disabling or removing any `systemd` unit that starts the Mender client. If you want to check if Mender is running as a daemon, you can try the following command:
```bash
pi@raspberrypi:~$ sudo systemctl status mender-client
● mender-client.service - Mender OTA update service
   Loaded: loaded (/lib/systemd/system/mender-client.service; enabled; vendor preset: enabled)
   Active: active (running) since Thu 2020-07-23 03:24:54 BST; 16h ago
 Main PID: 320 (mender)
    Tasks: 9 (limit: 1012)
   Memory: 7.5M
   CGroup: /system.slice/mender-client.service
           └─320 /usr/bin/mender -daemon
```

The status reported as active indicates that in order to use standalone mode you have to stop Mender running as a daemon.
```bash
pi@raspberrypi:~$ sudo systemctl stop mender-client
```


## Deploy an Artifact to a device

To deploy the new Artifact to your device, run the following command in the
device terminal:

```bash
mender -install <URI>
```

`<URI>` can be any type of file-based storage or an HTTP/HTTPS URL.
For example, if you are updating from a USB stick, you could use `/mnt/usb1/release1.mender`.
To use HTTPS, simply replace it with a URL like `https://fileserver.example.com/mender/release1.mender`.

!!! If you are doing a full file system update, now run the `reboot` command to boot into the new file system.

## Make the deployment permanent

If you are happy with the deployment, you can make it permanent by running the following command in your device terminal:

```bash
mender -commit
```

By running this command, Mender will mark the update as successful and permanent.

To deploy another update, simply run `mender -install <URI>` again, then reboot and commit.
