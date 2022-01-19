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
manufacturers and are ready to install the Mender client. They are used to
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
| Raspberry Pi 3 Model B and B+ | Raspberry Pi OS Buster Lite 2021-01-11 | [raspios-buster-lite-raspberrypi3-mender.img.xz][raspios-buster-lite-raspberrypi3-mender.img.xz] | 8 GB         |
| Raspberry Pi 4 Model B        | Raspberry Pi OS Buster Lite 2021-01-11 | [raspios-buster-lite-raspberrypi4-mender.img.xz][raspios-buster-lite-raspberrypi4-mender.img.xz] | 8 GB         |

<!--AUTOVERSION: "mender-convert-%.img.xz"/mender-convert -->
[raspios-buster-lite-raspberrypi3-mender.img.xz]: https://d4o6e0uccgv40.cloudfront.net/2021-01-11-raspios-buster-armhf-lite/arm/2021-01-11-raspios-buster-armhf-lite-raspberrypi3-mender-convert-master.img.xz
[raspios-buster-lite-raspberrypi4-mender.img.xz]: https://d4o6e0uccgv40.cloudfront.net/2021-01-11-raspios-buster-armhf-lite/arm/2021-01-11-raspios-buster-armhf-lite-raspberrypi4-mender-convert-master.img.xz

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

<!--AUTOVERSION: "mender-artifact %][x.x.x_mender-artifact-"/mender-artifact "mender-artifact %][%_mender-artifact-"/ignore-->
| Platform | Download link                                          |                                                                       |
|----------|--------------------------------------------------------|-----------------------------------------------------------------------|
| Linux    | [mender-artifact 3.7.0-build3][x.x.x_mender-artifact-linux]  | [mender-artifact master][master_mender-artifact-linux] (Pre-release)  |
| Mac OS X | [mender-artifact 3.7.0-build3][x.x.x_mender-artifact-darwin] | [mender-artifact master][master_mender-artifact-darwin] (Pre-release) |

