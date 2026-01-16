---
title: Manual package installation
taxonomy:
    category: docs
    label: tutorial
---

In some cases it might be necessary to manually install Debian packages. This is particularly useful in restricted locations where `downloads.mender.io` is inaccessible, such as:

- Networks in regions with restricted internet access
- Air-gapped or offline environments

By default, `mender-convert` automatically downloads and installs Mender packages (such as `mender-auth`, and `mender-update`) from the `https://downloads.mender.io/repos/device-components/pool/main/m/` repository.
If this repository is not accessible in your environment, you can disable the automatic installation and provide the packages manually.

## Configuration

### Step 1: Disable automatic package installation

Ensure that you have disabled the automatic installation of Mender packages.
By default, only `MENDER_CLIENT_INSTALL` is enabled. 

```bash
# Disable automatic installation of mender-auth and mender-update
echo 'MENDER_CLIENT_INSTALL=n' >> configs/custom_config
```

!!!!! Note that some of our pre-defined configs have dependencies downloaded from `downloads.mender.io`.

### Step 2: Place packages in the input directory

Create a directory for your packages and copy the `.deb` files there:

```bash
mkdir -p input/deb
cp /path/to/your/packages/*.deb input/deb/
```

### Step 3: Enable manual package installation

Add the following configuration to your config file:

```bash
echo 'MENDER_INSTALL_INPUT_PACKAGES=y' >> configs/custom_config
```

```bash
echo 'MENDER_INSTALL_INPUT_PACKAGES_PATH=input/deb' >> configs/custom_config
```

### Step 4: Run mender-convert
To use the config defined in `configs/custom_config`, you must include
`--config configs/custom_config` as an argument when running mender-convert.

!!!! See [Customization](../../02.Convert-a-Mender-Debian-image/01.Customization) for more information.
