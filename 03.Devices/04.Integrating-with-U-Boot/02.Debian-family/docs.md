---
title: Debian integration with U-Boot
taxonomy:
    category: docs
---

[Mender conversion scripts](https://github.com/mendersoftware/mender-conversion-tools) provide script for building and installing patched U-Boot for Raspbian. Currently only patched U-Boot is supported by Mender on RaspberryPi 3. This command will install bootloader on disk image with partition layout compliant with Mender requirements.

```bash
 ./mender-conversion-tool.sh install_bootloader --image <sdimg_file_path> --device-type raspberrypi3 --toolchain <toolchain_name e.g. arm-linux-gnueabihf>
```
