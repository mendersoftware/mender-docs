---
title: Mender command line interface
taxonomy:
    category: docs
---

##The partition layout of the device is not as expected

You have the Mender binary on your device and try to trigger a rootfs update but you get output similar to the following:

```
mender -rootfs /media/rootfs-image-mydevice.ext4

ERRO[0000] exit status 1                                 module=partitions
ERRO[0000] No match between boot and root partitions.    module=main
```

The problem here is most likely that the device does not have the [partition layout Mender expects](../../Devices/Partition-layout). This could have happened if you just placed the Mender binary into your rootfs, but did not [reflash the entire storage device](../../Getting-started/Your-first-update-on-BeagleBone#write-the-disk-image-to-the-sd-card) with the `.sdimg.` file output from the [Yocto Project build](../../Artifacts/Building-Mender-Yocto-image). When this happens, output from `mount` and `fw_printenv` can confirm that this is the problem you are seeing. The solution is to flash your entire storage device with the `.sdimg` output from the Yocto Project build process.
