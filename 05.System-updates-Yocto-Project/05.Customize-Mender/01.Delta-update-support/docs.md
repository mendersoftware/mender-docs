---
title: Delta update support
taxonomy:
    category: docs
---


If you are using [Mender Professional](https://mender.io/plans?target=_blank) or [Mender
Enterprise](https://mender.io/plans?target=_blank), you have access to robust delta updates. In this
section we describe the install procedure for the `mender-binary-delta` Update Module, using Yocto,
but we do not cover everything which is needed to use delta updates. For a more complete reference,
including how to create delta Artifacts, please go to the [Mender Hub page about
`mender-binary-delta`](https://hub.mender.io/t/robust-delta-update-rootfs/1144?target=_blank).


## Prerequisites

In order to use delta update, you must be using a read-only root filesystem. For details on how to
enable this, see the [Read only root
filesystem](../../04.Image-customization/02.Read-only-root-filesystem/) section.


## Download `mender-binary-delta`

If you are using *hosted Mender*, download the `mender-binary-delta` archive with the following
command:

<!--AUTOVERSION: "mender-binary-delta/%/mender-binary-delta-%.tar"/mender-binary-delta-->
```bash
HOSTED_MENDER_EMAIL="myusername@example.com"
curl -u $HOSTED_MENDER_EMAIL -O https://download.mender.io/hosted/content/mender-binary-delta/1.1.0/mender-binary-delta-1.1.0.tar.xz
```

On the other hand, if you are using *on-premise Mender Enterprise*, download using the following
command:

<!--AUTOVERSION: "mender-binary-delta/%/mender-binary-delta-%.tar"/mender-binary-delta-->
```bash
MENDER_ENTERPRISE_EMAIL="myusername@example.com"
curl -u $MENDER_ENTERPRISE_EMAIL -O https://download.mender.io/content/mender-binary-delta/1.1.0/mender-binary-delta-1.1.0.tar.xz
```


## Unpack `mender-binary-delta`

<!--AUTOVERSION: "mender-binary-delta-%.tar.xz"/mender-binary-delta-->
The archive `mender-binary-delta-1.1.0.tar.xz` contains the binaries needed to generate and apply
deltas.

Change directory to `$HOME`:

```bash
cd ${HOME}
```

<!--AUTOVERSION: "mender-binary-delta-%.tar.xz"/mender-binary-delta-->
Unpack the `mender-binary-delta-1.1.0.tar.xz` in your home directory:

<!--AUTOVERSION: "mender-binary-delta-%.tar.xz"/mender-binary-delta-->
```bash
tar xvf mender-binary-delta-1.1.0.tar.xz
```


## Integrate `mender-binary-delta` into the Yocto environment

Add `meta-mender-commerical` layer to your Yocto environment:


```bash
bitbake-layers add-layer ../sources/meta-mender/meta-mender-commercial
```

Add the following your `local.conf` to include `mender-binary-delta` in your build:

<!--AUTOVERSION: "mender-binary-delta-%"/mender-binary-delta-->
```bash
cat <<EOF >> conf/local.conf
# Customizations for Mender delta-update support

IMAGE_INSTALL_append = " mender-binary-delta"
LICENSE_FLAGS_WHITELIST_append = " commercial_mender-binary-delta"
FILESEXTRAPATHS_prepend_pn-mender-binary-delta := "${HOME}/mender-binary-delta-1.1.0/:"

EOF
```

! The trailing `:` in `FILESEXTRAPATHS_prepend_pn-mender-binary-delta` is intentional and
! important to have in place.


## Next steps

For more information about delta updates, including how to create delta Artifacts, how to deploy
them, as well as Troubleshooting, see the [Mender Hub page about
`mender-binary-delta`](https://hub.mender.io/t/robust-delta-update-rootfs/1144?target=_blank).
