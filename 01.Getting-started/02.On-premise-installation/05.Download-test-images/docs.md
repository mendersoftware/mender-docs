---
title: Download demo images
taxonomy:
    category: docs
---

For partial updates such as application updates, you can [install Mender on your device as a .deb package](../../../client-configuration/installing#install-mender-provided-debian-package). This is the quickest and easiest way to get started with Mender.

Pre-built demo images for a set of reference boards are provided below, so you do not have to integrate devices nor build images in order to test Mender.

!!! Steps to build Artifacts for other device types and with custom software are provided at [Building a Mender Yocto Project image](../../../artifacts/yocto-project/building), however we recommend using the demo images first.

! Do not use these images if you are using [Mender Professional](https://mender.io/products/mender-professional?target=_blank). Instead, use the images customized for your account from [the Help section](https://hosted.mender.io/ui/#/help/connecting-devices/demo-artifacts?target=_blank).

There are two types of images:
* Disk images (`*.sdimg`): Used to provision the device storage for devices without Mender running already.
* Mender Artifacts (`*.mender`): Upload them to the Mender server in order to deploy new root file systems to devices already running Mender and registered with the server.

Mender will skip deployments if the Artifact installed is the same as the one being deployed. Therefore, two Artifacts are provided for each device type so that you can do several deployments 
by deploying back and forth between these two Artifacts.

Download the Artifacts for your desired device types below:


| Device type      | Disk image | Artifact 1 | Artifact 2 |
|------------------|------------|------------|------------|
| BeagleBone Black | [mender-beagleboneblack.sdimg.gz][mender-beagleboneblack_x.x.x.sdimg.gz] | [beagleboneblack_release_1.mender][beagleboneblack_release_1_x.x.x.mender] | [beagleboneblack_release_2.mender][beagleboneblack_release_2_x.x.x.mender] |
| Raspberry Pi 3   | [mender-raspberrypi3.sdimg.gz][mender-raspberrypi3_x.x.x.sdimg.gz] | [raspberrypi3_release_1.mender][raspberrypi3_release_1_x.x.x.mender] | [raspberrypi3_release_2.mender][raspberrypi3_release_2_x.x.x.mender] |


<!--AUTOVERSION: "cloudfront.net/%/"/mender "%.sdimg.gz"/mender -->
[mender-beagleboneblack_x.x.x.sdimg.gz]: https://d1b0l86ne08fsf.cloudfront.net/2.1.1/beagleboneblack/mender-beagleboneblack_2.1.1.sdimg.gz
<!--AUTOVERSION: "cloudfront.net/%/"/mender "release_1_%"/mender -->
[beagleboneblack_release_1_x.x.x.mender]: https://d1b0l86ne08fsf.cloudfront.net/2.1.1/beagleboneblack/beagleboneblack_release_1_2.1.1.mender
<!--AUTOVERSION: "cloudfront.net/%/"/mender "release_2_%"/mender -->
[beagleboneblack_release_2_x.x.x.mender]: https://d1b0l86ne08fsf.cloudfront.net/2.1.1/beagleboneblack/beagleboneblack_release_2_2.1.1.mender

<!--AUTOVERSION: "cloudfront.net/%/"/mender "%.sdimg.gz"/mender -->
[mender-raspberrypi3_x.x.x.sdimg.gz]: https://d1b0l86ne08fsf.cloudfront.net/2.1.1/raspberrypi3/mender-raspberrypi3_2.1.1.sdimg.gz
<!--AUTOVERSION: "cloudfront.net/%/"/mender "release_1_%"/mender -->
[raspberrypi3_release_1_x.x.x.mender]: https://d1b0l86ne08fsf.cloudfront.net/2.1.1/raspberrypi3/raspberrypi3_release_1_2.1.1.mender
<!--AUTOVERSION: "cloudfront.net/%/"/mender "release_2_%"/mender -->
[raspberrypi3_release_2_x.x.x.mender]: https://d1b0l86ne08fsf.cloudfront.net/2.1.1/raspberrypi3/raspberrypi3_release_2_2.1.1.mender

If you have a BeagleBone Black or Raspberry Pi 3 you want to test Mender with
as well, download the *disk image and both Artifacts* for it.
