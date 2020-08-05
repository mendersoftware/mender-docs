---
title: Artifact
taxonomy:
    category: docs
---

In order to ensure a secure and robust update process, Mender needs *additional metadata*
alongside the raw bits of the update payload. Depending on the version of the Artifact used,
the metadata might be different, but must contain the:

* *Name* of the software build, used to track installed software on a given device
  and ensures that identical software versions are not redeployed.
* *Device types* the software is *compatible* with, so that software is not
  deployed to incompatible hardware (e.g. CPU architecture, hardware floating
  point support, peripheral drivers).
* *Checksum* of the payload, so that software is not run if it gets corrupted
  during transit or storage.


## The Mender Artifact file format

To handle the requirements mentioned above, Mender uses a
specific file format, identified by its `.mender` suffix which is also known as
a **Mender Artifact** or simply an **Artifact**. All relevant components of Mender,
such as the client and server, understand and use only this specific file
format when doing software deployments.

Internally, a Mender Artifact is simply a file archive in the
[tarball format](https://en.wikipedia.org/wiki/Tar_(computing)?target=_blank).
It contains several files for incorporating versioning, extensions, metadata and
the payload file(s).

Artifact payloads support multiple compression algorithms, and are compressed by
default.

The diagram below shows an example of the main attributes and structure of a
Mender Artifact file.

!!! The exact Artifact format may vary between versions.

![Mender Artifact format](mender-artifact-format.png)

<!--AUTOVERSION: "mender-artifact/blob/%"/mender-artifact-->
You can find more details about the Mender Artifact format in the
[Mender Artifact specification](https://github.com/mendersoftware/mender-artifact/blob/master/Documentation?target=_blank).


## Versions

Mender is constantly evolving to adapt to the needs of its users, and the Mender
Artifact format has several revisions. See the
[Compatibility section](../14.Compatibility/docs.md) for an overview of
which versions of the Mender Artifact format are supported by which Mender client
versions.


## Work with Mender Artifacts

The command-line utility `mender-artifact` is the best way to work directly with
Mender Artifacts. It allows you to view, create, modify and sign all types of
Mender Artifacts. Get it in the
[Downloads section](../../08.Downloads/docs.md#mender-artifact).

Mender also has OS-level integrations for creating system updates as part of
your existing OS build process. Learn more by reading the following sections:

- [System updates: Debian family](../../04.System-updates-Debian-family/chapter.md)
- [System updates: Yocto Project](../../05.System-updates-Yocto-Project/chapter.md)


### Sign and verify

To verify that the Artifact comes from a trusted source, the Mender Artifact
format supports end-to-end signing and verification. In order to create a
signed Artifact, please follow the instructions at
[Sign & Verify](../../06.Artifact-creation/07.Sign-and-verify/docs.md).
