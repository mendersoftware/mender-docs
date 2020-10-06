---
title: Software versioning
taxonomy:
    category: docs
    label: tutorial
---

## Introduction

Reporting the current software version running on a device can be challenging when mixing full system updates and application updates. On top of this, installing software on different partitions than the root filesystem requires additional flexibility in storing and reporting the current version of software installed into the device.

For these reasons, the Mender Artifact tool supports several options to customize the current software version's reporting, both for full system updates and application updates via Update Modules.

The software versioning is stored in the Mender Artifacts as *Provides*, and is automatically reported by the Mender Client as inventory data. See below for further details on how to override the default software versioning keys when generating the Artifacts.

## Full system updates

When creating a full system update, the Mender Artifact tool automatically generates a *Provides* entry using the key `rootfs-image.version` and the Artifact name as value. By default, the Mender Client will automatically report such a key/value pair as inventory data.

To override the value of the versioning key, which defaults to the Artifact's name, you can use the `--software-version` flag.

<!--AUTOVERSION: "value \"%\""/ignore-->
For example, to explicitly set the software version for a full system update to the value "1.0.0", you can use the following Mender Artifact command line:

<!--AUTOVERSION: "software-version %"/ignore-->
```bash
$ mender-artifact write rootfs-image \
    --software-version 1.0.0 \
   ...
```
The command above will generate the following versioning key/value pair:

<!--AUTOVERSION: "rootfs-image.version=%"/ignore-->
```
rootfs-image.version=1.0.0
```

## Application updates (Update modules)

When creating Application updates using the Update modules, the Mender Artifact tool automatically generates a *Provides* entry using the key `rootfs-image.MODULE.version`, where the name of the Update modules replaces `MODULE`, and the Artifact name as value. By default, the Mender Client will automatically report such a key/value pair as inventory data.

It is possible to customize this behaviour overriding the base key (`rootfs-image`) with a custom one using the `--software-filesystem` flag of `mender-artifact`. It is also possible to override the software name, which defaults to the name of the Update module, using the `--software-name` flag. If provided, the generated software version key will be `rootfs-image.NAME.version`. Additionally, to override the value of the versioning key, which defaults to the Artifact's name, you can use the `--software-version` flag.

<!--AUTOVERSION: "value \"%\""/ignore-->
For example, to explicitly set the software version for an application update to the value "1.0.0", you can use the following Mender Artifact command line:

<!--AUTOVERSION: "software-version %"/ignore-->
```bash
$ mender-artifact write module-image \
    -T script
    --software-version 1.0.0 \
   ...
```
The command above will generate the following versioning key/value pair:

<!--AUTOVERSION: "rootfs-image.script.version=%"/ignore-->
```
rootfs-image.script.version=1.0.0
```

To have the Mender Client report a custom name for the software you are installing, you can override the software name in the versioning key using the `--software-name" flag as follows:

<!--AUTOVERSION: "software-version %"/ignore-->
```bash
$ mender-artifact write module-image \
    -T script
    --software-name myapp \
    --software-version 1.0.0 \
   ...
```
The command above will generate the following versioning key/value pair:

<!--AUTOVERSION: "rootfs-image.myapp.version=%"/ignore-->
```
rootfs-image.myapp.version=1.0.0
```

Additionally, to track applications installed on other partitions than the rootfs, you can customize the name of the filesystem using the `--software-filesystem` flag, as follows:

<!--AUTOVERSION: "software-version %"/ignore-->
```bash
$ mender-artifact write rootfs-image \
    -T script
    --software-filesystem myfs \
    --software-name myapp \
    --software-version 1.0.0 \
   ...
```
The command above will generate the following versioning key/value pair:

<!--AUTOVERSION: "myfs.myapp.version=%"/ignore-->
```
myfs.myapp.version=1.0.0
```

## Advanced usage

To support advanced software reporting needs, the Mender Artifact tool also supports the so-named *Clear provides* payload field, a list of patterns that remove the *Provides* entries matching them.

Each pattern can contain multiple placeholders, each of them expressed using asterisks (`*`), which match a sequence of zero or more characters. For example, the pattern `rootfs-image.*` matches `rootfs-image.version` and `rootfs-image.checksum` but not `datafs-image.checksum` nor `rootfs-image`.

Mender Artifacts supports the following options:

* `--clears-provides`: adds the specified pattern to the *Clear provides*

* `--no-default-clears-provides`: disables the automatic generation of *Clear provides* to gain full control on the patterns.

For example, to provide an alternative rootfs-image update method based on an Update Module, you would need an Artifact that clears the `rootfs-image.version` and `rootfs-image.checksum` *Provides* keys.
To achieve this goal, you could use the following command:

```bash
$ mender-artifact write module-image \
    -T custom-root-image \
    --software-filesystem rootfs-image \
    --no-default-clears-provides \
    --clears-provides 'rootfs-image.*' ...
```

In another context, you could need to update other partitions than the rootfs, still taking advantage of the software versioning but using a different key.
Given the `part2-image` versioning key, you could use the following command:

```bash
$ mender-artifact write module-image \
    -T part2-image \
    --software-filesystem part2-image \
    --no-default-clears-provides \
    --clears-provides 'part2-image.*' ...
```

Finally, you may want to support proxy updates, where multiple connected devices can update either fully or partially.
In this scenario, for the full updates to report correctly, you need to create them specifying a custom software versioning key, as follows:

```bash
$ mender-artifact write module-image \
    -T full-proxy-update \
    --software-filesystem device1-fs \
    --no-default-clears-provides \
    --clears-provides 'device1-fs.*' ...
```
