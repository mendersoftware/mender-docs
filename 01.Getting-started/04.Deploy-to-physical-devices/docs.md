---
title: Deploy to physical devices
taxonomy:
    category: docs
---

In this tutorial we will deploy a full rootfs update to
a physical device, the BeagleBone Black, using the
Mender server.

## Prerequisites

The test environment should be set up and working successfully
as described in [Create a test environment](../Create-a-test-environment).

We also strongly recommend that you complete the tutorial
[Deploy to virtual devices](../Deploy-to-virtual-devices) so
that you have a basic understanding of how Mender works
before moving on to connecting a physical device.


### BeagleBone Black

You need one or more BeagleBone Black devices to deploy
updates to. To make it easy to provision the device we will use
a SD card to store the OS, so you will need one SD card
(1 GB or larger) per BeagleBone Black.

!!! It is possible to use this tutorial with any physical device, as long as you have integrated Mender with it. In this case you cannot use the demo images we provide in this tutorial, but you need to build your own images as described in [Building a Mender Yocto Project image](../../Artifacts/Building-Mender-Yocto-image).


### Network connectivity

The BeagleBone Black needs to have network set up
so it can connect directly to your workstation
(where you have the Mender server running).
If you have one BeagleBone Black, you could connect your
workstation and the device using a direct
Ethernet cable and use static IP addresses at both ends.
For multiple devices, you need a router or switch.

For the rest of the tutorial we will assume
`$IP_OF_MENDER_SERVER_FROM_DEVICE` will expand to the IP address
that your device(s) can connect to the Mender server.

!!! If you are using `bash`, you can set a variable to make the rest of the tutorial easier, for example `IP_OF_MENDER_SERVER_FROM_DEVICE="192.168.10.1"`.

! Using static IP addresses with one device and workstation is quite easy. If you are using several devices, we strongly recommend using a setup with dynamic IP assignment like a router with DHCP support. Otherwise you need to take care to preserve the unique IP address configuration of each device when provisioning the storage and deploying rootfs updates.


## Prepare the disk image

! Please make sure to set a shell variable that expands correctly with `$IP_OF_MENDER_SERVER_FROM_DEVICE` or edit the commands below accordingly.

