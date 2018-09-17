---
title: GRUB with Debian
taxonomy:
    category: docs
---

[Mender conversion scripts](https://github.com/mendersoftware/mender-conversion-tools) use GRUB as second stage bootloader for Debian on Beaglebone. Mender conversion tools build GRUB from [official repository](https://www.gnu.org/software/grub/grub-download.html). Mender project does not require any patches for GRUB. GRUB should be built with EFI platform support. This command will install GRUB bootloader for disk image with partition layout compliant to Mender requirements:

```bash
 ./mender-conversion-tool.sh install_bootloader --image <sdimg_file_path> --device-type beaglebone --toolchain <cross_compiler_name e.g. arm-linux-gnueabihf>
```

Mender updates require also some Mender specific files. These files are strongly connected with bootloader and they are responsible for the updates management. The command below will install all necessary files. It requires compiled Mender client application. Mender provides [tools for cross compilation of the client binary.](https://github.com/mendersoftware/mender-crossbuild)

```bash
./mender-conversion-tool.sh install_mender --image <sdimg_file_path> --device-type beaglebone --artifact <name_of_artifact> --server <server_address_ip> --mender <path_to_compiled_mender_client_binary>
```
