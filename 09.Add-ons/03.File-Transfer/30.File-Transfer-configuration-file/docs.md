---
title: Configuration file
taxonomy:
    category: docs
---

You can enable or disable the File Transfer from the Mender Connect configuration 
file `/etc/mender/mender-connect.conf`.

# Example mender-connect.conf file

Here is an example of a `mender-connect.conf` file with the File Transfer enabled:
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
    "FileTransfer": {
      "Disable": false
    }
}
```

# Providing mender-connect.conf

The mechanism for providing the configuration file and specifying the configuration values will depend on your choice of OS distribution or build system.

If you have already built an Artifact containing the rootfs, have a look at [modifying a Mender Artifact](../../../06.Artifact-creation/03.Modify-an-Artifact/docs.md).


