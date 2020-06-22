---
title: Taxonomy
taxonomy:
    category: docs
    label: reference
---

This section presents the basic terms used throughout the documentation.

* _Pending device_ - A device that has already sent an authorization request to the Mender server without admission through preauthorization or user authorization.

* _Rejected device_ - A device that has already sent an authorization request to the Mender server, which has been explicitly rejected by the user.

* _Decommission a device_ - User action on a non-pending device that removes the device
completely from the Mender server.

* _Accept a device_ - User action on pending or rejected device to enable it to
connect to Mender server.

* _Accepted device_ - An authorized device that can be deployed to by the Mender server

* _Reject device_ - User action on pending or accepted device, forbidding
the device to make API requests to server.

* _Artifact_ -  An archive containing everything needed for an update of a device.
Contains metadata and various payloads.

* _Artifact Payload_ - Consists of a type and actual data to be installed on a 
device. It is stored inside a Mender Artifact. It could be a rootfs image, package,
container, or other.

* _Authorization status_ - An attribute assigned to a device by the Mender server.
It reflects the current state of authentication of a device authorization set.

* _Authorization set_ - A key assigned to a device. It can be in one of
the following states:
  * "rejected"
  * "accepted"
  * "pending"
  * "preauthorized"
  
* _Pre authorized device_ - A device given by authorization set, that will 
shift into "accepted" state automatically when it requests authorization.

* _Binary delta_ - Binary patch for a filesystem image.

* _Board integration_ - The low-level integration required to get Mender working on
a board.

* _Deployment_ - An entity consisting at least of a name, a group of devices, and
artifact name. Used to get the software to devices.

* _Device_ - An element of IT system containing identity and authentication
data, running the Mender client, communicating with the Mender server via
Mender API, receiving updates.

* _Device ID_ - A string of letters, numbers, and dashes, uniquely identifying a
device in Mender.

* _Device type_ - The type of device, e.g.: "raspberrypi4"

* _Image name_ - A string describing an image, used by UI and API for identification
purposes.

* _Mender Hub Integration(s)_ - Any contribution on Mender Hub regarding new
board support for Mender

* _Organization_ - A single customer environment, either when Multi-tenancy is
supported or on Mender Enterprise

* _Reference board_ - A board officially supported by Mender, used as a reference
when porting to new boards.

* _Update Module_ - An extension to the Mender client for supporting a new type
of software update, such as a package manager, container or bootloader.

* _Mender server_ - An application implementing Mender API, and the web UI, providing
updates to devices.
