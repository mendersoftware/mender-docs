---
title: Compatibility
taxonomy:
    category: docs
---

This document outlines the compatibility between different versions of Mender components, such as the client and server.


## Backward compatibility policy

<!--AUTOVERSION: "% to %"/ignore-->
Mender always provides an [upgrade
path](../../07.Server-installation/03.Installation-with-docker-compose/01.Upgrading/docs.md) from the past patch
(e.g. 1.2.0 to 1.2.1) and minor version (e.g. 1.1.1 to 1.2.0), and releases
follow [Semantic Versioning](http://semver.org/?target=_blank). Note that
according to Semantic Versioning, minor releases add new functionality (e.g from
1.2.0 to 1.3.0) so be sure to upgrade components to support the newer
functionality before using it.

For example, when Mender releases a new [Artifact
format](../03.Artifact/docs.md#the-mender-artifact-file-format) version, the
*new* Mender client still supports older versions of the Artifact format.
However, the inverse is not true; the Mender client does not support *newer*
versions of the Artifact format. So in this case you need to upgrade all Mender
clients before starting to use new versions of the Artifact format (and the
features it enables).

As another example, the Mender client supports one version of the server API,
while the server can support several API versions. Therefore, always update the
server before the client.

Mender also follows different support durations for different minor versions with LTS releases.
Please refer to the [Release-information](../../302.Release-information/01.Release-schedule/docs.md) for more information about LTS releases and the release schedule.


### Specific versioning criteria

Since Semantic Versioning was primarily written for libraries, it is not
necessarily clear what constitutes an API in the context of Mender. Below are
the lists of specific criteria we use for our versioning policy.

#### Changes resulting in new major version (M.m.p)

* Removing or changing existing command line options

* Removing or changing existing REST API

* Edge case: Changing default behavior, with the old behavior still
  available. An example is changing the default artifact format version in
  `mender-artifact`. We have opted for upgrading the major version in this case,
  but this could also go into a minor release

#### Changes resulting in new minor version (m.M.p)

* Adding command line options

* Adding new REST API, or adding fields to responses of existing REST API

* Doing a database migration that is incompatible with the old schema (downgrade
  usually not possible without restoring a backup)

#### Changes resulting in new patch version (m.m.P)

* Any change to our Golang API. For example, the `mender-artifact` library has
  an API, used by other components, but this API is not considered public

* It should always be possible to freely upgrade and downgrade between patch
  versions in the same minor series

## Mender client and Yocto Project version

<!--AUTOVERSION: "% to %"/ignore-->
In general the Mender client introduces new features in minor (e.g. 1.2.0 to 1.3.0) versions and the [meta-mender layer](https://github.com/mendersoftware/meta-mender?target=_blank) is updated accordingly to easily support these new features (e.g. by exposing new [MENDER_* variables](../../05.System-updates-Yocto-Project/99.Variables/docs.md)). The [meta-mender layer](https://github.com/mendersoftware/meta-mender?target=_blank) has branches corresponding to [versions of the Yocto Project](https://wiki.yoctoproject.org/wiki/Releases?target=_blank). 

Clarification of the table:
* *stable* - recipe is maintained by Northern.tech
* *community* - best effort maintenance from community and Northern.tech
* *no* - recipe has never been release



<!--AUTOVERSION: "Mender client %"/ignore "| % ("/ignore-->
| Client vs meta-mender version   | warrior (2.7)<sup>2</sup> | zeus (3.0)            | dunfell (3.1)      |
|---------------------------------|---------------------------|-----------------------|--------------------|
| Older                           | no                        | no                    | no                 |
| Mender client 1.5.x             | no                        | no                    | no                 |
| Mender client 1.6.x             | no                        | no                    | no                 |
| Mender client 1.7.x<sup>1</sup> | community                 | no                    | no                 |
| Mender client 2.0.x             | community                 | no                    | no                 |
| Mender client 2.1.x             | community                 | no                    | no                 |
| Mender client 2.2.x             | community                 | community             | stable             |
| Mender client 2.3.x             | community                 | community             | stable             |
| Mender client 2.4.x             | community                 | community             | stable             |
| Mender client 2.5.x             | community                 | community             | stable             |
| Mender client 2.6.x             | community                 | community             | stable             |
| Mender client 3.0.x             | no                        | community             | stable<sup>3</sup> |
| Mender client 3.1.x             | no                        | community             | stable<sup>3</sup> |
| Mender client 3.2.x             | no                        | community             | stable<sup>3</sup> |
| Mender client 3.3.x             | no                        | community             | stable<sup>3</sup> |

!! <sup>1</sup> Rolling back to 1.x.x from a failed upgrade to 2.x.x is supported. However, it is not possible to downgrade to a Mender 1.x.x client from a 2.x.x client, once the update containing 2.x.x has been committed.

<!--AUTOVERSION: "from % to newer"/ignore "from-%-to-newer"/ignore-->
! <sup>2</sup> If upgrading from thud to newer versions, see also [known issues when upgrading from thud to newer versions](../../301.Troubleshoot/02.Yocto-Project-runtime/docs.md#upgrading-from-thud-to-newer-versions-fails-with-dual-rootfs-configuration-not-found).

<!--AUTOVERSION: "client % and later"/ignore "Yocto branches 3.1 (%) and older"/ignore-->
!!! <sup>3</sup> Mender client 3.0.0 and later are not installed by default in Yocto branches 3.1 (dunfell) and older. To enable this or a later version, please see [the `PREFERRED_VERSION` setting when configuring the Yocto build](../../05.System-updates-Yocto-Project/03.Build-for-demo/docs.md#configuring-the-build).

Leverage [Mender consulting services to support other versions of the Yocto Project](https://mender.io/product/board-support?target=_blank) for your board and environment.


## Mender client/server and Artifact format

The [Mender Artifact format](../03.Artifact/docs.md) is managed by the [Mender Artifacts Library](https://github.com/mendersoftware/mender-artifact?target=_blank), which is included in the Mender client and server (for reading Artifacts) as well as in a standalone utility `mender-artifact` (for [writing Artifacts](../../06.Artifact-creation/03.Modify-an-Artifact/docs.md)).

<!--AUTOVERSION: "Mender % / mender-artifact %"/ignore-->
|                                      | Artifact v1 | Artifact v2 | Artifact v3 |
|--------------------------------------|-------------|-------------|-------------|
| Mender 1.0.x / mender-artifact 1.0.x | yes         | no          | no          |
| Mender 1.1.x / mender-artifact 2.0.x | yes         | yes         | no          |
| Mender 1.2.x / mender-artifact 2.1.x | yes         | yes         | no          |
| Mender 1.3.x / mender-artifact 2.1.x | yes         | yes         | no          |
| Mender 1.4.x / mender-artifact 2.2.x | yes         | yes         | no          |
| Mender 1.5.x / mender-artifact 2.2.x | yes         | yes         | no          |
| Mender 1.6.x / mender-artifact 2.3.x | yes         | yes         | no          |
| Mender 1.7.x / mender-artifact 2.4.x | yes         | yes         | no          |
| Mender 2.0.x / mender-artifact 3.0.x | no          | yes         | yes         |
| Mender 2.1.x / mender-artifact 3.1.x | no          | yes         | yes         |
| Mender 2.2.x / mender-artifact 3.2.x | no          | yes         | yes         |
| Mender 2.3.x / mender-artifact 3.3.x | no          | yes         | yes         |
| Mender 2.4.x / mender-artifact 3.4.x | no          | yes         | yes         |
| Mender 2.5.x / mender-artifact 3.4.x | no          | yes         | yes         |
| Mender 2.6.x / mender-artifact 3.5.x | no          | yes         | yes         |
| Mender 2.7.x / mender-artifact 3.5.x | no          | yes         | yes         |
| Mender 3.0.x / mender-artifact 3.6.x | no          | yes         | yes         |
| Mender 3.1.x / mender-artifact 3.6.x | no          | yes         | yes         |
| Mender 3.2.x / mender-artifact 3.6.x | no          | yes         | yes         |
| Mender 3.3.x / mender-artifact 3.7.x | no          | yes         | yes         |

!! Older Mender clients do not support newer versions of the Artifact format; they will abort the deployment. You can build older versions of the Mender Artifact format to upgrade older Mender clients. See [Write a new Artifact](../../06.Artifact-creation/01.Create-an-Artifact/docs.md#create-a-full-filesystem-update-artifact) for an introduction how to do this.


## Mender server and client API

The compatibility between the Mender server and client is managed by the Device API versions exposed by the server and used by the client. If the Mender server supports the API version of the Mender client, they are compatible.  However, please ensure that the client and server support the [Artifact format](#mender-clientserver-and-artifact-format) version you are using. Device API docs are available in the [API chapter](../../200.Server-side-API/?target=_blank#device-apis).


The higher version API contains a mix of old and new API endpoints. For endpoints which haven't changed in the new version the previous version ones are assumed.


*Example* The device supports the V2 API. It expects the [single V2 endpoint](https://docs.mender.io/api/#device-api-deployments-v2) to be available. For all other endpoints it will use the V1. 


<!--AUTOVERSION: "Mender server % and %"/ignore "Mender server % and later"/ignore "Mender client % and %"/ignore "Mender client % and later"/ignore-->
|                               | API v1 | API v2 |
|-------------------------------|--------|--------|
| Mender server 1.x.x and 2.x.x | yes    | no     |
| Mender server 3.0.0 and later | yes    | yes    |
|-------------------------------|--------|--------|
| Mender client 1.x.x and 2.x.x | yes    | no     |
| Mender client 3.0.0 and later | yes    | yes    |


## Mender client and Mender connect

<!--AUTOVERSION: "|  %"/ignore "| %"/ignore -->
|     Mender client / mender-connect | mender-connect version |
|------------------------------------|------------------------|
|  2.6.x                             | 1.0.x                  |
|  2.7.x                             | 1.1.x                  |
|  3.0.x                             | 1.2.x                  |
|  3.1.x                             | 1.2.x                  |
|  3.2.x                             | 2.0.x <sup>1<sup>      |
|  3.3.x                             | 2.0.x <sup>1<sup>      |

<!--AUTOVERSION: "mender-connect % and later"/ignore "Yocto branches 3.1 (%) and older"/ignore-->
!!! <sup>1</sup> mender-connect 2.0.0 and later are not installed by default in Yocto branches 3.1 (dunfell) and older. To enable this or a later version, please see [the `PREFERRED_VERSION` setting when configuring the Yocto build](../../05.System-updates-Yocto-Project/03.Build-for-demo/docs.md#configuring-the-build).
