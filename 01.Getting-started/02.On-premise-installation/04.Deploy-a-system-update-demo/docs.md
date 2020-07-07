---
title: Deploy a system update demo
taxonomy:
  category: docs
---

In this tutorial we will deploy a full rootfs update to a physical device, a
Raspberry Pi, using the Mender server.

We will use two devices: one as our local "golden" device, which we use to
prepare the update, and other as a remote device that receives the OTA update.
It is also possible to use the same device for both roles if you have only one
device available.

## Prerequisites

The test environment should be set up and working successfully
as described in [Install a Mender demo server](../create-a-test-environment).

We also strongly recommend that you complete the tutorial that comes with the Mender GUI so
that you have a basic understanding of how Mender works before moving on to connecting a physical device.

### A device or two to test with

You need one or more Raspberry Pi devices. The original tutorial was written
using a Raspberry Pi 3, but a Raspberry Pi 4 will also work. Just replace
"Raspberry Pi 3" and similar looking strings with "Raspberry Pi 4" where you see
them.

To make it easy to provision the device we will use a SD card to store the OS,
so you will need one SD card (8 GB or larger) per device.

### Disk image

Get the disk image for your board(s) from [the Downloads
section](../../../downloads#disk-images).

!!! It is possible to use this tutorial with _any_ physical board, as long as you have integrated Mender with it. In this case you cannot use the demo Artifacts we provide in this tutorial, but you need to build your own artifacts as described in [Building a Mender Yocto Project image](../../../artifacts/yocto-project/building).

### Mender-Artifact tool

Download the prebuilt `mender-artifact` binary for your platform following the links
in [Downloads section](../../../downloads#mender-artifact).

Please see [Modifying a Mender Artifact](../../../artifacts/modifying-a-mender-artifact)
for a more detailed overview.

### Network connectivity

The device needs to have network set up
so it can connect directly to your workstation
(where you have the Mender server running).

! By default the Mender client will use ports **443** and **9000** to connect to the server. You can test the connection from your client later with networking tools like `telnet`.

If you have just one device, you could connect your
workstation and the device using a direct
Ethernet cable and use static IP addresses at both ends.
For multiple devices, you need a router or switch.

For the rest of the tutorial we will assume
`$IP_OF_MENDER_SERVER_FROM_DEVICE` will expand to the IP address
that your device(s) can connect to the Mender server.

!!! If you are using `bash`, you can set a variable to make the rest of the tutorial easier, for example `IP_OF_MENDER_SERVER_FROM_DEVICE="192.168.10.1"`.

! Using static IP addresses with one device and workstation is quite easy. If you are using several devices, we strongly recommend using a setup with dynamic IP assignment like a router with DHCP support. Otherwise you need to take care to preserve the unique IP address configuration of each device when provisioning the storage and deploying rootfs updates.

!!! If the device does not have internet connectivity, the device will not be able
!!! to sync the system time. This will in turn cause the server certificate check to
!!! fail. Thus if your device is not connected to the internet, you have to manually
!!! set the system time correctly. This can be done with the `date -s` command.

## Prepare the disk image

Locate the demo _disk image_ (`*.sdimg`) you downloaded for your device.
This image contains _all the partitions_ of the storage device, as described in [Partition
layout](../../../devices/general-system-requirements#partition-layout).

You can decompress a `.xz` image like the following:

```bash
unxz <PATH-TO-YOUR-DISK-IMAGE>.sdimg.xz
```

Or, if it is a `.gz` image, like this:

```bash
gunzip <PATH-TO-YOUR-DISK-IMAGE>.sdimg.gz
```

!!! The Mender images come with a predetermined size for the root filesystems,
!!! which may be too small for some use cases where a lot of space is required
!!! for applications. If you are building your own disk image by following
!!! [Building a Mender Yocto Project image](../../../artifacts/yocto-project/building),
!!! you can configure the desired space usage with the Yocto Project variable
!!! [MENDER_STORAGE_TOTAL_SIZE_MB](../../../artifacts/yocto-project/variables#mender_storage_total_size_mb).

If you are connecting your device with an Ethernet cable to the same LAN network
that your workstation, skip the following subsections and jump to
[the next section](#write-the-disk-image-to-the-SD-card)

Else, if you are using Wifi or an static IP address setup, we need to change
some configuration settings in this image so that the Mender client can
successfully reach your Mender server.

First set a shell variable describing the image name, by replacing `<sdimg>` in this snippet:

```bash
MENDER_IMGPATH=<sdimg>
```

### Set a static device IP address and subnet

This section assumes you use a static IP setup, for example if you are plugging
your device directly into your workstation with an Ethernet cable. If your
device uses a DHCP setup, this section can be skipped.

In this section, we assume that `$IP_OF_MENDER_CLIENT` and
`$IP_OF_MENDER_SERVER_FROM_DEVICE` are the IP address you assign to your device.

!!! If you are using `bash`, you can set variables before running the command
!!! below, for example `IP_OF_MENDER_CLIENT="192.168.10.2"`.

Run the command below to fill the `systemd`
networking configuration files of the rootfs partitions:

```bash
echo -n "\
[Match]
Name=eth0

[Network]
Address=$IP_OF_MENDER_CLIENT
Gateway=$IP_OF_MENDER_SERVER_FROM_DEVICE
" | mender-artifact cp - $MENDER_IMGPATH:/etc/systemd/network/eth.network
```

! If you have a static IP address setup for several devices, you need several disk images so each get different IP addresses.

### Wifi connectivity

The raspberrypi image comes with Wifi connectivity disabled by default,
thus we need to enable it and provide the credentials
in the `wpa_supplicant.conf` file on your device.
To this end, first let's create a file called `wpa.in`:

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=YourCountry

network={
	ssid="YourSSID"
	psk="YourPassword"
}
```
where YourCountry stands for two-letter country code (e.g.: PL for Poland),
YourSSID, and YourSSID are the SSID of your network and the password, respecively.
And then run:

```bash
mender-artifact cp wpa.in "$MENDER_IMGPATH":/boot/wpa_supplicant.conf
```

Now you should have wpa configuration set up correctly on start up. (Do not forget
to remove `wpa.in` file, it contains your password).

## Write the disk image to the SD card

Please see [Write the disk image to the SD card](../../../artifacts/provisioning-a-new-device#write-the-disk-image-to-the-sd-card)
for steps how to provision the device disk using the `*.sdimg`
image you downloaded and modified above.

If you have several devices, please write the disk image to all their SD cards.

## Boot the device

! Make sure that the Mender server is running as described in [Install a Mender demo server](../create-a-test-environment) and that the device can reach it on the IP address you configured above (`$IP_OF_MENDER_SERVER_FROM_DEVICE`). You might need to set a static IP address where the Mender server runs and disable any firewalls.

First, insert the SD card you just provisioned into the device. Then **connect
the device to power**.

## Run Mender setup

You need to connect a USB keyboard and an HDMI monitor at least for the first boot.

Once the device has booted, log in. On Raspberry Pi OS, the default user is "pi", and
the password is "raspberry".

!!! If you want to enable SSH on startup for further boots, execute'
!!! `sudo systemctl start ssh`

Once you have logged in, run the Mender setup command, like this:

```bash
sudo mender setup
```

This will start the text based interactive setup of the Mender client. Below you
can see a typical session, with example answers given throughout.

<!-- Why "html" in the below block? "text" would be the most correct, but it has
bugs and inserts unwanted spaces in the beginning -->

```html
Mender Client Setup
===================

Setting up the Mender client: The client will regularly poll the server to check
for updates and report its inventory data.
Get started by first configuring the device type and settings for communicating
with the server.


The device type property is used to determine which Mender Artifact are
compatible with this device.
Enter a name for the device type (e.g. raspberrypi3-raspios): [raspberrypi]

Are you connecting this device to hosted.mender.io? [Y/n] n

Demo mode uses short poll intervals and assumes the default demo server setup.
(Recommended for testing.)
Do you want to run the client in demo mode? [Y/n] y

Set the IP of the Mender Server: [127.0.0.1] 1.2.3.4
Mender setup successfully.
```

In the question about "IP of the Mender Server", use the value of
`$IP_OF_MENDER_SERVER_FROM_DEVICE` that you defined earlier. It is not possible
to use the variable itself in the setup, you have to type the IP value. In the
example above, the value is `1.2.3.4`, but it will be different in your setup.

After the setup has been done, restart the client with the following command:

```bash
sudo systemctl restart mender-client
```

## See the device in the Mender UI

If you refresh the Mender server UI (by default found at [https://localhost/](https://localhost/?target=_blank)),
you should see one or more devices pending authorization. If you do not see your device listed in the UI, please review [troubleshooting steps.](../../../troubleshooting/device-runtime#mender-server-connection-issues)

Once you **authorize** these devices, Mender will auto-discover
inventory about the devices, including the device type (e.g. beaglebone)
and the IP addresses, as shown in the example with a BeagleBone Black below.
Which information is collected about devices is fully configurable; see the documentation on [Identity](../../../client-configuration/identity) and [Inventory](../../../client-configuration/inventory) for more information.

![Mender UI - Device information for BeagleBone Black](device_information_bbb.png)

!!! If your device does not show up for authorization in the UI, you need to
!!! diagnose what went wrong. Most commonly this is due to problems with the
!!! network. You can test if your workstation can reach the device by trying to ping
!!! it, e.g. with `ping 192.168.10.2` (replace with the IP address of your
!!! device). If you can reach the device, you can ssh into it, e.g. `ssh
!!! pi@192.168.10.2`, or connect a USB keyboard and a HDMI monitor to it to have
!!! direct access. Check the log output from Mender with
!!! `journalctl -u mender-client`. If you get stuck, please feel free to reach
!!! out on the [Mender Hub discussion forum](https://hub.mender.io/)!

## Install new software in your golden device

Now upgrade or install custom software on your golden device. This represents
the update that will be sent to the rest of your device fleet.

For example, upgrade all packages of your Raspberry Pi OS with:

```bash
sudo apt-get update && sudo apt-get dist-upgrade
```

In addition, you can install other packages or copy your own application files
over SSH.

## Generate an Artifact from the golden device

In this section, we assume that `$IP_OF_MENDER_CLIENT` is the IP address of your
your device.

!!! If you are using `bash`, you can set a variable before running the command
!!! below, for example `IP_OF_MENDER_CLIENT="192.168.10.2"`. If you don't know
!!! it, run `hostname -I` on your device.

This section will create a Mender Artifact from a running device using the
snapshots feature of Mender. See [Snapshots](../../../artifacts/snapshots) to
learn more details about this feature.

First you need to start SSH service in your device. For Raspberry Pi OS image, start it
with:

```bash
sudo systemctl start ssh
```

For Yocto based images, it is enabled and started by default.

Now we will create the Mender Artifact. Run from your workstation:

```bash
mender-artifact write rootfs-image -f ssh://pi@$IP_OF_MENDER_CLIENT -n my_update_release_1 -o my_update_release_1.mender -t raspberrypi3
```

!!! Adjust `my_update_release_1` to the desired Artifact name and `raspberrypi`
!!! to the device type you selected during [Run Mender setup](#run-mender-setup)
!!! step.

This command will create a file `my_update_release_1.mender` which is a Mender
Artifact containing the golden image currently running software.

Before we can deploy the Artifact we prepared above, it needs to be uploaded to
the server.

Go to the Mender server UI, click the **Releases** tab and upload this Artifact.

## Deploy the Artifact to a new device

Take now a new device that will play the role of the remote device. Follow again
the previous steps to [Prepare the disk image](#prepare-the-disk-image), [Write
the disk image to the SD card](#write-the-disk-image-to-the-sd-card), [Boot the
device](#boot-the-device), [Run Mender setup](#run-mender-setup) and [See the
device in the Mender UI](#see-the-device-in-the-mender-ui)

!!! If you have only one device, just reflash it again and use it as if it was
!!! your second remote device.

Now that we have the device connected and the Artifact
uploaded to the server, all that remains is to go to the
**Deployments** tab and click **Create a deployment**.

Select the Artifact you just uploaded and **All devices**, then
**Create deployment**.

!!! If you deploy across several device types (e.g. `beaglebone` and
!!! `raspberrypi`), the Mender server will skip these if no compatible artifact
!!! is available. This condition is indicated by the _noartifact_ status in the
!!! deployment report. Mender does this to avoid deployments of incompatible
!!! rootfs images. However, if you have Artifacts for these other device types,
!!! identified by the same Artifact name, then Mender will deploy to all the
!!! devices there are compatible Artifacts for.

## See the progress of the deployment

As the deployment progresses, you can click on it to view more details about the current status across all devices.
In the example below, we can see that a BeagleBone is installing the update.

![Mender UI - Deployment progress - BeagleBone Black](deployment_report_bbb.png)

Once the deployment completes, you should see its report in _Past deployments_.

**Congratulations!** You have used the Mender server to deploy your first physical device update!

## Deploy another update

In order to deploy another update, we need to create another Artifact
with a different Artifact Name (than the one already installed at the devices).
This is because Mender _skips a deployment_ for a device if it detects that
the Artifact is already installed, in order to avoid unnecessary deployments.

You can do this by making more changes on your golden device and then repeating
the steps at [Generate an Artifact from the golden
device](#generate-an-artifact-from-the-golden-device).

Alternatively, to change the name of our existing Artifact, we can simply use
`modify` and the `-n` option of the `mender-artifact` tool, first making a copy
of the original. To do this, run these two commands (adjust the Artifact file
name accordingly):

```bash
cp my_update_release_1.mender my_update_release_2.mender
mender-artifact modify my_update_release_2.mender -n release-2
```

!!! Using`mender-artifact modify`, you can easily modify several configuration settings in existing disk image (`.sdimg`) and Mender Artifact (`.mender`) files, such as the server URI and certificate. See `mender-artifact help modify` for more options.

! Currently the `mender-artifact modify` command only supports modifying ext4 payloads.

Upload this modified Artifact file to your Mender server and deploy it to your device.
You should see that the Artifact Name has changed after the deployment.
Now that you have two Mender Artifact files that are configured for your
network with different names, you can deploy updates back and forth between them.

## Integrate Mender with your board

Now that you have seen how Mender works with a reference board, you might be wondering what it would take to port it to your own board.

To get support for robust system updates with rollback, Mender must be [integrated with production boards](../../../devices).

On the other hand, if you only need support for application updates (not full system updates), no board integration is required. In this case you can install Mender on an existing device and OS by following the documentation on [installing the Mender client](../../../client-configuration/installing).

You can find images for other devices in our Mender Hub community forum, see
[Debian Family](https://hub.mender.io/c/board-integrations/debian-family/11) or
[Yocto Project](https://hub.mender.io/c/board-integrations/yocto-project/10)
integration posts.
