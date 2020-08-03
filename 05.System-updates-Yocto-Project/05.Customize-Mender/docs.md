---
title: Customize Mender
taxonomy:
    category: docs
---


## Configuring server address and port

If the client should connect to a different address than the default of `https://docker.mender.io/`, then you should specify this variable in your `local.conf`:

```bash
MENDER_SERVER_URL = "https://my-mender-server.net/"
```

Port numbers can be specified in the same way as you would in a browser, as a colon after the address followed by the number, for example `https://my-mender-server.net:8999/`.

!! Note that the `https` protocol specifier is required in the address. For security reasons, Mender does not support the plaintext `http` protocol.


## Configuring polling intervals

You can configure how frequently the Mender client will make requests to the Mender server
as described in [Polling intervals](../../../05.Client-configuration/05.Configuration-file/01.Polling-intervals/docs.md) before
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
FILESEXTRAPATHS_prepend := "${THISDIR}/<DIRECTORY-WITH-MENDER-CONF>"
SRC_URI_append = " file://mender.conf"
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
MENDER_FEATURES_DISABLE_append = " mender-systemd"
```

Also, you do not need any daemon-related configuration items in your `local.conf` as outlined in [the section on configuring the Yocto Project build](../../../04.Artifacts/10.Yocto-project/01.Building/docs.md#configuring-the-build).

! If you disable Mender running as a daemon under `systemd`, you must run all required Mender commands from the CLI or scripts. Most notably, you need to run `mender -commit` after booting into and verifying a successful deployment. When running in managed mode, any pending `mender -commit` will automatically be run by the Mender daemon after it starts. See [Modes of operation](../../../02.Overview/01.Introduction/docs.md#client-modes-of-operation) for more information about the difference.


## Identity

In order to include an identity script, simply augment the `mender-client` recipe and install the
script in the expected folder. For example, create a `mender-client_%.bbappend` file in your layer,
and add this:

```bash
FILESEXTRAPATHS_prepend := "${THISDIR}/<DIRECTORY-WITH-IDENTITY-SCRIPT>"
SRC_URI_append = " file://mender-device-identity"

do_install_append() {
    install -d ${datadir}/mender/identity
    install -m 755 ${WORKDIR}/mender-device-identity ${datadir}/mender/identity/mender-device-identity
}
```

Replace `<DIRECTORY-WITH-IDENTITY-SCRIPT>` with the path to the `mender-device-identity` file, relative to the
recipe file.


## Inventory

In order to include an inventory script, simply augment the `mender-client` recipe and install the
script in the expected folder. For example, create a `mender-client_%.bbappend` file in your layer,
and add this:

```bash
FILESEXTRAPATHS_prepend := "${THISDIR}/<DIRECTORY-WITH-INVENTORY-SCRIPT>"
SRC_URI_append = " file://mender-inventory-custom-attribute"

do_install_append() {
    install -d ${datadir}/mender/inventory
    install -m 755 ${WORKDIR}/mender-inventory-custom-attribute ${datadir}/mender/inventory/mender-inventory-custom-attribute
}
```

Replace `<DIRECTORY-WITH-INVENTORY-SCRIPT>` with the path to the `mender-inventory-custom-attribute`
file, relative to the recipe file. The string `custom-attribute` can be replaced with a string of
your choice, as long as the filename starts with `mender-inventory-`.


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
PACKAGECONFIG_append = " modules"
```

Alternatively, add this to `local.conf`:

```bash
PACKAGECONFIG_append_pn-mender-client = " modules"
```

### Custom Update Modules

In order to include your own custom Update Module, simply augment the `mender-client` recipe and
install the Update Module in the expected folder. For example, create a `mender-client_%.bbappend`
file in your layer, and add this:

```bash
FILESEXTRAPATHS_prepend := "${THISDIR}/<DIRECTORY-WITH-UPDATE-MODULE>"
SRC_URI_append = " file://custom-update-module"

do_install_append() {
    install -d ${datadir}/mender/modules/v3
    install -m 755 ${WORKDIR}/custom-update-module ${datadir}/mender/modules/v3/custom-update-module
}
```

Replace `<DIRECTORY-WITH-UPDATE-MODULE>` with the path to the `custom-update-module` file, relative
to the recipe file. The name, custom-update-module, can be any string, and must be set to the name
of the payload type that will be used for Artifacts that will be installed with this Update
Module. See [Create a custom update module](../../artifact-creation/create-a-custom-update-module)
for more information.


## Delta update support

Delta update support is covered in [its own sub section](delta-update-support).
