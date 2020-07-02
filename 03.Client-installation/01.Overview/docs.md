---
title: Overview
taxonomy:
    category: docs
---

The Mender client is a user space Linux executable with one main purpose: to install
software updates to the device it is running on. It can operate in [managed](../../02.Overview/01.Introduction/docs.md#client-modes-of-operation)
or [standalone mode](../../02.Overview/01.Introduction/docs.md#client-modes-of-operation)
and perform two types of updates: [full filesystem](link-to-full-update) when
you update the complete filesystem with an image, and [application update](link-to-update-modules)
when you for instance change one file, or install some packages. We designed it to work with
the Mender server, to as authenticate, report inventory and store the outcome
of deployments.

For a more general overview of where the Mender client fits in as part
of the deployment process, please see the [Architecture overview](../../02.Overview/01.Introduction/docs.md).

In order to enable the client to work in as many environments as possible,
we designed it to be generic and extensible, while providing default setup
and configuration that should work with most environments. Especially
when running the client in managed mode, i.e. connected to a Mender server,
there are a number of settings and extension points that can be utilized.
