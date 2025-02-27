---
title: Taxonomy
taxonomy:
    category: docs
    label: reference
---

This section presents the basic terms used throughout the documentation.

* _Accepted device_ - An authorized device that can connect to the Mender Server
and receive software updates.

* _Add-on_ (also _Mender Add-on_)- An optional extension to Mender for supporting
use cases beyond core OTA updates features, e.g. Remote terminal.
Install Mender first, before installing any add-ons

* _Application update_ - An update which is not an Operating System update.

* _Artifact_ -  An archive containing everything needed for an update of a
device, including the Artifact Payload itself and metadata such as signatures.
See the documentation on [Artifact](../03.Artifact/docs.md) for more information.

* _Artifact Name_ - A human-readable string uniquely describing an Artifact,
used by the UI and Server-side API for identification purposes.

* _Artifact Payload_ - Actual data installed on a device, stored inside a
Mender Artifact. It could be a rootfs image, package, container, or other. See
the documentation on [Artifact](../03.Artifact/docs.md) for more information.

* _Authentication Set_ - A combination of an identity and public key for a
device, determining if a given device can check for- and apply software updates
from the Mender Server. A given device identity can have multiple Authentication
sets and each can be in one of the following states:
  * rejected
  * accepted
  * pending
  * preauthorized
You can accept only one Authentication set at a time.

* _Binary delta_ - The binary difference between two Operating System images. See the
documentation on [Delta updates](../06.Delta-update/docs.md) for more information.

* _Board integration_ - The low-level integration required to enable Operating System
updates with Mender on a board. Often includes OS bootloader and storage
integration and requires customization based on the hardware and OS.

* _Container update_ - An Application update for containerized software running on the devices.

* _Deployment_ - The process of delivering software to devices. It consists of
at least a group of devices and an Artifact name.

* _Device_, _Mender Client Device_ - A single unit that is able to connect to the Mender Server, usually
an independent product. Represented on the server by its identity and
authentication data.

* _Device-side API_ - The collection of APIs exposed by the Mender components
running on the device. The Device-side API constitutes the only public programmatic
interface of the Mender Client. It is a thin layer that receives messages over D-Bus,
processes them, transmits them to the Mender Client, receives the results
from the client, and transmits a response on the D-Bus.

* _Device ID_ - A single string uniquely identifying a device in the Mender
server, used in Server-side APIs to specify an individual device. See the
documentation on device [Identity](../07.Identity/docs.md) for more information.

* _Device type_ - The type of device, used to ensure compatibility between the
hardware and software. See the documentation on [Artifact](../03.Artifact/docs.md)
for more information.

* _Mender Client_ - A collective term for the Mender Update service, which consists
of two service components, `mender-auth` and `mender-update`.

* _Mender Connect_ - A user space application providing the add-ons
framework, as well as implementation of particular add-ons which you can enable
or disable as per configuration. It integrates with the Mender Client over
a well-defined and portable Device-side API.

* _Mender Hub Integration(s)_ - A contribution on
[Mender Hub](https://hub.mender.io/c/board-integrations?target=_blank)
of a Mender Board integration for a specific board.

* _Mender Gateway_ - An application that enables managing and deploying OTA
updates to devices on the local network. The gateway acts as a proxy with the
ability to understand and serve client requests locally.

* _Mender Server_ - An application implementing the Server-side Mender API, and the
web UI, providing updates to devices.

* `mender-auth`, `mender-auth` Client - A user space application running on a
device which provides authentication to the Mender Server for other
applications. This application is required by other applications that
communicate with the Mender Server.

* `mender-update`, `mender-update` Client - A user space application installing
updates to a device it is running on. It uses the the `mender-auth` client
service and Mender Server-side API to connect to the Mender Server, get the
artifacts, report inventory, log the progress and status of the installations.

* _Operating System update_ - An update which replaces the operating system's filesystem
thanks to the A/B partitioning schema. The Mender Client writes a new filesystem image
to the inactive partition and updates the bootloader configuration to flip the active and
inactive partition.

* _Organization_ - A single customer environment in the Mender Server. Also
known as a Tenant. Note that multi-tenancy is only supported in Mender
Enterprise.

* _Pending device_ - A device that has already sent an authorization request to
the Mender Server and is not yet authorized through preauthorization or
user authorization.

* _Preauthorized device_ - A device given by authorization set, that will change
into "accepted" state automatically when it requests authorization.

* _Reference board_ - A board officially supported by Mender, used as a
reference when porting to new boards.

* _Rejected device_ - A device that has already sent an authorization request to
the Mender Server, which has been explicitly rejected by the user. A device in
this state is not allowed to communicate with the Mender Server and will not
receive any updates.

* _Release_ - A set of one or more Artifacts with the same Artifact name. Used
by the Mender Server to assign the right Artifact to a given Device based on
software and hardware compatibility.

* _Rootfs-image update module_ - One of the standard extensions to
`mender-update` (part of the Mender Client) which offers full root filesystem
updates using a dual partition setup.

* _Server-side API_ - The collection of HTTP-based APIs exposed by the Mender
Server. They include management end-points, consumed by users and the UI,
device end-points, consumed by the Mender components running on the devices,
and internal end-points.

* _Service Provider tenant_ - A special _tenant_ which can create and manage
child tenants, e.g., different divisions or teams in the same organization
or customers managed by a service provider business partner. Service Provider
tenants are an Enterprise feature.

* _Signing system_ - A separated and not publicly accessible part of an IT
infrastructure used to cryptographically sign Artifacts or other items,
in the asymmetric encryption model.

* _System_ -  A System is a group of devices belonging to the same product or
logical entity connected to a [Mender Gateway](../../01.Get-started/06.Mender-Gateway/docs.md)
instance. Devices in a System usually require coordination during the update process.

* _Tenant_ - See _Organization_.

* _Update Module_ - An extension to the Mender Client for supporting a new type
software update, such as a package manager, container or bootloader.
