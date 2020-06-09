---
title: Deploy a system update
taxonomy:
    category: docs
---

This guide will walk you trough how to do robust system level updates with
rollback. These type of updates cover the whole system including system level
applications and the Linux kernel and ensure the device comes back in a
consistent state even if the update process is interrupted for any reason such
as power loss.

## Prerequisites

It is assumed you:

* have completed [Deploy an application update](../02.Deploy-an-application-update/docs.md)
* know the IP address of your device

### Step 1 - Download the mender-artifact utility on your workstation

Prepare destination directory:

```bash
mkdir -p ${HOME}/bin
```

Download the `mender-artifact` binary

<!--AUTOVERSION: "mender-artifact/%/"/mender-artifact -->
```bash
wget https://d1b0l86ne08fsf.cloudfront.net/mender-artifact/master/linux/mender-artifact -O ${HOME}/bin/mender-artifact
```

Make the `mender-artifact` binary executable:

```bash
chmod +x ${HOME}/bin/mender-artifact
```

Add `${HOME}/bin` to `PATH`:

```bash
export PATH="${PATH}:${HOME}/bin"
```

!!! The above should be added to `~/.bashrc` or equivalent to make it persistent
!!! across multiple terminal sessions.

## Step 2 - Setup shell variables on your workstation

Setup the `IP_ADDRESS` shell variable with correct IP address of your device:

```bash
IP_ADDRESS="<DEVICE-IP-ADDRESS>"
```

Setup `USER` environment variable to match an existing user on the device, e.g
for Raspberry Pi devices:

```bash
USER="pi"
```

!!! Use `USER="root"` if you are using a virtual device

[Mender Artifact's](../../02.Architecture/04.Mender-Artifacts/docs.md) require
a device compatibility field to be entered which **must** match what the device
is reporting to the Mender server or it will refuse to install it. This is a
safety mechanism to avoid installing software to incompatible hardware.

If you are unsure, you can check what the device is reporting on the server:

![connecting a device](Image_0.png)

Use the result from above to assign that value to `DEVICE_TYPE` shell variable:

```bash
DEVICE_TYPE="raspberry4"
```

!!! Make sure to replace `raspberrypi4` with the specific value that you are
!!! seeing in your setup

Set `SSH_ARGS` shell variable to specify the SSH access port:

```bash
SSH_ARGS="-p 22"
```

!!! If you are using a virtual device use `SSH_ARGS="-p 8822"`

## Step 3 - Create a Mender Artifact using the snapshot feature

The easiest way to create system level updates is to use the **snapshot**
functionality in Mender, which will create a snapshot of the full system on a
currently running device and package it as a
[Mender Artifact](../../02.Architecture/04.Mender-Artifacts/docs.md) that you
can deploy to other devices.

Run the following command on your workstation to generate a **snapshot**
[Mender Artifact](../../02.Architecture/04.Mender-Artifacts/docs.md) from your
device:

```bash
mender-artifact write rootfs-image -f ssh://"${USER}@${IP_ADDRESS}" \
                                   -t "${DEVICE_TYPE}" \
                                   -S "${SSH_ARGS}" \
                                   -n system-v1 \
                                   -o system-v1.mender
```

! You might be asked to enter the password of the user account on your device.


! Your device is not usable while the snapshot operation is in progress. Mender
! will freeze the storage device during this operation in order to create a
! consistent snapshot.

Depending on your local network and storage speed, this will take up to
10-20 minutes to finish. You will see a progress indicator, and when it
reaches 100% it will package the Mender Artifact which will take a few more
minutes because it will need to compress the snapshot image.

The end result is a file called `system-v1.mender`. Upload this file to
hosted Mender. You can do that using the UI under the **Releases** tab, as
demonstrated below.

![connecting a device](Image_1.png)

Once uploaded, go to the **DEPLOYMENTS** tab and click **CREATE DEPLYOMENT** in
order to deploy it to your device.

It is encouraged to experiment at this stage to familiarize yourself with robust
system updates with Mender.

As an example you can iterate this flow:

1. Make a change on the device, e.g change a configuration file or install an
application.
2. Create a **snapshot** of the device changes you made

    !!! Mender will skip a deployment to a device if the Artifact is already
    !!! installed, in order to limit resource usage, downtime and ensure consistency
    !!! across the fleet. Make sure to use different names for new Artifacts you
    !!! generate (instead of the two instances of `system-v1` above).

3. Upload the generated Artifact (`.mender`) to hosted Mender and deploy it.
4. Once you have two or more Artifacts uploaded you can switch between the
   software you have on your devices by deploying the respective Artifacts.

Deploy to many devices in order to effectively replicate the device software
and configuration.

To read more about system snapshots see the documentation on
[Artifact from system snapshot](../../04.Artifacts/22.Snapshots/docs.md).

Using the **snapshot** feature is one way to create system updates and additional
resources on more advanced ways can be found here:

1. [Building a Mender Yocto Project image](../../04.Artifacts/10.Yocto-project/01.Building/docs.md)
2. [Building a Mender Debian image](../../04.Artifacts/15.Debian-family/01.building-a-mender-debian-image/docs.md)

## Next step

Proceed to [Deploy a Docker container update](../04.Deploy-a-container-update/docs.md).
