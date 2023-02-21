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
Debian, Ubuntu or Raspberry Pi OS.

See the instructions in our [downloads
section](../../10.Downloads/docs.md#install-using-the-apt-repository) for the
explicit steps required.

### Configure the mender-client

The setup is different depending on your server configuration and the most
common cases are shown below. Use `mender setup --help` to learn about all
configuration options.

<!-- AUTOMATION: execute=DEBIAN_FRONTEND=noninteractive apt-get install --assume-yes wget libglib2.0-0 tzdata -->

<!--AUTOVERSION: "repos/debian/pool/%/"/ignore "mender-client_%-1"/mender -->
<!--AUTOMATION: execute=wget https://downloads.mender.io/repos/debian/pool/main/m/mender-client/mender-client_3.5.0-1%2Bdebian%2Bbullseye_$(dpkg --print-architecture).deb -->

<!--AUTOVERSION: "mender-client_%-1"/mender -->
<!--AUTOMATION: execute=DEBIAN_FRONTEND=noninteractive dpkg -i mender-client_3.5.0-1+debian+bullseye_$(dpkg --print-architecture).deb -->
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
[README.md](https://github.com/mendersoftware/mender/tree/3.5.0#installing-from-source?target=_blank)
of the Mender client source repository.



