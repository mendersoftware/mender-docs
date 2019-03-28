---
title: Installing
taxonomy:
    category: docs
---

This page describes how to install the Mender client in an existing Linux system.

If rootfs updates are also desired, full board integration is required. In this case, follow instead the device documentation on [Yocto Project](../../devices/yocto-project) or [Debian family](../../devices/debian-family).

## Install prebuilt package

An official `.deb` package with the Mender client that supports the ARM-v7 architecture is provided below. This package should work on most operating systems in the Debian family (e.g. Debian, Ubuntu, Raspbian) and devices (e.g. Raspberry Pi 2/3, BeagleBone)."

Run the following commands on your device to install the package:

<!--AUTOVERSION: "cloudfront.net/%/"/mender "mender_%-1_armhf.deb"/mender -->
```bash
wget https://d1b0l86ne08fsf.cloudfront.net/2.0.0b1/dist-packages/debian/armhf/mender_2.0.0b1-1_armhf.deb
sudo dpkg -i mender_2.0.0b1-1_armhf.deb
```

## Setup

After successfully installing the Mender client, some initial setup is required.

### Mender configuration file

First, we have to configure the Mender client with the configuration file at `/etc/mender/mender.conf`.

To configure the Mender client for Hosted Mender, you need to edit this file and insert your Tenant Token
where it says "Paste your Hosted Mender token here". Run the following commands:

```bash
TENANT_TOKEN="<INSERT YOURS FROM https://hosted.mender.io/ui/#/settings/my-organization>"
sudo sed -i "s/Paste your Hosted Mender token here/$TENANT_TOKEN/" /etc/mender/mender.conf
```

#### Use demo settings (optional)

By default Mender uses production-grade configuration settings. However, if this is a test or development device,
it is recommended to use the demo settings to get shorter polling intervals and allow an insecure certificate used
by the [Mender demo server](../../getting-started/create-a-test-environment). Run the following commands:

```bash
TENANT_TOKEN="<INSERT YOURS FROM https://hosted.mender.io/ui/#/settings/my-organization>"
sudo cp /etc/mender/mender.conf.demo /etc/mender/mender.conf
sudo sed -i "s/Paste your Hosted Mender token here/$TENANT_TOKEN/" /etc/mender/mender.conf
```

### Device type

The device type is a string that defines your device and the type of updates it supports. Run the following
command to set `raspberrypi3` as device type:

!!! Adjust the command below to set the device type of your device (used to ensure software compatibility)

```bash
sudo mkdir -p /var/lib/mender
echo "device_type=raspberrypi3" | sudo tee /var/lib/mender/device_type
```

## Start up

Now you have the Mender client installed and properly setup in your device. To start it in managed mode, run:

```bash
sudo systemctl enable mender && sudo systemctl start mender
```

After a few minutes, take a look at the Devices tab in your Mender server. You should see your new device under "Pending".
Click "Accept" to authorize it to join your Mender server. You are now ready to deploy updates to your device!

!!! If your device does not show up, follow the [troubleshooting section on Mender Server Connection Issues](../../troubleshooting/device-runtime#mender-server-connection-issues).
