---
title: Examples
taxonomy:
    category: docs
---

This section provides working examples to demonstrate how Mender Orchestrator operates with System-level updates through manifests and Components.

## Prerequisites

Before proceeding with these examples, you'll need:

- A working Mender Orchestrator setup with the demo mock environment (see [Installation section](../05.Installation/docs.md) for setup details)
- [mender-artifact](../../12.Downloads/01.Workstation-tools/docs.md#mender-artifact) tool on your host

## Demo Environment

The demo setup includes a **demo environment** that simulates a System with multiple Components.
This environment is provided by the [mender-orchestrator-support](https://github.com/mendersoftware/mender-orchestrator-support)
repository and includes a predefined Topology with the System device ("gateway") and two demo Components ("rtos"):
```yaml
api_version: mender/v1
kind: topology
system_type: "system-core"

components:
  - component_type: gateway
    interface: rootfs-image

  - component_type: rtos
    interface: rtos
    interface_args: ["1"]

  - component_type: rtos
    interface: rtos
    interface_args: ["2"]
```

### Example Manifest Structure

Each Manifest defines which Artifact to deploy to each Component:

```yaml
api_version: "mender/v1"
kind: "manifest"
name: "system-core-v1"
system_types_compatible: ["system-core"]

component_types:
  gateway:
    artifact_name: gateway-v1
    update_strategy:
      order: 10

  rtos:
    artifact_name: rtos-v1
    update_strategy:
      order: 20
```

## Demo Examples

These examples demonstrate System updates using the demo environment with a gateway (Linux rootfs) and two demo RTOS Components. You'll create your own manifests and Artifacts.

### Step 1: Create RTOS Component Artifacts

First, create demo RTOS Artifacts for your Components:

```bash
# Create RTOS v1 artifact
COMPONENT_TYPE=rtos
VERSION=rtos-v1
PAYLOAD=$VERSION-payload

touch $PAYLOAD
mender-artifact \
  write module-image \
  --type $COMPONENT_TYPE \
  --device-type $COMPONENT_TYPE \
  --provides version:$VERSION \
  --file $PAYLOAD \
  --output-path $VERSION.mender \
  --artifact-name $VERSION

rm $PAYLOAD
```

```bash
# Create RTOS v2 artifact
COMPONENT_TYPE=rtos
VERSION=rtos-v2
PAYLOAD=$VERSION-payload

touch $PAYLOAD
mender-artifact \
  write module-image \
  --type $COMPONENT_TYPE \
  --device-type $COMPONENT_TYPE \
  --provides version:$VERSION \
  --file $PAYLOAD \
  --output-path $VERSION.mender \
  --artifact-name $VERSION

rm $PAYLOAD
```

### Step 2: Create Gateway Artifacts

Generate rootfs Artifacts for the gateway Component using the `mender-artifact` snapshot feature:

```bash
IP_ADDRESS=<your-device-ip>
PORT=<your-device-port>
DEVICE_TYPE=<your-device-type>
USER=<your-user>

# Create gateway-v1 Artifact using snapshot
mender-artifact write rootfs-image \
    --file ssh://"${USER}@${IP_ADDRESS}" \
    --device-type "${DEVICE_TYPE}" \
    --artifact-name gateway-v1 \
    --output-path gateway-v1.mender \
    --ssh-args="-p ${PORT}" \
    --ssh-args="-o UserKnownHostsFile=/dev/null" \
    --ssh-args="-o StrictHostKeyChecking=no"

# Use same ext4 to create gateway-v2
mkdir -p gateway-dump
mender-artifact dump --files gateway-dump gateway-v1.mender
mender-artifact write rootfs-image \
    --file gateway-dump/rootfs* \
    --device-ttype "${DEVICE_TYPE}"  \
    --artifact-name gateway-v2 \
    --output-path gateway-v2.mender
rm -rf gateway-dump
```

!!! Your device will be temporarily frozen during snapshot creation to ensure consistency. This may take several minutes depending on the rootfs size.

### Step 3: Create Manifests

Create Manifests that define your System state:

```bash
# Create manifest-v1.yaml
cat > manifest-v1.yaml << 'EOF'
api_version: "mender/v1"
kind: "manifest"
name: "system-core-v1"
system_types_compatible: ["system-core"]

component_types:
  gateway:
    artifact_name: gateway-v1
    update_strategy:
      order: 10

  rtos:
    artifact_name: rtos-v1
    update_strategy:
      order: 20
EOF
```

This will first install the gateway-v1 Artifact to the gateway Component. Next it will install the rtos-v1 Artifact to the two rtos Components in parallel.

```bash
# Create manifest-v2.yaml
cat > manifest-v2.yaml << 'EOF'
api_version: "mender/v1"
kind: "manifest"
name: "system-core-v2"
system_types_compatible: ["system-core"]

component_types:
  gateway:
    artifact_name: gateway-v2
    update_strategy:
      order: 10

  rtos:
    artifact_name: rtos-v2
    update_strategy:
      order: 20
EOF
```

This will first install the gateway-v2 Artifact to the gateway Component. Next it will install the rtos-v2 Artifact to the two rtos Components in parallel.

### Step 4: Generate Manifest Artifacts

Use the Manifest Artifact generator to create Mender Artifacts from your Manifests. First, ensure you have the generator installed as described in [Create a Manifest Artifact](../02.Manifest/01.Manifest-Artifact/docs.md#installation).

```bash
# Generate manifest-v1 artifact
SYSTEM_TYPE="system-core"
mender-orchestrator-manifest-gen \
    --artifact-name manifest-v1 \
    --output-path manifest-v1.mender \
    --system-type $SYSTEM_TYPE \
    manifest-v1.yaml

# Generate manifest-v2 artifact
mender-orchestrator-manifest-gen \
    --artifact-name manifest-v2 \
    --output-path manifest-v2.mender \
    --system-type $SYSTEM_TYPE \
    manifest-v2.yaml
```

### Step 5: Upload All Artifacts

Upload all your created Artifacts to hosted Mender:

1. Go to your hosted Mender **Releases** section
2. Upload all the artifacts you just created:
   - `gateway-v1.mender`, `gateway-v2.mender`
   - `rtos-v1.mender`, `rtos-v2.mender`
   - `manifest-v1.mender`, `manifest-v2.mender`

### Step 6: System Update Example

Deploy a Manifest to update the entire System:

1. Create a deployment in hosted Mender
2. Select `manifest-v1` as the Release
3. Deploy to your device

**What happens:**
- Mender Client receives the Artifact containing the Manifest
- Mender Client invokes Mender Orchestrator
- Mender Orchestrator receives the Manifest
- It downloads and installs the specified Component Artifacts (`gateway-v1`, `rtos-v1`)
- Updates occur in the order specified by the Manifest
  - First it will install `gateway-v1` to the System device and reboot into the new rootfs image
  - Then it will install `rtos-v1` to the two rtos demo Components
- System maintains consistency across all Components

We can now check Mender Orchestrator's provides directly on the System device:
```bash
# irrelevant provides entries removed from example
root@qemux86-64:~# mender-orchestrator show-provides
record_id=1 severity=info time="2025-Oct-15 11:08:51.593812" name="Global" msg="Update Interface output (stderr): using interface /sys/class/net/enp0s3"
gateway.52:54:00:1d:94:82.artifact_name=gateway-v1
gateway.52:54:00:1d:94:82.data-partition.mender-orchestrator-manifest.version=manifest-v1
gateway.52:54:00:1d:94:82.device_type=qemux86-64
gateway.52:54:00:1d:94:82.rootfs-image.version=gateway-v1
rtos.R123.device_type=rtos
rtos.R123.version=rtos-v1
rtos.R456.device_type=rtos
rtos.R456.version=rtos-v1
```

You should see something similar to the output above. We can see that the gateway reports
`gateway-v1` as its version, and that the two rtos Components report `rtos-v1`. You can
also see this information by navigating to your System device's Software tab in hosted Mender.

### Step 7: Testing Update Failures

Test the rollback behavior when a Component update fails:

1. Simulate a Component failure:
   ```bash
   # Simulate a failure in one of the RTOS components
   touch /data/mender-orchestrator/mock-instances/2/ArtifactCommit.FAIL
   ```

2. Deploy `manifest-v2` from hosted Mender.

3. Observe the failure:

    First `gateway-v2` will be installed and the System device will reboot. Then the update
    to one of the Components will fail, and Mender Orchestrator will rollback all components.

    Run `mender-orchestrator show-provides` on the System device again to see that the rollback
    was succesful, and see that the System maintained consistency as described by the previous
    successful Manifest installation.

4. Remove the failure condition:
   ```bash
   # Remove the failure condition
   rm -f /data/mender-orchestrator/mock-instances/2/ArtifactCommit.FAIL
   ```
5. Retry the deployment:
   Deploy `manifest-v2` again - it should now succeed.

    We can again verify the update by checking the Software tab in hosted Mender or by
    running `show-provides` directly in the System device:
    ```bash
    # irrelevant provides entries removed from example
    root@qemux86-64:~# mender-orchestrator show-provides
    record_id=1 severity=info time="2025-Oct-15 11:21:01.770356" name="Global" msg="Update Interface output (stderr): using interface /sys/class/net/enp0s3"
    gateway.52:54:00:1d:94:82.artifact_name=gateway-v2
    gateway.52:54:00:1d:94:82.data-partition.mender-orchestrator-manifest.version=manifest-v2
    gateway.52:54:00:1d:94:82.device_type=qemux86-64
    gateway.52:54:00:1d:94:82.rootfs-image.checksum=83c6b1eee18dc7e3ac2f47a601bdbd93093785be9220bf386e05c7782affa209
    gateway.52:54:00:1d:94:82.rootfs-image.version=gateway-v2
    rtos.R123.device_type=rtos
    rtos.R123.version=rtos-v2
    rtos.R456.device_type=rtos
    rtos.R456.version=rtos-v2
    ```
