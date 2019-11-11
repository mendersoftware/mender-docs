---
title: Installing
taxonomy:
    category: docs
---

This page describes how to install the Mender client in an existing Linux system. Installing this way does not offer a full Mender integration. However, it is possible to use Update Modules and update parts of the system.

If full board integration is desired, follow the device documentation on [Yocto Project](../../devices/yocto-project) or [Debian family](../../devices/debian-family).

## Install from source

<!--AUTOVERSION: "mender/tree/%#installing-from-source"/mender -->
It is possible to install the Mender client from source by following the guidelines outlined in the [README.md](https://github.com/mendersoftware/mender/tree/master#installing-from-source) of the Mender client source repository.

## Install Mender provided Debian package

A Debian package (`.deb`) is provided for convenience to install on e.g Debian, Ubuntu or Raspbian. We provide packages for the following architectures:

- armhf (ARM-v6): ARM 32bit distributions, for example Raspbian for Raspberry Pi or Debian for BeagleBone.
- arm64: (ARM-v8): ARM 64bit processors, for example Debian for Asus Tinker Board
- amd64: Generic 64-bit x86 processors, the most popular among workstations

Download the package:

<!--AUTOVERSION: "cloudfront.net/%/"/mender "mender-client_%-1_armhf.deb"/mender -->
```bash
wget https://d1b0l86ne08fsf.cloudfront.net/master/dist-packages/debian/armhf/mender-client_master-1_armhf.deb
```

!!!Note that the above link is for armhf devices. Adjust the url for your architecture accordingly

The Mender package comes with a wizard that will let you easily configure and
customize your installation. To install and configure Mender run the following
command:

<!--AUTOVERSION: "mender-client_%-1_armhf.deb"/mender -->
```bash
sudo dpkg -i mender-client_master-1_armhf.deb
```

After the installation wizard is completed, Mender is correctly setup on your
device and will automatically start in [managed
mode](../../architecture/overview#modes-of-operation). Your device is now ready
to authenticate with the server and start receiving updates.

## Unattended installation

Alternatively to the above method, the package can be installed in a
non-interactive way, suitable for scripts or other situations where no user
input is desired.

Here are presented three common use cases as examples, use `mender setup --help`
to learn about all configuration options. Use the below scripts to download and
setup the Mender client on different scenarios.

- Connecting to Mender Professional with demo settings

<!--AUTOVERSION: "cloudfront.net/%/"/mender "mender-client_%-1_armhf.deb"/mender -->
```bash
DEVICE_TYPE="<INSERT YOUR DEVICE TYPE>"
TENANT_TOKEN="<INSERT YOUR TOKEN FROM https://hosted.mender.io/ui/#/settings/my-organization>"
wget https://d1b0l86ne08fsf.cloudfront.net/master/dist-packages/debian/armhf/mender-client_master-1_armhf.deb
sudo DEBIAN_FRONTEND=noninteractive dpkg -i mender-client_master-1_armhf.deb
sudo mender setup \
            --device-type $DEVICE_TYPE \
            --mender-professional \
            --tenant-token $TENANT_TOKEN \
            --retry-poll 30 \
            --update-poll 5 \
            --inventory-poll 5
sudo systemctl restart mender-client
```

- Connecting to a demo server with demo settings

<!--AUTOVERSION: "cloudfront.net/%/"/mender "mender-client_%-1_armhf.deb"/mender -->
```bash
DEVICE_TYPE="<INSERT YOUR DEVICE TYPE>"
SERVER_IP_ADDR="<INSERT THE IP ADDRESS OF YOUR DEMO SERVER>"
wget https://d1b0l86ne08fsf.cloudfront.net/master/dist-packages/debian/armhf/mender-client_master-1_armhf.deb
sudo DEBIAN_FRONTEND=noninteractive dpkg -i mender-client_master-1_armhf.deb
sudo mender setup \
            --device-type $DEVICE_TYPE \
            --demo \
            --server-ip $SERVER_IP_ADDR
sudo systemctl restart mender-client
```

- Connecting to an Enterprise server

<!--AUTOVERSION: "cloudfront.net/%/"/mender "mender-client_%-1_armhf.deb"/mender -->
```bash
DEVICE_TYPE="<INSERT YOUR DEVICE TYPE>"
SERVER_URL="<INSERT YOUR ENTERPRISE SERVER URL>"
TENANT_TOKEN="<INSERT YOUR TOKEN FROM YOUR ENTERPRISE SERVER>"
wget https://d1b0l86ne08fsf.cloudfront.net/master/dist-packages/debian/armhf/mender-client_master-1_armhf.deb
sudo DEBIAN_FRONTEND=noninteractive dpkg -i mender-client_master-1_armhf.deb
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

## Additional information

! There are security implications to connecting a client and server for the first time, also known as *bootstrapping*. If a client and server have not exchanged any information in advance, they need to accept each other on trust this first time, with the risk that the information the other party presents is spoofed. To mitigate this risk, the Mender client preinstalls the TLS certificate of the server when it is provisioned, as part of the Yocto Project image build. So it is not possible for a rogue server to intercept the connection from a client or pretend to be a different server, assuming server's private TLS key is securely managed. A rogue device can still spoof the information it sends to the server in order to be authorized, and this is why Mender asks you to make the authorization decision. However, the risk of letting the server manage a rogue device is much lower than the risk of a rogue server managing devices.

