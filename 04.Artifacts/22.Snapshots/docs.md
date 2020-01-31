---
title: Artifact from system snapshot
taxonomy:
    category: docs
---
To support an easy golden image workflow, Mender supports creating a snapshot of 
the currently running system. In this workflow a "golden image" is maintained on
a single device (or SD card) by making run-time modifications on the device, 
such as installing packages, changing configurations and updating the operating
system. When this device has been tested and the environment should be 
replicated, a snapshot can be taken with Mender. This results in a file system
image and Mender Artifact that can be deployed to the rest of the device fleet.

!!!!!! This feature is available from version 2.3 and fully supported by the
!!!!!! following filesystems: ext[234], XFS, JFS, btrfs, f2fs, and ReiserFS.

## Creating a snapshot on the golden device
The `mender` executable provides a command `mender snapshot dump` for dumping a 
frozen copy of the root filesystem to standard error. In this section, we go
through two common approaches for using the snapshot feature from the device:
dumping a snapshot to a remote host or to a storage device.

!!! While a snapshot is in progress, all processes that writes to the filesystem
!!! being backed up will be blocked until the snapshot is complete. Redirecting
!!! the output to the same filesystem will cause the process to freeze and
!!! terminate after a short while.

If you've installed `ssh` on the device and have set up a computer with the ssh
daemon running; then, redirecting the dumped output as follows will store the
snapshot on the workstation as a filesystem image:
```bash
USER="user"
HOST="host-ip"

mender snapshot dump | ssh $USER@$HOST /bin/sh -c 'cat > $HOME/root-part.fs`
```

If `ssh` is not available, you can attach a removable storage device (e.g.
USB stick) and redirect the output to a file on the mounted device.
```bash
mount /dev/(...) /mnt
mender snapshot dump > /mnt/root-part.fs
```

! Make sure you have enough storage space on the removable device creating the
! snapshot.

To help save storage space and bandwidth for the target storage, a built-in
`--compression` option is available. For the example above, a gzip-compressed
version of the filesystem is produced by passing gzip to the `--compression` 
flag.
```bash
mount /dev/(...) /mnt
mender snapshot dump --compression gzip > /mnt/root-part.fs.gz
```

!!! Don't forget the `.gz` extension in the target filename.

In this case, passing `root-part.fs` (or `root-part.fs.gz`) as the 
file-parameter to [mender-artifact](../../08.Downloads/docs.md#mender-artifact)
produces a deployment ready Mender Artifact:
```bash
mender-artifact write rootfs-image -f /mnt/root-part.fs \
                                   -n artifact-name \
                                   -o snapshot-release.1.0.mender \
                                   -t device-type
```
Uploading this artifact to the mender server and creating a deployment ensures
that all devices runs an identical rootfs version as the golden device.

## Creating a snapshot using mender-artifact CLI
There is support for creating a snapshot artifact directly from a workstation 
with mender-artifact installed. This approach requires that the golden device 
is reachable and has *ssh* and *sudo* installed. `mender-artifact` accepts a
file URL with ssh schema and will automatically run the commands above
on the golden device. For example, the command:
```bash
USER="user"
ADDR="device-ip:port"

mender-artifact write rootfs-image -f ssh://$USER@$ADDR \
                                   -n artifact-name \
                                   -o snapshot-release.1.0.mender \
                                   -t device-type
```
Yields the exact same artifact as above.
