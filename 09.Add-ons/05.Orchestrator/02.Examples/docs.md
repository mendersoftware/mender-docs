---
title: Examples
taxonomy:
    category: docs
---

# Examples

This section will explain how the Orchestrator works through copy-pastable working examples.

REQUIREMENTS:
* you can run [mender-artifact](../../../10.Downloads/docs.md#mender-artifact) on your host
* you can run a Docker image on your host
* you have a Hosted Mender tenant and can get a token
<!-- MEN-7215: Needs to be replaced with package install. -->
* you have the preview binary of the Mender Orchestrator software (please [contact us](https://mender.io/contact?target=_blank) to get this)


## Prepare the environment

Run this on the **build host**:

```bash
mkdir orch-install
ORCH_EVAL_DIR=$(realpath orch-install)
mkdir -p $ORCH_EVAL_DIR/bin
```

<!-- MEN-7215: Needs to be replaced with package install. -->
Put the `mender-update-orchestrator` binary in the `orch-install/bin` folder.

Clone the repository which contains the support files and the demo:

```bash
git clone https://github.com/mendersoftware/mender-orchestrator-update-interfaces
```

Copy the pregenerated demo env and the interface:

``` bash
cp -r mender-orchestrator-update-interfaces/demo/pregenerated_env/* orch-install
cp -r mender-orchestrator-update-interfaces/interfaces/v1/rootfs-image  \
      $ORCH_EVAL_DIR/share/mender-update-orchestrator/update-interfaces/v1
```

Copy the update module and the inventory script:

```bash
mkdir -p $ORCH_EVAL_DIR/share/mender/modules/v3
cp mender-orchestrator-update-interfaces/modules/mender-orchestrator-manifest/module/v3/mender-orchestrator-manifest \
      $ORCH_EVAL_DIR/share/mender/modules/v3
mkdir -p $ORCH_EVAL_DIR/share/mender/inventory
cp mender-orchestrator-update-interfaces/inventory/mender-inventory-mender-orchestrator \
      $ORCH_EVAL_DIR/share/mender/inventory
```

Install the manifest artifact generator for the host:

```bash
cp mender-orchestrator-update-interfaces/modules/mender-orchestrator-manifest/module-artifact-gen/mender-orchestrator-manifest-gen .
```


## Preparing the QEMU host

The starting point for successfully completing the examples in this README is a clean `orch-install` directory ready.

### Manual installation on QEMU

The content of the orch-install directory is ready to be copied to the QEMU device.

Run the command below in a separate terminal on the host.
The command will run a virtual device and consume the terminal.
You have to set the tenant token from your tenant.

<!--AUTOVERSION: "mendersoftware/mender-client-qemu:mender-%"/integration-->
```bash
TENANT_TOKEN='<FILL WITH TOKEN>'

# Change this to eu.hosted.mender.io if you're in that zone.
SERVER_URL=https://hosted.mender.io

docker run -it -p 85:85 -e SERVER_URL=$SERVER_URL -e TENANT_TOKEN=$TENANT_TOKEN mendersoftware/mender-client-qemu:mender-master
```

Once the logging prompt shows, you can log in.
The username is root.


Once the device boots it will be visible in Hosted Mender as pending.
Accept it.

With the previous terminal consumed by the virtual device, execute these commands on a different terminal on the **host**:

<!--AUTOVERSION: "mendersoftware/mender-client-qemu:mender-%"/integration-->
``` bash
IP_ADDRESS=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -aqf "ancestor=mendersoftware/mender-client-qemu:mender-master"))
# If you get multiple IPs use the alternative
# where you need to manually get the container id first
# docker ps
# CONTAINER_ID=<FILL IT>
# IP_ADDRESS=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $CONTAINER_ID)

scp -r -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -P 8822 orch-install root@$IP_ADDRESS:
```

On the **device**:


```bash
# Manually install the Orchestrator and the environment
orch-install/install_demo.sh
# Export the variable the readme suggests
```

``` bash
# Test if the cli is executing correctly
mender-update-orchestrator -h
```

### Prepare the real rootfs artifacts

The real rootfs update artifacts will be created from runtime using the mender-artifact tool.

On the **device**

```bash
mkfifo /data/mender/dump
mender-snapshot dump > /data/mender/dump
```

The last command will not terminate, but will wait for you to execute commands from the host. So
back in the shell on the **host** where you have the variables form the Get Started guide, run:

``` bash
USER="root"
DEVICE_TYPE="qemux86-64"
TYPE="rootfs-image"


ssh -o UserKnownHostsFile=/dev/null  \
    -o StrictHostKeyChecking=no \
    -p 8822 root@${IP_ADDRESS} \
    cat /data/mender/dump > rootfs.ext4

mender-artifact write rootfs-image \
    -f ssh://"${USER}@${IP_ADDRESS}" \
    -t "${DEVICE_TYPE}" \
    -n gateway-v3 \
    -o gateway-v3.mender \
    -f rootfs.ext4

mender-artifact write rootfs-image \
    -f ssh://"${USER}@${IP_ADDRESS}" \
    -t "${DEVICE_TYPE}" \
    -n gateway-v5 \
    -o gateway-v5.mender \
    -f rootfs.ext4
```


Put the `gateway-v3.mender` artifact on the device:

```bash
# This is the path on the device where we deliver the created artifact
MOCK_DIR=/data/mender-update-orchestrator/mock_env
scp -P 8822 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no gateway-v3.mender ${USER}@${IP_ADDRESS}:${MOCK_DIR}/system-core-v3/gateway-v3.mender
```

Upload the `gateway-v5.mender` artifact to Hosted Mender to the tenant the device is accepted on.


## Examples

In these examples we will update the root filesystem of the gateway where the Orchestrator runs, as
well as update two peripheral mock RTOS devices. The two RTOS devices are configured in the manifest
so that their updates will be installed after the gateway.

### Example: Standard system update - managed by Hosted Mender

In this example we will perform the update of the system using Hosted Mender. This works just like a
regular Mender deployment, including rolling back automatically if a failure is detected.

Here we are only deploying an artifact containing the manifest; the artifacts for each component
will be downloaded from Hosted Mender as they are needed.

#### Prepare the deployment

When updating the system, any failure in applying the manifest, whether it happens before or after
updating the gateway, triggers a full rollback of all components mentioned in the manifest. Let's
try this functionality in practice by simulating a failure in the last component we update. On the
**device**, execute this:

```bash
MOCK_DIR=/data/mender-update-orchestrator/mock_env
touch $MOCK_DIR/mock_instances/R456/ArtifactCommit.FAIL
```

We need to create a special artifact containing the new manifest we want to install. For this we use
the `mender-orchestrator-manifest-gen` tool. On the **host**, execute this:


```bash
DEVICE_TYPE="qemux86-64"
ORCH_EVAL_DIR=$(realpath orch-install)
./mender-orchestrator-manifest-gen \
    -n manifest-v5 \
    -o manifest-v5.mender \
    -t $DEVICE_TYPE \
    $ORCH_EVAL_DIR/mock_env/system-core-v5/manifest.yaml
```

Upload the resulting `manifest-v5.mender` artifact to Hosted Mender.

We also need to upload the `rtos-v5.mender` artifact for the mock device, in addition to the
`gateway-v5.mender` artifact which we already uploaded above when creating the rootfs artifacts. Go
ahead and upload the artifact which you can find at this path:
`orch-install/mock_env/system-core-v5/rtos-v5.mender`.

#### Launch the deployment

While logged into Hosted Mender in your browser, click on the "Releases" tab and select the
`manifest-v5` release from the list. Then select "Create a deployment from this release" from the
"Release actions" menu, select "All devices" from the device group list, and click "Create
deployment" to start the deployment.

!!! Make sure the all three releases, `manifest-v5`, `gateway-v5`, and `rtos-v5` are present in the
!!! list, which we uploaded when preparing above.

After a little while, the deployment should finish with the failed status, because of the failure we
introduced above. View it under the "Finished" tab. Go ahead and take a look at the failure log by
clicking "View details", and then "View log" while inside the failed deployment popout. Note in
particular that it was not the rootfs update of the gateway that failed, but the rtos component
which was updated after it, yet it caused both to be rolled back.

Let's remove the failure and retry the deployment. On the **device**, execute this:

```bash
MOCK_DIR=/data/mender-update-orchestrator/mock_env
rm -f $MOCK_DIR/mock_instances/R456/ArtifactCommit.FAIL
```

Then repeat the steps to start the deployment, and wait for it to finish. It should finish with
success this time.

Take a look at the updated inventory for the device by clicking the "Devices" tab in the UI, then
click on the device. Then click on "Software" and "Inventory" tabs to view the installed software
and the rest of the inventory, respectively.


### Example: Standard system update - offline

Let's introduce an artificial failure again, to see how the system responds when using the offline
mode. Execute this on the **device**:

```bash
MOCK_DIR=/data/mender-update-orchestrator/mock_env
touch $MOCK_DIR/mock_instances/R456/ArtifactCommit.FAIL
```

Then execute this to start the installation.

``` bash
MOCK_DIR=/data/mender-update-orchestrator/mock_env
mender-update-orchestrator install $MOCK_DIR/system-core-v3/manifest.yaml
```

The Orchestrator installs the rootfs for the gateway and reboots. So far there are no failures,
since the failure simulation has not kicked in yet.

Log in into the new system to resume the system update:

``` bash
MOCK_DIR=/data/mender-update-orchestrator/mock_env
mender-update-orchestrator resume
```

The orchestrator tries to continue, but the simulated failure happens, which makes it roll back
instead, and reboot once more.

``` bash
MOCK_DIR=/data/mender-update-orchestrator/mock_env
mender-update-orchestrator resume
mender-update-orchestrator show-provides
```

This completes the rollback, and from the listed Provides data, we can see that the version we
wanted to install has not been installed.

Now execute this to remove the failure simulation:

```bash
MOCK_DIR=/data/mender-update-orchestrator/mock_env
rm -f $MOCK_DIR/mock_instances/R456/ArtifactCommit.FAIL
```

Then execute this to apply the manifest a second time:

``` bash
MOCK_DIR=/data/mender-update-orchestrator/mock_env
mender-update-orchestrator install $MOCK_DIR/system-core-v3/manifest.yaml
```

The system should reboot. When it is back online, log in and execute this:

``` bash
MOCK_DIR=/data/mender-update-orchestrator/mock_env
mender-update-orchestrator resume
mender-update-orchestrator show-provides
```

The orchestrator continues updating the rest of the system components and concludes the system update.
