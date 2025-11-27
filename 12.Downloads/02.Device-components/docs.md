---
title: Device components
taxonomy:
    category: docs
markdown:
    extra: true
process:
    twig: true
---

<!--AUTOVERSION: "Mender Client %"/ignore -->
! **[2025-11] Repository Change Notice**
! As of Mender Client 5.0.3 (mender-client4 package), the repository location has changed ([announcement](https://mender.io/blog/new-mender-packaging-and-distribution-channels)):
! - **Old:** `https://downloads.mender.io/repos/debian/pool/main/m/`
! - **New:** `https://downloads.mender.io/repos/device-components/pool/main/m/`
! 
! **Action required:** Update your sources list to regain access to the supported versions.


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

!!! With APT repo method, you will always install the latest released Mender components. If you need to install a specific version,
!!! or you want to stick to a specific minor release (e.g., to the latest LTS version), you can manually download the
!!! Debian packages from the [device components repository](https://downloads.mender.io/repos/device-components/pool/main).

1. Update the `apt` package index and install required dependencies.

    ```bash
    sudo apt-get update
    sudo apt-get install --assume-yes --no-install-recommends \
    		apt-transport-https \
    		ca-certificates \
    		curl \
    		gnupg \
    		jq
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
    [ui-tab title="Debian 13"]
    <!--AUTOMATION: ignore -->
    ```bash
    echo "deb [arch=$(dpkg --print-architecture)] https://downloads.mender.io/repos/device-components debian/trixie/stable main" \
     | sudo tee /etc/apt/sources.list.d/mender.list
    ```
    [/ui-tab]
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
See [Client installation](../../03.Client-installation/chapter.md) for more information
about how to configure and use the Mender Client.

The `mender-client` Debian package includes the legacy Mender Client written in Go (version 3.x.y),
and it installs:

* the binary,
* a systemd service,
* the default [identity script](../../03.Client-installation/03.Identity/docs.md)
* the default [inventory scripts](../../03.Client-installation/04.Inventory/docs.md)
* and the default [update modules](../../03.Client-installation/05.Use-an-updatemodule/docs.md)
  (and its generators).

The `mender-client4` Debian package includes the 4.x series of the client, which has slightly
different components than the legacy one. The `mender-client4` Debian package installs:

* a `mender-auth` package, for server authentication
* a `mender-update` package, for doing updates
* two binaries, `mender-auth` and `mender-update`
* two systemd services, `mender-authd` and `mender-updated`
* the default [identity script](../../03.Client-installation/03.Identity/docs.md)
* the default [inventory scripts](../../03.Client-installation/04.Inventory/docs.md)
* and the default [update modules](../../03.Client-installation/05.Use-an-updatemodule/docs.md)
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
Follow the steps in [Set up the APT repository](#set-up-the-apt-repository) chapter to enable the repository and install `mender-client`.

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
[Set up the APT repository](#set-up-the-apt-repository). The other alternatives include: 
[mender-convert integration](../../04.Operating-System-updates-Debian-family/99.Variables/docs.md#mender_addon_connect_install)
for installation in the existing images,
and [Yocto projects](../../05.Operating-System-updates-Yocto-Project/05.Customize-Mender/docs.md#mender-connect)
for the installation in a Yocto Project environment.

To install `mender-connect` using Mender APT repository, follow the instructions
for [installing the Mender Client using the APT
repository](#install-using-the-apt-repository). After the final step, install
`mender-connect` using the package manager:

<!--AUTOMATION: ignore -->
```bash
sudo apt-get install mender-connect
```
<!-- AUTOMATION: execute=DEBIAN_FRONTEND=noninteractive apt-get install -y mender-connect -->

!!! You need two applications for any add-on to function: [`mender-auth`](../../02.Overview/16.Taxonomy/docs.md),
!!! one of the components of the Mender Client, and [Mender Connect](../../02.Overview/16.Taxonomy/docs.md).
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
[add-on page for Mender Configure](../../11.Add-ons/10.Configure/docs.md) for
more information.

The easiest way to install Configure on an existing device is by using the
Mender APT repository. See the [add-on page for Mender
Configure](../../11.Add-ons/10.Configure/docs.md) for more information for other
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


Mender offers a [Monitor](../../11.Add-ons/20.Monitor/docs.md) add-on which
enables monitoring your devices for events and anomalies.

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
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-monitor/debian/1.4.3/mender-monitor_1.4.3-1%2Bdebian%2Btrixie_all.deb
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
<!--AUTOVERSION: "/mender-monitor_%-1"/monitor-client "/mender-monitor/debian/%/"/monitor-client -->
```bash
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_USER" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-monitor/debian/1.4.3/mender-monitor_1.4.3-1%2Bdebian%2Btrixie_all.deb
```
[/ui-tab]
[/ui-tabs]


Then install the package with:

<!--AUTOVERSION: "mender-monitor_%-1"/monitor-client -->
```bash
sudo dpkg -i mender-monitor_1.4.3-1+debian+trixie_all.deb || sudo apt --fix-broken -y install
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
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-monitor/debian/1.4.3/mender-monitor-demo_1.4.3-1%2Bdebian%2Btrixie_all.deb
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
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_USER" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-monitor/debian/1.4.3/mender-monitor-demo_1.4.3-1%2Bdebian%2Btrixie_all.deb
```
[/ui-tab]
[/ui-tabs]


Then install the package with:

<!--AUTOVERSION: "mender-monitor-demo_%-1"/monitor-client -->
```bash
sudo dpkg -i mender-monitor-demo_1.4.3-1+debian+trixie_all.deb
```

## Mender Gateway

!!!!! Mender Gateway is only available in the Mender Enterprise plan.
!!!!! See [the Mender plans page](https://mender.io/pricing/plans?target=_blank)
!!!!! for an overview of all Mender plans and features.

Mender offers [Mender Gateway](../../10.Server-integration/04.Mender-Gateway/docs.md) which enables
managing and deploying OTA updates to devices on the local network from a gateway device.

To install `mender-gateway` using the Mender Gateway Debian package, first
download it by running:

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="hosted"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="Debian 13"]

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
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bdebian%2Btrixie_armhf.deb
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
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bdebian%2Btrixie_arm64.deb
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
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bdebian%2Btrixie_amd64.deb
```
[/ui-tab]
[/ui-tabs]

[/ui-tab]
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
[ui-tab title="Debian 13"]

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
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_USER" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bdebian%2Btrixie_armhf.deb
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
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_USER" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bdebian%2Btrixie_arm64.deb
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
wget --auth-no-challenge --user "$MENDER_ENTERPRISE_USER" --password "$MENDER_ENTERPRISE_PASSWORD" https://downloads.customer.mender.io/content/on-prem/mender-gateway/debian/2.0.0/mender-gateway_2.0.0-1%2Bdebian%2Btrixie_amd64.deb
```
[/ui-tab]
[/ui-tabs]

[/ui-tab]
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

<!--AUTOMATION: test=test $(ls mender-gateway_*.deb | wc -l) -eq 15 -->
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
wget --auth-no-challenge --user "$HOSTED_MENDER_EMAIL" --password "$HOSTED_MENDER_PASSWORD" https://downloads.customer.mender.io/content/hosted/mender-binary-delta/1.5.2/mender-binary-delta-1.5.2.tar.xz
```
On the other hand, if you are using *on-premise Mender Enterprise*, download using the following
command:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "mender-binary-delta/%/mender-binary-delta-%.tar"/mender-binary-delta-->
```bash
MENDER_ENTERPRISE_USER=<your.user>
curl -u $MENDER_ENTERPRISE_USER -O https://downloads.customer.mender.io/content/on-prem/mender-binary-delta/1.5.2/mender-binary-delta-1.5.2.tar.xz
```

<!--AUTOVERSION: "mender-binary-delta-%.tar.xz"/mender-binary-delta-->
The archive `mender-binary-delta-1.5.2.tar.xz` contains the binaries needed to generate and apply deltas.

<!--AUTOVERSION: "mender-binary-delta-%.tar.xz"/mender-binary-delta-->
Unpack the `mender-binary-delta-1.5.2.tar.xz` in your home directory:

<!--AUTOVERSION: "mender-binary-delta-%.tar.xz"/mender-binary-delta-->
```bash
tar xvf mender-binary-delta-1.5.2.tar.xz
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

You will need this binary on the host to [create a delta between two artifacts](../../08.Artifact-creation/05.Create-a-Delta-update-Artifact/docs.md) locally.

!!! The enterprise plan allows auto generation of [delta images directly on the mender server](../../08.Artifact-creation/05.Server-side-generation-of-Delta-Artifacts/docs.md).

Copy the generator compatible with your workstation architecture to `/usr/bin`; for a `x86_64` one, it should look like this:

<!--AUTOVERSION: "mender-binary-delta-%"/mender-binary-delta-->
```bash
sudo cp mender-binary-delta-1.5.2/x86_64/mender-binary-delta-generator /usr/bin
```


