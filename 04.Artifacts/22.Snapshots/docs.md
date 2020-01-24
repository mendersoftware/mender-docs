---
title: Artifact from system snapshot
taxonomy:
    category: docs
---

After provisioning the first batch of devices it is sometimes useful to have a
device to tinker with - e.g reconfigure, test and install new packages, before
deploying to the rest of the fleet. When satisfied with the rootfs, the mender
binary provides an easy way to create a  snapshot of the root filesystem. The
snapshot feature is also available within the 
[mender-artifact](../../08.Downloads/docs.md#mender-artifact) CLI tool.

!!!!!! This feature is available from version 2.3 and fully supported by the
!!!!!! following filesystems: ext4, ext3, XFS, JFS, btrfs, f2fs, and ReiserFS.
!!!!!! If your device runs on a different filesystem a workaround is described 
!!!!!! in the [Snapshot a partition](#snapshot-a-partition) section below.

## Creating a snapshot on the device
The *Mender* binary has a command `mender snapshot dump` for dumping a frozen
copy of the root filesystem to standard error. In this section, two approaches
are described: dumping to a remote host or to external storage.

!!! While a snapshot is in progress, all processes that writes to the filesystem
!!! being backed up will be blocked until the snapshot is complete. If the output
!!! of `mender snapshot dump` is redirected to a process that writes to the
!!! filesystem, the process will freeze for a short while until an internal timer
!!! expires and unfreezes the filesystem.

If the device has `ssh` installed and a host is reachable and has an ssh server 
running, the output from the command can be redirected to standard an ssh 
session as follows:
```bash
mender snapshot dump | ssh user@host-ip /bin/sh -c 'cat > $HOME/root-part.fs`
```

If a USB stick is available, simply redirecting the output to a file on the
mounted device.
```bash
mount /dev/(...) /mnt
mender snapshot dump > /mnt/root-part.fs
```

!!! The snapshot command also accepts a `--compression` parameter to save
!!! storage/bandwidth for the target output.

In this case, `root-part.fs` can be passed as the file parameter to
[mender-artifact](../../08.Downloads/docs.md#mender-artifact):
```bash
mender-artifact write rootfs-image -f /mnt/root-part.fs \
                                   -n artifact-name \
                                   -o snapshot-release.1.0.mender \
                                   -t device-type
```
Uploading this artifact to the mender server and creating a deployment ensures
that all devices runs an identical rootfs version as the snapshot host.

## Creating a snapshot from a host machine
As already mentioned there is support to create a snapshot artifact directly
from a host machine. This approach requires that the snapshot target device 
is reachable and has *ssh* and *sudo* installed. *mender-artifact* accepts a
file URL with ssh schema and will automatically try to run the commands above
on the remote device. For example, the command:
```bash
mender-artifact write rootfs-image -f ssh://user@device-ip:port \
                                   -n artifact-name \
                                   -o snapshot-release.1.0.mender \
                                   -t device-type
```
Will yield the exact same artifact as above.

## Snapshot a partition
It is also possible to specify the partition to capture using the `--fs-path` <!--- FIXME: or source? -->
flag. The path must point to either a file/directory on the target filesystem or
to the device file (other special filetypes will throw an error). To illustrate,
consider a device with a filesystem which does not implement the ioctl freeze 
operation (see supported filesystems [above](#artifact-from-system-snapshot)). As
an alternative to running snapshot from the active partition, rollback to the
inactive partition and perform the snapshot from there. That is,
```bash
# Ready to snapshot partition
mender rollback
# <rebooting...>
mender snapshot dump --fs-path /dev/<insert inactive partition device here> | \
                ssh user@host /bin/sh -c 'cat > snapshot.fs'

```
!!!!!! Make sure that the inactive partition has a stable image with Mender 2.3 or
!!!!!! later.
