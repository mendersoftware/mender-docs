---
title: Deployments
taxonomy:
    category: docs
---

A Deployment ensures delivery of a Release to one or more devices. A Release can contain one or more Mender Artifacts, one of the Artifacts is assigned when the device receives the update based on software and hardware compatibility.

Deployments in Mender represent the explicit association of a release (Mender Artifact) and one or more devices running a client that implements the [Device APIs](../../200.APIs/01.Open-source/01.Device-APIs/01.Device-authentication/docs.md), e.g., the Mender client.

At its basics, the definition of a Deployment includes:

* *ID*, randomly generated, unique identifier of the Deployment, assigned by Mender at creation time
* *Artifact* to be used to update the targeted devices
* *Devices* targeted by the update
* *Phases* (_professional/enterprise only_) describing a phased and/or scheduled roll-out
* *Number of retries* (_professional/enterprise only_) for each device in case of a failure during the update process

Only accepted devices can be part of a deployment, and any given device finishes the Deployment once. Ordering of deployments is also maintained, so the oldest Deployment is the one the device gets first.

## Static groups

A *static group* contains a list of Device IDs. Devices can explicitly be added or removed from a group manually in the UI, or through automation by using the APIs.

Before a device can be added or removed to a static group, it needs to exist in the Mender server.

## Deployment to static groups

It is possible to create a Deployment targeting one or more specific devices, both using the UI and the APIs, selecting an explicit list of Device IDs.

The Mender UI also supports the creation of a Deployment targeting a static device group, to update all the devices belonging to it.

A Deployment to a static group contains a list of devices and finishes once all the devices in the Deployment have finished.

Please note that Mender uses the group to retrieve the list of the Device IDs at creation time, and devices assigned to the group after the creation of the Deployment will not be included in it.

## Dynamic groups

A *dynamic group* does not contain a list of predefined Device IDs. It instead contains the definition of a dynamic filter that can match one or more devices, and the matched devices could change in the future as new devices are accepted into Mender, or device attributes change and fulfill the filter criteria.

## Deployment to dynamic groups

Mender Enterprise also supports the creation of Deployments using a dynamic filter to assign a deployment to an open, variable group of devices fulfilling the filter criteria as long as the Deployment is not closed.

Deployments to dynamic groups behave very differently than deployments to a static group in that it will never implicitly finish, but stay active until the user stops it because we do not necessarily know up-front how many devices are part of this Deployment. It is, however, possible to set a maximum number of devices so that the Deployment finishes after this number of devices have been updated. A device can only be in one static group at the same time, while it can be in multiple dynamic groups.

## Deployment lifecycle

Once a Deployment has been created, it stays in "*pending*" state until one or more Devices matching the definition of the Deployment, either by the inclusion of their ID (static) or matching of the filter's criteria (dynamic) ask for an update.

When at least one device running the Mender client is performing the defined update, the Deployment transitions to the status "*inprogress*".

When all the devices included in the Deployment to a static group finished the update, either successfully or not, the Deployment's status changes to "*finished*".

Deployments to dynamic groups behave in a different way as they do not include the explicit list of devices targeted by the update. For this reason, a Deployment to dynamic groups remains in *pending* status until one of the following conditions is true:

* The user explicitly, either programmatically via API or using the Mender UI, marks the Deployment as completed.
* The number of devices updated matches the optional Deployment's parameter *maximum number of devices*.

At this point, the Deployment's status transitions to *finished*, and any other device will not use it.

### Device Deployment

Each device, while processing a deployment and after finishing it, stores the details of the update process defined by a Deployment in a database entity called Device Deployment.

The definition of a Device Deployment includes:

* The details of the Device, Deployment, and Artifact
* Status, and optionally sub-status of the upgrade process
* Creation and completion timestamps
* Optionally, the logs generated during the update process

The list of the possible values for the status field of an update in progress are:

* "downloading"
* "installing"
* "rebooting"
* "pending"

The following values for the status field for a finished update are:

* "success"
* "failure"
* "noartifact"
* "already-installed"
* "aborted"
* "decommissioned"

### Algorithm for selecting the Deployment for the Device

It is possible that the device has been targeted for one deployment or more.
When the device is asking for the deployment, the deployments service looks for the oldest, not finished deployment the device was targeted for.
If there is one, the deployments service creates the instance of the deployment for the device (device deployment) with a "pending" state and executes the following operations:
* checks if the deployment is phased and in case it is, checks if there is an active phase; if yes, the deployments service proceed, if not, the deployment service returns no instructions to the device;
* tries to assign artifact to the device; if there is an artifact returns the deployment instructions to the device; if not - returns no instructions and sets the device deployment status to "no artifact"; in case the artifact installed on the device is the same as the one in the deployment, deployments service returns no instructions and sets the device deployment status to "already installed".
