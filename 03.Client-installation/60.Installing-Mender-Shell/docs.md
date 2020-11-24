---
title: Installing Remote Terminal Extention
taxonomy:
    category: docs
---

This page describes how to install the Remote Terminal extension to the Mender
client on an existing Linux system. Installing the Remote Terminal requires first
[installing the Mender client](../10.Install-with-Debian-package/docs.md)
on the target system in order to function.

## Install Remote Terminal using the Debian package

Mender provides a Debian package (`.deb`) for installing the Remote Terminal add-on
for Debian based systems such as Debian, Ubuntu and Raspberry Pi OS. The package
supports the following architectures:

- armhf (ARM-v6): ARM 32bit distributions, for example Raspberry Pi OS for Raspberry Pi or Debian for BeagleBone.
- arm64 (ARM-v8): ARM 64bit processors, for example Debian for Asus Tinker Board
- amd64: Generic 64-bit x86 processors, the most popular among workstations

See the [downloads page](../../09.Downloads/docs.md#Remote-terminal) for links
to downloading the packages.

### Download the package

The following instructions will assume *armhf* architecture, make sure to replace
the URLs with the one for your architecture, which you will find in [the downloads
page](../../09.Downloads/docs.md#Remote-terminal).

<!--AUTOVERSION: "downloads.mender.io/%/"/mender-shell "mender-shell_%-1_armhf.deb"/mender-shell -->
```bash
wget https://downloads.mender.io/master/dist-packages/debian/armhf/mender-shell_master-1_armhf.deb
```

### Install the package

Install the package with the `dpkg` tool shipped with Debian systems.

<!--AUTOVERSION: "mender-shell_%-1_armhf.deb"/mender-shell -->
```bash
sudo dpkg -i mender-shell_master-1_armhf.deb
```

After completing the installation, the Remote Terminal will run a default 
configuration targeting the Hosted Mender service. Read the [configuration
page](../70.Mender-shell-configuration-file/docs.md) for a complete list of
configuration options.

!!! If you are hosting your own Mender server on premises you must reconfigure
!!! the [connection settings](../70.Mender-shell-configuration-file/docs.md)
!!! to target your new server.

## Install from source

<!--AUTOVERSION: "mender-shell/tree/%#building-from-source/mender-shell-->
As an alternative to using the Debian package, it is possible to install the
Remote Terminal add-on from source by following the instructions outlined
in the [README.md
](https://github.com/mendersoftware/mender-shell/tree/master#building-from-source)
in the [mender-shell](https://github.com/mendersoftware/mender-shell/tree/master)
source repository.
