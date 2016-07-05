---
title: Your first update on QEMU
taxonomy:
    category: docs
---

This tutorial will show you how to deploy a rootfs image onto a QEMU machine and verify that the update was successful after reboot. We will use prebuilt images, so you don't have to compile or build Mender.


## Prerequisites

The workstation needs [QEMU](http://wiki.qemu.org/?target=_blank) with ARM processor support installed and a minimum of 1 GiB of free memory. QEMU runs on various platforms and can easily be installed using package managers.

Debian and Ubuntu:

```
apt-get install qemu-system-arm
```

Red Hat, CentOS and Fedora:

```
yum install qemu-system-arm
```

To verify that QEMU is correctly installed, check its version with:

```
qemu-system-arm -version
```

## Download and unpack prebuilt images 
If you have already [built a Yocto Project image with Mender](../../Artifacts/Building-Mender-Yocto-image), please move on to the [next section](#run-the-image-in-qemu). If you don't have any images to test, you can download our latest build which contains the necessary images for testing. It will also contain images for BeagleBone Black.

```
mkdir mender
cd mender
wget https://goo.gl/mmJoxs
```

Unpack the tarball:

```
tar -zxvf mmJoxs

  vexpress-qemu/u-boot.elf
  vexpress-qemu/core-image-full-cmdline-vexpress-qemu.sdimg
  vexpress-qemu/core-image-full-cmdline-vexpress-qemu.ext3
  vexpress-qemu/mender-qemu.sh
  beaglebone/core-image-base-beaglebone.ext3
  beaglebone/core-image-base-beaglebone.sdimg
  BUILD
  README
```


## Run the image in QEMU
Run the image in QEMU by running the following commands:

```
cd vexpress-qemu
```
```
/bin/sh mender-qemu.sh
```

This will take you to the login prompt. Above the prompt you should see a welcome message similar
to this:

> "Poky (Yocto Project Reference Distro) 2.0.2 vexpress..."

You can login with user *root*. No password is required. 

## Serve a rootfs image for the QEMU machine

To deploy a new rootfs to the QEMU machine, you need to start a http server on your workstation to serve the image. Open a new shell on your workstation and change into the vexpress-qemu directory. There you will find an update image named ```core-image-full-cmdline-vexpress-qemu.ext3```. Start a simple Python webserver in that directory, like so:

```
python -m SimpleHTTPServer
```

!!! By default the QEMU machine can reach your workstation on IP address 10.0.2.2 and SimpleHTTPServer starts on port 8000, so your QEMU machine should now be able to access your workstation's directory at ```http://10.0.2.2:8000/```, while you can test it from a browser at [http://localhost:8000](http://localhost:8000).

## Deploy the new rootfs to the QEMU machine with Mender

In your QEMU machine's terminal, test the connection to the workstation with:

```
ping 10.0.2.2
```

To deploy the new image to your QEMU machine, run the following command in its terminal:

```
mender -log-level info -rootfs http://10.0.2.2:8000/core-image-full-cmdline-vexpress-qemu.ext3
```

Mender will download the new image, write it to the inactive rootfs partition and configure the bootloader to boot into it on the next boot. This should take about 2 minutes to complete.

To run the updated rootfs image, simply reboot your QEMU machine:

```
reboot
```

QEMU should boot into the updated rootfs, and a welcome message like this should greet you:

> "This system has been updated by Mender build 376 compiled on..."

**Congratulations!** You have just deployed your first rootfs image with Mender! To deploy another update, simply follow the same steps again.

!!! Behind the scenes the Mender daemon comes up after a successful boot into the updated partition and runs `mender -commit`. This configures the bootloader to persistently boot from this updated rootfs partition. However, if the boot fails before the Mender daemon comes up, it will boot into the previous rootfs partition that is known to be working (where we deployed the update from). This ensures strong reliability in form of a rollback in cases where the newly deployed rootfs does not boot correctly for any reason.