Remember to add execute permission and ensure that the mender-artifact utility is in a directory that is specified in your [PATH environment variable](https://en.wikipedia.org/wiki/PATH_(variable)?target=_blank). Most systems automatically have `/usr/local/bin` in your PATH so the following should allow proper execution and location of this binary.

```bash
sudo chmod +x mender-artifact
sudo cp mender-artifact /usr/local/bin/
```

Please refer to your host Operating System documentation for more details.


<!--AUTOVERSION: "mender-artifact/%/"/mender-artifact -->
[x.x.x_mender-artifact-linux]: https://downloads.mender.io/mender-artifact/3.7.0-build3/linux/mender-artifact
[x.x.x_mender-artifact-darwin]: https://downloads.mender.io/mender-artifact/3.7.0-build3/darwin/mender-artifact
<!--AUTOVERSION: "[%_mender-artifact-"/ignore "mender-artifact/%/"/ignore -->
[master_mender-artifact-linux]: https://downloads.mender.io/mender-artifact/master/linux/mender-artifact
[master_mender-artifact-darwin]: https://downloads.mender.io/mender-artifact/master/darwin/mender-artifact

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
* The latest released Mender components will be installed.

!! Always examine scripts downloaded over the Internet before running them
!! locally.

```bash
curl -fLsS https://get.mender.io -o get-mender.sh
# INSPECT get-mender.sh BEFORE PROCEEDING
sudo bash get-mender.sh
```

By default, the script installs the [remote terminal
extension](#remote-terminal-add-on) plugin in addition to the client. If you do
not want this feature you can provide additional arguments to the script
specifying which packages you want to install. For example, the following will
only install the Mender client:
```bash
curl -fLsS https://get.mender.io -o get-mender.sh
# INSPECT get-mender.sh BEFORE PROCEEDING
sudo bash get-mender.sh mender-client
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

!!! To prevent the Mender client from upgrading when upgrading the rest of the
!!! system, mark it to be held with `sudo apt-mark hold mender-client`.


!!! Updating mender this way doesn't provide a rollback mechanism in case of issues.
!!! For production devices always update mender as part of the full system update with A/B partitions.

#### Install using the APT repository

Before installing the Mender client, you need to set up the Mender APT
repository. Afterwards, you can install and update the Mender client using the
`apt` command line interface.

##### Set up the APT repository

!!! With this method the latest released Mender components will be installed

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

   First in order to make sure that there are no mender sources in
   '/etc/apt/sources.list' lingering from a previous install, run

   ```bash
      sed -i.bak -e "\,https://downloads.mender.io/repos/debian,d" /etc/apt/sources.list
   ```

   Then add the sources:

   [ui-tabs position="top-left" active="0" theme="lite" ]
   [ui-tab title="armhf"]
   ```bash
    echo "deb [arch=armhf] https://downloads.mender.io/repos/debian stable main" \
    | sudo tee /etc/apt/sources.list.d/mender.list > /dev/null
   ```
   [/ui-tab]
   [ui-tab title="arm64"]
   ```bash
    echo "deb [arch=arm64] https://downloads.mender.io/repos/debian stable main" \
    | sudo tee /etc/apt/sources.list.d/mender.list > /dev/null
   ```
   [/ui-tab]
   [ui-tab title="amd64"]
   ```bash
    echo "deb [arch=amd64] https://downloads.mender.io/repos/debian stable main" \
    | sudo tee /etc/apt/sources.list.d/mender.list > /dev/null
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

!!! To prevent the Mender client from upgrading when upgrading the rest of the
!!! system, mark it to be held with `sudo apt-mark hold mender-client`.

#### Install from package

We also provide the Debian package (`.deb`) for users wanting to install the
Mender client manually outside the package manager. This can be useful for
airtight systems with limited access to the Internet, or when running
Mender in [standalone
mode](../02.Overview/01.Introduction/docs.md#client-modes-of-operation).

<!--AUTOVERSION: "mender-client_%-1"/mender -->
| Architecture   | Devices                                                                                        | Download link                                                       | Download link                                                                      |
|----------------|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|------------------------------------------------------------------------------------|
| armhf (ARM-v6) | ARM 32bit distributions, for example Raspberry Pi OS for Raspberry Pi or Debian for BeagleBone | [mender-client_mender-3.2.0-build3-1_armhf.deb][mender-client_x.x.x-1_armhf.deb] | [mender-client_mender-3.2.0-build3-1_armhf.deb][mender-client_mender-3.2.0-build3-1_armhf.deb] (Pre-release) |
| arm64          | ARM 64bit processors, for example Debian for Asus Tinker Board                                 | [mender-client_mender-3.2.0-build3-1_arm64.deb][mender-client_x.x.x-1_arm64.deb] | [mender-client_mender-3.2.0-build3-1_arm64.deb][mender-client_mender-3.2.0-build3-1_arm64.deb] (Pre-release) |
| amd64          | Generic 64-bit x86 processors, the most popular among workstations                             | [mender-client_mender-3.2.0-build3-1_amd64.deb][mender-client_x.x.x-1_amd64.deb] | [mender-client_mender-3.2.0-build3-1_amd64.deb][mender-client_mender-3.2.0-build3-1_amd64.deb] (Pre-release) |

<!--AUTOVERSION: "downloads.mender.io/%/"/mender "mender-client_%-1_"/mender -->
[mender-client_x.x.x-1_armhf.deb]: https://downloads.mender.io/mender-3.2.0-build3/dist-packages/debian/armhf/mender-client_mender-3.2.0-build3-1_armhf.deb
[mender-client_x.x.x-1_arm64.deb]: https://downloads.mender.io/mender-3.2.0-build3/dist-packages/debian/arm64/mender-client_mender-3.2.0-build3-1_arm64.deb
[mender-client_x.x.x-1_amd64.deb]: https://downloads.mender.io/mender-3.2.0-build3/dist-packages/debian/amd64/mender-client_mender-3.2.0-build3-1_amd64.deb
<!--AUTOVERSION: "downloads.mender.io/%/"/ignore "mender-client_%-1_"/ignore -->
[mender-client_master-1_armhf.deb]: https://downloads.mender.io/master/dist-packages/debian/armhf/mender-client_master-1_armhf.deb
[mender-client_master-1_arm64.deb]: https://downloads.mender.io/master/dist-packages/debian/arm64/mender-client_master-1_arm64.deb
[mender-client_master-1_amd64.deb]: https://downloads.mender.io/master/dist-packages/debian/amd64/mender-client_master-1_amd64.deb


## Mender add-ons

### Requirements

You need two applications for any add-on to function: the [Mender Client](../02.Overview/15.Taxonomy/docs.md)
and [Mender Connect](../02.Overview/15.Taxonomy/docs.md). If you have used the [express
installation](#express-installation) script, you already have both installed.

### mender-connect

The easiest way to install Mender Connect on an existing device is by using the
Mender APT repository. The other alternatives include: 
[mender-convert integration](../04.System-updates-Debian-family/99.Variables/docs.md#mender_addon_connect_install)
for installation in the existing images,
and [Yocto projects](../05.System-updates-Yocto-Project/05.Customize-Mender/docs.md#mender-connect)
for the installation in a Yocto Project environment.

To install `mender-connect` using Mender APT repository, follow the instructions
for [installing `mender-client` using the APT
repository](#install-using-the-apt-repository). After the final step, install
`mender-connect` using the package manager:

```bash
sudo apt-get install mender-connect
```

### Remote Terminal add-on

The Remote Terminal does not require any items installed other than the Mender Client
and Mender Connect.

### File transfer add-on

The File Transfer does not require any items installed other than the Mender Client
and Mender Connect.

### Mender Configure add-on

Mender offers a configure extension (`mender-configure`) to the Mender client
that enables managing device configuration. See the
[add-on page for Mender Configure](../09.Add-ons/10.Configure/docs.md) for
more information.

The easiest way to install Configure on an existing device is by using the
Mender APT repository. See the [add-on page for Mender
Configure](../09.Add-ons/10.Configure/docs.md) for more information for other
installation alternatives.

To install `mender-configure` using Mender APT repository, follow the
instructions for [installing `mender-client` using the APT
repository](#install-using-the-apt-repository). After the final step, install
`mender-configure` using the package manager:

```bash
sudo apt-get install mender-configure
```

## mender-cli

The `mender-cli` utility enables an easy interface to key use cases
of the Mender server API, such as uploading a Mender Artifact, from
the command line. See [Server integration](../08.Server-integration/chapter.md) for
more information.

Follow the correct link according to your host platform to download `mender-cli`:

<!--AUTOVERSION: "mender-cli %][x.x.x_mender-cli-"/mender-cli "mender-cli %][%_mender-cli-"/ignore-->
| Platform | Download link                                |                                                             |
|----------|----------------------------------------------|-------------------------------------------------------------|
| Linux    | [mender-cli 1.7.0][x.x.x_mender-cli-linux]  | [mender-cli master][master_mender-cli-linux] (Pre-release)  |
| Mac OS X | [mender-cli 1.7.0][x.x.x_mender-cli-darwin] | [mender-cli master][master_mender-cli-darwin] (Pre-release) |


Remember to add execute permission and ensure that the mender-cli utility is in a directory that is specified in your [PATH environment variable](https://en.wikipedia.org/wiki/PATH_(variable)?target=_blank). Most systems automatically have `/usr/local/bin` in your PATH so the following should allow proper execution and location of this binary.

```bash
sudo chmod +x mender-cli
sudo cp mender-cli /usr/local/bin/
```

Please refer to your host Operating System documentation for more details.

<!--AUTOVERSION: "mender-cli/%/"/mender-cli -->
[x.x.x_mender-cli-linux]: https://downloads.mender.io/mender-cli/1.7.0/linux/mender-cli
[x.x.x_mender-cli-darwin]: https://downloads.mender.io/mender-cli/1.7.0/darwin/mender-cli
<!--AUTOVERSION: "[%_mender-cli-"/ignore "mender-cli/%/"/ignore -->
[master_mender-cli-linux]: https://downloads.mender.io/mender-cli/master/linux/mender-cli
[master_mender-cli-darwin]: https://downloads.mender.io/mender-cli/master/darwin/mender-cli

## Monitor

!!! Note: The Mender Monitor add-on package is required. See the [Mender features page](https://mender.io/plans/features?target=_blank) for an overview of all Mender plans and features.


Mender offers a [Monitor](../09.Add-ons/20.Monitor/docs.md) add-on which
enables monitoring your devices for events and anomalies.

The easiest way to install Monitor on an existing device is by using the Mender
APT repository, see alternate installation methods on the [add-on page for
Mender Monitor](../09.Add-ons/20.Monitor/10.Installation/docs.md).

To install `mender-monitor` using the Mender Monitor Debian package, first
download it by running:

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="hosted"]
<!--AUTOVERSION: "/mender-monitor_%-1_all.deb"/monitor-client "/mender-monitor/debian/%/"/monitor-client -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
curl --fail -u "$HOSTED_MENDER_EMAIL" -O https://downloads.customer.mender.io/content/hosted/mender-monitor/debian/mender-3.2.0-build3/mender-monitor_mender-3.2.0-build3-1_all.deb
```
[/ui-tab]
[ui-tab title="enterprise"]
<!--AUTOVERSION: "/mender-monitor_%-1_all.deb"/monitor-client "/mender-monitor/debian/%/"/monitor-client -->
```bash
MENDER_ENTERPRISE_EMAIL=<your.email@example.com>
curl --fail -u $MENDER_ENTERPRISE_EMAIL -O https://downloads.customer.mender.io/content/on-prem/mender-monitor/debian/mender-3.2.0-build3/mender-monitor_mender-3.2.0-build3-1_all.deb
```
[/ui-tab]
[/ui-tabs]


Then install the package with:

<!--AUTOVERSION: "mender-monitor_%-1_all.deb"/monitor-client -->
```bash
dpkg -i mender-monitor_mender-3.2.0-build3-1_all.deb
apt --fix-broken -y install
```

# Mender monitor demo

If you have already installed the `mender-monitor` package, as shown in
[Installing Mender Monitor](#Monitor), the demo monitors can be installed
through the package:

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="hosted"]
<!--AUTOVERSION: "/mender-monitor_demo_%-1_all.deb"/monitor-client "/mender-monitor/debian/%/"/monitor-client -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
curl --fail -u "$HOSTED_MENDER_EMAIL" -O https://downloads.customer.mender.io/content/hosted/mender-monitor/debian/mender-3.2.0-build3/mender-monitor_demo_mender-3.2.0-build3-1_all.deb
```
[/ui-tab]
[ui-tab title="enterprise"]
<!--AUTOVERSION: "/mender-monitor_demo_%-1_all.deb"/monitor-client "/mender-monitor/debian/%/"/monitor-client -->
```bash
MENDER_ENTERPRISE_EMAIL=<your.email@example.com>
curl --fail -u $MENDER_ENTERPRISE_EMAIL -O https://downloads.customer.mender.io/content/on-prem/mender-monitor/debian/mender-3.2.0-build3/mender-monitor_demo_mender-3.2.0-build3-1_all.deb
```
[/ui-tab]
[/ui-tabs]


Then install the package with:

<!--AUTOVERSION: "mender-monitor_demo_%-1_all.deb"/monitor-client -->
```bash
dpkg -i mender-monitor_demo_mender-3.2.0-build3-1_all.deb
```
