---
title: Device Support
taxonomy:
    category: docs
---

## Installation types

The Mender-update client runs on the device in order to install software updates.
Therefore, at minimum you need to install the client binary on the device
and it must support the device OS and hardware architecture. This allows
you to deploy application updates by using Update Modules.

In addition, you need a deeper integration for supporting robust
A/B *Operating System updates* because Mender needs to control which system
partition (A or B) is updated and booted. The mechanisms used for this are
specific to the distribution or build system you are using to maintain
your OS. This is called a Mender *board integration*.
Note that a board integration also covers installing the Mender-update client on
the device, so you do not need to install the Mender-update client after using a
board integration.

See [Update types](../../02.Overview/01.Introduction/docs.md#update-types) for more information
on Application and Operating System updates.

For production environments a *board integration is strongly recommended*
because Operating System updates are usually needed over time and it
is very difficult to retrofit this type of integration after devices have been
deployed to the field.


In general Mender officially supports the most common Linux OSes, and has
reference implementations for specific devices. Note that both your OS and
device hardware combination needs to be supported for Mender to work.

!!! We offer [Consulting services](https://mender.io/support-and-services/board-integration?target=_blank) if you would like to save time and ensure verified integration of a specific OS and device.

!!! If you decide to create an integration for your OS and device, please consider to post it back to the [Board integrations category of the Mender Hub community](https://hub.mender.io/c/board-integrations?target=_blank). This way, the community will benefit and help maintain your integration.


## Operating systems


### Debian family

Debian family OSes, such as Debian, Ubuntu and Raspberry Pi OS are officially supported.


#### Board integrations

A board integration for Raspberry Pi OS is available in [the downloads section](../../10.Downloads/docs.md).

To find board integrations for other Debian family OSes,
go to the [Debian family in the Mender Hub community](https://hub.mender.io/c/board-integrations/debian-family?target=_blank).

If no board integration is available for your device, follow the documentation on
[Operating System updates: Debian family](../../04.Operating-System-updates-Debian-family) to integrate your device.


#### Installation with .deb packages

If you only need to deploy application updates (not Operating System updates),
we provide Debian packages (`.deb`) for installing the Mender-update client that works
on almost any Debian family OS and device.

Follow the documentation on [install Mender using the Debian package](../../03.Client-installation/02.Install-with-Debian-package/docs.md)
in this case.


### Yocto Project

Due to the nature of the Yocto Project of building a full Linux OS image instead of
installing packages while the device is running,
board integration is the only supported method for Yocto Project distributions.

Integrations for the Yocto Project are available in
[Yocto Project in the Mender Hub community](https://hub.mender.io/c/board-integrations/yocto-project?target=_blank).

If no board integration is available for your device, follow the documentation on
[Operating System updates: Yocto Project](../../05.Operating-System-updates-Yocto-Project/chapter.md) to integrate your
device with the `meta-mender` layer.


### Other Linux OSes

#### Board integrations

Board integrations are also available for devices running other types of Linux OSes
such as Buildroot and OpenWRT. See existing integrations for OSes in the
[Mender Hub community](https://hub.mender.io/c/board-integrations?target=_blank).

If you can not find a board integration for the OS you are looking for,
take a look at the [Mender from scratch](https://hub.mender.io/t/mender-from-scratch?target=_blank)
community post for steps to create one.


#### General Linux installation

<!--AUTOVERSION: "mender/tree/%?target=_blank"/mender -->
You can compile the Mender clients for a wide variety of architectures. Follow the steps in the
[README.md](https://github.com/mendersoftware/mender/tree/master?target=_blank#installing-from-source)
of the Mender source repository. This is also the first step to a board integration for other types of Linux OSes.


### Other non-Linux OSes

<!--AUTOVERSION: "mender/tree/%?target=_blank"/mender -->
For a POSIX compliant OS it may be possible to compile the Mender clients to run natively,
as outlined in the
[README.md](https://github.com/mendersoftware/mender/tree/master?target=_blank#installing-from-source).

For other types of OSes you can either use a nearby Linux system to update it via a
[proxy deployment](../../02.Overview/01.Introduction/docs.md#proxy-deployments) or
[create a custom Mender client](https://hub.mender.io/t/how-to-write-a-custom-client-interfacing-a-mender-server).


## Board integration overview

You can customize a an existing board integration or create your own
to meet your exact needs. A board integration generally consists of the following.


### Bootloader changes

To use [robust system
updates](../../02.Overview/01.Introduction/docs.md#robust-operating-system-updates) with
Mender, update your bootloader with logic to select the appropriate partition at
boot time. Additionally, install utilities that can update the bootloader
environment into the root filesystem.


### Mender-update client application installation

The Mender-update client application is a standard Linux executable installed into the
root filesystem. If your design uses [managed
mode](../../02.Overview/01.Introduction/docs.md#client-modes-of-operation), you
also need to ensure that the Mender-update client is running as a system service.


### Mender-update client configuration files

Install the [Mender configuration
files](../../03.Client-installation/07.Configuration-file/docs.md) into your
root filesystem. These are standard text files containing JSON code that defines
parameters for the Mender-update client, such as polling intervals.


### Installation of Update Modules

If you require support for payload types other than Operating System
updates, ensure to install appropriate [Update
Modules](../../06.Artifact-creation/08.Create-a-custom-Update-Module/docs.md)
into your root filesystem, which are invoked by the Mender-update client.


### Installation of root filesystem State Scripts

If you require support of [root filesystem State
Scripts](../../06.Artifact-creation/04.State-scripts/docs.md#root-filesystem-and-artifact-scripts),
ensure that they are installed into your root filesystem, so they are invoked by the
Mender-update client.
