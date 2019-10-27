---
title: Requirements
taxonomy:
    category: docs
---

For quickly testing the Mender server, we have created a demo version that
does not take into account production-grade issues like security and scalability.
When you are ready to install for production, please follow
the [Production installation documentation](../../administration/production-installation).

The Mender server is using the microservices design pattern, meaning that
multiple small, isolated services make up the server. 
In order to make it easy to test Mender as a whole, we have created a
Docker Compose environment that brings all of these components up
and connects them together on a single machine.
During the onboarding process a virtual device can be started for you to test with,
which is handy because it means that you can test Mender without
having to configure any hardware.


#### OS and web browser

We assume you are using **Ubuntu 18.04** with **Google Chrome** as web browser
and at least **10 GB free disk space** and **2 GB RAM available** for Mender.

#### Docker Engine 17.03

Follow the [documentation to install Docker Engine](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/?target=_blank), version **17.03 or later**.

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

If you need support for application updates (but not full system updates), no device integration is required. In this case you can install Mender on an existing device and OS by following the documentation on [installing the Mender client](../../client-configuration/installing). For first-time Mender users, the Mender server onboarding will guide you through this process. All you need is an ARM-based device with a Debian-family OS (e.g. Debian, Raspbian, Ubuntu) pre-installed and network connectivity set up.

On the other hand, to get support for robust system updates with rollback, Mender must be [integrated with production devices](../../devices).

## Trying Mender

After installing the above prerequisites, follow the steps in [Install a Mender demo server](../create-a-test-environment).
