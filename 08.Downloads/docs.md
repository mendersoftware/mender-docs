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

A Debian package (`.deb`) is provided for convenience to install on e.g Debian,
Ubuntu or Raspbian. We provide packages for the following architectures:

<!--AUTOVERSION: "mender-client_%-1"/mender -->
| Architecture   | Devices                                   | Download link                                                       |
|----------------|-------------------------------------------|---------------------------------------------------------------------|
| armhf (ARM-v6) | ARM 32bit distributions, for example Raspbian for Raspberry Pi or Debian for BeagleBone | [mender-client_master-1_armhf.deb][mender-client_x.x.x-1_armhf.deb] |
| arm64 | ARM 64bit processors, for example Debian for Asus Tinker Board | [mender-client_master-1_arm64.deb][mender-client_x.x.x-1_arm64.deb] |
| amd64 | Generic 64-bit x86 processors, the most popular among workstations | [mender-client_master-1_amd64.deb][mender-client_x.x.x-1_amd64.deb] |

<!--AUTOVERSION: "cloudfront.net/%/"/mender "mender-client_%-1_armhf.deb"/mender -->
[mender-client_x.x.x-1_armhf.deb]: https://d1b0l86ne08fsf.cloudfront.net/master/dist-packages/debian/armhf/mender-client_master-1_armhf.deb
<!--AUTOVERSION: "cloudfront.net/%/"/mender "mender-client_%-1_arm64.deb"/mender -->
[mender-client_x.x.x-1_arm64.deb]: https://d1b0l86ne08fsf.cloudfront.net/master/dist-packages/debian/arm64/mender-client_master-1_arm64.deb
<!--AUTOVERSION: "cloudfront.net/%/"/mender "mender-client_%-1_amd64.deb"/mender -->
[mender-client_x.x.x-1_amd64.deb]: https://d1b0l86ne08fsf.cloudfront.net/master/dist-packages/debian/amd64/mender-client_master-1_amd64.deb

## Mender CLI

To download `mender-cli`, follow the correct link according to your host
platform:

<!--AUTOVERSION: "mender-cli %"/mender-cli -->
| Platform | Download link                                                |
|----------|--------------------------------------------------------------|
| Linux    | [mender-cli master][x.x.x_mender-cli-linux]                  |
| Mac OS X | [mender-cli master][x.x.x_mender-cli-darwin]                 |

Remember to add execute permission (e.g. with `chmod +x mender-cli`).

<!--AUTOVERSION: "mender-cli/%/"/mender-cli -->
[x.x.x_mender-cli-linux]: https://d1b0l86ne08fsf.cloudfront.net/mender-cli/master/linux/mender-cli
<!--AUTOVERSION: "mender-cli/%/"/mender-cli -->
[x.x.x_mender-cli-darwin]: https://d1b0l86ne08fsf.cloudfront.net/mender-cli/master/darwin/mender-cli
