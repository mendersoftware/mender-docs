---
title: Delta update support
taxonomy:
    category: docs
    label: tutorial
---


If you are using [Mender Professional](https://mender.io/product/features?target=_blank) or [Mender
Enterprise](https://mender.io/product/features?target=_blank), you have access to robust delta updates. In this section we describe how to enable support for delta updates on your devices,  by installing the `mender-binary-delta` Update Module with your Yocto Project build.

Once your devices support installing delta updates, see [Create a Delta update Artifact](../../../06.Artifact-creation/05.Create-a-Delta-update-Artifact/docs.md) for a tutorial on how to create a delta update from two Operating System updates.

## Prerequisites

In order to use delta update, you must be using a read-only root filesystem. For details on how to
enable this, see the [Read only root
filesystem](../../04.Image-customization/02.Read-only-root-filesystem/) section.

## Download

Download the `mender-binary-delta` binaries following the [instructions](../../../10.Downloads/docs.md#mender-binary-delta).

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

IMAGE_INSTALL:append = " mender-binary-delta"
LICENSE_FLAGS_ACCEPTED:append = " commercial_mender-yocto-layer-license"
SRC_URI:pn-mender-binary-delta = "file://${HOME}/mender-binary-delta-1.5.1.tar.xz"

EOF
```

<!--AUTOVERSION: "older than %, such as % or older"/ignore-->
!!! If you are using a Yocto branch older than kirkstone, such as dunfell or older, you need slightly altered steps to use mender-binary-delta. See [the mender-binary-delta section on Mender Hub](https://hub.mender.io/t/robust-delta-update-rootfs/1144) for more information about this.

## Next steps

For information on how to create delta update Artifacts, see [Create a Delta update Artifact](../../../06.Artifact-creation/05.Create-a-Delta-update-Artifact/docs.md).

For more information about delta updates, including how to deploy them, as well as troubleshooting, see the
[Mender Hub page about `mender-binary-delta`](https://hub.mender.io/t/robust-delta-update-rootfs/1144?target=_blank).
