---
title: State scripts
taxonomy:
    category: docs
---

The Mender client has the ability to run pre- and postinstall scripts, before and after it writes the root file system. The most common use case is to do application data migration, for example if application data like a user profile is stored in an SQLite database and a new column needs to be added before starting the new version of the application.
There are a wide variety of other use cases that are covered by state scripts. State scripts are more general and useful than pre/postinstall scripts because they can be run between any state transition, not just (before/after) the install state. For more use cases see [example use cases](#example-use-cases).


## The nine states

Starting with the Mender client version 1.2, support is available for scripts to be run before and after nine different states:

* **Idle**: this is a state where no communication with the server is needed nor is there any update in progress
* **Sync**: communication with the server is needed (currently while checking if there is an update for the given device and when inventory data is sent to server)
* **Download**: there is an update for the given device and a new image is downloaded and written (i.e. streamed) to the passive rootfs partition
* **ArtifactInstall**: swapping active and inactive partitions after the download and writing is completed
* **ArtifactReboot**: after the update is installed we need to reboot the device to apply the new image. The Enter actions run before the reboot; the Leave actions run after.
* **ArtifactCommit**: device is up and running after rebooting with the new image, the commit takes care of making the update persistent
* **ArtifactRollback**: if the new update is broken and we need to go back to the previous one
* **ArtifactRollbackReboot**: if we need to reboot the device after performing rollback
* **ArtifactFailure**: if any of the "Artifact" states are failing, the device enters and executes this state. This state always runs after the ArtifactRollback and ArtifactRollbackReboot states.

State scripts can either be run as we transition into a state; "Enter", or out from a state "Leave". Most of the states have also "Error" action which is run when some error occurs while executing any action inside given state (including execution of Enter and Leave scripts).


## Root file system and artifact scripts

There are two types of the state scripts: root file system and artifact. The root file systems scripts are stored as a part of the current root file system. The default location
for those scripts is `/etc/mender/scripts`.
The artifact scripts are part of the artifact and are delivered to the client inside the artifact. All the artifact scripts are prefixed with `Artifact`.

The reason for having both root file system and artifact scripts is related to the fact that some scripts must run before the client downloads the artifact and as such can not be delivered with the artifact. Those scripts are Idle, Sync and Download. Therefore it is important to remember that when deploying a new update, all scripts will be run from old update until ArtifactInstall, at which point the scripts from the new artifact will take over.


## Running scripts

State scripts are run by the Mender client after reaching a given state. Before entering the new state the Enter scripts are run. After all the actions belonging to the given state are executed, the Leave scripts are run. For most of the states, if some error occurs while executing either an Enter or a Leave script, or some action inside the state (like installing a new artifact which is broken and therefore installation is failing) the corresponding Error scripts are executed.
The exceptions are Idle, Sync, ArtifactRollback, ArtifactRollbackReboot, ArtifactFailure and Leave script for ArtifactCommit. The reason for ignoring errors and not calling Error scripts is either that the state is already an error state, such as for example ArtifactRollback, or there is no meaningful action that can be taken in the event of an error, such as for Idle or ArtifactCommit.Leave (it is too late to roll back after a commit).

There can be more than one script for a given state. Each script contains an ordering number as a part of the name, and if more than one script for a given state exists, scripts are executed in accessing order.

**There are no arguments passed to the scripts.**
**If a script returns 0 Mender proceeds, but if it returns 1 the update is aborted and rolled back. All other return codes are reserved for future use by Mender and should not be used.**

 

## Example use cases

In addition to the standard pre/postinstall use cases, there are a number of interesting use cases that are enabled by this more general state scripting support:

Enable network: In order to save power and bandwidth, network connectivity may not be enabled by default. However, state scripts in Sync_Enter and Download_Enter can enable network connectivity (and it can optionally be disabled in corresponding Leave scripts).
Custom sanity checks: Mender already automatically rolls back an update if it can not reach the Mender Server after the update is applied, in order to ensure another update can be deployed. Scripts in ArtifactCommit_Enter can do additional sanity checks to make sure that the device and applications are working as expected. For example, is the UI application running and responding?
Wait for user confirmation: A script may integrate with a UI framework to show a pop-up to the end user of a display-connected device and only return 0 once the user selects "Update".


## Naming convention

The scripts follow a naming convention to determine when they should be run:

```
<STATE_NAME>_<ACTION>_<ORDERING_NUMBER>_<OPTIONAL_DESCRIPTION>
```

For example, Download_Enter_05_wifi-driver and Download_Enter_10_ask-user would both run before the Download state, and the wifi-driver script would run before the ask-user script.


## Embedding state scripts inside artifact or image

The easiest way to have Mender run the state scripts is to create a new OpenEmbedded recipe that inherits mender-state-scripts and copies them into place in do_compile, using the [${MENDER_STATE_SCRIPTS_DIR}](../../artifacts/variables#mender_state_scripts_dir) variable.

You can take a look at the [example-state-scripts](https://github.com/mendersoftware/meta-mender/tree/master/meta-mender-demo/recipes-mender/example-state-scripts) recipe to get started.

## Execution paths

A typical order of script execution for various scenarios might look like the below diagrams:

### Normal execution without errors
```
(device boot) -> [Idle_Enter] Idle [Idle_Leave] -> [Sync_Enter] Sync [Sync_Leave] -> [Download_Enter] Download [Download_Leave] -> [ArtifactInstall_Enter] ArtifactInstall [ArtifactInstall_Leave] -> [ArtifactReboot_Enter] ArtifactReboot -> (device reboot) -> [ArtifactReboot_Leave] -> [ArtifactCommit_Enter] ArtifactCommit [ArtifactCommit_Leave] -> [Idle_Enter] Idle [Idle_Leave] -> ...
```
Please note that ArtifactReboot Leave script is run after device reboots.


### Error while downloading the artifact
```
(device boot) -> [Idle_Enter] Idle [Idle_Leave] -> [Sync_Enter] Sync [Sync_Leave] -> [Download_Enter] Download -> (error while downloading) -> [Download_Error] -> [Idle_Enter] Idle [Idle_Leave] -> ...
```
Please note no Download Leave script is run after downloading fails. Instead the Download Error script is called.

### Error while installing new artifact
```
(device boot) -> [Idle_Enter] Idle [Idle_Leave] -> [Sync_Enter] Sync [Sync_Leave] -> [Download_Enter] Download [Download_Leave] -> [ArtifactInstall_Enter] ArtifactInstall -> (error while installing) -> [ArtifactInstall_Error] ->  [ArtifactFailure_Enter] ArtifactFailure [ArtifactFailure_Leave] -> [Idle_Enter] Idle [Idle_Leave] -> ...
```
In case any of the "Artifact" scripts fails, an additional ArtifactFailure state is entered and the corresponding Enter and Leave scripts are run. Please also note that there are no ArtifactFailure Error scripts and if any error happens while executing actions inside the ArtifactFailure state, ArtifactFailure Leave scripts will run and an appropriate error path will be executed.

### Error while committing an update
```
(device boot) -> [Idle_Enter] Idle [Idle_Leave] -> [Sync_Enter] Sync [Sync_Leave] -> [Download_Enter] Download [Download_Leave] -> [ArtifactInstall_Enter] ArtifactInstall [ArtifactInstall_Leave] -> [ArtifactReboot_Enter] ArtifactReboot -> (device reboot) -> [ArtifactReboot_Leave] -> [ArtifactCommit_Enter] ArtifactCommit -> (error while commiting) -> [ArtifactCommit_Error] -> [ArtifactFailure_Enter] ArtifactFailure [ArtifactFailure_Leave] -> [ArtifactRollback_Enter] ArtifactRollback [ArtifactRollback_Leave] -> [ArtifactRollbackReboot_Enter] ArtifactRollbackReboot -> (device reboot) -> [ArtifactRollbackReboot_Leave] -> [Idle_Enter] Idle [Idle_Leave] -> ...
```
Please note that similar to the ArtifactReboot, ArtifactRollbackReboot Leave script is called after device reboots.


