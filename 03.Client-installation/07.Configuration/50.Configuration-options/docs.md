---
title: Configuration options
taxonomy:
    category: docs
---

This section lists all the available configuration options in the `mender.conf` file.

#### ArtifactVerifyKey

There are two options for specifying verification keys:
* `ArtifactVerifyKey` is a single path to a key.
* `ArtifactVerifyKeys` is a list of paths to keys. When multiple keys are
    specified, the keys will be
    tried in order, and the first key that verifies
    an artifact signature will be
    used. This is useful for key rotation or
    signing different types of artifacts.

Only one of `ArtifactVerifyKey` or `ArtifactVerifyKeys` may be specified.

When set, the Mender Client verifies the following:

* All Artifact installs contain a signature. If a signature is not provided,
    then the client rejects the update.
* The provided public key verifies the signature of the update.

See also the section about [signing and
verification](../../../08.Artifact-creation/09.Sign-and-verify/docs.md).

#### BootUtilitiesGetNextActivePart

This option is **deprecated** and does not exist anymore in Mender Client v4.0 and later. For
earlier versions, please see [documentation for Mender
3.6](https://docs.mender.io/3.6/client-installation/configuration-file/configuration-options#bootutilitiesgetnextactivepart)
or older.

#### BootUtilitiesSetActivePart

This option is **deprecated** and does not exist anymore in Mender Client v4.0 and later. For
earlier versions, please see [documentation for Mender
3.6](https://docs.mender.io/3.6/client-installation/configuration-file/configuration-options#bootutilitiessetactivepart)
or older.

#### Connectivity

!! This option is not supported starting from the Mender Client version 4.0, and all the HTTP requests will be sent without the Keep-Alive header.

Allows you to configure additional connection-related settings.

##### DisableKeepAlive

!! This option is not supported starting from the Mender Client version 4.0, and all the HTTP requests will be sent without the Keep-Alive header.

If set to true, disables the connections keep alive in general. All the HTTP transactions
will cause a new connection to be created.

##### IdleConnTimeoutSeconds

!! This option is not supported starting from the Mender Client version 4.0, and all the HTTP requests will be sent without the Keep-Alive header.

Specifies the time after which a connection is terminated. The larger it is,
the longer keep alive traffic will happen, as the client will maintain
the connection.

Introduced in Mender Client 3.3.

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

Allows you to configure the certificate, private key, and SSL Engine id to use
during the SSL handshake. If you provide the certificate and private key
as locally accessible files you don't have to specify
<!--AUTOVERSION: "docs/man%"/ignore-->
[SSLEngine](https://www.openssl.org/docs/man1.1.1/man1/engine.html).
If you want to use a Hardware Security Module (HSM) you can provide the private
key as a [PKCS#11 URI](https://tools.ietf.org/html/rfc7512) and in that case
you must also specify the `SSLEngine`.

Note that the client will not use this key for signing authentication requests, which is always
required, even when using SSL client certificates. For that you need to use
[`Security.AuthPrivateKey`](#security).

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

#### RetryDownloadCount

The maximum number of times that mender-update retries continuing a download of an Artifact
that was interrupted e.g. by network issues.

If not set, the default applies (10).
Minimum allowed value is 1, maximum is 10,000.
The waiting time between the retries is 60 seconds and can't be configured.


#### RetryPollCount

The maximum number of tries that the Mender Client performs when contacting the Mender Server before giving up.

It applies to the following Device APIs:
* [Check Update](https://docs.mender.io/api/#device-api-deployments-v2-check-update)
* [Inventory reporting APIs](https://docs.mender.io/api/#device-api-device-inventory)
* [Update Deployment Status](https://docs.mender.io/api/#device-api-deployments-update-deployment-status)
  * Only when reporting [status](https://docs.mender.io/api/#device-api-deployments-schemas-deploymentstatus) "commit", "success" and "failure"
    * _for historical reasons, commit gets reported to the server as a second "install"_


If the setting is zero (the default), the maximum number of retries is `3 * ceil(log2(RetryPollIntervalSeconds) + 1)`.

Introduced in Mender Client 3.3.

#### RetryPollIntervalSeconds

Maximum interval to retry contacting to the server on failed communications. 

**Minimum value.** 
Must be more than 60 seconds. If you specify less than 60, the Mender Client will ignore the setting and use 60 seconds instead.

**Exponential backoff.**
The algorithm starts with 60 seconds between retries. After three failures, the interval doubles for the next three attempts, and so on, until reaching  `RetryPollIntervalSeconds`. From there, the interval won't be increased further and it will keep retrying until the total number of attempts (as set by [RetryPollCount](#retrypollcount)) is reached.

Example for `RetryPollIntervalSeconds=300` and `RetryPollCount=15`:

```markdown
try to connect -> fail
wait 60sec    -> try to connect -> fail
wait 60sec    -> try to connect -> fail
wait 60sec    -> try to connect -> fail

wait 120sec    -> try to connect -> fail
wait 120sec    -> try to connect -> fail
wait 120sec    -> try to connect -> fail

wait 240sec    -> try to connect -> fail
wait 240sec    -> try to connect -> fail
wait 240sec    -> try to connect -> fail

wait 300sec (max)    -> try to connect -> fail
wait 300sec (max)    -> try to connect -> fail
wait 300sec (max)    -> try to connect -> fail
wait 300sec (max)    -> try to connect -> fail
wait 300sec (max)    -> try to connect -> fail
wait 300sec (max)    -> try to connect -> fail

give up
```

The algorithm applies to the same endpoints as described in [RetryPollCount](#retrypollcount).


!!! The same algorithm applies when resuming an Artifact download. 
!!! If the connection to the server is lost in the middle of a download, the client will resume from the last received byte using the algorithm above, but with a fixed retry duration of 60 seconds.

As of Mender Client 3.3 this configuration option applies to inventory updates as well.


#### RootfsPartA

The Linux device that contains root filesystem A. The build system (ie Yocto or
mender-convert) sets this variable so it is rarely modified manually.

Note: Starting with Mender Client v4.0, this configuration option is no longer parsed by the client,
but instead by the `rootfs-image` update module. For most users this does not make any difference,
but for advanced users it allows changing how it is handled, since the update module is a shell
script.

#### RootfsPartB

The Linux device that contains root filesystem B. The build system (ie Yocto or
mender-convert) sets this variable, so it is rarely modified manually.

Note: Starting with Mender Client v4.0, this configuration option is no longer parsed by the client,
but instead by the `rootfs-image` update module. For most users this does not make any difference,
but for advanced users it allows changing how it is handled, since the update module is a shell
script.

#### Security

Allows you to specify the basic security options, `AuthPrivateKey`
and `SSLEngine`, which you can use for signing of authentication requests.

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
server which runs the Mender Server services. It should include the whole URL,
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

See also the section about [state scripts](../../../08.Artifact-creation/04.State-scripts/docs.md).

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

See also the section about [state scripts](../../../08.Artifact-creation/04.State-scripts/docs.md).

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

See also the section about [state scripts](../../../08.Artifact-creation/04.State-scripts/docs.md).

#### TenantToken

A token which identifies which tenant a device belongs to. This is only relevant
if using a multi-tenant environment such as [hosted Mender](https://hosted.mender.io?target=_blank). Always treat the tenant token as a secret.

#### UpdateLogPath

The location where to store the deployment (update) log. This must be on a
persistent partition to avoid losing the logs due to a root filesystem update.

#### DeviceTypeFile

The location where to store the device_type. This must be on a persistent
partition to avoid it accidentally changing due to a root filesystem update. The
default location is `/var/lib/mender/device_type`

#### UpdateControlMapExpirationTimeSeconds

!! This option is not supported starting from the Mender Client version 4.0. For server-side support duration, please refer to our [blog post](https://mender.io/blog/mender-3-6-auto-generation-of-delta-updates#:~:text=Deprecation%3A%20Synchronized%20updates).

The expire time in seconds for an update control map. The value provides the
time window for an application using the update control _dbus API_ to refresh
the update control map before it enters the expired state. _Defaults to
2*UpdatePollIntervalSeconds_
<!-- TODO: Insert links to dbus api specs for update control -->

#### UpdateControlMapBootExpirationTimeSeconds

!! This option is not supported starting from the Mender Client version 4.0. For server-side support duration, please refer to our [blog post](https://mender.io/blog/mender-3-6-auto-generation-of-delta-updates#:~:text=Deprecation%3A%20Synchronized%20updates).

The maximum expire time in seconds after startup for an update control map. The
value provides an upper bound on the update control map [expire
time](#UpdateControlMapExpirationTimeSeconds) after system startup. _Defaults to 600
(10 minutes)_

#### UpdateControlMapPollIntervalSeconds

!! This option is not supported starting from the Mender Client version 4.0. For server-side support duration, please refer to our [blog post](https://mender.io/blog/mender-3-6-auto-generation-of-delta-updates#:~:text=Deprecation%3A%20Synchronized%20updates).

The polling interval at which the client checks for new control maps once the
deployment has started to take place. This influences how quickly will the
device respond to continuing after a pause. It can not be higher than
_UpdateControlMapExpirationTimeSeconds / 2_. _Defaults to
UpdatePollIntervalSeconds_.

#### DaemonLogLevel

The log level for when the daemon is running. Note that this option will get overridden by the cli option `--log-level`.

Introduced in Mender Client 3.4.
