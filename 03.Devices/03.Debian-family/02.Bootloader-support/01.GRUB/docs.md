---
title: GRUB
taxonomy:
    category: docs
---

The [mender-convert](https://github.com/mendersoftware/mender-conversion-tools) tools uses GRUB as second stage bootloader for Debian on Beaglebone. This tool build GRUB from the [official repository](https://www.gnu.org/software/grub/grub-download.html). Mender does not require any patches for GRUB and should be built with EFI platform support. Execute the following to install the GRUB bootloader into a disk image with partition layout compliant with Mender requirements:

```bash
 ./mender-conversion-tool.sh install_bootloader --image <sdimg_file_path> --device-type beaglebone --toolchain <cross_compiler_name e.g. arm-linux-gnueabihf>
```

Mender updates require also some Mender specific files. These files are strongly connected with bootloader and they are responsible for the updates management. The command below will install all necessary files. It requires compiled Mender client application. Mender provides [tools for cross compilation of the client binary.](https://github.com/mendersoftware/mender-crossbuild)

```bash
./mender-conversion-tool.sh install_mender --image <sdimg_file_path> --device-type beaglebone --artifact <name_of_artifact> --server <server_address_ip> --mender <path_to_compiled_mender_client_binary>
```
