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
`<IP-OF-MENDER-SERVER-FROM-DEVICE>` will be the IP address
that your device(s) can connect to the Mender server.


## Prepare the storage image

Download the demo *storage* image with Mender support for the BeagleBone Black
at [https://mender.s3.amazonaws.com/latest/beaglebone/core-image-base-beaglebone.sdimg](https://mender.s3.amazonaws.com/latest/beaglebone/core-image-base-beaglebone.sdimg).
This image contains *all the partitions* of the storage device, as
described in [Partition layout](../../Devices/Partition-layout).

We need to change some configurations in this image so that
the Mender client connects to your Mender server when it starts.

Please see [Modifying a storage image](../../Artifacts/Modifying-a-storage-image) for a description
on how to mount partitions for editing within the device storage image
`core-image-base-beaglebone.sdimg`.

We assume that *both* rootfs partitions are mounted read-write below,
to `/mnt/rootfs1` and `/mnt/rootfs2`. Then run the following commands
to make the Mender client able to find the server when the Mender client starts:

```
IP_OF_MENDER_SERVER_FROM_DEVICE="<IP-OF-MENDER-SERVER-FROM-DEVICE>"  # insert the actual IP to fill this shell variable
```

```
echo "$IP_OF_MENDER_SERVER_FROM_DEVICE docker.mender.io mender-artifact-storage.s3.docker.mender.io" | sudo tee -a /mnt/rootfs[12]/etc/hosts
```

We also need to modify `ServerURL` in the rootfs partitions at `/etc/mender/mender.conf`
to `https://docker.mender.io:8080`. This can be achieved by manually editing or running
the command below:

```
sudo sed -i -E "s/([ ]*\"ServerURL\"[ ]*:[ ]*)\".*\"/\1\"https:\/\/docker.mender.io:8080\"/" /mnt/rootfs[12]/etc/mender/mender.conf
```

It is very important to unmount the storage image after modifying it, so all changes are written to the image:

```
sudo umount /mnt/rootfs1
```

```
sudo umount /mnt/rootfs2
```

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
