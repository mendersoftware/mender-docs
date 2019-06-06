---
title: Downloads
taxonomy:
    category: docs
---

## Mender Artifact

To download `mender-artifact` as an standalone tool, follow the correct link
according to your host platform:

<!--AUTOVERSION: "mender-artifact %"/mender-artifact -->
| Platform | Download link                                                |
|----------|--------------------------------------------------------------|
| Linux    | [mender-artifact master][x.x.x_mender-artifact-linux]     |
| Mac OS X | [mender-artifact master][x.x.x_mender-artifact-darwin] |

Remember to add execute permission (e.g. with `chmod +x mender-artifact`).

!!! If you need to build `mender-artifact` from source, please see [Compiling mender-artifact](../artifacts/modifying-a-mender-artifact#compiling-mender-artifact).

<!--AUTOVERSION: "mender-artifact/%/"/mender-artifact -->
[x.x.x_mender-artifact-linux]: https://d1b0l86ne08fsf.cloudfront.net/mender-artifact/master/linux/mender-artifact
<!--AUTOVERSION: "mender-artifact/%/"/mender-artifact -->
[x.x.x_mender-artifact-darwin]: https://d1b0l86ne08fsf.cloudfront.net/mender-artifact/master/darwin/mender-artifact


## Mender client

A Debian package (`.deb`) is provided for convenience to install on e.g Debian, Ubuntu or Raspbian. We provide packages for the following architectures:

<!--AUTOVERSION: "mender-client_%-1"/mender -->
| Architecture   | Devices                                   | Download link                                                       |
|----------------|-------------------------------------------|---------------------------------------------------------------------|
| armhf (ARM-v6) | Raspberry Pi, BeagleBone, other ARM based | [mender-client_master-1_armhf.deb][mender-client_x.x.x-1_armhf.deb] |

<!--AUTOVERSION: "cloudfront.net/%/"/mender "mender-client_%-1_armhf.deb"/mender -->
[mender-client_x.x.x-1_armhf.deb]: https://d1b0l86ne08fsf.cloudfront.net/master/dist-packages/debian/armhf/mender-client_master-1_armhf.deb
