---
title: Modifying a rootfs image
taxonomy:
    category: docs
---

When testing deployments, it is useful that the rootfs image you are deploying is different from the one that you have installed so you can see that the update is successful.
A simple way to acheive this is to loopback-mount the rootfs on your workstation and modify `/etc/issue` so you can see which image you are running just before the login prompt.

For example, if you are using the `ext4` file system type you can do the following.

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
After deploying this rootfs image with Mender and rebooting, you should see your new message at the login prompt!
