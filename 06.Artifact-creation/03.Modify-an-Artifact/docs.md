---
title: Modify an Artifact
taxonomy:
    category: docs
---

It is possible to modify an Artifact after it has been created. There two types of modifications
available: Header modification and content modification. Header modification is supported for all
Artifact types, while content modification is only supported for `rootfs-image` Artifacts.

## Prerequisites

All modifications require the `mender-artifact` tool. If you do not yet have this tool, it can be
downloaded from our [Downloads section](../../downloads).

## Header modification

Header modification allows you to change the name, as well as certain other attributes, of an
Artifact.

!!! It is also possible to change the name of disk images (files ending with `img`), except for
!!! `.ubimg` images.

To change the name of an Artifact, execute the following command:

```bash
mender-artifact modify -n new-name <PATH-TO-ARTIFACT>
```

Certain other attributes of Artifacts are also possible to change using `mender-artifact`, but these
are a lot less common. Please refer to the `mender-artifact modify --help` screen for more
information.

## Content modification

The `mender-artifact` tool supports copying files in and out of Artifacts.

! Content modification is only possible on Artifacts with the `rootfs-image` payload type.

!!! It is also possible to copy files in and out of disk images (files ending with `img`), except
!!! for `.ubimg` images. If copying into a disk image, the standard Mender paths, `/boot/efi`,
!!! `/boot/grub`, `/data` and `/uboot`, will map to the correct partitions where these are normally
!!! mounted.

### Copy a file into an Artifact

To copy a file into an Artifact, use the following command:

```bash
mender-artifact cp <FILE> <PATH-TO-ARTIFACT>:<FILE-PATH-INSIDE-ARTIFACT>
```

For example, to update the `/etc/motd` file in the Artifact, use these commands:

```bash
ARTIFACT=<PATH-TO-ARTIFACT>
echo "Welcome to this Mender device!" > motd
mender-artifact cp motd ${ARTIFACT}:/etc/motd
```

Note that the operation may sometimes take a few minutes even though the file is small. This is
because the Artifact is uncompressed and unpacked, and then re-packed and re-compressed afterwards.


### Copy a file out of an Artifact

To fetch a file from an Artifact so that you can modify it and copy it back, use this command:

```bash
mender-artifact cp <PATH-TO-ARTIFACT>:<FILE-PATH-INSIDE-ARTIFACT> <LOCAL-FILE-PATH>
```

Afterwards you can modify the file to suit your needs and copy it back by reversing the arguments.
