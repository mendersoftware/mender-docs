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
package architectures.


### Download the package

<!-- AUTOMATION: execute=DEBIAN_FRONTEND=noninteractive apt-get install -y libglib2.0-0 tzdata -->

<!--AUTOVERSION: "downloads.mender.io/%/"/mender "mender-client_%-1"/mender -->
```bash
wget https://downloads.mender.io/3.3.0-build1/dist-packages/debian/$(dpkg --print-architecture)/mender-client_3.3.0-build1-1%2Bdebian%2Bbuster_$(dpkg --print-architecture).deb
```

!!! The above link will use the native architecture. See [the downloads
page](../../09.Downloads/docs.md) for other architectures, and also make sure to modify the
references to the package in commands below.


### Option 1: Attended installation with a wizard

The Mender package comes with an install wizard that will let you configure and
customize your installation. This is the recommended option for new users.

To install and configure Mender run the following command:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "mender-client_%-1"/mender -->
```bash
sudo dpkg -i mender-client_3.3.0-build1-1+debian+buster_$(dpkg --print-architecture).deb
```

After completing the installation wizard, Mender is correctly set up on your
device and automatically starts in [managed
mode](../../02.Overview/01.Introduction/docs.md#client-modes-of-operation). Your
device is now ready to authenticate with the server and start receiving updates.


### Option 2: Unattended installation

Alternatively, install the package non-interactively. This is suitable for
scripts or other situations where no user input is desired.

First, to install Mender without configuring it run the following command:

<!--AUTOVERSION: "mender-client_%-1"/mender -->
```bash
sudo DEBIAN_FRONTEND=noninteractive dpkg -i mender-client_3.3.0-build1-1+debian+buster_$(dpkg --print-architecture).deb
```

The setup is different depending on your server configuration and the most
common cases are shown below. Use `mender setup --help` to learn about all
configuration options.

<!--AUTOMATION: execute=DEVICE_TYPE=device-type -->
<!--AUTOMATION: execute=TENANT_TOKEN=secure-token -->
<!--AUTOMATION: execute=SERVER_IP_ADDR=1.2.3.4 -->
<!--AUTOMATION: execute=SERVER_URL=https://secure.server -->

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="Hosted Mender"]
Set the following variables:

<!--AUTOMATION: ignore -->
```bash
DEVICE_TYPE="<INSERT YOUR DEVICE TYPE>"
TENANT_TOKEN="<INSERT YOUR TOKEN FROM https://hosted.mender.io/ui/#/settings/my-organization>"
```

Configure Mender with:

```bash
sudo mender setup \
            --device-type $DEVICE_TYPE \
            --hosted-mender \
            --tenant-token $TENANT_TOKEN \
            --demo-polling
```
[/ui-tab]
[ui-tab title="Demo server"]
Set the following variables:

<!--AUTOMATION: ignore -->
```bash
DEVICE_TYPE="<INSERT YOUR DEVICE TYPE>"
SERVER_IP_ADDR="<INSERT THE IP ADDRESS OF YOUR DEMO SERVER>"
```

Configure Mender with:

```bash
sudo mender setup \
            --device-type $DEVICE_TYPE \
            --demo-server \
            --server-ip $SERVER_IP_ADDR \
            --demo-polling
```
[/ui-tab]
[ui-tab title="[Enterprise](https://mender.io/products/mender-enterprise?target=_blank) server"]
Set the following variables:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "downloads.mender.io/%/"/mender "mender-client_%-1"/mender -->
```bash
DEVICE_TYPE="<INSERT YOUR DEVICE TYPE>"
SERVER_URL="<INSERT YOUR ENTERPRISE SERVER URL>"
TENANT_TOKEN="<INSERT YOUR TOKEN FROM YOUR ENTERPRISE SERVER>"
```

Configure Mender with:

```bash
sudo mender setup \
            --device-type $DEVICE_TYPE \
            --server-url $SERVER_URL \
            --server-cert="" \
            --tenant-token $TENANT_TOKEN \
            --demo-polling
```
[/ui-tab]
[/ui-tabs]

Finally, to restart the Mender service for the new configuration to take effect run the following command:

<!--AUTOMATION: ignore -->
```bash
sudo systemctl restart mender-client
```

## Install from source

<!--AUTOVERSION: "mender/tree/%#installing-from-source"/mender -->
As an alternative to using a Debian package, it is possible to install the
Mender client from source by following the guidelines outlined in the
[README.md](https://github.com/mendersoftware/mender/tree/3.3.0-build1#installing-from-source?target=_blank)
of the Mender client source repository.



