---
title: Device Integration
taxonomy:
    category: docs
---

The Mender client is a user space Linux executable with one main
purpose: to install software updates to the device it is running on.
Broadly speaking, there are two types of updates: full filesystem when
you update the complete filesystem, and application updates where, for
example, you change one file, install some packages, or execute
arbitrary commands.  Device integration is the set of steps needed to
ensure Mender is running on your system, with appropriate
configuration for your update
type.

In most instances, the full filesystem update will use a redundant
root filesystem partition and the application updates will update
components in the active root filesystem.

If Mender is to be used only for application updates, then it
can be installed like any other application using your system package
management utilities. You can find more details about this in the section
on [Install with Debian package](../../03.Client-installation/02.Install-with-Debian-package/docs.md)

To support full file system updates, a more thorough integration is
required which includes install Mender on top of a running operating
system as well as modifying the boot commands and providing extra
partitions. The mechanisms used for this are specific to the
distribution or build system you are using to maintain your image.  We
provide detailed instructions for full system integration with the
[Yocto Project](../../05.System-updates-Yocto-Project/chapter.md) and
with [Debian-based distributions](../../04.System-updates-Debian-family/chapter.md).

For a more general overview of where the Mender client fits in as part of the deployment process, please see the Architecture overview.

At its basics, the definition of Device integration includes

* Bootloader changes
* Mender client application installation
* Mender client configuration files
* Installation of Update Modules
* Installation of root filesystem State Scripts.

## Bootloader changes

To use [robust system updates](../../02.Overview/01.Introduction/docs.md#robust-system-updates) with Mender, your bootloader needs to be updated with logic to select the appropriate partition at boot time.  Additionally, utilities that can update the bootloader environment need to be installed into the root filesystem.

## Mender client application installation

The Mender client application is a standard Linux executable that is installed into the root filesystem. If your design uses [managed mode](../../02.Overview/01.Introduction/docs.md#client-modes-of-operation), you also need to ensure that the Mender client is running as a system servce.

## Mender client configuration files

The [Mender configuration files](../../03.Client-installation/06.Configuration-file/docs.md) need to be installed into your root filesystem. These are standard text files containing JSON code that defines parameters for the Mender client, such as polling intervals.

## Installation of Update Modules

If you require support of payload types other than the full root filesystem updates, you will need to ensure that appropriate [Update Modules](../../06.Artifact-creation/08.Create-a-custom-Update-Module/docs.md) are installed into your root filesystem, to be invoked by the Mender client.

## Installation of root filesystem State Scripts

If you require support of [root filesystem State Scripts](../../06.Artifact-creation/04.State-scripts/docs.md#root-file-system-and-Artifact-scripts), you need to ensure that they are installed into your root filesystem, to be invoked by the Mender client.
