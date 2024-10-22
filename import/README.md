# Update Orchestrator

The Update Orchestrator is the software responsible for updating the devices in a system.

It is responsible for inspecting the system’s current state, such as the software versions running on the devices. It can also read the system's desired state from a configuration file, the Update Manifest, and apply the changes to the different Devices to reach the state described in the Manifest. If this is not possible, the Orchestrator may roll back to the previously known working state, in other words, the previous version of the Update Manifest.


Skip concepts, give me [working examples](#installing-from-source).

## Concepts

###  A system

A combination of coupled connected devices belonging to the same physical or logical product.


For the purpose of introducing the Orchestrator, the example system will consist of the following devices:

```
+--------+     +-------+      +-------+
|Linux   |     | RTOS  |      |RTOS   |
|Gateway |     |       |      |       |
|ID: G13 |     |ID:R998|      |ID:R456|
+--------+     +-------+      +-------+
```

Linux Gateway G13:
* A device running Linux and having direct internet connectivity
* Can deliver updates to all other devices
* Has means to provide backward compatibility
    * Communicate with different RTOS versions
* Can fix (update) the RTOS
* Can fetch the  update content outside system boundaries


Two specialized Real-Time Operating System (RTOS) devices with no direct internet connectivity.
Besides running their specific function and having a rudimentary update system, there is not much they can do.

The IDs are arbitrary unique device names used to distinguish one from the other.

### Orchestrator runner

The Orchestrator is software that needs to be executed on some device within the system.
In the example case, the Linux Gateway is the obvious choice as it can update other devices within the system.


#### Components vs devices

A device can contain more than one software version or contain multiple logical components within a single hardware.
That is why, in the context of a system, we talk about components that have a software version regardless of how they map to devices.

For simplicity, the example system has a simple 1-1 mapping of components to devices.

i.e.
A Linux gateway that has OS and application versioned and updated separately would represent a device with two components.

### Declarative approach to updates


Systems consist of multiple components, all of which need to be updated by respecting certain update constraints.
Two types of constraints exist:
* end state constraints - the acceptable combinations of versions the system components can be once the update completes
* transition state constraints - the acceptable combination of versions the system components can be in while transitioning from one end state to another

In an imperative approach used by the Mender client, you would define a set of individual actions that need to take place for the system to update.
i.e.

```
Action 1 - Update the first system component from v1 to version v2
Action 2 - Update the second system component from v1 to v2
...
...
```

In the declarative approach, you specify the end state and the constraints, and the Orchestrator is in charge of defining and executing the steps.


### Constraints

#### End state constraints

An acceptable combination of versions representing a working version of a system.


| Gateway            | Rtos             | Acceptable | System version |
|--------------------|------------------|------------|----------------|
| gateway-v1.mender  | rtos-v1.mender   |   YES      |    v.1         |
| gateway-v1.mender  | rtos-v2.mender   |    NO      |    n/a         |
| gateway-v2.mender  | rtos-v1.mender   |    NO      |    n/a         |
| gateway-v2.mender  | rtos-v2.mender   |   YES      |    v.2         |


#### Transition state constraints

Because the Gateway is the more capable of the devices with the capacity to rollback on its own, it is the component that needs to update first.

An acceptable combination of versions to go through while transitioning to a valid end state of the system.


| Gateway           | Rtos            | Acceptable |
|-------------------|-----------------|------------|
| gateway-v1.mender | rtos-v1.mender  |   n/a      |
| gateway-v1.mender | rtos-v2.mender  |    NO      |
| gateway-v2.mender | rtos-v1.mender  |   YES      |
| gateway-v2.mender | rtos-v2.mender  |   n/a      |



The Manifest is an instruction to the Orchestrator on how to update a system while respecting the update constraints.

Below is an example Manifest for the given system.
The explanation of what field means is best explored through the examples below.


```
api_version: mender/v1
kind: update_manifest
version: "system-core-v1"
component_types:
  gateway:
    artifact_path: gateway-v1.mender
    update_strategy:
      order: 10
  rtos:
    artifact_path: rtos-v1.mender
    update_strategy:
      order: 20

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
```


### Update interface

An update interface is a command line application that serves as a translator between the updatable component and the Orchestrator

The update interface protocol finds inspiration in the update [modules protocol](https://github.com/mendersoftware/mender/blob/master/Documentation/update-modules-v3-file-api.md) in such that the Orchestrator acts as a state machine runner that invokes the update interface.

The update interface has an expanded set of arguments compared to an update module.

For all states, the arguments look like this:


```
./update-interface <State> <Work Dir> <Component Type> <Component ID> [<Custom arguments>]
```

`State` - the current state in the state machine as defined by the Orchestrator

`Work Dir` - the working directory for the interface. It follows the same structure and guarantees defined for the [Update modules protocol](https://github.com/mendersoftware/mender/blob/master/Documentation/update-modules-v3-file-api.md#file-api).
When using packed Artifacts and "files tree", the Artifact will be at the path `files/artifact.mender`.

`Component Type` - the type of the component instance

`Component Id` - a unique ID of the component instance

```
components:
  - component_type: gateway   # This is the component type
    id: G13                   # This is the component ID
```

`Custom arguments` - a list of customizable list of arguments as defined in the updatable component instance.

```
components:
  - component_type: gateway
    id: G13
    args:
      - arg1  # These are the custom arguments
      - arg2
      - arg3
```

### The Orchestrator bundle

For the Orchestrator to be able to update the system, the Manifest and the artifacts for the system components need to be accessible.
Those two things (Manifest + artifact) are called the Orchestrator bundle.

The Orchestrator is agnostic about the way the bundle is delivered to it.
For the default case, the Mender client (in daemon mode, communicating with the Mender server) is used to deploy the bundle to the device so that the Orchestrator can act on it.

It is also possible to just pass a Manifest file without the artifacts.
In that case, nothing is 'bundled', and the Manifest is the sole input.
The Orchestrator pulls the needed artifacts from the server on its own.

## Known limitations

When provided through a bundle, the artifacts need to be available to the Orchestrator in complete content as a .mender file.
In the worst-case scenario, this means the device needs to have enough storage to download its own compressed rootfs update first.
For comparison, in the Mender client implementation, the content is streamed into the inactive partition.


## Persistent data store

The persistent data store is the location where the Orchestrator stores the current active Manifest and artifacts it might have additionally downloaded.

The recommended setup is to have the data store of `mender-update-orchestrator` in a persistent separate partition, `/data` in the commands below, and use a symlink from `/var/lib`.


Create the directory and the symlink:

```
mkdir -p /data/mender-update-orchestrator
ln -s /data/mender-update-orchestrator /var/lib/mender-update-orchestrator
```


# Examples

All the commands expect you to be in the root directory of the Orchestrator folder (`mender-update-orchestrator*`).

This section will explain how the Orchestrator works through copy-pastable working examples.
The code can be executed on a machine that can run Python.


## Prepare the environment

Copy the pregenerated demo env:

``` bash
cp -r demo/pregenerated_env/* orch-install
```

Copy the real interface

```bash
git clone https://github.com/mendersoftware/mender-orchestrator-update-interfaces
cp -r mender-orchestrator-update-interfaces/interfaces/v1/rootfs-image  \
      $ORCH_EVAL_DIR/share/mender-update-orchestrator/update-interfaces/v1
```


## Examples

For examples to run please look the README-examples.md
That's the document that is also shared with externals during the beta stage.

