---
title: Artifact
taxonomy:
    category: docs
---

As described in the [architecture overview](../01.Introduction/docs.md) Mender uses the output
from a build system and deploys this to remote devices.

In order to ensure a robust update process, Mender needs *additional metadata*
alongside the raw bits of the file system. Depending on the version of the Artifact used, 
the metadata might be different, but must contain:

* *Name* of the software build, so that software is not redeployed if it is already installed at the device.
* Device types the software is *compatible* with, so that software is not deployed to incompatible hardware (e.g. CPU architecture, hardware floating point support, peripheral drivers).
* *Checksum* of the root file system, so that software is not run if it gets corrupted during transit or storage.

Furthermore, as new use cases and platforms are supported in the future,
more metadata is expected to be needed as part of the Mender deployment process.


## The Mender Artifact file format

To handle the requirements mentioned above, Mender defines and uses a
specific file format, identified by its `.mender` suffix. A file in this format
is referred to as a **Mender Artifact**, or simply *an Artifact*.
All relevant components of Mender, such as the client and server, understand
and use (only) this specific file format when working with software deployments.

Internally, a Mender Artifact is simply a file archive in the [tarball format](https://en.wikipedia.org/wiki/Tar_(computing)?target=_blank).
It contains several files for incorporating versioning, extensions and metadata,
as well as the main file: the root file system.

The diagram below shows an example of the main attributes and structure of a
Mender Artifact file. Please note that the exact format of the artifact may vary between versions.

![Mender Artifact format](mender-artifact-format.png)

<!--AUTOVERSION: "mender-artifact/blob/%"/mender-artifact-->
More details about the exact format of the Mender Artifact can be found in the
[Mender Artifact file documentation](https://github.com/mendersoftware/mender-artifact/blob/master/Documentation?target=_blank).


## Versions

Mender is constantly evolving to adapt to the needs of its users. As new features are added, new versions of the 
Mender Artifact format may be introduced as well, if the features require it.
See the [compatibility documentation](../02.Compatibility/docs.md) for an overview of which versions of the Mender Artifact format is supported by Mender clients.


## Streaming, resume and compression

The tar format supports streaming, which Mender takes advantage of. As a Mender
Artifact is downloaded from the Mender server or external storage, the Mender
client streams the root file system within it directly to the inactive partition,
without needing any temporary storage for unpacking it before it is written.
This drastically reduces storage requirements for the update process,
improves performance and reduces flash wear.

In cases where Artifact downloads are interrupted, e.g. due to unreliable wireless
network connectivity, Mender will resume the download from where it was
interrupted, using [HTTP range requests](https://tools.ietf.org/html/rfc7233?target=_blank).

To enable streaming and control based on metadata, like aborting the download
if the Artifact is not compatible with the device, the Mender Artifact itself
is not compressed. Instead, the root file systems within Artifacts are
compressed, currently with the [gzip compression algorithm](https://en.wikipedia.org/wiki/gzip?target=_blank)
by default.


## Signing and verification

To verify that the Artifact comes from a known source, the Mender Artifact format supports 
image signing and verification. In order to create a signed Artifact, which can be verified by the Mender Client
during the update process, please follow the instructions at [Signing and verifying Mender Artifact](../../04.Artifacts/40.Signing-and-verification/docs.md).

## State scripts

Starting with the Mender client version 1.2, support for state scripts is included. The most common use case is to do application data migration, 
for example if application data like a user profile is stored in an SQLite database and a new column needs to be added before starting the new version of the application.
There are a wide variety of other use cases that are covered by state scripts. For more use cases see [example use cases](../../04.Artifacts/50.State-scripts/docs.md#example-use-cases).
For more information how to use state scripts see [Mender state scripts](../../04.Artifacts/50.State-scripts/docs.md).


## Working with Mender Artifacts

The easiest and most common way to generate Mender Artifacts is by
adding the [meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank)
layer to your Yocto Project build environment. There is more information
on how to do this as part of the tutorial [Building a Mender Yocto Project image](../../04.Artifacts/10.Yocto-project/01.Building/docs.md).

Although it is possible to use a tar utility to extract, modify and package
Mender Artifacts, this is error-prone due to the amount of details
that need to be handled, like the ordering of the files, contents of
metadata and checksum computation.
For this reason, it is recommended to use the Mender Artifact utility or Go library
when you need to work with Mender Artifacts. The Mender Artifacts library and utility
is available as open source in the [Mender Artifacts repository](https://github.com/mendersoftware/mender-artifact?target=_blank)
and there is a tutorial using the utility at [Modifying a Mender Artifact](../../04.Artifacts/25.Modifying-a-Mender-Artifact/docs.md).
