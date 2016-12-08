---
title: Modifying poll intervals
taxonomy:
    category: docs
---

The whole communication between the Mender client and the server is always initiated by the client. Thus it is important to
configure the client so that the frequency of sending various requests to the server is accurate.

At the moment, there are two configuration parameters allowing setting up the frequency of communication between
the client and the server: `UpdatePollIntervalSeconds` and `InventoryPollIntervalSeconds`.

`UpdatePollIntervalSeconds` indicates how frequently the client will send an update check request to the server.
The default value is set to 1800 (seconds).

`InventoryPollIntervalSeconds` sets the frequency of sending the inventory data by the client. The default value is set so that the client
updates the inventory once every day. Additionally inventory information are send after each boot of the device and after the new
update has been correctly applied and committed by the device.

## How to choose right intervals

In order to set up the intervals correctly several things needs to be taken into account.

The higher the frequency is the sooner the server will be updated with the client inventory data and the client will
polls the update install request faster. But there is a trade-off as the higher frequency is, the more load
server will receive. Having lot of clients connected to one server will cause more resources will be needed server side
to keep the environment responsive.
From the other hand, the lower frequency is the lower server load will be and having the same hardware, server will be
able to handle more client connections.

## Changing the parameters for existing image file

Both parameters are stored in `/etc/mender/mender.conf` configuration file:

```
{
  "ClientProtocol": "http",
  "HttpsClient": {
    "Certificate": "",
    "Key": ""
  },
  "RootfsPartA": "/dev/mmcblk0p2",
  "RootfsPartB": "/dev/mmcblk0p3",
  "UpdatePollIntervalSeconds": 1800,
  "InventoryPollIntervalSeconds": 3600,
  "ServerURL": "https://docker.mender.io",
  "ServerCertificate": "/etc/mender/server.crt"
```

In order to change the default values loopback-mount the rootfs on your workstation
and modify the configuration you need.

In this example we will modify  `/etc/mender/mender.conf` on an `ext4` file system,
but these steps can be used for modifying any configuration file and for
several file system types.

```
sudo mkdir /mnt/rootfs
```

```
sudo mount -t ext4 -o loop <PATH-TO-ROOTFS-IMAGE>.ext4 /mnt/rootfs/
```

Now you can modify the file found at `/mnt/rootfs/etc/mender/mender.conf`.
After saving your changes, simply unmount the rootfs again:

```
sudo umount /mnt/rootfs
```

You need to adjust the path to the rootfs image and its type depending on the machine and file system you are building for.
After deploying this rootfs image with Mender and rebooting, your configuration changes will be in effect!

## Modifying the Yocto build parameters

In order to set up the custom values for both `UpdatePollIntervalSeconds` and `InventoryPollIntervalSeconds` in Yocto
change the following in `meta-mender/meta-mender-core/recipes-mender/mender/mender_0.1.bb` file:

```
MENDER_UPDATE_POLL_INTERVAL_SECONDS ?= "1800"
MENDER_INVENTORY_POLL_INTERVAL_SECONDS ?= "1800
```

After this is done, continue building the Yocto image as documented [here](../../Artifacts/Building-Mender-Yocto-image).





