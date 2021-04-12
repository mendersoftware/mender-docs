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

#### File transfer configuration

!!!!! [Mender Troubleshoot](https://mender.io/plans/features?target=_blank) add-on required.

* `FileTransfer`:  File transfer configuration options.
  * `Disable`: Disable file transfer.


#### Mender client configuration

* `MenderClient`: Configuration for mender-client dbus API.
  * `Disable`: Disable mender-client dbus hooks.
  
#### Port forward configuration

!!!!! [Mender Troubleshoot](https://mender.io/plans/features?target=_blank) add-on required.

* `PortForward`: Configuration for port forwarding
  * `Disable`: Disable the port forwarding feature.
  
#### Remote terminal configuration

!!!!! [Mender Troubleshoot](https://mender.io/plans/features?target=_blank) add-on required.

* `ShellCommand`: Command executed initiating a new remote terminal session.
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
