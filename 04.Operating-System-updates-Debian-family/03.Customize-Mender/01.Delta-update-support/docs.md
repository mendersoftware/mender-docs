---
title: Delta update support
taxonomy:
    category: docs
    label: tutorial
---

! Please note we provide these manual steps as an example only for creating Delta images on Debian-based distros.
! For a delta integration tested in our pipelines, please use Yocto to generate your images with delta.

You have access to robust delta updates if you are using [Mender Professional](https://mender.io/product/features?target=_blank) or
[Mender Enterprise](https://mender.io/product/features?target=_blank). This section describes how to enable delta updates on your devices by installing the `mender-binary-delta` Update Module with your Yocto Project build.

Once your devices support installing delta updates, see [Create a Delta update Artifact](../../../06.Artifact-creation/05.Create-a-Delta-update-Artifact/docs.md) for a tutorial on creating a delta update from two Operating System updates.

## Prerequisites

To use delta update, you must be using a read-only root filesystem. There are several ways of achieving this, which is out of this tutorial's scope. Generally speaking, ensure the bootloader and the `/etc/fstab` don't contain any `rw` reference.

You will need the binaries from the downloaded content both on the host and the device.
More information on where to place every file in the sections below.

For additional troubleshooting, you can check the [Delta updates troubleshooting guide](../../../301.Troubleshoot/03.Mender-Client/docs.md#delta-updates).

## Download

Download the `mender-binary-delta` binaries following the [instructions](../../../10.Downloads/docs.md#mender-binary-delta).

## Integrate `mender-binary-delta` into your image

Delta updates require the `mender-binary-delta` Update Module and the configuration file (`mender-binary-delta.conf`) on the device side. The steps on how to achieve this will depend on the way you're generating the image. We'll present only the location where you need to place the files.

Copy the `mender-binary-delta` binary into `/usr/share/mender/modules/v3/` on your device from the content you downloaded in the [previous step](#download). Please ensure you're copying the binary from the directory specifying your architecture.

The `mender-binary-delta.conf` is a configuration on the device telling the update module the location of A/B partitions. It must be generated and placed in `/etc/mender/mender-binary-delta.conf`.

The content of the `mender-binary-delta.conf` configuration file is case-dependent. Below is an example of how it might look, but you might need different `/dev/*` locations depending on your device's name:

```json
{
  "RootfsPartA": "/dev/mmcblk0p2",
  "RootfsPartB": "/dev/mmcblk0p3"
}
```

## Next steps

For information on creating Delta update Artifacts, see [Create a Delta update Artifact](../../../06.Artifact-creation/05.Create-a-Delta-update-Artifact/docs.md).

For more information about delta updates, including how to deploy them, as well as troubleshooting, see the [Mender Hub page about `mender-binary-delta`](https://hub.mender.io/t/robust-delta-update-rootfs/1144?target=_blank).
