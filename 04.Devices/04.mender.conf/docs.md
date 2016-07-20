---
title: mender.conf
taxonomy:
    category: docs
---

The behaviour of the client is controlled by the configuration file
`/etc/mender.conf`. The template is in recipes-mender/mender/files/mender.conf
Here is a typical example:
```
{
  "ClientProtocol": "http",
  "DeviceID": "3a11a5bf-521f-4889-832b-a9d5e2e79f5a",
  "HttpsClient": {
    "Certificate": "",
    "Key": ""
  },
  "RootfsPartA": "/dev/mmcblk0p2",
  "RootfsPartB": "/dev/mmcblk0p3",
  "PollIntervalSeconds": 60,
  "ServerURL": "https://mender.io",
  "ServerCertificate": "/etc/mender/server.crt"
}
```
## The variables
Here is a list of the variables. In some cases, the default value can be
overridden in the build by defining the corresponding Yocto Project (YP)
variable in, for example, local.conf

| Name                | Description                                | Default               | YP variable       |
| ------------------- | ------------------------------------------ | --------------------- | ----------------- |
| ClientProtocol      | Client protocol                            | https                 | -                 |
| DeviceID            | ?                                          |                       | ?                 |
| pollIntervalSeconds | Interval between polls to server (seconds) | 60                    | ?                 |
| RootfsPartA         | Partition number for rootfs A partition    | ?                     | MENDER_ROOTFS_PART_A |
| RootfsPartB         | Partition number for rootfs B partition    | ?                     | MENDER_ROOTFS_PART_B |
| ServerCertificate   | ?                                          |/etc/mender/server.crt | MENDER_CERT_LOCATION |
| ServerURL           | URL of Mender server                       | https://mender.io     | MENDER_SERVER_URL |

TBD: add example YP configuration for hypothetical target board.



TBD: mention recipes-mender/mender/mender_0.1.bb