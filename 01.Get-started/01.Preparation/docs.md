---
title: Preparation
taxonomy:
    category: docs
---

Quickly and easily deploy your first over-the-air (OTA) software update with
Mender using a secure server we host for you. We will walk you through
installing Mender on a device and deploying:

* a simple *application* update
* a full *system* update.
* a *Docker container* update

To get started testing Mender, create a hosted Mender account by
[signing up here](https://mender.io/signup?target=_blank).

!!! We provide three months free usage on the Mender Starter plan for you to use
!!! for evaluation. You can cancel at any time without incurring a cost.

## Next step

With an hosted Mender account in place, it is time to prepare a device to
connect to hosted Mender.

Chose one of the next options below, based on if you have a Raspberry Pi
available or not:

1. [Prepare a Raspberry Pi device](./01.Prepare-a-Raspberry-Pi-device/docs.md) (**recommended**)

  Due to the popularity of Raspberry Pi devices our reference environment is
  optimized for evaluation on this specific device using Raspbian as operating
  system. This environment should already be familiar to most people.

1. [Prepare a virtual device](./02.Prepare-a-virtual-device/docs.md)

  If you do not have a Raspberry Pi available, a virtual device is can be used
  to evaluate key Mender use cases.

  This guide provides the steps for preparing your workstation to be able to run
  a virtual ([QEMU process emulator](https://www.qemu.org/)) device with Mender
  integrated.

## Have any questions?

If you need help or have any questions:

* Visit our community forum at [Mender Hub](https://hub.mender.io?target=_blank),
dedicated to OTA updates where you can discuss any issues you may be having.
Share and learn from other Mender users.

* Learn more about Mender by reading the rest of the documentation, for example
the [Overview](../../02.Architecture/01.Overview/docs.md),
[Troubleshooting](../../201.Troubleshooting/) or
[Mender FAQ](https://mender.io/plans/faq?target=_blank) sections.
