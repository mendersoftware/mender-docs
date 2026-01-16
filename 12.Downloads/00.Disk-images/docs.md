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

* Images for **Raspberry Pi 4** and **Raspberry Pi 5**, which are based on the
  [Raspberry Pi OS Linux
  distribution](https://www.raspberrypi.com/software/operating-systems/?target=_blank)

!! Note that we do not offer commercial support for these images. They are based
!! on images supported by board manufacturers, like the Raspberry Pi Foundation,
!! and provide the same software and configuration options as the original
!! images. Please use the support resources available from the board
!! manufacturer, or [contact us](mailto:contact@mender.io) if you have any
!! questions on the Mender integration.

!!! The RPi5 integration with mender-convert currently uses a separate U-Boot binary with \`CONFIG_BOOTDELAY=-2\`
!!! for our RPi5 images.
!!! This is a workaround for an issue where RPi5 with U-Boot is stuck waiting for UART.

| Board                         | OS                              | Disk image                                                                                         | Storage size |
|-------------------------------|---------------------------------|----------------------------------------------------------------------------------------------------|--------------|
| Raspberry Pi 4 Model B        | Raspberry Pi OS Trixie Lite 2025-10-01 | [raspios-lite-raspberrypi4_trixie_64bit-mender-convert.img.xz][raspios-lite-raspberrypi4_trixie_64bit-mender-convert.img.xz] | 8 GB |
| Raspberry Pi 5                | Raspberry Pi OS Trixie Lite 2025-10-01 | [raspios-lite-raspberrypi5_trixie_64bit-mender-convert.img.xz][raspios-lite-raspberrypi5_trixie_64bit-mender-convert.img.xz]     | 8 GB |

<!--
IMPORTANT: When updating the disk images, also remember to update https://docs.mender.io/releases/rpi_imager_schema.json
           You can find the json in the mender-docs-site repository.
           `url`, `release_date`, `image_download_size` and `extract_sha256` must all be updated and correspond to the images listed here
-->
<!--AUTOVERSION: "mender-convert-%.img.xz"/mender-convert -->
[raspios-lite-raspberrypi4_trixie_64bit-mender-convert.img.xz]: https://d4o6e0uccgv40.cloudfront.net/2025-10-01-raspios-lite/arm/2025-10-01-raspios-lite-raspberrypi4_trixie_64bit-mender-convert-5.1.0.img.xz
[raspios-lite-raspberrypi5_trixie_64bit-mender-convert.img.xz]: https://d4o6e0uccgv40.cloudfront.net/2025-10-01-raspios-lite/arm/2025-10-01-raspios-lite-raspberrypi5_trixie_64bit-mender-convert-5.1.0.img.xz

You can find images for other devices in our Mender Hub community forum, see
[Debian Family](https://hub.mender.io/c/board-integrations/debian-family/11?target=_blank) or
[Yocto Project](https://hub.mender.io/c/board-integrations/yocto-project/10?target=_blank)
integration posts.


