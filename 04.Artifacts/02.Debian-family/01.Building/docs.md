---
title: Building a Mender Debian image
taxonomy:
    category: docs
---

Mender provides a tool for converting existing binary OS images for use with Mender. These tools are available in a [github repository](https://github.com/mendersoftware/mender-conversion-tools/).

Execute the following on an Ubuntu host OS to install the prerequisites for these scripts:

```bash
sudo apt install mtools parted mtd-utils e2fsprogs u-boot-tools pigz
```

Execute the following to convert an existing image into a Mender-enabled image:

```bash
git clone https://github.com/mendersoftware/mender-conversion-tools.git
cd mender-conversion-tools
./mender-conversion-tool.sh make_all --embedded <original_debian_image> --image <output_image_name> --mender <mender_binary_path> --artifact <name_of_the_artifact>  --demo-ip <ip_of_demo_server> --toolchain <path_to_toolchain>
```

This command will generate an image compliant with Mender requirements.

The above invocation will configure your image for use with the [Mender demo environment](../../../getting-started/create-a-test-environment). 

See [the next chapter](../image-configuration) for details on configuring your images for [Hosted Mender](https://hosted.mender.io) or a [production installation](../../../administration/production-installation).
