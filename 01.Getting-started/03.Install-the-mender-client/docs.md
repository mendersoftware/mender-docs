---
title: Install the Mender client
taxonomy:
    category: docs
---

! It is strongly recommended you **complete the Mender server onboarding to connect your first device** as outlined in [install a Mender demo server](../create-a-test-environment#open-the-mender-ui) before proceeding.

Your devices first need to have the Mender client running on them in order to connect to the server.
There are two approaches to this, depending on what kind of updates you want to do.

### Application updates

###### (Recommended for new users)

Installing this way does not offer a full Mender integration. However, it is possible to use Update Modules and update parts of the system.

For partial updates such as application updates, you can [install Mender on your device using a .deb package](../../client-configuration/installing#install-mender-provided-debian-package). This is the quickest and easiest way to get started with Mender. A detailed introduction to partial updates using update modules can be found [here](../../devices/update-modules).

### System updates

The most robust approach is full rootfs system updates. This approach also enables support for partial updates, but there are some device partition layout requirements so the board integration is more effort.

For this, the Mender client needs to be integrated as part of the disk image, which can be done by [building with Yocto](../../devices/yocto-project) or [converting an existing Debian disk image](../../devices/debian-family). Check out the board integrations at [Mender Hub](https://hub.mender.io/c/board-integrations) to see if your board has already been integrated. There are over 40 different board and OS combinations, and more being added by the community. If you would like professional assistance supporting your board and OS, please refer to the [commercial device support offering](https://mender.io/product/board-support?target=_blank).
