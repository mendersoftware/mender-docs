---
title: What is Mender?
taxonomy:
    category: docs
---

Mender is an **open source** remote updater for embedded Linux devices.

The aim of the project is to help secure connected devices by providing a **robust** and **easy** software update process.

As an open source project we welcome contributions. Find out more about how to contribute at [mender.io/community](https://mender.io/community?target=_blank).


## What problem does Mender solve?

One of the challenges surrounding connected devices and the Internet of Things is that devices are now further from your control. Manual, physical updates are difficult when your devices are distributed over a wide area, or in hard-to-reach locations.

You want your devices to be secure and healthy. It is critical that devices are kept up and running on the latest versions of software where vulnerabilities and bugs have been patched. Remote updates also allow you to get new features out to your devices more quickly.

Any failures or interruptions in the update process should not cause your device to be 'bricked' or unreachable. It is important to be able to roll back to the previous working version should anything go wrong during updates.

Remote updates also require a means of secure communication with each device.


## Mender reference devices

In order to lower cost of scaling and meeting needs of specific applications, no two production devices have the same hardware specifications.
This means that software such as Mender must be [integrated with production devices](../../devices).

However, during the testing and validation stage, it is common to use development device to shorten time to experiment and prototype.
Thus, Mender supports two reference devices, one virtual and one physical:

* vexpress-qemu. This is a virtual device, which is handy as you do not need to configure any hardware to try Mender. This device type also comes bundled with the Mender server for easy testing.
* [BeagleBone Black](https://beagleboard.org/black?target=_blank). This is a popular and open physical device, used in many professional environments.

These reference devices are well supported and included in the Mender continuous integration environment.
They are thus an easy way to get started with testing Mender.
You will see references to them throughout the documentation.


## Trying Mender

We have a series of tutorials that show you how Mender works, while giving you hands-on experience.

!!! Going from a fresh system to completing your first managed deployment with Mender, including server setup, should take **less than 1 hour**!

We will start off by getting the Mender server installed and running in [Create a test environment](../create-a-test-environment).
Next, we will deploy to a virtual [Quick Emulator (QEMU)](http://qemu.org?target=_blank) device in [Deploy to virtual devices](../deploy-to-virtual-devices).
Doing the first deployment using QEMU is handy because it means that you do not have to configure any hardware to test Mender.
If you have real hardware in the form of the popular Mender reference device, the [BeagleBone Black](https://beagleboard.org/black?target=_blank),
you can follow the final tutorial in this series, [Deploy to physical devices](../deploy-to-physical-devices).

On the other hand, if you are only interested in triggering deployments with the Mender client manually at the device,
you can follow the [Standalone deployments](../standalone-deployments) tutorial. For an explanation of the
difference between *managed* and *standalone* deployments, please see
[Modes of operation](../../architecture/overview#modes-of-operation).
