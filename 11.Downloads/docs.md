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

# Disk images

These disk images (`*.img` or `*.sdimg`) are based on images provided by board
manufacturers and are ready to install the Mender Client. They are used to
provision the device storage for devices without Mender running already.

Mender provides images based on the following distributions:

* Images for **Raspberry Pi 3** and **Raspberry Pi 4**, which are based on the
  [Raspberry Pi OS Linux
  distribution](https://www.raspberrypi.com/software/operating-systems/?target=_blank)

!! Note that we do not offer commercial support for these images. They are based
!! on images supported by board manufacturers, like the Raspberry Pi Foundation,
!! and provide the same software and configuration options as the original
!! images. Please use the support resources available from the board
!! manufacturer, or [contact us](mailto:contact@mender.io) if you have any
!! questions on the Mender integration.

| Board                         | OS                              | Disk image                                                                                         | Storage size |
|-------------------------------|---------------------------------|----------------------------------------------------------------------------------------------------|--------------|
| Raspberry Pi 3 Model B and B+ | Raspberry Pi OS Bookworm Lite 2024-10-22 | [raspios-lite-raspberrypi3_bookworm_64bit-mender-convert.img.xz][raspios-lite-raspberrypi3_bookworm_64bit-mender-convert.img.xz] | 8 GB         |
| Raspberry Pi 4 Model B        | Raspberry Pi OS Bookworm Lite 2024-10-22 | [raspios-lite-raspberrypi4_bookworm_64bit-mender-convert.img.xz][raspios-lite-raspberrypi4_bookworm_64bit-mender-convert.img.xz] | 8 GB         |

<!--AUTOVERSION: "mender-convert-%.img.xz"/mender-convert -->
[raspios-lite-raspberrypi3_bookworm_64bit-mender-convert.img.xz]: https://d4o6e0uccgv40.cloudfront.net/2024-10-22-raspios-lite/arm/2024-10-22-raspios-lite-raspberrypi3_bookworm_64bit-mender-convert-4.3.0.img.xz
[raspios-lite-raspberrypi4_bookworm_64bit-mender-convert.img.xz]: https://d4o6e0uccgv40.cloudfront.net/2024-10-22-raspios-lite/arm/2024-10-22-raspios-lite-raspberrypi4_bookworm_64bit-mender-convert-4.3.0.img.xz

You can find images for other devices in our Mender Hub community forum, see
[Debian Family](https://hub.mender.io/c/board-integrations/debian-family/11?target=_blank) or
[Yocto Project](https://hub.mender.io/c/board-integrations/yocto-project/10?target=_blank)
integration posts.


# Workstation tools

## Set up the APT repository

Right now we support two package repositories: `workstation-tools` and `device-components`.

Workstation tools repo contains:
* mender-artifact
* mender-cli

!!! If you want the bleeding edge version of software, you can use our
!!! `experimental` repository by replacing `stable` with `experimental` in
!!! the above command. Do not use the `experimental` repository in production
!!! as these releases are not fully tested.

<!--AUTOVERSION: "Mender %"/ignore -->
!!! As of Mender 3.2.1 we deprecated the previous stable repository and stopped updating it. As of Mender 3.3 we removed it.

!!! With APT repo method, you will always install the latest released Mender components. If you need to install a specific version,
!!! or you want to stick to a specific minor release (e.g., to the latest LTS version), you can manually download the
!!! Debian packages from the [workstation tools repository](https://downloads.mender.io/repos/workstation-tools/pool/main).

<!-- AUTOMATION: execute=DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata -->

1. Update the `apt` package index and install required dependencies.

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
    pub   rsa3072 2020-11-13 [SC] [expires: 2026-10-01]
          E6C8 5734 5575 F921 8396  5662 2407 2B80 A1B2 9B00
    uid                      Mender Team <mender@northern.tech>
    sub   rsa3072 2020-11-13 [E] [expires: 2026-10-01]
    ```

3. Add the Mender repository to your sources list by selecting the architecture
matching your device.

    First, in order to make sure that there are no mender sources in
    '/etc/apt/sources.list' lingering from a previous install, run

    <!--AUTOMATION: ignore -->
    ```bash
    sudo sed -i.bak -e "\,https://downloads.mender.io/repos/workstation-tools,d" /etc/apt/sources.list
    ```

    Then add the sources according to your Linux distribution

    !!! For Raspberry OS, use Debian distributions. To know which version is your device running,
    !!! do `(. /etc/os-release && echo $VERSION_CODENAME)`

    [ui-tabs position="top-left" active="0" theme="lite" ]
    [ui-tab title="Debian 12"]
    <!--AUTOMATION: ignore -->
    ```bash
    echo "deb [arch=$(dpkg --print-architecture)] https://downloads.mender.io/repos/workstation-tools debian/bookworm/stable main" \
     | sudo tee /etc/apt/sources.list.d/mender.list
    ```
    [/ui-tab]
    [ui-tab title="Debian 11"]
    <!--AUTOMATION: ignore -->
    ```bash
    echo "deb [arch=$(dpkg --print-architecture)] https://downloads.mender.io/repos/workstation-tools debian/bullseye/stable main" \
     | sudo tee /etc/apt/sources.list.d/mender.list
    ```
    [/ui-tab]
    [ui-tab title="Ubuntu 24.04"]
    <!--AUTOMATION: ignore -->
    ```bash
    echo "deb [arch=$(dpkg --print-architecture)] https://downloads.mender.io/repos/workstation-tools ubuntu/noble/stable main" \
     | sudo tee /etc/apt/sources.list.d/mender.list
    ```
    [/ui-tab]
    [ui-tab title="Ubuntu 22.04"]
    <!--AUTOMATION: ignore -->
    ```bash
    echo "deb [arch=$(dpkg --print-architecture)] https://downloads.mender.io/repos/workstation-tools ubuntu/jammy/stable main" \
     | sudo tee /etc/apt/sources.list.d/mender.list
    ```
    [/ui-tab]
    [/ui-tabs]


## mender-artifact

The `mender-artifact` utility is used to work with Mender Artifacts,
which are files with the `.mender` suffix and contain software to be deployed.
See [Artifact creation](../07.Artifact-creation/chapter.md) for more information on how to
use this utility.

### Install using the APT repository

`mender-artifact` is available in the APT repository.
Follow the steps in [Set up the APT repository](#set-up-the-apt-repository) chapter to enable the repository and install `mender-artifact`.

Update the package index and install the Mender Artifact:

<!--AUTOMATION: ignore -->
```bash
sudo apt-get update
sudo apt-get install mender-artifact
```
<!-- AUTOMATION: execute=apt-get update -->
<!-- AUTOMATION: execute=DEBIAN_FRONTEND=noninteractive apt-get install -y mender-client4 -->

### Mac OS X

Use `brew` to install `mender-artifact` from [the Homebrew repository](https://brew.sh/):

<!--AUTOMATION: ignore -->
```bash
brew install mender-artifact
```

! Note that using `mender-artifact` on MacOS with disk image files (e.g.: `*.sdimg`,
! `*.img`, or others holding the storage partitions) has limited functionality. Commands
! like `mender-artifact cat` or `mender-artifact cp` will not work due to lack of support
! for certain utilities on the Mac platform.


!!! `mender-artifact` binary is shipped also in [mender-ci-tools Docker image](https://hub.docker.com/r/mendersoftware/mender-ci-tools). More information [here](../07.Artifact-creation/10.CI-CD/docs.md#mender-ci-workflows-docker-image).


## mender-cli

The `mender-cli` utility enables an easy interface to key use cases
of the Mender Server API, such as uploading a Mender Artifact, from
the command line. See [Server integration](../09.Server-integration/chapter.md) for
more information.

### Install using the APT repository

`mender-cli` is available in the APT repository.
Follow the steps in [Set up the APT repository](#set-up-the-apt-repository) chapter to enable the repository and install `mender-cli`.

Update the package index and install the Mender CLI:

<!--AUTOMATION: ignore -->
```bash
sudo apt-get update
sudo apt-get install mender-cli
```
<!-- AUTOMATION: execute=apt-get update -->
<!-- AUTOMATION: execute=DEBIAN_FRONTEND=noninteractive apt-get install -y mender-client4 -->

### Mac OS X

Use `brew` to install `mender-cli` from [the Homebrew repository](https://brew.sh/):

<!--AUTOMATION: ignore -->
```bash
brew install mender-cli
```

!!! `mender-cli` binary is shipped also in [Docker image](https://hub.docker.com/r/mendersoftware/mender-ci-tools). More information [here](../07.Artifact-creation/10.CI-CD/docs.md#mender-ci-workflows-docker-image).


# Device components

## Set up the APT repository

Right now we support two packages repositories: `workstation-tools` and `device-components`.

Device components repo contains:
* mender-app-update-module
* mender-client
* mender-client4
* mender-configure
* mender-connect
* mender-flash
* mender-setup
* mender-snapshot

!!! If you want the bleeding edge version of software, you can use our
!!! `experimental` repository by replacing `stable` with `experimental` in
!!! the above command. Do not use the `experimental` repository in production
!!! as these releases are not fully tested.

<!--AUTOVERSION: "Mender %"/ignore -->
!!! As of Mender 3.2.1 we deprecated the previous stable repository and stopped updating it. As of Mender 3.3 we removed it.

!!! With APT repo method, you will always install the latest released Mender components. If you need to install a specific version,
!!! or you want to stick to a specific minor release (e.g., to the latest LTS version), you can manually download the
!!! Debian packages from the [device components repository](https://downloads.mender.io/repos/device-components/pool/main).

1. Update the `apt` package index and install required dependencies.

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
    pub   rsa3072 2020-11-13 [SC] [expires: 2026-10-01]
          E6C8 5734 5575 F921 8396  5662 2407 2B80 A1B2 9B00
    uid                      Mender Team <mender@northern.tech>
    sub   rsa3072 2020-11-13 [E] [expires: 2026-10-01]
    ```

3. Add the Mender repository to your sources list by selecting the architecture
matching your device.

    First, in order to make sure that there are no mender sources in
    '/etc/apt/sources.list' lingering from a previous install, run

    <!--AUTOMATION: ignore -->
    ```bash
    sudo sed -i.bak -e "\,https://downloads.mender.io/repos/device-components,d" /etc/apt/sources.list
    ```

    Then add the sources according to your Linux distribution

    !!! For Raspberry OS, use Debian distributions. To know which version is your device running,
    !!! do `(. /etc/os-release && echo $VERSION_CODENAME)`

    [ui-tabs position="top-left" active="0" theme="lite" ]
    [ui-tab title="Debian 12"]
    <!--AUTOMATION: ignore -->
    ```bash
    echo "deb [arch=$(dpkg --print-architecture)] https://downloads.mender.io/repos/device-components debian/bookworm/stable main" \
     | sudo tee /etc/apt/sources.list.d/mender.list
    ```
    [/ui-tab]
    [ui-tab title="Debian 11"]
    <!--AUTOMATION: ignore -->
    ```bash
    echo "deb [arch=$(dpkg --print-architecture)] https://downloads.mender.io/repos/device-components debian/bullseye/stable main" \
     | sudo tee /etc/apt/sources.list.d/mender.list
    ```
    [/ui-tab]
    [ui-tab title="Ubuntu 24.04"]
    <!--AUTOMATION: ignore -->
    ```bash
    echo "deb [arch=$(dpkg --print-architecture)] https://downloads.mender.io/repos/device-components ubuntu/noble/stable main" \
     | sudo tee /etc/apt/sources.list.d/mender.list
    ```
    [/ui-tab]
    [ui-tab title="Ubuntu 22.04"]
    <!--AUTOMATION: ignore -->
    ```bash
    echo "deb [arch=$(dpkg --print-architecture)] https://downloads.mender.io/repos/device-components ubuntu/jammy/stable main" \
     | sudo tee /etc/apt/sources.list.d/mender.list
    ```
    [/ui-tab]
    [/ui-tabs]


## Mender Client

The Mender Client runs on the device, checks for and installs
software updates packaged as Mender Artifacts.
See [Client installation](../03.Client-installation/chapter.md) for more information
about how to configure and use the Mender Client.

The `mender-client` Debian package includes the legacy Mender Client written in Go (version 3.x.y),
and it installs:

* the binary,
* a systemd service,
* the default [identity script](../03.Client-installation/03.Identity/docs.md)
* the default [inventory scripts](../03.Client-installation/04.Inventory/docs.md)
* and the default [update modules](../03.Client-installation/05.Use-an-updatemodule/docs.md)
  (and its generators).

The `mender-client4` Debian package includes the 4.x series of the client, which has slightly
different components than the legacy one. The `mender-client4` Debian package installs:

* a `mender-auth` package, for server authentication
* a `mender-update` package, for doing updates
* two binaries, `mender-auth` and `mender-update`
* two systemd services, `mender-authd` and `mender-updated`
* the default [identity script](../03.Client-installation/03.Identity/docs.md)
* the default [inventory scripts](../03.Client-installation/04.Inventory/docs.md)
* and the default [update modules](../03.Client-installation/05.Use-an-updatemodule/docs.md)
  (and its generators).
* the `mender-flash` tool
* the `mender-setup` tool
* the `mender-snapshot` tool


### Installation methods

You can install the Mender Client in different ways depending on your preference.

* Express installation using the [convenience
  script](#express-installation) from [https://get.mender.io](https://get.mender.io).
* Set up Mender's APT repository and install using the [package
  manager](#install-using-the-apt-repository).

#### Express installation

Mender provides a convenience script available at [get.mender.io
](https://get.mender.io) that non-interactively installs the Mender Client
[using the package manager](#install-using-the-apt-repository). Users installing
the Mender Client this way, should be aware that:

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
install. For example, the following will only install the Mender Client:

<!--AUTOMATION: ignore -->
```bash
curl -fLsS https://get.mender.io -o get-mender.sh
# INSPECT get-mender.sh BEFORE PROCEEDING
sudo bash get-mender.sh mender-client4
```

!!! Mender offers an `experimental` version of the package repository. To use
!!! the latest experimental version of Mender, run the script with an additional
!!! flag `-c experimental`. Do not use the `experimental` repository for
!!! production devices as these releases are not fully tested.

#### Upgrading Mender after the express installation

After installing the Mender Client with [get.mender.io](https://get.mender.io),
the packages are maintained by the package manager. To upgrade the software, simply run

<!--AUTOMATION: ignore -->
```bash
sudo apt-get update
sudo apt-get upgrade
```

!!! Updating mender this way doesn't provide a rollback mechanism in case of issues.
!!! For production devices always update mender as part of the Operating System update with A/B partitions.

### Install using the APT repository

`mender-client` is available in the APT repository.
Follow the steps in [Set up the APT repository](#set-up-the-apt-repository-1) chapter to enable the repository and install `mender-client`.

Update the package index and install the Mender Client:

<!--AUTOMATION: ignore -->
```bash
sudo apt-get update
sudo apt-get install mender-client4
```
<!-- AUTOMATION: execute=apt-get update -->
<!-- AUTOMATION: execute=DEBIAN_FRONTEND=noninteractive apt-get install -y mender-client4 -->


## mender-connect

The easiest way to install Mender Connect on an existing device is by using the
[Set up the APT repository](#set-up-the-apt-repository-1). The other alternatives include: 
[mender-convert integration](../04.Operating-System-updates-Debian-family/99.Variables/docs.md#mender_addon_connect_install)
for installation in the existing images,
and [Yocto projects](../05.Operating-System-updates-Yocto-Project/05.Customize-Mender/docs.md#mender-connect)
for the installation in a Yocto Project environment.

To install `mender-connect` using Mender APT repository, follow the instructions
for [installing the Mender Client using the APT
repository](#install-using-the-apt-repository). After the final step, install
`mender-connect` using the package manager:

```bash
sudo apt-get install mender-connect
```

!!! You need two applications for any add-on to function: [`mender-auth`](../02.Overview/16.Taxonomy/docs.md),
!!! one of the components of the Mender Client, and [Mender Connect](../02.Overview/16.Taxonomy/docs.md).
!!! If you have used the [express installation](#express-installation) script, you already have both installed.


### Remote Terminal add-on

The Remote Terminal does not require any items installed other than `mender-auth`
and Mender Connect.

### File transfer add-on

The File Transfer does not require any items installed other than `mender-auth`
and Mender Connect.

### Mender Configure add-on

Mender offers a configure extension (`mender-configure`) to the `mender-update` client
that enables managing device configuration. See the
[add-on page for Mender Configure](../10.Add-ons/10.Configure/docs.md) for
more information.

The easiest way to install Configure on an existing device is by using the
Mender APT repository. See the [add-on page for Mender
Configure](../10.Add-ons/10.Configure/docs.md) for more information for other
installation alternatives.

To install `mender-configure` using Mender APT repository, follow the
instructions for [installing the Mender Client using the APT
repository](#install-using-the-apt-repository). After the final step, install
`mender-configure` using the package manager:

```bash
sudo apt-get install mender-configure
```


## Monitor

!!! Note: The Mender Monitor add-on package is required. See the [Mender features page](https://mender.io/product/features?target=_blank) for an overview of all Mender plans and features.


Mender offers a [Monitor](../10.Add-ons/20.Monitor/docs.md) add-on which
enables monitoring your devices for events and anomalies.

To install `mender-monitor` using the Mender Monitor Debian package, first
download it by running:

<!--AUTOMATION: execute=HOSTED_MENDER_EMAIL="$HOSTED_MENDER_IO_USERNAME" -->
<!--AUTOMATION: execute=HOSTED_MENDER_PASSWORD="$HOSTED_MENDER_IO_PASSWORD" -->

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="Hosted Mender"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
HOSTED_MENDER_PASSWORD=<yoursecurepassword>
```
And download it with:
<!--AUTOVERSION: "/mender-monitor_%-1"/monitor-client "/mender-monitor/debian/%/"/monitor-client -->
```bash
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-monitor/debian/1.4.1/mender-monitor_1.4.1-1%2Bdebian%2Bbullseye_all.deb
```
[/ui-tab]
[ui-tab title="Mender Server Enterprise"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_USER=<your.user>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
!!!!! Please keep in mind that these are the credentials used to access the Mender Docker Registry.
And download it with:
<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-monitor_%-1"/monitor-client "/mender-monitor/debian/%/"/monitor-client -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_USER" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-monitor/debian/1.4.1/mender-monitor_1.4.1-1%2Bdebian%2Bbullseye_all.deb
```
[/ui-tab]
[/ui-tabs]


Then install the package with:

<!--AUTOVERSION: "mender-monitor_%-1"/monitor-client -->
```bash
sudo dpkg -i mender-monitor_1.4.1-1+debian+bullseye_all.deb || sudo apt --fix-broken -y install
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
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-monitor/debian/1.4.1/mender-monitor-demo_1.4.1-1%2Bdebian%2Bbullseye_all.deb
```
[/ui-tab]
[ui-tab title="enterprise"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_USER=<your.user>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-monitor-demo_%-1"/monitor-client "/mender-monitor/debian/%/"/monitor-client -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_USER" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-monitor/debian/1.4.1/mender-monitor-demo_1.4.1-1%2Bdebian%2Bbullseye_all.deb
```
[/ui-tab]
[/ui-tabs]


Then install the package with:

<!--AUTOVERSION: "mender-monitor-demo_%-1"/monitor-client -->
```bash
sudo dpkg -i mender-monitor-demo_1.4.1-1+debian+bullseye_all.deb
```

## Mender Gateway

!!!!! Mender Gateway is only available in the Mender Enterprise plan.
!!!!! See [the Mender plans page](https://mender.io/pricing/plans?target=_blank)
!!!!! for an overview of all Mender plans and features.

Mender offers [Mender Gateway](../09.Server-integration/04.Mender-Gateway/docs.md) which enables
managing and deploying OTA updates to devices on the local network from a gateway device.

To install `mender-gateway` using the Mender Gateway Debian package, first
download it by running:

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="hosted"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="Debian 12"]

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
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bdebian%2Bbookworm_armhf.deb
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
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bdebian%2Bbookworm_arm64.deb
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
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bdebian%2Bbookworm_amd64.deb
```
[/ui-tab]
[/ui-tabs]

[/ui-tab]
[ui-tab title="Debian 11"]

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
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bdebian%2Bbullseye_armhf.deb
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
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bdebian%2Bbullseye_arm64.deb
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
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bdebian%2Bbullseye_amd64.deb
```
[/ui-tab]
[/ui-tabs]

[/ui-tab]
[ui-tab title="Ubuntu 24.04"]

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
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bubuntu%2Bnoble_armhf.deb
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
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bubuntu%2Bnoble_arm64.deb
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
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bubuntu%2Bnoble_amd64.deb
```
[/ui-tab]
[/ui-tabs]

[/ui-tab]
[ui-tab title="Ubuntu 22.04"]

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
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bubuntu%2Bjammy_armhf.deb
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
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bubuntu%2Bjammy_arm64.deb
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
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bubuntu%2Bjammy_amd64.deb
```
[/ui-tab]
[/ui-tabs]

[/ui-tab]



[/ui-tabs]

[/ui-tab]
[ui-tab title="enterprise"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="Debian 12"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="armhf"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_USER=<your.user>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_USER" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bdebian%2Bbookworm_armhf.deb
```
[/ui-tab]
[ui-tab title="arm64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_USER=<your.user>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_USER" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bdebian%2Bbookworm_arm64.deb
```
[/ui-tab]
[ui-tab title="amd64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_USER=<your.user>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_USER" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bdebian%2Bbookworm_amd64.deb
```
[/ui-tab]
[/ui-tabs]

[/ui-tab]
[ui-tab title="Debian 11"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="armhf"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_USER=<your.user>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_USER" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bdebian%2Bbullseye_armhf.deb
```
[/ui-tab]
[ui-tab title="arm64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_USER=<your.user>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_USER" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bdebian%2Bbullseye_arm64.deb
```
[/ui-tab]
[ui-tab title="amd64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_USER=<your.user>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_USER" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bdebian%2Bbullseye_amd64.deb
```
[/ui-tab]
[/ui-tabs]

[/ui-tab]
[ui-tab title="Ubuntu 24.04"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="armhf"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_USER=<your.user>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_USER" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bubuntu%2Bnoble_armhf.deb
```
[/ui-tab]
[ui-tab title="arm64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_USER=<your.user>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_USER" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bubuntu%2Bnoble_arm64.deb
```
[/ui-tab]
[ui-tab title="amd64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_USER=<your.user>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_USER" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bubuntu%2Bnoble_amd64.deb
```
[/ui-tab]
[/ui-tabs]

[/ui-tab]
[ui-tab title="Ubuntu 22.04"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="armhf"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_USER=<your.user>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_USER" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bubuntu%2Bjammy_armhf.deb
```
[/ui-tab]
[ui-tab title="arm64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_USER=<your.user>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_USER" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bubuntu%2Bjammy_arm64.deb
```
[/ui-tab]
[ui-tab title="amd64"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_USER=<your.user>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway_%-1"/mender-gateway "/mender-gateway/debian/%/"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_USER" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bubuntu%2Bjammy_amd64.deb
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

<!--AUTOMATION: test=test $(ls mender-gateway_*.deb | wc -l) -eq 12 -->
<!--AUTOMATION: execute=dpkg -i mender-gateway_*-1+ubuntu+noble_amd64.deb -->

### Examples package

!!!!! You should not use this package on production devices.

If you have already installed the `mender-gateway` package, as shown in [Installing Mender
Gateway](#mender-gateway), you can install demo content through the examples package. This will
install the following:
* Self-signed demo certificate and key for `*.docker.mender.io`
* Demo configuration file with `UpstreamServer` configured for `hosted.mender.io`

<!--AUTOVERSION: "/mender-gateway/examples/%/"/mender-gateway "/mender-gateway-%.tar"/mender-gateway -->
Download the Mender Gateway examples package from
https://downloads.customer.mender.io/content/hosted/mender-gateway/examples/2.0.0/mender-gateway-2.0.0.tar
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
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/examples/2.0.0/mender-gateway-examples-2.0.0.tar
```
[/ui-tab]
[ui-tab title="enterprise"]
Set the following variables with your credentials:
<!--AUTOMATION: ignore -->
```bash
MENDER_ENTERPRISE_USER=<your.user>
MENDER_ENTERPRISE_PASSWORD=<yoursecurepassword>
```
And download it with:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-gateway/examples/%/"/mender-gateway "/mender-gateway-examples-%.tar"/mender-gateway -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_USER" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/examples/2.0.0/mender-gateway-examples-2.0.0.tar
```
[/ui-tab]
[/ui-tabs]

Then install the contents with:

<!--AUTOVERSION: "mender-gateway-examples-%.tar"/mender-gateway -->
```bash
sudo tar -C / --strip-components=2 -xvf mender-gateway-examples-2.0.0.tar
```

<!--AUTOMATION: test=test -d /usr/share/doc/mender-gateway/examples -->
<!--AUTOMATION: test=grep hosted.mender.io /etc/mender/mender-gateway.conf -->


## Mender Binary Delta

### Download

If you are using *hosted Mender*, set the following variables with your credentials:

<!--AUTOMATION: ignore -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
HOSTED_MENDER_PASSWORD=<yoursecurepassword>
```
!!! If you signed up using your Google or GitHub login, use the email address linked to that account and enter `x` as the password.

Now, download the `mender-binary-delta` archive with the following command:

<!--AUTOMATION: execute=HOSTED_MENDER_EMAIL="$HOSTED_MENDER_IO_USERNAME" -->
<!--AUTOMATION: execute=HOSTED_MENDER_PASSWORD="$HOSTED_MENDER_IO_PASSWORD" -->

<!--AUTOVERSION: "mender-binary-delta/%/mender-binary-delta-%.tar"/mender-binary-delta-->
```bash
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-binary-delta/1.5.1/mender-binary-delta-1.5.1.tar.xz
```
On the other hand, if you are using *on-premise Mender Enterprise*, download using the following
command:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "mender-binary-delta/%/mender-binary-delta-%.tar"/mender-binary-delta-->
```bash
MENDER_ENTERPRISE_USER=<your.user>
curl -u $MENDER_ENTERPRISE_USER -O https://downloads.customer.mender.io/content/on-prem/mender-binary-delta/1.5.1/mender-binary-delta-1.5.1.tar.xz
```

<!--AUTOVERSION: "mender-binary-delta-%.tar.xz"/mender-binary-delta-->
The archive `mender-binary-delta-1.5.1.tar.xz` contains the binaries needed to generate and apply deltas.

<!--AUTOVERSION: "mender-binary-delta-%.tar.xz"/mender-binary-delta-->
Unpack the `mender-binary-delta-1.5.1.tar.xz` in your home directory:

<!--AUTOVERSION: "mender-binary-delta-%.tar.xz"/mender-binary-delta-->
```bash
tar xvf mender-binary-delta-1.5.1.tar.xz
```

The file structure should look like this:

```text
├── aarch64
│   ├── mender-binary-delta
│   └── mender-binary-delta-generator
├── arm
│   ├── mender-binary-delta
│   └── mender-binary-delta-generator
├── licenses
│   └── ...
└── x86_64
    ├── mender-binary-delta
    └── mender-binary-delta-generator
```

### The `mender-binary-delta-generator`

You will need this binary on the host to [create a delta between two artifacts](../07.Artifact-creation/05.Create-a-Delta-update-Artifact/docs.md) locally.

!!! The enterprise plan allows auto generation of [delta images directly on the mender server](../07.Artifact-creation/05.Server-side-generation-of-Delta-Artifacts/docs.md).

Copy the generator compatible with your workstation architecture to `/usr/bin`; for a `x86_64` one, it should look like this:

<!--AUTOVERSION: "mender-binary-delta-%"/mender-binary-delta-->
```bash
sudo cp mender-binary-delta-1.5.1/x86_64/mender-binary-delta-generator /usr/bin
```



