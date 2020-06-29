---
title: Identity
taxonomy:
    category: docs
    label: reference
---

## The identity of a device

We designed Mender to manage an arbitrary number of devices. Internally, the server assigns
a unique, unchangeable identifier to each one of them. The Device ID does not
have a directly visible relation to any device attributes.
To address this problem we created a constant set of key-value pairs that uniquely identify a device. 

The MAC address of a network interface controller, a serial number, the eMMC CID,
are all pieces of data that:
* do not change over the lifetime of a device
* are human-readable
* form a 1:1 relationship with the device
* you can store as key-value pairs

Unless the system designer has modified the default Mender configuration,
the Mender client will use the MAC address as the identity attribute.
Once you have accepted the device, you can see it in the UI:

![identity](identity.png)

The Mender client allows you to define the identity attributes, which means that Mender
can adapt to the identity scheme of any environment. However, Mender imposes the following
requirements for device identities:

* The combination of the attribute values must be *unique* to each device, so that identities are not ambiguous when deploying software.
* Identity attributes must *never change* for the lifetime of a device, so that the Mender server can recognize them reliably.

It is important to have the ability to regenerate keys if a device gets compromised,
or as a recurring proactive security measure.
Therefore, we do not recommend using device keys as part of an identity, as it
makes the rotation or regeneration of keys over the lifetime of the device
(as it in effect changes the identity) difficult.

When a device requests [authentication](../../200.APIs/01.Open-source/01.Device-APIs/01.Device-authentication/),
it includes the identity attributes. The Mender server computes the persistent
identity of the device based on these attributes.

Please refer to the [client configuration section](../../05.Client-configuration/03.Identity)
to find detailed tutorial on managing the identities.
