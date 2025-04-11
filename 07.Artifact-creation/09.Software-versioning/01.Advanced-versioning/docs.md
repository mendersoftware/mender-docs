---
title: Advanced versioning
taxonomy:
    category: docs
---

To support advanced software reporting needs, the Mender Artifact utility also supports the *Clear Provides* payload field, which contains a list of patterns to be removed from the *Provides* entries on the device.

Each pattern can contain multiple placeholders, each of them expressed using asterisks (`*`), which match a sequence of zero or more characters. For example, the pattern `rootfs-image.*` matches `rootfs-image.version` and `rootfs-image.checksum` but not `data-partition.checksum` nor `rootfs-image`.

Mender Artifacts supports the following options:

* `--clears-provides`: adds the specified pattern to the *Clear Provides*

* `--no-default-clears-provides`: disables the automatic generation of *Clear Provides* to gain full control on the patterns.

For example, to provide an alternative rootfs-image update method based on an Update Module, you would need an Artifact that clears the `rootfs-image.version` and `rootfs-image.checksum` *Provides* keys.
To achieve this goal, you could use the following command:

```bash
mender-artifact write module-image \
    -T custom-root-image \
    --software-filesystem rootfs-image \
    --no-default-clears-provides \
    --clears-provides 'rootfs-image.*' ...
```

In another context, you could need to update other partitions than the rootfs, still taking advantage of the software versioning but using a different key.
Given the `part2-image` versioning key, you could use the following command:

```bash
mender-artifact write module-image \
    -T part2-image \
    --software-filesystem part2-image \
    --no-default-clears-provides \
    --clears-provides 'part2-image.*' ...
```

Finally, you may want to support proxy updates, where multiple connected devices can update either fully or partially.
In this scenario, for the full updates to report correctly, you need to create them specifying a custom software versioning key, as follows:

```bash
mender-artifact write module-image \
    -T full-proxy-update \
    --software-filesystem device1-fs \
    --no-default-clears-provides \
    --clears-provides 'device1-fs.*' ...
```
