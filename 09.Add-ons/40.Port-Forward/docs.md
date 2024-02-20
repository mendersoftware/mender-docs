---
title: Port forward
taxonomy:
    category: docs
    label: user guide
---

!!!!! The Mender Troubleshoot add-on package is required.
!!!!! See [the Mender features page](https://mender.io/product/features?target=_blank)
!!!!! for an overview of all Mender plans and features.

The Mender Troubleshoot add-on package includes the ability to forward TCP/UDP
traffic securely to a remote device utilizing the bidirectional communication
channel already in use by `mender-connect`. Port forwarding allows you to troubleshoot
services on the device's local area network without exposing open ports to the
Internet. As a special case you can forward traffic on your workstation to a
local port on the device without opening any additional ports.

## Prerequisites

To enable port forwarding, you will need to install and configure the necessary
software on the device and your workstation.
* Install [mender-connect](../../10.Downloads/docs.md#mender-connect) on the
  device.
  * Enable port forwarding for [mender-connect
    configuration](../90.Mender-Connect/docs.md#port-forward-configuration). 
* Install [mender-auth](../../03.Client-installation/02.Install-with-Debian-package/docs.md) on the
  device.
  * [Accept](../../01.Get-started/01.Preparation/01.Prepare-a-Raspberry-Pi-device/docs.md#step-7-accept-the-device)
    the device on the Mender Server.
* Install [mender-cli](../../10.Downloads/docs.md#mender-cli) on your workstation.
  

## Port forwarding

Having the device setup, you can *port forward* traffic from your workstation
using the `mender-cli port-forward` command:
```bash
mender-cli port-forward <Device ID> [tcp|udp/][LOCAL_PORT:[REMOTE_HOST:]]REMOTE_PORT
```
Obtain the Device ID from the device list in the [Mender
UI](https://hosted.mender.io/ui#/devices). 
!!!! Alternatively, get a list of your device IDs using the `mender-cli devices
!!!! list` command.
```bash
DEVICE_ID=<Device ID>
```

The second argument specifies the port mapping - if a single port is specified,
traffic on the local port is routed to the same remote port on the device. You can
also specify different local and remote port, and forward traffic to/from:
a different *REMOTE_HOST* accessible to the device.

! Before using the `mender-cli port-forward` command you need to authenticate with the
! server  running `mender-cli login`.  
! Run `mender-cli --help` to get a complete list of available commands and options.

### Examples

1. Listen on port `8080` locally, forwarding data to/from port `8080` on the device
   ```bash
   mender-cli port-forward $DEVICE_ID 8080
   ```

2. Listen to port `8080` locally, forwarding data to/from port `4443` on the device
   ```bash
   mender-cli port-forward $DEVICE_ID 8080:4443
   ```

3. Listen to port `8080` locally, forwarding data to/from localhost and port
   `4443` on the device
   ```bash
   mender-cli port-forward $DEVICE_ID 8080:localhost:4443
   ```

4. Listen to port `8080` locally, forwarding data to/from port `4443` on the
   remote host with IP `192.168.1.123` in the device's local network
   ```bash
   mender-cli port-forward $DEVICE_ID 8080:192.168.1.123:4443
   ```
   
5. Listen to port `8080` locally, forwarding data as UDP traffic  to port `4443`
   on the remote host `hidden.service.fqdn` in the device's local network.
   ```bash
   mender-cli port-forward $DEVICE_ID udp/8080:hidden.service.fqdn:4443
   ```

## Further reading

* For a detailed list of the configuration options please refer to the
[mender-connect configuration section](../90.Mender-Connect/docs.md#port-forward-configuration).
* You can find the `mender-connect` installation steps for Yocto-based projects,
and for Debian family,
in the [customize with Yocto](../../05.Operating-System-updates-Yocto-Project/05.Customize-Mender/docs.md#mender-connect),
and [customize with Debian](../../04.Operating-System-updates-Debian-family/03.Customize-Mender/docs.md) respectively.
