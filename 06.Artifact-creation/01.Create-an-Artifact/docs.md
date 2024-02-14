---
title: Create an Artifact
taxonomy:
    category: docs
    label: tutorial
---

Mender uses [Artifacts](../../02.Overview/03.Artifact/docs.md) to package the
software updates for delivery to devices. As a user you manage the Artifacts
with the help of the `mender-artifact` command. You can get it either as a pre-built
executable from the [downloads section](../../10.Downloads)
or [build from sources](https://github.com/mendersoftware/mender-artifact?target=_blank).
The two basic usage scenarios of this utility reflect the two main update types
Mender supports: Operating System update and Application update.

### Create an Operating System update Artifact

Assuming you already have a generated filesystem image in `rootfs.ext4` file,
you can use the following command to generate an Artifact that contains the entire filesystem image as the payload:

```bash
mender-artifact write rootfs-image \
   -t beaglebone \
   -n release-1 \
   --software-version rootfs-v1 \
   -f rootfs.ext4 \
   -o artifact.mender
```

Note that the `rootfs.ext4` filesystem image must be properly integrated with Mender for successful deployments. This generally means that you either generated it using [the Yocto Project](../../05.Operating-System-updates-Yocto-Project/03.Build-for-demo/docs.md), or converted it from an existing
[Debian image](../../04.Operating-System-updates-Debian-family/02.Convert-a-Mender-Debian-image/docs.md).

The remaining flags specify the parameters used to [match devices to deployments](../../02.Overview/05.Deployment/docs.md#Algorithm-for-selecting-the-Deployment-for-the-Device) as follows:
* `-t`: specifies the compatible device types.
* `-n`: specifies the name of the Artifact.
* `--software-version` specifies the version string for the rootfs-image.
* `-o`: specifies the path to the output file.

!!! Use the Mender Web UI to see which rootfs-image version is currently installed on the device, and which Artifact was the last one to be installed.

### Create an application update Artifact

Creating an Artifact takes a different form in the case of [application updates](../../02.Overview/01.Introduction/docs.md#application-updates).

For application updates, the command for `mender-artifact` tool will be different depending on the
implementation details of the actual update module. Most of the Update Modules come with a script
to simplify the Artifact creation so that the implementation details are hidden from the final user.

For example, assume that you want to copy a new `authorized_keys` file to the `/home/${USER}/.ssh`
directory on your devices, where `USER` holds your user name.

We will use the [single file](https://hub.mender.io/t/single-file/486/26?target=_blank) [Update Module](../../06.Artifact-creation/08.Create-a-custom-Update-Module/docs.md) to create a *module-image*.

First, download the script to generate the Artifact and make it executable:
<!--AUTOVERSION: "mendersoftware/mender/%/support"/mender-->
```
curl -O https://raw.githubusercontent.com/mendersoftware/mender/4.0.1/support/modules-artifact-gen/single-file-artifact-gen
chmod +x single-file-artifact-gen
```

Now create the Artifact with:
```bash
./single-file-artifact-gen \
  --device-type raspberrypi4 \
  -o artifact.mender \
  -n updated-authorized_keys-1.0 \
  --software-name authorized_keys \
  --software-version 1.0 \
  --dest-dir /home/${USER}/.ssh \
  authorized_keys
```

Note specifically that in this case we are creating a *module-image*, using the [single
file](https://hub.mender.io/t/single-file/486/26?target=_blank) [Update
Module](../../06.Artifact-creation/08.Create-a-custom-Update-Module/docs.md). The Artifact created
will be compatible with the *raspberrypi4* device type, although you can specify more device types
using multiple times `--device-type` if needed. The name of the Artifact is declared as
*updated-authorized_keys-1.0*, we set the version of the software to *1.0* and indicate that it will
be installed in the *rootfs* partition. The resulting file `artifact.mender` holds the Artifact.

<!--AUTOVERSION: "mendersoftware/mender/blob/%/support"/mender-->
Inspect the source code of the
[single file Update Module](https://github.com/mendersoftware/mender/blob/4.0.1/support/modules/single-file?target=_blank)
to learn about the implementation details of this module.


#### Server side Artifact generation

!!! Hosted Mender is available in multiple [regions](/11.General/00.Hosted-Mender-regions/docs.md) to connect to. Make sure you select your desired one before proceeding.

The [hosted Mender Server](https://hosted.mender.io?target=_blank) and any on-premise server installation, can generate application update Artifacts automatically using the [single file](https://hub.mender.io/t/single-file/486?target=_blank)
Update Module. You can test it by uploading any file to the [releases page](https://hosted.mender.io/ui/#/releases?target=_blank). The resulting Artifact
will carry the file you have uploaded, the destination
directory, the filename, and permissions, exactly as we saw above.

<!--AUTOVERSION: "mendersoftware/mender/blob/%/Documentation"/mender-->
For more details on how to write Update Modules, visit the [Create a custom Update Module](../08.Create-a-custom-Update-Module/docs.md) section and the [Update Module API specification](https://github.com/mendersoftware/mender/blob/4.0.1/Documentation/update-modules-v3-file-api.md?target=_blank).
