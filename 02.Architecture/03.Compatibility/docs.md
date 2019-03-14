---
title: Compatibility
taxonomy:
    category: docs
---

This document outlines the compatibility between different versions of Mender components, such as the client and server.


## Backward compatibility policy

<!--AUTOVERSION: "% to %"/ignore-->
Mender always provides an [upgrade path](../../administration/upgrading) from the past patch (e.g. 1.2.0 to 1.2.1) and minor version (e.g. 1.1.1 to 1.2.0), and releases follow [Semantic Versioning](http://semver.org/?target=_blank). Note that according to Semantic Versioning, new functionality can be added in minor releases (e.g from 1.2.0 to 1.3.0) so be sure to upgrade components to support the newer functionality before starting to use it.

For example, when a new [Artifact format](../mender-artifacts#the-mender-artifact-file-format) version is released, the *new* Mender client would support older versions of the Artifact format. However, the inverse is not true; the Mender client does not support *newer* versions of the Artifact format. So in this case you need to upgrade all Mender clients before starting to use new versions of the Artifact format (and the features it enables).

As another example, the Mender client supports one version of the server API, while the server can support several API versions. Therefore, the server should always be upgraded before the client.

### Specific versioning criteria

Since Semantic Versioning was primarily written for libraries, it is not
necessarily clear what constitutes an API in the context of Mender. Below are
the lists of specific criteria we use for our versioning policy.

#### Changes counting towards new major version

* Removing or changing existing command line options

* Removing or changing existing REST API

* Edge case: Changing default behavior, with the old behavior still
  available. An example is changing the default artifact format version in
  `mender-artifact`. We have opted for upgrading the major version in this case,
  but this could also go into a minor release

#### Changes counting towards new minor version

* Adding command line options

* Adding new REST API, or adding fields to responses of existing REST API

* Doing a database migration that is incompatible with the old schema (downgrade
  usually not possible without restoring a backup)

#### Changes counting towards new patch version

* Any change to our Golang API. For example, the `mender-artifact` library has
  an API, which is used by some other components, but this API is not considered
  public

* It should always be possible to freely upgrade and downgrade between patch
  versions in the same minor series

## Mender client and Yocto Project version

<!--AUTOVERSION: "% to %"/ignore-->
In general the Mender client introduces new features in minor (e.g. 1.2.0 to 1.3.0) versions and the [meta-mender layer](https://github.com/mendersoftware/meta-mender?target=_blank) is updated accordingly to easily support these new features (e.g. by exposing new [MENDER_* variables](../../artifacts/yocto-project/variables)). The [meta-mender layer](https://github.com/mendersoftware/meta-mender?target=_blank) has branches corresponding to [versions of the Yocto Project](https://wiki.yoctoproject.org/wiki/Releases?target=_blank).

<!--AUTOVERSION: "Mender client %"/ignore "meta-mender %"/ignore-->
|                     | meta-mender krogoth (2.1) and older | meta-mender morty (2.2) | meta-mender pyro (2.3) | meta-mender rocko (2.4) | meta-mender sumo (2.5) | meta-mender thud (2.6) |
|---------------------|-------------------------------------|-------------------------|------------------------|-------------------------|------------------------|------------------------|
| Mender client 1.0.x | no                                  | community               | no                     | no                      | no                     | no                     |
| Mender client 1.1.x | no                                  | community               | community              | no                      | no                     | no                     |
| Mender client 1.2.x | no                                  | community               | community              | community               | no                     | no                     |
| Mender client 1.3.x | no                                  | community               | community              | community               | community              | no                     |
| Mender client 1.4.x | no                                  | community               | community              | community               | community              | no                     |
| Mender client 1.5.x | no                                  | community               | community              | community               | community              | stable                 |
| Mender client 1.6.x | no                                  | community               | community              | community               | community              | stable                 |
| Mender client 1.7.x | no                                  | community               | community              | community               | community              | stable                 |

Leverage [Mender consulting services to support other versions of the Yocto Project](https://mender.io/product/board-support?target=_blank) for your board and environment.


## Mender client/server and Artifact format

The [Mender Artifact format](../mender-artifacts) is managed by the [Mender Artifacts Library](https://github.com/mendersoftware/mender-artifact?target=_blank), which is included in the Mender client and server (for reading Artifacts) as well as in a standalone utility `mender-artifacts` (for [writing Artifacts](../../artifacts/modifying-a-mender-artifact)).

<!--AUTOVERSION: "Mender % / mender-artifact %"/ignore-->
|                                      | Artifact v1 | Artifact v2 |
|--------------------------------------|-------------|-------------|
| Mender 1.0.x / mender-artifact 1.0.x | yes         | no          |
| Mender 1.1.x / mender-artifact 2.0.x | yes         | yes         |
| Mender 1.2.x / mender-artifact 2.1.x | yes         | yes         |
| Mender 1.3.x / mender-artifact 2.1.x | yes         | yes         |
| Mender 1.4.x / mender-artifact 2.2.x | yes         | yes         |
| Mender 1.5.x / mender-artifact 2.2.x | yes         | yes         |
| Mender 1.6.x / mender-artifact 2.3.x | yes         | yes         |
| Mender 1.7.x / mender-artifact 2.4.x | yes         | yes         |

!! Older Mender clients do not support newer versions of the Artifact format; they will abort the deployment. You can build older versions of the Mender Artifact format to upgrade older Mender clients. See [Write a new Artifact](../../artifacts/modifying-a-mender-artifact#create-an-artifact-from-a-raw-root-file-system) for an introduction how to do this.


## Mender server and client API

The compatibility between the Mender server and client is managed by the [Device API versions](../../apis/device-apis) exposed by the server and used by the client. If the Mender server supports the API version of the Mender client, they are compatible.  However, please ensure that the client and server support the [Artifact format](#mender-clientserver-and-artifact-format) version you are using.

<!--AUTOVERSION: "| %"/ignore-->
|        | Mender server versions | Mender client versions |
|--------|------------------------|------------------------|
| API v1 | 1.0.x                  | 1.0.x                  |
|        | 1.1.x                  | 1.1.x                  |
|        | 1.2.x                  | 1.2.x                  |
|        | 1.3.x                  | 1.3.x                  |
|        | 1.4.x                  | 1.4.x                  |
|        | 1.5.x                  | 1.5.x                  |
|        | 1.6.x                  | 1.6.x                  |
|        | 1.7.x                  | 1.7.x                  |
