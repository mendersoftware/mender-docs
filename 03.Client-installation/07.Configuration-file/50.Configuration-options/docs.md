---
title: Configuration options
taxonomy:
    category: docs
---

This sections lists all the configuration options in `mender.conf`.

#### ArtifactVerifyKey

When set, the Mender client verifies the following:

* All Artifact installs contain  a signature. If a signature is not provided, then the client rejects the update.
* The provided public key verifies the signature of the update.

See also the section about [signing and
verification](../../../06.Artifact-creation/07.Sign-and-verify/docs.md).

#### BootUtilitiesGetNextActivePart

This setting controls which command is
used to get information about the
currently active rootfs, when using `rootfs-image` Artifacts. The tool must
follow the same conventions as the `u-boot-fw-utils`, `libubootenv` and
`grub-mender-grubenv` user space tools. This includes command line options as
well as variables it is expected to return: `bootcount`, `mender_boot_part`,
`mender_boot_part_hex` and `upgrade_available`. If this value is not set, it
defaults to trying `grub-mender-grubenv-print` first, followed by `fw_printenv`
if the former is not found.

Introduced in Mender client 3.1.

#### BootUtilitiesSetActivePart

This setting controls which command is
used to set the active rootfs partition,
when using `rootfs-image` Artifacts. The tool must follow the same conventions
as the `u-boot-fw-utils`, `libubootenv` and `grub-mender-grubenv` user space
tools. This includes command line options as well as variables it is expected to
honor: `bootcount`, `mender_boot_part`, `mender_boot_part_hex` and
`upgrade_available`. If this value is not set, it defaults to trying
`grub-mender-grubenv-set` first, followed by `fw_setenv` if the former is not
found.

Introduced in Mender client 3.1.

#### Connectivity

Allows you to configure additional connection-related settings.

##### DisableKeepAlive

If set to true, disables the connections keep alive in general. All the HTTP transactions
will cause a new connection to be created.

##### IdleConnTimeoutSeconds

Specifies the time after which a connection is terminated. The larger it is,
the longer keep alive traffic will happen, as the client will maintain
the connection.

Introduced in Mender client 3.3.

Example:

```
    "Connectivity": {
        "DisableKeepAlive": false,
        "IdleConnTimeoutSeconds": 30
    },
```
The above will cause the client keep a connection and to terminate it after 30 seconds.
During the 30 seconds each request will reuse an existing connection, which should
in principle reduce the bandwidth, as we avoid a TLS negotiation and connection establishing
every time the client has to contact the server.

#### HttpsClient

