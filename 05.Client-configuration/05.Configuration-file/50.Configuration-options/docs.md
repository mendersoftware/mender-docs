---
title: Configuration options
taxonomy:
    category: docs
---

This sections lists all the configuration options in `mender.conf`. Some of
these options can also be modified using Yocto variables.

#### ArtifactVerifyKey

Specifies the location of the public key used to verify signed updates, and also
enables signed-updates-only mode when it is set. If set the client will reject
incorrectly signed updates, or updates without a signature. See also the section
about [signing and verification](../../../artifacts/signing-and-verification).

#### InventoryPollIntervalSeconds

An integer that sets the number of seconds to wait between each inventory
update. Note that the client may occasionally post its inventory more often if
there has been recent activity on the device. See also the section about
[polling intervals](../polling-intervals).

#### UpdatePollIntervalSeconds

An integer that sets the number of seconds to wait between each check for a new
update. Note that the client may occasionally check more often if there has been
recent activity on the device. See also the section about [polling
intervals](../polling-intervals).

#### ModuleTimeoutSeconds

An integer that specifies the number of seconds that an update module will be
allowed to run, before it is considered hanging and killed. The process will
first be sent a SIGTERM signal, and one minute later, if it has not exited,
SIGKILL. The default is 4 hours.

#### RetryPollIntervalSeconds

An integer that sets the number of seconds to wait between each attempt to
communicate with the server. Note that the client may attempt more often
initially to enable rapid upgrades, but will gradually fall back to this value
if the server is busy. See also the section about [polling
intervals](../polling-intervals).

#### RootfsPartA

The Linux device that contains root filesystem A. This is set by the build
system based on Yocto configuration and rarely needs to be modified.

#### RootfsPartB

The Linux device that contains root filesystem B. This is set by the build
system based on Yocto configuration and rarely needs to be modified.

#### Servers

An array of json objects on the form
`[{"ServerURL": "https://mender-server.com"},
{"ServerURL": "https://mender-server2.com"}, ...]`, where `ServerURL` has the
same interpretation as the root [`ServerURL` attribute](#ServerURL).
If `Servers` entry is specified, the configuration cannot contain an additional
`ServerURL` entry in the top level of the json configuration. Upon an unserved
request (4XX/5XX-response codes) the client will attempt the next server on the
list in the given order.

#### ServerURL

The server URL which is used as the basis for API requests. This should be set
to the server that runs the Mender server services. It should include the whole
URL, including `https://` and a trailing slash.
*NOTE: This entry conflicts with [`Servers` attribute](#Servers), i.e. only one
of these entries are accepted.*

#### ServerCertificate

The location of the public certificate of the server, if any. If this
certificate is missing, or the one presented by the server doesn't match the one
specified in this setting, the server certificate will be validated using
standard certificate trust chains.

#### StateScriptRetryIntervalSeconds

This variable relates to state scripts returning `21` meaning `retry-later`.
This variable specifies how long time should elapse from the `retry-later`
until the script is called again.

Example:

```
"StateScriptRetryIntervalSeconds": 30
```

Above will ensure that the state-script is called every 30 seconds as long as
it is returning `retry-later`.

Default value is: `60`

See also the section about [state scripts](../../../artifacts/state-scripts).

<!--AUTOVERSION: "mender v%"/ignore-->
*Note*: Before mender v2.0.0 release, this option used to be called
`StateScriptRetryTimeoutSeconds`.

#### StateScriptRetryTimeoutSeconds

This variable specifies how much time a state script is allowed to consume by
returning `retry-later`, meaning retry with `StateScriptRetryIntervalSeconds`
until `StateScriptRetryTimeoutSeconds` is spent.

You can not wait indefinitely but the `StateScriptRetryTimeoutSeconds` variable
is only limited by the size of an `int`.

!! It is recommend to set a sane maximum value to handle unexpected behavior, as this could potentially disable OTA capabilities on your device for long periods.

Example:

```
StateScriptRetryIntervalSeconds: 30
StateScriptRetryTimeoutSeconds: 86400
```

The above example will allow a state script to return `retry-later` for 24 hours before
aborting and marking the update as failed.

Default value is: `1800` (30 min)

See also the section about [state scripts](../../../artifacts/state-scripts).

<!--AUTOVERSION: "mender v%"/ignore-->
*Note*: Before mender v2.0.0 release, this option used to be called
`StateScriptRetryIntervalSeconds`.

#### StateScriptTimeoutSeconds

This variables specifies the timeout value for a state-script while executing,
measuring time from start of script until a return code is delivered. This is
too prevent a script "hanging/freezing" or taking to long on specific command.
If the timer elapses the state-script will be "killed" by the Mender client and
the update marked as failure.

The default value is dimensioned to be tolerant of most scripts, but you should
set it based on the expected execution time of your scripts.

Default value is: `3600` (60 min)

See also the section about [state scripts](../../../artifacts/state-scripts).

#### TenantToken

A token which identifies which tenant a device belongs to. This is only relevant
if using a multi-tenant environment such as [hosted Mender](https://hosted.mender.io?target=_blank).

#### UpdateLogPath

The location where deployment logs will be written. This must be on a persistent
partition to avoid it losing the logs due to an root filesystem update.

#### DeviceTypeFile

The location where to store the device_type. This must be on a persistent
partition to avoid it accidentally being changed due to an root filesystem
update. The default location is `/var/lib/mender/device_type`
