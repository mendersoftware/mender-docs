---
title: Disk images
taxonomy:
    category: docs
markdown:
    extra: true
process:
    twig: true
---

<!-- AUTOMATION: execute=if [ "$TEST_ENTERPRISE" -ne 1 ]; then echo "TEST_ENTERPRISE must be set to 1!"; exit 1; fi -->

# Disk images

These disk images (`*.img` or `*.sdimg`) are based on images provided by board
manufacturers and are ready to install the Mender Client. They are used to
provision the device storage for devices without Mender running already.

Mender provides images based on the following distributions:

* Images for **Raspberry Pi 3** and **Raspberry Pi 4**, which are based on the
  [Raspberry Pi OS Linux
  distribution](https://www.raspberrypi.com/software/operating-systems/?target=_blank)

!! Note that we do not offer commercial support for these images. They are based
!! on images supported by board manufacturers, like the Raspberry Pi Foundation,
!! and provide the same software and configuration options as the original
!! images. Please use the support resources available from the board
!! manufacturer, or [contact us](mailto:contact@mender.io) if you have any
!! questions on the Mender integration.

| Board                         | OS                              | Disk image                                                                                         | Storage size |
|-------------------------------|---------------------------------|----------------------------------------------------------------------------------------------------|--------------|
| Raspberry Pi 3 Model B and B+ | Raspberry Pi OS Bookworm Lite 2024-10-22 | [raspios-lite-raspberrypi3_bookworm_64bit-mender-convert.img.xz][raspios-lite-raspberrypi3_bookworm_64bit-mender-convert.img.xz] | 8 GB         |
| Raspberry Pi 4 Model B        | Raspberry Pi OS Bookworm Lite 2024-10-22 | [raspios-lite-raspberrypi4_bookworm_64bit-mender-convert.img.xz][raspios-lite-raspberrypi4_bookworm_64bit-mender-convert.img.xz] | 8 GB         |

<!--AUTOVERSION: "mender-convert-%.img.xz"/mender-convert -->
[raspios-lite-raspberrypi3_bookworm_64bit-mender-convert.img.xz]: https://d4o6e0uccgv40.cloudfront.net/2024-10-22-raspios-lite/arm/2024-10-22-raspios-lite-raspberrypi3_bookworm_64bit-mender-convert-5.0.0.img.xz
[raspios-lite-raspberrypi4_bookworm_64bit-mender-convert.img.xz]: https://d4o6e0uccgv40.cloudfront.net/2024-10-22-raspios-lite/arm/2024-10-22-raspios-lite-raspberrypi4_bookworm_64bit-mender-convert-5.0.0.img.xz

You can find images for other devices in our Mender Hub community forum, see
[Debian Family](https://hub.mender.io/c/board-integrations/debian-family/11?target=_blank) or
[Yocto Project](https://hub.mender.io/c/board-integrations/yocto-project/10?target=_blank)
integration posts.


