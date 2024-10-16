---
title: Mender Connect
taxonomy:
    category: docs
    label: reference
---

`mender-connect` is a daemon responsible for handling bidirectional
(websocket) communication with the Mender Server. The daemon is responsible for
implementing a range of troubleshooting features to the device as well as
several enhancement to the [Mender
client](../../03.Client-installation/01.Overview/docs.md).

Mender Connect is loosely coupled with the `mender-auth`. The main information passed between
`mender-auth` and `mender-connect` is the device authorization status. Since only accepted devices
can interact with the Mender Server, `mender-auth` passes the authorization token over DBus
which Mender Connect uses to establish a
[Websocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) connection to the
server. We use the well-known and well-defined open APIs, which makes the solution flexible and
portable.

## Installation

Please refer to the following sections for the Mender Connect installation:
* [mender-convert integration](../../04.Operating-System-updates-Debian-family/99.Variables/docs.md#mender_addon_connect_install) for installation in the existing images
* [Yocto projects](../../05.Operating-System-updates-Yocto-Project/05.Customize-Mender/docs.md#mender-connect) for the installation in a Yocto Project environment
* [installation with a deb](../../10.Downloads/docs.md#remote-terminal-add-on) for the installation from the Debian package

After installation, please refer to the [add-ons subsections](../../09.Add-ons/chapter.md) for the configuration options,
including the enabling and disabling of the features.

## Configuration

The mechanism for providing the configuration file and specifying the configuration values will depend on your choice of OS distribution or build system.

If you have already built an Artifact containing the rootfs, have a look at [modifying a Mender Artifact](../../06.Artifact-creation/03.Modify-an-Artifact/docs.md).

Following is a complete reference of the configuration options for
mender-connect along with the default values. The default configuration path is
`/etc/mender/mender-connect.conf`.

```json
{
  "ReconnectIntervalSeconds": 5,
  "Limits": {
    "Enabled": true,
    "FileTransfer": {
      "Chroot": "/var/lib/mender/filetransfer",
      "OwnerGet": ["mender","root"],
      "GroupGet": ["games","users"],
      "OwnerPut": "root",
      "GroupPut": "mender",
      "MaxFileSize": 4,
      "FollowSymLinks": true,
      "AllowOverwrite": true,
      "RegularFilesOnly": true,
      "PreserveOwner": true,
      "PreserveGroup": true,
      "PreserveMode": true,
      "Umask": "",
      "Counters": {
        "MaxBytesTxPerMinute": 1048576,
        "MaxBytesRxPerMinute": 1048576
      }
    }
  },
  "FileTransfer": {
    "Disable": false
  },
  "MenderClient": {
    "Disable": false
  },
  "PortForward": {
    "Disable": false
  },
  "ShellCommand": "/bin/sh",
  "ShellArguments": ["--login"],
  "Sessions": {
    "ExpireAfter": 0,
    "ExpireAfterIdle": 0,
    "MaxPerUser": 1,
    "StopExpired": false
  },
  "Terminal": {
    "Disable": false,
    "Height": 40,
    "Width": 80
  },
  "User": ""
}
```

* `ReconnectIntervalSeconds`: Number of seconds to wait before reconnecting on
  connection errors.

<!--AUTOVERSION: "version `%`"/ignore-->
! `Servers` and `ServerURL` are deprecated and unused since `mender-connect`
! version `1.0.0` - the values are automatically configured by `mender-auth`.

#### Limits configuration
There are certain features that you would want to keep under finer
control than just enable/disable. File Transfer is one example; imagine
you would like to restrict the transfers to a certain user or a group,
or limit the average number of bytes that a device can transfer in an hour.
The Limits section can be helpful here.

* `Limits`:  Limits configuration options.
  * `Enabled`: Enable limits control.
  * `FileTransfer`: File Transfer limits configuration.

##### File Transfer limits configuration
The `FileTransfer` section in the `Limits` configuration block has the following
options available:

* `Chroot`: limit the directory from which you can transfer files and to which you can upload them.
* `OwnerGet`: you can only transfer the files owned by the users on this list. If left empty, all users are allowed.
* `GroupGet`: you can only transfer the files that have a group from this list. If left empty, all groups are allowed.
* `OwnerPut`: all the files you upload to a device will have this username set as an owner.
* `GroupPut`: all the files you upload to a device will have this group set.
* `MaxFileSize`: the maximal file size that you can download from or upload to a device. Omitting this property or setting it to `0` will allow files of any size. 
* `FollowSymLinks`: if set to true, `mender-connect` will resolve all the links in the target or destination path and the transfer will proceed. If false, and if any part of an upload or download path is a link, `mender-connect` will refuse to carry out the request.
* `AllowOverwrite`: if set to true, `mender-connect` will overwrite the target file path when processing the upload request. If set to false `mender-connect` will refuse to overwrite the file.
* `RegularFilesOnly`: allow only the transfer of regular files.
* `PreserveOwner`: preserve the file owner from the upload request.
* `PreserveGroup`: preserve the file group from the upload request.
* `Umask`: set file permission upon upload - string representation. e.g. `"600"`
* `Counters`: Bytes transmitted/bytes received limits.
  * `MaxBytesTxPerMinute`: the maximal outgoing bytes that a device can transmit per minute. calculated as a moving exponential average. Omitting this property or setting it to `0` will allow transmits of any size.
  * `MaxBytesRxPerMinute`: the maximal incoming bytes that a device can receive per minute. calculated as a moving exponential average. Omitting this property or setting it to `0` will allow receives of any size.

#### File Transfer configuration

!!!!! The Mender Troubleshoot add-on package is required.
!!!!! See [the Mender plans page](https://mender.io/pricing/plans?target=_blank)
!!!!! for an overview of all Mender plans and features.

* `FileTransfer`:  File Transfer configuration options.
  * `Disable`: Disable file transfer.

#### Mender client configuration

* `MenderClient`: Configuration for mender-client dbus API.
  * `Disable`: Disable mender-client dbus hooks.
  
#### Port forward configuration

!!!!! The Mender Troubleshoot add-on package is required.
!!!!! See [the Mender plans page](https://mender.io/pricing/plans?target=_blank)
!!!!! for an overview of all Mender plans and features.

* `PortForward`: Configuration for port forwarding
  * `Disable`: Disable the port forwarding feature.
  
#### Remote Terminal configuration

!!!!! The Mender Troubleshoot add-on package is required.
!!!!! See [the Mender plans page](https://mender.io/pricing/plans?target=_blank)
!!!!! for an overview of all Mender plans and features.

* `ShellCommand`: Command executed initiating a new remote terminal session.
* `ShellArguments`: The command line arguments passed to the shell when spawned (defaults to `--login`).
* `Sessions`: Configuration for remote terminal sessions.
  * `StopExpired`: Terminate remote terminal sessions after
  * `ExpireAfter`: Time in seconds until a remote terminal expires.<sup>*</sup>
  * `ExpireAfterIdle` Time in seconds until a remote terminal expires after not
    receiving any traffic.<sup>*</sup>
  * `MaxPerUser`: Maximum number of terminal sessions allowed per user.
* `Terminal`: Terminal configuration options.
  * `Disable`: Disable the remote terminal feature.
  * `Height`: Terminal height in number of characters.
  * `Width`: Terminal width in number of characters.
* `User`: Login user for the remote terminal session.
    
!!! <sup>*</sup>`ExpireAfter` and `ExpireAfterIdle` are mutually exclusive
!!! configuration options, only one option can be configured at the time.

## Troubleshooting

By default, `mender-connect` runs as a `systemd` service. The easiest way to
troubleshoot any issues related to `mender-connect` is by inspecting the service
logs:
```bash
journalctl -u mender-connect
```

! If you're having difficulty troubleshooting an issue, don't hesitate to ask our
! community on [Mender Hub](https://hub.mender.io).
