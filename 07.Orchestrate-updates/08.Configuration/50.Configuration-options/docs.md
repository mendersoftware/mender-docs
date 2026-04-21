---
title: Configuration options
taxonomy:
    category: docs
---

This section lists all the available configuration options in the
`mender-orchestrator.conf` file.

#### ArtifactVerifyKey

There are two options for specifying verification keys:

* `ArtifactVerifyKey` is a single path to a key.
* `ArtifactVerifyKeys` is a list of paths to keys. When multiple keys are
  specified, the keys are tried in order, and the first key that verifies an
  Artifact signature is used. This is useful for key rotation or signing
  different types of Artifacts.

Only one of `ArtifactVerifyKey` or `ArtifactVerifyKeys` may be specified.

When set, Mender Orchestrator verifies the following:

* All Artifact installs contain a signature. If a signature is not provided,
  then the Orchestrator rejects the update.
* The provided public key verifies the signature of the update.

See also the section about [signing and
verification](../../../08.Artifact-creation/09.Sign-and-verify/docs.md).

#### ArtifactsCache

Configures Artifacts caching behavior. When enabled, Mender Orchestrator caches
downloaded Artifacts locally so that Components sharing the same Artifact do not
cause redundant downloads.

##### Enabled

Set to `true` to activate caching. Defaults to `false`.

##### Path

The directory where cached Artifacts are stored. Defaults to
`{datastore}/artifacts` (typically `/var/lib/mender-orchestrator/artifacts`).

!!! Note: The path configured for the cache must exist on the filesystem before the Orchestrator starts. The service will not attempt to create the directory structure if it is missing.

##### MaxSizeBytes

The maximum size in bytes for the Artifacts cache. When the cache exceeds this
limit, the oldest cached Artifacts are removed to make room for new ones. A
value of `0` means no limit. Defaults to `0`.

Example:

```json
{
  "ArtifactsCache": {
    "Enabled": true,
    "Path": "/var/cache/mender-orchestrator",
    "MaxSizeBytes": 2147483648
  }
}
```

See also the section about [Artifacts
caching](../../07.Artifacts%20handling/01.Caching/docs.md).

#### HttpsClient

Allows you to configure the certificate, private key, and SSL Engine id to use
during the SSL handshake. If you provide the certificate and private key as
locally accessible files you don't have to specify SSLEngine.

If you want to use a Hardware Security Module (HSM) you can provide the private
key as a [PKCS#11 URI](https://tools.ietf.org/html/rfc7512).

##### Certificate

A path to the file in PEM format holding the client certificate.

##### Key

Either a valid PKCS#11 URI or a path to a file holding the private key.

Example:

```json
{
  "HttpsClient": {
    "Certificate": "/certs/cert.pem",
    "Key": "/keys/private/key.pem"
  }
}
```

#### InterfaceTimeoutSeconds

An integer that specifies the number of seconds that an update
[Interface](../../04.Interface-protocol/docs.md) is allowed to run before it is
considered hung and killed. The default is `14400` (4 hours).

#### LogLevel

The default log level for Mender Orchestrator. Valid values are: `trace`,
`debug`, `info`, `warning`, `error`, `fatal`.

Note that this option will get overridden by the cli option `--log-level`.

If not set, defaults to `info`.

#### ManifestStore

The directory where manifests are stored. Defaults to `{datastore}/manifests`
(typically `/var/lib/mender-orchestrator/manifests`).

#### ServerCertificate

The location of the public certificate of the server, if any. If this
certificate is missing, or the one presented by the server does not match the one
specified in this setting, the server certificate is validated using standard
certificate trust chains.

#### TopologyComponents

The file path to the Topology components YAML file. This defines the Components
present in the System and how they can be updated.
