---
title: Taxonomy
taxonomy:
    category: docs
    label: reference
---

This section presents the basic terms used throughout the documentation.

* _Accepted device_ - An authorized device that can connect to the Mender server
and receive software updates.

* _Artifact_ -  An archive containing everything needed for an update of a
device, including the Artifact Payload itself and metadata such as signatures.
See the documentation on [Artifact](../02.Artifact/docs.md) for more information.

* _Artifact Name_ - A human-readable string uniquely describing an Artifact,
used by UI and API for identification purposes.

* _Artifact Payload_ - Actual data installed on a device, stored inside a
Mender Artifact. It could be a rootfs image, package, container, or other. See
the documentation on [Artifact](../02.Artifact/docs.md) for more information.

* _Authentication Set_ - A combination of an identity and public key for a
device, determining if a given device is allowed to check for- and apply
software updates from the Mender server. A given device identity can have
multiple Authentication sets and each can be in one of the following states,
where only one can be accepted at a given time:
  * rejected
  * accepted
  * pending
  * preauthorized

* _Binary delta_ - The binary difference between two filesystem images. See the
documentation on [Delta updates](../06.Delta-update/docs.md) for more information.

* _Board integration_ - The low-level integration required to enable system
updates with Mender on a board. Often includes OS bootloader and storage
integration and requires customization based on the hardware and OS.

* _Deployment_ - The process of delivering software to devices. It consists of
at least a group of devices and an Artifact name.

* _Device_, _Mender Client Device_ - A single unit that is able to connect to the Mender server, usually
an independent product. Represented on the server by its identity and
authentication data.

* _Device ID_ - A single string uniquely identifying a device in the Mender
server, used in APIs to specify an individual device. See the documentation on
[Identity](../07.Identity/docs.md) for more information.

* _Device type_ - The type of device, used to ensure compatibility between the
hardware and software. See the documentation on [Artifact](../02.Artifact/docs.md)
for more information.

* _Mender Client_ - A user space application installing updates to a device
it is running on. It uses the Mender API to connect to the Mender Server
to authenticate, get the artifacts, report inventory, log the progress
and status of the installations.

* _Mender Hub Integration(s)_ - A contribution on
[Mender Hub](https://hub.mender.io/c/board-integrations?target=_blank)
of a Mender Board integration for a specific board.

* _Mender Server_ - An application implementing Mender API, and the web UI,
providing updates to devices.

* _Organization_ - A single customer environment in the Mender server. Also
known as a Tenant. Note that multi-tenancy is only supported in Mender
Enterprise.

* _Pending device_ - A device that has already sent an authorization request to
the Mender server and is not yet authorized through preauthorization or
user authorization.

* _Preauthorized device_ - A device given by authorization set, that will change
into "accepted" state automatically when it requests authorization.

* _Reference board_ - A board officially supported by Mender, used as a
reference when porting to new boards.

* _Rejected device_ - A device that has already sent an authorization request to
the Mender server, which has been explicitly rejected by the user. A device in
this state is not allowed to communicate with the Mender server and will not
receive any updates.

* _Release_ - A set of one or more Artifacts with the same Artifact name. Used
by the Mender server to assign the right Artifact to a given Device based on
software and hardware compatibility.

* _Signing system_ - A separated and not publicly accessible part of an IT
infrastructure used to cryptographically sign Artifacts or other items,
in the asymmetric encryption model.

* _Update Module_ - An extension to the Mender client for supporting a new type
software update, such as a package manager, container or bootloader.
