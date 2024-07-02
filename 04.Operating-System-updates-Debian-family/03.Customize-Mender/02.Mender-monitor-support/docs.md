---
title: Mender-monitor support
taxonomy:
    category: docs
    label: tutorial
---

!!!!! It is required to have the _Mender Monitor_ add-on enabled in your account.
!!!!! See [the Mender features page](https://mender.io/product/features?target=_blank)
!!!!! for an overview of all Mender plans and features.

## Download

Download the Mender Monitor Debian package following the [instructions](../../../10.Downloads/docs.md#monitor).

## Installing `mender-monitor` in the converted image

To install `mender-monitor` in an image using `mender-convert`, you will need to copy the Mender Monitor Debian package you downloaded in the [previous step](#download) into a specific directory.

The default directory for input packages is `input/deb`, but you can change it like this:

```bash
echo 'MENDER_INSTALL_INPUT_PACKAGES_PATH=/path/to/deb_packages' >> configs/custom_config
```

Then you will need to enable the installation of input packages:

```bash
echo 'MENDER_INSTALL_INPUT_PACKAGES=y' >> configs/custom_config
```

Since you've set the variables in `configs/custom_config`, you will need to
explicitly pass this file with the `--config` option when running `docker-mender-convert` as described [here](../../02.Convert-a-Mender-Debian-image/01.Customization/docs.md#configuration-files).

When running the `mender-convert` tool, you should see something like this in the output:

```
2024-06-19 13:10:34 [INFO] [mender-convert-modify] Installing input/deb/mender-monitor.deb
2024-06-19 13:10:34 [INFO] [mender-convert-modify] Installing dependencies for mender-convert/input/deb/mender-monitor.deb
```
