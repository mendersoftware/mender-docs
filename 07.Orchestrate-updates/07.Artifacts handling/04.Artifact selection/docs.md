---
title: Artifact selection
taxonomy:
    category: docs
---

A Deployment to a System device delivers a single [Manifest Artifact](../../02.Manifest/01.Manifest-Artifact/docs.md). The Artifacts for the individual Components are not part of the Deployment. Mender Orchestrator selects and downloads them on the device, one Component at a time.

## Selecting the Manifest Artifact

The Mender Server selects the Manifest Artifact with the regular [algorithm for selecting the Deployment for the Device](../../../02.Overview/05.Deployment/docs.md#algorithm-for-selecting-the-deployment-for-the-device), matching on the System type from the [Topology](../../03.Topology/docs.md) instead of the device type.

## Selecting the Component Artifacts

Mender Orchestrator receives a Manifest either from a Deployment, through the `mender-orchestrator-manifest` Update Module, or directly in [Standalone mode](../../09.Standalone-mode/docs.md). It then goes through the Components in the Topology and decides which Artifact, if any, to install on each.

Which Artifacts are candidates depends on how the Component type is set in the Manifest:

* `artifact_path`: the Artifact at that path is the only candidate. If the file does not exist and `artifact_name` is also set, Mender Orchestrator falls back to `artifact_name`.
* `artifact_name`: the candidates are the Artifacts in that Release on the Mender Server that are compatible with the `component_type` from the Topology. Artifacts without `artifact_provides` are ignored.

Mender Orchestrator then queries the Component's Interface for its `Provides` and narrows the candidates down:

1. Artifacts already installed on the Component are excluded. An Artifact counts as installed if applying its `artifact_provides` and `clears_artifact_provides` to the Component's `Provides` would change nothing. Keys the Artifact does not clear are kept, so an Artifact that updates only part of a Component counts as installed when its own keys match. An Artifact without `clears_artifact_provides` clears all keys. `artifact_name` is left out of this comparison unless it is the only key on either side.
2. The remaining Artifacts are filtered by `artifact_depends`: every key the Artifact depends on must be present in the Component's `Provides` with one of the listed values. See [Compatibility checks](../03.Compatibility%20checks/docs.md) for how `device_type` is handled.
3. Of the remaining Artifacts, the one with the smallest size is selected.

Selection runs for every Component before any Artifact is downloaded or installed.

## Example

Consider a System with this Topology:

```yaml
api_version: mender/v1
kind: topology
system_type: "system-core"

components:
  - component_type: rtos
    interface: rtos-interface
    interface_args: ["1"]

  - component_type: rtos
    interface: rtos-interface
    interface_args: ["2"]

  - component_type: rtos
    interface: rtos-interface
    interface_args: ["3"]
```

The `rtos-interface` Interface reports these Components as `R123`, `R456` and `R789`. The Manifest contains:

```yaml
component_types:
  rtos:
    artifact_name: rtos-v2
    update_strategy:
      order: 10
```

The Artifact `rtos-v2` has:

| `artifact_provides` | `artifact_depends` |
|---------------------|--------------------|
| `rootfs-image.rtos-interface.version: rtos-v2` | `rootfs-image.rtos-interface.version: [rtos-v1]` |

Mender Orchestrator runs the steps for each Component:

| Component | `Provides` | 1. Installed? | 2. Depends met? | Result |
|-----------|------------|---------------|-----------------|--------|
| `R123` | `rootfs-image.rtos-interface.version=rtos-v1` | no | yes | Artifact selected |
| `R456` | `rootfs-image.rtos-interface.version=rtos-v2` | yes | - | left unchanged |
| `R789` | `rootfs-image.rtos-interface.version=rtos-v0` | no | no | no candidate, update fails |

With `R789` in the Topology the update fails before any Component is modified. Without it, `R123` is updated and `R456` is skipped. Step 3 only matters when more than one Artifact is compatible with the Component type, for example a full image and a smaller patch.
