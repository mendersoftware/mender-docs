---
title: State script support
taxonomy:
    category: docs
---

[State scripts](../../08.Artifact-creation/04.State-scripts/docs.md) let you hook custom
commands into the states of an update. Mender Orchestrator does not run state scripts itself.
Instead, whether an Artifact's state scripts run depends on the Interface that installs the
Artifact.

## How the Orchestrator handles state scripts

An Interface only has access to the state scripts if it requests the full, packed Artifact by
answering `No` to the [`NeedsUnpackedArtifact`](../04.Interface-protocol/docs.md#download-state)
query. The Orchestrator then forwards the complete Artifact, and the Interface — or a downstream
consumer such as the Mender Client — is responsible for running the scripts.

If the Interface does not request the full Artifact, any state scripts the Artifact contains are
ignored.

## The `rootfs-image` Interface

The built-in [rootfs-image](https://github.com/mendersoftware/mender-orchestrator-support/blob/main/interfaces/v1/rootfs-image)
Interface requests the full Artifact and runs `mender-update` in standalone mode, which executes
the state scripts.

Because `mender-update` runs in standalone mode, the [reboot-related state scripts are not run](../../08.Artifact-creation/04.State-scripts/docs.md#standalone-mode).
Standalone mode omits the `ArtifactReboot` and `ArtifactRollbackReboot` states, so their state
scripts (`ArtifactReboot_Enter`, `ArtifactReboot_Leave`, `ArtifactReboot_Error`,
`ArtifactRollbackReboot_Enter`, and `ArtifactRollbackReboot_Leave`) are never executed.
