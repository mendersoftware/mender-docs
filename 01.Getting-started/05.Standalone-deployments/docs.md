---
title: Standalone deployments
taxonomy:
    category: docs
---

In this tutorial we will demonstrate *standalone* deployments with the Mender client,
where no Mender server is used and the deployments are triggered at the
device terminal either manually or by custom scripts. This can be useful in order
to deploy updates to devices which do not have network connectivity or
are updated through external storage like a USB stick.

For an explanation of the difference between *managed* and *standalone* deployments, please see
[Modes of operation](../../Architecture/overview#modes-of-operation).


## Prerequisites

The tutorial will in general assume that you use a physical device connected
to your workstation. However, it can also be carried out with a virtual
QEMU device so you do not have to configure any hardware. If you follow
it using a QEMU device, please make sure QEMU for the ARM architecture
works, it is typically installed with the `qemu-system-arm` package.

### Device storage and rootfs images

You will need two images of different types.

The first is an image file to flash to the entire storage of the
device. `meta-mender` creates these files with a `.sdimg`
suffix, so they are easy to recognize. This file contains
all the partitions of the given storage device, as
described in [Partition layout](../../Devices/Partition-layout).
In addition, you need a rootfs image to update to. The suffix
of this file depends on the file system used for rootfs,
for example `.ext4`.

You can build the required images by following the steps
described in [Building a Mender Yocto Project image](../../Artifacts/Building-Mender-Yocto-image).

!!! If you are testing Mender on the reference platforms BeagleBone Black or QEMU, you can save the build time by using the [latest prebuilt demo images](https://mender-standalone.s3.amazonaws.com/latest/latest.tar.gz). The `.sdimg` and `.ext4` images are found in the `vexpress-qemu` and `beaglebone` directories.


### Network connectivity

There must be network connectivity between your workstation and the device.
For example, you could connect your workstation and the device using a cross-over
Ethernet cable and use static IP addresses at both ends.

!!! If you are testing with QEMU, the network is automatically set up by the provided script `mender-qemu.sh`.


## Write the disk image to the SD card

Please see [Provisioning a new device](../../Artifacts/Provisioning-a-new-device)
for steps how to provision the device storage using the `*.sdimg` image.

!!! If you are testing with QEMU, there is no need to do this step as you will run it from virtual storage.


## Boot the device

Take the SD card out of your card reader and insert it into your device.
Then boot the device from the SD card, which might entail keeping a button pressed
during boot until you see console output, or change of a jumper setting.

! If you boot from internal flash storage (which is standard on BeagleBone Black unless the S2 button is pressed), this will interfere with Mender's rollback mechanism.

!!! If you are testing with QEMU, you can boot the device by changing directory to the location of the `mender-qemu.sh` script and running `/bin/sh mender-qemu.sh`.

This will take you to the login prompt, and you should see a message similar to the following:

> "Poky (Yocto Project Reference Distro)..."

!!! If you are using the Mender demo images, you can login with user *root*. No password is required. 


## Serve a rootfs image to the device over http

To deploy a new rootfs to the device, you need to start a http server on your workstation to serve the image. Open a new terminal **on your workstation** and change into the directory with your rootfs image (e.g. `*.ext4`). Start a simple Python webserver in that directory, like so:

```
python -m SimpleHTTPServer
```

!!! SimpleHTTPServer starts on port 8000, but the IP address your device should use to reach it depends on the network setup between your device and workstation. You can find the IP address by using network tools like ```ip``` on your workstation. We will assume the device can reach your workstation's web server on ```http://<IP-OF-WORKSTATION>:8000/```.

!!! If you are testing with QEMU, the virtual device should be able to access your workstation's directory at `http://10.0.2.2:8000/`, i.e. `<IP-OF-WORKSTATION>` is `10.0.2.2` in this case.


## Deploy the new rootfs to the device

In your **device terminal**, test the connection to the workstation with:

```
ping <IP-OF-WORKSTATION>
```

To deploy the new rootfs image to your device, run the following command in its terminal:


```
mender -log-level info -rootfs http://<IP-OF-WORKSTATION>:8000/<ROOTFS-IMAGE>
```

Use the appropriate rootfs image file in place of `<ROOTFS-IMAGE>`, e.g. `core-image-full-cmdline.ext4`.
You can find the right name by opening a browser at [http://localhost:8000](http://localhost:8000?target=_blank).

Mender will download the new image, write it to the inactive rootfs partition and configure the bootloader to boot into it on the next reboot. This should take about 2 minutes to complete.

!!! The `mender -rootfs` option accepts http(s) URIs, as well as file paths. Thus you can also update from a file system file from local storage like a USB-stick or remotely-mounted storage like NFS by simply changing the path to the image accordingly.

To run the updated rootfs image, simply reboot your device:

```
reboot
```

Your device should boot into the updated rootfs.

!!! If you are using the Mender demo images, you can verify the new rootfs image is running as you see a message similar to *This system has been updated by Mender build...* before the login prompt.

**Congratulations!** You have just deployed your first rootfs image with Mender!
If you are happy with the update, you can make it permanent by running the following in your device terminal:


```
mender -commit
```

By running this command, Mender will configure the bootloader to persistently boot from this updated rootfs partition. To deploy another update, simply follow these instructions again (from `mender ... -rootfs ...`).

!!! If we reboot the device again *without* running ```mender -commit```, it will boot into the previous rootfs partition that is known to be working (where we deployed the update from). This ensures a robust update process in cases where the newly deployed rootfs does not boot or otherwise has issues that we want to roll back from. Also note that it is possible to automate deployments by [running the Mender client as a daemon](../../Architecture/overview#modes-of-operation).
