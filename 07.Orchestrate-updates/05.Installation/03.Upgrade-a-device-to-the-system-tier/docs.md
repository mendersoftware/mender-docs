---
title: Upgrade a device to the system tier
taxonomy:
    category: docs
---

This guide describes how to convert an existing, already-managed [standard tier](../../../02.Overview/17.Device-tiers/docs.md#standard-tier)
device into a [system tier](../../../02.Overview/17.Device-tiers/docs.md#system-tier) device running [Mender Orchestrator](../../01.Overview/docs.md),
entirely over-the-air. It assumes the device is already connected to Mender and receiving regular rootfs updates.

If you are provisioning a new device from scratch, follow the [Installation](../docs.md) section instead.

## Making the upgrade robust

The upgrade is performed as three separate deployments:

1. Deliver the [Topology](../../03.Topology/docs.md) to the data partition, using the `directory` Update Module.
2. Install Mender Orchestrator and the [Interfaces](../../04.Interface-protocol/docs.md) with a rootfs update, **without** changing the device tier.
3. Change the device tier to `system` with a second rootfs update, then accept the new authentication set.

It is tempting to do this in fewer deployments, in particular to combine Steps 2 and 3 into a single
rootfs update that installs the Orchestrator, installs the Interfaces, and sets `DeviceTier` to `system`
all at once. This can leave the device unrecoverable over-the-air:

1. On boot, the device authenticates as a system tier device, creating a new authentication set in the
   **pending** state that no one has accepted yet.
2. The Mender Client cannot complete its check-in while the new authentication set is pending. When its
   update window elapses, the client concludes the update failed and **rolls back** to the previous rootfs,
   which is the original standard tier image, without the Orchestrator or the Interfaces.
3. You then accept the pending system authentication set. The device is now a system tier device, but it is
   running the rolled-back image.
4. A system tier device is updated through a [Manifest](../../02.Manifest/docs.md) (payload type
   `mender-orchestrator-manifest`); a plain rootfs deployment to the System device no longer applies. But
   the rolled-back image has no Interfaces installed, so any Manifest deployment fails. The device is stuck:
   it will not accept a plain rootfs update, and it cannot complete a Manifest update.

Splitting the tier change into its own deployment avoids this. The Orchestrator and Interfaces are
committed in Step 2 while the device is still a standard tier device, so they survive independently of the
tier flip. Even if the Step 3 rootfs rolls back, the device retains the Orchestrator and Interfaces and
stays recoverable, as described in [If the device rolls back before you accept it](#if-the-device-rolls-back-before-you-accept-it).

## Prerequisites

- A device already managed by Mender as a standard tier device.
<!--AUTOVERSION: "Mender Client % or newer"/ignore-->
- Mender Client 6.0.0 or newer.
- The Mender Orchestrator packages for your platform. See [Installation](../docs.md).
- A `topology.yaml` prepared for your System. See [Topology](../../03.Topology/docs.md).
- The [mender-artifact](../../../12.Downloads/01.Workstation-tools/docs.md#mender-artifact) tool on your host.

The examples below use a Raspberry Pi 5 as the System device, with the device type `raspberrypi5`.
Substitute your own device type where relevant.

## Step 1: Deliver the Topology to the data partition

Mender Orchestrator reads the Topology from `/data/mender-orchestrator/topology.yaml` by default, on the
persistent data partition. A rootfs update swaps the inactive A/B rootfs partition and never touches
`/data`, so it cannot place the Topology there. Deliver the file with the `directory` [Update Module](../../../03.Client-installation/05.Use-an-updatemodule/docs.md)
instead, which writes files onto a chosen directory on the device.

The `directory` Update Module is one of the Update Modules installed by default with the Mender Client,
so no extra installation is required on a standard tier device. You can find its documentation and source
in the [Update Modules category on Mender Hub](https://hub.mender.io/c/update-modules?target=_blank).

Stage the files you want on the data partition, then build the Artifact with the `directory-artifact-gen` helper:

```bash
DEVICE_TYPE=raspberrypi5

# Stage the files to deliver to the data partition
mkdir -p topology-payload
cp topology.yaml topology-payload/
```

<!--AUTOVERSION: "mendersoftware/mender/%/support"/mender-->
```bash
# Download the directory Update Module Artifact generator
curl -O https://raw.githubusercontent.com/mendersoftware/mender/5.1.0/support/modules-artifact-gen/directory-artifact-gen
chmod +x directory-artifact-gen
```

```bash
# Create an Artifact that installs the Topology to /data/mender-orchestrator
./directory-artifact-gen \
  --artifact-name topology-v1 \
  --device-type $DEVICE_TYPE \
  --dest-dir /data/mender-orchestrator \
  --output-path topology-v1.mender \
  topology-payload
```

The contents of `topology-payload` are installed into `--dest-dir`, so `topology.yaml` ends up at
`/data/mender-orchestrator/topology.yaml`. Upload `topology-v1.mender` to Mender and deploy it to the
device as a normal Release. The device is still a standard tier device at this point, so the deployment
completes like any other update.

## Step 2: Install Mender Orchestrator and the Interfaces

Build a new rootfs image that includes the Mender Orchestrator components, but **leave the device tier
unchanged** (`standard`). The image must contain:

- `mender-orchestrator-core`, which provides the `mender-orchestrator` binary.
- `mender-orchestrator-support`, which provides the Interfaces (installed under
  `/usr/share/mender-orchestrator/interfaces/v1`, including the out-of-the-box `rootfs-image` Interface),
  the `mender-orchestrator-manifest` Update Module, and the inventory scripts.

See the [Installation](../docs.md) section for how to obtain and integrate these components for your platform.

Do **not** set `DeviceTier` to `system` in `mender.conf` yet. Because the device is still a standard tier
device, it keeps polling and accepts this rootfs update normally, and the update commits safely. When this
deployment finishes, the device has all the Orchestrator machinery in place but still authenticates as a
standard tier device.

## Step 3: Change the device tier to system

Build a second rootfs image, identical to the one from Step 2, but with the device tier set to `system` in
`mender.conf`:

```json
{
  "DeviceTier": "system"
}
```

See [Setting the device tier](../../../02.Overview/17.Device-tiers/docs.md#setting-the-device-tier) for the
configuration details for your integration.

Deploy this rootfs to the device. On the next boot, the Mender Client reads the `system_type` from the
Topology and authenticates as a system tier device, which creates a new authentication set in the
**pending** state.

!!! Accept the new authentication set promptly, before the client's update window elapses. If you do not, the client concludes it cannot communicate with the server and rolls the update back. See [If the device rolls back before you accept it](#if-the-device-rolls-back-before-you-accept-it).

Accept the pending authentication set through the UI or API, as described in
[Changing the device tier](../../../02.Overview/17.Device-tiers/docs.md#changing-the-device-tier). Because the
Orchestrator and Interfaces were already committed in Step 2, the device can now receive
[Manifest](../../02.Manifest/docs.md) deployments and operate as a full system tier device.

### If the device rolls back before you accept it

If the new system authentication set is not accepted before the client's update window elapses, the client
rolls the Step 3 update back and the device runs the image from Step 2 again. When you accept the system
authentication set afterwards, the device is a system tier device.

Unlike the deadlock described in [Making the upgrade robust](#making-the-upgrade-robust), this situation is
recoverable, precisely because Step 2 installed the Orchestrator and Interfaces and those survived the
rollback. A system tier device is updated through a Manifest, not a plain rootfs deployment, so recover the
device by deploying a Manifest.

There is one subtlety when building the recovery Manifest Artifact. The server has accepted the device as a
system tier device, but the device is running the Step 2 image, whose `mender.conf` still has
`DeviceTier` set to `standard`. The device therefore still considers itself a standard tier device. When it
polls for deployments, it sends its own device type rather than the [System type](../../01.Overview/docs.md#system-type-vs-device-type)
from the Topology. As a result, the Manifest Artifact must be compatible with the device type
(`raspberrypi5` in this example), not with the Topology's `system_type` (`system-core` in this example),
or the device will not receive the deployment.

1. Build a [Manifest](../../02.Manifest/docs.md) that brings the System device and all other Components to
   the target state.
2. Generate the Manifest Artifact so that it is compatible with the device type. See [Create a Manifest Artifact](../../02.Manifest/01.Manifest-Artifact/docs.md):

    ```bash
    mender-orchestrator-manifest-gen \
        --artifact-name recovery-manifest \
        --output-path recovery-manifest.mender \
        --system-type raspberrypi5 \
        manifest.yaml
    ```

    !!! Note the `--system-type raspberrypi5` value: it sets the type the Artifact is compatible with. Here it must be the device type the device sends while it still considers itself a standard tier device, not the Topology's `system_type`.

3. Deploy the recovery Manifest to the device.

Because the Interfaces are present, the Manifest deployment succeeds and the device reaches the intended
system tier state. Do not try to recover with a plain rootfs deployment to the System device; it no longer
applies once the device is a system tier device.

## Verify the upgrade

Confirm that Mender Orchestrator is running and reporting the expected state on the device:

```bash
mender-orchestrator show-provides
```

Then deploy a Manifest to the device to confirm the full system update path works end-to-end. See the
[Examples](../../06.Examples/docs.md) section for a complete walkthrough.
