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
at [https://d1b0l86ne08fsf.cloudfront.net/latest/beaglebone/core-image-base-beaglebone.sdimg](https://d1b0l86ne08fsf.cloudfront.net/latest/beaglebone/core-image-base-beaglebone.sdimg).
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

You should see output similar to the following:

> 192.168.10.1 docker.mender.io mender-artifact-storage.s3.docker.mender.io

We also need to modify `ServerURL` in the rootfs partitions at `/etc/mender/mender.conf`
to `https://docker.mender.io:8080`. This can be achieved by manually editing or running
the command below:

```
sudo sed -i -E "s/([ ]*\"ServerURL\"[ ]*:[ ]*)\".*\"/\1\"https:\/\/docker.mender.io:8080\"/" /mnt/rootfs[12]/etc/mender/mender.conf
```


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
echo -n "\
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

! Make sure that the Mender server is running as described in [Create a test environment](../Create-a-test-environment) and that the device can reach it on the IP address you configured above (`$IP_OF_MENDER_SERVER_FROM_DEVICE`). You might need to set a static IP address where the Mender server runs and disable any firewalls.

First, insert the SD card you just provisioned into the BeagleBone black.

Before powering on the device, please press the
*S2 button*, as shown below. Connect the power and keep the button
pressed for about 5 seconds. This will make the BeagleBone
Black boot from the SD card instead of internal storage.

![Booting BeagleBone Black from SD card](beaglebone_black_sdboot.png)

!! If the BeagleBone Black boots from internal storage, the rollback mechanism of Mender will not work properly. However, the device will still boot so this condition is hard to detect.

!!! There is no need to press the S2 button when rebooting, just when power is lost and it is powered on again.


## See the BeagleBone Black(s) in the Mender UI

If you refresh the Mender server UI (by default found at [http://localhost:8080/](http://localhost:8080/?target=_blank)),
you should see one or more devices waiting authorization.

Once you **authorize** these devices, Mender will auto-discover
inventory about the devices, including the device type (e.g. beaglebone)
and the IP addresses, as shown in the example below.

![Mender UI - Device information for BeagleBone Black](device_information_bbb.png)


!!! If your BeagleBone Black does not show up for authorization in the UI, you need to diagnose what went wrong. Most commonly this is due to problems with the network. You can test if your workstation can reach the device by trying to ping it, e.g. with `ping 192.168.10.2` (replace with the IP address of your device). If you have a serial cable, you can log in to the device to diagnose. The `root` user is present and has an empty password in this test image. If you get stuck, please feel free to reach out on the [Mender community mailing list](https://groups.google.com/a/lists.mender.io/forum?target=_blank#!forum/mender)!


## Prepare the rootfs image to update to

! Please make sure to set shell variables that expand correctly with `$IP_OF_MENDER_SERVER_FROM_DEVICE` (always) and `$IP_OF_MENDER_CLIENT` (if you are using static IP addressing) or edit the commands below accordingly.

In order to deploy an update, we need a rootfs image to update to.
Download the demo *rootfs* image with Mender support for the BeagleBone Black
at [https://d1b0l86ne08fsf.cloudfront.net/latest/beaglebone/core-image-base-beaglebone.ext4](https://d1b0l86ne08fsf.cloudfront.net/latest/beaglebone/core-image-base-beaglebone.ext4).

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

Next, ensure we have the right `ServerURL`:

```
sudo sed -i -E "s/([ ]*\"ServerURL\"[ ]*:[ ]*)\".*\"/\1\"https:\/\/docker.mender.io:8080\"/" /mnt/rootfs/etc/mender/mender.conf
```

Finally, **only if you are using static IP addressing**, you need to set the
device IP address, as shown below. Please note that the same
constraints as described in [Set a static device IP address and subnet](#set-a-static-device-ip-address-and-subnet)
for the disk image apply here.

```
echo -n "\
[Match]
Name=eth0

[Network]
Address=$IP_OF_MENDER_CLIENT
Gateway=$IP_OF_MENDER_SERVER_FROM_DEVICE
" | sudo tee /mnt/rootfs/etc/systemd/network/eth.network
```

You should see output similar to the following:

> [Match]  
> Name=eth0  
  
> [Network]  
> Address=192.168.10.2  
> Gateway=192.168.10.1  


!!! The Mender client will roll back the deployment if it is not able to report the final update status to the server when it boots from the updated partition. This helps ensure that you can always deploy a new update to your device, even when fatal conditions like network misconfiguration occur.


### Set the rootfs Image ID

When you upload this image (below), it is very important that you use the right Image ID,
which is used to decide if a given update is already installed or not.
Mender will skip a deployment for a given device if it sees that
the Image ID in a deployment is the same as the one installed.

Furthermore, the disk image we wrote to the SD card might have the
same Image ID in its rootfs partitions as the rootfs we downloaded above.
For these reasons, we will set the rootfs Image ID to **release10**,
as shown with the command below.

```
sudo sed -i -E "s/(IMAGE_ID[ ]*=[ ]*).*/\1release10/" /mnt/rootfs/etc/mender/build_mender
```

You can also make any other modifications you wish in this image
prior to deploying it.


### Unmount the rootfs image

It is very important to unmount the rootfs image after modifying it, so all changes are written to the image:

```
sudo umount /mnt/rootfs
```


## Upload the rootfs image to the server

Before we can deploy the rootfs image we prepared above it needs
to be uploaded to the server.

Go to the Mender server UI, click the **Software** tab and upload this image,
using the fields below:

* Name: `release10`
* Yocto ID: `release10` (**NB! use the string you [set above](#set-the-rootfs-image-id)**)
* Checksum: `test`
* Device type compatibility: `beaglebone`
* Description: `My test build`

In the UI, it should look something like this:

![Mender UI - Upload image BeagleBone Black](upload_image_bbb.png)


## Deploy the rootfs image

Now that we have the device connected and the image
uploaded to the server, all that remains is to go to the
**Deployments** tab and click **Create a deployment**.

Select the image you just uploaded and **All devices**, then
**Create deployment**.

!!! If you deploy to several device types (e.g. vexpress-qemu), the Mender server will skip these if no compatible image is available. This condition is indicated by the *noimage* status. Mender does this to avoid deployments of incompatible rootfs images.


## See the progress of the deployment

As the deployment progresses, you can click on it to view more details about the current status across all devices.
In the example below, we can see that a BeagleBone has installed the update and is rebooting into it,
while a QEMU device skipped the deployment because no compatible image was available for it.

![Mender UI - Deployment progress - BeagleBone Black](deployment_report_bbb.png)

Once the deployment completes, you should see its report in *Past deployments*.

**Congratulations!** You have used the Mender server to deploy your first physical device update!


## Deploy another update

As we noted in [Set the rootfs Image ID](#set-the-rootfs-image-id) above,
the Image ID of the deployment needs to be different than the currently running Image ID for
Mender to deploy a new update. So if you want to reuse the rootfs image we
already have by making changes to it and deploying it again, make sure to
change the Image ID as well!

With that in mind, now might be a good time to tweak the image, add some
more BeagleBone Black devices to the environment and try to get the
required blinkenlights going!

If you want to build your own image for the BeagleBone Black,
head over to the tutorial [Building a Mender Yocto Project image](../../Artifacts/Building-Mender-Yocto-image).


## Integrate Mender with your device

We can have a lot of fun with the BeagleBone Black, however
it is rarely used in production due to the cost of scaling and specific
needs of custom applications.

Now that you have seen how Mender works with a reference device, you might be wondering what
it would take to port it to your own platform. The first place to go is
[Device integration](../../Devices), where you will find out how to integrate
the Mender client with your device software, and then look at
[Creating artifacts](../../Artifacts) to see how to build images ready to be
deployed over the network to your devices.
