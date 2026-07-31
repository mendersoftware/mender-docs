---
title: Update a Raspberry Pi with a Raspberry Pi over MQTT
taxonomy:
    category: docs
---

This section walks through updating a **second Raspberry Pi** from a first one
running Mender Orchestrator, using **MQTT** to push updates to the second board
instead of having it poll a Mender Server. A **Raspberry Pi** runs Mender
Orchestrator as the System Device, and a **second Raspberry Pi**, connected only
running Mender, is a Component that the first Pi updates by pushing
commands and Artifact data over MQTT and reading back the results. This approach
leverages the built-in Mender functionality like rollbacks on the second Raspberry Pi.

## How this differs from the ESP32-S3 example

In [Update an ESP32-S3 with a Raspberry Pi](../02.Update-an-ESP32-S3-with-a-Raspberry-Pi/docs.md)
the Component (the ESP32-S3) does not run Mender at all, is physically wired to
the System Device over USB, and the System Device *pulls* by calling
`esptool.py` whenever an Interface state runs.

Here the roles are different:

* The **Component, the second Raspberry Pi, runs Mender**  in standalone mode.
* The Component is **outbound-only**: it dials out to a broker on the System
  Device and never accepts an inbound connection. Instead of the System Device
  reaching in and pulling status, the Component's agent *pushes* results back
  the moment they're ready.
* Commands and results are pushed over MQTT, but the Artifact's *bytes* are
  not: `mqtt-component` starts a short-lived HTTP server (alive only for the
  `Download` state) and tells the Component agent to fetch from it. This
  avoids needing to buffer a possibly
  multi-GB Artifact in memory -- the Interface streams it from the
  Orchestrator's own download straight into the HTTP response as it arrives.

The System we build looks like this:

| Component | `component_type` | Interface | Role |
|-----------|-------------------|-----------|------|
| Raspberry Pi #1 | its own `device_type`, e.g. `raspberrypi5` | `rootfs-image` | System Device, runs Orchestrator |
| Raspberry Pi #2 | its own `device_type`, e.g. `raspberrypi4` | `mqtt-component` | Component, runs Mender standalone |

`component_type` for Raspberry Pi #2 must be exactly its own `device_type` --
[Interface protocol](../../04.Interface-protocol/docs.md) and
[Compatibility checks](../../07.Artifacts%20handling/03.Compatibility%20checks/docs.md)
require this whenever a Component runs Mender itself.

## Prerequisites

* **Two Raspberry Pi boards**, on the same local network, each with the Mender
  Client (`mender-update`) installed by following
  [Prepare a Raspberry Pi device](../../../01.Get-started/01.Preparation/01.Prepare-a-Raspberry-Pi-device/docs.md)
  (any model it supports). Keep an SSH session open to each, and note the
  login user and IP address of both.
* A **hosted Mender account** -- only Raspberry Pi #1 (the System Device) is
  provisioned to it. Raspberry Pi #2 never talks to Mender Server, but still
  needs the Mender Client installed locally to run `mender-update` in
  standalone mode (Step 2).
