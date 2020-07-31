---
title: Read-only root filesystem
taxonomy:
    category: docs
---

## Configuring the image for read-only rootfs

To build an image containing read-only rootfs add the following changes to the `conf/local.conf` file:

```bash
IMAGE_FEATURES += "read-only-rootfs"
```

You can read more about this feature in the [Yocto Project Mega-Manual - 7.27. Creating a Read-Only Root Filesystem](https://www.yoctoproject.org/docs/latest/mega-manual/mega-manual.html#creating-a-read-only-root-filesystem?target=_blank)

!!! This feature is highly package dependent and even if Mender works correctly when this feature is enabled there might be other packages in your image that expect the root filesystem to be writable and might not function properly. We recommend testing this feature as Mender will gradually move to support read-only root filesystem by default in the future.
