---
title: Downloads
taxonomy:
    category: docs
---

## Disk images

These disk images (`*.img` or `*.sdimg`) are based on images provided by board
manufacturers and already have Mender fully integrated. They are used to
provision the device storage for devices without Mender running already.

Mender provides images based on the following distributions:

* Images for **Raspberry Pi 3** and **Raspberry Pi 4**, which are based on the
  [Raspberry Pi OS Linux
  distribution](https://www.raspberrypi.org/downloads/raspberry-pi-os/?target=_blank)

!! Note that we do not offer commercial support for these images. They are based
!! on images supported by board manufacturers, like the Raspberry Pi Foundation,
!! and provide the same software and configuration options as the original
!! images. Please use the support resources available from the board
!! manufacturer, or [contact us](mailto:contact@mender.io) if you have any
!! questions on the Mender integration.

| Board                         | OS                              | Disk image                                                                                         | Storage size |
|-------------------------------|---------------------------------|----------------------------------------------------------------------------------------------------|--------------|
| Raspberry Pi 3 Model B and B+ | Raspberry Pi OS Buster Lite 2020-05-27 | [raspios-buster-lite-raspberrypi3-mender.img.xz][raspios-buster-lite-raspberrypi3-mender.img.xz] | 8 GB         |
| Raspberry Pi 4 Model B        | Raspberry Pi OS Buster Lite 2020-05-27 | [raspios-buster-lite-raspberrypi4-mender.img.xz][raspios-buster-lite-raspberrypi4-mender.img.xz] | 8 GB         |

<!--AUTOVERSION: "mender-%.img.xz"/mender-convert-client -->
[raspios-buster-lite-raspberrypi3-mender.img.xz]: https://d4o6e0uccgv40.cloudfront.net/2020-05-27-raspios-buster-lite-armhf/arm/2020-05-27-raspios-buster-lite-armhf-raspberrypi3-mender-2.3.0b1.img.xz
[raspios-buster-lite-raspberrypi4-mender.img.xz]: https://d4o6e0uccgv40.cloudfront.net/2020-05-27-raspios-buster-lite-armhf/arm/2020-05-27-raspios-buster-lite-armhf-raspberrypi4-mender-2.3.0b1.img.xz

You can find images for other devices in our Mender Hub community forum, see
[Debian Family](https://hub.mender.io/c/board-integrations/debian-family/11) or
[Yocto Project](https://hub.mender.io/c/board-integrations/yocto-project/10)
integration posts.

## Mender Artifact

To download `mender-artifact` as an standalone tool, follow the correct link
according to your host platform:

<!--AUTOVERSION: "mender-artifact %"/mender-artifact -->
| Platform | Download link                                                |
|----------|--------------------------------------------------------------|
| Linux    | [mender-artifact 3.4.0][x.x.x_mender-artifact-linux]     |
| Mac OS X | [mender-artifact 3.4.0][x.x.x_mender-artifact-darwin] |

Remember to add execute permission (e.g. with `chmod +x mender-artifact`).

Note that you need to ensure that the mender-artifact utility is in a directory that is specified in your [PATH environment variable](https://en.wikipedia.org/wiki/PATH_(variable)?target=_blank). Most systems automatically have `/usr/local/bin` in your PATH so the following should allow proper execution and location of this binary. Please refer to your host Operating System documentation for more details.

```bash
$ sudo mv mender-artifact /usr/local/bin/
```

!!! If you need to build `mender-artifact` from source, please see [Compiling mender-artifact](../artifacts/modifying-a-mender-artifact#compiling-mender-artifact).

<!--AUTOVERSION: "mender-artifact/%/"/mender-artifact -->
[x.x.x_mender-artifact-linux]: https://d1b0l86ne08fsf.cloudfront.net/mender-artifact/3.4.0/linux/mender-artifact
<!--AUTOVERSION: "mender-artifact/%/"/mender-artifact -->
[x.x.x_mender-artifact-darwin]: https://d1b0l86ne08fsf.cloudfront.net/mender-artifact/3.4.0/darwin/mender-artifact

_Mac OS X note_: Please remember, that `mender-artifact` when working with
disk image files (e.g.: `*.sdimg`, `*.img`, or others holding the storage
partitions) under Mac OS X has limited functionalities, and commands like 
`mender-artifact cat` or `mender-artifact cp` will not work, due to lack
of support for certain utilities on the Mac platform.

## Mender client

A Debian package (`.deb`) is provided for convenience to install on e.g Debian,
Ubuntu or Raspberry Pi OS. We provide packages for the following architectures:

<!--AUTOVERSION: "mender-client_%-1"/mender -->
| Architecture   | Devices                                   | Download link                                                       |
|----------------|-------------------------------------------|---------------------------------------------------------------------|
| armhf (ARM-v6) | ARM 32bit distributions, for example Raspberry Pi OS for Raspberry Pi or Debian for BeagleBone | [mender-client_2.3.0-1_armhf.deb][mender-client_x.x.x-1_armhf.deb] |
| arm64 | ARM 64bit processors, for example Debian for Asus Tinker Board | [mender-client_2.3.0-1_arm64.deb][mender-client_x.x.x-1_arm64.deb] |
| amd64 | Generic 64-bit x86 processors, the most popular among workstations | [mender-client_2.3.0-1_amd64.deb][mender-client_x.x.x-1_amd64.deb] |

<!--AUTOVERSION: "cloudfront.net/%/"/mender "mender-client_%-1_armhf.deb"/mender -->
[mender-client_x.x.x-1_armhf.deb]: https://d1b0l86ne08fsf.cloudfront.net/2.3.0/dist-packages/debian/armhf/mender-client_2.3.0-1_armhf.deb
<!--AUTOVERSION: "cloudfront.net/%/"/mender "mender-client_%-1_arm64.deb"/mender -->
[mender-client_x.x.x-1_arm64.deb]: https://d1b0l86ne08fsf.cloudfront.net/2.3.0/dist-packages/debian/arm64/mender-client_2.3.0-1_arm64.deb
<!--AUTOVERSION: "cloudfront.net/%/"/mender "mender-client_%-1_amd64.deb"/mender -->
[mender-client_x.x.x-1_amd64.deb]: https://d1b0l86ne08fsf.cloudfront.net/2.3.0/dist-packages/debian/amd64/mender-client_2.3.0-1_amd64.deb

## Mender CLI

To download `mender-cli`, follow the correct link according to your host
platform:

<!--AUTOVERSION: "mender-cli %"/mender-cli -->
| Platform | Download link                                                |
|----------|--------------------------------------------------------------|
| Linux    | [mender-cli 1.4.0][x.x.x_mender-cli-linux]                  |
| Mac OS X | [mender-cli 1.4.0][x.x.x_mender-cli-darwin]                 |

Remember to add execute permission (e.g. with `chmod +x mender-cli`).

Note that you need to ensure that the mender-cli utility is in a directory that is specified in your [PATH environment variable](https://en.wikipedia.org/wiki/PATH_(variable)?target=_blank). Most systems automatically have `/usr/local/bin` in your PATH so the following should allow proper execution and location of this binary. Please refer to your host Operating System documentation for more details.

```bash
$ sudo mv mender-cli /usr/local/bin/
```

<!--AUTOVERSION: "mender-cli/%/"/mender-cli -->
[x.x.x_mender-cli-linux]: https://d1b0l86ne08fsf.cloudfront.net/mender-cli/1.4.0/linux/mender-cli
<!--AUTOVERSION: "mender-cli/%/"/mender-cli -->
[x.x.x_mender-cli-darwin]: https://d1b0l86ne08fsf.cloudfront.net/mender-cli/1.4.0/darwin/mender-cli
