---
title: Examples
taxonomy:
    category: docs
---

# Examples

This section will explain how the Orchestrator works through copy-pastable working examples.

REQUIREMENTS:
* you can run Python on your host
* you can run [mender-artifact](../../../10.Downloads/docs.md#mender-artifact) on your host
* you can run a Docker image on your host
* you have a Hosted Mender tenant and can get a token


## Prepare the environment

```bash
mkdir orch-install
ORCH_EVAL_DIR=$(realpath orch-install)
mkdir -p $ORCH_EVAL_DIR/bin
PATH=$PATH:$ORCH_EVAL_DIR/bin
```

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
cp mender-orchestrator-update-interfaces/modules/mender-orchestrator-manifest/module-artifact-gen/mender-orchestrator-manifest-gen \
      $ORCH_EVAL_DIR/bin
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
CONTAINER_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -aqf "ancestor=mendersoftware/mender-client-qemu:mender-master"))
# If you get multiple IPs use the alternative
# where you need to manually get the container id first
# docker ps
# CONTAINER_ID=<FILL IT>
# CONTAINER_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $CONTAINER_ID)

scp -r -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -P 8822 orch-install root@$CONTAINER_IP:
```

On the **device**:


```bash
# Manually install the Orchestrator and the environment
orch-install/manual_install.sh
# Export the variable the readme suggests
```

``` bash
# Test if the cli is executing correctly
mender-update-orchestrator -h
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


## Examples with real gateway updates


The most complicated orchestrator case is the one where the device that runs the Orchestrator gets updated.
The cases below still use mock devices for the peripheral ROTS devices, but the gateway is going through a full rootfs update.


### Prepare the real rootfs artifacts

The real rootfs update artifacts will be created from runtime using the mender-artifact tool.

On the **host**.

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

``` bash
USER="root"
DEVICE_TYPE="qemux86-64"
TYPE="rootfs-image"
mender-artifact write rootfs-image -f ssh://${USER}@${CONTAINER_IP} \
                                   -n gateway-v5 \
                                   -o gateway-v5.mender \
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

Upload the `gateway-v4.mender` and `gateway-v5.mender` artifacts to Hosted Mender to the tenant the
device is accepted on.


### Example: Standard system update - real gateway - offline

When updating the gateway, any failure in applying the manifest, whether it happens before or after
updating the gateway, triggers a full rollback of all components mentioned in the manifest. Let's
try this functionality in practice by simulating a failure in the last component we update. Execute
this on the **device**:

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
mender-update-orchestrator show-provides
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


### Example: Standard system update - real gateway - Hosted Mender download

In this case the artifact of the gateway is not available on the device but is present on Hosted Mender.
The RTOS artifacts are present on the device.

The orchestrator will pull the gateway artifact form Hosted Mender using the authentication from the Mender client.


```bash
MOCK_DIR=/data/mender-update-orchestrator/mock_env
mender-update-orchestrator install  $MOCK_DIR/system-core-v4/manifest.yaml
# Orchestrator installs the rootfs and reboots
```
Log in into the new system

``` bash
MOCK_DIR=/data/mender-update-orchestrator/mock_env
mender-update-orchestrator resume
mender-update-orchestrator show-provides
```


### Example: Standard system update - real gateway - managed by Hosted Mender

In this example we will perform the same update as in the previous example, but we will do so using
a Hosted Mender deployment instead of installing the manifest using the command line. This makes use
of the `mender-orchestrator-manifest` update module that we installed earlier.

This works just like a regular Mender deployment, including rolling back automatically if a failure
is detected.

#### Prepare the deployment

Let's introduce a failure to see this in action. On the **device**, execute this:

```bash
MOCK_DIR=/data/mender-update-orchestrator/mock_env
touch $MOCK_DIR/mock_instances/R456/ArtifactCommit.FAIL
```

We need to create a special artifact containing the new manifest we want to install. For this we use
the `mender-orchestrator-manifest-gen` tool. On the **host**, execute this:

```bash
DEVICE_TYPE="qemux86-64"
mender-orchestrator-manifest-gen \
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

!!! Make sure the `gateway-v5` release is also present in the list, which we uploaded when preparing
!!! the rootfs artifacts above.

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
