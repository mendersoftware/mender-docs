---
title: Manifest
taxonomy:
    category: docs
---

A Manifest is a YAML file used for defining the Software versions for a given System.

The Manifest defines the exact combination of Artifacts that should be deployed to Components. It specifies which Artifact should be installed on each Component type and controls the update strategy.

## Example:

<!--AUTOVERSION: "electric-vehicle-software-v%"/ignore "tcu-firmware-v%"/ignore "brake-ecu-firmware-v%"/ignore "seat-heating-fw-v%"/ignore-->
```yaml
api_version: "mender/v1"
kind: "manifest"
name: "electric-vehicle-software-v3.2.1"
system_types_compatible: ["electric-vehicle-2026"]

component_types:
  telematics_control_unit:
    artifact_name: tcu-firmware-v2.4.1
    update_strategy:
      order: 30

  ecu_brake_controller:
    artifact_path: /artifacts/brake-ecu-firmware-v1.8.3.mender
    artifact_name: brake-ecu-firmware-v1.8.3
    update_strategy:
      order: 10

  seat_heating:
    artifact_name: seat-heating-fw-v1.2.0
    update_strategy:
      order: 20
```

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `api_version` | string | ✓ | API version specification |
| `kind` | string | ✓ | Kind of yaml (should be set to "manifest") |
| `name` | string | ✓ | Name of the Manifest |
| `system_types_compatible` | list of strings | ✓ | Compatible System types |
| `component_types` | map | ✓ | Defines Artifacts and update strategies for Component types |

### Component types map
`component_types` is a map where each key is a component type defined in the Topology. Each entry should have the component type as the key with the following fields (see [example](#example)):

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `artifact_name` | string | ✓<sup>1</sup> | Name of the Mender Artifact to deploy |
| `artifact_path` | string | ✓<sup>1</sup> | Local file path to Artifact (takes precedence over `artifact_name`) |
| `update_strategy` | map | ✓ | Update configuration |

<sup>1</sup> `artifact_name` and/or `artifact_path` is required. If both are specified, `artifact_path` takes precedence. If the file at `artifact_path` doesn't exist, the system falls back to using `artifact_name`.

### Update strategy
The `update_strategy` map has the following field:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `order` | integer | ✓ | Installation priority<sup>1</sup>.  |

<sup>1</sup> Components are updated in ascending order (lower orders first), with Components having the same order updated in parallel.