Allows you to configure the certificate, private key and, SSL Engine id to use
during the SSL handshake. If you provide the certificate and private key
as locally accessible files you don't have to specify
<!--AUTOVERSION: "docs/man%"/ignore-->
[SSLEngine](https://www.openssl.org/docs/man1.1.1/man1/engine.html).
If you want to use a Hardware Security Module (HSM) you can provide the private
key as a [PKCS#11 URI](https://tools.ietf.org/html/rfc7512) and in that case
you must also specify the `SSLEngine`. The client will use this key for signing
the authorization requests unless you provide `Security.AuthPrivateKey`
(see below).

##### Certificate

A path to the file in pem format holding the certificate.

##### Key

Either a valid PKCS#11 URI or a path to a file holding the private key.

##### SSLEngine

Example (with HSM, using Nitrokey HSM):

```
    "HttpsClient": {
        "Certificate": "/certs/cert.pem",
        "Key": "pkcs11:model=PKCS%2315%20emulated;manufacturer=www.CardContact.de;serial=SOMESERIAL;token=UserPIN%20%28SmartCard-HSM%29;id=%10;object=Private%20Key;pin-value=1234;type=private",
        "SSLEngine": "pkcs11"
    },
```
where "pkcs11:" means that Mender should load the key not from the file but using PKCS#11 URI.
The above can have the following example OpenSSL configuration present:
You can accompany the above with the following OpenSSL configuration:

```
[openssl_init]
engines=engine_section

[engine_section]
pkcs11 = pkcs11_section

[pkcs11_section]
engine_id = pkcs11
MODULE_PATH = /usr/lib/arm-linux-gnueabihf/opensc-pkcs11.so
init = 0
```

Example (plain files):

```
    "HttpsClient": {
        "Certificate": "/certs/cert.pem",
        "Key": "/keys/private/key.pem"
    },
```
where "/certs/cert.pem" holds the certificate and "/keys/private/key.pem" the private key.

#### InventoryPollIntervalSeconds

An integer that sets the number of seconds to wait between each inventory
update. Note that the client may occasionally post its inventory more often if
there has been recent activity on the device. See also the section about
[polling intervals](../01.Polling-intervals/docs.md).

#### UpdatePollIntervalSeconds

An integer that sets the number of seconds to wait between each check for a new
update. Note that the client may occasionally check more often if there has been
recent activity on the device. See also the section about [polling
intervals](../01.Polling-intervals/docs.md).

#### ModuleTimeoutSeconds

An integer that specifies the number of seconds that an update module is allowed
to run, before it is considered hung and killed. The process will first be sent
a SIGTERM signal, and one minute later, if it has not exited, a SIGKILL signal
is sent. The default is 4 hours.

#### RetryPollCount

The maximum number of tries that the Mender client performs when contacting
the Mender Server.

If the setting is zero (the default), the maximum number of retries is `3 * ceil(log2(RetryPollIntervalSeconds) + 1)`.

Introduced in Mender client 3.3.

#### RetryPollIntervalSeconds

An integer that sets the number of seconds to wait between each attempt to
communicate with the server. Note that the client may attempt more often
initially to enable rapid upgrades, but will gradually fall back to this value
if the server is busy. See also the section about [polling
intervals](../01.Polling-intervals/docs.md).

As of Mender client 3.3 this one also applies to inventory updates.

#### RootfsPartA

The Linux device that contains root filesystem A. The build system (ie Yocto or
mender-convert) sets this variable so it is rarely modified manually.

#### RootfsPartB

The Linux device that contains root filesystem B. The build system (ie Yocto or
mender-convert) sets this variable, so it is rarely modified manually.

#### Security

Allows you to specify the basic security options, `AuthPrivateKey`
and `SSLEngine`, which you can use for signing of authentication requests.
If you specify both `Security.AuthPrivateKey` and `HttpsClient.Key`
the former takes precedence.

##### AuthPrivateKey

A path to the file in pem format holding the private key, or a
[PKCS#11 URI](https://tools.ietf.org/html/rfc7512).

##### SSLEngine

<!--AUTOVERSION: "docs/man%"/ignore-->
The [SSLEngine](https://www.openssl.org/docs/man1.1.1/man1/engine.html) to use.

#### Servers

An array of json objects on the form `[{"ServerURL":
"https://mender-server.com"}, {"ServerURL": "https://mender-server2.com"},
...]`, where `ServerURL` has the same interpretation as the root [`ServerURL`
attribute](#ServerURL). If `Servers` entry is set, the configuration cannot
contain an additional `ServerURL` entry in the top level of the json
configuration. Upon an unserved request (4XX/5XX-response codes) the client
attempts the next server on the list in the given order.

#### ServerURL

The server URL is the basis for API requests. This needs to point to the
server which runs the Mender server services. It should include the whole URL,
including `https://` and a trailing slash. *NOTE: This entry conflicts with
[`Servers` attribute](#Servers), i.e. the server only accepts one of these entries.*

#### ServerCertificate

The location of the public certificate of the server, if any. If this
certificate is missing, or the one presented by the server does not match the
one specified in this setting, the server certificate is validated using
standard certificate trust chains.

#### StateScriptRetryIntervalSeconds

This variable relates to state scripts returning `21` - meaning `retry-later`.
This variable specifies how long time should elapse from the `retry-later` until
the script is rerun.

Example:

```
"StateScriptRetryIntervalSeconds": 30
```

If set, the client retries the state-script every 30 seconds as long as it keeps returning `retry-later`.

Default value is: `60`

See also the section about [state scripts](../../../06.Artifact-creation/04.State-scripts/docs.md).

<!--AUTOVERSION: "mender v%"/ignore-->
*Note*: Before mender v2.0.0 release, this option used to be called
`StateScriptRetryTimeoutSeconds`.

#### StateScriptRetryTimeoutSeconds

This variable specifies how much time a state script can consume by returning
`retry-later`, meaning retry with `StateScriptRetryIntervalSeconds` for the
period of `StateScriptRetryTimeoutSeconds`.

You can not wait indefinitely but the `StateScriptRetryTimeoutSeconds` variable
is only limited by the size of an `int`.

!! It is recommended to set a sane maximum value to handle unexpected behavior, as this could potentially disable OTA capabilities on your device for long periods of time.

Example:

```
StateScriptRetryIntervalSeconds: 30
StateScriptRetryTimeoutSeconds: 86400
```

The above example will allow a state script to return `retry-later` for 24 hours before
aborting and marking the update as failed.

Default value is: `1800` (30 min)

See also the section about [state scripts](../../../06.Artifact-creation/04.State-scripts/docs.md).

<!--AUTOVERSION: "mender v%"/ignore-->
*Note*: Before mender v2.0.0 release, this option used to be called
`StateScriptRetryIntervalSeconds`.

#### StateScriptTimeoutSeconds

This variables specifies the timeout value for a state-script while executing,
measuring time from start of script until is returns an exit code. This is to
prevent a script "hanging/freezing" or taking too long executing a specific
command. If the timer elapses the state-script will be "killed" by the Mender
client and the update marked as failure.

The default value needs to be tolerant of most scripts, hence you should base it
on the expected execution time of your scripts.

Default value is: `3600` (60 min)

See also the section about [state scripts](../../../06.Artifact-creation/04.State-scripts/docs.md).

#### TenantToken

A token which identifies which tenant a device belongs to. This is only relevant
if using a multi-tenant environment such as [hosted Mender](https://hosted.mender.io?target=_blank).

#### UpdateLogPath

The location where to store the deployment (update) log. This must be on a
persistent partition to avoid losing the logs due to a root filesystem update.

#### DeviceTypeFile

The location where to store the device_type. This must be on a persistent
partition to avoid it accidentally changing due to a root filesystem update. The
default location is `/var/lib/mender/device_type`

#### UpdateControlMapExpirationTimeSeconds

The expire time in seconds for an update control map. The value provides the
time window for an application using the update control _dbus API_ to refresh
the update control map before it enters the expired state. _Defaults to
2*UpdatePollIntervalSeconds_
<!-- TODO: Insert links to dbus api specs for update control -->

#### UpdateControlMapBootExpirationTimeSeconds

The maximum expire time in seconds after startup for an update control map. The
value provides an upper bound on the update control map [expire
time](#UpdateControlMapExpirationTimeSeconds) after system startup. _Defaults to 600
(10 minutes)_
