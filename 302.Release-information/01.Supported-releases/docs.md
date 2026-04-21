---
title: Supported releases
taxonomy:
    category: docs
---

This document outlines the currently supported releases and compatibility between
individual Mender components. To understand the general compatibility policy
of Mender, see the [Compatibility policy](../../02.Overview/15.Compatibility-policy/docs.md).


## Components and LTS releases

The latest long term support (LTS) versions of Mender components are shown in the
in the table below:

| Released component    | Release month | Support status          |
|-----------------------|---------------|-------------------------|
| Mender Client 6.0     | 2026-03       | Supported               |
| Mender Client 5.0     | 2025-01       | Supported               |
| Mender MCU Client 1.0 | 2026-04       | Supported               |
| Mender Gateway 2.0    | 2025-01       | Supported               |
| Mender Server 4.1     | 2026-01       | Supported               |
| Mender Server 4.0     | 2025-01       | Supported until 2026-08 |
| Mender 3.7 (bundle)   | 2024-05       | EOL (since 2025-05)     |

When a new LTS version is released for a component, the previous LTS
version is supported for at least 6 months.


## Yocto Project releases supported by meta-mender

The following [Yocto Project LTS releases](https://wiki.yoctoproject.org/wiki/Releases?target=_blank)
are currently supported by [meta-mender](https://github.com/mendersoftware/meta-mender?target=_blank):

* Scarthgap (5.0)
* Kirkstone (4.0)

Each Yocto Project release has a corresponding branch in meta-mender.
Note that you will find other branches in meta-mender but they are not
updated during a future Mender release.


## Zephyr Project releases supported by Mender MCU Client

The following [Zephyr Project
releases](https://github.com/zephyrproject-rtos/zephyr/releases) are currently
supported by the [Mender MCU Client](https://github.com/mendersoftware/mender-mcu):

<!--AUTOVERSION: "Zephyr %"/ignore "/v%"/ignore-->
* [Zephyr 4.2](https://github.com/zephyrproject-rtos/zephyr/releases/tag/v4.2.0)


## Debian family releases supported for Mender Client

The following Debian and Ubuntu LTS releases are currently supported for the Mender Client and
Mender Gateway through [Debian packages](../../12.Downloads/02.Device-components/docs.md):

| Distribution | Version  |
| ------------ | -------  |
| Debian       | Trixie   |
| Debian       | Bookworm |
| Ubuntu       | Noble    |
| Ubuntu       | Jammy    |


## Debian family and macOS releases supported for workstation tools

The following Debian and Ubuntu LTS releases are currently supported for Mender workstation tools
(mender-artifact and mender-cli) through [Debian packages](../../12.Downloads/01.Workstation-tools/docs.md):

| Distribution | Version  |
| ------------ | -------  |
| Debian       | Trixie   |
| Debian       | Bookworm |
| Ubuntu       | Noble    |
| Ubuntu       | Jammy    |

The workstation tools are also available for macOS through [Homebrew](https://brew.sh/?target=_blank).
Homebrew support is determined by the Homebrew project's own compatibility policies.


## Mender Artifact format support

The [Mender Artifact format](../../02.Overview/03.Artifact/docs.md) is versioned
to support new features over time. It is used by the Mender Client (to install Artifacts),
Mender Server (to parse and display meta-data, and to generate some types of Artifacts)
and the mender-artifact CLI utility (to create Artifacts).

| Artifact format | Client | Server | mender-artifact |
| --------------- | ------ | ------ | --------------- |
| Artifact v1     | 1.0    | 1.0    | 1.0             |
| Artifact v2     | 1.1    | 1.1    | 2.0             |
| Artifact v3     | 2.0    | 2.0    | 3.0             |

!!! Before you create Artifacts of a new format version, make sure that every Mender
component you use anywhere supports the version of the Artifact format.


## Device API version support

The compatibility between the Mender Server and Client is managed by the
[Device API](https://docs.mender.io/api/#device-apis?target=_blank#device-apis)
versions exposed by the Server and used by the Client.
If the Mender Server supports the API version of the Mender Client, they are compatible.

The higher version API contains a mix of old and new API endpoints. For endpoints which
have not changed in the new version, previous version ones are assumed. For example, if
the Device uses the v2 Device API, it expects
[this single v2 Deployments endpoint](https://docs.mender.io/api/?target=_blank#device-api-deployments-v2)
to be available. For all other endpoints it will use v1.

| Device API | Server | Gateway | Client |
| ---------- | ------ | ------- | ------ |
| API v1     | 1.0    | N/A     | 1.0    |
| API v2     | 3.0    | 1.0     | 3.0    |

!!! Make sure to upgrade the Server first to support a new API version. Next it is
!!! recommended to update any Gateway components and finally Client.

!!! So far, Mender Server supports all Device API versions ever released. In other words,
!!! a current Mender Server will still work with Mender Client v1.0. However, it is good practice
!!! and required for commercial support to regularly update all your Mender components to
!!! ensure they all run supported versions. This will prevent issues in the future.


## Mender Client
### Subcomponents
The Mender Client consists of several subcomponents. See the table below for a mapping
of which subcomponents are included in a given Mender Client version.

| Mender Client | → | mender-update | mender-auth | mender-connect | mender-monitor | mender-flash |
| ------------- | - |-------------- | ----------- | -------------- | -------------- | ------------ |
| 6.0           |   | 5.1           | 5.1         | 3.0            | 1.5            | 1.1          |
| 5.0           |   | 5.0           | 5.0         | 2.3            | 1.4            | 1.0          |

### Update Modules
The Mender Client consists of several Update Modules. See the table below for a mapping
of which Update Modules are included in a given Mender Client version.

| Mender Client | → | mender-configure | mender-binary-delta | single-file     | rootfs          | directory       | docker-compose  |
| ------------- | - | ---------------- | ------------------- | --------------- | --------------- | --------------- | --------------- |
| 6.0           |   | 1.1              | 1.5                 | 5.1<sup>1</sup> | 5.1<sup>1</sup> | 5.1<sup>1</sup> | 1.0             |
| 5.0           |   | 1.1              | 1.5                 | 5.0<sup>1</sup> | 5.0<sup>1</sup> | 5.0<sup>1</sup> | -               |

<sup>1</sup> Versioned and delivered with `mender-update`
