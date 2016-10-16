---
title: Modifying a rootfs image
taxonomy:
    category: docs
---

When testing deployments, it is useful that the rootfs image you are deploying
is different from the one that you have installed so you can see that the update is successful.
You might also want to configure certain aspects of the rootfs update after you build it,
but before deploying it.

A simple way to achieve this is to loopback-mount the rootfs on your workstation
and modify the configuration files you need.

In this example we will modify  `/etc/issue` on an `ext4` file system
so you can see which rootfs image you are running just before the login prompt,
but these steps can be used for modifying any configuration file and for
several file system types.

```
sudo mkdir /mnt/rootfs
```

```
sudo mount -t ext4 -o loop <PATH-TO-ROOTFS-IMAGE>.ext4 /mnt/rootfs/
```

Now you can modify the file `/mnt/rootfs/etc/issue` so you can detect a change.
After saving your modified issue-file, simply unmount the rootfs again:

```
sudo umount /mnt/rootfs
```

You need to adjust the path to the rootfs image and its type depending on the machine and file system you are building for.
After deploying this rootfs image with Mender and rebooting, your configuration changes will be in effect!
