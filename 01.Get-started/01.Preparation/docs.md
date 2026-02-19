---
title: Preparation
taxonomy:
    category: docs
    label: tutorial
---

Quickly and easily deploy your first over-the-air (OTA) software update with
Mender using a secure server we host for you. We will walk you through
installing Mender on a device and deploying:

* a simple *Application* update
* an *Operating System* update.

To get started testing Mender, create a hosted Mender account by
[signing up here](https://mender.io/signup?target=_blank).

!!! We provide a 12 month free evaluation period of the Mender Enterprise plan
!!! for up to 5 devices (all device tiers). No credit card is required to signup.

## Understanding device tiers

Mender supports different types of devices through a concept called [device tiers](../../02.Overview/17.Device-tiers/docs.md).
During this getting started guide, you'll be working with **standard tier** devices (default).
Device tiers affect polling intervals, artifact size limits, and available features.
The free trial includes 5 devices for all tiers.

## Next step

With a hosted Mender account in place, it is time to prepare a device to
connect to hosted Mender.

You can connect almost any device and Linux OS with Mender, but to make things simple 
during evaluation we recommend you use a Raspberry Pi as a test device.
You can learn how to integrate other devices and OSes later.


* [To prepare a Raspberry Pi device](01.Prepare-a-Raspberry-Pi-device/docs.md) (**recommended**)

  Due to the popularity of Raspberry Pi devices our reference environment is
  optimized for evaluation on this specific device using Raspberry Pi OS
  (previously called Raspbian) as operating system. This environment should
  already be familiar to most people.

* [To prepare a virtual device](02.Prepare-a-virtual-device/docs.md)

  If you do not have a Raspberry Pi available, you can use a virtual device to
  evaluate key Mender use cases.

  This tutorial provides the steps for preparing your workstation to be able to run
  a virtual ([QEMU process emulator](https://www.qemu.org/?target=_blank)) device with Mender
  integrated.


### Connecting other devices

For other device types and OSes, we provide documentation to integrate with Mender.

* Learn how to integrate devices with [Debian family](../../04.Operating-System-updates-Debian-family) or 
  [Yocto OSes](../../05.Operating-System-updates-Yocto-Project)
* Visit [Mender Hub Board Integrations](https://hub.mender.io/c/board-integrations?target=_blank) for community discussions on different board integrations
* Visit [Mender Hub - Community Board Integrations Index](https://hub.mender.io/t/board-support-index/5742/5)for a list of community contributed boards and their status

!!! We recommend running through the Get Started guide with a Raspberry Pi or virtual device to 
!!! learn the basics before diving into other board integrations.

## Have any questions?

If you need help or have any questions:

* Visit our community forum at [Mender Hub](https://hub.mender.io?target=_blank),
dedicated to OTA updates where you can discuss any issues you may be having.
Share and learn from other Mender users.

* Learn more about Mender by reading the rest of the documentation, for example
the [Overview](../../02.Overview/01.Introduction/docs.md),
[Troubleshoot](../../301.Troubleshoot/) or
[Mender FAQ](https://mender.io/product/faq?target=_blank) sections.
