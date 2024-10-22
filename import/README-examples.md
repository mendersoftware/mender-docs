## Preparing the QEMU

The starting point for successfully completing the examples in this README is a clean `orch-install` directory ready.

REQUIREMENTS:
* you can run mender-artifact on your host
* you can run a Docker image on your host
* you have a Hosted Mender tenant and can get a token

### Manual installation on QEMU

The content of the orch-install directory is ready to be copied to the QEMU device.

Run the command below in a separate terminal on the host.
The command will run a virtual device and consume the terminal.
You have to set the tenant token from your tenant.

```bash
TENANT_TOKEN='<FILL WITH TOKEN>'

docker run -it -p 85:85 -e SERVER_URL='https://hosted.mender.io' -e TENANT_TOKEN=$TENANT_TOKEN --pull=always mendersoftware/mender-client-qemu:resized-for-demo
```

Once the logging prompt shows, you can log in.
The username is root.


Once the device boots it will be visible in Hosted Mender as pending.
Accept it.

With the previous terminal consumed by the virtual device, execute these commands on a different terminal on the host:

``` bash
CONTAINER_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -aqf "ancestor=mendersoftware/mender-client-qemu:resized-for-demo"))
# If you get multiple IPs use the alternative
# where you need to manually get the container id first
# docker ps
# CONTAINER_ID=<FILL IT>
# CONTAINER_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $CONTAINER_ID)

scp -r -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -P 8822 orch-install root@$CONTAINER_IP:
```

On the device:


```bash
# Manually install the Orchestrator and the environment
orch-install/manual_install.sh
# Export the variable the readme suggests
```

``` bash
# Test if the cli is executing correctly
mender-update-orchestrator -h
```

``` bash
# Do a mock install
mender-update-orchestrator install $MOCK_DIR/system-core-v1/manifest.yaml

# Check the state of the system after the install
mender-update-orchestrator show-provides
```


## Examples with mock interfaces and devices

These examples are all executed with mocked devices and versions.
The fact that they are running on a device with an installed Mender client is just a convenience to have a common environment.
They could have easily enough been natively run on an x86_64 machine.

They are all executed on the terminal of the QEMU device.


### Example: Standard system update


Point the Orchestrator to the bundle manifest to update the system.

```bash
mender-update-orchestrator install $MOCK_DIR/system-core-v1/manifest.yaml
```

Once that succeeds, you can see the system components versions with the command below:

```bash
mender-update-orchestrator show-provides
```

The Orchestrator keeps track of the last successfully applied Manifest and prints that with the `show-provides` command.


#### Don't apply version if already present


Attempting to apply the v1 again skips the steps.

```bash
mender-update-orchestrator  install $MOCK_DIR/system-core-v1/manifest.yaml
mender-update-orchestrator show-provides
```

#### System rollback

In this case, one of the devices in a system will fail.
As a result, the system rolls back as a whole.

Set up a failure for one of the mock interfaces.

```bash
touch $MOCK_DIR/mock_instances/R456/ArtifactCommit.FAIL
```

Assuming the device is on v.1 commence an update to v.2:

```bash
mender-update-orchestrator install $MOCK_DIR/system-core-v2/manifest.yaml
```

Because of the failure in one component the whole system stays on v1.

``` bash
mender-update-orchestrator show-provides
```

Clean up the mocked failure and reapply the update:

```bash
rm $MOCK_DIR/mock_instances/R456/ArtifactCommit.FAIL
mender-update-orchestrator install $MOCK_DIR/system-core-v2/manifest.yaml
mender-update-orchestrator show-provides
```

As there was no failure this time, the system successfully updated to v2.


### Example: Multipart Manifest

Sometimes, the full system topology isn't available at the time the bundle is created.
You know what components the system can, in theory, consist of, but the final combination is known only once it's installed in the field.
This is often the case with systems that get assembled on the customer site from modular components.

To accommodate this use case, the bundle comes with a manifest that isn't fully defined and needs to get information available only on the end device.
This is where the multipart Manifest is used.

