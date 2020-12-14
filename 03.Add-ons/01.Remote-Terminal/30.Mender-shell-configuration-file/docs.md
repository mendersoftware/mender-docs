---
title: Mender-shell configuration file
taxonomy:
    category: docs
---

Mender-shell client's add-on configuration resides in `/etc/mender/mender-shell.conf`
on the root filesystem. This file is JSON structured and defines various
parameters for Mender-shell operation.

# Example mender-shell.conf file

Here is an example of a `mender.conf` file:
```
{
    "ClientProtocol": "https",
    "HttpsClient": {
        "Certificate": "/certs/cert.pem",
        "Key": "/keys/key.pem"
    },
    "ServerCertificate": "/certs/hosted.pem",
    "ServerURL": "wss://192.168.1.1",
    "User": "mender",
    "Terminal": {
        "Height": 24,
        "Width": 128
    },
    "Sessions": {
      "StopExpired": false,
      "ExpireAfter": 255,
      "ExpireAfterIdle": 16,
      "MaxPerUser": 4
    }
}
```

# Providing mender-shell.conf

The mechanism for providing the configuration file and specifying the configuration values will depend on your choice of OS distribution or build system.

If you have already built an Artifact containing the rootfs, have a look at [modifying a Mender Artifact](../../../06.Artifact-creation/03.Modify-an-Artifact/docs.md).