* The [mender-artifact](../../../12.Downloads/01.Workstation-tools/docs.md#mender-artifact)
  tool on your workstation.

## Step 1 - Install Mender Orchestrator on Raspberry Pi #1

On Raspberry Pi #1 (over SSH), download and install the
`mender-orchestrator-core` and `mender-orchestrator-support` Debian packages by
following the
[Debian family installation instructions](../../05.Installation/02.Debian-family/docs.md).

Tell the Mender Client that this device runs in the system tier. Edit
`/etc/mender/mender.conf` and set the `DeviceTier` option to `system`:

```json
{
  "DeviceTier": "system"
}
```

Restart the Mender Client so the change takes effect.

```bash
sudo systemctl restart mender-authd mender-updated
```

Confirm the device's built-in device type -- we use this as the
`component_type` of the System Device in the Topology:

```bash
cat /var/lib/mender/device_type
```

Accept the device in Mender Server.

## Step 2 - Prepare Raspberry Pi #2 as a standalone Component

Raspberry Pi #2 runs `mender-update`, but is **never connected to a Mender
Server** -- Raspberry Pi #1 delivers Artifacts to it directly, so it only ever
needs `mender-update` running in
[standalone mode](../../../08.Artifact-creation/08.Standalone-deployment/docs.md).
If it was flashed with a Mender-ready image following
[Prepare a Raspberry Pi device](../../../01.Get-started/01.Preparation/01.Prepare-a-Raspberry-Pi-device/docs.md),
`mender-update` is already installed; you only need to stop it running as a
daemon:

```bash
sudo systemctl stop mender-updated
sudo systemctl disable mender-updated
sudo systemctl mask mender-updated
```

Note its device type -- we use this both as its `component_type` in the
Topology and to name its Artifacts later:

```bash
cat /var/lib/mender/device_type
```

Do **not** accept or provision this device in Mender Server -- it should never
appear in the **Devices** list.

## Step 3 - Install the broker and the Component agent

The `mqtt-component` Interface and its `mosquitto` broker configuration usedo n Raspberry Pi #1,
as well as the `mender-mqtt-agent` Component agent used on Raspberry Pi #2 all ship in the
`mender-orchestrator-demo` package.

Install it on **Raspberry Pi #1** by following the
[Debian family installation instructions](../../05.Installation/02.Debian-family/docs.md#demo-package-optional).
It installs the `mqtt-component` Interface into
`/usr/share/mender-orchestrator/interfaces/v1/`, alongside the `esp32` example
Interface, plus the broker configuration and `mender-mqtt-agent`.

!!! The demo package is intended for evaluation and is not appropriate for
!!! production devices. We use it here as a convenient way to obtain
!!! `mqtt-component`, its broker configuration, and `mender-mqtt-agent`.

This example runs the broker in plaintext, with no authentication, which is
appropriate for a demo on a trusted local network -- it avoids certificate
management this example doesn't need.

!! Anyone who can reach Raspberry Pi #1 on port 1883 can publish or subscribe
!! to any Component's MQTT topics, including issuing update commands. Do not
!! expose this port beyond a trusted LAN.

Install `python3-paho-mqtt` and the broker, then start it:

```bash
sudo apt-get update
sudo apt-get install -y python3-paho-mqtt mosquitto mosquitto-clients
sudo systemctl restart mosquitto
sudo systemctl status mosquitto --no-pager
```

`mqtt-component` runs the `Download` state's short-lived HTTP server on
whatever address you give it via `MENDER_MQTT_INTERFACE_ARTIFACT_HOST` --
Raspberry Pi #2 needs this address to fetch the Artifact. Since
`mender-orchestrator` runs as a child process of the Mender Client daemon
(`mender-updated`), set its value on Raspberry Pi #1 so the Interface inherits it:

```bash
sudo systemctl edit mender-updated
```

Add these lines in the editor that opens, then save and exit:

```ini
[Service]
Environment="MENDER_MQTT_INTERFACE_ARTIFACT_HOST=<raspberry-pi-1-ip-or-hostname>"
```

```bash
sudo systemctl restart mender-updated
```

On **Raspberry Pi #2**, install `python3-paho-mqtt` and the same
`mender-orchestrator-demo` package (following the same
[Debian family installation instructions](../../05.Installation/02.Debian-family/docs.md#demo-package-optional)
as above) -- it's what provides `mender-mqtt-agent`, even though this board
never runs Mender Orchestrator itself and doesn't need
`mender-orchestrator-core`/`mender-orchestrator-support`:

```bash
sudo apt-get update
sudo apt-get install -y python3-paho-mqtt
sudo cp /etc/mender-mqtt-agent/mender-mqtt-agent.conf.example /etc/mender-mqtt-agent/mender-mqtt-agent.conf
```

Edit `/etc/mender-mqtt-agent/mender-mqtt-agent.conf` and set:

```bash
MENDER_MQTT_COMPONENT_ID=rpi2-component
MENDER_MQTT_BROKER_HOST=<raspberry-pi-1-ip-or-hostname>
```

Then enable and start the agent:

```bash
sudo systemctl enable --now mender-mqtt-agent
sudo systemctl status mender-mqtt-agent --no-pager
```

Check that Raspberry Pi #2 connected, on **Raspberry Pi #1**:

```bash
mosquitto_sub -h 127.0.0.1 -p 1883 -t 'mender-orchestrator/rpi2-component/status' -C 1
```

This should print `online`.

## Step 4 - Edit the Topology

The [Topology](../../03.Topology/docs.md) describes the Components of the
System. On **Raspberry Pi #1**, create it at
`/data/mender-orchestrator/topology.yaml`, using the two device types you
noted in Steps 1 and 2:

```bash
sudo mkdir -p /data/mender-orchestrator
sudo tee /data/mender-orchestrator/topology.yaml > /dev/null << 'EOF'
api_version: "mender/v1"
kind: "topology"
system_type: "rpi-rpi-mqtt-system"

components:
  - component_type: raspberrypi5
    interface: rootfs-image

  - component_type: raspberrypi4
    interface: mqtt-component
    interface_args: ["rpi2-component"]
EOF
```

Replace `raspberrypi5` with Raspberry Pi #1's own `device_type`, and
`raspberrypi4` with Raspberry Pi #2's. `interface_args: ["rpi2-component"]`
must match `MENDER_MQTT_COMPONENT_ID` set on Raspberry Pi #2 in Step 3 -- this
is how `mqtt-component` finds the right MQTT topics for this Component.

## Step 5 - Create the Component Artifacts

Run these commands on your **workstation**:

```bash
RPI1_USER=<rpi1-user>
RPI1_IP=<rpi1-ip>
RPI2_USER=<rpi2-user>
RPI2_IP=<rpi2-ip>
```

### Raspberry Pi #2's Artifact

Raspberry Pi #2 runs Mender itself, so, just like `rootfs-image` does locally
for the System Device, `mqtt-component` expects to receive a complete, separate
Mender Artifact and hand it straight to `mender-update install` on the
Component. Build that inner Artifact first, snapshotting Raspberry Pi #2's
live filesystem over SSH:

```bash
DEVICE_TYPE=raspberrypi4    # Raspberry Pi #2's own device_type

mender-artifact write rootfs-image \
    --file ssh://"${RPI2_USER}@${RPI2_IP}" \
    --compatible-types "${DEVICE_TYPE}" \
    --artifact-name rpi2-v1 \
    --output-path rpi2-rootfs-v1.mender \
    --ssh-args="-o UserKnownHostsFile=/dev/null" \
    --ssh-args="-o StrictHostKeyChecking=no"
```

!!! Raspberry Pi #2 is temporarily frozen during snapshot creation to ensure
!!! consistency. This may take several minutes depending on the root
!!! filesystem size.

Now wrap that Artifact as the payload for the `mqtt-component` Interface,
so the Orchestrator routes it there:

```bash
mender-artifact write module-image \
    --type mqtt-component \
    --compatible-types "${DEVICE_TYPE}" \
    --artifact-name rpi2-v1 \
    --file rpi2-rootfs-v1.mender \
    --output-path rpi2-v1.mender
```

`--compatible-types` here must be the same `raspberrypi4` used as
`component_type` in the Topology.

### Raspberry Pi #1's Artifact

The System Device's own Artifact is built exactly as in the ESP32-S3 example,
with `rootfs-image` directly:

```bash
mender-artifact write rootfs-image \
    --file ssh://"${RPI1_USER}@${RPI1_IP}" \
    --compatible-types raspberrypi5 \
    --artifact-name rpi1-v1 \
    --output-path rpi1-v1.mender \
    --ssh-args="-o UserKnownHostsFile=/dev/null" \
    --ssh-args="-o StrictHostKeyChecking=no"
```

Replace `raspberrypi5` with Raspberry Pi #1's own `device_type`.

## Step 6 - Create the Manifest and its Artifact

The [Manifest](../../02.Manifest/docs.md) defines the target state of the
whole System. On your **workstation**:

```bash
cat > manifest-v1.yaml << 'EOF'
api_version: "mender/v1"
kind: "manifest"
name: "system-v1"
system_types_compatible: ["rpi-rpi-mqtt-system"]

component_types:
  raspberrypi5:
    artifact_name: rpi1-v1
    update_strategy:
      order: 10

  raspberrypi4:
    artifact_name: rpi2-v1
    update_strategy:
      order: 20
EOF
```

Replace `raspberrypi5` / `raspberrypi4` with your two boards' actual device
types, matching the Topology from Step 4. Order 10 installs Raspberry Pi #1
first, then order 20 pushes the update to Raspberry Pi #2 over MQTT.

Turn the Manifest into a Mender Artifact with
`mender-orchestrator-manifest-gen` (install it as described in
[Create a Manifest Artifact](../../02.Manifest/01.Manifest-Artifact/docs.md#installation)
if you don't have it yet):

```bash
mender-orchestrator-manifest-gen \
    --artifact-name system-v1 \
    --output-path system-v1.mender \
    --system-type rpi-rpi-mqtt-system \
    manifest-v1.yaml
```

## Step 7 - Upload the Artifacts and deploy

Upload the three Artifacts to hosted Mender, under the **Software** section:

* `rpi1-v1.mender` - Raspberry Pi #1's root filesystem
* `rpi2-v1.mender` - Raspberry Pi #2's wrapped root filesystem
* `system-v1.mender` - the Manifest

Then deploy the Manifest:

1. In hosted Mender, go to **Devices** and find Raspberry Pi #1.
2. From **Device actions**, select **Create a deployment for this device**.
3. Choose the `system-v1` Release and start the deployment.

## Step 8 - Verify the result

Watch the Component agent on **Raspberry Pi #2** while the deployment runs:

```bash
journalctl -u mender-mqtt-agent -f
```

You should see it execute `Download`, `ArtifactInstall`, then reboot itself
for `ArtifactReboot`. The agent comes back up automatically (its systemd unit
has `Restart=always`), reconnects, and the retained MQTT command it receives on
reconnect is recognized as already handled rather than re-executed, so it
proceeds straight to `ArtifactVerifyReboot`, `ArtifactCommit`, and `Cleanup`.

Once the deployment reaches **Finished** in hosted Mender, check the installed
versions in the Server UI or from **Raspberry Pi #1**:

```bash
sudo mender-orchestrator show-provides
```

You should see Raspberry Pi #1 reporting `rpi1-v1` and Raspberry Pi #2's
Component ID (`rpi2-component`) reporting `rootfs-image.version=rpi2-v1`. You
can confirm independently on **Raspberry Pi #2** itself:

```bash
mender-update show-provides
```

## Deploy a second version

To push an update to just Raspberry Pi #2, build a new snapshot the same way
as Step 5, with a new name:

```bash
mender-artifact write rootfs-image \
    --file ssh://"${RPI2_USER}@${RPI2_IP}" \
    --compatible-types raspberrypi4 \
    --artifact-name rpi2-v2 \
    --output-path rpi2-rootfs-v2.mender \
    --ssh-args="-o UserKnownHostsFile=/dev/null" \
    --ssh-args="-o StrictHostKeyChecking=no"

mender-artifact write module-image \
    --type mqtt-component \
    --compatible-types raspberrypi4 \
    --artifact-name rpi2-v2 \
    --file rpi2-rootfs-v2.mender \
    --output-path rpi2-v2.mender
```

Create a version 2 Manifest. Raspberry Pi #1 keeps `rpi1-v1` (nothing to do
there, so it is not reinstalled), and only Raspberry Pi #2 moves to `rpi2-v2`:

```bash
cat > manifest-v2.yaml << 'EOF'
api_version: "mender/v1"
kind: "manifest"
name: "system-v2"
system_types_compatible: ["rpi-rpi-mqtt-system"]

component_types:
  raspberrypi5:
    artifact_name: rpi1-v1
    update_strategy:
      order: 10

  raspberrypi4:
    artifact_name: rpi2-v2
    update_strategy:
      order: 20
EOF

mender-orchestrator-manifest-gen \
    --artifact-name system-v2 \
    --output-path system-v2.mender \
    --system-type rpi-rpi-mqtt-system \
    manifest-v2.yaml
```

Upload `rpi2-v2.mender` and `system-v2.mender` to hosted Mender, then deploy
the `system-v2` Release to Raspberry Pi #1 as before. Watch
`journalctl -u mender-mqtt-agent -f` on Raspberry Pi #2 again to see the push
arrive and the second reboot happen automatically.
