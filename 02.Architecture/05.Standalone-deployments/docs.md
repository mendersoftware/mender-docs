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
[Modes of operation](../overview#modes-of-operation).

!!! Note that [state scripts](../../artifacts/state-scripts) are a feature of managed mode.  State scripts are not executed when running Mender in standalone mode.


## Setting Mender up for standalone mode

The Mender client will by default run in *managed* mode, i.e. connected to a Mender server.
In managed mode, mender runs as a daemon on the device.

If you would like to run Mender in *standalone* mode, the only difference is that you
must make sure that the Mender client does *not run as a daemon*. In most cases this
will entail disabling or removing any `systemd` unit that starts the Mender client.


## Building standalone images

When [building a Mender Yocto Project image](../../artifacts/building-mender-yocto-image),
you can ensure Mender runs in standalone mode by following the
[image configuration steps to make sure Mender does not run as a system service](../../artifacts/image-configuration#disabling-mender-as-a-system-service)
before building.

From the Yocto Project build output configured as above you will get two
image types that work in standalone mode.

The first is a disk image that is used to flash to the entire disk of the
device, i.e. do the initial device storage provisioning.
`meta-mender` creates these files with a `.sdimg`
suffix, so they are easy to recognize. This file contains
all the partitions of the given storage device, as
described in [Partition layout](../../devices/partition-layout).
Please see [Provisioning a new device](../../artifacts/provisioning-a-new-device)
for steps how to provision the device storage using the `*.sdimg` image.

Secondly, you will get an Artifact file that is used for deployments with Mender,
and it is recognized by its `.mender` suffix.
See [Mender Artifacts](../../architecture/mender-artifacts)
for a more detailed overview.


## Deploy an Artifact to a device

After provisioning the device with the disk image (`.sdimg` file) and building a new Artifact (`.mender` file),
you can trigger a deployment of the Artifact.
To deploy the new Artifact to your device, run the following command in the device terminal:


```bash
mender -rootfs <URI>
```

`<URI>` can be any type of file-based storage or a https URL.
For example, if you are updating from a USB stick, you could use `/mnt/usb1/release1.mender`.
To use http, simply replace it with a URL like `https://fileserver.example.com/mender/release1.mender`.

Mender will download the new Artifact, process its metadata information, extract the contents and write it to the inactive rootfs partition. It will configure the bootloader to boot into it on the next reboot. This will likely take several minutes to complete, depending on the performance of your device and the size of the Artifact.
Note that Mender does not use any temporary space, it [streams the Artifact](../mender-artifacts#streaming-and-compression).

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

By running this command, Mender will configure the bootloader to persistently boot from this newly written deployment. To deploy another update, simply run `mender -rootfs <URI>` again, then reboot and commit.

!!! If we reboot the device again *without* running `mender -commit`, it will boot into the previous rootfs partition that is known to be working (where we deployed the update from). This ensures a robust update process in cases where the newly deployed rootfs does not boot or otherwise has issues that we want to roll back from. Also note that it is possible to automate deployments by [running the Mender client as a daemon](../../architecture/overview#modes-of-operation).
