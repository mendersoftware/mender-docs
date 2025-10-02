---
title: Topology
taxonomy:
    category: docs
---

A Topology is a YAML file used for defining the Components of a System.

The Topology should be provisioned alongside a new System. It defines what Components are present in a System and how they can be updated. Once defined, the Topology is shown as part of Mender Orchestrator's provides, and is sent to the Mender Server as regular inventory through an inventory script.

The mechanism for providing a Topology will depend on your choice of OS distribution or build system.
It should be located at `MENDER_ORCHESTRATOR_TOPOLOGY_DIR` (default: `/data/mender-orchestrator/topology.yaml`).

## Example:

```yaml
api_version: "mender/v1"
kind: "topology"
system_type: "electric-vehicle-2021"

components:
  - component_type: telematics_control_unit
    interface: cellular-ota
    interface_args: ["tcu1", "15:22:aa:33:ff"]

  - component_type: ecu_brake_controller
    interface: canbus
    interface_args: ["front", "15:22:aa:33:ff"]

  - component_type: seat_heating
    interface: i2c
    interface_args: ["--bus=1", "--address=0x48"]
```

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `api_version` | string | ✓ | API version specification |
| `kind` | string | ✓ | Kind of yaml (should be set to "topology") |
| `system_type` | string | ✓ | The System type of the System |
| `components` | list | ✓ | List of all Components in the System |

### Component list
Each component entry in `components` should have these fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `component_type` | string | ✓ | Unique identifier for this Component type |
| `interface` | string | | Interface used to update this Component (defaults to `component_type` if not set)|
| `interface_args` | list of strings | | Custom arguments passed to the Interface |
