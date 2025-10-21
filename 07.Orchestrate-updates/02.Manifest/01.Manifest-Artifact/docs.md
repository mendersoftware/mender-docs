---
title: Create a Manifest Artifact
taxonomy:
    category: docs
---

`mender-orchestrator-manifest-gen` creates Mender Artifacts containing [Manifests](../docs.md).

### Installation

**Prerequisites**: The `mender-artifact` tool must be installed on your workstation. Follow the [installation instructions here](../../../12.Downloads/01.Workstation-tools/docs.md#mender-artifact).

Download the generator tool from the repository:
<!--AUTOVERSION: "/mender-orchestrator-support/%"/mender-orchestrator-support -->
```bash
curl -O https://raw.githubusercontent.com/mendersoftware/mender-orchestrator-support/0.4.0/modules/mender-orchestrator-manifest/module-artifact-gen/mender-orchestrator-manifest-gen
chmod +x mender-orchestrator-manifest-gen
sudo mv mender-orchestrator-manifest-gen /usr/local/bin/
```

### Usage

Generate a Manifest Artifact from a Manifest YAML file:

```bash
mender-orchestrator-manifest-gen [options] <manifest> [-- [mender-artifact-options]]
```

For usage examples, see the [Examples section](../../06.Examples/docs.md#step-4-generate-manifest-artifacts).

#### Options

- `--artifact-name`: Name for the generated Artifact (defaults to the manifest name)
- `--system-type`: System types compatible with the Artifact (can be specified multiple times for multi-platform support)
- `--output-path`: Output file path (default: `orchestrator-manifest.mender`)
- `manifest`: Path to the Manifest YAML file
- `-- [mender-artifact-options]`: Additional options passed directly to `mender-artifact`

The generated artifact contains:
- **Type**: `mender-orchestrator-manifest`
- **Payload**: The manifest YAML file
- **Provides**: `data-partition.mender-orchestrator-manifest.version`
- **Clears**: `data-partition.mender-orchestrator-manifest.*`
