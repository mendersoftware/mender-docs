---
title: Mender Gateway
taxonomy:
    category: docs
---

!!!!! Mender Gateway is only available in the Mender Enterprise plan.
!!!!! See [the Mender features page](https://mender.io/product/features?target=_blank)
!!!!! for an overview of all Mender plans and features.

In segregated networks, most devices may operate without direct access to the
Internet. In such networks, typically only a gateway has Internet access and
offers a limited set of services to devices in the local network. _Mender
Gateway_ is such an application service that runs on the gateway and enables
managing and deploying OTA updates to devices on the local network. The gateway
acts as a proxy with the ability to understand and serve client requests
locally.

Mender Gateway operates by proxying requests from a local HTTP(S) server on the
local network to the upstream Mender Server. It is capable of proxying Artifacts
from an s3-compatible file server to the devices and enabling mutual TLS
authentication requests on behalf of devices.

![Mender gateway](mender-gateway-schema.png)

## Artifact Proxy and Cache
The Mender Gateway can understand when a device has an available update
and serves Artifacts on the server's behalf. Without this feature, the device
would try downloading the Artifacts referenced by the download link contained
in the deployment instructions directly from the internet. The Mender Gateway
will instead replace the download link in the deployment instructions with a
local URL served by itself.

It can also cache the Artifacts locally and serve them locally when needed.
In this way, when multiple devices request the same Artifact, it will be
downloaded only once and then served from the cache for the subsequent
download requests saving bandwidth. The Mender Gateway will automatically
manage the cache eviction when the Artifacts cache is enabled if there is
no more free space on the path specified in the configuration file. 

See the [Mender Gateway User Guide](../../01.Get-started/06.Mender-Gateway/docs.md)
for a reference setup of Mender Gateway as an Artifact Proxy.

## Systems
A System is a group of devices belonging to the same product or logical entity
connected to a Mender Gateway instance. Devices in a System usually require
coordination during the update process. To define a System, each device must
report to the Mender Server a special inventory attribute named
`mender_gateway_system_id`, containing a unique identifier for the given
system. See the Mender Gateway [getting started](../../01.Get-started/06.Mender-Gateway/docs.md)
for an example configuration.

## Mutual TLS Authentication
The Mender Gateway is capable of automatic provisioning of devices using *mTLS*
authentication. Any device with a valid certificate signed by the Certificate
Authority (CA) configured on the gateway, is automatically accepted by the
Mender Server. See the [mTLS user guide](10.Mutual-TLS-authentication/docs.md) for a
reference mutual TLS setup in a testing environment.
