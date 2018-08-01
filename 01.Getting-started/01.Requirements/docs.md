---
title: Requirements
taxonomy:
    category: docs
---

Mender is an open source remote software updater for embedded Linux devices.
It enables management of software updates to connected devices remotely over any TCP/IP network.
For a high-level introduction to Mender and its architecture, we recommend reading the [What is Mender page on Mender.io](https://mender.io/what-is-mender?target=_blank).

This section of the documentation contains tutorials to help you deploy your first update with Mender.

!!! Going from a fresh system to completing your first deployment with Mender, including server setup, should take **less than 1 hour**!

! Do not follow this getting started documentation if you are using [Hosted Mender](https://hosted.mender.io?target=_blank). Instead, follow the instructions you received in the welcome email when you signed up to Hosted Mender.


## Demo server requirements

For quickly testing the Mender server, we have created a demo version that
does not take into account production-grade issues like security and scalability.
When you are ready to install for production, please follow
the [Production installation documentation](../../administration/production-installation).

The Mender server is using the microservices design pattern, meaning that
multiple small, isolated services make up the server. 
In order to make it easy to test Mender as a whole, we have created a
Docker Compose environment that brings all of these components up
and connects them together on a single machine.
It also includes a virtual device for you to test with,
which is handy because it means that you can test Mender without
having to configure any hardware.


#### OS and web browser

We assume you are using **Ubuntu 18.04** with **Google Chrome** as web browser
and at least **10 GB free disk space** and **2 GB RAM available** for Mender.

!!! If you want to set up Mender on **Windows**, please [see this note](http://bit.ly/2M3B5IJ).

#### Docker Engine 1.11

Follow the [documentation to install Docker Engine](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/?target=_blank),
version **1.11 or later** (17.03 or later in [Docker's new versioning scheme](https://blog.docker.com/2017/03/docker-enterprise-edition/?target=_blank)).

##### Docker permissions

Invoking the docker commands may fail when the local user has insufficient permissions to connect to the docker daemon. In Ubuntu 18.04, the user must be a member of the `docker` group to be able to access it. Please check the documentation for your host OS if you encounter connection issues with docker.

#### Docker Compose 1.6

Follow the [documentation to install Docker Compose](https://docs.docker.com/compose/install/?target=_blank),
version **1.6 or later**.

#### Fast Internet connection

While bringing up the environment, several gigabytes of docker
images may be downloaded. We recommend using a fast Internet
connection in order to avoid long wait times.

!!! It is very likely possible to use the test environment on other platforms, versions, or with less resources. We recommend using this exact environment for testing Mender because it is known to work and you will thus avoid any issues specific to your test environment if you use this reference.


## Device requirements
The Mender updater client is designed to run on embedded Linux devices and connects to the server
so that deployments can be managed across many devices.
In order to support robust updates with rollback, Mender must be [integrated with production devices](../../devices).

However, during the testing and validation stage, it is common to use development device to shorten time to experiment and prototype.
For demo and testing purposes, we provide pre-built demo images for the [Raspberry Pi 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b?target=_blank) and [BeagleBone Black](https://beagleboard.org/black?target=_blank) devices with the latest version of Mender.


## Trying Mender

After installing the above prerequisites, follow the steps in [Install a Mender demo server](../create-a-test-environment).
