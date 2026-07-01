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
system_type: "electric-vehicle-2026"

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
| `components` | list | ✓<sup>1</sup> | List of all Components in the System |

<sup>1</sup> Required in this file unless the Components are supplied through a separate Topology components file. See [Splitting the Topology](#splitting-the-topology).

### Component list
Each component entry in `components` should have these fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `component_type` | string | ✓ | Unique identifier for this Component type |
| `interface` | string | | Interface used to update this Component (defaults to `component_type` if not set)|
| `interface_args` | list of strings | | Custom arguments passed to the Interface |

## Splitting the Topology

A Topology has two parts: the top-level fields (`api_version`, `kind`,
`system_type`) that describe the System, and the **Topology components**, the
`components` list that describes each Component of the System and how it is
updated. These two parts do not have to live in the same file.

By default both parts are in a single `topology.yaml` (as in the example above).
Alternatively, you can keep only the top-level fields in the main `topology.yaml`
and move the Topology components into their own file: a YAML file that contains
just the `components` list.

When splitting the Topology:

* The main `topology.yaml` contains only the top-level fields and **no**
  `components` section.
* A separate file contains **only** the `components` list, using the same
  Component fields described above.

Point Mender Orchestrator at the separate Components file in one of three ways:

* the `--topology-components` (`-t`) command-line option,
* the `MENDER_ORCHESTRATOR_TOPOLOGY_COMPONENTS_FILE` environment variable, or
* the [`TopologyComponents`](../08.Configuration/50.Configuration-options/docs.md#topologycomponents)
  configuration option.

!! The `components` list must be defined in exactly one place. If both the main
!! `topology.yaml` and a separate Components file define Components, or if neither
!! does, Mender Orchestrator rejects the Topology with an error.

### Example

Main `topology.yaml` with top-level fields only:

```yaml
api_version: "mender/v1"
kind: "topology"
system_type: "electric-vehicle-2026"
```

Separate Topology components file (for example `topology-components.yaml`):

```yaml
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

Provide the Components file when invoking Mender Orchestrator:

```bash
mender-orchestrator --topology-components /data/mender-orchestrator/topology-components.yaml install <manifest>
```

## Adding and removing Components

The Topology describes the set of Components that make up a System, and that set
can change over the lifetime of a System, for example when a new peripheral is
added or an old one is decommissioned.

### When a Topology change takes effect

When a deployment starts, Mender Orchestrator reads the Topology, including any
separate Topology components file, **once**, and uses that snapshot for the
whole deployment. Editing the Topology, or the separate Topology components
file, while a deployment is in progress has **no effect on it**. The change is
picked up only by the **next** deployment.

So a Component you add does not become part of a deployment that is already
running or has already finished; it becomes part of the System from the next
deployment onwards.

### Adding a Component

To add a Component, list it in the Topology (or the Topology components file) and
deploy a Manifest that includes it. Mender Orchestrator installs the new
Component on the next deployment.

Every Component in the Topology must have a matching `component_type` in the deployed
Manifest, otherwise the deployment fails with a validation error.

### Removing a Component

To remove a Component, delete it from the Topology (or the Topology components
file). From the next deployment onwards, Mender Orchestrator no longer updates it.

!! Removing a Component from the Topology does **not** uninstall it from the
!! device — it stays installed and keeps running.

While a Component is still listed in the Topology, every deployment must include a
matching artifact for it in the deployed Manifest. To keep a Component listed
without updating it, deploy the artifact it already has installed: when the
Component's installed provides already match that artifact, nothing is installed.

If you are also removing the Component's hardware, delete it from the Topology
**first** and let the next deployment apply the change, then remove the hardware.
Mender Orchestrator queries a listed Component's Interface on every deployment, so
removing the hardware while the Component is still listed can break those
deployments.
