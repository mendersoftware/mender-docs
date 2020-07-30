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

This is simple to accomplish by adding a `recipes-mender/mender/mender_%.bbappend` file in your Yocto Project layer, with the following content:

```bash
SYSTEMD_AUTO_ENABLE = "disable"
```

In this case it is also possible to avoid Mender's current dependency on systemd. If you do not wish to enable systemd in your build, add the following to `local.conf`:

```bash
MENDER_FEATURES_DISABLE_append = " mender-systemd"
```

Also, you do not need any daemon-related configuration items in your `local.conf` as outlined in [the section on configuring the Yocto Project build](../../../04.Artifacts/10.Yocto-project/01.Building/docs.md#configuring-the-build).

! If you disable Mender running as a daemon under `systemd`, you must run all required Mender commands from the CLI or scripts. Most notably, you need to run `mender -commit` after booting into and verifying a successful deployment. When running in managed mode, any pending `mender -commit` will automatically be run by the Mender daemon after it starts. See [Modes of operation](../../../02.Overview/01.Introduction/docs.md#client-modes-of-operation) for more information about the difference.
