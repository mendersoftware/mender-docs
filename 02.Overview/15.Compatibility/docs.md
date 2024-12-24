---
title: Compatibility policy
taxonomy:
    category: docs
---

This document outlines the Mender compatibility and support policy. For support
for specific system releases, compatibility between individual Mender components
and currently supported Mender releases, see
[Release-information](../../302.Release-information/01.Release-schedule/docs.md).


## Components

Mender consists of different components that are independently released and supported.
They are:

* Mender Client: Runs on Devices, authenticates the device with the Server
(using component `mender-auth`), reports inventory, and manages updates
(using `mender-update`). Also includes add-on components mender-connect,
mender-configure, mender-monitor and Update Modules Rootfs, Delta, File, and Directory.

* Mender Gateway: Is on the network between Mender Client and Mender Server,
and can enable OTA access for devices, cache Artifacts to reduce uplink load and/or
implement mutual TLS (mTLS) by authenticating Devices which are using device certificates.

* Mender Server: Enables management of Devices, Releases and Deployments.
Devices connect and receive OTA updates from the Mender Server.
Available as on-premise and hosted solution. When using hosted Mender, upgrades and
support is managed by Northern.tech so versioning of the server itself is not
relevant to users.

!!! Historically Mender was released as a bundle release with these components included, and Mender 3.7 LTS is the last such bundle release. Read more about this change in [this blog post](https://mender.io/blog/mender-versioning-new-releases-by-component?target=_blank).


## Yocto Project LTS support in meta-mender

The Mender Client and Mender Gateway components are supported for installation
and configuration in [meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank),
which follows [Yocto Project LTS releases](https://wiki.yoctoproject.org/wiki/Releases?target=_blank)
and generally supports the **two latest Yocto Project LTS releases**.

There is a corresponding branch in meta-mender for the Yocto Project release it supports.
When a new Mender component version is released, all currently supported Yocto Project
branches in meta-mender are updated with this Mender component version.

When a new Yocto Project LTS is released, all currently supported Mender components are
supported in this Yocto Project LTS. Once a Yocto Project LTS release becomes unsupported,
Mender stops providing updates with new Mender software to it, essentially leaving the
last Mender components fixed in that release.


## Backward compatibility

<!--AUTOVERSION: "% to %"/ignore-->
Mender always provides an upgrade path from the past patch (e.g. 3.2.0 to 3.2.1)
and minor version (e.g. 3.1.1 to 3.2.0), and releases follow
[Semantic Versioning](http://semver.org/?target=_blank). Note that according to
Semantic Versioning, minor releases add new functionality (e.g. from 3.2.0 to 3.3.0)
so be sure to upgrade components to support the newer functionality before using it.

For example, when Mender releases a new
[Artifact format](../03.Artifact/docs.md#the-mender-artifact-file-format) version,
the new Mender Client still supports older versions of the Artifact format.
However, the inverse is not true; the Mender Client does not support newer versions
of the Artifact format. So in this case you need to upgrade all Mender Clients before
starting to use new versions of the Artifact format (and the features it enables).

As another example, the Mender Client supports one version of the Server API,
while the Server can support several API versions. Therefore,
*always update the Server before the Client*.

In general, to avoid backward compatibility issues upgrade components in this order:

1. Mender Server (N/A if using hosted Mender)

2. Mender Gateway (if used)

3. Mender Client

4. Logic or data used by Mender Client such as Update Modules, Artifact versions

Mender components have different support durations for different minor versions with
LTS releases. Please refer to the
[Release-information](../../302.Release-information/01.Release-schedule/docs.md) page
for the currently supported components.


## Versioning scheme

Since Mender components use [Semantic Versioning](http://semver.org/?target=_blank),
the version numbers are in the MAJOR.MINOR.PATCH format.

We increment:

* MAJOR version when we make incompatible API or functionality changes

* MINOR version when we add functionalities in a backward compatible manner

* PATCH version when we make backward compatible bug fixes to existing releases

Mender comes with long-term supported (LTS) releases, which are the only ones which are commercially supported. We maintain LTS releases through patch releases for *one year* from the release date.


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
