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
(where you have the Mender server running) and vice versa.
If you have one BeagleBone Black, you could connect your
workstation and the device using a cross-over
Ethernet cable and use static IP addresses at both ends.
For multiple devices, you need a router or switch.


## Prepare the storage image

Download the demo *storage* image with Mender support for the BeagleBone Black
at [https://mender.s3.amazonaws.com/latest/beaglebone/core-image-base-beaglebone.sdimg](https://mender.s3.amazonaws.com/latest/beaglebone/core-image-base-beaglebone.sdimg).
This image contains *all the partitions* of the storage device, as
described in [Partition layout](../../Devices/Partition-layout).

We need to edit some configurations in this image so that
the Mender client connects to your Mender server when it starts.

There are multiple ways you can connect your device to the Mender server. As the detailed setup depends on your network topology 
in this tutorial we will focus on the simplest case. The host where the Mender server is running is connected with your device 
via ethernet cable. In this setup you need to configure static IP address on both eth0 network interface of your server and eth0 interface 
of your beaglebone.

In order to set static IP address on a given interface, use the following command:
`ifconfig eth0 192.168.10.10`

Once the IP address is set, modify the content of `/etc/hosts` file on the device. In order to be able to connect to the Mender server,
add following line:
`192.168.10.10 docker.mender.io mender-artifact-storage.s3.docker.mender.io`

It is also needed to modify `/etc/mender/mender.conf` and update `ServerURL` to look like below:
`"ServerURL": "https://docker.mender.io:8080"`.

This can be done before device is up and running by modifying appropriate files after copying `.sdimg` file to the SD card. 


## Write the storage image to the SD card

Please see [Write the storage image to the SD card](../../Artifacts/Provisioning-a-new-device#write-the-storage-image-to-the-sd-card)
for steps how to provision the device storage using the `core-image-base-beaglebone.sdimg`
image you downloaded and modified above.


## Prepare the rootfs image to update to

In order to deploy an update, we need a rootfs image to update to.

Download the demo *rootfs* image with Mender support for the BeagleBone Black
at [https://mender.s3.amazonaws.com/latest/beaglebone/core-image-base-beaglebone.ext4](https://mender.s3.amazonaws.com/latest/beaglebone/core-image-base-beaglebone.ext4).

**TODO** mount & edit configs:
- check the IP address of the host machine where server is running (ip a or similar command)
- modify the /etc/hosts file on the device (you can modify the image before installing as well) to contain following changes:
-- IP_of_mender_server docker.mender.io
-- IP_of_mender_server mender-artifact-storage.s3.docker.mender.io
- modify /etc/mender/mender.conf file to contain following line:
-- "ServerURL": "docker.mender.io:8080"


## Boot device

**TODO** Note & picture about pressing S2 button.!



## Create a group with the BeagleBone Black device(s)

**TODO** How to create group, warn that mixing qemu & BBB in same deployment is not reliable yet for reporting.


## Upload image

**TODO**

## Deploy image

**TODO**


**Congratulations!** You have used the Mender server to deploy your first physical device update!
Now that you have seen how Mender works with a reference device, you might be wondering what
it would take to port it to your own platform. The first place to go is
[Device integration](../../Devices), where you will find out how to integrate
the Mender client with your device software, and then look at
[Creating artifacts](../../Artifacts) to see how to build images ready to be
deployed over the network to your devices.
