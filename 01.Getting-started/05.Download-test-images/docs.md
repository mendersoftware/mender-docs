---
title: Download demo images
taxonomy:
    category: docs
---

Pre-built demo images for a set of reference devices are provided below, so you do not have to integrate devices nor build images in order to test Mender.

!!! Steps to build Artifacts for other device types and with custom software are provided at [Building a Mender Yocto Project image](../../artifacts/building-mender-yocto-image), however we recommend using the demo images first.

! Do not use these images if you are using [Hosted Mender](https://hosted.mender.io?target=_blank). Instead, use the images customized for your account from [Hosted Mender's Help section](https://hosted.mender.io/ui/?target=_blank#/help).

There are two types of images:
* Disk images (`*.sdimg`): Used to provision the device storage for devices without Mender running already.
* Mender Artifacts (`*.mender`): Upload them to the Mender server in order to deploy new root file systems to devices already running Mender and registered with the server.

Mender will skip deployments if the Artifact installed is the same as the one being deployed. Therefore, two Artifacts are provided for each device type so that you can do several deployments 
by deploying back and forth between these two Artifacts.

Download the Artifacts for your desired device types below:


| Device type      | Disk image | Artifact 1 | Artifact 2 |
|------------------|------------|------------|------------|
| Virtual          | N/A (part of server) | [vexpress_release_1.mender][autoupdate_vexpress_release_1_x.x.x.mender] | [vexpress_release_2.mender][autoupdate_vexpress_release_2_x.x.x.mender]          |
| BeagleBone Black | [mender-beaglebone-yocto.sdimg.gz][autoupdate_mender-beaglebone-yocto_x.x.x.sdimg.gz] | [beaglebone-yocto_release_1.mender][autoupdate_beaglebone-yocto_release_1_x.x.x.mender] | [beaglebone-yocto_release_2.mender][autoupdate_beaglebone-yocto_release_2_x.x.x.mender] |
| Raspberry Pi 3   | [mender-raspberrypi3.sdimg.gz][autoupdate_mender-raspberrypi3_x.x.x.sdimg.gz] | [raspberrypi3_release_1.mender][autoupdate_raspberrypi3_release_1_x.x.x.mender] | [raspberrypi3_release_2.mender][autoupdate_raspberrypi3_release_2_x.x.x.mender] |


[autoupdate_vexpress_release_1_x.x.x.mender]: https://d1b0l86ne08fsf.cloudfront.net/master/vexpress-qemu/vexpress_release_1_master.mender
[autoupdate_vexpress_release_2_x.x.x.mender]: https://d1b0l86ne08fsf.cloudfront.net/master/vexpress-qemu/vexpress_release_2_master.mender

[autoupdate_mender-beaglebone-yocto_x.x.x.sdimg.gz]: https://d1b0l86ne08fsf.cloudfront.net/master/beaglebone-yocto/mender-beaglebone-yocto_master.sdimg.gz
[autoupdate_beaglebone-yocto_release_1_x.x.x.mender]: https://d1b0l86ne08fsf.cloudfront.net/master/beaglebone-yocto/beaglebone-yocto_release_1_master.mender
[autoupdate_beaglebone-yocto_release_2_x.x.x.mender]: https://d1b0l86ne08fsf.cloudfront.net/master/beaglebone-yocto/beaglebone-yocto_release_2_master.mender

[autoupdate_mender-raspberrypi3_x.x.x.sdimg.gz]: https://d1b0l86ne08fsf.cloudfront.net/master/raspberrypi3/mender-raspberrypi3_master.sdimg.gz
[autoupdate_raspberrypi3_release_1_x.x.x.mender]: https://d1b0l86ne08fsf.cloudfront.net/master/raspberrypi3/raspberrypi3_release_1_master.mender
[autoupdate_raspberrypi3_release_2_x.x.x.mender]: https://d1b0l86ne08fsf.cloudfront.net/master/raspberrypi3/raspberrypi3_release_2_master.mender


For the [Deploy to virtual devices tutorial](../deploy-to-virtual-devices), download both Artifacts for the *Virtual* device.

If you have a BeagleBone Black or Raspberry Pi 3 you want to test Mender with
as well, download the *disk image and both Artifacts* for it.
