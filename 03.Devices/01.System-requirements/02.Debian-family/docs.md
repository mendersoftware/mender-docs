---
title: Debian based family
taxonomy:
    category: docs
---

Currently Mender supports updates Raspbian on Raspberry Pi 3 and Debian on BeagleBone Black. [Mender conversion scripts](https://github.com/mendersoftware/mender-conversion-tools) can transform original system image into image, which fully satisfies all Mender requirements. Mender conversion scripts are tested on Fedora 28. Before scripts are launched it is recommended to install several packages:

```bash
sudo dnf install mtools parted mtd-utils e2fsprogs uboot-tools pigz
```

[Bootloader support section](bootloader-support) provides more information how to install bootloader which supports Mender updates.
