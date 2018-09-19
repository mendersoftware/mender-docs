---
title: Debian bootloader support
taxonomy:
    category: docs
---

Currently [Mender conversion scripts](https://github.com/mendersoftware/mender-conversion-tools) use patched U-Boot for Raspbian and GRUB for Debian on Beaglebone. Mender scripts do not provide an opportunity to choose bootloader.

Mender scripts require that bootloader installation is done after repartitioning of original system image. To install correct bootloader, execute the following script:

```bash
git clone https://github.com/mendersoftware/mender-conversion-tools.git
./mender-conversion-tool.sh make_sdimg --image <output_image_file_name> --embedded <original_image_file_path> --size-data <size_of_data_partition_in_MB> --device-type <beaglebone/raspberrypi3>
./mender-conversion-tool.sh install_bootloader --image <sdimg_file_path>  --device-type <beaglebone/raspberrypi3> --toolchain <toolchaain name e.g. arm-linux-gnueabihf>
```

The `./mender-conversion-tool.sh make_sdimg` command is responsible for adjusting the partition layout of an original image according to Mender needs. The [partition layout section](../../../partition-layout) explains Mender's requirements for partition layout in details.
