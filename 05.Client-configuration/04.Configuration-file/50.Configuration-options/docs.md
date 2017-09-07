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

#### RetryPollIntervalSeconds

An integer that sets the number of seconds to wait between each attempt to
download an update file. Note that the client may attempt more often initially
to enable rapid upgrades, but will gradually fall back to this value if the
server is busy. See also the section about [polling
intervals](../polling-intervals).

#### RootfsPartA

The Linux device that contains root filesystem A. This is set by the build
system based on Yocto configuration and rarely needs to be modified.

#### RootfsPartB

The Linux device that contains root filesystem B. This is set by the build
system based on Yocto configuration and rarely needs to be modified.

#### ServerURL

The server URL which is used as the basis for API requests. This should be set
to the server that runs the Mender server services. It should include the whole
URL, including `https://` and a trailing slash.

#### ServerCertificate

The location of the public certificate of the server, if any. If this
certificate is missing, or the one presented by the server doesn't match the one
specified in this setting, the server certificate will be validated using
standard certificate trust chains.

#### StateScriptTimeoutSeconds

The number of seconds to wait for any state script to terminate. If a script
exceeds this running time, its process group will be killed and Mender will
continue, treating the script as having failed. See also the section about
[state scripts](../../../artifacts/state-scripts).

#### TenantToken

A token which identifies which tenant a device belongs to. This is only relevant
if using Hosted Mender.

#### UpdateLogPath

The location where deployment logs will be written. This must be on a persistent
partition to work correctly.

#### UpdatePollIntervalSeconds

An integer that sets the number of seconds to wait between each check for a new
update. Note that the client may occasionally check more often if there has been
recent activity on the device. See also the section about [polling
intervals](../polling-intervals).
