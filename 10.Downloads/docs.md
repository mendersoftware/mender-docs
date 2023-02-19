---
title: Downloads
taxonomy:
    category: docs
markdown:
    extra: true
process:
    twig: true
---

<!-- AUTOMATION: execute=if [ "$TEST_ENTERPRISE" -ne 1 ]; then echo "TEST_ENTERPRISE must be set to 1!"; exit 1; fi -->

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
| Raspberry Pi 3 Model B and B+ | Raspberry Pi OS Bullseye Lite 2022-09-22 | [raspios-bullseye-armhf-lite-raspberrypi3-mender.img.xz][raspios-bullseye-armhf-lite-raspberrypi3-mender.img.xz] | 8 GB         |
| Raspberry Pi 4 Model B        | Raspberry Pi OS Bullseye Lite 2022-09-22 | [raspios-bullseye-armhf-lite-raspberrypi4-mender.img.xz][raspios-bullseye-armhf-lite-raspberrypi4-mender.img.xz] | 8 GB         |

<!--AUTOVERSION: "mender-convert-%.img.xz"/mender-convert -->
[raspios-bullseye-armhf-lite-raspberrypi3-mender.img.xz]: https://d4o6e0uccgv40.cloudfront.net/2022-09-22-raspios-bullseye-armhf-lite/arm/2022-09-22-raspios-bullseye-armhf-lite-raspberrypi3-mender-convert-4.0.0.img.xz
[raspios-bullseye-armhf-lite-raspberrypi4-mender.img.xz]: https://d4o6e0uccgv40.cloudfront.net/2022-09-22-raspios-bullseye-armhf-lite/arm/2022-09-22-raspios-bullseye-armhf-lite-raspberrypi4-mender-convert-4.0.0.img.xz

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

<!--AUTOVERSION: "keeps \"%\" version"/ignore-->
<!-- The second column points to pre-release software and keeps "master" version in the name and link -->
<!--AUTOVERSION: "mender-artifact %][x.x.x_mender-artifact-"/mender-artifact "mender-artifact %][%_mender-artifact-"/ignore-->
| Platform | Download link                                          |                                                                       |
|----------|--------------------------------------------------------|-----------------------------------------------------------------------|
| Linux    | [mender-artifact 3.10.0][x.x.x_mender-artifact-linux]  | [mender-artifact master][master_mender-artifact-linux] (Pre-release)  |
| Mac OS X | [mender-artifact 3.10.0][x.x.x_mender-artifact-darwin] | [mender-artifact master][master_mender-artifact-darwin] (Pre-release) |

