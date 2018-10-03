---
title: Bootloader support
taxonomy:
    category: docs
---

Currently [mender-convert](https://github.com/mendersoftware/mender-conversion-tools?target=_blank) uses a modified U-Boot for Raspbian and an unmodified GRUB for Debian on Beaglebone. Choosing a different bootloader is not supported.

These scripts require bootloader installation after repartitioning of original system image. To install the correct bootloader, execute the following:

```bash
git clone https://github.com/mendersoftware/mender-conversion-tools.git
./mender-conversion-tool.sh make_sdimg --image <output_image_file_name> --embedded <original_image_file_path> --size-data <size_of_data_partition_in_MB> --device-type <beaglebone/raspberrypi3>
./mender-conversion-tool.sh install_bootloader --image <sdimg_file_path>  --device-type <beaglebone/raspberrypi3> --toolchain <toolchain name e.g. arm-linux-gnueabihf>
```

The `./mender-conversion-tool.sh make_sdimg` command is responsible for adjusting the partition layout of an original image according to Mender needs. The [partition layout section](../../general-system-requirements#partition-layout) explains Mender's requirements for partition layout in detail.
