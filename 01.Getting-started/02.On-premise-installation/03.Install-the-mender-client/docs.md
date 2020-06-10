---
title: Install the Mender client
taxonomy:
    category: docs
---

! It is strongly recommended you **complete the Mender server onboarding to connect your first device** as outlined in [install a Mender demo server](../02.Create-a-test-environment/docs.md#open-the-mender-ui) before proceeding.

Your devices first need to have the Mender client running on them in order to connect to the server.
There are two approaches to this, depending on what kind of updates you want to do.

### Application updates

###### (Recommended for new users)

Installing this way does not offer a full Mender integration. However, it is possible to use Update Modules and update parts of the system.

For partial updates such as application updates, you can [install Mender on your device using a .deb package](../../../05.Client-configuration/06.Installing/docs.md#install-mender-using-the-debian-package). This is the quickest and easiest way to get started with Mender. A detailed introduction to partial updates using update modules can be found [here](../../../03.Devices/10.Update-Modules/docs.md).

### System updates

The most robust approach is full rootfs system updates. This approach also enables support for partial updates, but there are some device partition layout requirements so the board integration is more effort.

For this, the Mender client needs to be integrated as part of the disk image,
which can be done by [building with Yocto](../../../03.Devices/02.Yocto-project/docs.md) or
[converting an existing Debian disk image](../../../03.Devices/03.Debian-family/docs.md).
Check out [the Downloads section](../../../08.Downloads/docs.md#disk-images) to the disk
image for your board, or the board integrations at
[Mender Hub](https://hub.mender.io/c/board-integrations) to see if your board
has already been integrated. There are over 40 different board and OS
combinations, and more being added by the community. If you would like
professional assistance supporting your board and OS, please refer to the
[commercial device support offering](https://mender.io/support-and-services/board-integration?target=_blank).

If you have a Raspberry Pi 3 or a Raspberry Pi 4, you can test out system
updates by following the tutorial [deploy a system update
demo](../04.Deploy-a-system-update-demo/docs.md).
