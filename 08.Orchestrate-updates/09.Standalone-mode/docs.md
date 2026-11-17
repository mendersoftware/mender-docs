---
title: Standalone mode
taxonomy:
    category: docs
---

Mender Orchestrator supports *standalone* mode, where updates are triggered locally
on the System device instead of being deployed from the Mender Server. This is useful
for Systems without network connectivity, or Systems updated through external storage
like a USB stick.

In standalone mode, you provide a [Manifest](../02.Manifest/docs.md) YAML file directly
to Mender Orchestrator, and reference the Artifacts for each Component type with the
`artifact_path` field.

## Install a Manifest

Create a Manifest which references the local Artifacts with `artifact_path`:

<!--AUTOVERSION: "electric-vehicle-software-v%"/ignore "tcu-firmware-v%"/ignore "brake-ecu-firmware-v%"/ignore-->
```yaml
api_version: "mender/v1"
kind: "manifest"
name: "electric-vehicle-software-v3.2.1"
system_types_compatible: ["electric-vehicle-2026"]

component_types:
  telematics_control_unit:
    artifact_path: tcu-firmware-v2.4.1.mender
    update_strategy:
      order: 30

  ecu_brake_controller:
    artifact_path: brake-ecu-firmware-v1.8.3.mender
    update_strategy:
      order: 10
```

`artifact_path` can be an absolute path, or a path relative to the location of the
Manifest file. Relative paths are resolved throughout the installation, so if the Manifest
resides on external storage, the mount point must stay the same across reboots for `resume`
to find the Artifacts.

!!! If a referenced Artifact is not available locally, Mender Orchestrator falls back to downloading the Artifact given by `artifact_name` from the Mender Server, see the [Manifest documentation](../02.Manifest/docs.md#component-types-map). On a System device without server access, every Component's Artifact must be available through `artifact_path`.

Install the Manifest by running the following command on the System device:

```bash
mender-orchestrator install /path/to/manifest.yaml
```

Mender Orchestrator updates the Components as described in the
[update process](../01.Overview/docs.md#update-process), and commits the update
automatically once all Components are updated successfully. If any Component fails,
the whole System is rolled back.

## Reboots

If a Component update requires rebooting the System device, Mender Orchestrator reboots
it as part of the installation. After the System device has booted, continue the
installation by running:

```bash
mender-orchestrator resume
```

## Verify the update before committing

By default, the installation runs to completion and commits automatically. To inspect
the System before making the update permanent, stop the installation before the commit:

```bash
mender-orchestrator install /path/to/manifest.yaml --stop-before ArtifactCommit
```

After verifying the update, commit it by resuming the installation:

```bash
mender-orchestrator resume
```

If you are not happy with the update, roll back the System instead:

```bash
mender-orchestrator rollback
```

`--stop-before` accepts the states `ArtifactCommit`, `ArtifactRollback` and `Cleanup`,
and can also be given to the `resume` and `rollback` commands.

## Ongoing deployments

Standalone and [managed updates](../01.Overview/docs.md#managed-updates-by-leveraging-mender-client)
share the same installation state. If a deployment is already in progress, `install` refuses
to start a new one until the ongoing installation is resumed or rolled back.
