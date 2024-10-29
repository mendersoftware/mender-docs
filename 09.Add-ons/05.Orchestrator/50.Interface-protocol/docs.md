Update modules v3 protocol
==========================

Update modules are executables that are placed in `/usr/share/mender/modules/v3`
directory, where `v3` is a reference to the version of the protocol, which is
the same as [the version of the Artifact
format](https://github.com/mendersoftware/mender-artifact/tree/master/Documentation). Mender
will look for update modules in the directory with the same version as the
version of the Artifact being processed.


States and execution flow
-------------------------

Update modules are modelled after the same execution flow as [state
scripts](https://docs.mender.io/artifacts/state-scripts), and consists of the
following states:

* `Download`
* `ArtifactInstall`
* `ArtifactReboot`
* `ArtifactVerifyReboot`
* `ArtifactCommit`
* `Cleanup`

These all execute in the order listed, given that there are no errors. There are
also some additional error states:

* `ArtifactRollback`
* `ArtifactRollbackReboot`
* `ArtifactVerifyRollbackReboot`
* `ArtifactFailure`

There are also a few calls in addition to the states that don't perform any
action, but which just gather information:

* `SupportsRollback`
* `NeedsArtifactReboot`
* `SupportsAugmentedArtifacts`
* `ListSupportedOriginalTypes`
* `PermittedAugmentedHeaders`
* `ProvidePayloadFileSizes`

`SupportsRollback` is described under [the `ArtifactRollback`
state](#artifactrollback-state), `NeedsArtifactReboot` under [the
`ArtifactReboot` state](#artifactreboot-state), and the remaining ones under
[the Signatures and augmented Artifacts
section](#signatures-and-augmented-artifacts).

### Regular states

#### `Download` state

This state executes while the Artifact is still being streamed, and allows
grabbing the file streams directly while they are downloading, instead of
storing them first. See `streams` under File API below.

**Important:** An update module must not install the update in the final
location during the `Download` state, because checksums are not verified until
after the streaming stage is over. If it must be streamed to the final location
(such as for example a partition), it should be stored in an inactive state, so
that it is not accidentally used, and then it should be activated in the
`ArtifactInstall` stage. Failure to do so can lead to the update module being
vulnerable to security attacks.

Before the `Download` state is entered the update module will be called with the
`ProvidePayloadFileSizes` query, to which the update module must answer:

* `No` - No file sizes will be provided during the `Download` state. This is the
  default, and answering nothing has the same effect.

* `Yes` - `Download` will not be called, and `DownloadWithFileSizes` will be
  called instead. The state behaves the same as the `Download` state, except
  that file sizes are provided when streaming payload files.

If `DownloadWithFileSizes` is implemented, then it is recommended to return
failure for `Download`, unless the update module is prepared to handle both
scenarios. This ensures that if the module is used with an old client which does
not provide file sizes, it will not succeed in the `Download` state by
mistake. `DownloadWithFileSizes` was first added in Mender client v4.0.

#### `ArtifactInstall` state

Executes after `Download` and should be used to install the update into its
final destination, or activate an already installed, but deactivated update.

#### `ArtifactReboot` state

Before `ArtifactReboot` is considered, the module is called with:

```bash
./update-module NeedsArtifactReboot
```

The module should print one of the valid responses:

* `No` - Mender will not run `ArtifactReboot`. This is the same as returning
  nothing, **and hence the default**.
* `Automatic` - Mender will not call the module with the `ArtifactReboot`
  argument, but will instead perform one single reboot itself. The intended use
  of this response is to group the reboots of several update modules into one
  reboot. **This is usually the best choice** for all modules that just require
  a normal reboot, but modules that reboot a peripheral device may need to use
  `Yes` instead, and implement their own method.
* `Yes` - Mender will run the update module with the `ArtifactReboot`
  argument. Use this when you want to reboot a peripheral device that's
  connected to the host. Don't use this if you want to reboot the host that
  Mender runs on; use `Automatic` instead.

**Note:** Even though the update module won't be called with the
`ArtifactReboot` argument when using `Automatic`, `ArtifactReboot` still counts as having
executed -- as far as the conditional logic is concerned.

If any update module returns `Automatic`, then a reboot of the system will be
performed after the `ArtifactReboot` state of all update modules that responded
`Yes` have been executed. This means that the reboot caused by a module that
responded `Automatic` will always come after one that responded `Yes`, even
though that may not be the original order in the Artifact.

Unless all modules responded `No` in the `NeedsArtifactReboot` query, the
`ArtifactReboot` state executes after `ArtifactInstall`. Inside this state it is
permitted to call commands that reboot the system. However, if this happens,
execution will resume in the `ArtifactVerifyReboot` state, not the
`ArtifactReboot` state. Therefore it is possible for some update modules'
`ArtifactReboot` states not to run, if an earlier update module's
`ArtifactReboot` state caused the system to reboot. To make sure this doesn't
cause problems, one of the following conditions should always be true:

* There is only one payload in the artifact
* All payloads require a simple system reboot, with no reboots of
  peripheral devices
* All payloads reboot only peripheral devices, not the host system
* If there is a mix, all payloads that want to reboot the host system respond
  `Automatic` to the `NeedsArtifactReboot` query

If all update modules in the Artifact returned `No`, then the state scripts
associated with this state, if any, will not run either.

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

Executes after `ArtifactVerifyReboot`, if `ArtifactVerifyReboot` runs at all, or
else after `ArtifactInstall`. `ArtifactCommit` must be used to remove/disable
automatic rollback mechanisms, such as for example the automatic rollback that a
bootloader might do. This essentially makes the update permanent, but it is
important to retain enough data so that an explicit `ArtifactRollback` can still
roll back the update. If additional steps are required to clean up the rollback
data, this should be done in the `Cleanup` state instead.

#### `Cleanup` state

`Cleanup` executes unconditionally at the end of all the other states,
regardless of all outcomes. `Cleanup` can be used to clean up various temporary
files that might have been used during an update, but should not be used to make
any system changes. For example, cleaning up an update that has failed,
returning it to the previous state, should rather be done in the
`ArtifactRollback` state. However, rollback data that has been kept around in
order to facilite a rollback (which never happened), should be cleaned up in
`Cleanup`.

It is not necessary to clean up files inside the official update module file
tree, since these will be cleaned up automatically, including any temporary
files.

`Cleanup` is the only additional state that executes if `Download` fails.

### Error states

#### `ArtifactRollback` state

`ArtifactRollback` is only considered in some circumstances. When a rollback is
being considered, Mender calls the update module with:

```bash
./update-module SupportsRollback
```

The exact time is not specified, but it is always after `Download` has
completed, and before either `ArtifactRollbackReboot` or `ArtifactFailure` are
executed. If the installation is successful it may not be called at all.

The module can respond with the following responses:

* `No` - Signals that the update module does not support rollback. This is the
  same as responding with nothing, and hence the default
* `Yes` - Signals that the update module supports rollback and it should be
  handled by calling `ArtifactRollback` and possibly `ArtifackRollbackReboot`
  states (if the update module requested reboot in the `NeedsArtifactReboot`
  query)

`ArtifactRollback` then executes whenever:

* the `SupportsRollback` call has returned a non-`No` response
* `ArtifactInstall` has started executing (this includes `ArtifactInstall` state
  scripts)
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
done when an Artifact install has failed. For example the update module may undo
a data migration step that was done before or during the install.


### Command line invocation

Calling the Mender client from the command line with the `install` command
will only invoke the two first states, `Download` and
`ArtifactInstall`. Additionally, `ArtifactFailure` may be executed if there is
an error.

Calling the Mender client from the command line with the `commit` command will
only invoke the two last states, `ArtifactCommit` and `Cleanup`. Additionally,
`ArtifactRollback` and `ArtifactFailure` may be executed if there is an error.

The `ArtifactReboot`, `ArtifactVerifyReboot` and `ArtifactRollbackReboot` states
are never invoked when calling the Mender client from the command line.


Relation to state scripts
-------------------------

The states used in state script naming mostly map directly to states in the
update module framework, but there are a few exceptions:

* The `Idle` and `Sync` states from state scripts are not used in update
  modules

* The `Cleanup` state in update modules is not available as a state script

* All `_Enter` and `_Leave` scripts from state scripts execute at the beginning
  and end of the same state in update modules, with one exception:
  `ArtifactReboot_Enter` scripts run before `ArtifactReboot` as expected, but
  `ArtifactReboot_Leave` scripts run after `ArtifactVerifyReboot`. No state
  scripts run between `ArtifactReboot` and `ArtifactVerifyReboot`


File API
--------

This document describes the file layout of the directory that is given to update
modules when they launch. This directory will be pre-filled with certain pieces
of information from the client, and must be used by update modules.

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

`version` is the version of the format of the Artifact that is being installed,
which is always the same as the version of the update module. This is reflected
by the location of the update module, which is always inside `v3` folder (for
version 3).

### `current_artifact_group`, `current_artifact_name` and `current_device_type`

`current_artifact_group`, `current_artifact_name` and `current_device_type`
correspond to the currently installed Artifact group, name and the device type
which is normally stored at `/var/lib/mender/device_type`. They contain pure
values, unlike the original files that contain key/value pairs.

### `header`

The `header` directory contains the verbatim headers from the `header.tar.gz`
header file of the Artifact, in addition to a few extra files. One Artifact can
contain payloads for several update modules, so the three files: `files`,
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
in the `header-info` file, under the `type` key. The rest of the list
corresponds to payloads that are being installed using different trees, and
possibly with different update modules.

`payload_type` will always be the nth from the `payloads` list, which n is the
index number which can be found in the path to the file tree.

### `tmp`

`tmp` is merely a convenience directory that the update module can use for
temporary storage. It is guaranteed to exist, to be empty, and to be cleaned up
after the update has completed (or failed). The module is not obligated to use
this directory, it can also use other, more suited locations if desirable, but
then the module must clean it up by implementing the `Cleanup` state.

### Streams tree

The streams tree only exists during the `Download` state, which is when the
download is still being streamed from the server. If the update module doesn't
want to perform its own streaming, and just wishes to save the streams to
files, it can simply do nothing in the `Download` state, and Mender will
automatically save the streams in the "files tree".

`stream-next` is a named pipe which is intended to be read in a loop, where each
time it lists the next stream available for streaming inside the `streams`
directory. The path returned will have exactly two components: which directory
it is in, and the name of the pipe which is used to stream the content. The
directory component only becomes important if using augmented Artifacts (see
below), but is nevertheless always present. For example:

```
streams/pkg-file.deb
streams/patch.diff
```

Each entry is a named pipe which can be used to stream the content from the
update. The stream is taken from the `data/nnnn.tar.gz` payload that corresponds
to the indexed subfolder being processed by Mender, just like the header.

When there are no more streams left, reading `stream-next` will result in a zero
length read. The update module must not attempt to read `stream-next` again
after receiving a zero length read, or the update procedure may hang.

**Important:** Reads must proceed in the following order: one complete read of
`stream-next` (will always be exactly one line), then read the stream it
returned, then another full read of `stream-next`, and so on. In addition, each
stream can only be read once. If this is not followed the update module may
hang.

**Important:** An update module must not install the update in the final
location during the streaming stage, because checksums are not verified until
after the streaming stage is over. If it must be streamed to the final location
(such as for example a partition), it should be stored in an inactive state, so
that it is not accidentally used, and then be activated in the
`ArtifactInstall` stage. Failure to do so can mean that the update module will
be vulnerable to security attacks.

#### File sizes

If the update module answered `Yes` to the `ProvidePayloadFileSizes` query, then
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
Mender will download the streams automatically and put them in the file tree.

The `files` directory contains the payloads from the Artifact, and is taken from
the `data/nnnn.tar.gz` payload that corresponds to the indexed subfolder being
processed by Mender, just like the header.

### Compatibility

The API may be expanded in the future with additional entries in the file and
streams trees. This may happen without increasing the version number, as long as
compatibility is maintained with the existing entries. Therefore the update
module should not assume that the entries described in the current revision of
the update module specification are the only entries.


Execution
---------

Since the API may be expanded in the future with additional calls and states,
all update modules should simply print nothing and return zero if they are
invoked with an unknown first argument.

For all the states, the update module is called once for each state that occurs,
with the working directory set to the directory where the File API resides. It
is called with exactly two arguments: The current state, and the absolute path
of the File API location. For example:

```bash
update-module ArtifactInstall /data/mender/modules/0000
```

Returning any non-zero value in the update module triggers a failure, and will
invoke the relevant failure states.


Signatures and augmented Artifacts
----------------------------------

**Warning:** Augmented Artifacts are by their very nature security sensitive,
and it is easy to open up for vulnerabilities if the consequences are not fully
understood. It is recommended not to use augmented Artifacts unless strictly
needed, and not until the reader has a solid understanding of how they work.

If signatures are being used, sometimes it may be necessary to put data into the
Artifact that isn't signed, while at the same time keeping a trusted chain. For
example, one can generate a master image, which is signed, and then generate
many binary delta images from this. Ideally one would not like to sign each and
every one of these.

Augmented Artifacts are Artifacts that can contain some parts that are signed
(the "original" part) and some parts that are not (the "augmented"
part). Obviously the unsigned content can be very security sensitive, and by
default, all content in these files will be rejected. Only consider enabling
augmented content if your update module is prepared to handle untrusted input
and still guarantee a trusted result (more about best practices below).

### Marking augmented Artifacts as supported

If you wish to accept `augment` files you need to implement this calling
interface:

```bash
./update-module SupportsAugmentedArtifacts
```

The module must respond by printing this exact string, followed by a newline:

```
YesThisModuleSupportsAugmentedArtifacts
```

and then return zero. All other output and return codes will be interpreted as
not supporting augmented Artifacts, and if any Artifact arrives that has
augmented headers or files, it will be rejected.


### Determining which types of Artifacts are supported

When using augmented Artifacts, sometimes the augmented Artifact will have a
different update `type` than the originally signed Artifact, and the `type` is
also the name of the update module. Since this makes the type untrusted, it is
important that the update module listed in the augmented header knows how to
handle an Artifact with the `type` listed in the original header.

Let's take an example, and call it `rootfs-delta-image`. This update module is
used to package binary deltas from an original rootfs image. Therefore the
update module knows how to handle Artifacts whose original `type` was
`rootfs-image`. To communicate this to Mender, the module is expected to answer
the following call:

```bash
./update-module ListSupportedOriginalTypes
```

to which it should reply with a newline separated list of types it supports. In
our example there is only one, so it responds by printing:

```
rootfs-image
```

This confirms that an Artifact whose augmented `type` is `rootfs-delta-image` is
an acceptable `type` for an original signed Artifact whose `type` was
`rootfs-image`.

As examples of negative matches, for a bogus `type` value, the update module won't
be found, and hence the update will fail. If listing a different update module,
which exists, but is unrelated, that module will not list `rootfs-image` as
being in its list of supported original types, and hence this update will also
fail. Only when there is a match between the two will the `type` field be
accepted.

Note that in our `rootfs-delta-image` example, `rootfs-image` would also need to
be prepared for this scenario, because its payload should be stored in the
augmented section so that it can be removed in an augmented update in favor of
the binary delta file.


### Filtering header fields

In general, augmented Artifacts should not be allowed to override most headers
from the original Artifact, because this may be insecure. But some headers may
need to be overrideable so that the update module can be provided with the
context it needs to install the augmented Artifact.

To permit specific header fields to be overridden, Mender calls the update
module like this:

```bash
./update-module PermittedAugmentedHeaders
```

The module is expected to return a JSON structure like this:

```
{
    "header-info": {
        "artifact_depends": {
            "device_type": [
                True
            ]
        }
    }
    "type-info": {
        "artifact_depends": {
            "rootfs_image_checksum": True
        }
    }
    "meta-data": {
        "custom_list": [
            True
        ]
    }
}
```

The root keys correspond to the files in the Artifact format header, and must be
one of `header-info`, `type-info` and `meta-data`. Since `header-info` is a
shared header between all the updates contained in one Artifact, if any
augmented headers are present here, all the update modules used in the update
must agree that the field can be overridden.

Each innermost element allows one field to be overriden. They come in these
variants:

* A boolean with a `True` value: This makes this field, contained in the same
  hierarchy, overridable by any non-list and non-object value.

* A single `True` boolean inside a list: This makes the list in that hierarchy
  overridable by any number of list elements of non-list and non-object type.

Any other type of JSON structure will be rejected and cause a failed update.


### Content of augmented Artifacts

Once all the API calls above have passed and Mender has verified that all
augmented components are valid and permitted, the update continues as usual, but
update module with augmented components will have additional elements in the
file tree:

```
-<DIRECTORY>
  |
  `----header-augment
       |
       +---header-info
       |
       +---type-info
       |
       `---meta-data
```

The `header-augment` directory functions exactly as the `header` directory, but
is taken from the `header-augment.tar.gz` file from the Artifact.

**Warning:** Be very careful with using contents from `header-augment` because
it contains unsigned data.

In addition, in the `Download` state, the file tree will contain:

```
-<DIRECTORY>
  |
  `---streams-augment
       |
       +---<STREAM-1>
       +---<STREAM-2>
       `---<STREAM-n> ...
```

where any entries in the `streams-augment` directory will be listed in the
`stream-next` from the original file API.

**Warning:** The `streams-augment` directory contains unsigned data, so make
sure the update module treats it as untrusted.

And similarly, for all the other states:

```
-<DIRECTORY>
  |
  `---files-augment
       |
       +---<FILE-1>
       +---<FILE-2>
       `---<FILE-n> ...
```

where `files-augment` contains downloaded files from the augmented section of
the Artifact, which will exist if, and only if, the streams were not consumed
during the `Download` state.

**Warning:** The `files-augment` directory contains unsigned data, so make sure
the update module treats it as untrusted.


### Best practice for augmented Artifacts

Even when using augmented Artifacts, we do want signatures to keep the updates
safe. The important property that all update modules must have, is to verify the
**end state**. In our example from above, with `rootfs-image` and
`rootfs-delta-image`, both modules need to verify that both the rootfs image,
and the result of applying the binary delta to the base, results in a valid
checksum, and the same checksum. This checksum must be stored in the original,
signed header, and **must not** be accepted in the augmented headers.

In general, augmented payloads typically mean that the payload must be
transformed into something (binary delta into full binary image, encrypted image
into decrypted image, etc), and it is typically the result of that
transformation that needs to be verified with a checksum.


Deprecated
==========

Parts of the protocol that have been deprecated and are non-functional.

Full vs partial updates
-----------------------

The `PerformsFullUpdate` call to the Update Module was present in earlier
versions of the API, but was never implemented, and has been removed.


Future possibilities
====================

Here are described some things that have not been planned in detail, but that
may be considered in the future.


Verification command
--------------------

For augmented Artifacts (which will cover delta updates), it is impossible to
verify signatures without getting help from the update module, because Mender
doesn't know how the augmented (and hence unsigned) parts can be
verified. Sometimes it is completely impossible to verify, because the result is
not available until you have a base on which to apply the delta, but for others
it may be possible.