Download the demo *disk* image with Mender support for the BeagleBone Black
at [https://mender.s3.amazonaws.com/latest/beaglebone/core-image-base-beaglebone.sdimg](https://mender.s3.amazonaws.com/latest/beaglebone/core-image-base-beaglebone.sdimg).
This image contains *all the partitions* of the storage device, as
described in [Partition layout](../../Devices/Partition-layout).

We need to change some configuration settings in this image so that
the Mender client successfully connects to your Mender
server when it starts.


### Insert the address of Mender server

Please see [Modifying a disk image](../../Artifacts/Modifying-a-disk-image) for a description
on how to mount partitions for editing within the disk image
`core-image-base-beaglebone.sdimg`.

We assume that *both* rootfs partitions are mounted read-write below,
to `/mnt/rootfs1` and `/mnt/rootfs2`. Then run the following commands
to make the Mender client able to find the server when the Mender client starts:

```
echo "$IP_OF_MENDER_SERVER_FROM_DEVICE docker.mender.io mender-artifact-storage.s3.docker.mender.io" | sudo tee -a /mnt/rootfs[12]/etc/hosts
```

We also need to modify `ServerURL` in the rootfs partitions at `/etc/mender/mender.conf`
to `https://docker.mender.io:8080`. This can be achieved by manually editing or running
the command below:

```
sudo sed -i -E "s/([ ]*\"ServerURL\"[ ]*:[ ]*)\".*\"/\1\"https:\/\/docker.mender.io:8080\"/" /mnt/rootfs[12]/etc/mender/mender.conf
```

You should see output similar to the following:

> 192.168.10.1 docker.mender.io mender-artifact-storage.s3.docker.mender.io


### Set a static device IP address and subnet

This section assumes you use a static IP setup.
If your BeagleBone Black device uses a DHCP setup,
you need to adjust or skip the steps described here accordingly.
In this section, we assume that `$IP_OF_MENDER_CLIENT` is
the IP address you assign to your device.

!!! If you are using `bash`, you can set a variable before running the command below, for example `IP_OF_MENDER_CLIENT="192.168.10.2"`.

Run the command below to fill the `systemd`
networking configuration files of the rootfs partitions:

```
echo -n "
[Match]
Name=eth0

[Network]
Address=$IP_OF_MENDER_CLIENT
Gateway=$IP_OF_MENDER_SERVER_FROM_DEVICE
" | sudo tee /mnt/rootfs[12]/etc/systemd/network/eth.network
```

You should see output similar to the following:

> [Match]  
> Name=eth0  
  
> [Network]  
> Address=192.168.10.2  
> Gateway=192.168.10.1  


! If you have a static IP address setup for several BeagleBone Black devices, you need several disk images so each get different IP addresses. After unmounting (as described below), you can copy it and mount another one.

### Unmount the disk image

It is very important to unmount the disk image after modifying it, so all changes are written to the image:

```
sudo umount /mnt/rootfs1 && sudo umount /mnt/rootfs2
```

!! If you do not properly unmount the disk image, changes may be lost or corrupted when it is written to flash.


## Write the disk image to the SD card

Please see [Write the disk image to the SD card](../../Artifacts/Provisioning-a-new-device#write-the-disk-image-to-the-sd-card)
for steps how to provision the device disk using the `core-image-base-beaglebone.sdimg`
image you downloaded and modified above.

If you have several BeagleBone Black devices, please
write the disk image to all their SD cards.


## Boot the BeagleBone Black(s)

First, insert the SD card you just provisioned into the BeagleBone black.

Before powering on the device, please press the
S2 button, as shown below. Connect the power and keep the button
pressed for about 5 seconds. This will make the BeagleBone
Black boot from the SD card instead of internal storage.

![Booting BeagleBone Black from SD card](beaglebone_black_sdboot.png)

!! If the BeagleBone Black boots from internal storage, the rollback mechnism of Mender will not work properly. However, the device will still boot so this condition is hard to detect.

!!! There is no need to press the S2 button when rebooting, just when power is lost and it is powered on again.


## See devices in UI authorize

**TODO** Verify they show. Network & Mender daemon Diagnostics? Log in to BBB / serial cable. root wihtout PW.


## Create a group with the BeagleBone Black device(s)

**TODO** How to create group, warn that mixing qemu & BBB in same deployment is not reliable yet for reporting.


## Prepare the rootfs image to update to

! Please make sure to set a shell variable that expands correctly with `$IP_OF_MENDER_SERVER_FROM_DEVICE` or edit the commands below accordingly.

In order to deploy an update, we need a rootfs image to update to.
Download the demo *rootfs* image with Mender support for the BeagleBone Black
at [https://mender.s3.amazonaws.com/latest/beaglebone/core-image-base-beaglebone.ext4](https://mender.s3.amazonaws.com/latest/beaglebone/core-image-base-beaglebone.ext4).

Please see [Modifying a rootfs image](../../Artifacts/Modifying-a-rootfs-image)
for a description on how to modify configuration files in rootfs images.
For the following steps we assume that you have mounted `core-image-base-beaglebone.ext4`
to `/mnt/rootfs`.

We carry out exactly the same configuration steps for the rootfs image
as we did for the rootfs partitions in the disk image above:

```
echo "$IP_OF_MENDER_SERVER_FROM_DEVICE docker.mender.io mender-artifact-storage.s3.docker.mender.io" | sudo tee -a /mnt/rootfs/etc/hosts
```

You should see output similar to the following:

> 192.168.10.1 docker.mender.io mender-artifact-storage.s3.docker.mender.io

```
sudo sed -i -E "s/([ ]*\"ServerURL\"[ ]*:[ ]*)\".*\"/\1\"https:\/\/docker.mender.io:8080\"/" /mnt/rootfs/etc/mender/mender.conf
```

Separate section!
﻿⁠⁠⁠⁠vi /etc/systemd/network/eth.network
**TODO** If not using DHCP server (like router), set IP address of device and same subnet on device & workstation.

```
[Match]
Name=eth0

[Network]
Address=192.168.10.105
Gateway=192.168.10.1
```

!!! ROllback no network

It is very important to unmount the rootfs image after modifying it, so all changes are written to the image:

```
sudo umount /mnt/rootfs
```

!! If you do not properly unmount the rootfs image, changes may be lost or corrupted when it is written to flash.


## Upload rootfs image

**TODO**


## Deploy rootfs image

**TODO**

**Congratulations!** You have used the Mender server to deploy your first physical device update!
Now that you have seen how Mender works with a reference device, you might be wondering what
it would take to port it to your own platform. The first place to go is
[Device integration](../../Devices), where you will find out how to integrate
the Mender client with your device software, and then look at
[Creating artifacts](../../Artifacts) to see how to build images ready to be
deployed over the network to your devices.


## Next steps

**TODO** modify rootfs; blinken lights
build for your device.
