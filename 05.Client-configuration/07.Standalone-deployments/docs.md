---
title: Standalone deployments
taxonomy:
    category: docs
---

This document will show how *standalone* deployments work with the Mender client,
where no Mender server is used and the deployments are triggered at the
device, either manually in the terminal or by custom scripts. This can be useful in order
to deploy updates to devices which do not have network connectivity or
are updated through external storage like a USB stick.

For an explanation of the difference between *managed* and *standalone* deployments, please see
[Modes of operation](../../02.Overview/01.Introduction/docs.md#client-modes-of-operation).

!!! Note that [state scripts](../../04.Artifacts/50.State-scripts/docs.md) work slightly differently in standalone mode, see [state scripts and standalone mode](../../04.Artifacts/50.State-scripts/docs.md#standalone-mode) for more information.


## Setting Mender up for standalone mode

If you would like to run Mender in *standalone* mode, the only difference is that you
must make sure that the Mender client does *not run as a daemon*. In most cases this
will entail disabling or removing any `systemd` unit that starts the Mender client.


## Deploy an Artifact to a device

To deploy the new Artifact to your device, run the following command in the
device terminal:


```bash
mender -install <URI>
```

`<URI>` can be any type of file-based storage or an HTTP/HTTPS URL.
For example, if you are updating from a USB stick, you could use `/mnt/usb1/release1.mender`.
To use HTTPS, simply replace it with a URL like `https://fileserver.example.com/mender/release1.mender`.

Mender will download the new Artifact, process its metadata information, extract the contents and write it to the inactive rootfs partition. It will configure the bootloader to boot into it on the next reboot. This will likely take several minutes to complete, depending on the performance of your device and the size of the Artifact.
Note that Mender does not use any temporary space, it streams the Artifact.

To run the newly deployed rootfs image, simply reboot your device:

```bash
reboot
```

Your device should boot into the newly deployed rootfs.


## Make the deployment permanent

If you are happy with the deployment, you can make it permanent by running the following command in your device terminal:

```bash
mender -commit
```

By running this command, Mender will configure the bootloader to persistently boot from this newly written deployment. To deploy another update, simply run `mender -install <URI>` again, then reboot and commit.

!!! If we reboot the device again *without* running `mender -commit`, it will boot into the previous rootfs partition that is known to be working (where we deployed the update from). This ensures a robust update process in cases where the newly deployed rootfs does not boot or otherwise has issues that we want to roll back from. Also note that it is possible to automate deployments by [running the Mender client as a daemon](../../02.Overview/01.Introduction/docs.md#client-modes-of-operation).
