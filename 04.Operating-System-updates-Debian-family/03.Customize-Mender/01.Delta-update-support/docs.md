---
title: Delta update support
taxonomy:
    category: docs
    label: tutorial
---

! Please note that these manual steps are provided as an example only for creating Delta images on Debian based distros.
! For a delta integration that is tested in our pipelines, please use Yocto as means to generate your images with delta. 

If you are using [Mender Professional](https://mender.io/product/features?target=_blank) or [Mender
Enterprise](https://mender.io/product/features?target=_blank), you have access to robust delta updates. In this section we describe how to enable delta updates on your devices,  by installing the `mender-binary-delta` Update Module with your Yocto Project build.

Once your devices support installing delta updates, see [Create a Delta update Artifact](../../../06.Artifact-creation/05.Create-a-Delta-update-Artifact/docs.md) for a tutorial on how to create a delta update from two Operating System updates.

## Prerequisites

In order to use delta update, you must be using a read-only root filesystem. There are several ways of achiving this and it is out of the scope of this tutorial. Generally speaking, just make sure the bootloader and the `/etc/fstab` don't contain any `rw` reference.

In the sections below we will be adding files to the host as well as the device.
The binaries from the downloaded content will also be used on the host as well as the device.


For additional troubleshooting, you can check the [Delta updates troubleshoot guide](../../../301.Troubleshoot/03.Mender-Client/docs.md#delta-updates).

## Download `mender-binary-delta`

If you are using *Hosted Mender*, download the `mender-binary-delta` archive with the following
command:

<!--AUTOVERSION: "mender-binary-delta/%/mender-binary-delta-%.tar"/mender-binary-delta-->
```bash
HOSTED_MENDER_EMAIL="myusername@example.com"
curl -u $HOSTED_MENDER_EMAIL -O https://downloads.customer.mender.io/content/hosted/mender-binary-delta/1.4.1/mender-binary-delta-1.4.1.tar.xz
```

Replace the value of `HOSTED_MENDER_EMAIL` with the email address you used to sign up on *hosted Mender*, then enter your hosted Mender password when prompted to proceed.

!!! If you signed up using your Google or GitHub login, use the email address linked to that account and enter `x` as the password.

On the other hand, if you are using *on-premise Mender Enterprise*, download using the following
command:

<!--AUTOVERSION: "mender-binary-delta/%/mender-binary-delta-%.tar"/mender-binary-delta-->
```bash
MENDER_ENTERPRISE_USER=<your.user>
curl -u $MENDER_ENTERPRISE_USER -O https://downloads.customer.mender.io/content/on-prem/mender-binary-delta/1.4.1/mender-binary-delta-1.4.1.tar.xz
```


<!--AUTOVERSION: "mender-binary-delta-%.tar.xz"/mender-binary-delta-->
The archive `mender-binary-delta-1.4.1.tar.xz` contains the binaries needed to generate and apply deltas.

<!--AUTOVERSION: "mender-binary-delta-%.tar.xz"/mender-binary-delta-->
Unpack the `mender-binary-delta-1.4.1.tar.xz` in your home directory:

<!--AUTOVERSION: "mender-binary-delta-%.tar.xz"/mender-binary-delta-->
```bash
tar xvf mender-binary-delta-1.4.1.tar.xz
```

The file structure should look like this:

```
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

It is assumed that you will need this on the host to [create a delta between two artifacts](../../../06.Artifact-creation/05.Create-a-Delta-update-Artifact/docs.md).


Copy the generator compatible with your workstation architecture to `/usr/bin`, for a `x86_64` one, it should look like this:

<!--AUTOVERSION: "mender-binary-delta-%"/mender-binary-delta-->
```
sudo cp mender-binary-delta-1.4.1/x86_64/mender-binary-delta-generator /usr/bin
```

!!! The enterprise plan allows auto generation of [delta images directly on the mender server](../../../06.Artifact-creation/05.Server-side-generation-of-Delta-Artifacts/docs.md).

### Integrate `mender-binary-delta` into your image

On the device side Delta updates require the `mender-binary-delta` Update Module and the configuration file (`mender-binary-delta.conf`). The steps on how to achieve this will depend on the way you're generating the image. We'll present only the location where the files need to be placed.

From the content you downloaded in the [previous step](#download-mender-binary-delta) copy the `mender-binary-delta` binary it into `/usr/share/mender/modules/v3/` on your device. Please make sure you're copying the binary from the directory specifying your architecture.


The `mender-binary-delta.conf` is a configuration on the device telling the update module the location of A/B partitions. It needs to be generated and placed in `/etc/mender/mender-binary-delta.conf`.

The content of the cnfiguration file is case dependent.
Below is an example on how it might look, but depending on your device names other locations might be needed.

Example `mender-binary-delta.conf` 
```
{
  "RootfsPartA": "/dev/mmcblk0p2",
  "RootfsPartB": "/dev/mmcblk0p3"
}
```

## Next steps

For information on how to create delta update Artifacts, see [Create a Delta update Artifact](../../../06.Artifact-creation/05.Create-a-Delta-update-Artifact/docs.md).

For more information about delta updates, including how to deploy them, as well as troubleshooting, see the
[Mender Hub page about `mender-binary-delta`](https://hub.mender.io/t/robust-delta-update-rootfs/1144?target=_blank).
