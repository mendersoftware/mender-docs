---
title: Yocto Project
taxonomy:
    category: docs
---

!!! Check out the board integrations at [Mender Hub](https://hub.mender.io?target=_blank) to see if your board is already integrated. If you would like professional assistance supporting your board and OS, please refer to the [commercial device support offering](https://mender.io/support-and-services/board-integration?target=_blank).

##Yocto Project
Although it is possible to compile and install Mender independently, we have optimized the installation experience for those who build their Linux images using [Yocto Project](https://www.yoctoproject.org?target=_blank).

Mender's meta layer, [meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank), has several branches that map to given releases of the Yocto Project. However, note that Mender is tested and maintained against the **latest release branch of the Yocto Project** only. Older branches for the Yocto Project are still kept in [meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank), but they might not work seamlessly as they are not continuously tested by Mender. If you need support for older branches we recommend subscribing to [Mender commercial software support](https://mender.io/support-and-services/software-support?target=_blank).

