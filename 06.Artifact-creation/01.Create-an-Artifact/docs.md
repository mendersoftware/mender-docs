---
title: Create an Artifact
taxonomy:
    category: docs
    label: tutorial
---

Mender uses [Artifacts](../../02.Overview/02.Artifact/docs.md) to package the
software updates for delivery to devices. As a user you manage the Artifacts
with the help of the `mender-artifact` command. You can get it either as a pre-built
executable from the [downloads section](../../09.Downloads)
or [build from sources](https://github.com/mendersoftware/mender-artifact?target=_blank).
The two basic usage scenarios of this utility reflect the two main update types
Mender supports: full filesystem update and application update.

### Create a full filesystem update Artifact

Assuming you already have a generated filesystem image in `rootfs.ext4` file,
you can use the following command to generate an Artifact that contains the entire filesystem image as the payload:

```bash
mender-artifact write rootfs-image \
   -t beaglebone \
   -n release-1 \
   -f rootfs.ext4 \
   -o artifact.mender
```

Note that the `rootfs.ext4` filesystem image must be properly integrated with Mender for successful deployments. This generally means that you either generated it using [the Yocto Project](../../05.System-updates-Yocto-Project/03.Build-for-demo/docs.md), or converted it from an existing
[Debian image](../../04.System-updates-Debian-family/02.Convert-a-Mender-Debian-image/docs.md).

The remaining flags specify the parameters used to [match devices to deployments](../../02.Overview/04.Deployment/docs.md#Algorithm-for-selecting-the-Deployment-for-the-Device) as follows:
* `-t`: specifies the compatible device types.
* `-n`: specifies the name of the Artifact.
* `-o`: specifies the path to the output file.

### Create an application update Artifact

Creating an Artifact takes a different form in the case of [application updates](../../02.Overview/01.Introduction/docs.md#Application-updates).

For example, assume that you want copy a new `authorized_keys` file to the `/home/pi/.ssh`
directory on your devices. We first store the path to the destination directory and file into two separate files, for packaging purposes:

```bash
echo /home/pi/.ssh > dest_dir # store the destination target directory
echo authorized_keys > filename # store the filename of the file we want to update
```

We can now create the Artifact using mender-artifact by running the following command:

```bash
mender-artifact write module-image \
  -T single-file \
  --device-type raspberrypi4 \
  -o artifact.mender \
  -n updated-authorized_keys-1.0 \
  -f dest_dir \
  -f filename \
  -f authorized_keys
```

Note specifically that in this case we are creating a *module-image*, using the [single file](https://hub.mender.io/t/single-file/486/26?target=_blank) (Update Module)[(../../06.Artifact-creation/08.Create-a-custom-Update-Module/docs.md]. The Artifact created will be compatible with the *raspberrypi4* device type, although you can specify multiple device types if needed. The name of the Artifact is declared as *updated-authorized_keys-1.0* and the payload files we created earlier are included. The resulting file `artifact.mender` holds the Artifact. Please note that, _single-file_ is both the name of the Update Module and the Artifact type. Please note also, that the payload files must use the name specified here.

#### Update Modules generation script

<!--AUTOVERSION: "mendersoftware/mender/blob/%/support"/mender-->
You can see the above example in the [single file Update Module](https://hub.mender.io/t/single-file/486?target=_blank). You can also see how simple it is to [write a custom Update Module.](https://github.com/mendersoftware/mender/blob/2.3.0/support/modules/single-file?target=_blank)

<!--AUTOVERSION: "mendersoftware/mender/blob/%/support"/mender-->
Also note that most of the Update Modules come with a [script to simplify the Artifact creation](https://github.com/mendersoftware/mender/blob/2.3.0/support/modules-artifact-gen/single-file-artifact-gen?target=_blank), but generally these are wrappers around `mender-artifact` utility to hide the complexity and make it easy to generate artifacts.

#### Server side Artifact generation

The [hosted Mender server](https://hosted.mender.io?target=_blank) and any on-premise server installation, can generate application update Artifacts automatically using the [single file](https://hub.mender.io/t/single-file/486?target=_blank)
Update Module. You can test it by uploading any file to the [releases page](https://hosted.mender.io/ui/#/releases?target=_blank). The resulting Artifact
will carry the file you have uploaded, the destination
directory, the filename, and permissions, exactly as we saw above.

<!--AUTOVERSION: "mendersoftware/mender/blob/%/Documentation"/mender-->
For more details on how to write Update Modules, visit the [Create a custom Update Module](../08.Create-a-custom-Update-Module/docs.md) section and the [Update Module API specification](https://github.com/mendersoftware/mender/blob/2.3.0/Documentation/update-modules-v3-file-api.md?target=_blank).
