---
title: Downloads
taxonomy:
    category: docs
markdown:
    extra: true
process:
    twig: true
---

## Disk images

These disk images (`*.img` or `*.sdimg`) are based on images provided by board
manufacturers and already have Mender fully integrated. They are used to
provision the device storage for devices without Mender running already.

Mender provides images based on the following distributions:

* Images for **Raspberry Pi 3** and **Raspberry Pi 4**, which are based on the
  [Raspberry Pi OS Linux
  distribution](https://www.raspberrypi.org/downloads/raspberry-pi-os/?target=_blank)

!! Note that we do not offer commercial support for these images. They are based
!! on images supported by board manufacturers, like the Raspberry Pi Foundation,
!! and provide the same software and configuration options as the original
!! images. Please use the support resources available from the board
!! manufacturer, or [contact us](mailto:contact@mender.io) if you have any
!! questions on the Mender integration.

| Board                         | OS                              | Disk image                                                                                         | Storage size |
|-------------------------------|---------------------------------|----------------------------------------------------------------------------------------------------|--------------|
| Raspberry Pi 3 Model B and B+ | Raspberry Pi OS Buster Lite 2020-05-27 | [raspios-buster-lite-raspberrypi3-mender.img.xz][raspios-buster-lite-raspberrypi3-mender.img.xz] | 8 GB         |
| Raspberry Pi 4 Model B        | Raspberry Pi OS Buster Lite 2020-05-27 | [raspios-buster-lite-raspberrypi4-mender.img.xz][raspios-buster-lite-raspberrypi4-mender.img.xz] | 8 GB         |

<!--AUTOVERSION: "mender-%.img.xz"/mender-convert-client -->
[raspios-buster-lite-raspberrypi3-mender.img.xz]: https://d4o6e0uccgv40.cloudfront.net/2020-05-27-raspios-buster-lite-armhf/arm/2020-05-27-raspios-buster-lite-armhf-raspberrypi3-mender-2.5.0.img.xz
[raspios-buster-lite-raspberrypi4-mender.img.xz]: https://d4o6e0uccgv40.cloudfront.net/2020-05-27-raspios-buster-lite-armhf/arm/2020-05-27-raspios-buster-lite-armhf-raspberrypi4-mender-2.5.0.img.xz

You can find images for other devices in our Mender Hub community forum, see
[Debian Family](https://hub.mender.io/c/board-integrations/debian-family/11?target=_blank) or
[Yocto Project](https://hub.mender.io/c/board-integrations/yocto-project/10?target=_blank)
integration posts.


## mender-artifact

The `mender-artifact` utility is used to work with Mender Artifacts,
which are files with the `.mender` suffix and contain software to be deployed.
See [Artifact creation](../06.Artifact-creation/chapter.md) for more information on how to
use this utility.

Follow the correct link according to your host platform to download
`mender-artifact` as a standalone utility:

<!--AUTOVERSION: "mender-artifact %"/mender-artifact -->
| Platform | Download link                                                |
|----------|--------------------------------------------------------------|
| Linux    | [mender-artifact 3.5.0][x.x.x_mender-artifact-linux]     |
| Mac OS X | [mender-artifact 3.5.0][x.x.x_mender-artifact-darwin] |

Remember to add execute permission and ensure that the mender-artifact utility is in a directory that is specified in your [PATH environment variable](https://en.wikipedia.org/wiki/PATH_(variable)?target=_blank). Most systems automatically have `/usr/local/bin` in your PATH so the following should allow proper execution and location of this binary.

```bash
sudo chmod +x mender-artifact
sudo cp mender-artifact /usr/local/bin/
```

Please refer to your host Operating System documentation for more details.


<!--AUTOVERSION: "mender-artifact/%/"/mender-artifact -->
[x.x.x_mender-artifact-linux]: https://downloads.mender.io/mender-artifact/3.5.0/linux/mender-artifact
<!--AUTOVERSION: "mender-artifact/%/"/mender-artifact -->
[x.x.x_mender-artifact-darwin]: https://downloads.mender.io/mender-artifact/3.5.0/darwin/mender-artifact

! If you are using Mac OS X, note that using `mender-artifact` with
! disk image files (e.g.: `*.sdimg`, `*.img`, or others holding the storage
! partitions) has limited functionality. Commands like
! `mender-artifact cat` or `mender-artifact cp` will not work due to lack
! of support for certain utilities on the Mac platform.


## Mender client

The Mender client runs on the device, checks for and installs
software updates packaged as Mender Artifacts.
See [Client installation](../03.Client-installation/chapter.md) for more information
about how to configure and use the Mender client.

### Installation methods

You can install the Mender client in different ways depending on your preference.

* Express installation using the [convenience
  script](#express-installation) from [https://get.mender.io](https://get.mender.io).
* Set up Mender's APT repository and install using the [package
  manager](#install-using-the-apt-repository).
* Download the Debian package and [install it manually](#install-from-package).

#### Express installation

Mender provides a convenience script available at [get.mender.io
](https://get.mender.io) that non-interactively installs the Mender client
[using the package manager](#install-using-the-apt-repository). Users installing
the Mender client this way, should be aware that:

* The script requires `root` privileges to run. Therefore, carefully examine the
  script before executing it.
* The script will install several dependencies with the package manager without
  asking for confirmation.
* The Mender GPG public key and APT repository will be added to your trusted APT
  keychain and sources list respectively without asking for confirmation.

!! Always examine scripts downloaded over the Internet before running them
!! locally.

```bash
curl -fLsS https://get.mender.io -o get-mender.sh
# INSPECT get-mender.sh BEFORE PROCEEDING
sudo sh get-mender.sh
```

By default, the script installs the [remote terminal
extension](#remote-terminal-add-on) plugin in addition to the client. If you do
not want this feature you can provide additional arguments to the script
specifying which packages you want to install. For example, the following will
only install the Mender client:
```bash
curl -fLsS https://get.mender.io -o get-mender.sh
# INSPECT get-mender.sh BEFORE PROCEEDING
sudo sh get-mender.sh mender-client
```

!!! Mender offers an `experimental` version of the package repository. To use
!!! the latest experimental version of Mender, run the script with an additional
!!! flag `-c experimental`. Do not use the `experimental` repository for
!!! production devices as these releases are not fully tested.

##### Upgrading Mender after the express installation

After installing the Mender client with [get.mender.io](https://get.mender.io),
the `mender-client` package is maintained by the package manager. To upgrade the
Mender client, simply run
```bash
sudo apt-get update
sudo apt-get upgrade
```

#### Install using the APT repository

Before installing the Mender client, you need to set up the Mender APT
repository. Afterwards, you can install and update the Mender client using the
`apt` command line interface.

##### Set up the APT repository
1. Update the `apt` package index and install required dependencies.
   ```bash
   sudo apt-get update
   sudo apt-get install \
   		apt-transport-https \
   		ca-certificates \
   		curl \
   		gnupg-agent \
   		software-properties-common
   ```
2. Add the official Mender GPG key to your trusted `apt` keychain:
   ```bash
   curl -fLsS https://downloads.mender.io/repos/debian/gpg | sudo apt-key add -
   ```

   Inspect the GPG key fingerprint and verify that it matches
   `E6C8 5734 5575 F921 8396  5662 2407 2B80 A1B2 9B00`.
   ```bash
   sudo apt-key fingerprint A1B29B00
   ```
   ```
pub   rsa3072 2020-11-13 [SC] [expires: 2022-11-13]
          E6C8 5734 5575 F921 8396  5662 2407 2B80 A1B2 9B00
uid           [ unknown] Mender Team <mender@northern.tech>
sub   rsa3072 2020-11-13 [E] [expires: 2022-11-13]
   ```
3. Add the Mender repository to your sources list by selecting the architecture
   matching your device.
   [ui-tabs position="top-left" active="0" theme="lite" ]
   [ui-tab title="armhf"]
   ```bash
   sudo add-apt-repository \
           "deb [arch=armhf] https://downloads.mender.io/repos/debian \
           stable \
           main"
   ```
   [/ui-tab]
   [ui-tab title="arm64"]
   ```bash
   sudo add-apt-repository \
           "deb [arch=arm64] https://downloads.mender.io/repos/debian \
           stable \
           main"
   ```
   [/ui-tab]
   [ui-tab title="amd64"]
   ```bash
   sudo add-apt-repository \
           "deb [arch=amd64] https://downloads.mender.io/repos/debian \
           stable \
           main"
   ```
   [/ui-tab]
   [/ui-tabs]
   !!! If you want the bleeding edge version of mender, you can use our
   !!! `experimental` repository by replacing `stable` with `experimental` in
   !!! the above command. Do not use the `experimental` repository in production
   !!! as these releases are not fully tested.

4. Update the package index and install the Mender client:
   ```bash
   sudo apt-get update
   sudo apt-get install mender-client
   ```

#### Install from package

We also provide the Debian package (`.deb`) for users wanting to install the
Mender client manually outside the package manager. This can be useful for
airtight systems with limited access to the Internet, or when running
Mender in [standalone
mode](../02.Overview/01.Introduction/docs.md#client-modes-of-operation).

<!--AUTOVERSION: "mender-client_%-1"/mender -->
| Architecture   | Devices                                   | Download link                                                       |
|----------------|-------------------------------------------|---------------------------------------------------------------------|
| armhf (ARM-v6) | ARM 32bit distributions, for example Raspberry Pi OS for Raspberry Pi or Debian for BeagleBone | [mender-client_2.5.0-1_armhf.deb][mender-client_x.x.x-1_armhf.deb] |
| arm64 | ARM 64bit processors, for example Debian for Asus Tinker Board | [mender-client_2.5.0-1_arm64.deb][mender-client_x.x.x-1_arm64.deb] |
| amd64 | Generic 64-bit x86 processors, the most popular among workstations | [mender-client_2.5.0-1_amd64.deb][mender-client_x.x.x-1_amd64.deb] |

<!--AUTOVERSION: "downloads.mender.io/%/"/mender "mender-client_%-1_armhf.deb"/mender -->
[mender-client_x.x.x-1_armhf.deb]: https://downloads.mender.io/2.5.0/dist-packages/debian/armhf/mender-client_2.5.0-1_armhf.deb
<!--AUTOVERSION: "downloads.mender.io/%/"/mender "mender-client_%-1_arm64.deb"/mender -->
[mender-client_x.x.x-1_arm64.deb]: https://downloads.mender.io/2.5.0/dist-packages/debian/arm64/mender-client_2.5.0-1_arm64.deb
<!--AUTOVERSION: "downloads.mender.io/%/"/mender "mender-client_%-1_amd64.deb"/mender -->
[mender-client_x.x.x-1_amd64.deb]: https://downloads.mender.io/2.5.0/dist-packages/debian/amd64/mender-client_2.5.0-1_amd64.deb


## Remote Terminal add-on

Mender offers a remote terminal extension (`mender-connect`) to the Mender client
that enables accessing the device terminal using the Mender UI. See the
[configuration page for remote
terminal](../09.Add-ons/01.Remote-Terminal/30.Mender-connect-configuration-file/docs.md) for
more information.

### Install the remote terminal client

The remote terminal add-on requires the [Mender client](#mender-client) in order
to function. If you have already installed the Mender client using
the [express installation](#express-installation) script, you will already have
`mender-connect` installed by default.

The add-on is only available from the Mender APT repository.
To install `mender-connect`, follow the instructions for [installing
`mender-client` using the APT repository](#install-using-the-apt-repository).
After the final step, install `mender-connect` using the package manager:

```bash
sudo apt-get install mender-connect
```

## mender-cli

The `mender-cli` utility enables an easy interface to key use cases
of the Mender server API, such as uploading a Mender Artifact, from
the command line. See [Server integration](../08.Server-integration/chapter.md) for
more information.

Follow the correct link according to your host platform to download `mender-cli`:

<!--AUTOVERSION: "mender-cli %"/mender-cli -->
| Platform | Download link                                                |
|----------|--------------------------------------------------------------|
| Linux    | [mender-cli 1.6.0][x.x.x_mender-cli-linux]                  |
| Mac OS X | [mender-cli 1.6.0][x.x.x_mender-cli-darwin]                 |


Remember to add execute permission and ensure that the mender-cli utility is in a directory that is specified in your [PATH environment variable](https://en.wikipedia.org/wiki/PATH_(variable)?target=_blank). Most systems automatically have `/usr/local/bin` in your PATH so the following should allow proper execution and location of this binary.

```bash
sudo chmod +x mender-cli
sudo cp mender-cli /usr/local/bin/
```

Please refer to your host Operating System documentation for more details.

<!--AUTOVERSION: "mender-cli/%/"/mender-cli -->
[x.x.x_mender-cli-linux]: https://downloads.mender.io/mender-cli/1.6.0/linux/mender-cli
<!--AUTOVERSION: "mender-cli/%/"/mender-cli -->
[x.x.x_mender-cli-darwin]: https://downloads.mender.io/mender-cli/1.6.0/darwin/mender-cli
