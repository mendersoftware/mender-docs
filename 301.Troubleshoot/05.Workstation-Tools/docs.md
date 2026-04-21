---
title: Workstation Tools
taxonomy:
    category: docs
---

This document details troubleshooting steps for common problems with Mender workstation tools (`mender-artifact` and `mender-cli`).

## mender-artifact

### Error: `flag provided but not defined: -c`

<!--AUTOVERSION: "introduced in version %"/mender-artifact "e.g. %"/ignore-->
The `-c` flag for `mender-artifact` was introduced in version 4.3.0. If you are using an older version (e.g. 3.9.0 from the default Ubuntu 24.04/Noble repository), you will see this error when trying to use the `-c` flag.

**Solutions:**

1. **Use the legacy `-t` flag instead of `-c`** in your commands. For example:
   ```bash
   mender-artifact write rootfs-image -t device-type -n artifact-name ...
   ```

<!--AUTOVERSION: "version %"/mender-artifact-->
2. **Upgrade to the latest version** by following the [installation instructions](../../12.Downloads/01.Workstation-tools/docs.md) or [manually downloading the binary](../../12.Downloads/01.Workstation-tools/docs.md#mender-artifact).

### Error: `/bin/sh: 1: mender: not found`

<!--AUTOVERSION: "version older than %"/mender-artifact-->
This error occurs when using `mender-artifact` version older than 4.0.0 with Mender 4.0+ devices. The older `mender-artifact` versions are incompatible with the newer device client.

**Solution:**

<!--AUTOVERSION: "version %"/mender-artifact-->
Upgrade your `mender-artifact` to version 4.0.0 or later by following the [installation instructions](../../12.Downloads/01.Workstation-tools/docs.md).

### Verify your installation

To check which version of `mender-artifact` you have installed:

```bash
mender-artifact --version
```

<!--AUTOVERSION: "recommended version is %"/mender-artifact-->
The recommended version is 4.3.0 or later for full compatibility with current documentation examples.

## mender-cli

### Verify your installation

To check which version of `mender-cli` you have installed:

```bash
mender-cli --version
```

For installation and upgrade instructions, see [Workstation Tools](../../12.Downloads/01.Workstation-tools/docs.md).
