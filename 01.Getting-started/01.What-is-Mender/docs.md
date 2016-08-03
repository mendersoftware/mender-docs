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

We have two tutorials that show you how Mender works. Each demonstrates how to use Mender to update the root filesystem of a target device.
The first uses [QEMU to create an emulated device](../../Getting-started/Your-first-update-on-qemu), which is handy becasue it means that you do not have to configure any hardware.
The second tutorial uses real hardware in the form of the popular [BeagleBone Black development board](../../Getting-started/Your-first-update-on-BeagleBone).

### Using these docs

The simplest way to navigate the documentation is to use the Next and Previous arrows (**<**   **>**) on each page. You can see which pages you've finished reading by the checkmarks (✓) that mark your progress in the sidebar.
