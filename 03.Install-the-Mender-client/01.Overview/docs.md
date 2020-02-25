---
title: Overview
taxonomy:
    category: docs
    label: guide
---

# Migration notes
~~~~~~~~~~~~~~~~~~~~
* NOTE: Application updates/Update Modules (not for system updates)
~~~~~~~~~~~~~~~~~~~~

The main purpose of the Mender updater client is to install software updates to
the device it is running on. However, it also includes functionality to work
with a Mender server, such as authenticate, report inventory and the outcome of
deployments. The Mender client runs in user space on top of an embedded Linux
operating system. It can be run in standalone or managed mode, as described in
[Modes of operation](../../architecture/overview#modes-of-operation). For a more
general overview of where the Mender client fits in as part of the deployment
process, please see the [Architecture overview](../../architecture/overview).

In order to enable the client to work in as many environments as possible, it is
built to be generic and extensible, while providing default setup and
configuration that should work with most environments. Especially when running
the client in managed mode, i.e. connected to a Mender server, there are a
number of settings and extension points that can be utilized.

