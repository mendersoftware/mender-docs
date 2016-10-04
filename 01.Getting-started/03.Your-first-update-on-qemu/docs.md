---
title: Your first update on QEMU
taxonomy:
    category: docs
---

This tutorial will demonstrate Mender using a virtual device in the [Quick Emulator (QEMU)](http://qemu.org), which is handy because it means that you do not have to configure any hardware.
We will go through how to deploy a rootfs image onto a QEMU machine and verify that the update was successful after reboot, using prebuilt images, so you don't have to compile or build Mender.

!!! This tutorial typically takes less than 10 minutes to complete.

## Prerequisites

The workstation needs [QEMU](http://wiki.qemu.org/?target=_blank) with ARM processor support installed and a minimum of 1 GiB of free memory. QEMU runs on various platforms and can easily be installed using package managers.

Debian and Ubuntu:

```
sudo apt-get install qemu-system-arm
```

Red Hat, CentOS and Fedora:

```
yum install qemu-system-arm
```


## Download and unpack prebuilt images 
If you have already [built a Yocto Project image with Mender](../../Artifacts/Building-Mender-Yocto-image), please move on to the [next section](#run-the-image-in-qemu). If you don't have any images to test, you can download our latest build which contains the necessary images for testing. It will also contain images for BeagleBone Black.

Download the latest Mender build:

```
wget https://s3-eu-west-1.amazonaws.com/yocto-builds/latest/latest.tar.gz
```

Unpack the tarball:

```
tar zxvf latest.tar.gz
```

You should see the files being unpacked:

> mender/  
> mender/vexpress-qemu/  
> mender/vexpress-qemu/core-image-full-cmdline-vexpress-qemu.ext4  
> mender/vexpress-qemu/mender-qemu.sh  
> mender/vexpress-qemu/core-image-full-cmdline-vexpress-qemu.sdimg  
> mender/vexpress-qemu/u-boot.elf  
> mender/beaglebone/  
> mender/beaglebone/core-image-base-beaglebone.ext4  
> mender/beaglebone/core-image-base-beaglebone.sdimg  
> mender/README  
> mender/BUILD

## Run the image in QEMU
Run the image in QEMU by running the following commands:

```
cd mender/vexpress-qemu
```
```
/bin/sh mender-qemu.sh
```

This will take you to the login prompt. Above the prompt you should see a welcome message similar
to this:

> "Poky (Yocto Project Reference Distro) 2.0.2 vexpress..."

You can login with user *root*. No password is required. 

## Serve a rootfs image for the QEMU machine

To deploy a new rootfs to the QEMU machine, you need to start a http server on your workstation to serve the image. Open a new shell on your workstation and change into the vexpress-qemu directory. There you will find an update image named ```core-image-full-cmdline-vexpress-qemu.ext4```. Start a simple Python webserver in that directory, like so:

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
mender -log-level info -rootfs http://10.0.2.2:8000/core-image-full-cmdline-vexpress-qemu.ext4
```

Mender will download the new image, write it to the inactive rootfs partition and configure the bootloader to boot into it on the next boot. This should take about 2 minutes to complete.

!!! The `mender -rootfs` option accepts http(s) URIs, as well as file paths. Thus you can also update from a file system file from local storage like a USB-stick or remotely-mounted storage like NFS by simply changing the path to the image accordingly.

To run the updated rootfs image, simply reboot your QEMU machine:

```
reboot
```

QEMU should boot into the updated rootfs, and a welcome message like this should greet you:

> "This system has been updated by Mender build..."

**Congratulations!** You have just deployed your first rootfs image with Mender! If you are happy with the update, you can make it permanent by logging in to the QEMU machine as *root* and running:

```
mender -commit
```

By running this command, Mender will configure the bootloader to persistently boot from this updated rootfs partition. To deploy another update, simply follow these instructions again (from `mender ... -rootfs ...`).

!!! If we reboot the machine again *without* running ```mender -commit```, it will boot into the previous rootfs partition that is known to be working (where we deployed the update from). This ensures strong reliability in cases where the newly deployed rootfs does not boot or otherwise has issues that we want to roll back from. Also note that it is possible to automate deployments by [running the Mender client as a daemon](../../Architecture/overview#modes-of-operation).



## Next steps

Now that you have seen how Mender works with QEMU, you might be wondering what
it would take to port it to your own platform. The first place to go is
[Device configuration](../../Devices), where you will find out how to integrate
the Mender client with your device software, and then look at
[Creating artifacts](../../Artifacts) to see how to build images ready to be
deployed over the network to your devices.
