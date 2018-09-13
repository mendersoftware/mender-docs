---
title: Building a Mender Debian image
taxonomy:
    category: docs
---

Mender provides a tool for converting Beaglebone Debian and Raspbian images. Proper tools are available on [Mender repository](https://github.com/mendersoftware/mender-conversion-tools/). It is possible to convert an existing image into a Mender image by using the following commands:

```bash
git clone https://github.com/mendersoftware/mender-conversion-tools.git
cd mender-conversion-tools
./mender-conversion-tool.sh make_all --embedded <original_debian_image> --image <output_image_name> --mender <mender_binary_path> --artifact <name_of_the_artifact>  --demo-ip <ip_of_demo_server> --toolchain <path_to_toolchain>
```

This command will generate an image compliant with Mender requirements. This script will install demo certificate. [Next chapter](../../Image-configuration/02.debian-image-configuration) provides hints on how to setup image conversion tool for production requirements.
