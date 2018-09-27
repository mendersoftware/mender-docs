---
title: Debian family
taxonomy:
    category: docs
---

Currently Mender supports updating Debian-based systems, including Raspbian and Ubuntu. The [Mender conversion scripts](https://github.com/mendersoftware/mender-conversion-tools) can transform a system image into an image which fully satisfies all Mender requirements. These scripts have been tested on Ubuntu 18.04.  Other desktop distributions will likely work as the requirements on the host OS are minimal. Install the following packages on your Ubuntu system before invoking the Mender conversion scripts:

```bash
sudo apt install mtools parted mtd-utils e2fsprogs u-boot-tools pigz
```

The [Bootloader support section](bootloader-support) provides more information for installing a bootloader which supports Mender updates.
