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

You can read more about this feature in the [Yocto Project Mega-Manual - 7.27.
Creating a Read-Only Root
Filesystem](https://www.yoctoproject.org/docs/latest/mega-manual/mega-manual.html#creating-a-read-only-root-filesystem?target=_blank)

!!! This feature is highly package dependent and even though Mender works
!!! correctly with this feature enabled, there might be other packages in your
!!! image that expect the root filesystem to be writable and might not function
!!! properly.
