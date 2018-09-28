---
title: U-Boot
taxonomy:
    category: docs
---

[Mender conversion scripts](https://github.com/mendersoftware/mender-conversion-tools) provide script for building and installing patched U-Boot for Raspbian. Currently only patched U-Boot is supported by Mender on Raspberry Pi 3. This command will install bootloader on disk image with partition layout compliant with Mender requirements.

```bash
 ./mender-conversion-tool.sh install_bootloader --image <sdimg_file_path> --device-type raspberrypi3 --toolchain <toolchain_name e.g. arm-linux-gnueabihf>
```

Mender updates require not only patched U-Boot but also some Mender specific files. These files are strongly connected with patched U-Boot and they are responsible for the updates management. The command below will install all necessary files. It requires compiled Mender client application. Mender provides [tools for cross compilation of the client binary.](https://github.com/mendersoftware/mender-crossbuild)

```bash
./mender-conversion-tool.sh install_mender --image <sdimg_file_path> --device-type raspberrypi3 --artifact <name_of_artifact> --server <server_address_ip> --mender <path_to_compiled_mender_client_binary>
```