!!! The `mender-artifact` pre-built binaries depend on OpenSSL 1.1 shared library. If you are
!!! running a system that has already migrated to OpenSSL 3, like Alpine Linux 3.17 or Ubuntu 22.04,
!!! you cannot run the binary directly. Follow one of these workarounds:
!!! * For Alpine Linux, install the `openssl1.1-compat` package
!!! * For Ubuntu 22.04 or newer, the recommended process is to install `mender-artifact` through the
!!! [Mender APT repositories](#install-using-the-apt-repository).
!!! * For the other cases where the distribution does not provide a compatibility package, build
!!! `mender-artifact` from the source.

Remember to add execute permission and ensure that the mender-artifact utility is in a directory that is specified in your [PATH environment variable](https://en.wikipedia.org/wiki/PATH_(variable)?target=_blank). Most systems automatically have `/usr/local/bin` in your PATH so the following should allow proper execution and location of this binary.

<!--AUTOMATION: ignore -->
```bash
sudo chmod +x mender-artifact
sudo cp mender-artifact /usr/local/bin/
```

Please refer to your host Operating System documentation for more details.


<!--AUTOVERSION: "mender-artifact/%/"/mender-artifact -->
[x.x.x_mender-artifact-linux]: https://downloads.mender.io/mender-artifact/3.10.0/linux/mender-artifact
[x.x.x_mender-artifact-darwin]: https://downloads.mender.io/mender-artifact/3.10.0/darwin/mender-artifact
<!--AUTOVERSION: "[%_mender-artifact-"/ignore "mender-artifact/%/"/ignore -->
[master_mender-artifact-linux]: https://downloads.mender.io/mender-artifact/master/linux/mender-artifact
[master_mender-artifact-darwin]: https://downloads.mender.io/mender-artifact/master/darwin/mender-artifact

! If you are using Mac OS X, note that using `mender-artifact` with
! disk image files (e.g.: `*.sdimg`, `*.img`, or others holding the storage
! partitions) has limited functionality. Commands like
! `mender-artifact cat` or `mender-artifact cp` will not work due to lack
! of support for certain utilities on the Mac platform.

!!! `mender-artifact` binary is shipped also in [mender-ci-tools Docker image](https://hub.docker.com/r/mendersoftware/mender-ci-tools). More information [here](../06.Artifact-creation/10.CI-CD/docs.md#mender-ci-workflows-docker-image).


## Mender client

The Mender client runs on the device, checks for and installs
software updates packaged as Mender Artifacts.
See [Client installation](../03.Client-installation/chapter.md) for more information
about how to configure and use the Mender client.

The `mender-client` Debian package installs:
* the binary,
* a systemd service,
* the default [identity script](../03.Client-installation/03.Identity/docs.md),
* the default [inventory scripts](../03.Client-installation/04.Inventory/docs.md)
* and the default [update modules](../03.Client-installation/05.Use-an-updatemodule/docs.md)
(and its generators).


### Installation methods

You can install the Mender client in different ways depending on your preference.

* Express installation using the [convenience
  script](#express-installation) from [https://get.mender.io](https://get.mender.io).
* Set up Mender's APT repository and install using the [package
  manager](#install-using-the-apt-repository).

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

<!--AUTOMATION: ignore -->
```bash
curl -fLsS https://get.mender.io -o get-mender.sh
# INSPECT get-mender.sh BEFORE PROCEEDING
sudo bash get-mender.sh
```

By default, the script installs the [remote terminal](#remote-terminal-add-on) and
[configure](#mender-configure-add-on) add-ons in addition to the client. If you do not want this
feature you can provide additional arguments to the script specifying which packages you want to
install. For example, the following will only install the Mender client:

<!--AUTOMATION: ignore -->
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

<!--AUTOMATION: ignore -->
```bash
sudo apt-get update
sudo apt-get upgrade
```

!!! If you customize any of the installed files from `mender-client` (for example modifying identity
!!! or inventory scripts), then please make sure to also save your work in an additional place.
!!! Files at paths that match the defaults shipped by the package will be overwritten when the
!!! client is upgraded or re-installed, so you might lose your work if you only modified the
!!! original files.


!!! To prevent the Mender client from upgrading when upgrading the rest of the
!!! system, mark it to be held with `sudo apt-mark hold mender-client`.


!!! Updating mender this way doesn't provide a rollback mechanism in case of issues.
!!! For production devices always update mender as part of the Operating System update with A/B partitions.

#### Install using the APT repository

Before installing the Mender client, you need to set up the Mender APT
repository. Afterwards, you can install and update the Mender client using the
`apt` command line interface.

##### Set up the APT repository

<!--AUTOVERSION: "Mender %"/ignore -->
!!! As of Mender 3.2.1 we deprecated the previous stable repository and stopped updating it. As of Mender 3.3 we removed it.
!!! Please use `https://downloads.mender.io/repos/debian debian/buster/stable main` and _not_
!!! "https://downloads.mender.io/repos/debian stable main".
!!! Please make sure you have the currently supported version of your choice in place and please
!!! see below for all the possible options.

!!! With this method, you will always install the latest released Mender components. If you need to install a specific version,
!!! or you want to stick to a specific minor release (e.g., to the latest LTS version), you can manually download the
!!! Debian packages from the [APT repository pool](https://downloads.mender.io/repos/debian/pool/main/).

1. Update the `apt` package index and install required dependencies.

<!-- AUTOMATION: execute=DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata -->
   ```bash
   sudo apt-get update
   sudo apt-get install --assume-yes \
   		apt-transport-https \
   		ca-certificates \
   		curl \
   		gnupg-agent \
   		software-properties-common
   ```

2. Add the official Mender GPG key to your trusted `apt` keychain:

   ```bash
   curl -fsSL https://downloads.mender.io/repos/debian/gpg | sudo tee /etc/apt/trusted.gpg.d/mender.asc
   ```

   Inspect the GPG key fingerprint and verify that it matches
   `E6C8 5734 5575 F921 8396  5662 2407 2B80 A1B2 9B00`.

<!--AUTOMATION: ignore -->
   ```bash
   gpg --show-keys --with-fingerprint /etc/apt/trusted.gpg.d/mender.asc
   ```
   ```
   pub   rsa3072 2020-11-13 [SC] [expires: 2024-10-23]
         E6C8 5734 5575 F921 8396  5662 2407 2B80 A1B2 9B00
   uid                      Mender Team <mender@northern.tech>
   sub   rsa3072 2020-11-13 [E] [expires: 2024-10-23]
   ```

3. Add the Mender repository to your sources list by selecting the architecture
   matching your device.

   First in order to make sure that there are no mender sources in
   '/etc/apt/sources.list' lingering from a previous install, run

<!--AUTOMATION: ignore -->
   ```bash
      sed -i.bak -e "\,https://downloads.mender.io/repos/debian,d" /etc/apt/sources.list
   ```

   Then add the sources according to your Linux distribution

   !!! For Raspberry OS, use Debian distributions. To know which version is your device running,
   !!! do `(. /etc/os-release && echo $VERSION_CODENAME)`

   [ui-tabs position="top-left" active="0" theme="lite" ]
   [ui-tab title="Debian Bullseye"]
<!--AUTOMATION: ignore -->
   ```bash
    echo "deb [arch=$(dpkg --print-architecture)] https://downloads.mender.io/repos/debian debian/bullseye/stable main" \
    | sudo tee /etc/apt/sources.list.d/mender.list > /dev/null
   ```
   [/ui-tab]
   [ui-tab title="Debian Buster"]
<!--AUTOMATION: ignore -->
   ```bash
    echo "deb [arch=$(dpkg --print-architecture)] https://downloads.mender.io/repos/debian debian/buster/stable main" \
    | sudo tee /etc/apt/sources.list.d/mender.list > /dev/null
   ```
   [/ui-tab]
   [ui-tab title="Ubuntu Bionic"]
<!--AUTOMATION: ignore -->
   ```bash
    echo "deb [arch=$(dpkg --print-architecture)] https://downloads.mender.io/repos/debian ubuntu/bionic/stable main" \
    | sudo tee /etc/apt/sources.list.d/mender.list > /dev/null
   ```
   [/ui-tab]
   [ui-tab title="Ubuntu Focal"]
   ```bash
    echo "deb [arch=$(dpkg --print-architecture)] https://downloads.mender.io/repos/debian ubuntu/focal/stable main" \
    | sudo tee /etc/apt/sources.list.d/mender.list > /dev/null
   ```
   [/ui-tab]
   [ui-tab title="Ubuntu Jammy"]
<!--AUTOMATION: ignore -->
   ```bash
    echo "deb [arch=$(dpkg --print-architecture)] https://downloads.mender.io/repos/debian ubuntu/jammy/stable main" \
    | sudo tee /etc/apt/sources.list.d/mender.list > /dev/null
   ```
   [/ui-tab]
   [/ui-tabs]

   !!! If you want the bleeding edge version of mender, you can use our
   !!! `experimental` repository by replacing `stable` with `experimental` in
   !!! the above command. Do not use the `experimental` repository in production
   !!! as these releases are not fully tested.

4. Update the package index and install the Mender client:

<!--AUTOMATION: ignore -->
   ```bash
   sudo apt-get update
   sudo apt-get install mender-client
   ```

<!-- AUTOMATION: execute=apt-get update -->
<!-- AUTOMATION: execute=DEBIAN_FRONTEND=noninteractive apt-get install -y mender-client -->

!!! To prevent the Mender client from upgrading when upgrading the rest of the
!!! system, mark it to be held with `sudo apt-mark hold mender-client`.

## Mender add-ons

### Requirements

You need two applications for any add-on to function: the [Mender Client](../02.Overview/15.Taxonomy/docs.md)
and [Mender Connect](../02.Overview/15.Taxonomy/docs.md). If you have used the [express
installation](#express-installation) script, you already have both installed.

### mender-connect

The easiest way to install Mender Connect on an existing device is by using the
Mender APT repository. The other alternatives include: 
[mender-convert integration](../04.Operating-System-updates-Debian-family/99.Variables/docs.md#mender_addon_connect_install)
for installation in the existing images,
and [Yocto projects](../05.Operating-System-updates-Yocto-Project/05.Customize-Mender/docs.md#mender-connect)
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

<!--AUTOVERSION: "keeps \"%\" version"/ignore-->
<!-- The second column points to pre-release software and keeps "master" version in the name and link -->
<!--AUTOVERSION: "mender-cli %][x.x.x_mender-cli-"/mender-cli "mender-cli %][%_mender-cli-"/ignore-->
| Platform | Download link                                |                                                             |
|----------|----------------------------------------------|-------------------------------------------------------------|
| Linux    | [mender-cli 1.10.0][x.x.x_mender-cli-linux]  | [mender-cli master][master_mender-cli-linux] (Pre-release)  |
| Mac OS X | [mender-cli 1.10.0][x.x.x_mender-cli-darwin] | [mender-cli master][master_mender-cli-darwin] (Pre-release) |


Remember to add execute permission and ensure that the mender-cli utility is in a directory that is specified in your [PATH environment variable](https://en.wikipedia.org/wiki/PATH_(variable)?target=_blank). Most systems automatically have `/usr/local/bin` in your PATH so the following should allow proper execution and location of this binary.

<!--AUTOMATION: ignore -->
```bash
sudo chmod +x mender-cli
sudo cp mender-cli /usr/local/bin/
```

Please refer to your host Operating System documentation for more details.

<!--AUTOVERSION: "mender-cli/%/"/mender-cli -->
[x.x.x_mender-cli-linux]: https://downloads.mender.io/mender-cli/1.10.0/linux/mender-cli
[x.x.x_mender-cli-darwin]: https://downloads.mender.io/mender-cli/1.10.0/darwin/mender-cli
<!--AUTOVERSION: "[%_mender-cli-"/ignore "mender-cli/%/"/ignore -->
[master_mender-cli-linux]: https://downloads.mender.io/mender-cli/master/linux/mender-cli
[master_mender-cli-darwin]: https://downloads.mender.io/mender-cli/master/darwin/mender-cli

!!! `mender-cli` binary is shipped also in [Docker image](https://hub.docker.com/r/mendersoftware/mender-ci-tools). More information [here](../06.Artifact-creation/10.CI-CD/docs.md#mender-ci-workflows-docker-image).

## Monitor

!!! Note: The Mender Monitor add-on package is required. See the [Mender features page](https://mender.io/product/features?target=_blank) for an overview of all Mender plans and features.


Mender offers a [Monitor](../09.Add-ons/20.Monitor/docs.md) add-on which
enables monitoring your devices for events and anomalies.

The easiest way to install Monitor on an existing device is by using the Mender
APT repository, see alternate installation methods on the [add-on page for
Mender Monitor](../09.Add-ons/20.Monitor/10.Installation/docs.md).

To install `mender-monitor` using the Mender Monitor Debian package, first
download it by running:

<!--AUTOMATION: execute=HOSTED_MENDER_EMAIL="$HOSTED_MENDER_IO_USERNAME" -->
<!--AUTOMATION: execute=HOSTED_MENDER_PASSWORD="$HOSTED_MENDER_IO_PASSWORD" -->

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="hosted"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
 HOSTED_MENDER_PASSWORD=<yoursecurepassword>
```
And download it with:
<!--AUTOVERSION: "/mender-monitor_%-1"/monitor-client "/mender-monitor/debian/%/"/monitor-client -->
```bash
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-monitor/debian/1.2.1/mender-monitor_1.2.1-1%2Bdebian%2Bbuster_all.deb
```
[/ui-tab]
[ui-tab title="enterprise"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_EMAIL=<your.email@example.com>
 MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:
<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-monitor_%-1"/monitor-client "/mender-monitor/debian/%/"/monitor-client -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_EMAIL" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-monitor/debian/1.2.1/mender-monitor_1.2.1-1%2Bdebian%2Bbuster_all.deb
```
[/ui-tab]
[/ui-tabs]


Then install the package with:

<!--AUTOVERSION: "mender-monitor_%-1"/monitor-client -->
```bash
sudo dpkg -i mender-monitor_1.2.1-1+debian+buster_all.deb || sudo apt --fix-broken -y install
```

### Demo monitors

If you have already installed the `mender-monitor` package, as shown in
[Installing Mender Monitor](#monitor), the demo monitors can be installed
through the package:

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="hosted"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
 HOSTED_MENDER_PASSWORD=<yoursecurepassword>
```
And download it with:
<!--AUTOVERSION: "/mender-monitor-demo_%-1"/monitor-client "/mender-monitor/debian/%/"/monitor-client -->
```bash
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-monitor/debian/1.2.1/mender-monitor-demo_1.2.1-1%2Bdebian%2Bbuster_all.deb
```
[/ui-tab]
[ui-tab title="enterprise"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_EMAIL=<your.email@example.com>
 MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-monitor-demo_%-1"/monitor-client "/mender-monitor/debian/%/"/monitor-client -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_EMAIL" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-monitor/debian/1.2.1/mender-monitor-demo_1.2.1-1%2Bdebian%2Bbuster_all.deb
```
[/ui-tab]
[/ui-tabs]


Then install the package with:

<!--AUTOVERSION: "mender-monitor-demo_%-1"/monitor-client -->
```bash
sudo dpkg -i mender-monitor-demo_1.2.1-1+debian+buster_all.deb
```

## Mender Gateway

!!!!! Mender Gateway is only available in the Mender Enterprise plan.
!!!!! See [the Mender features page](https://mender.io/product/features?target=_blank)
!!!!! for an overview of all Mender plans and features.

Mender offers [Mender Gateway](../08.Server-integration/04.Mender-Gateway/docs.md) which enables
managing and deploying OTA updates to devices on the local network from a gateway device.

To install `mender-gateway` using the Mender Gateway Debian package, first
download it by running:

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="hosted"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="Debian Bullseye"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="armhf"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
HOSTED_MENDER_PASSWORD=<yoursecurepassword>
```
And download it with:
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bdebian%2Bbullseye_armhf.deb
```
[/ui-tab]
[ui-tab title="arm64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
HOSTED_MENDER_PASSWORD=<yoursecurepassword>
```
And download it with:
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bdebian%2Bbullseye_arm64.deb
```
[/ui-tab]
[ui-tab title="amd64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
HOSTED_MENDER_PASSWORD=<yoursecurepassword>
```
And download it with:
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bdebian%2Bbullseye_amd64.deb
```
[/ui-tab]
[/ui-tabs]

[/ui-tab]
[ui-tab title="Debian Buster"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="armhf"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
HOSTED_MENDER_PASSWORD=<yoursecurepassword>
```
And download it with:
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bdebian%2Bbuster_armhf.deb
```
[/ui-tab]
[ui-tab title="arm64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
HOSTED_MENDER_PASSWORD=<yoursecurepassword>
```
And download it with:
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bdebian%2Bbuster_arm64.deb
```
[/ui-tab]
[ui-tab title="amd64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
HOSTED_MENDER_PASSWORD=<yoursecurepassword>
```
And download it with:
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bdebian%2Bbuster_amd64.deb
```
[/ui-tab]
[/ui-tabs]

[/ui-tab]
[ui-tab title="Ubuntu Bionic"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="armhf"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
HOSTED_MENDER_PASSWORD=<yoursecurepassword>
```
And download it with:
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bubuntu%2Bbionic_armhf.deb
```
[/ui-tab]
[ui-tab title="arm64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
HOSTED_MENDER_PASSWORD=<yoursecurepassword>
```
And download it with:
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bubuntu%2Bbionic_arm64.deb
```
[/ui-tab]
[ui-tab title="amd64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
HOSTED_MENDER_PASSWORD=<yoursecurepassword>
```
And download it with:
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bubuntu%2Bbionic_amd64.deb
```
[/ui-tab]
[/ui-tabs]

[/ui-tab]
[ui-tab title="Ubuntu Focal"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="armhf"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
HOSTED_MENDER_PASSWORD=<yoursecurepassword>
```
And download it with:
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bubuntu%2Bfocal_armhf.deb
```
[/ui-tab]
[ui-tab title="arm64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
HOSTED_MENDER_PASSWORD=<yoursecurepassword>
```
And download it with:
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bubuntu%2Bfocal_arm64.deb
```
[/ui-tab]
[ui-tab title="amd64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
HOSTED_MENDER_PASSWORD=<yoursecurepassword>
```
And download it with:
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bubuntu%2Bfocal_amd64.deb
```
[/ui-tab]
[/ui-tabs]

[/ui-tab]

[ui-tab title="Ubuntu Jammy"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="armhf"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
HOSTED_MENDER_PASSWORD=<yoursecurepassword>
```
And download it with:
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bubuntu%2Bjammy_armhf.deb
```
[/ui-tab]
[ui-tab title="arm64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
HOSTED_MENDER_PASSWORD=<yoursecurepassword>
```
And download it with:
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bubuntu%2Bjammy_arm64.deb
```
[/ui-tab]
[ui-tab title="amd64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
HOSTED_MENDER_PASSWORD=<yoursecurepassword>
```
And download it with:
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bubuntu%2Bjammy_amd64.deb
```
[/ui-tab]
[/ui-tabs]

[/ui-tab]



[/ui-tabs]

[/ui-tab]
[ui-tab title="enterprise"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="Debian Bullseye"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="armhf"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_EMAIL=<your.email@example.com>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_EMAIL" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bdebian%2Bbullseye_armhf.deb
```
[/ui-tab]
[ui-tab title="arm64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_EMAIL=<your.email@example.com>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_EMAIL" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bdebian%2Bbullseye_arm64.deb
```
[/ui-tab]
[ui-tab title="amd64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_EMAIL=<your.email@example.com>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_EMAIL" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bdebian%2Bbullseye_amd64.deb
```
[/ui-tab]
[/ui-tabs]

[/ui-tab]
[ui-tab title="Debian Buster"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="armhf"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_EMAIL=<your.email@example.com>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_EMAIL" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bdebian%2Bbuster_armhf.deb
```
[/ui-tab]
[ui-tab title="arm64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_EMAIL=<your.email@example.com>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_EMAIL" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bdebian%2Bbuster_arm64.deb
```
[/ui-tab]
[ui-tab title="amd64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_EMAIL=<your.email@example.com>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_EMAIL" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bdebian%2Bbuster_amd64.deb
```
[/ui-tab]
[/ui-tabs]

[/ui-tab]
[ui-tab title="Ubuntu Bionic"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="armhf"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_EMAIL=<your.email@example.com>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_EMAIL" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bubuntu%2Bbionic_armhf.deb
```
[/ui-tab]
[ui-tab title="arm64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_EMAIL=<your.email@example.com>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_EMAIL" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bubuntu%2Bbionic_arm64.deb
```
[/ui-tab]
[ui-tab title="amd64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_EMAIL=<your.email@example.com>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_EMAIL" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bubuntu%2Bbionic_amd64.deb
```
[/ui-tab]
[/ui-tabs]

[/ui-tab]
[ui-tab title="Ubuntu Focal"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="armhf"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_EMAIL=<your.email@example.com>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_EMAIL" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bubuntu%2Bfocal_armhf.deb
```
[/ui-tab]
[ui-tab title="arm64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_EMAIL=<your.email@example.com>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_EMAIL" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bubuntu%2Bfocal_arm64.deb
```
[/ui-tab]
[ui-tab title="amd64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_EMAIL=<your.email@example.com>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_EMAIL" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bubuntu%2Bfocal_amd64.deb
```
[/ui-tab]
[/ui-tabs]

[/ui-tab]

[ui-tab title="Ubuntu Jammy"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="armhf"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_EMAIL=<your.email@example.com>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_EMAIL" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bubuntu%2Bjammy_armhf.deb
```
[/ui-tab]
[ui-tab title="arm64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_EMAIL=<your.email@example.com>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_EMAIL" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bubuntu%2Bjammy_arm64.deb
```
[/ui-tab]
[ui-tab title="amd64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_EMAIL=<your.email@example.com>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_EMAIL" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/1.1.0/mender-gateway_1.1.0-1%2Bubuntu%2Bjammy_amd64.deb
```
[/ui-tab]
[/ui-tabs]

[/ui-tab]

[/ui-tabs]

[/ui-tab]
[/ui-tabs]


Then install the package with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "mender-gateway%-1"/mender-gateway -->
```bash
sudo dpkg -i mender-gateway_*.deb
```

<!--AUTOMATION: test=test $(ls mender-gateway_*.deb | wc -l) -eq 15 -->
<!--AUTOMATION: execute=dpkg -i mender-gateway_*-1+ubuntu+focal_amd64.deb -->

### Examples package

!!!!! You should not use this package on production devices.

If you have already installed the `mender-gateway` package, as shown in [Installing Mender
Gateway](#mender-gateway), you can install demo content through the examples package. This will
install the following:
* Self-signed demo certificate and key for `*.docker.mender.io`
* Demo configuration file with `UpstreamServer` configured for `hosted.mender.io`

<!--AUTOVERSION: "/mender-gateway/examples/%/"/mender-gateway "/mender-gateway-%.tar"/mender-gateway -->
Download the Mender Gateway examples package from
https://downloads.customer.mender.io/content/hosted/mender-gateway/examples/1.1.0/mender-gateway-1.1.0.tar
and download the tarball to a known location on your local system using your hosted
Mender username and password:

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="hosted"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
HOSTED_MENDER_PASSWORD=<yoursecurepassword>
```
And download it with:
<!--AUTOVERSION: "/mender-gateway/examples/%/"/mender-gateway "/mender-gateway-examples-%.tar"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/examples/1.1.0/mender-gateway-examples-1.1.0.tar
```
[/ui-tab]
[ui-tab title="enterprise"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_EMAIL=<your.email@example.com>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway/examples/%/"/mender-gateway "/mender-gateway-examples-%.tar"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_EMAIL" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/examples/1.1.0/mender-gateway-examples-1.1.0.tar
```
[/ui-tab]
[/ui-tabs]

Then install the contents with:

<!--AUTOVERSION: "mender-gateway-examples-%.tar"/mender-gateway -->
```bash
sudo tar -C / --strip-components=2 -xvf mender-gateway-examples-1.1.0.tar
```

<!--AUTOMATION: test=test -d /usr/share/doc/mender-gateway/examples -->
<!--AUTOMATION: test=grep hosted.mender.io /etc/mender/mender-gateway.conf -->
