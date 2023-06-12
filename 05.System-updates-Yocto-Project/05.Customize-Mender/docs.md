---
title: Customize Mender
taxonomy:
    category: docs
    label: tutorial
---


## Pre-release versions

If you want to use pre-release versions of the Mender components, please have a look at [the
`PREFERRED_VERSION` variables in the `local.conf`
example](../03.Build-for-demo/docs.md#configuring-the-build).


## Configuring server address and port

If the client should connect to a different address than the default of `https://docker.mender.io/`, then you should specify this variable in your `local.conf`:

```bash
MENDER_SERVER_URL = "https://mender.example.com"
```

Port numbers can be specified in the same way as you would in a browser, as a colon after the address followed by the number, for example `https://mender.example.com:8999`.

!! Note that the `https` protocol specifier is required in the address. For security reasons, Mender does not support the plaintext `http` protocol.


## Configuring polling intervals

You can configure how frequently the Mender client will make requests to the Mender server
as described in [Polling intervals](../../03.Client-installation/07.Configuration-file/01.Polling-intervals/docs.md) before
starting the build process.

In order to do this, add the following in your `local.conf`:

```bash
MENDER_UPDATE_POLL_INTERVAL_SECONDS = "1800"
MENDER_INVENTORY_POLL_INTERVAL_SECONDS = "28800"
```


## Configuration file

It is possible to put your own `mender.conf` configuration file in the image. The file will be
merged with settings from Yocto variables. To use your own file, use a `mender-client_%.bbappend`
file in your own layer, add a `mender.conf` file to the layer, and list this file in the `SRC_URI`
of the `mender-client` recipe, like this:

```bash
FILESEXTRAPATHS:prepend := "${THISDIR}/<DIRECTORY-WITH-MENDER-CONF>:"
SRC_URI:append = " file://mender.conf"
```

Replace `<DIRECTORY-WITH-MENDER-CONF>` with the path to the `mender.conf` file, relative to the
recipe file.

Note that variables take precedence over entries in the `mender.conf` file, so if there are any
conflicts, you should either set the affected variables to the empty string, or remove the entry
from your `mender.conf` file. The message will normally look like this:

```text
Configuration key 'ServerURL', found in mender.conf, conflicts with MENDER_SERVER_URL. Choosing the latter.
```


## Disabling Mender as a system service

If you do not want Mender to run as a system service, and you prefer to carry out update steps manually using the command line client interface, you can disable the service that starts Mender at boot.

This is simple to accomplish by adding a `recipes-mender/mender/mender-client_%.bbappend` file in your Yocto Project layer, with the following content:

```bash
SYSTEMD_AUTO_ENABLE = "disable"
```

In this case it is also possible to avoid Mender's current dependency on systemd. If you do not wish to enable systemd in your build, add the following to `local.conf`:

```bash
MENDER_FEATURES_DISABLE:append = " mender-systemd"
```

Also, you do not need any daemon-related configuration items in your `local.conf` as outlined in [the section on configuring the Yocto Project build](../../05.System-updates-Yocto-Project/03.Build-for-demo/docs.md#configuring-the-build).

! If you disable Mender running as a daemon under `systemd`, you must run all required Mender commands from the CLI or scripts. Most notably, you need to run `mender commit` after booting into and verifying a successful deployment. When running in managed mode, any pending `mender commit` will automatically run by the Mender daemon after it starts. See [Modes of operation](../../02.Overview/01.Introduction/docs.md#client-modes-of-operation) for more information about the difference.


## Identity

In order to include an identity script, simply augment the `mender-client` recipe and install the
script in the expected folder. For example, create a `mender-client_%.bbappend` file in your layer,
and add this:

```bash
FILESEXTRAPATHS:prepend := "${THISDIR}/<DIRECTORY-WITH-IDENTITY-SCRIPT>:"
SRC_URI:append = " file://mender-device-identity"

do_install:append() {
    install -d ${D}/${datadir}/mender/identity
    install -m 755 ${WORKDIR}/mender-device-identity ${D}/${datadir}/mender/identity/mender-device-identity
}
```

Replace `<DIRECTORY-WITH-IDENTITY-SCRIPT>` with the path to the `mender-device-identity` file, relative to the
recipe file.


## Inventory

Mender comes with some inventory scripts available out of the box. These are:

* mender-inventory-bootloader-integration
* mender-inventory-geo
* mender-inventory-hostinfo
* mender-inventory-network
* mender-inventory-os
* mender-inventory-provides
* mender-inventory-rootfs-type
* mender-inventory-update-modules

In order to include an inventory script of your own making, augment the
`mender-client` recipe and install the script in the expected folder. For
example, create a `mender-client_%.bbappend` file in your layer, and add this:

```bash
FILESEXTRAPATHS:prepend := "${THISDIR}/<DIRECTORY-WITH-INVENTORY-SCRIPT>:"
SRC_URI:append = " file://mender-inventory-custom-attribute"

do_install:append() {
    install -d ${D}/${datadir}/mender/inventory
    install -m 755 ${WORKDIR}/mender-inventory-custom-attribute ${D}/${datadir}/mender/inventory/mender-inventory-custom-attribute
}
```

Replace `<DIRECTORY-WITH-INVENTORY-SCRIPT>` with the path to the `mender-inventory-custom-attribute`
file, relative to the recipe file. The string `custom-attribute` can be replaced with a string of
your choice, as long as the filename starts with `mender-inventory-`.

### Remove the mender-inventory-geolocation script

By default the Mender client installs with the `mender-inventory-geo` script
enabled. To some users this is undesireable, as the script relies on a third
party service for geolocating the device through its IP address. If this is
applicable to you, then disable the script through setting:

```bash
PACKAGECONFIG:remove:pn-mender-client = " inventory-network-scripts"
```

in your `local.conf` file.


## Update Modules

Mender comes with some standard Update Modules available for install, and it's also possible to
install your own custom Update Modules with Yocto.


### Standard Update Modules

Mender comes with some Update Modules available out of the box. These are:

* deb
* directory
* docker
* rpm
* script
* single-file

These Update Modules are available for install, but they are not enabled by default unless you are
building with the demo layer. To enable the standard Update Modules, you need to add the `modules`
entry to the `PACKAGECONFIG` of the `mender-client` recipe. This can be done either by adding your
own `.bbappend` recipe file, or by adding it to `local.conf`. To add it to a recipe file, create
`mender-client_%.bbappend` and add this:

```bash
PACKAGECONFIG:append = " modules"
```

Alternatively, add this to `local.conf`:

```bash
PACKAGECONFIG:append:pn-mender-client = " modules"
```

### Custom Update Modules

In order to include your own custom Update Module, simply augment the `mender-client` recipe and
install the Update Module in the expected folder. For example, create a `mender-client_%.bbappend`
file in your layer, and add this:

```bash
FILESEXTRAPATHS:prepend := "${THISDIR}/<DIRECTORY-WITH-UPDATE-MODULE>:"
SRC_URI:append = " file://custom-update-module"

do_install:append() {
    install -d ${D}/${datadir}/mender/modules/v3
    install -m 755 ${WORKDIR}/custom-update-module ${D}/${datadir}/mender/modules/v3/custom-update-module
}
```

Replace `<DIRECTORY-WITH-UPDATE-MODULE>` with the path to the
`custom-update-module` file, relative to the recipe file. The name,
"custom-update-module", can be any string, and must have the same name as the
payload type used for Artifacts installed with this Update Module.
See [Create a custom update
module](../../06.Artifact-creation/08.Create-a-custom-Update-Module/docs.md)
for more information.


## Delta update support

Delta update support is covered in [its own sub section](01.Delta-update-support/docs.md).


## Add-ons 

### Mender Connect

We do not enable Mender Connect by default, unless you are building with the demo layer.
To enable Mender Connect you can add it either via your own `.bbappend` recipe file,
or via your `local.conf` file.

To add it to a recipe file, create `mender-client_%.bbappend` and add this:

```bash
IMAGE_INSTALL:append = " mender-connect"
```

Alternatively, add the snippet to your `local.conf`.

Mender Connect provides several [configuration
options](../../09.Add-ons/90.Mender-Connect/docs.md#configuration). Set `MENDER_CONNECT_USER` and
`MENDER_CONNECT_SHELL` via your `local.conf` file for `meta-mender` to generate a
`mender-connect.conf` with `User` and `ShellCommand` fields:

```bash
MENDER_CONNECT_USER = "root"
MENDER_CONNECT_SHELL = "/bin/bash"
```

To add optional fields, or override the values for the required ones, create your own `mender-connect.conf` and
augment the `mender-connect` recipe with the new configuration. For example, create a `mender-connect_%.bbappend` file in your layer, and add this:

```bash
FILESEXTRAPATHS:prepend := "${THISDIR}/<DIRECTORY-WITH-MENDER-CONNECT-CONF>:"
SRC_URI:append = " file://mender-connect.conf"

do_install:append() {
    install -m 600 ${WORKDIR}/mender-connect.conf ${D}/${sysconfdir}/mender/mender-connect.conf
}
```

Replace <DIRECTORY-WITH-MENDER-CONNECT-CONF> with the path to the `mender-connect.conf` file, relative to the recipe file.

### Monitor

!!! Note: The Mender Monitor add-on package is required. See the [Mender features page](https://mender.io/product/features?target=_blank) for an overview of all Mender plans and features.

<!--AUTOVERSION: "/mender-monitor/yocto/%/"/monitor-client "/mender-monitor-%.tar.gz"/monitor-client -->
Download the Mender Monitor add-on from
https://downloads.customer.mender.io/content/hosted/mender-monitor/yocto/1.2.1/mender-monitor-1.2.1.tar.gz
and download the tarball to a known location on your local system using your hosted
Mender username and password:

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="hosted"]
<!--AUTOVERSION: "/mender-monitor/yocto/%/"/monitor-client "/mender-monitor-%.tar.gz"/monitor-client -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
curl --fail -u $HOSTED_MENDER_EMAIL -o ${HOME}/mender-monitor-1.2.1.tar.gz https://downloads.customer.mender.io/content/hosted/mender-monitor/yocto/1.2.1/mender-monitor-1.2.1.tar.gz
```
[/ui-tab]
[ui-tab title="enterprise"]
<!--AUTOVERSION: "/mender-monitor/yocto/%/"/monitor-client "/mender-monitor-%.tar.gz"/monitor-client -->
```bash
MENDER_ENTERPRISE_USER=<your.user>
curl --fail -u $MENDER_ENTERPRISE_USER -o ${HOME}/mender-monitor-1.2.1.tar.gz https://downloads.customer.mender.io/content/on-prem/mender-monitor/yocto/1.2.1/mender-monitor-1.2.1.tar.gz
```
[/ui-tab]
[/ui-tabs]

Add the `meta-mender` commercial layer to your build layers:

```bash
bitbake-layers add-layer ../sources/meta-mender/meta-mender-commercial
```

To use Mender Monitor you need to accept its commercial license. If you decide
to accept it, add the following line to your `local.conf`:

```bash
LICENSE_FLAGS_ACCEPTED:append = " commercial_mender-yocto-layer-license"
```

Give the `mender-monitor` recipe the path to the local source code just downloaded:

<!--AUTOVERSION: "/mender-monitor-%.tar.gz"/monitor-client -->
```bash
SRC_URI:pn-mender-monitor = "file://${HOME}/mender-monitor-1.2.1.tar.gz"
```

Then make Mender monitor a part of your image with:

```bash
IMAGE_INSTALL:append = " mender-monitor"
```

Which means your `local.conf` should now contain the following lines:

<!--AUTOVERSION: "/mender-monitor-%.tar.gz"/monitor-client -->
```bash
LICENSE_FLAGS_ACCEPTED:append = " commercial_mender-yocto-layer-license"
SRC_URI:pn-mender-monitor = "file://${HOME}/mender-monitor-1.2.1.tar.gz"
IMAGE_INSTALL:append = " mender-monitor"
```

## mender-gateway

!!!!! Mender Gateway is only available in the Mender Enterprise plan.
!!!!! See [the Mender features page](https://mender.io/product/features?target=_blank)
!!!!! for an overview of all Mender plans and features.

<!--AUTOVERSION: "/mender-gateway/yocto/%/"/mender-gateway "/mender-gateway-%.tar.xz"/mender-gateway -->
Download the Mender Gateway from
https://downloads.customer.mender.io/content/hosted/mender-gateway/yocto/1.0.1/mender-gateway-1.0.1.tar.xz
and download the tarball to a known location on your local system using your hosted
Mender username and password:

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="hosted"]
<!--AUTOVERSION: "/mender-gateway/yocto/%/"/mender-gateway "/mender-gateway-%.tar.xz"/mender-gateway -->
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
curl --fail -u $HOSTED_MENDER_EMAIL -o ${HOME}/mender-gateway-1.0.1.tar.xz https://downloads.customer.mender.io/content/hosted/mender-gateway/yocto/1.0.1/mender-gateway-1.0.1.tar.xz
```
[/ui-tab]
[ui-tab title="enterprise"]
<!--AUTOVERSION: "/mender-gateway/yocto/%/"/mender-gateway "/mender-gateway-%.tar.xz"/mender-gateway -->
```bash
MENDER_ENTERPRISE_USER=<your.user>
curl --fail -u $MENDER_ENTERPRISE_USER -o ${HOME}/mender-gateway-1.0.1.tar.xz https://downloads.customer.mender.io/content/on-prem/mender-gateway/yocto/1.0.1/mender-gateway-1.0.1.tar.xz
```
[/ui-tab]
[/ui-tabs]

Add the `meta-mender` commercial layer to your build layers:

```bash
bitbake-layers add-layer ../sources/meta-mender/meta-mender-commercial
```

To use Mender Monitor you need to accept its commercial license. If you decide
to accept it, add the following line to your `local.conf`:

```bash
LICENSE_FLAGS_ACCEPTED:append = " commercial_mender-yocto-layer-license"
```

Give the `mender-gateway` recipe the path to the local source code just downloaded:

<!--AUTOVERSION: "/mender-gateway-%.tar.xz"/mender-gateway -->
```bash
SRC_URI:pn-mender-gateway = "file://${HOME}/mender-gateway-1.0.1.tar.xz"
```

Then make Mender monitor a part of your image with:

```bash
IMAGE_INSTALL:append = " mender-gateway"
```

Which means your `local.conf` should now contain the following lines:

<!--AUTOVERSION: "/mender-gateway-%.tar.xz"/mender-gateway -->
```bash
LICENSE_FLAGS_ACCEPTED:append = " commercial_mender-yocto-layer-license"
SRC_URI:pn-mender-gateway = "file://${HOME}/mender-gateway-1.0.1.tar.xz"
IMAGE_INSTALL:append = " mender-gateway"
```

### Configuration

To configure `mender-gateway`, create your own `mender-gateway.conf` and
augment the `mender-gateway` recipe with the new configuration. For example, create a `mender-gateway_%.bbappend` file in your layer, and add this:

```bash
FILESEXTRAPATHS:prepend := "${THISDIR}/<DIRECTORY-WITH-MENDER-GATEWAY-CONF>:"
SRC_URI:append = " file://mender-gateway.conf"

do_install:append() {
    install -m 600 ${WORKDIR}/mender-gateway.conf ${D}/${sysconfdir}/mender/mender-gateway.conf
}
```

Replace <DIRECTORY-WITH-MENDER-GATEWAY-CONF> with the path to the `mender-gateway.conf` file, relative to the recipe file.

### Examples package

!!!!! You should not use this package on production devices.

See [Downloads](../../09.Downloads/docs.md#examples-package) for download links for this package.

To integrate it on your Yocto build, add the `meta-mender` demo layer to your build layers:

```bash
bitbake-layers add-layer ../sources/meta-mender/meta-mender-demo
```

Then, append the packae to `mender-gateway` sources:

<!--AUTOVERSION: "/mender-gateway-examples-%.tar"/mender-gateway -->
```bash
SRC_URI:pn-mender-gateway:append = " file:///${HOME}/mender-gateway-examples-1.0.1.tar"
```

This will install the following on your device:
* Self-signed demo certificate and key for `*.docker.mender.io`
* Demo configuration file with `UpstreamServer` configured for `hosted.mender.io`
