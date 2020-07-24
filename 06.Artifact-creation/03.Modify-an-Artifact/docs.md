---
title: Modify a disk image
taxonomy:
    category: docs
---

When provisioning a device, it is useful to modify the disk image (`.img`) before flashing it to SD
cards in order to edit necessary configurations. The `mender-artifact` tool supports copying files
in and out of disk images. If you do not yet have the `mender-artifact` tool, it can be downloaded
from our [Downloads section](../../downloads).

## Prerequisites

You need to have an image ending with `img`. There are several possible suffixes, `.img`, `.uefiimg`
and `.sdimg`. Note that mender-artifact currently does not support modifying `.ubimg` images.

## Copy a file into the disk image

To copy a file into the disk image (`img` file), use the following command:

```bash
mender-artifact cp <FILE> <PATH-TO-IMAGE>:<FILE-PATH-INSIDE-IMAGE>
```

For example, to update the `/etc/motd` file on the device, use these commands:

```bash
IMAGE=<PATH-TO-IMAGE>
echo "Welcome to this Mender device!" > motd
mender-artifact cp motd ${IMAGE}:/etc/motd
```

Note that the operation may sometimes take a few minutes even though the file is small. This is
because the image partitions are being unpacked and repacked automatically.


## Copy a file out of the disk image

To fetch a file from the image so that you can modify it and copy it back, use this command:

```bash
mender-artifact cp <PATH-TO-IMAGE>:<FILE-PATH-INSIDE-IMAGE> <LOCAL-FILE-PATH>
```

Afterwards you can modify the file to suit your needs and copy it back by reversing the arguments.
