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


## Download `mender-binary-delta`

If you are using *hosted Mender*, download the `mender-binary-delta` archive with the following
command:

<!--AUTOVERSION: "mender-binary-delta/%/mender-binary-delta-%.tar"/mender-binary-delta-->
```bash
HOSTED_MENDER_EMAIL="myusername@example.com"
curl -u $HOSTED_MENDER_EMAIL -O https://downloads.customer.mender.io/content/hosted/mender-binary-delta/1.4.1/mender-binary-delta-1.4.1.tar.xz
```

Replace the value of `HOSTED_MENDER_EMAIL` with the email address you used to sign up on *hosted Mender*, then enter your hosted Mender password when prompted to proceed.
**NOTE**: if you signed up using your Google or GitHub login, use the email address linked to that account and enter `x` as the password.

On the other hand, if you are using *on-premise Mender Enterprise*, download using the following
command:

<!--AUTOVERSION: "mender-binary-delta/%/mender-binary-delta-%.tar"/mender-binary-delta-->
```bash
MENDER_ENTERPRISE_USER=<your.user>
curl -u $MENDER_ENTERPRISE_USER -O https://downloads.customer.mender.io/content/on-prem/mender-binary-delta/1.4.1/mender-binary-delta-1.4.1.tar.xz
```


## Unpack `mender-binary-delta-generator`

<!--AUTOVERSION: "mender-binary-delta-%.tar.xz"/mender-binary-delta-->
The archive `mender-binary-delta-1.4.1.tar.xz` contains the binaries needed to generate and apply
deltas.

Change directory to `$HOME`:

```bash
cd ${HOME}
```

<!--AUTOVERSION: "mender-binary-delta-%.tar.xz"/mender-binary-delta-->
Unpack the `mender-binary-delta-1.4.1.tar.xz` in your home directory:

<!--AUTOVERSION: "mender-binary-delta-%.tar.xz"/mender-binary-delta-->
```bash
tar xvf mender-binary-delta-1.4.1.tar.xz
```

We only need the generator, so copy it to `/usr/bin`:

<!--AUTOVERSION: "mender-binary-delta-%"/mender-binary-delta-->
```
sudo cp mender-binary-delta-1.4.1/x86_64/mender-binary-delta-generator /usr/bin
```

Then delete the rest of the unpacked files:

<!--AUTOVERSION: "mender-binary-delta-%"/mender-binary-delta-->
```
rm -rf mender-binary-delta-1.4.1
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

IMAGE_INSTALL:append = " mender-binary-delta"
LICENSE_FLAGS_ACCEPTED:append = " commercial_mender-yocto-layer-license"
SRC_URI:pn-mender-binary-delta = "file://${HOME}/mender-binary-delta-1.4.1.tar.xz"

EOF
```

<!--AUTOVERSION: "older than %, such as % or older"/ignore-->
!!! If you are using a Yocto branch older than kirkstone, such as dunfell or older, you need slightly altered steps to use mender-binary-delta. See [the mender-binary-delta section on Mender Hub](https://hub.mender.io/t/robust-delta-update-rootfs/1144) for more information about this.

## Next steps

For information on how to create delta update Artifacts, see [Create a Delta update Artifact](../../../06.Artifact-creation/05.Create-a-Delta-update-Artifact/docs.md).

For more information about delta updates, including how to deploy them, as well as troubleshooting, see the
[Mender Hub page about `mender-binary-delta`](https://hub.mender.io/t/robust-delta-update-rootfs/1144?target=_blank).
