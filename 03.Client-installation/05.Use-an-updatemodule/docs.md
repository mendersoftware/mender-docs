---
title: Use an Update Module
taxonomy:
    category: docs
---

Performing Operating System updates may not be appropriate for all update scenarios.  For instance, if you only need to change a single configuration file, an Operating System update may require too much overhead, both in size of the Artifact and the time needed to install it, not to mention a reboot is required. Mender addresses this use case with
the idea of [Update Modules](../../02.Overview/15.Taxonomy/docs.md),  as described [in the overview section](../../02.Overview/01.Introduction/docs.md#application-updates).

Update Modules are executable files in the _/usr/share/mender/modules/v3_
directory on the device (note: v3 is the current version of the protocol). The Mender
client executes these files with a defined set of parameters to [perform the update](../../06.Artifact-creation/08.Create-a-custom-Update-Module/docs.md#The-state-machine-workflow).
All Update Modules originate from the artifacts of [a special payload and type](../../06.Artifact-creation/08.Create-a-custom-Update-Module/docs.md#Create-an-Artifact-with-a-payload-for-the-new-Update-Module).

When deploying updates using update modules, the Mender client will unpack the payload and then pass that to the Update Module with the correct arguments; the actual processing of the payload depends on the implementation of the update module. Mender imposes no limits on what the Update Module can or cannot do. In order to create an update module, you need to first create and install the actual code of the module, and then create an Artifact with the custom payload type.

Whether you need to install a new application onto your devices, update some files,
or perform some other operation of your choosing, the Update modules are
an option worth considering; they reduce the size of artifact, and time
of the deployment compared to Operating System updates and can extend the Mender client to handle any type of software update.


## Install a new Update Module

In order to install an Update Module to extend the capabilities of the Mender client, you simply need to place it in _/usr/share/mender/modules/v3_ and ensure that it is executable.

You can find existing Update Modules in the [Update Module category of the Mender Hub community forums](https://hub.mender.io/c/update-modules?target=_blank).
