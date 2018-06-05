---
title: Compatibility
taxonomy:
    category: docs
---

This document outlines the compatibility between different versions of Mender components, such as the client and server.


## Backward compatibility policy

Mender always provides an [upgrade path](../../administration/upgrading) from the past patch (e.g. 1.2.0 to 1.2.1) and minor version (e.g. 1.1.1 to 1.2.0), and releases follow [Semantic Versioning](http://semver.org/?target=_blank). Note that according to Semantic Versioning, new functionality can be added in minor releases (e.g from 1.2.0 to 1.3.0) so be sure to upgrade components to support the newer functionality before starting to use it.

For example, when a new [Artifact format](../mender-artifacts#the-mender-artifact-file-format) version is released, the *new* Mender client would support older versions of the Artifact format. However, the inverse is not true; the Mender client does not support *newer* versions of the Artifact format. So in this case you need to upgrade all Mender clients before starting to use new versions of the Artifact format (and the features it enables).

As another example, the Mender client supports one version of the server API, while the server can support several API versions. Therefore, the server should always be upgraded before the client.


## Mender client and Yocto Project version

In general the Mender client introduces new features in minor (e.g. 1.2.0 to 1.3.0) versions and the [meta-mender layer](https://github.com/mendersoftware/meta-mender?target=_blank) is updated accordingly to easily support these new features (e.g. by exposing new [MENDER_* variables](../../artifacts/variables)). The [meta-mender layer](https://github.com/mendersoftware/meta-mender?target=_blank) has branches corresponding to [versions of the Yocto Project](https://wiki.yoctoproject.org/wiki/Releases?target=_blank).

|                     | meta-mender krogoth (2.1) and older | meta-mender morty (2.2) | meta-mender pyro (2.3) | meta-mender rocko (2.4) |
|---------------------|-------------------------------------|-------------------------|------------------------|-------------------------|
| Mender client 1.0.x | no                                  | yes                     | no                     | no                      |
| Mender client 1.1.x | no                                  | no                      | yes                    | no                      |
| Mender client 1.2.x | no                                  | no                      | yes                    | yes                     |
| Mender client 1.3.x | no                                  | no                      | yes                    | yes                     |
| Mender client 1.4.x | no                                  | no                      | no                     | yes                     |

Leverage [Mender consulting services to support other versions of the Yocto Project](https://mender.io/product/board-support?target=_blank) for your board and environment.


## Mender client/server and Artifact format

The [Mender Artifact format](../mender-artifacts) is managed by the [Mender Artifacts Library](https://github.com/mendersoftware/mender-artifact?target=_blank), which is included in the Mender client and server (for reading Artifacts) as well as in a standalone utility `mender-artifacts` (for [writing Artifacts](../../artifacts/modifying-a-mender-artifact)).

|                     | Artifact v1 | Artifact v2 |
|---------------------|-------------|-------------|
| Mender 1.0.x / mender-artifact 1.0.x | yes         | no          |
| Mender 1.1.x / mender-artifact 2.0.x | yes         | yes         |
| Mender 1.2.x / mender-artifact 2.1.x | yes         | yes         |
| Mender 1.3.x / mender-artifact 2.1.x | yes         | yes         |
| Mender 1.4.x / mender-artifact 2.2.x | yes         | yes         |

!! Older Mender clients do not support newer versions of the Artifact format; they will abort the deployment. You can build older versions of the Mender Artifact format to upgrade older Mender clients. See [Write a new Artifact](../../artifacts/modifying-a-mender-artifact#write-a-new-artifact) for an introduction how to do this.


## Mender server and client API

The compatibility between the Mender server and client is managed by the [Device API versions](../../apis/device-apis) exposed by the server and used by the client. If the Mender server supports the API version of the Mender client, they are compatible.  However, please ensure that the client and server support the [Artifact format](#mender-client-and-artifact-format) version you are using.

|        | Mender server versions | Mender client versions |
|--------|------------------------|------------------------|
| API v1 | 1.0.x                  | 1.0.x                  |
|        | 1.1.x                  | 1.1.x                  |
|        | 1.2.x                  | 1.2.x                  |
|        | 1.3.x                  | 1.3.x                  |
|        | 1.4.x                  | 1.4.x                  |
