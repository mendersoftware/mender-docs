---
title: Mender Artifact
taxonomy:
    category: docs
    label: reference
---

As described in the [overview](../overview) Mender uses the output from a build
system and deploys this to remote devices.

In order to ensure a robust update process, Mender needs *additional metadata*
alongside the update payload. Depending on the version of the
Artifact used, the metadata might be different, but must contain:

* *Name* of the software build, so that software is not redeployed if it is
  on the device.
* Device types the software is *compatible* with, so that software is not
  deployed to incompatible hardware (e.g. CPU architecture, hardware floating
  point support, peripheral drivers).

For system updates, the metadata contains also a *checksum* of the root file
  system, so that software is not run if it gets corrupted during transit or
  storage. For application updates, the metadata may include other fields.

## The Mender Artifact file format

To handle the requirements mentioned above, Mender defines and uses a specific
file format, identified by its `.mender` suffix. A file in this format is
referred to as a **Mender Artifact**, or simply *an Artifact*. All relevant
components of Mender, such as the client and server, understand and use (only)
this specific file format when working with software deployments.

Internally, a Mender Artifact is simply a file archive in the [tarball
format](https://en.wikipedia.org/wiki/Tar_(computing)?target=_blank). It
contains several files for incorporating versioning, extensions and metadata, as
well as the main file: the update payload.

The diagram below shows an example of the main attributes and structure of a
Mender Artifact file. Please note that the exact format of the artifact may vary
between versions.

![Mender Artifact format](mender-artifact-format.png)

<!--AUTOVERSION: "mender-artifact/blob/%"/mender-artifact-->
See the [Mender Artifact file
documentation](https://github.com/mendersoftware/mender-artifact/blob/master/Documentation?target=_blank)
to find more details about the exact format of the Mender Artifact.

## Versions

Mender is constantly evolving to adapt to the needs of its users. When a new
feature requires it, the Mender Artifact format gets upgraded. See the
[compatibility documentation](../compatibility) for an overview of the
compatibility between Mender client and Mender Artifact format versions.

## Streaming

Mender takes advantage of the tar format's support for streaming. When
downloading a Mender Artifact from the Mender server or external storage, the
Mender client streams the payload directly to the inactive partition, without
needing any temporary storage for unpacking it before writing it. This
drastically reduces storage requirements for the update process, improves
performance and reduces flash wear.

## Download interrupted

In cases where Artifact downloads are interrupted, e.g. due to unreliable
wireless network connectivity, Mender will resume the download from where it was
interrupted, using [HTTP range
requests](https://tools.ietf.org/html/rfc7233?target=_blank).

## Compression

To enable streaming and control based on metadata, like aborting the download if
the Artifact is not compatible with the device, the Mender Artifact itself is
not compressed. Instead, it compresses the root filesystems within Artifacts,
with the [gzip compression
algorithm](https://en.wikipedia.org/wiki/gzip?target=_blank) by default. Other
compression formats like `lzma` is available through configuration.

## Signature verification

To verify that the Artifact comes from a known source, the Mender Artifact
format supports image signing and verification. To create a signed Artifact,
which the Mender Client will verify during the update process, please follow the
instructions at [Signing and verifying Mender
Artifact](../../artifact-creation/sign-and-verify).

## State scripts

Mender client supports extending and customizing the installation process using
state scripts functionality. The most common use case is to do application data
migration, for example if an SQLite database stores application data like a user
profile and a new column needs to be added before starting the new version of
the application. A wide variety of other use cases are covered by state scripts.
For more use cases more information on how to use state scripts see [Mender
state scripts](../state-scripts).

## Working with Mender Artifacts

Although it is possible to use a tar utility to extract, modify and package
Mender Artifacts this is error-prone due to the details that need to be handled,
like the ordering of the files, contents of metadata or checksum computations.
For this reason, Mender recommends to use the Mender Artifact utility or Go
library when you need to work with Mender Artifacts. The Mender Artifact library
and utility is available as open source in the [Mender Artifact
repository](https://github.com/mendersoftware/mender-artifact?target=_blank).
See [Artifact Creation section](../../artifact-creation) to learn more about the
usage of the utility.

For system updates, there are two paths to generate Mender Artifacts.

* For Yocto based projects, Mender integrates by adding the
  [meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank)
  layer to the build environment. Find more information on how to do this as
  part of the [System updates using Yocto
  Project](../../system-updates/yocto-project).
* For Debian based OS, Mender supports various workflows to generate Mender
  Artifacts. Find more information for this workflows at [System updates for
  Debian family boards](../../system-updates/debian-family).

For application updates, the Artifact generation is use case dependent.
