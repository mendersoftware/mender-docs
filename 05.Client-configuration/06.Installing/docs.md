---
title: Installing
taxonomy:
    category: docs
---

This page describes how to install the Mender client in an existing Linux system. Installing this way does not offer a a full Mender integration. However, it is possible to use Update Modules and update parts of the system.

If full board integration is desired, follow the device documentation on [Yocto Project](../../devices/yocto-project) or [Debian family](../../devices/debian-family).

## Install from source

<!--AUTOVERSION: "mender/tree/%#installing-from-source"/mender -->
It is possible to install the Mender client from source by following the guidelines outlined in the [README.md](https://github.com/mendersoftware/mender/tree/2.0.0b1#installing-from-source) of the Mender client source repository.

## Install Mender provided Debian package

A Debian package (`.deb`) is provided for convince to install on e.g Debian, Ubuntu or Raspbian. We provide packages for the following architectures:

- armhf (ARM-v6)
    - Raspberry Pi, BeagleBone and other ARM based devices.

Download the package:

<!--AUTOVERSION: "cloudfront.net/%/"/mender "mender_%-1_armhf.deb"/mender -->
```bash
wget https://d1b0l86ne08fsf.cloudfront.net/2.0.0b1/dist-packages/debian/armhf/mender_2.0.0b1-1_armhf.deb
```

Install the package:

<!--AUTOVERSION: "mender_%-1_armhf.deb"/mender -->
```bash
sudo dpkg -i mender_2.0.0b1-1_armhf.deb
```

### Setup

After successfully installing the Mender client Debian package, some initial setup is required.

#### Mender configuration file

First, we have to configure the Mender client using the configuration file at `/etc/mender/mender.conf`.

##### Use demo settings (optional)

By default Mender uses production-grade configuration settings. However, if this is a test or development device,
it is recommended to use the demo settings to get shorter polling intervals.

Copy the demo configuration file:

```bash
sudo cp /etc/mender/mender.conf.demo /etc/mender/mender.conf
```

##### Configuration for Hosted Mender server

To configure the Mender client for Hosted Mender, you need to edit `/etc/mender/mender.conf` and insert your Tenant Token
where it says "Paste your Hosted Mender token here".

Set the `TENANT_TOKEN` variable:

```bash
TENANT_TOKEN="<INSERT YOURS FROM https://hosted.mender.io/ui/#/settings/my-organization>"
```

Update configuration file with your token:

```bash
sudo sed -i "s/Paste your Hosted Mender token here/$TENANT_TOKEN/" /etc/mender/mender.conf
```

#### Device type

The device type is a string that defines your device and is used to ensure software compatibility by comparing the device type set in a [Mender Artifact](../../architecture/mender-artifacts) with the string on the device.

In below example we will set the device type to `raspberrypi3`, adjust according to your desired device type identifier.

Create Mender client state directory:

```bash
sudo mkdir -p /var/lib/mender
```

Create the device type file:

```bash
echo "device_type=raspberrypi3" | sudo tee /var/lib/mender/device_type
```

#### Start up

Now you have the Mender client installed and properly setup in your device.

Start the Mender client in [managed mode](../../architecture/overview#modes-of-operation) and enable autostart of the Mender service on subsequent boots:

```bash
sudo systemctl enable mender && sudo systemctl start mender
```

After a few minutes, take a look at the Devices tab in your Mender server. You should see your new device under "Pending".
Click "Accept" to authorize it to join your Mender server. You are now ready to deploy updates to your device!

!!! If your device does not show up, follow the [troubleshooting section on Mender Server Connection Issues](../../troubleshooting/device-runtime#mender-server-connection-issues).
