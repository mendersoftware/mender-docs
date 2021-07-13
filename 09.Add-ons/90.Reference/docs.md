---
title: Reference: mender-connect
taxonomy:
    category: docs
    label: reference
---

`mender-connect` is a daemon responsible for handling bidirectional
(websocket) communication with the Mender server. The daemon is responsible for
implementing a range of troubleshooting features to the device as well as
several enhancement to the [mender-client](../../03.Client-installation/01.Overview/docs.md).

## Configuration

Following is a complete reference of the configuration options for
mender-connect along with the default values. The default configuration path is
`/etc/mender/mender-connect.conf`.

```json
{
  "HttpsClient": {
    "Certificate": "",
    "Key": "",
    "SSLEngine": ""
  },
  "ReconnectIntervalSeconds": 5,
  "ServerCertificate": "",
  "Servers": null,
  "ServerURL": "",
  "SkipVerify": false,
  "Limits": {
    "Enabled": true,
    "FileTransfer": {
      "Chroot": "/var/lib/mender/filetransfer",
      "OwnerGet": ["pi","root"],
      "GroupGet": ["games","users"],
      "OwnerPut": "root",
      "GroupPut": "pi",
      "MaxFileSize": 4,
      "FollowSymLinks": true,
      "AllowOverwrite": true,
      "RegularFilesOnly": true,
      "PreserveOwner": true,
      "PreserveGroup": true,
      "PreserveMode": true,
      "Counters": {
       "MaxBytesTxPerHour": 1048576,
       "MaxBytesRxPerHour": 1048576
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

* `HttpsClient`: Client TLS configuration.
  * `Certificate`: Path to client certificate.
  * `Key`: Path to client certificate private key.
  * `SSLEngine`: OpenSSL cryptographic engine.
* `ReconnectIntervalSeconds`: Number of seconds to wait before reconnecting on
  connection errors.
* `ServerCertificate`: Path to a custom certificate trust store.
  _mender-connect_ will automatically use the system-wide certificate store.
* `Servers`: *Deprecated* List of server URLs to connect with<sup>*</sup>.
* `ServerURL`: *Deprecated* Server URL to connect with<sup>*</sup>.
* `SkipVerify`: Skip TLS certificate verification.

<!--AUTOVERSION: "version `%`"/ignore-->
! `Servers` and `ServerURL` are deprecated and unused since `mender-connect`
! version `1.0.0` - the values are automatically configured by the `mender-client`.

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
* `OwnerGet`: you can only transfer the files owned by the users on this list.
* `GroupGet`: you can only transfer the files that have a group from this list.
* `OwnerPut`: all the files you upload to a device will have this username set as an owner.
* `GroupPut`: all the files you upload to a device will have this group set.
* `MaxFileSize`: the maximal file size that you can download from or upload to a device.
* `FollowSymLinks`: if set to true, `mender-connect` will resolve all the links in the target or destination path and the transfer will proceed. If false, and if any part of an upload or download path is a link, `mender-connect` will refuse to carry out the request.
* `AllowOverwrite`: if set to true, `mender-connect` will overwrite the target file path when processing the upload request. If set to false `mender-connect` will refuse to overwrite the file.
* `RegularFilesOnly`: allow only the transfer of regular files.
* `PreserveOwner`: preserve the file owner from the upload request.
* `PreserveGroup`: preserve the file group from the upload request.
* `Counters`: Bytes transmitted/bytes received limits.
  * `MaxBytesTxPerHour`: the maximal outgoing bytes that a device can transmit per hour. calculated as a moving exponential average.
  * `MaxBytesRxPerHour`: the maximal incoming bytes that a device can receive per hour. calculated as a moving exponential average.

#### File Transfer configuration

!!!!! The Mender Troubleshoot add-on package is required.
!!!!! See [the Mender features page](https://mender.io/plans/features?target=_blank)
!!!!! for an overview of all Mender plans and features.

* `FileTransfer`:  File Transfer configuration options.
  * `Disable`: Disable file transfer.

#### Mender client configuration

* `MenderClient`: Configuration for mender-client dbus API.
  * `Disable`: Disable mender-client dbus hooks.
  
#### Port forward configuration

!!!!! The Mender Troubleshoot add-on package is required.
!!!!! See [the Mender features page](https://mender.io/plans/features?target=_blank)
!!!!! for an overview of all Mender plans and features.

* `PortForward`: Configuration for port forwarding
  * `Disable`: Disable the port forwarding feature.
  
#### Remote Terminal configuration

!!!!! The Mender Troubleshoot add-on package is required.
!!!!! See [the Mender features page](https://mender.io/plans/features?target=_blank)
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
