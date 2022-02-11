---
title: Mender Gateway
taxonomy:
    category: docs
---

!!!!! Mender Gateway is only available in the Mender Enterprise plan.
!!!!! See [the Mender features page](https://mender.io/plans/features?target=_blank)
!!!!! for an overview of all Mender plans and features.

For devices running in secure environments, the devices may operate without
direct access to the Internet. In such environments, it is common to include a
single _security hardened machine_ with access to the Internet to the network
topology offering limited set of services for devices in the local network.
_Mender Gateway_ is such an application service that runs on the gateway host,
that enables managing and sending OTA updates to devices on the local network.
The gateway acts as a proxy with the ability to understand and serve client
requests locally.

Mender Gateway operates by proxying requests from a local HTTP(S) server on the
local network to the upstream Mender server. It is capable of proxying artifacts
from an s3-compatible file server to the devices and enabling mutual TLS
authentication requests on behalf of devices.

![Mender gateway](mender-gateway-schema.png)

## Artifact Proxy
The Mender Gateway is able to understand when a device has an available update
and is able to serve artifacts on behalf of the server. Configuring Mender
Gateway to serve as an artifact proxy will make the gateway serve any artifacts
assigned by a deployment. See the [Artifact Proxy User Guide]()<!--FIXME/MEN-5302-->
for a reference setup of Mender Gateway as an Artifact Proxy.

## Mutual TLS Authentication
The Mender Gateway is capable of automatic provisioning of devices using *mTLS*
authentication. Any device with a valid certificate signed by the Certificate
Authority (CA) configured on the gateway, is automatically accepted by the
Mender server. See the [mTLS user guide]()<!--FIXME/MEN-5302--> for a reference mutual
TLS setup in a testing enviroment.
