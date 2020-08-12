---
title: Overview
taxonomy:
    category: docs
---

The Mender client is a user space Linux executable with one main purpose: to install
software updates to the device it is running on.It can operate in [managed
or standalone mode](../../02.Overview/01.Introduction/docs.md#client-modes-of-operation).

At a high level, two types of updates are supported: [full filesystem](../../02.Overview/01.Introduction/docs.md#Robust-system-updates) when
you update the complete filesystem, and [application updates](../../02.Overview/01.Introduction/docs.md#Application-updates) where, for example, you change one file, install some packages, or execute arbitrary commands. In most instances, the full filesystem update will use a redundant root filesystem partition and the application updates will update components in the active root filesystem.

Note that in order to support *system updates*, a *board integration* is required which includes more than simply installing Mender on top of a running operating system. If you want support for system updates, either use OS images provided in [Get started](../../01.Get-started) or follow the chapters on System updates for [Debian family](../../04.System-updates-Debian-family/chapter.md) or [Yocto Project](../../05.System-updates-Yocto-Project/chapter.md).

If you are interested in *application updates* only, you can easily install Mender on top of an existing Linux OS as described in the [Debian package](../02.Install-with-Debian-package/docs.md) chapter.

For a more general overview of where the Mender client fits in as part
of the deployment process, please see the [Architecture overview](../../02.Overview/01.Introduction/docs.md).

In order to enable the client to work in as many environments as possible,
we designed it to be generic and extensible while providing a default setup
and configuration that should work for most environments. When running managed mode, i.e. connected to a Mender server, there are a number of settings and extension points that you may need to modify for your particular setup.


