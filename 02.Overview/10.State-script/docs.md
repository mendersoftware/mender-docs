---
title: State Script
taxonomy:
    category: docs
    label: reference
---

The Mender Client has the ability to run pre- and postinstall scripts, before
and after it writes the root file system. However, Mender state scripts are more
general and useful than pre/postinstall scripts because they run between
any state transition, not just (before/after) the install state.

Common use cases are:

* Enable/disable network connectivity before and after checking for an update to reduce bandwidth.
* Migrate persistent data during a software update.
* User or application confirmation before a reboot. This is common in applications which have a UI or that provide critical functionality e.g network routers.
* Run additional sanity checks before committing to the update.

![Mender state machine diagram](mender-state-machine.png)

## State script hooks

* **Idle**: The Mender client idles and waits for the next action to handle. At this stage, no communication with the server, or downloads are in progress.
* **Sync**: At this stage the Mender client will either send or update its inventory to the server, or check if an update is available. This requires communication with the server.
* **Download**: When an update is ready at the server side Mender downloads it (streams it) to the inactive rootfs partition.
* **ArtifactInstall**: Swap the active and inactive partitions through interaction with the bootloader.
* **ArtifactReboot**: Reboots the device. Note: the _Enter_ scripts run prior to reboot; the _Leave_ scripts run after.
* **ArtifactCommit**: If the new image in the passive partition passes all the integrity checks, the Mender client will mark the update as successful and continue running from this partition. The commit makes the update persistent. A pre-script here can add custom integrity checks beyond what the Mender client provides out of the box.
* **ArtifactRollback**: If the new update fails any of the above mentioned integrity checks, the Mender client will revert the update payload. At this point, scripts in this state can help revert migrations done as a part of the update.
* **ArtifactRollbackReboot**: Some update types - most notably rootfs images - require a reboot, if any of the integrity checks fail. This state runs right before the client reboots back (i.e., rollback) into the old image partition.
* **ArtifactFailure**: if any of the States with an "Artifact" prefix fail, execute this state. Note: this state always runs after the ArtifactRollback and the ArtifactRollbackReboot states.

Most of the states also have an _Error_ transition which runs if some error
occurs while executing any script for the given state.

## Execution

State scripts run as pre- and post-scripts to every state in the Mender
state machine shown above. The state in which a given script runs is
determined by the script name and index.

Exit codes from a state script can control the execution of the Mender state
machine. Depending on the return code from the script the Mender client will:

* Move on to the next state, if successful.
* Retry this state at a later time.
* Mark the update as failed, and report the error to the server.

## Logging

The Mender client collects logs during an update. In case of a failure, these
logs are sent to the Mender server. The output from state scripts are included
in these logs. This is useful when troubleshooting intermittent update failures.

## Further reading

To learn more, have a look at the [tutorial on how to implement State
scripts](../../04.Artifacts/50.State-scripts/docs.md).
