---
title: Customize Mender
taxonomy:
    category: docs
    label: guide
---

The Mender client can be customized in any number of ways. Configure the:

- [Configuration file](#configuration-file)
- [Mender server address](#serverurl)
- [Identity](#identity)
- [Inventory](#inventory)
- [Update Modules](#update-modules)


## Configuration file

All the configuration variables available for `mender.conf` are:

---------------------------

####  ArtifactVerifyKey

Specifies the location of the public key used to verify signed updates, and also
enables signed-updates-only mode when it is set. If set the client will reject
incorrectly signed updates, or updates without a signature. See also the section
about [signing and verification](../../../artifacts/signing-and-verification).


---------------------------

####  DeviceTypeFile

> Note: deprecated in Mender 2.x

The location where to store the device_type. This must be on a persistent
partition to avoid it accidentally being changed due to an root filesystem
update. The default location is `/var/lib/mender/device_type`

---------------------------

####  InventoryPollIntervalSeconds

An integer that sets the number of seconds to wait between each inventory
update. Note that the client may occasionally post its inventory more often if
there has been recent activity on the device. See also the section about
[polling intervals](../polling-intervals).


---------------------------

####  ModuleTimeoutSeconds

An integer that specifies the number of seconds that an update module will be
allowed to run, before it is considered hanging and killed. The process will
first be sent a SIGTERM signal, and one minute later, if it has not exited,
SIGKILL. The default is 4 hours.


---------------------------

####  RetryPollIntervalSeconds

An integer that sets the number of seconds to wait between each attempt to
communicate with the server. Note that the client may attempt more often
initially to enable rapid upgrades, but will gradually fall back to this value
if the server is busy. See also the section about [polling
intervals](../polling-intervals).


---------------------------

####  RootfsPartA

The Linux device that contains root filesystem A. This is set by the build
system based on Yocto configuration and rarely needs to be modified.


---------------------------

####  RootfsPartB

The Linux device that contains root filesystem B. This is set by the build
system based on Yocto configuration and rarely needs to be modified.


---------------------------

####  ServerCertificate

The location of the public certificate of the server, if any. If this
certificate is missing, or the one presented by the server doesn't match the one
specified in this setting, the server certificate will be validated using
standard certificate trust chains.


---------------------------

####  ServerURL

The server URL which is used as the basis for API requests. This should be set
to the server that runs the Mender server services. It should include the whole
URL, including `https://` and a trailing slash.
*NOTE: This entry conflicts with [`Servers` attribute](#Servers), i.e. only one
of these entries are accepted.*


---------------------------

####  Servers

An array of json objects on the form
`[{"ServerURL": "https://mender-server.com"},
{"ServerURL": "https://mender-server2.com"}, ...]`, where `ServerURL` has the
same interpretation as the root [`ServerURL` attribute](#ServerURL).
If `Servers` entry is specified, the configuration cannot contain an additional
`ServerURL` entry in the top level of the json configuration. Upon an unserved
request (4XX/5XX-response codes) the client will attempt the next server on the
list in the given order.


---------------------------

####  StateScriptRetryIntervalSeconds

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


---------------------------

####  StateScriptRetryTimeoutSeconds

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


---------------------------

####  StateScriptTimeoutSeconds

> Default value is: `3600` (60 min)

This variables specifies the timeout value for a state-script while executing,
measuring time from start of script until a return code is delivered. This is
too prevent a script "hanging/freezing" or taking to long on specific command.
If the timer elapses the state-script will be "killed" by the Mender client and
the update marked as failure.

The default value is dimensioned to be tolerant of most scripts, but you should
set it based on the expected execution time of your scripts.

See also the section about [state scripts](../../../artifacts/state-scripts).


---------------------------

####  TenantToken

A token which identifies which tenant a device belongs to. This is only relevant
if using a multi-tenant environment such as [hosted Mender](https://hosted.mender.io?target=_blank).


---------------------------

####  UpdateLogPath

The location where deployment logs will be written. This must be on a persistent
partition to avoid it losing the logs due to an root filesystem update.


---------------------------

####  UpdatePollIntervalSeconds

An integer that sets the number of seconds to wait between each check for a new
update. Note that the client may occasionally check more often if there has been
recent activity on the device. See also the section about [polling
intervals](../polling-intervals).


--------------------------

## Identity

The Mender client obtains the identity attributes by running an executable (e.g.
binary or script) named `mender-device-identity` and parsing its standard output
as the identity. For more in depth information, have a look at the [identity
section](../../../overview/identity). The executable must be placed under the
path `/usr/share/mender/identity/mender-device-identity`. This means that it can
be user configured through overwriting the
`/usr/share/mender/identity/mender-device-identity` script.

! The device identity must remain unchanged throughout lifetime of the device. Thus, it is advised to use attributes that will not change or are unlikely to change in the future. Examples of such attributes are device/CPU serial numbers, interface MAC addresses, and in-factory burned EEPROM contents.

### Example device identity executable

As an example have a look at the example identity script below, which collects
the mac address of the wireless interface `wlp58s0`:

``` bash
#! /bin/sh

echo "mac=$(cat /sys/class/net/wlp58s0/address)"
```

<!-- AUTOVERSION: "mender/tree/%"/mender -->
This sets the device identity to `00:28:f8:5f:17:11`. For more advanced
examples, have a look at the example scripts are provided in the [support
directory in the Mender client source code
repository](https://github.com/mendersoftware/mender/tree/master/support?target=_blank).

## Inventory

Inventory is a set of simple key-value attributes that are useful know about a
device, similar to the [device identity attributes](#identity). However, the
device inventory attributes are not used to uniquely identify over time, they
are just informational. As such, they do not need to be unique for each device
like the device identity attributes. For more information have a look at the
overview of [inventory attributes](../.../../overview/inventory) section.
 
The Mender client will periodically collect inventory-related data for reporting to the
Mender server. This data is obtained by running executables located in the directory
`/usr/share/mender/inventory`. The Mender client will list and run files
that are executable and have `mender-inventory-` prefix. Other files are
ignored. Each executable may be a simple shell script or a binary.


### Example inventory attribute executable

As an example have a look at the example inventory script below, which creates a
list of all the network interfaces on the device, and reports them to the Mender
server. The contents of the file `mender-inventory-network-interfaces` is places
into `/usr/share/mender/inventory` with the following contents:

```bash
#! /bin/sh

for interface in $(ls /sys/class/net/); do
    echo "interface=${interface}"
done
```

Which reports the interfaces on the device to the Mender server at intervals
decided by the [InventoryPollIntervalSeconds](#InventoryPollIntervalSeconds)
configuration variable in `mender.conf`.


## Update Modules

An _Update Module_ is an extension to the Mender client for supporting a custom
software update, such as a package manager, container, bootloader or even
updates of microcontrollers. An Update Module can be tailored to a specific
device or environment (e.g. update a proprietary bootloader), or be more
general-purpose (e.g. install a set of `.deb` packages.).

### Example

This example creates an Update Module which copies files into the `/var/www`
directory on the device. This is done to show how simple it can be to add custom
update functionality to your device running Mender.

#### Create a Update Module script

```bash
#!/bin/bash

set -e

STATE="$1"
FILES="$2"

case "$STATE" in
    ArtifactInstall)
        cp "$FILES"/files/* /var/www
        ;;
esac
exit 0
```

See [Create a custom Update
Module](../../../install-the-mender-client/create-a-custom-update-module) for
more detailed information on how to incorporate this in an update.

