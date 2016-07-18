---
title: Your first update on BeagleBone Black
taxonomy:
    category: docs
---


This page will show you how to deploy an image update onto a BeagleBone Black board and verify that the update was successful after reboot. We will use prebuilt images, so you do not have to compile or build Mender.

## Prerequisites

Your workstation must be on the same subnet as the BeagleBone Black. For example, you could connect your workstation and the BeagleBone Black using a cross-over Ethernet cable and use static IP addresses at both ends.

## Download and unpack prebuilt images 
If you have already [built an image which includes Mender](../../Artifacts/Building-Mender-Yocto-image), please move on to [next section](#write-the-disk-image-to-the-sd-card). If you do not have any images to test, you can download our latest builds which contains the necessary images for testing. It will also contain images for QEMU.

Download the latest Mender build:

```
wget https://goo.gl/mmJoxs
```

Unpack the tarball:

```
tar zxvf mmJoxs
```

You should see the files being unpacked:

> mender/  
> mender/beaglebone/  
> mender/beaglebone/core-image-base-beaglebone.ext3  
> mender/beaglebone/core-image-base-beaglebone.sdimg  
> mender/README  
> mender/vexpress-qemu/  
> mender/vexpress-qemu/mender-qemu.sh  
> mender/vexpress-qemu/u-boot.elf  
> mender/vexpress-qemu/core-image-full-cmdline-vexpress-qemu.ext3  
> mender/vexpress-qemu/core-image-full-cmdline-vexpress-qemu.sdimg  
> mender/BUILD  

## Write the disk image to the SD card
The sdimg image is a partitioned image that can be written directly to the SD card.

!! Be careful! If you point to the wrong device when executing the command below, you risk overwriting your workstation's local or connected storage devices.

Assuming you are in the same directory as the beaglebone sdimg, you can write the sdimg to the SD card using the following command:

```
sudo dd if=core-image-base-beaglebone.sdimg of=<DEVICE> bs=1M
```

!!! &lt;DEVICE&gt; depends on where your SD card is placed. Normally this would be something like  ***/dev/mmcblk0*** or ***/dev/sdb***.  If you are unsure how to find the correct device, the Raspberry PI Foundation provide some nice references that can help you: [Linux](https://www.raspberrypi.org/documentation/installation/installing-images/linux.md?target=_blank), [Mac OSX](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md?target=_blank), [Windows](https://www.raspberrypi.org/documentation/installation/installing-images/windows.md?target=_blank).

Writing the sdimg file to to the SD card should take less than one minute.

## Boot the BeagleBone Black from the SD card

Take the SD card out of your card reader and insert it into your BeagleBone Black. Then boot the BeagleBone Black while keeping the S2 button pressed for about 5 seconds or until you see console output.

! The standard BeagleBone Black boot process uses the bootloader from internal flash storage, which will interfere with Mender's rollback mechanism. In order to use the bootloader from the SD card, make sure that S2 (boot) button is pressed while powering on your BeagleBone Black(see image below).

![BeagleBone sdboot button](beaglebone_black_sdboot.jpg)

This will take you to the login prompt. Above the prompt you should see a welcome message like:

> "Poky (Yocto Project Reference Distro) 2.0.2 beaglebone..."

You can login with user *root*. No password is required. 


## Serve a rootfs image for the BeagleBone Black

To deploy a new rootfs to the BeagleBone Black, you need to start a http server on your workstation to serve the image. Open a new shell on your workstation and change into the beaglebone directory. There you will find an update image named ```core-image-base-beaglebone.ext3```. Start a simple Python webserver in that directory, like so:

```
python -m SimpleHTTPServer
```

!!! SimpleHTTPServer starts on port 8000, but the IP address depends on the network setup between the BeagleBone Black and your workstation. You can find the IP address by using tools like ```ifconfig``` on your workstation. We will assume the BeagleBone Black can reach your workstation's web server on ```http://<IP-OF-WORKSTATION>:8000/```, while you can test it from a browser at [http://localhost:8000](http://localhost:8000).

## Deploy the new rootfs to the BeagleBone Black with Mender


In your BeagleBone Black's terminal, test the connection to the workstation with:

```
ping <IP-OF-WORKSTATION>
```

To deploy the new image to your BeagleBone Black, run the following command in its terminal:


```
mender -log-level info -rootfs http://<IP-OF-WORKSTATION>:8000/core-image-base-beaglebone.ext3
```

Mender will download the new image, write it to the inactive rootfs partition and configure the bootloader to boot into it on the next reboot. This should take about 2 minutes to complete.

To run the updated rootfs image, simply reboot your BeagleBone Black:

```
reboot
```

Your device should boot into the updated rootfs, and a welcome message like this should greet you:

> "This system has been updated by Mender build..."

**Congratulations!** You have just deployed your first rootfs image with Mender! To deploy another update, simply follow the same steps again.

!!! Behind the scenes the Mender daemon comes up after a successful boot into the updated partition and runs `mender -commit`. This configures the bootloader to persistently boot from this updated rootfs partition. However, if the boot fails before the Mender daemon comes up, it will boot into the previous rootfs partition that is known to be working (where we deployed the update from). This ensures strong reliability in form of a rollback in cases where the newly deployed rootfs does not boot correctly for any reason.
