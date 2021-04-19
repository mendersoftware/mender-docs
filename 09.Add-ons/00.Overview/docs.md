---
title: Overview
taxonomy:
    category: docs
---


# Mender Connect

The add-ons are independent applications, but they run under a common executable:
`mender-connect`. Every add-on, with [configure](../02.Configure/docs.md) being one notable
exception, requires [Mender Connect](../../09.Downloads/docs.md#mender-connect) to function.

Once you have installed `mender-connect`, there are no other items needed to get the add-ons
on your device. All you need is a proper configuration.
 
The following table shows a brief summary of the add-ons.

| Add-on name     | Description | Availability |
| --------------- | ----------- | ------------ |
| [Remote Terminal](../01.Remote-Terminal/docs.md) | Provides interactive shell sessions with full terminal emulation in both UI and CLI | Troubleshooting package |
| [File Transfer](../03.File-Transfer/docs.md) | Allows you to upload and download files to and from a device with both UI and CLI | Troubleshooting package |
| Port Forward | Gives an ability to forward any local port to a port on a device, allowing you to connect to any service without the necessity to open ports on the device | Troubleshooting package |
| [Configure](../02.Configure/docs.md) | Lets you apply arbitrary configuration to your devices through a uniform interface | Configure package |

# Add-ons and the Mender Client

Mender Connect is loosely coupled with the Mender Client. The main information passed between
`mender-client` and `mender-connect` is the device authorization status. Since only accepted
devices can interact with the Mender Server, the Mender Client passes over DBus
the authorization token which Mender Connect uses to establish
a [Websocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) connection
to the server. We use the well-known and well-defined open APIs, which makes the solution flexible
and portable.

# Installation

Please refer to the following sections for the Mender Connect installation:
* [mender-convert integration](../../04.System-updates-Debian-family/99.Variables/docs.md#mender_addon_connect_install) for installation in the existing images
* [Yocto projects](../../05.System-updates-Yocto-Project/05.Customize-Mender/docs.md#mender-connect) for the installation in a Yocto Project environment
* [installation with a deb](../../09.Downloads/docs.md#remote-terminal-add-on) for the installation from the Debian package

After installation, please refer to the [add-ons subsections](../../09.Add-ons/chapter.md) for the configuration options,
including the enabling and disabling of the features.

Please note, that you have to enable DBus in the Mender client for most of the add-ons
to function.

# Mender Connect Configuration

We describe the specific add-ons configuration in the following sections. All
Mender Connect based add-ons can share the same configuration file
`/etc/mender/mender-connect.conf`. Which, for example, can look like that:

```
{
    "ClientProtocol": "https",
    "HttpsClient": {
        "Certificate": "/certs/cert.pem",
        "Key": "/keys/key.pem"
    },
    "ServerCertificate": "/certs/hosted.pem",
    "ServerURL": "wss://192.168.1.1",
}
```

## Providing mender-connect.conf

The mechanism for providing the configuration file and specifying the configuration values will depend on your choice of OS distribution or build system.

If you have already built an Artifact containing the rootfs, have a look at [modifying a Mender Artifact](../../06.Artifact-creation/03.Modify-an-Artifact/docs.md).

## Global configuration options

#### HttpsClient

Allows you to configure a client certificate and a private key.

##### Certificate

A path to the file in pem format holding the certificate.

##### Key

A path to a file holding the private key.

#### Servers

An array of json objects on the form `[{"ServerURL":
"https://mender-server.com"}, {"ServerURL": "https://mender-server2.com"},
...]`, where `ServerURL` has the same interpretation as the root [`ServerURL`
attribute](#ServerURL). If `Servers` entry is set, the configuration cannot
contain an additional `ServerURL` entry in the top level of the json
configuration. Upon an unserved request (4XX/5XX-response codes) the client
attempts the next server on the list in the given order. Please note that 
you can also use `"wss://..."` protocol in the URL.

#### ServerURL

The server URL is the basis for API requests. This needs to point to to the
server which runs the Mender server services. It should include the whole URL,
including `https://` and a trailing slash. *NOTE: This entry conflicts with
[`Servers` attribute](#Servers), i.e. the server only accepts one of these entries.*
Please note that you can also use `"wss://..."` protocol in the URL.
You have to specify at least one valid URL for a server to connect to.

#### ServerCertificate

The location of the public certificate of the server, if any. If this
certificate is missing, or the one presented by the server does not match the
one specified in this setting, `mender-connect` validates the server certificate using
standard certificate trust chains.

#### ReconnectIntervalSeconds

The number of seconds to wait between consecutive reconnection attempts.
