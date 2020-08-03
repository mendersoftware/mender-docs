---
title: Image configuration
taxonomy:
    category: docs
---

## Configuring the image for read-only rootfs

To build an image containing read-only rootfs add the following changes to the `conf/local.conf` file:

```bash
 IMAGE_FEATURES = "read-only-rootfs"
```

You can read more about this feature in the [Yocto Project Mega-Manual - 7.27. Creating a Read-Only Root Filesystem](https://www.yoctoproject.org/docs/latest/mega-manual/mega-manual.html#creating-a-read-only-root-filesystem)

!!! This feature is highly package dependent and even if Mender works correctly when this feature is enabled there might be other packages in your image that expect the root filesystem to be writable and might not function properly. We recommend testing this feature as Mender will gradually move to support read-only root filesystem by default in the future.

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


## Configuring polling intervals

You can configure how frequently the Mender client will make requests to the Mender server
as described in [Polling intervals](../../../03.Client-installation/06.Configuration-file/01.Polling-intervals/docs.md) before
starting the build process.

In order to do this, change the following in the file
`meta-mender/meta-mender-core/recipes-mender/mender/mender_0.1.bb`:

```bash
MENDER_UPDATE_POLL_INTERVAL_SECONDS ?= "1800"
MENDER_INVENTORY_POLL_INTERVAL_SECONDS ?= "28800"
```


## Configuring server address and port

If the client should connect to a different address than the default of `https://docker.mender.io/`, then you should specify this variable in your `local.conf`:

```bash
MENDER_SERVER_URL = "https://my-mender-server.net/"
```

Port numbers can be specified in the same way as you would in a browser, as a colon after the address followed by the number, for example `https://my-mender-server.net:8999/`.

!! Note that the `https` protocol specifier is required in the address. For security reasons, Mender does not support the plaintext `http` protocol.
