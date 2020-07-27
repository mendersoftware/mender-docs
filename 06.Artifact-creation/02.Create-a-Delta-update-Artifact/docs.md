---
title: Create a Delta update Artifact
taxonomy:
    category: docs
    label: reference
---

Imagine that you have a large fleet of devices, all needing a full filesystem
update. Furthermore, assume that most of the image is unchanged from the previous release; i.e.: the number of bytes actually changed between the two images constitutes a very small fraction of total image size. Deploying the complete filesystem image to all the devices takes considerable time and bandwidth, even though we know that the [delta](../../02.Overview/15.Taxonomy/docs.md) between them
is relatively small. To address this issue you can use 
[binary delta update Artifacts](../../02.Overview/06.Delta-update/docs.md) that
pass only the difference between the two images.

To generate binary delta Artifacts, you must start with two full file system Artifacts. You can use [Yocto](https://hub.mender.io/t/robust-delta-update-rootfs/1144),
[mender-convert](../../03.Devices/03.Debian-family/docs.md), or any mechanism of your choice to create the images. You can generate an binary default Artifact with the following command.

```bash
./mender-binary-delta-generator \
    -o v2.0-deltafrom-v1.0.mender \
    release-v.1.0.mender release-v.2.0.mender
```

In the above we have assumed that the current working directory contains at least:

```bash
$ ls -1
mender-binary-delta-generator
release-v.1.0.mender
release-v.2.0.mender
```

with the `mender-binary-delta-generator` application coming from mender-binary-delta archive which you need to [download](https://hub.mender.io/t/robust-delta-update-rootfs/1144).

You can now use `v2.0-deltafrom-v1.0.mender` with Mender, and the Client will 
automatically detect its type and handle it appropriately.

The above approach can save considerable time and bandwidth, but it requires
read-only root filesystem support to ensure that the delta calculated offline will apply properly to the active root filesystem. Please refer to the [Mender Hub](https://hub.mender.io/t/robust-delta-update-rootfs/1144)
for more information on how to incorporate the binary Delta update Artifacts into
your build.
