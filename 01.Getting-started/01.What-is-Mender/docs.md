---
title: What is Mender?
taxonomy:
    category: docs
---

Mender is an **open source** remote updater for embedded Linux devices.

The aim of the project is to help secure connected devices by providing a **robust** and **secure** software update process.

As an open source project we welcome contributions. Find out more about how to contribute at [mender.io/community](https://mender.io/community?target=_blank).


## What problem does Mender solve?

One of the challenges surrounding connected devices and the Internet of Things is that devices are now further from your control. Manual, physical updates are difficult when your devices are distributed over a wide area, or in hard-to-reach locations.

You want your devices to be secure and healthy. It is critical that devices are kept up and running on the latest versions of software where vulnerabilities and bugs have been patched. Remote updates also allow you to get new features out to your devices more quickly.

Any failures or interruptions in the update process should not cause your device to be 'bricked' or unreachable. It is important to be able to roll back to the previous working version should anything go wrong during updates.

Remote updates also require a means of secure communication with each device.


## Trying Mender

We have a series of tutorials that show you how Mender works, while giving you hands-on experience.

!!! Going from a fresh system to completing your first managed deployment with Mender, including server setup, should take **less than 1 hour**!

We will start off by getting the Mender server installed and running in [Create a test environment](../Create-a-test-environment).
Next, we will deploy to a virtual [Quick Emulator (QEMU)](http://qemu.org?target=_blank) device in [Deploy to virtual devices](../Deploy-to-virtual-devices).
Doing the first deployment using QEMU is handy becasue it means that you do not have to configure any hardware to test Mender.
If you have real hardware in the form of the popular Mender reference board, the [BeagleBone Black](https://beagleboard.org/black?target=_blank),
you can follow the final tutorial in this series, [Deploy to physical devices](../Deploy-to-physical-devices).

On the other hand, if you are only interested in triggering deployments with the Mender client manually at the device,
you can follow the [Standalone deployments](../Standalone-deployments) tutorial. For an explanation of the
difference between *managed* and *standalone* deployments, please see
[Modes of operation](../../Architecture/overview#modes-of-operation).


### Using these docs

The simplest way to navigate the documentation is to use the Next and Previous arrows (**<**   **>**) on each page. You can see which pages you've finished reading by the checkmarks (✓) that mark your progress in the sidebar.
