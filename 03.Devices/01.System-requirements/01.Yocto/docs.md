---
title: Yocto
taxonomy:
    category: docs
---

!!! Mender has four reference boards already integrated: [Raspberry Pi 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b?target=_blank), [BeagleBone Black](https://beagleboard.org/black?target=_blank) and two virtual devices (`qemux86-64` and `vexpress-qemu`). If you would like assistance supporting your device and OS, please refer to the [commercial device support offering](https://mender.io/product/board-support?target=_blank).

##Yocto Project
Although it is possible to compile and install Mender independently, we have optimized the installation experience for those who build their Linux images using [Yocto Project](https://www.yoctoproject.org?target=_blank).

Mender's meta layer, [meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank), has several branches that map to given releases of the Yocto Project. However, note that Mender is tested and maintained against the **latest release branch of the Yocto Project** only. Older branches for the Yocto Project are still kept in [meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank), but they might not work seamlessly as they are not continuously tested by Mender. If you need support for older branches we recommend subscribing to [Mender commercial software support](https://mender.io/product/software-support?target=_blank).

### Other build systems

Mender has no official support for other build systems. However, by following the right steps, it is possible to adapt other build systems to Mender's needs. Please see [this blog post](https://mender.io/blog/porting-mender-to-a-non-yocto-build-system) for an example (note that some of Mender's needs may have changed since the blog post was made).

