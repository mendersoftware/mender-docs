---
title: Create an Artifact with system snapshot
taxonomy:
    category: docs
    label: tutorial
---
To support an easy golden image workflow, Mender supports creating a snapshot of 
the currently running system. In this workflow a "golden image" is maintained on
a single device (or SD card) by making run-time modifications on the device, 
such as installing packages, changing configurations and updating the operating
system. When this device has been tested and the environment should be 
replicated, a snapshot can be taken with Mender. This results in a filesystem
image and Mender Artifact that can be deployed to the rest of the device fleet.

!!! This feature is fully supported by the
!!! following filesystems: ext[234], XFS, JFS, btrfs, f2fs, and ReiserFS.


## Option 1: Creating a snapshot using mender-artifact directly

There is support for creating a snapshot Artifact directly from a workstation
with `mender-artifact` installed, which is usually the easiest approach.
First, make sure your workstation has the [latest version of
mender-artifact installed](../../12.Downloads/01.Workstation-tools/docs.md#mender-artifact).

This approach requires that the golden device
is reachable and has *ssh* and *sudo* installed. `mender-artifact` accepts a
file URL with ssh schema and will automatically run the commands above
on the golden device.

!!! While a snapshot is in progress, all processes that writes to the root
!!! filesystem will be blocked for the duration of the snapshot process.

For example, the command:

```bash
USER="user"
ADDR="device-ip:port"
DEVICE_TYPE="raspberrypi4"

mender-artifact write rootfs-image -f ssh://${USER}@${ADDR} \
                                   -n artifact-name \
                                   --software-version 1.0 \
                                   -o snapshot-release.1.0.mender \
                                   -t $DEVICE_TYPE
```

creates an Artifact directly on your workstation, containing the system image of your device.

Please note you can pass extra arguments to ssh. To do this, specify
each one of them in a separate `-S "${SSH_ARG}"` option, e.g.:

```bash
USER="user"
ADDR="device-ip"

mender-artifact write rootfs-image \
    -f ssh://"${USER}@${ADDR}" \
    -n artifact-name \
    --software-version 1.0 \
    -o snapshot-release.1.0.mender \
    -t device-type
    --ssh-args="-p 8122" \
    --ssh-args="-o UserKnownHostsFile=/dev/null" \
    --ssh-args="-o StrictHostKeyChecking=no" \
    --ssh-args="-o PubKeyAuthentication=no"
```


## Option 2: Creating a snapshot on the golden device

With this approach, you can create a snapshot in several steps, working
directly in the device terminal. This approach is more suitable if you
do not have direct SSH access to the device, the network connectivity
is not strong or you would like to customize the workflow more.

The `mender-snapshot` executable provides a command `mender-snapshot dump` for
dumping a frozen copy of the root filesystem to standard output. In this section,
we go through two common approaches for using the snapshot feature from the
device: dumping a snapshot to a remote host or to a storage device.

If `ssh` is available on your device, then it is possible to redirect the output
from the snapshot command to a remote host. Assuming a computer is reachable and
running the ssh daemon, running the following command will generate a snapshot
file `root-part.ext4` in the user's home directory on the remote machine:

!!! While a snapshot is in progress, all processes that writes to the root
!!! filesystem will be blocked for the duration of the snapshot process.
!!! Redirecting the output of the snapshot command to the same filesystem will
!!! freeze the system for a short duration before aborting.

```bash
USER="user"
HOST="host-ip"

mender-snapshot dump | ssh $USER@$HOST /bin/sh -c 'cat > $HOME/root-part.ext4'
```

<!--AUTOVERSION: "Before `mender-snapshot` %"/ignore-->
!!! Before `mender-snapshot` 4.0.0, the functionality was built into the `mender`
!!! command. Please use `mender snapshot` in place of `mender-snapshot` (note
!!! the dash) in the snippet above, as well as in the remaining snippets below.

If `ssh` is not available, you can attach a removable storage device (e.g.
USB stick) and redirect the output to a file on the device.
```bash
mount /dev/(...) /mnt
mender-snapshot dump > /mnt/root-part.ext4
```

! Make sure there is enough available space on the storage device for the
! entire root filesystem (e.g. comparing the output of `df -h / /mnt`).

To help save storage space and bandwidth, a built-in `--compression` option is 
available. For the example above, a gzip-compressed version of the filesystem is
produced by passing gzip to the `--compression` flag.
```bash
mount /dev/(...) /mnt
mender-snapshot dump --compression gzip > /mnt/root-part.ext4.gz
```

!!! Note that if you used compression while creating the snapshot, after
!!! transferring the image to the build host, you need to uncompress it again
!!! with `gunzip root-part.ext4.gz`. Mender-artifact cannot use a compressed
!!! image as input.

In this case, passing `root-part.ext4` as the file-parameter to
[mender-artifact](../../12.Downloads/01.Workstation-tools/docs.md#mender-artifact) produces a
deployment ready Mender Artifact:
```bash
mender-artifact write rootfs-image -f /mnt/root-part.ext4 \
                                   -n artifact-name \
                                   --software-version 1.0 \
                                   -o snapshot-release.1.0.mender \
                                   -t device-type
```
Uploading this artifact to the mender server and creating a deployment ensures
that all devices runs an identical rootfs version as the golden device.
