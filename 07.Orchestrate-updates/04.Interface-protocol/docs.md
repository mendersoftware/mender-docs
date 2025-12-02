---
title: Interface Protocol
taxonomy:
    category: docs
---


Interfaces are executables that are placed in the
`/usr/share/mender-orchestrator/interfaces/v1` directory, where `v1` is a
reference to the version of the protocol. Mender Orchestrator will look for
Interfaces in this directory.


States and execution flow
-------------------------

<!--AUTOVERSION: "mendersoftware/mender/blob/%"/mender-->
Interfaces are modelled after [Update
Modules](https://github.com/mendersoftware/mender/blob/5.0.3/Documentation/update-modules-v3-file-api.md)
from the Mender Client, and are very similar in nature.

One key difference is that the Orchestrator may execute installations for
several Components at once, by executing Interfaces either in parallel or
in series. The ordering is defined by the `order` field in the `update_strategy`
section of the Manifest. See [Ordering](#ordering) below.

Interfaces correspond to the Interface types defined in your [Topology](../03.Topology/docs.md). Each Component type in the Topology specifies which interface to use for updates.

The installation states for one single Component consist of the following
states:

* `Download`
* `ArtifactInstall`
* `ArtifactReboot`
* `ArtifactVerifyReboot`
* `ArtifactCommit`
* `Cleanup`

These are all execute in the order listed, given that there are no errors. There are
also some additional error states:

* `ArtifactRollback`
* `ArtifactRollbackReboot`
* `ArtifactVerifyRollbackReboot`
* `ArtifactFailure`

There are also a few calls in addition to the states that don't perform any
action, but which just gather information:

* `SupportsRollback`
* `NeedsArtifactReboot`
* `NeedsUnpackedArtifact`
* `ProvidePayloadFileSizes`
* `Inventory`
* `Provides`
* `Identity`

`SupportsRollback` is described under [the `ArtifactRollback`
state](#artifactrollback-state), `NeedsArtifactReboot` under [the
`ArtifactReboot` state](#artifactreboot-state), `NeedsUnpackedArtifact` and
`ProvidePayloadFileSizes` under [the `Download` state](#download-state), and the
remaining ones under their own headers.

### Ordering

In this section we define "order group" as being all Components whose `order` field
in the `update_strategy` section of the Manifest is the same.

#### Normal ordering

The ordering works like this:

1. Start with the lowest order group.
2. This order group executes the following states, in order:
    1. `Download`
    2. `ArtifactInstall`
    3. `ArtifactReboot` (if applicable)
    4. `ArtifactVerifyReboot` (if applicable)

   Each individual state may be executed in parallel for multiple different
   Components, but will wait for all Components to finish before moving on to
   the next state.
3. Then the next lowest order group is picked, and step number 2 is repeated.
4. When there are no more order groups left, we restart from the lowest one, and
   execute the state:
    1. `ArtifactCommit`

   And then loop over all the order groups, just like in step 2 and 3.
5. When all order groups are done again, we start from the lowest one again, and
   execute the state:
    1. `Cleanup`

   And then loop over all the order groups, just like in step 2 and 3.
6. Update finished with success.

#### Rollback ordering

If there is a failure at any point during steps 2 to 4, this happens:

1. Reverse the direction of order group traversal, starting at the highest one
   whose any state has run.
2. Execute the states:
    1. `ArtifactRollback`
    2. `ArtifactRollbackReboot`
    3. `ArtifactVerifyRollbackReboot`
    4. `ArtifactFailure`
3. Pick the next highest order group and then repeat step 2 for that order group.
4. When there are no more order groups, we change direction of traversal
   back to normal, start from the lowest one, and execute the state:
    1. `Cleanup`

   And then loop over all the order groups.
5. Update finished with failure.

Any failures in the rollback ordering is ignored, except for failure in
`ArtifactVerifyRollbackReboot` (see notes for [that specific
state](#artifactverifyrollbackreboot-state)).

### Regular states

#### `Download` state

This state executes while the Artifact is still being streamed, and allows
grabbing the file streams directly while they are downloading, instead of
storing them first. See `streams` under File API below.

**Important:** An Interface must not install the update in the final
location during the `Download` state, because checksums are not verified until
after the streaming stage is over. If it must be streamed to the final location
(such as for example a partition), it should be stored in an inactive state, so
that it is not accidentally used, and then it should be activated in the
`ArtifactInstall` stage. Failure to do so can lead to the Interface being
vulnerable to security attacks.

Before the `Download` state is entered the Interface will be called with the
`NeedsUnpackedArtifact` query, to which the Interface must answer:

* `No` - One single stream will be passed to Interface, containing the full
  artifact, including headers.

* `Yes` - The individual payload files inside the artifact will be streamed one
  by one. This is the default, and answering nothing has the same effect.

Answering `No` allows for passing the artifact to a downstream consumer, such as
the Mender Client, or a different host. Answering `Yes` means that the files
inside the artifact are streamed, which is usually more convenient when those
files are being installed directly.

Then, the Interface will receive the `ProvidePayloadFileSizes` query, to which
it must answer:

* `No` - No file sizes will be provided during the `Download` state. This is the
  default, and answering nothing has the same effect.

* `Yes` - `Download` will not be called, and `DownloadWithFileSizes` will be
  called instead. The state behaves the same as the `Download` state, except
  that file sizes are provided when streaming payload files.

#### `ArtifactInstall` state

Executes after `Download` and should be used to install the update into its
final destination, or activate an already installed, but deactivated update.

#### `ArtifactReboot` state

Before `ArtifactReboot` is considered, the Interface is called with the
`NeedsArtifactReboot` query:

The Interface should print one of the valid responses:

* `No` - Mender will not run `ArtifactReboot`. This is the same as returning
  nothing, **and hence the default**.
* `Automatic` - Mender will not call the Interface with the `ArtifactReboot`
  argument, but will instead perform one single reboot itself. The intended use
  of this response is to group the reboots of several Interfaces into one
  reboot. **This is usually the best choice** for all Interfaces that just
  require a normal reboot, but Interfaces that reboot a peripheral device may
  need to use `Yes` instead, and implement their own method.
* `Yes` - Mender will run the Interface with the `ArtifactReboot`
  argument. Use this when you want to reboot a peripheral device that's
  connected to the host. Don't use this if you want to reboot the host that
  Mender runs on; use `Automatic` instead.

**Note:** Even though the Interface won't be called with the
`ArtifactReboot` argument when using `Automatic`, `ArtifactReboot` still counts
as having executed -- as far as the conditional logic is concerned.

If any Interface returns `Automatic`, then a reboot of the device will be
performed after the `ArtifactReboot` state of all Interfaces in the same
"order group" that responded `Yes` have been executed. "Order group" means all
Interfaces for components that are using the same `order` field in the
manifest.

**Note:** The `NeedsArtifactReboot` query is guaranteed to be carried out after
`ArtifactInstall` has been executed. In other words it is possible to, for
example, query package managers whether a reboot is required after it has
installed a package.

#### `ArtifactVerifyReboot` state

Executes after `ArtifactReboot` has run, if it runs at all.

`ArtifactVerifyReboot` should be used to verify that the reboot has
been performed correctly, and that it was not rolled back by an external
component, such as a watch dog or the boot loader. A common use of the script is
to make sure the correct partition has been booted.

#### `ArtifactCommit` state

Executes after all components have finished `ArtifactVerifyReboot`, if
`ArtifactVerifyReboot` runs at all, or else after
`ArtifactInstall`. `ArtifactCommit` must be used to remove/disable automatic
rollback mechanisms, such as for example the automatic rollback that a
bootloader might do. This essentially makes the update permanent, but it is
important to retain enough data so that an explicit `ArtifactRollback` can still
roll back the update. If additional steps are required to clean up the rollback
data, this should be done in the `Cleanup` state instead.

#### `Cleanup` state

`Cleanup` executes unconditionally at the end of all the other states,
regardless of all outcomes. `Cleanup` can be used to clean up various temporary
files that might have been used during an update, but should not be used to make
any changes. For example, cleaning up an update that has failed,
returning it to the previous state, should rather be done in the
`ArtifactRollback` state. However, rollback data that has been kept around in
order to facilite a rollback (which never happened), should be cleaned up in
`Cleanup`.

It is not necessary to clean up files inside the official update Interface file
tree, since these will be cleaned up automatically, including any temporary
files.

`Cleanup` is the only additional state that executes if `Download` fails.

### Error states

#### `ArtifactRollback` state

`ArtifactRollback` is only considered in some circumstances. When a rollback is
being considered, Mender Orchestrator calls the Interface with the
`SupportsRollback` query.

The exact time is not specified, but it is always after `Download` has
completed, and before either `ArtifactRollbackReboot` or `ArtifactFailure` are
executed. If the installation is successful it may not be called at all.

The Interface can respond with the following responses:

* `No` - Signals that the Interface does not support rollback. This is the
  same as responding with nothing, and hence the default
* `Yes` - Signals that the Interface supports rollback and it should be
  handled by calling `ArtifactRollback` and possibly `ArtifackRollbackReboot`
  states (if the Interface requested reboot in the `NeedsArtifactReboot`
  query)

`ArtifactRollback` then executes whenever:

* the `SupportsRollback` call has returned a non-`No` response
* `ArtifactInstall` has started executing
* Any of these states fail or experience a spontaneous reboot:
  * `ArtifactInstall`
  * `ArtifactReboot`
  * `ArtifactVerifyReboot`
  * `ArtifactCommit`

It should be used to roll back to the previously installed software, either by
restoring a backup or deactivating the new software so that the old software
becomes active again.

#### `ArtifactRollbackReboot` state

`ArtifactRollbackReboot` executes whenever:

* `NeedsArtifactReboot` query has returned `Yes`
* `ArtifactRollback` has executed

As an alternative to invoking `ArtifactRollbackReboot`, Mender instead calls the
`reboot` command if:

* `NeedsArtifactReboot` query has returned `Automatic`
* Mender has called `reboot` command instead of calling `ArtifactReboot`
* `ArtifactRollback` has executed

The `reboot` command execution follows the same mechanics as those described in
the `ArtifactReboot` state.

Additionally, `ArtifactRollbackReboot` (or the `reboot` command) will execute if
the next state, `ArtifactVerifyRollbackReboot` has executed and returned
failure. This will only happen a limited number of times, to avoid endless
reboot loops.

#### `ArtifactVerifyRollbackReboot` state

`ArtifactVerifyRollbackReboot` executes whenever:

* `ArtifactRollbackReboot` has executed

This state should be used to verify that the system or peripheral was
successfully rebooted back into its old state. Note that if this returns
failure, the reboot will be attempted again using the `ArtifactRollbackReboot`
state. Mender will only try a limited number of times before moving on to the
`ArtifactFailure` state, but **if `ArtifactVerifyRollbackReboot` keeps returning
failure the system may be left in a permanently inconsistent state**.

#### `ArtifactFailure` state

`ArtifactFailure` executes whenever:

* Either of `ArtifactInstall`, `ArtifactReboot`, `ArtifactVerifyReboot` or
  `ArtifactCommit` has failed or experiences a spontaneous reboot
* Executes after `ArtifactRollback` and `ArtifactRollbackReboot`, if they
  execute at all

`ArtifactFailure` can be used to perform any reverts or cleanups that need to be
done when an Artifact install has failed. For example the Interface may
undo a data migration step that was done before or during the install.

### Query states

#### `Inventory` query

The `Inventory` query is not called as part of an installation, but as a means to
gather information about Components. When called, it is expected to print the
inventory data of the relevant Component type and ID. See
[Execution](#execution) below to find out how the type and ID are obtained.

The output format is the same as for [Mender inventory
scripts](../../03.Client-installation/04.Inventory/docs.md). This consists of
"key=value" pairs, with no spaces, separated by newlines. Printing list data is
supported by using the same key multiple times.

#### `Provides` query

The `Provides` query is not called as part of an installation, but as a means to
gather information about Components. When called, it is expected to print the
Provides data (also called "software versions") of the relevant Component type
and ID. See [Software
versioning](../../08.Artifact-creation/11.Software-versioning/docs.md) for
more information about what Provides values are, and see [Execution](#execution)
below to find out how the type and ID are obtained.

The output format is the same as the output from the Mender Client
`show-provides` command, which consists of "key=value" pairs, with no spaces,
separated by newlines. Unlike in the `Inventory` query, list data is not
permitted in Provides data.

#### `Identity` query

The `Identity` query is called during Component initialization to determine the unique Component ID for this specific Component instance. This is called before any update operations begin and is used to establish the Component's identity dynamically.

The output format should be a single line containing:
```
id=<component_id>
```

Where `<component_id>` is a unique identifier for this Component instance. For example:
```
id=R123
```

**Note:** The Component ID returned by `Identity` becomes the unique identifier for this Component and is used in all subsequent Interface calls as well as in the work directory structure.


File API
--------

This document describes the file layout of the directory that is given to update
Interfaces when they launch. This directory will be pre-filled with certain
pieces of information from the orchestrator, and must be used by update
Interfaces. Each Component from the Manifest gets its own directory, and update
Interfaces are executed independently from each other, though they can execute
at the same time if their `order` field in the Manifest is the same.

```
-<DIRECTORY>
  |
  +---version
  |
  +---current_artifact_group
  |
  +---current_artifact_name
  |
  +---current_device_type
  |
  +---header
  |    |
  |    +---artifact_group
  |    |
  |    +---artifact_name
  |    |
  |    +---payload_type
  |    |
  |    +---header-info
  |    |
  |    +---type-info
  |    |
  |    `---meta-data
  |
  `---tmp
```

In addition it may contain one of these two trees, depending on context. The
"streams tree":

```
-<DIRECTORY>
  |
  +---stream-next
  |
  `---streams
       |
       +---<STREAM-1>
       +---<STREAM-2>
       `---<STREAM-n> ...
```

or the "files tree":

```
-<DIRECTORY>
  |
  `---files
       |
       +---<FILE-1>
       +---<FILE-2>
       `---<FILE-n> ...
```

### `versions`

`version` is the version of Interface protocol (this document). This is
reflected by the location of the Interface, which is always inside `v1`
folder (for version 1).

### `current_artifact_group`, `current_artifact_name` and `current_device_type`

`current_artifact_group`, `current_artifact_name` and `current_device_type`
correspond to the currently provided Artifact group, name and device type, which
is obtained using the `Provides` query to the Interface. They contain
pure values, unlike the original files that contain key/value pairs.

### `header`

The `header` directory contains the verbatim headers from the `header.tar.gz`
header file of the Artifact, in addition to a few extra files. One Artifact can
contain payloads for several Interfaces, so the three files: `files`,
`type-info` and `meta-data` are taken from the indexed subfolder currently being
processed by Mender.

#### `artifact_group` and `artifact_name`

`artifact_group` and `artifact_name` contain the group and name of the Artifact
that is being installed, respectively. This is the same information as that
which is available inside `header/header-info`, under the `artifact_provides ->
`artifact_group` and `artifact_name` keys, and is merely for convenience.

#### `payload_type`

`payload_type` contains the type of the payload which is current being installed
using this file tree. It is always one of the elements from the `payloads` list
in the `header-info` file, under the `type` key. It is also the name of the
currently executing Interface.

`payload_type` will always be the nth from the `payloads` list, which n is the
index number which can be found in the path to the file tree.

### `tmp`

`tmp` is merely a convenience directory that the Interface can use for
temporary storage. It is guaranteed to exist, to be empty, and to be cleaned up
after the update has completed (or failed). The Interface is not obligated to
use this directory, it can also use other, more suited locations if desirable,
but then the Interface must clean it up by implementing the `Cleanup` state.

### Streams tree

The streams tree only exists during the `Download` state, which is when the
download is still being streamed from the Mender Server. If the Interface
doesn't want to perform its own streaming, and just wishes to save the streams
to files, it can simply do nothing in the `Download` state, and Mender Client will
automatically save the streams in the "files tree".

`stream-next` is a named pipe which is intended to be read in a loop, where each
time it lists the next stream available for streaming inside the `streams`
directory. The path returned will have exactly two components: which directory
it is in, and the name of the pipe which is used to stream the content. For
example:

```
streams/pkg-file.deb
streams/patch.diff
```

Each entry is a named pipe which can be used to stream the content from the
update. The stream is taken from the `data/nnnn.tar.gz` payload that corresponds
to the indexed subfolder being processed by Mender, just like the header.

When there are no more streams left, reading `stream-next` will result in a zero
length read. The Interface must not attempt to read `stream-next` again
after receiving a zero length read, or the update procedure may hang.

**Important:** Reads must proceed in the following order: one complete read of
`stream-next` (will always be exactly one line), then read the stream it
returned, then another full read of `stream-next`, and so on. In addition, each
stream can only be read once. If this is not followed the Interface may
hang.

**Important:** An Interface must not install the update in the final
location during the streaming stage, because checksums are not verified until
after the streaming stage is over. If it must be streamed to the final location
(such as for example a partition), it should be stored in an inactive state, so
that it is not accidentally used, and then be activated in the `ArtifactInstall`
stage. Failure to do so can mean that the Interface will be vulnerable to
security attacks.

#### File sizes

If the Interface answered `Yes` to the `ProvidePayloadFileSizes` query, then
the streaming process is slightly different. First of all, the `Download` state
is not called, and `DownloadWithFileSizes` is called instead. Second, each line
obtained from `stream-next` will contain the file size as well, separated from
the file name by a space. For example:

```
streams/pkg-file.deb 45853
streams/patch.diff 201
```

Everything else remains the same as with the regular `Download` state.

### File tree

The file tree only exists in the `ArtifactInstall` and later states, and only
if the streams were **not** consumed during the `Download` state. In this case
the Orchestrator will download the streams automatically and put them in the file tree.

The `files` directory contains the payloads from the Artifact, and is taken from
the `data/nnnn.tar.gz` payload that corresponds to the indexed subfolder being
processed by the Orchestrator, just like the header.

### Compatibility

The API may be expanded in the future with additional entries in the file and
streams trees. This may happen without increasing the version number, as long as
compatibility is maintained with the existing entries. Therefore the update
Interface should not assume that the entries described in the current revision of
the Interface specification are the only entries.


Execution
---------

Since the API may be expanded in the future with additional calls and states,
all Interfaces should simply print nothing and return zero if they are
invoked with an unknown first argument.

For all the states, the Interface is called once for each state that
occurs, with the working directory set to the directory where the File API
resides. It is called with at least three arguments, plus any number of optional
arguments following that:

1. the current state
2. the absolute path of the File API location
3. the Component type (as defined in the Topology)
4. *optional*: any other arguments specified in the `Interface_args` list in the Topology

**Note:** The Component ID is NOT passed as an argument to the Interface. Instead, it is determined dynamically by the Orchestrator calling the `Identity` query and using the returned value.

For example:

```bash
# Normal update state call
update-module \
    ArtifactInstall \
    /data/mender/modules/0000 \
    component_type
```

Returning any non-zero value in the Interface triggers a failure, and
will invoke the relevant failure states.
