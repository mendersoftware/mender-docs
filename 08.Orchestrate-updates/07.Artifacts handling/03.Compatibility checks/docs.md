---
title: Compatibility checks
taxonomy:
    category: docs
---
As the System Device is running Mender, it stores all information about currently installed Artifacts in its database, allowing direct comparisons between a given Artifact and what's currently present on the Device. This is used to check if an Artifact is currently installed and if an Artifact can be installed on the Device.

However, as the Components do not need to run Mender in order to be updated by the Orchestrator, there's no requirement for them to keep track of all the data from the Artifact.

To allow the Components to handle the updates and not require them to have a database, Orchestrator checks are different.

This section contains details on how Orchestrator checks whether an Artifact is currently installed on a Component and if an Artifact can be installed on a Component.

## Artifact versioning for Components

Every Interface must include a `version` key-value pair in its Inventory data.
The `version` field is used exclusively for inventory reporting: the Component sends this specific field to the Mender Server as its currently installed software version.

This does not influence checking if an Artifact is currently installed on a Component. For more
information on this topic, see [Artifact selection](../04.Artifact%20selection/docs.md).

### Example

Creating an Artifact for a `custom-interface`:

```bash
INTERFACE=custom-interface
COMPONENT_TYPE=rtos
VERSION=custom-v1
PAYLOAD=$VERSION-payload

touch $PAYLOAD
mender-artifact \
  write module-image \
  --type $INTERFACE \
  --artifact-name $VERSION \
  --compatible-types $COMPONENT_TYPE \
  --provides custom-version:$VERSION \
  --clears-provides custom-version.* \
  --no-default-clears-provides \
  --no-default-software-version \
  --file $PAYLOAD \
  --output-path $VERSION.mender

rm $PAYLOAD
```

Will result in an Artifact like this:

```
Mender Artifact:
  Name: custom-v1
  Format: mender
  Version: 3
  Signature: no signature
  Compatible types: [rtos]
  Provides group: 
  Depends on one of artifact(s): []
  Depends on one of group(s): []
  State scripts: []

Updates:
  - Type: custom-interface
    Provides:
      custom-version: custom-v1
    Depends: {}
    Clears Provides: [custom-version.*]
    Metadata: {}
    Files:
      - checksum: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
        modified: 2026-10-19 15:27:47 +0200 CEST
        name: custom-v1-payload
        size: 0
```

To ensure that, while deploying this Artifact to a Component that already uses it, the Artifact is not installed again, the Interface must report `custom-version=rtos-v1` in its `Provides` output.
The Interface must still report the `version` key from the `Inventory` command output.

See [Artifact selection](../04.Artifact%20selection/docs.md) for more information on how Artifacts
are chosen for installation.

## Topology's component_type and Artifact's device_type relationship
<!--AUTOVERSION: "mender-artifact/blob/%/Documentation/artifact-format-v3.md"/ignore-->
When deploying updates to Systems, Mender Orchestrator abstracts the verification of Artifact compatibility based on `component_type`. While [Mender Artifacts](https://github.com/mendersoftware/mender-artifact/blob/master/Documentation/artifact-format-v3.md?target=_blank) rely on the `artifact_depends: device_type` field for compatibility matching, Components do not - and must not - report a `device_type` key from their Interfaces for `Provides` command.

The Orchestrator uses the `component_type` from the Topology corresponding to a given component, and compares this value against the incoming Artifact's `device_type`.

This is done to prevent errors that can arise from mismatching `component_type` and `device_type`. This way, each Component has only `component_type` which defines its type exclusively.

### Interface requirements

Returning a `device_type` field in `Provides` command output is prohibited.

### Compatibility with Components running Mender

Each Component that runs Mender, has its own `device_type` built-in. See how Mender determines the `device_type` [here](../../../03.Client-installation/07.Configuration/50.Configuration-options/docs.md#devicetypefile).

Since the Orchestrator uses the `component_type` from the Topology to verify Artifact compatibility, Component's built-in `device_type` must be equal to the corresponding `component_type` in the Topology. Otherwise, the Artifact created for a given `component_type` will be rejected by the Component running Mender, as the Artifact's `artifact_depends` will not match the Component's built-in `device_type`.

### Example

Given an example [Topology](../../06.Examples/01.Mock-components/docs.md#demo-environment):

```yaml
api_version: mender/v1
kind: topology
system_type: "system-core"

components:
  - component_type: gateway
    interface: rootfs-image

  - component_type: rtos
    interface: rtos-interface
    interface_args: ["1"]

  - component_type: rtos
    interface: rtos-interface
    interface_args: ["2"]
```

When creating Artifacts for this system, `gateway` and `rtos` `--compatible-types` flag must be used to ensure that the Artifacts can be installed. Just as in the [example](#example) above.

This means that the System Device in this example must have the built-in `device_type` set to `gateway`. Otherwise, when deploying an Artifact for `gateway` `component_type`, it will be rejected by the System Device, due to the Artifact's `artifact_depends: device_type` value and the built-in `device_type` mismatch.
