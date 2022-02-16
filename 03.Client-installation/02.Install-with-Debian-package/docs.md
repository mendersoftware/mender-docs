---
title: Installing
taxonomy:
    category: docs
---

This page describes how to install the Mender client on an existing Linux
system. Installing Mender this way does not offer a full Mender board
integration, so you can not carry out full system updates, however, it is
possible to use Update Modules to update applications and other parts of the
system.

If you need the full board integration, follow the device documentation
in [System Updates: Yocto Project](../../05.System-updates-Yocto-Project/chapter.md)
or [System Updates: Debian family](../../04.System-updates-Debian-family/chapter.md).


## Install Mender using the Debian package

Mender provides a Debian package (`.deb`) for convenience to install on e.g
Debian, Ubuntu or Raspberry Pi OS. The package supports the following
architectures:

- armhf (ARM-v6): ARM 32bit distributions, for example Raspberry Pi OS for Raspberry Pi or Debian for BeagleBone.
- arm64: (ARM-v8): ARM 64bit processors, for example Debian for Asus Tinker Board
- amd64: Generic 64-bit x86 processors, the most popular among workstations

See [the downloads page](../../09.Downloads/docs.md) for links to download all
package architectures. We will assume *armhf* in the following instructions as
this is the most common for users getting starting with Mender.


### Download the package

<!--AUTOVERSION: "downloads.mender.io/%/"/mender "mender-client_%-1"/mender -->
```bash
wget https://downloads.mender.io/3.0.2/dist-packages/debian/armhf/mender-client_3.0.2-1%2Bdebian%2Bbuster_armhf.deb
```

!!! The above link is for *armhf* devices, which is the most common device architecture. See [the downloads page](../../09.Downloads/docs.md) for other architectures, and also make sure to modify the references to the package in commands below.


### Option 1: Attended installation with a wizard

The Mender package comes with an install wizard that will let you configure and
customize your installation. This is the recommended option for new users.

To install and configure Mender run the following command:

<!--AUTOVERSION: "mender-client_%-1"/mender -->
```bash
sudo dpkg -i mender-client_3.0.2-1+debian+buster_armhf.deb
```

After completing the installation wizard, Mender is correctly set up on your
device and automatically starts in [managed
mode](../../02.Overview/01.Introduction/docs.md#client-modes-of-operation). Your
device is now ready to authenticate with the server and start receiving updates.


### Option 2: Unattended installation

Alternatively, install the package non-interactively. This is suitable for
scripts or other situations where no user input is desired.

The setup is different depending on your server configuration and the most
common cases are shown below. Use `mender setup --help` to learn about all
configuration options.

- Connecting to [hosted Mender](https://hosted.mender.io?target=_blank) using demo settings

<!--AUTOVERSION: "downloads.mender.io/%/"/mender "mender-client_%-1"/mender -->
```bash
DEVICE_TYPE="<INSERT YOUR DEVICE TYPE>"
TENANT_TOKEN="<INSERT YOUR TOKEN FROM https://hosted.mender.io/ui/#/settings/my-organization>"
sudo DEBIAN_FRONTEND=noninteractive dpkg -i mender-client_3.0.2-1+debian+buster_armhf.deb
sudo mender setup \
            --device-type $DEVICE_TYPE \
            --hosted-mender \
            --tenant-token $TENANT_TOKEN \
            --retry-poll 30 \
            --update-poll 5 \
            --inventory-poll 5
sudo systemctl restart mender-client
```

- Connecting to a demo server using demo settings

<!--AUTOVERSION: "downloads.mender.io/%/"/mender "mender-client_%-1"/mender -->
```bash
DEVICE_TYPE="<INSERT YOUR DEVICE TYPE>"
SERVER_IP_ADDR="<INSERT THE IP ADDRESS OF YOUR DEMO SERVER>"
sudo DEBIAN_FRONTEND=noninteractive dpkg -i mender-client_3.0.2-1+debian+buster_armhf.deb
sudo mender setup \
            --device-type $DEVICE_TYPE \
            --demo \
            --server-ip $SERVER_IP_ADDR
sudo systemctl restart mender-client
```

- Connecting to an [Enterprise](https://mender.io/products/mender-enterprise?target=_blank) server

<!--AUTOVERSION: "downloads.mender.io/%/"/mender "mender-client_%-1"/mender -->
```bash
DEVICE_TYPE="<INSERT YOUR DEVICE TYPE>"
SERVER_URL="<INSERT YOUR ENTERPRISE SERVER URL>"
TENANT_TOKEN="<INSERT YOUR TOKEN FROM YOUR ENTERPRISE SERVER>"
sudo DEBIAN_FRONTEND=noninteractive dpkg -i mender-client_3.0.2-1+debian+buster_armhf.deb
sudo mender setup \
            --device-type $DEVICE_TYPE \
            --server-url $SERVER_URL \
            --server-cert="" \
            --tenant-token $TENANT_TOKEN \
            --retry-poll 30 \
            --update-poll 5 \
            --inventory-poll 5
sudo systemctl restart mender-client
```

## Install from source

<!--AUTOVERSION: "mender/tree/%#installing-from-source"/mender -->
As an alternative to using a Debian package, it is possible to install the
Mender client from source by following the guidelines outlined in the
[README.md](https://github.com/mendersoftware/mender/tree/3.0.2#installing-from-source?target=_blank)
of the Mender client source repository.



