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

* _Component_ - Part of a _System_. _Components_ are the logical units that are updated during a _System_ update. The _System device_ (i.e. a device running Mender Orchestrator) and all dependent devices are considered _Components_ of the _System_. Dependent devices may be either physical boards connected to the _System device_ (for example, a control unit connected via CAN) or logical parts of the application stack.
See the documentation on [Orchestrating updates](../../07.Orchestrate-updates/chapter.md) for more information.

* _Compatible type_ - The type of a device, a Component or
[System](../../07.Orchestrate-updates/01.Overview/docs.md#system-type-vs-device-type)
used to ensure compatibility between the hardware and software. See the
documentation on [Artifact](../03.Artifact/docs.md) for more information.

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

* _Device tier_ - A classification that describes the class of an authenticated device.
There are three device tiers:
  * **standard** - An embedded Linux device running the Mender Client (mender-auth and mender-update)
  * **micro** - A microcontroller unit (MCU) running `mender-mcu`, typically with constrained resources
  * **system** - A device running Mender Orchestrator for coordinated multi-component updates
  
  Device tiers affect artifact size limits, polling intervals, deployment restrictions, and
  device count limits in your plan. See the documentation on [Device tiers](../17.Device-tiers/docs.md)
  for more information.

* _Device type_ - The type of device, used to ensure compatibility between the
hardware and software. A more generic term _Compatible type_ (see above) is now
preferred. See the documentation on [Artifact](../03.Artifact/docs.md) for more
information.

* _Identity (Mender Client Device)_ - A set of immutable, human-readable attributes that uniquely identify a _Mender Client Device_. See the
documentation on Device [Identity](../07.Identity/docs.md) for more information.

* _Identity (Component)_ - In the context of a System, an attribute provided by the _Component’s Interface_ that uniquely identifies it. This attribute may change (for example, when a _Component_ is physically replaced), making the change visible.
See the documentation on [Identity query](../../07.Orchestrate-updates/04.Interface-protocol/docs.md#identity-query) for more information.
  * For _System devices_, the _Identity_ is always _Identity (Mender Client Device)_, even when the device is represented as a _Component_ in a _System_.

* _Interface_ - Used in the context of a System. An Interface used for updating _Components_. See the
documentation on [Interface Protocol](../../07.Orchestrate-updates/04.Interface-protocol/docs.md) for more information.

* _Inventory_ - A set of attributes of a _Mender Client Device_ or a _Component_. See the
documentation on [Inventory](../../02.Overview/08.Inventory/docs.md) for more information.

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

* _System device_ - Main _Component_ of a _System_. A _Mender Client Device_ that is running Mender Orchestrator. See the
documentation on [Orchestrating updates](../../07.Orchestrate-updates/chapter.md) for more information.

* _Tenant_ - See _Organization_.

* _Update Module_ - An extension to the Mender Client for supporting a new type
software update, such as a package manager, container or bootloader.

* _Topology_ - A YAML file defining the Components of a System. Provisioned alongside new Systems, it specifies
what Components are present and how they can be updated.
See the documentation on [Topology](../../07.Orchestrate-updates/03.Topology/docs.md) for more information.

* _Manifest_ - A YAML file defining Software versions for a given System. Maps Artifacts to Component types
and controls update strategy.
See the documentation on [Manifest](../../07.Orchestrate-updates/02.Manifest/docs.md) for more information.

* _System_ - Consists of one Device running Mender Orchestrator and one or more Components. A System exists
when a Device has a System type and corresponding Topology.