The top part of the Manifest which comes with the bundle is already present in the environment.

Create the bottom manifest that didn't come with the bundle.

```bash
cat > $MOCK_DIR/system-core-v1.bottom.manifest.yaml << EOF
api_version: mender/v1
kind: update_manifest
components:
  - component_type: gateway
    id: "G13"
    args:
      - arg1
  - component_type: rtos
    id: "R456"
    args:
      - arg1
  - component_type: rtos
    id: "R998"
    args:
      - arg1
EOF
```

We're updating the device back to v1 again using the split manifest approach.
When invoking the mender comment, pass the bottom Manifest to the cli as well.


```bash
mender-update-orchestrator --manifest-components $MOCK_DIR/system-core-v1.bottom.manifest.yaml install $MOCK_DIR/system-core-v1-top-only/manifest.yaml
mender-update-orchestrator --manifest-components $MOCK_DIR/system-core-v1.bottom.manifest.yaml show-provides
```

The Orchestrator will merges the two manifests and updates the system as a whole.


## Examples with real gateway updates


The most complicated orchestrator case is the one where the device that runs the Orchestrator gets updated.
The cases below still use mock devices for the peripheral ROTS devices, but the gateway is going through a full rootfs update.


### Prepare the real rootfs artifacts

The real rootfs update artifacts will be created from runtime using the mender-artifact tool.

On the host.

``` bash
USER="root"
DEVICE_TYPE="qemux86-64"
TYPE="rootfs-image"

mender-artifact write rootfs-image -f ssh://${USER}@${CONTAINER_IP} \
                                   -n gateway-v3 \
                                   -o gateway-v3.mender \
                                   -t $DEVICE_TYPE \
                                   --ssh-args '-p 8822' \
                                   --ssh-args '-o UserKnownHostsFile=/dev/null' \
                                   --ssh-args '-o StrictHostKeyChecking=no'
```

``` bash
USER="root"
DEVICE_TYPE="qemux86-64"
TYPE="rootfs-image"
mender-artifact write rootfs-image -f ssh://${USER}@${CONTAINER_IP} \
                                   -n gateway-v4 \
                                   -o gateway-v4.mender \
                                   -t $DEVICE_TYPE \
                                   --ssh-args '-p 8822' \
                                   --ssh-args '-o UserKnownHostsFile=/dev/null' \
                                   --ssh-args '-o StrictHostKeyChecking=no'
```

```bash
# This is the path on the device where we deliver the created artifact
MOCK_DIR=/data/mender-update-orchestrator/mock_env
scp -P 8822 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no gateway-v3.mender ${USER}@${CONTAINER_IP}:${MOCK_DIR}/system-core-v3/gateway-v3.mender
```

Upload the `gateway-v4.mender` to Hosted Mender to the tenant the device is accepted on.


### Example: Standard system update - real gateway - offline


On the device.

``` bash
MOCK_DIR=/data/mender-update-orchestrator/mock_env
mender-update-orchestrator --log-level debug  install $MOCK_DIR/system-core-v3/manifest.yaml
```

The Orchestrator installs the rootfs for the gateway and reboots.

Log in into the new system to resume the system update:

``` bash
MOCK_DIR=/data/mender-update-orchestrator/mock_env
mender-update-orchestrator resume
mender-update-orchestrator show-provides
```

The orchestrator continues updating the rest of the system components and concludes the system update.


### Example: Standard system update - real gateway - Hosted Mender download

In this case the artifact of the gateway is not available on the device but is present on Hosted Mender.
The RTOS artifacts are present on the device.

The orchestrator will pull the gateway artifact form Hosted Mender using the authentication from the Mender client.


```bash
MOCK_DIR=/data/mender-update-orchestrator/mock_env
mender-update-orchestrator --log-level debug  install  $MOCK_DIR/system-core-v4/manifest.yaml
# Orchestrator installs the rootfs and reboots
```
Log in into the new system

``` bash
MOCK_DIR=/data/mender-update-orchestrator/mock_env
mender-update-orchestrator resume
mender-update-orchestrator show-provides
```
