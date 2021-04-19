---
title: Release notes & changelog
taxonomy:
    category: docs
shortcode-core:
    active: false
---

## mender-binary-delta 1.2.1

_Released 04.16.2021_

### Changelogs

#### mender-binary-delta (1.2.1)

New changes in mender-binary-delta since 1.2.0:

* Remove harmless warning message about unhandled states.
* Fix failed rollback status when bootloader is the one to roll back.
* Detect mismatches between `mender_boot_part` and `RootfsPart(A|B)` variables.
* Fix integer overflow bug in the Artifact creation logic, where the
  `rootfs_image_checksum` would get truncated through the use of the 32-bit
  interface for JSON values in the JSON libary used.
  ([MEN-4516](https://tracker.mender.io/browse/MEN-4516))


## mender-convert 2.4.0

_Released 04.19.2021_

### Statistics

A total of 3340 lines added, 1222 removed (delta 2118)

| Developers with the most changesets | |
|---|---|
| Ole Petter Orhagen | 19 (50.0%) |
| Lluis Campos | 9 (23.7%) |
| Kristian Amlie | 8 (21.1%) |
| Fabio Tranchitella | 2 (5.3%) |

| Developers with the most changed lines | |
|---|---|
| Ole Petter Orhagen | 3240 (95.5%) |
| Lluis Campos | 84 (2.5%) |
| Kristian Amlie | 58 (1.7%) |
| Fabio Tranchitella | 12 (0.4%) |

| Developers with the most lines removed | |
|---|---|
| Kristian Amlie | 38 (3.1%) |

| Developers with the most signoffs (total 1) | |
|---|---|
| Lluis Campos | 1 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 38 (100.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 3394 (100.0%) |

| Employers with the most signoffs (total 1) | |
|---|---|
| Northern.tech | 1 (100.0%) |

| Employers with the most hackers (total 4) | |
|---|---|
| Northern.tech | 4 (100.0%) |

### Changelogs

#### mender-convert (2.4.0)

New changes in mender-convert since 2.3.0:

* Set mender-connect version to latest
  ([MEN-4200](https://tracker.mender.io/browse/MEN-4200))
* Support installing mender-configure addon. Not installed by
  default, it can be configured using MENDER_ADDON_CONFIGURE_INSTALL and
  MENDER_ADDON_CONFIGURE_VERSION variables.
  ([MEN-4422](https://tracker.mender.io/browse/MEN-4422))
* Set mender-configure version to master
  ([MEN-4422](https://tracker.mender.io/browse/MEN-4422))
* The standard RasperryPi configuration now comes with UBoot 2020.01 as
  the default. ([MEN-4395](https://tracker.mender.io/browse/MEN-4395))
* raspberrypi_config: Modify headless configuration services to
  expect boot partition in /uboot instead of /boot.
  ([MEN-4117](https://tracker.mender.io/browse/MEN-4117))
* [raspberrypi_config] Enable UART in U-Boot config.txt
  ([MEN-4567](https://tracker.mender.io/browse/MEN-4567))
* Update mender-artifact to 3.5.x.
* Switch to stable version of mender-configure.
* Always create symlinks from `/var/lib/mender-configure` to
  `/data/mender-configure`. They always need to installed in a
  rootfs-image prepared image, even if the software isn't, because if
  the package is installed later, the links must be present or it will
  act as if it is a non-rootfs image, and store the settings on the
  rootfs partition, when they should be stored on the data partition.


## Mender 2.7.0

_Released 04.16.2021_

### Statistics

A total of 54335 lines added, 26195 removed (delta 28140)

| Developers with the most changesets | |
|---|---|
| Manuel Zedel | 229 (30.0%) |
| Fabio Tranchitella | 127 (16.6%) |
| Alf-Rune Siqveland | 124 (16.2%) |
| Lluis Campos | 77 (10.1%) |
| Marcin Chalczynski | 75 (9.8%) |
| Krzysztof Jaskiewicz | 46 (6.0%) |
| Peter Grzybowski | 28 (3.7%) |
| Ole Petter Orhagen | 24 (3.1%) |
| Kristian Amlie | 23 (3.0%) |
| Michael Clelland | 8 (1.0%) |

| Developers with the most changed lines | |
|---|---|
| Alf-Rune Siqveland | 24379 (37.1%) |
| Fabio Tranchitella | 13130 (20.0%) |
| Manuel Zedel | 11624 (17.7%) |
| Peter Grzybowski | 4655 (7.1%) |
| Marcin Chalczynski | 4509 (6.9%) |
| Krzysztof Jaskiewicz | 3332 (5.1%) |
| Lluis Campos | 3023 (4.6%) |
| Ole Petter Orhagen | 636 (1.0%) |
| Kristian Amlie | 356 (0.5%) |
| Michael Clelland | 112 (0.2%) |

| Developers with the most signoffs (total 1) | |
|---|---|
| Lluis Campos | 1 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 643 (84.2%) |
| RnDity | 121 (15.8%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 57924 (88.1%) |
| RnDity | 7841 (11.9%) |

| Employers with the most signoffs (total 1) | |
|---|---|
| Northern.tech | 1 (100.0%) |

| Employers with the most hackers (total 13) | |
|---|---|
| Northern.tech | 11 (84.6%) |
| RnDity | 2 (15.4%) |

### Changelogs

#### auditlogs (1.1.0)

New changes in auditlogs since 1.0.0:

* Aggregated Dependabot Changelogs:
  * Bumps alpine from 3.12 to 3.13.0.
  * Bumps [github.com/stretchr/testify](https://github.com/stretchr/testify) from 1.6.1 to 1.7.0.
    - [Release notes](https://github.com/stretchr/testify/releases)
    - [Commits](https://github.com/stretchr/testify/compare/v1.6.1...v1.7.0)
  * Bumps golang from 1.14-alpine3.12 to 1.15.6-alpine3.12.
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.4 to 1.4.6.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.4...1.4.6)
  * Bumps golang from 1.15.6-alpine3.12 to 1.16.0-alpine3.12.
  * Bumps golang from 1.16.0-alpine3.12 to 1.16.2-alpine3.12.
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.6 to 1.5.0.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/1.4.6...v1.5.0)

#### create-artifact-worker (1.0.2)

New changes in create-artifact-worker since 1.0.1:

* bugfix to allow spaces in artifact names
  ([MEN-4179](https://tracker.mender.io/browse/MEN-4179))
* upgrade mender-artifact to version 3.5.0.
  This enables the create-artifact-worker to generate artifacts that
  implement the provides and clear provides fields.
  ([MEN-4409](https://tracker.mender.io/browse/MEN-4409))

#### deployments (2.3.0)

New changes in deployments since 2.2.0:

* New internal endpoint for creating configuration deployments
* extend get /deployment query params with optional deployment type
* New endpoint for generating configuration artifacts on the fly
* Handle configuration artifacts on /device/deployments/next
* Aggregated Dependabot Changelogs:
  * Bumps alpine from 3.12 to 3.13.0.
  * Bumps [github.com/stretchr/testify](https://github.com/stretchr/testify) from 1.6.1 to 1.7.0.
    - [Release notes](https://github.com/stretchr/testify/releases)
    - [Commits](https://github.com/stretchr/testify/compare/v1.6.1...v1.7.0)
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.36.24 to 1.36.28.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.36.24...v1.36.28)
  * Bumps [github.com/google/uuid](https://github.com/google/uuid) from 1.1.4 to 1.1.5.
    - [Release notes](https://github.com/google/uuid/releases)
    - [Commits](https://github.com/google/uuid/compare/v1.1.4...v1.1.5)
  * Bumps alpine from 3.13.0 to 3.13.1.
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.36.28 to 1.37.1.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.36.28...v1.37.1)
  * Bumps [github.com/google/uuid](https://github.com/google/uuid) from 1.1.5 to 1.2.0.
    - [Release notes](https://github.com/google/uuid/releases)
    - [Commits](https://github.com/google/uuid/compare/v1.1.5...v1.2.0)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.4 to 1.4.6.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.4...1.4.6)
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.37.1 to 1.37.10.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.37.1...v1.37.10)
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.37.10 to 1.37.20.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.37.10...v1.37.20)
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.37.20 to 1.37.25.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.37.20...v1.37.25)
  * Bumps [github.com/sirupsen/logrus](https://github.com/sirupsen/logrus) from 1.7.0 to 1.8.1.
    - [Release notes](https://github.com/sirupsen/logrus/releases)
    - [Changelog](https://github.com/sirupsen/logrus/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/sirupsen/logrus/compare/v1.7.0...v1.8.1)
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.37.25 to 1.37.30.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.37.25...v1.37.30)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.6 to 1.5.0.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/1.4.6...v1.5.0)

#### deployments-enterprise (2.3.0)

New changes in deployments-enterprise since 2.2.0:

* New internal endpoint for creating configuration deployments
* extend get /deployment query params with optional deployment type
* New endpoint for generating configuration artifacts on the fly
* Handle configuration artifacts on /device/deployments/next
* FIX: Phased deployments getting stuck on retries
* Fix: do not increment attempts on multiple subsequent failure status reports
* docs: Fix naming conflict in v1 and v2 NewDeployment definitions.
* docs: Document missing parameters for NewDeploymentForGroup schema.
* Aggregated Dependabot Changelogs:
  * Bumps alpine from 3.12 to 3.13.0.
  * Bumps alpine from 3.12 to 3.13.0.
  * Bumps [github.com/stretchr/testify](https://github.com/stretchr/testify) from 1.6.1 to 1.7.0.
    - [Release notes](https://github.com/stretchr/testify/releases)
    - [Commits](https://github.com/stretchr/testify/compare/v1.6.1...v1.7.0)
  * Bumps [github.com/stretchr/testify](https://github.com/stretchr/testify) from 1.6.1 to 1.7.0.
    - [Release notes](https://github.com/stretchr/testify/releases)
    - [Commits](https://github.com/stretchr/testify/compare/v1.6.1...v1.7.0)
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.36.24 to 1.36.28.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.36.24...v1.36.28)
  * Bumps [github.com/google/uuid](https://github.com/google/uuid) from 1.1.4 to 1.1.5.
    - [Release notes](https://github.com/google/uuid/releases)
    - [Commits](https://github.com/google/uuid/compare/v1.1.4...v1.1.5)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.4 to 1.4.5.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.4...v1.4.5)
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.36.23 to 1.36.28.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.36.23...v1.36.28)
  * Bumps alpine from 3.13.0 to 3.13.1.
  * Bumps alpine from 3.13.0 to 3.13.1.
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.36.28 to 1.37.1.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.36.28...v1.37.1)
  * Bumps [github.com/google/uuid](https://github.com/google/uuid) from 1.1.5 to 1.2.0.
    - [Release notes](https://github.com/google/uuid/releases)
    - [Commits](https://github.com/google/uuid/compare/v1.1.5...v1.2.0)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.5 to 1.4.6.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.5...1.4.6)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.4 to 1.4.6.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.4...1.4.6)
  * Bumps [github.com/google/uuid](https://github.com/google/uuid) from 1.1.5 to 1.2.0.
    - [Release notes](https://github.com/google/uuid/releases)
    - [Commits](https://github.com/google/uuid/compare/v1.1.5...v1.2.0)
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.36.28 to 1.37.7.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.36.28...v1.37.7)
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.37.1 to 1.37.10.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.37.1...v1.37.10)
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.37.7 to 1.37.10.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.37.7...v1.37.10)
  * Bumps alpine from 3.13.1 to 3.13.2.
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.37.10 to 1.37.20.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.37.10...v1.37.20)
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.37.10 to 1.37.20.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.37.10...v1.37.20)
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.37.20 to 1.37.25.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.37.20...v1.37.25)
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.37.20 to 1.37.25.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.37.20...v1.37.25)
  * Bumps [github.com/sirupsen/logrus](https://github.com/sirupsen/logrus) from 1.7.0 to 1.8.1.
    - [Release notes](https://github.com/sirupsen/logrus/releases)
    - [Changelog](https://github.com/sirupsen/logrus/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/sirupsen/logrus/compare/v1.7.0...v1.8.1)
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.37.25 to 1.37.30.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.37.25...v1.37.30)
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.37.25 to 1.37.30.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.37.25...v1.37.30)
  * Bumps [github.com/sirupsen/logrus](https://github.com/sirupsen/logrus) from 1.7.0 to 1.8.1.
    - [Release notes](https://github.com/sirupsen/logrus/releases)
    - [Changelog](https://github.com/sirupsen/logrus/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/sirupsen/logrus/compare/v1.7.0...v1.8.1)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.6 to 1.5.0.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/1.4.6...v1.5.0)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.6 to 1.5.0.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/1.4.6...v1.5.0)

#### deviceauth (2.6.0)

New changes in deviceauth since 2.5.0:

* Enable support for using the service with Traefik.
* Aggregated Dependabot Changelogs:
  * Bumps alpine from 3.12 to 3.13.0.
  * Bumps [github.com/stretchr/testify](https://github.com/stretchr/testify) from 1.6.1 to 1.7.0.
    - [Release notes](https://github.com/stretchr/testify/releases)
    - [Commits](https://github.com/stretchr/testify/compare/v1.6.1...v1.7.0)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.4 to 1.4.5.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.4...v1.4.5)
  * Bumps golang from 1.14-alpine3.12 to 1.15.7-alpine3.12.
  * Bumps [github.com/go-redis/redis/v8](https://github.com/go-redis/redis) from 8.4.8 to 8.4.10.
    - [Release notes](https://github.com/go-redis/redis/releases)
    - [Changelog](https://github.com/go-redis/redis/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/go-redis/redis/compare/v8.4.8...v8.4.10)
  * Bumps alpine from 3.13.0 to 3.13.1.
  * Bumps golang from 1.15.7-alpine3.12 to 1.15.8-alpine3.12.
  * Bumps [github.com/go-redis/redis/v8](https://github.com/go-redis/redis) from 8.4.10 to 8.5.0.
    - [Release notes](https://github.com/go-redis/redis/releases)
    - [Changelog](https://github.com/go-redis/redis/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/go-redis/redis/compare/v8.4.10...v8.5.0)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.5 to 1.4.6.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.5...1.4.6)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.6 to 1.5.0.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/1.4.6...v1.5.0)
  * Bumps [github.com/go-redis/redis/v8](https://github.com/go-redis/redis) from 8.5.0 to 8.7.1.
    - [Release notes](https://github.com/go-redis/redis/releases)
    - [Changelog](https://github.com/go-redis/redis/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/go-redis/redis/compare/v8.5.0...v8.7.1)

#### deviceconfig (1.0.0)

* First release of deviceconfig

#### deviceconnect (1.1.0)

New changes in deviceconnect since 1.0.0:

* New API end-points to trigger check-update and send-inventory on device
* New internal API end-points to trigger check-update and send-inventory
* , implement file upload and download end-points
  ([MEN-4418](https://tracker.mender.io/browse/MEN-4418), [MEN-4482](https://tracker.mender.io/browse/MEN-4482))
* Aggregated Dependabot Changelogs:
  * Bumps alpine from 3.12 to 3.13.0.
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.4 to 1.4.6.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.4...1.4.6)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.6 to 1.5.0.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/1.4.6...v1.5.0)

#### gui (2.7.0)

New changes in gui since 2.6.0:

* Rename Retry deployment to Recreate deployment.
* fix page number on rowsPerPage change
  ([MEN-4364](https://tracker.mender.io/browse/MEN-4364))
* fixed an issue that prevented existing user roles from being removed
* fixed an issue that prevented loading dynamic group devices when navigating to device groups
* fixed an issue that prevented the deployment attempt count from being shown in the deployment report
  ([MEN-4399](https://tracker.mender.io/browse/MEN-4399))
* added single device configuration editor
* fixed onboarding tips dismissal not being saved right away
* switched auditlogs to drawer interaction for details
  ([MEN-4313](https://tracker.mender.io/browse/MEN-4313))
* onboarding: Pass `--demo` flag to `get.mender.io` script.
  ([MEN-4461](https://tracker.mender.io/browse/MEN-4461))
* extend RBAC with "Deployments Manager" role
* added user verification requirement for 2fa activation
  ([MEN-4484](https://tracker.mender.io/browse/MEN-4484))
* improved deployment creation for large device fleets
* fixed an error that prevented deployment timeframe selection
* prevented enter press on 2fa code entry causing a redirect
* Aggregated Dependabot Changelogs:
  * Bumps [@testing-library/dom](https://github.com/testing-library/dom-testing-library) from 7.29.2 to 7.29.4.
    - [Release notes](https://github.com/testing-library/dom-testing-library/releases)
    - [Changelog](https://github.com/testing-library/dom-testing-library/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/testing-library/dom-testing-library/compare/v7.29.2...v7.29.4)
  * Bumps [webpack](https://github.com/webpack/webpack) from 5.12.3 to 5.15.0.
    - [Release notes](https://github.com/webpack/webpack/releases)
    - [Commits](https://github.com/webpack/webpack/compare/v5.12.3...v5.15.0)
  * Bumps [@stripe/react-stripe-js](https://github.com/stripe/react-stripe-js) from 1.1.2 to 1.2.0.
    - [Release notes](https://github.com/stripe/react-stripe-js/releases)
    - [Changelog](https://github.com/stripe/react-stripe-js/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/stripe/react-stripe-js/compare/v1.1.2...v1.2.0)
  * Bumps [mini-css-extract-plugin](https://github.com/webpack-contrib/mini-css-extract-plugin) from 1.3.3 to 1.3.4.
    - [Release notes](https://github.com/webpack-contrib/mini-css-extract-plugin/releases)
    - [Changelog](https://github.com/webpack-contrib/mini-css-extract-plugin/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/mini-css-extract-plugin/compare/v1.3.3...v1.3.4)
  * Bumps [cypress-localstorage-commands](https://github.com/javierbrea/cypress-localstorage-commands) from 1.3.1 to 1.4.0.
    - [Release notes](https://github.com/javierbrea/cypress-localstorage-commands/releases)
    - [Changelog](https://github.com/javierbrea/cypress-localstorage-commands/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/javierbrea/cypress-localstorage-commands/compare/v1.3.1...v1.4.0)
  * Bumps [@cypress/skip-test](https://github.com/cypress-io/cypress-skip-test) from 2.5.1 to 2.6.0.
    - [Release notes](https://github.com/cypress-io/cypress-skip-test/releases)
    - [Commits](https://github.com/cypress-io/cypress-skip-test/compare/v2.5.1...v2.6.0)
  * Bumps [generate-password](https://github.com/brendanashworth/generate-password) from 1.5.1 to 1.6.0.
    - [Release notes](https://github.com/brendanashworth/generate-password/releases)
    - [Changelog](https://github.com/brendanashworth/generate-password/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/brendanashworth/generate-password/commits)
  * Bumps [eslint](https://github.com/eslint/eslint) from 7.17.0 to 7.18.0.
    - [Release notes](https://github.com/eslint/eslint/releases)
    - [Changelog](https://github.com/eslint/eslint/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/eslint/eslint/compare/v7.17.0...v7.18.0)
  * Bumps [husky](https://github.com/typicode/husky) from 4.3.7 to 4.3.8.
    - [Release notes](https://github.com/typicode/husky/releases)
    - [Commits](https://github.com/typicode/husky/compare/v4.3.7...v4.3.8)
  * Bumps [react-copy-to-clipboard](https://github.com/nkbt/react-copy-to-clipboard) from 5.0.2 to 5.0.3.
    - [Release notes](https://github.com/nkbt/react-copy-to-clipboard/releases)
    - [Commits](https://github.com/nkbt/react-copy-to-clipboard/compare/v5.0.2...v5.0.3)
  * Bumps [@testing-library/jest-dom](https://github.com/testing-library/jest-dom) from 5.11.8 to 5.11.9.
    - [Release notes](https://github.com/testing-library/jest-dom/releases)
    - [Changelog](https://github.com/testing-library/jest-dom/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/testing-library/jest-dom/compare/v5.11.8...v5.11.9)
  * Bumps [core-js](https://github.com/zloirock/core-js) from 3.8.2 to 3.8.3.
    - [Release notes](https://github.com/zloirock/core-js/releases)
    - [Changelog](https://github.com/zloirock/core-js/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/zloirock/core-js/compare/v3.8.2...v3.8.3)
  * Bumps [react-idle-timer](https://github.com/supremetechnopriest/react-idle-timer) from 4.5.1 to 4.5.2.
    - [Release notes](https://github.com/supremetechnopriest/react-idle-timer/releases)
    - [Changelog](https://github.com/SupremeTechnopriest/react-idle-timer/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/supremetechnopriest/react-idle-timer/compare/4.5.1...4.5.2)
  * Bumps [@mdi/js](https://github.com/Templarian/MaterialDesign-JS) from 5.8.55 to 5.9.55.
    - [Release notes](https://github.com/Templarian/MaterialDesign-JS/releases)
    - [Commits](https://github.com/Templarian/MaterialDesign-JS/compare/v5.8.55...v5.9.55)
  * Bumps [webpack](https://github.com/webpack/webpack) from 5.15.0 to 5.17.0.
    - [Release notes](https://github.com/webpack/webpack/releases)
    - [Commits](https://github.com/webpack/webpack/compare/v5.15.0...v5.17.0)
  * Bumps node from 15.5.1-alpine to 15.6.0-alpine.
  * Bumps [dayjs](https://github.com/iamkun/dayjs) from 1.10.3 to 1.10.4.
    - [Release notes](https://github.com/iamkun/dayjs/releases)
    - [Changelog](https://github.com/iamkun/dayjs/blob/v1.10.4/CHANGELOG.md)
    - [Commits](https://github.com/iamkun/dayjs/compare/v1.10.3...v1.10.4)
  * Bumps [cypress](https://github.com/cypress-io/cypress) from 6.2.1 to 6.3.0.
    - [Release notes](https://github.com/cypress-io/cypress/releases)
    - [Changelog](https://github.com/cypress-io/cypress/blob/develop/.releaserc.base.js)
    - [Commits](https://github.com/cypress-io/cypress/compare/v6.2.1...v6.3.0)
  * Bumps [cypress-image-snapshot](https://github.com/palmerhq/cypress-image-snapshot) from 4.0.0 to 4.0.1.
    - [Release notes](https://github.com/palmerhq/cypress-image-snapshot/releases)
    - [Changelog](https://github.com/jaredpalmer/cypress-image-snapshot/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/palmerhq/cypress-image-snapshot/compare/v4.0.0...v4.0.1)
  * Bumps cypress/included from 6.2.1 to 6.3.0.
  * Bumps [autoprefixer](https://github.com/postcss/autoprefixer) from 10.2.1 to 10.2.3.
    - [Release notes](https://github.com/postcss/autoprefixer/releases)
    - [Changelog](https://github.com/postcss/autoprefixer/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/postcss/autoprefixer/compare/10.2.1...10.2.3)
  * Bumps [@testing-library/user-event](https://github.com/testing-library/user-event) from 12.6.0 to 12.6.2.
    - [Release notes](https://github.com/testing-library/user-event/releases)
    - [Changelog](https://github.com/testing-library/user-event/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/testing-library/user-event/compare/v12.6.0...v12.6.2)
  * Bumps [cypress-file-upload](https://github.com/abramenal/cypress-file-upload) from 4.1.1 to 5.0.2.
    - [Release notes](https://github.com/abramenal/cypress-file-upload/releases)
    - [Commits](https://github.com/abramenal/cypress-file-upload/compare/v4.1.1...v5.0.2)
  * Bumps [webpack-cli](https://github.com/webpack/webpack-cli) from 4.3.1 to 4.4.0.
    - [Release notes](https://github.com/webpack/webpack-cli/releases)
    - [Changelog](https://github.com/webpack/webpack-cli/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack/webpack-cli/compare/webpack-cli@4.3.1...webpack-cli@4.4.0)
  * Bumps [postcss-loader](https://github.com/webpack-contrib/postcss-loader) from 4.1.0 to 4.2.0.
    - [Release notes](https://github.com/webpack-contrib/postcss-loader/releases)
    - [Changelog](https://github.com/webpack-contrib/postcss-loader/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/postcss-loader/compare/v4.1.0...v4.2.0)
  * Bumps node from 15.6.0-alpine to 15.7.0-alpine.
  * Bumps [eslint](https://github.com/eslint/eslint) from 7.18.0 to 7.19.0.
    - [Release notes](https://github.com/eslint/eslint/releases)
    - [Changelog](https://github.com/eslint/eslint/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/eslint/eslint/compare/v7.18.0...v7.19.0)
  * Bumps [less](https://github.com/less/less.js) from 4.1.0 to 4.1.1.
    - [Release notes](https://github.com/less/less.js/releases)
    - [Changelog](https://github.com/less/less.js/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/less/less.js/compare/v4.1.0...v4.1.1)
  * Bumps [webpack](https://github.com/webpack/webpack) from 5.17.0 to 5.19.0.
    - [Release notes](https://github.com/webpack/webpack/releases)
    - [Commits](https://github.com/webpack/webpack/compare/v5.17.0...v5.19.0)
  * Bumps [xterm-addon-search](https://github.com/xtermjs/xterm.js) from 0.7.0 to 0.8.0.
    - [Release notes](https://github.com/xtermjs/xterm.js/releases)
    - [Commits](https://github.com/xtermjs/xterm.js/compare/0.7...0.8)
  * Bumps [react-big-calendar](https://github.com/jquense/react-big-calendar) from 0.30.0 to 0.31.0.
    - [Release notes](https://github.com/jquense/react-big-calendar/releases)
    - [Changelog](https://github.com/jquense/react-big-calendar/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/jquense/react-big-calendar/compare/v0.30.0...v0.31.0)
  * Bumps [xterm-addon-fit](https://github.com/xtermjs/xterm.js) from 0.4.0 to 0.5.0.
    - [Release notes](https://github.com/xtermjs/xterm.js/releases)
    - [Commits](https://github.com/xtermjs/xterm.js/compare/0.4...0.5)
  * Bumps [autoprefixer](https://github.com/postcss/autoprefixer) from 10.2.3 to 10.2.4.
    - [Release notes](https://github.com/postcss/autoprefixer/releases)
    - [Changelog](https://github.com/postcss/autoprefixer/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/postcss/autoprefixer/compare/10.2.3...10.2.4)
  * Bumps [mini-css-extract-plugin](https://github.com/webpack-contrib/mini-css-extract-plugin) from 1.3.4 to 1.3.5.
    - [Release notes](https://github.com/webpack-contrib/mini-css-extract-plugin/releases)
    - [Changelog](https://github.com/webpack-contrib/mini-css-extract-plugin/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/mini-css-extract-plugin/compare/v1.3.4...v1.3.5)
  * Bumps [@stripe/react-stripe-js](https://github.com/stripe/react-stripe-js) from 1.2.0 to 1.2.1.
    - [Release notes](https://github.com/stripe/react-stripe-js/releases)
    - [Changelog](https://github.com/stripe/react-stripe-js/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/stripe/react-stripe-js/compare/v1.2.0...v1.2.1)
  * Bumps [msw](https://github.com/mswjs/msw) from 0.25.0 to 0.26.0.
    - [Release notes](https://github.com/mswjs/msw/releases)
    - [Changelog](https://github.com/mswjs/msw/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/mswjs/msw/compare/v0.25.0...v0.26.0)
  * Bumps [victory](https://github.com/formidablelabs/victory) from 35.4.6 to 35.4.8.
    - [Release notes](https://github.com/formidablelabs/victory/releases)
    - [Changelog](https://github.com/FormidableLabs/victory/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/formidablelabs/victory/compare/v35.4.6...v35.4.8)
  * Bumps [msw](https://github.com/mswjs/msw) from 0.26.0 to 0.26.1.
    - [Release notes](https://github.com/mswjs/msw/releases)
    - [Changelog](https://github.com/mswjs/msw/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/mswjs/msw/compare/v0.26.0...v0.26.1)
  * Bumps [@testing-library/user-event](https://github.com/testing-library/user-event) from 12.6.3 to 12.7.0.
    - [Release notes](https://github.com/testing-library/user-event/releases)
    - [Changelog](https://github.com/testing-library/user-event/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/testing-library/user-event/compare/v12.6.3...v12.7.0)
  * Bumps [msgpack5](https://github.com/mcollina/msgpack5) from 5.0.0 to 5.1.0.
    - [Release notes](https://github.com/mcollina/msgpack5/releases)
    - [Commits](https://github.com/mcollina/msgpack5/compare/v5.0.0...v5.1.0)
  * Bumps [eslint](https://github.com/eslint/eslint) from 7.19.0 to 7.20.0.
    - [Release notes](https://github.com/eslint/eslint/releases)
    - [Changelog](https://github.com/eslint/eslint/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/eslint/eslint/compare/v7.19.0...v7.20.0)
  * Bumps [@babel/core](https://github.com/babel/babel/tree/HEAD/packages/babel-core) from 7.12.13 to 7.12.16.
    - [Release notes](https://github.com/babel/babel/releases)
    - [Changelog](https://github.com/babel/babel/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel/commits/v7.12.16/packages/babel-core)
  * Bumps [@babel/preset-env](https://github.com/babel/babel/tree/HEAD/packages/babel-preset-env) from 7.12.13 to 7.12.16.
    - [Release notes](https://github.com/babel/babel/releases)
    - [Changelog](https://github.com/babel/babel/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel/commits/v7.12.16/packages/babel-preset-env)
  * Bumps [@testing-library/user-event](https://github.com/testing-library/user-event) from 12.7.0 to 12.7.1.
    - [Release notes](https://github.com/testing-library/user-event/releases)
    - [Changelog](https://github.com/testing-library/user-event/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/testing-library/user-event/compare/v12.7.0...v12.7.1)
  * Bumps [html-webpack-plugin](https://github.com/jantimon/html-webpack-plugin) from 5.0.0 to 5.1.0.
    - [Release notes](https://github.com/jantimon/html-webpack-plugin/releases)
    - [Changelog](https://github.com/jantimon/html-webpack-plugin/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/jantimon/html-webpack-plugin/compare/v5.0.0...v5.1.0)
  * Bumps [react-big-calendar](https://github.com/jquense/react-big-calendar) from 0.31.0 to 0.32.0.
    - [Release notes](https://github.com/jquense/react-big-calendar/releases)
    - [Changelog](https://github.com/jquense/react-big-calendar/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/jquense/react-big-calendar/compare/v0.31.0...v0.32.0)
  * Bumps [victory](https://github.com/formidablelabs/victory) from 35.4.8 to 35.4.9.
    - [Release notes](https://github.com/formidablelabs/victory/releases)
    - [Changelog](https://github.com/FormidableLabs/victory/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/formidablelabs/victory/compare/v35.4.8...v35.4.9)
  * Bumps [esbuild-loader](https://github.com/privatenumber/esbuild-loader) from 2.9.1 to 2.9.2.
    - [Release notes](https://github.com/privatenumber/esbuild-loader/releases)
    - [Commits](https://github.com/privatenumber/esbuild-loader/compare/v2.9.1...v2.9.2)
  * Bumps cypress/included from 6.4.0 to 6.5.0.
  * Bumps [@babel/plugin-transform-runtime](https://github.com/babel/babel/tree/HEAD/packages/babel-plugin-transform-runtime) from 7.12.15 to 7.13.9.
    - [Release notes](https://github.com/babel/babel/releases)
    - [Changelog](https://github.com/babel/babel/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel/commits/v7.13.9/packages/babel-plugin-transform-runtime)
  * Bumps [@stripe/stripe-js](https://github.com/stripe/stripe-js) from 1.12.1 to 1.13.1.
    - [Release notes](https://github.com/stripe/stripe-js/releases)
    - [Commits](https://github.com/stripe/stripe-js/compare/v1.12.1...v1.13.1)
  * Bumps [elliptic](https://github.com/indutny/elliptic) from 6.5.3 to 6.5.4.
    - [Release notes](https://github.com/indutny/elliptic/releases)
    - [Commits](https://github.com/indutny/elliptic/compare/v6.5.3...v6.5.4)
  * Bumps [react-idle-timer](https://github.com/supremetechnopriest/react-idle-timer) from 4.5.5 to 4.5.6.
    - [Release notes](https://github.com/supremetechnopriest/react-idle-timer/releases)
    - [Changelog](https://github.com/SupremeTechnopriest/react-idle-timer/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/supremetechnopriest/react-idle-timer/compare/4.5.5...4.5.6)
  * Bumps [eslint](https://github.com/eslint/eslint) from 7.21.0 to 7.22.0.
    - [Release notes](https://github.com/eslint/eslint/releases)
    - [Changelog](https://github.com/eslint/eslint/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/eslint/eslint/compare/v7.21.0...v7.22.0)
  * Bumps [@testing-library/user-event](https://github.com/testing-library/user-event) from 12.8.1 to 12.8.3.
    - [Release notes](https://github.com/testing-library/user-event/releases)
    - [Changelog](https://github.com/testing-library/user-event/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/testing-library/user-event/compare/v12.8.1...v12.8.3)
  * Bumps [webpack](https://github.com/webpack/webpack) from 5.24.3 to 5.25.1.
    - [Release notes](https://github.com/webpack/webpack/releases)
    - [Commits](https://github.com/webpack/webpack/compare/v5.24.3...v5.25.1)
  * Bumps [@babel/preset-env](https://github.com/babel/babel/tree/HEAD/packages/babel-preset-env) from 7.13.9 to 7.13.10.
    - [Release notes](https://github.com/babel/babel/releases)
    - [Changelog](https://github.com/babel/babel/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel/commits/v7.13.10/packages/babel-preset-env)
  * Bumps nginx from 1.19.7-alpine to 1.19.8-alpine.
  * Bumps [@material-ui/pickers](https://github.com/mui-org/material-ui-pickers) from 3.2.10 to 3.3.10.
    - [Release notes](https://github.com/mui-org/material-ui-pickers/releases)
    - [Changelog](https://github.com/mui-org/material-ui-pickers/blob/next/CHANGELOG.md)
    - [Commits](https://github.com/mui-org/material-ui-pickers/compare/v3.2.10...v3.3.10)
  * Bumps [msw](https://github.com/mswjs/msw) from 0.27.0 to 0.27.1.
    - [Release notes](https://github.com/mswjs/msw/releases)
    - [Changelog](https://github.com/mswjs/msw/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/mswjs/msw/compare/v0.27.0...v0.27.1)
  * Bumps [@babel/core](https://github.com/babel/babel/tree/HEAD/packages/babel-core) from 7.13.8 to 7.13.10.
    - [Release notes](https://github.com/babel/babel/releases)
    - [Changelog](https://github.com/babel/babel/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel/commits/v7.13.10/packages/babel-core)
  * Bumps [postcss](https://github.com/postcss/postcss) from 8.2.7 to 8.2.8.
    - [Release notes](https://github.com/postcss/postcss/releases)
    - [Changelog](https://github.com/postcss/postcss/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/postcss/postcss/compare/8.2.7...8.2.8)
  * Bumps [esbuild-loader](https://github.com/privatenumber/esbuild-loader) from 2.9.2 to 2.10.0.
    - [Release notes](https://github.com/privatenumber/esbuild-loader/releases)
    - [Commits](https://github.com/privatenumber/esbuild-loader/compare/v2.9.2...v2.10.0)
  * Bumps [@babel/plugin-transform-runtime](https://github.com/babel/babel/tree/HEAD/packages/babel-plugin-transform-runtime) from 7.13.9 to 7.13.10.
    - [Release notes](https://github.com/babel/babel/releases)
    - [Changelog](https://github.com/babel/babel/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel/commits/v7.13.10/packages/babel-plugin-transform-runtime)
  * Bumps [html-webpack-plugin](https://github.com/jantimon/html-webpack-plugin) from 5.3.0 to 5.3.1.
    - [Release notes](https://github.com/jantimon/html-webpack-plugin/releases)
    - [Changelog](https://github.com/jantimon/html-webpack-plugin/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/jantimon/html-webpack-plugin/compare/v5.3.0...v5.3.1)
  * Bumps [webpack](https://github.com/webpack/webpack) from 5.25.1 to 5.26.0.
    - [Release notes](https://github.com/webpack/webpack/releases)
    - [Commits](https://github.com/webpack/webpack/compare/v5.25.1...v5.26.0)
  * Bumps [css-loader](https://github.com/webpack-contrib/css-loader) from 5.1.1 to 5.1.3.
    - [Release notes](https://github.com/webpack-contrib/css-loader/releases)
    - [Changelog](https://github.com/webpack-contrib/css-loader/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/css-loader/compare/v5.1.1...v5.1.3)
  * Bumps [jest](https://github.com/facebook/jest) from 27.0.0-next.4 to 27.0.0-next.5.
    - [Release notes](https://github.com/facebook/jest/releases)
    - [Changelog](https://github.com/facebook/jest/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/facebook/jest/compare/v27.0.0-next.4...v27.0.0-next.5)
  * Bumps [xterm](https://github.com/xtermjs/xterm.js) from 4.10.0 to 4.11.0.
    - [Release notes](https://github.com/xtermjs/xterm.js/releases)
    - [Commits](https://github.com/xtermjs/xterm.js/compare/4.10.0...4.11.0)
  * Bumps [postcss-loader](https://github.com/webpack-contrib/postcss-loader) from 5.1.0 to 5.2.0.
    - [Release notes](https://github.com/webpack-contrib/postcss-loader/releases)
    - [Changelog](https://github.com/webpack-contrib/postcss-loader/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/postcss-loader/compare/v5.1.0...v5.2.0)
  * Bumps [victory](https://github.com/formidablelabs/victory) from 35.4.11 to 35.4.12.
    - [Release notes](https://github.com/formidablelabs/victory/releases)
    - [Changelog](https://github.com/FormidableLabs/victory/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/formidablelabs/victory/compare/v35.4.11...v35.4.12)
  * Bumps [@testing-library/user-event](https://github.com/testing-library/user-event) from 12.8.3 to 13.0.6.
    - [Release notes](https://github.com/testing-library/user-event/releases)
    - [Changelog](https://github.com/testing-library/user-event/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/testing-library/user-event/compare/v12.8.3...v13.0.6)
  * Bumps [husky](https://github.com/typicode/husky) from 5.1.3 to 5.2.0.
    - [Release notes](https://github.com/typicode/husky/releases)
    - [Commits](https://github.com/typicode/husky/compare/v5.1.3...v5.2.0)
  * Bumps [webpack](https://github.com/webpack/webpack) from 5.26.0 to 5.27.1.
    - [Release notes](https://github.com/webpack/webpack/releases)
    - [Commits](https://github.com/webpack/webpack/compare/v5.26.0...v5.27.1)
  * Bumps node from 15.11.0-alpine to 15.12.0-alpine.
  * Bumps [cypress-file-upload](https://github.com/abramenal/cypress-file-upload) from 5.0.2 to 5.0.3.
    - [Release notes](https://github.com/abramenal/cypress-file-upload/releases)
    - [Commits](https://github.com/abramenal/cypress-file-upload/compare/v5.0.2...v5.0.3)
  * Bumps [@testing-library/user-event](https://github.com/testing-library/user-event) from 13.0.6 to 13.0.7.
    - [Release notes](https://github.com/testing-library/user-event/releases)
    - [Changelog](https://github.com/testing-library/user-event/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/testing-library/user-event/compare/v13.0.6...v13.0.7)
  * Bumps [@testing-library/jest-dom](https://github.com/testing-library/jest-dom) from 5.11.9 to 5.11.10.
    - [Release notes](https://github.com/testing-library/jest-dom/releases)
    - [Changelog](https://github.com/testing-library/jest-dom/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/testing-library/jest-dom/compare/v5.11.9...v5.11.10)
  * Bumps [@babel/preset-env](https://github.com/babel/babel/tree/HEAD/packages/babel-preset-env) from 7.13.10 to 7.13.12.
    - [Release notes](https://github.com/babel/babel/releases)
    - [Changelog](https://github.com/babel/babel/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel/commits/v7.13.12/packages/babel-preset-env)
  * Bumps [esbuild-loader](https://github.com/privatenumber/esbuild-loader) from 2.10.0 to 2.11.0.
    - [Release notes](https://github.com/privatenumber/esbuild-loader/releases)
    - [Commits](https://github.com/privatenumber/esbuild-loader/compare/v2.10.0...v2.11.0)
  * Bumps [msw](https://github.com/mswjs/msw) from 0.27.1 to 0.28.0.
    - [Release notes](https://github.com/mswjs/msw/releases)
    - [Changelog](https://github.com/mswjs/msw/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/mswjs/msw/compare/v0.27.1...v0.28.0)
  * Bumps [msgpack5](https://github.com/mcollina/msgpack5) from 5.3.1 to 5.3.2.
    - [Release notes](https://github.com/mcollina/msgpack5/releases)
    - [Commits](https://github.com/mcollina/msgpack5/compare/v5.3.1...v5.3.2)
  * Bumps [react-redux](https://github.com/reduxjs/react-redux) from 7.2.2 to 7.2.3.
    - [Release notes](https://github.com/reduxjs/react-redux/releases)
    - [Changelog](https://github.com/reduxjs/react-redux/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/reduxjs/react-redux/compare/v7.2.2...v7.2.3)
  * Bumps [webpack-cli](https://github.com/webpack/webpack-cli) from 4.5.0 to 4.6.0.
    - [Release notes](https://github.com/webpack/webpack-cli/releases)
    - [Changelog](https://github.com/webpack/webpack-cli/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack/webpack-cli/compare/webpack-cli@4.5.0...webpack-cli@4.6.0)
  * Bumps [@testing-library/user-event](https://github.com/testing-library/user-event) from 13.0.7 to 13.0.16.
    - [Release notes](https://github.com/testing-library/user-event/releases)
    - [Changelog](https://github.com/testing-library/user-event/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/testing-library/user-event/compare/v13.0.7...v13.0.16)
  * Bumps [eslint](https://github.com/eslint/eslint) from 7.22.0 to 7.23.0.
    - [Release notes](https://github.com/eslint/eslint/releases)
    - [Changelog](https://github.com/eslint/eslint/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/eslint/eslint/compare/v7.22.0...v7.23.0)
  * Bumps [@babel/core](https://github.com/babel/babel/tree/HEAD/packages/babel-core) from 7.13.10 to 7.13.13.
    - [Release notes](https://github.com/babel/babel/releases)
    - [Changelog](https://github.com/babel/babel/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel/commits/v7.13.13/packages/babel-core)
  * Bumps [@stripe/stripe-js](https://github.com/stripe/stripe-js) from 1.13.1 to 1.13.2.
    - [Release notes](https://github.com/stripe/stripe-js/releases)
    - [Commits](https://github.com/stripe/stripe-js/compare/v1.13.1...v1.13.2)
  * Bumps [mini-css-extract-plugin](https://github.com/webpack-contrib/mini-css-extract-plugin) from 1.3.9 to 1.4.0.
    - [Release notes](https://github.com/webpack-contrib/mini-css-extract-plugin/releases)
    - [Changelog](https://github.com/webpack-contrib/mini-css-extract-plugin/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/mini-css-extract-plugin/compare/v1.3.9...v1.4.0)
  * Bumps [eslint-plugin-react](https://github.com/yannickcr/eslint-plugin-react) from 7.22.0 to 7.23.1.
    - [Release notes](https://github.com/yannickcr/eslint-plugin-react/releases)
    - [Changelog](https://github.com/yannickcr/eslint-plugin-react/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/yannickcr/eslint-plugin-react/compare/v7.22.0...v7.23.1)
  * Bumps [@testing-library/dom](https://github.com/testing-library/dom-testing-library) from 7.30.0 to 7.30.1.
    - [Release notes](https://github.com/testing-library/dom-testing-library/releases)
    - [Changelog](https://github.com/testing-library/dom-testing-library/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/testing-library/dom-testing-library/compare/v7.30.0...v7.30.1)
  * Bumps [react-dropzone](https://github.com/react-dropzone/react-dropzone) from 11.3.1 to 11.3.2.
    - [Release notes](https://github.com/react-dropzone/react-dropzone/releases)
    - [Commits](https://github.com/react-dropzone/react-dropzone/compare/v11.3.1...v11.3.2)
  * Bumps [css-loader](https://github.com/webpack-contrib/css-loader) from 5.1.3 to 5.2.0.
    - [Release notes](https://github.com/webpack-contrib/css-loader/releases)
    - [Changelog](https://github.com/webpack-contrib/css-loader/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/css-loader/compare/v5.1.3...v5.2.0)
  * Bumps [husky](https://github.com/typicode/husky) from 5.2.0 to 6.0.0.
    - [Release notes](https://github.com/typicode/husky/releases)
    - [Commits](https://github.com/typicode/husky/compare/v5.2.0...v6.0.0)
  * Bumps [webpack](https://github.com/webpack/webpack) from 5.27.1 to 5.28.0.
    - [Release notes](https://github.com/webpack/webpack/releases)
    - [Commits](https://github.com/webpack/webpack/compare/v5.27.1...v5.28.0)
  * Bumps [@babel/preset-react](https://github.com/babel/babel/tree/HEAD/packages/babel-preset-react) from 7.12.13 to 7.13.13.
    - [Release notes](https://github.com/babel/babel/releases)
    - [Changelog](https://github.com/babel/babel/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel/commits/v7.13.13/packages/babel-preset-react)
  * Bumps [y18n](https://github.com/yargs/y18n) from 3.2.1 to 3.2.2.
    - [Release notes](https://github.com/yargs/y18n/releases)
    - [Changelog](https://github.com/yargs/y18n/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/yargs/y18n/commits)
  * Bumps [@testing-library/dom](https://github.com/testing-library/dom-testing-library) from 7.30.1 to 7.30.3.
    - [Release notes](https://github.com/testing-library/dom-testing-library/releases)
    - [Changelog](https://github.com/testing-library/dom-testing-library/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/testing-library/dom-testing-library/compare/v7.30.1...v7.30.3)
  * Bumps [postcss](https://github.com/postcss/postcss) from 8.2.8 to 8.2.9.
    - [Release notes](https://github.com/postcss/postcss/releases)
    - [Changelog](https://github.com/postcss/postcss/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/postcss/postcss/compare/8.2.8...8.2.9)
  * Bumps [victory](https://github.com/formidablelabs/victory) from 35.4.12 to 35.4.13.
    - [Release notes](https://github.com/formidablelabs/victory/releases)
    - [Changelog](https://github.com/FormidableLabs/victory/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/formidablelabs/victory/compare/v35.4.12...v35.4.13)
  * Bumps [webpack](https://github.com/webpack/webpack) from 5.28.0 to 5.30.0.
    - [Release notes](https://github.com/webpack/webpack/releases)
    - [Commits](https://github.com/webpack/webpack/compare/v5.28.0...v5.30.0)
  * Bumps [core-js](https://github.com/zloirock/core-js/tree/HEAD/packages/core-js) from 3.9.1 to 3.10.0.
    - [Release notes](https://github.com/zloirock/core-js/releases)
    - [Changelog](https://github.com/zloirock/core-js/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/zloirock/core-js/commits/v3.10.0/packages/core-js)
  * Bumps [cypress-localstorage-commands](https://github.com/javierbrea/cypress-localstorage-commands) from 1.4.1 to 1.4.2.
    - [Release notes](https://github.com/javierbrea/cypress-localstorage-commands/releases)
    - [Changelog](https://github.com/javierbrea/cypress-localstorage-commands/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/javierbrea/cypress-localstorage-commands/compare/v1.4.1...v1.4.2)
  * Bumps node from 15.12.0-alpine to 15.13.0-alpine.
  * Bumps nginx from 1.19.8-alpine to 1.19.9-alpine.
  * Bumps [jest-watch-typeahead](https://github.com/jest-community/jest-watch-typeahead) from 0.6.1 to 0.6.2.
    - [Release notes](https://github.com/jest-community/jest-watch-typeahead/releases)
    - [Changelog](https://github.com/jest-community/jest-watch-typeahead/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/jest-community/jest-watch-typeahead/compare/v0.6.1...v0.6.2)
  * Bumps [@babel/core](https://github.com/babel/babel/tree/HEAD/packages/babel-core) from 7.13.13 to 7.13.14.
    - [Release notes](https://github.com/babel/babel/releases)
    - [Changelog](https://github.com/babel/babel/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel/commits/v7.13.14/packages/babel-core)
  * Bumps [@testing-library/react](https://github.com/testing-library/react-testing-library) from 11.2.5 to 11.2.6.
    - [Release notes](https://github.com/testing-library/react-testing-library/releases)
    - [Changelog](https://github.com/testing-library/react-testing-library/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/testing-library/react-testing-library/compare/v11.2.5...v11.2.6)
  * Bumps [mzedel-cypress-image-snapshot](https://github.com/mzedel/cypress-image-snapshot) from 4.0.3 to 4.0.5.
    - [Release notes](https://github.com/mzedel/cypress-image-snapshot/releases)
    - [Changelog](https://github.com/mzedel/cypress-image-snapshot/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/mzedel/cypress-image-snapshot/compare/v4.0.3...v4.0.5)
  * Bumps [cypress](https://github.com/cypress-io/cypress) from 6.8.0 to 6.9.1.
    - [Release notes](https://github.com/cypress-io/cypress/releases)
    - [Changelog](https://github.com/cypress-io/cypress/blob/develop/.releaserc.base.js)
    - [Commits](https://github.com/cypress-io/cypress/commits)
  * Bumps [msw](https://github.com/mswjs/msw) from 0.28.0 to 0.28.1.
    - [Release notes](https://github.com/mswjs/msw/releases)
    - [Changelog](https://github.com/mswjs/msw/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/mswjs/msw/compare/v0.28.0...v0.28.1)

#### integration (2.7.0)

New changes in integration since 2.6.0:

* demo script, include docker-compose.connect.yml by default
  ([MEN-4357](https://tracker.mender.io/browse/MEN-4357))
* Add auditlogs and deviceconnect to production templates
* migrated gateway service to use traefik
* production template: configure mender-api-gateway as a storage proxy
* Include the configuration add-on in the demo script
* Remove nginx-based api-gateway and replace with Traefik.
* fix auth verification on useradm APIs
  ([MEN-4623](https://tracker.mender.io/browse/MEN-4623))
* Upgrade auditlogs to 1.1.0.
* Upgrade create-artifact-worker to 1.0.2.
* Upgrade deployments to 2.3.0.
* Upgrade deployments-enterprise to 2.3.0.
* Upgrade deviceauth to 2.6.0.
* Add deviceconfig 1.0.0.
* Upgrade deviceconnect to 1.1.0.
* Upgrade gui to 2.7.0.
* Upgrade integration to 2.7.0.
* Upgrade inventory to 2.3.0.
* Upgrade inventory-enterprise to 2.3.0.
* Upgrade mender to 2.6.0.
* Upgrade mender-artifact to 3.5.1.
* Upgrade mender-cli to 1.7.0.
* Upgrade mender-connect to 1.1.0.
* Upgrade tenantadm to 3.1.0.
* Upgrade useradm to 1.14.0.
* Upgrade useradm-enterprise to 1.14.0.
* Upgrade workflows to 1.4.0.
* Upgrade workflows-enterprise to 1.4.0.
* Aggregated Dependabot Changelogs:
  * Bumps [docker-compose](https://github.com/docker/compose) from 1.27.4 to 1.28.0.
    - [Release notes](https://github.com/docker/compose/releases)
    - [Changelog](https://github.com/docker/compose/blob/1.28.0/CHANGELOG.md)
    - [Commits](https://github.com/docker/compose/compare/1.27.4...1.28.0)
  * Bumps [fabric](http://fabfile.org) from 2.5.0 to 2.6.0.
  * Bumps [docker-compose](https://github.com/docker/compose) from 1.28.0 to 1.28.2.
    - [Release notes](https://github.com/docker/compose/releases)
    - [Changelog](https://github.com/docker/compose/blob/1.28.2/CHANGELOG.md)
    - [Commits](https://github.com/docker/compose/compare/1.28.0...1.28.2)
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 6.2.1 to 6.2.2.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/6.2.1...6.2.2)
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 6.2.1 to 6.2.2.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/6.2.1...6.2.2)
  * Bumps [pyotp](https://github.com/pyotp/pyotp) from 2.4.1 to 2.5.1.
    - [Release notes](https://github.com/pyotp/pyotp/releases)
    - [Changelog](https://github.com/pyauth/pyotp/blob/develop/Changes.rst)
    - [Commits](https://github.com/pyotp/pyotp/compare/v2.4.1...v2.5.1)
  * Bumps [pyotp](https://github.com/pyotp/pyotp) from 2.5.1 to 2.6.0.
    - [Release notes](https://github.com/pyotp/pyotp/releases)
    - [Changelog](https://github.com/pyauth/pyotp/blob/develop/Changes.rst)
    - [Commits](https://github.com/pyotp/pyotp/compare/v2.5.1...v2.6.0)
  * Bumps [stripe](https://github.com/stripe/stripe-python) from 2.55.1 to 2.55.2.
    - [Release notes](https://github.com/stripe/stripe-python/releases)
    - [Changelog](https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/stripe/stripe-python/compare/v2.55.1...v2.55.2)
  * Bumps [pymongo](https://github.com/mongodb/mongo-python-driver) from 3.11.2 to 3.11.3.
    - [Release notes](https://github.com/mongodb/mongo-python-driver/releases)
    - [Changelog](https://github.com/mongodb/mongo-python-driver/blob/3.11.3/doc/changelog.rst)
    - [Commits](https://github.com/mongodb/mongo-python-driver/compare/3.11.2...3.11.3)
  * Bumps [pymongo](https://github.com/mongodb/mongo-python-driver) from 3.11.2 to 3.11.3.
    - [Release notes](https://github.com/mongodb/mongo-python-driver/releases)
    - [Changelog](https://github.com/mongodb/mongo-python-driver/blob/3.11.3/doc/changelog.rst)
    - [Commits](https://github.com/mongodb/mongo-python-driver/compare/3.11.2...3.11.3)
  * Bumps [cryptography](https://github.com/pyca/cryptography) from 3.3.1 to 3.4.4.
    - [Release notes](https://github.com/pyca/cryptography/releases)
    - [Changelog](https://github.com/pyca/cryptography/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pyca/cryptography/compare/3.3.1...3.4.4)
  * Bumps [cryptography](https://github.com/pyca/cryptography) from 3.3.2 to 3.4.4.
    - [Release notes](https://github.com/pyca/cryptography/releases)
    - [Changelog](https://github.com/pyca/cryptography/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pyca/cryptography/compare/3.3.2...3.4.4)
  * Bumps [cryptography](https://github.com/pyca/cryptography) from 3.3.2 to 3.4.4.
    - [Release notes](https://github.com/pyca/cryptography/releases)
    - [Changelog](https://github.com/pyca/cryptography/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pyca/cryptography/compare/3.3.2...3.4.4)
  * Bumps [cryptography](https://github.com/pyca/cryptography) from 3.4.4 to 3.4.5.
    - [Release notes](https://github.com/pyca/cryptography/releases)
    - [Changelog](https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst)
    - [Commits](https://github.com/pyca/cryptography/compare/3.4.4...3.4.5)
  * Bumps [cryptography](https://github.com/pyca/cryptography) from 3.4.4 to 3.4.5.
    - [Release notes](https://github.com/pyca/cryptography/releases)
    - [Changelog](https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst)
    - [Commits](https://github.com/pyca/cryptography/compare/3.4.4...3.4.5)
  * Bumps python from 3.9.1 to 3.9.2.
  * Bumps [cryptography](https://github.com/pyca/cryptography) from 3.4.5 to 3.4.6.
    - [Release notes](https://github.com/pyca/cryptography/releases)
    - [Changelog](https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst)
    - [Commits](https://github.com/pyca/cryptography/compare/3.4.5...3.4.6)
  * Bumps [docker-compose](https://github.com/docker/compose) from 1.28.2 to 1.28.4.
    - [Release notes](https://github.com/docker/compose/releases)
    - [Changelog](https://github.com/docker/compose/blob/1.28.4/CHANGELOG.md)
    - [Commits](https://github.com/docker/compose/compare/1.28.2...1.28.4)
  * Bumps [cryptography](https://github.com/pyca/cryptography) from 3.4.5 to 3.4.6.
    - [Release notes](https://github.com/pyca/cryptography/releases)
    - [Changelog](https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst)
    - [Commits](https://github.com/pyca/cryptography/compare/3.4.5...3.4.6)
  * Bumps [stripe](https://github.com/stripe/stripe-python) from 2.55.2 to 2.56.0.
    - [Release notes](https://github.com/stripe/stripe-python/releases)
    - [Changelog](https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/stripe/stripe-python/compare/v2.55.2...v2.56.0)
  * Bumps [docker-compose](https://github.com/docker/compose) from 1.28.4 to 1.28.5.
    - [Release notes](https://github.com/docker/compose/releases)
    - [Changelog](https://github.com/docker/compose/blob/1.28.5/CHANGELOG.md)
    - [Commits](https://github.com/docker/compose/compare/1.28.4...1.28.5)
  * Bumps [pillow](https://github.com/python-pillow/Pillow) from 8.1.0 to 8.1.2.
    - [Release notes](https://github.com/python-pillow/Pillow/releases)
    - [Changelog](https://github.com/python-pillow/Pillow/blob/master/CHANGES.rst)
    - [Commits](https://github.com/python-pillow/Pillow/compare/8.1.0...8.1.2)
  * Bumps [urllib3](https://github.com/urllib3/urllib3) from 1.26.3 to 1.26.4.
    - [Release notes](https://github.com/urllib3/urllib3/releases)
    - [Changelog](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst)
    - [Commits](https://github.com/urllib3/urllib3/compare/1.26.3...1.26.4)
  * Bumps [urllib3](https://github.com/urllib3/urllib3) from 1.26.2 to 1.26.4.
    - [Release notes](https://github.com/urllib3/urllib3/releases)
    - [Changelog](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst)
    - [Commits](https://github.com/urllib3/urllib3/compare/1.26.2...1.26.4)
  * Bumps [contextlib2](https://github.com/jazzband/contextlib2) from 0.6.0 to 0.6.0.post1.
    - [Release notes](https://github.com/jazzband/contextlib2/releases)
    - [Commits](https://github.com/jazzband/contextlib2/compare/v0.6.0...v0.6.0.post1)

#### inventory (2.3.0)

New changes in inventory since 2.2.0:

* Support returning a subset of attributes in filters/search
* docs: deprecate DELETE /devices/{id} management endpoint
* Aggregated Dependabot Changelogs:
  * Bumps alpine from 3.12 to 3.13.0.
  * Bumps [github.com/stretchr/testify](https://github.com/stretchr/testify) from 1.6.1 to 1.7.0.
    - [Release notes](https://github.com/stretchr/testify/releases)
    - [Commits](https://github.com/stretchr/testify/compare/v1.6.1...v1.7.0)
  * Bumps golang from 1.14-alpine3.12 to 1.15.7-alpine3.12.
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.4 to 1.4.5.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.4...v1.4.5)
  * Bumps alpine from 3.13.0 to 3.13.1.
  * Bumps golang from 1.15.7-alpine3.12 to 1.15.8-alpine3.12.
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.5 to 1.5.0.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.5...v1.5.0)

#### inventory-enterprise (2.3.0)

New changes in inventory-enterprise since 2.2.0:

* Support returning a subset of attributes in filters/search
* docs: deprecate DELETE /devices/{id} management endpoint
* Aggregated Dependabot Changelogs:
  * Bumps alpine from 3.12 to 3.13.0.
  * Bumps alpine from 3.12 to 3.13.0.
  * Bumps [github.com/stretchr/testify](https://github.com/stretchr/testify) from 1.6.1 to 1.7.0.
    - [Release notes](https://github.com/stretchr/testify/releases)
    - [Commits](https://github.com/stretchr/testify/compare/v1.6.1...v1.7.0)
  * Bumps [github.com/stretchr/testify](https://github.com/stretchr/testify) from 1.6.1 to 1.7.0.
    - [Release notes](https://github.com/stretchr/testify/releases)
    - [Commits](https://github.com/stretchr/testify/compare/v1.6.1...v1.7.0)
  * Bumps golang from 1.14-alpine3.12 to 1.15.7-alpine3.12.
  * Bumps golang from 1.14-alpine3.12 to 1.15.7-alpine3.12.
  * Bumps [github.com/go-redis/redis/v8](https://github.com/go-redis/redis) from 8.4.8 to 8.4.10.
    - [Release notes](https://github.com/go-redis/redis/releases)
    - [Changelog](https://github.com/go-redis/redis/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/go-redis/redis/compare/v8.4.8...v8.4.10)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.4 to 1.4.5.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.4...v1.4.5)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.4 to 1.4.5.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.4...v1.4.5)
  * Bumps alpine from 3.13.0 to 3.13.1.
  * Bumps alpine from 3.13.0 to 3.13.1.
  * Bumps golang from 1.15.7-alpine3.12 to 1.15.8-alpine3.12.
  * Bumps alpine from 3.13.1 to 3.13.2.
  * Bumps golang from 1.15.7-alpine3.12 to 1.16.0-alpine3.12.
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.5 to 1.4.6.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.5...1.4.6)
  * Bumps [github.com/go-redis/redis/v8](https://github.com/go-redis/redis) from 8.4.10 to 8.7.1.
    - [Release notes](https://github.com/go-redis/redis/releases)
    - [Changelog](https://github.com/go-redis/redis/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/go-redis/redis/compare/v8.4.10...v8.7.1)
  * Bumps golang from 1.16.0-alpine3.12 to 1.16.2-alpine3.12.
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.6 to 1.5.0.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/1.4.6...v1.5.0)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.5 to 1.5.0.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.5...v1.5.0)

#### mender (2.6.0)

New changes in mender since 2.5.0:

* fix, support white spaces in single-file artifacts' names
  ([MEN-4179](https://tracker.mender.io/browse/MEN-4179))
* Change provider in inventory-geo script to ipinfo.io
* Cache geo-location inventory data in volatile memory
* Log which scripts are run at the info level
* Filter out docker network interfaces in inventory
  This adds functionality for filtering out interfaces matching
  * br-.*
  * veth.*
  * docker.*
  by default, so that docker network interfaces do not flood the inventory on
  hosts running a lot of docker containers.
  If re-adding this functionality is required, set the environment variable:
  * INCLUDE_DOCKER_INTERFACES=true
  ([MEN-4487](https://tracker.mender.io/browse/MEN-4487))
* single-file: Use atomic file operations.
* single-file: Use stderr for all error messages.
* Remove deprecated field HttpsClient from config file (gets
  the rid of bogus SSL warnings on `mender show-artifact` and any other
  cli operation).
  ([MEN-4398](https://tracker.mender.io/browse/MEN-4398))
* Send the inventory after a successful deployment, even though the
  device has not rebooted.
  ([MEN-4518](https://tracker.mender.io/browse/MEN-4518))
* mender setup: when configuring for demo using self-signed
  certificate, install the certificate in the local trust store so that
  all components in the system (namely, Mender addons) can trust the
  Mender server without extra configuration.
  ([MEN-4580](https://tracker.mender.io/browse/MEN-4580))
* Warn in the log when the system certificates contain the demo cert.
* Aggregated Dependabot Changelogs:
  * Bumps [github.com/stretchr/testify](https://github.com/stretchr/testify) from 1.6.1 to 1.7.0.
    - [Release notes](https://github.com/stretchr/testify/releases)
    - [Commits](https://github.com/stretchr/testify/compare/v1.6.1...v1.7.0)

#### mender-artifact (3.5.1)

New changes in mender-artifact since 3.5.0:

* Do not change the underlying Artifact unnecessarily
  Previously the commands modifying an Artifact would always repack an Artifact,
  no matter whether or not that modifications had actually been made to the
  Artifact. As an example of this, if you had a signed Artifact compressed with
  lzma, running `mender-artifact cat <artifact>:/<path-to-file>` would then cat
  the file, and repack the Artifact with the standard compression, which is
  `gzip`. Along the way the signature would also be lost.
  This fix adds the following changes to the tooling:
  * Modified images are no longer repacked, unless the command run has changed the
  underlying image. This means that cat and copying out of an image will keep your
  image intact. While copying into, installing, and removing files from the image
  will repack the image.
  * If an image is modified, and needs to be repacked, the existing compression
  will be respected when repacking. The only exception is the `--compression` flag
  for `mender-artifact modify` which can override the existing compression when repacking.
  * `mender-artifact {cat,install,cp,rm}` do not respect the `--compression` flag,
  but rather prints a warning, that the flag is ignored. If you want to change the
  compression of your Artifact, run `mender-artifact modify <Artifact>
  --compression <type>`
  ([MEN-4502](https://tracker.mender.io/browse/MEN-4502))
* Add a note about the proper usage of the 'compression' flag in the
  global help text.

#### mender-cli (1.7.0)

New changes in mender-cli since 1.6.0:

* Fix: Respect the --server flag from config everywhere
* `mender-cli --record <my-file> terminal <DEVICE-ID>` records
  the terminal session into a local file.
  ([MEN-4318](https://tracker.mender.io/browse/MEN-4318))
* `mender-cli --playback <my-file> terminal` playbacks the
  previously recorded terminal session from a local file.
  ([MEN-4318](https://tracker.mender.io/browse/MEN-4318))
* New command `mender-cli devices list` to list all devices
  from /devauth/devices endpoint. The amount of detail can be controlled
  using cli parameter `-d/--detail`, same as for other commands.
* Previously, the --generate-autocomplete call would silently ignore
  errors, when the autocomplete directory was not present. This explicitly logs
  the errors returned during autocomplete script generation.
* New command port-forward: port-forward TCP and UDP ports from the device
* Add filetransfer upload and download support
  ([MEN-4323](https://tracker.mender.io/browse/MEN-4323))
* Aggregated Dependabot Changelogs:
  * Bumps golang from 1.15.6-alpine3.12 to 1.15.8-alpine3.12.
  * Bumps [github.com/spf13/cobra](https://github.com/spf13/cobra) from 1.1.1 to 1.1.3.
    - [Release notes](https://github.com/spf13/cobra/releases)
    - [Changelog](https://github.com/spf13/cobra/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/spf13/cobra/compare/v1.1.1...v1.1.3)
  * Bumps [github.com/cheggaaa/pb/v3](https://github.com/cheggaaa/pb) from 3.0.5 to 3.0.6.
    - [Release notes](https://github.com/cheggaaa/pb/releases)
    - [Commits](https://github.com/cheggaaa/pb/compare/v3.0.5...v3.0.6)
  * Bumps golang from 1.15.8-alpine3.12 to 1.16.0-alpine3.12.
  * Bumps golang from 1.16.0-alpine3.12 to 1.16.2-alpine3.12.
  * Bumps [github.com/cheggaaa/pb/v3](https://github.com/cheggaaa/pb) from 3.0.6 to 3.0.7.
    - [Release notes](https://github.com/cheggaaa/pb/releases)
    - [Commits](https://github.com/cheggaaa/pb/compare/v3.0.6...v3.0.7)

#### mender-connect (1.1.0)

New changes in mender-connect since 1.0.0:

* Add remote triggers for Mender client's check-update and send-inventory
* [examples/mender-connect.conf] Remove unnecessary ServerURL
* Add handler for File Transfer protocol.
  ([MEN-4322](https://tracker.mender.io/browse/MEN-4322))
* filetransfer: Add handler for fetching file and file info
* New feature: TCP and UDP port-forwarding
* stat(2) file path and verify conditions before starting upload
* Add option to pass src_path to file upload requests

#### tenantadm (3.1.0)

New changes in tenantadm since 3.0.0:

* Return Add-ons in GET user/tenant
  ([MEN-4306](https://tracker.mender.io/browse/MEN-4306))
* internal api: PUT /tenant/:id accepts addons
* Aggregated Dependabot Changelogs:
  * Bumps alpine from 3.12 to 3.13.0.
  * Bumps [github.com/stretchr/testify](https://github.com/stretchr/testify) from 1.6.1 to 1.7.0.
    - [Release notes](https://github.com/stretchr/testify/releases)
    - [Commits](https://github.com/stretchr/testify/compare/v1.6.1...v1.7.0)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.4 to 1.4.5.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.4...v1.4.5)
  * Bumps golang from 1.14-alpine3.12 to 1.15.7-alpine3.12.
  * Bumps alpine from 3.13.0 to 3.13.1.
  * Bumps golang from 1.15.7-alpine3.12 to 1.15.8-alpine3.12.
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.5 to 1.4.6.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.5...1.4.6)
  * Bumps golang from 1.15.8-alpine3.12 to 1.16.0-alpine3.12.
  * Bumps alpine from 3.13.1 to 3.13.2.
  * Bumps [github.com/sirupsen/logrus](https://github.com/sirupsen/logrus) from 1.7.0 to 1.8.0.
    - [Release notes](https://github.com/sirupsen/logrus/releases)
    - [Changelog](https://github.com/sirupsen/logrus/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/sirupsen/logrus/compare/v1.7.0...v1.8.0)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.6 to 1.5.0.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/1.4.6...v1.5.0)
  * Bumps [github.com/sirupsen/logrus](https://github.com/sirupsen/logrus) from 1.8.0 to 1.8.1.
    - [Release notes](https://github.com/sirupsen/logrus/releases)
    - [Changelog](https://github.com/sirupsen/logrus/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/sirupsen/logrus/compare/v1.8.0...v1.8.1)
  * Bumps golang from 1.16.0-alpine3.12 to 1.16.2-alpine3.12.

#### useradm (1.14.0)

New changes in useradm since 1.13.0:

* use traefik's X-Forwarded-* headers
* Aggregated Dependabot Changelogs:
  * Bumps alpine from 3.12 to 3.13.0.
  * Bumps [github.com/stretchr/testify](https://github.com/stretchr/testify) from 1.6.1 to 1.7.0.
    - [Release notes](https://github.com/stretchr/testify/releases)
    - [Commits](https://github.com/stretchr/testify/compare/v1.6.1...v1.7.0)
  * Bumps golang from 1.14-alpine3.12 to 1.15.7-alpine3.12.
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.4 to 1.4.5.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.4...v1.4.5)
  * Bumps alpine from 3.13.0 to 3.13.1.
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.5 to 1.4.6.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.5...1.4.6)
  * Bumps alpine from 3.13.1 to 3.13.2.
  * Bumps [github.com/sirupsen/logrus](https://github.com/sirupsen/logrus) from 1.7.0 to 1.8.0.
    - [Release notes](https://github.com/sirupsen/logrus/releases)
    - [Changelog](https://github.com/sirupsen/logrus/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/sirupsen/logrus/compare/v1.7.0...v1.8.0)
  * Bumps golang from 1.15.7-alpine3.12 to 1.16.2-alpine3.12.
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.6 to 1.5.0.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/1.4.6...v1.5.0)
  * Bumps [github.com/sirupsen/logrus](https://github.com/sirupsen/logrus) from 1.8.0 to 1.8.1.
    - [Release notes](https://github.com/sirupsen/logrus/releases)
    - [Changelog](https://github.com/sirupsen/logrus/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/sirupsen/logrus/compare/v1.8.0...v1.8.1)

#### useradm-enterprise (1.14.0)

New changes in useradm-enterprise since 1.13.0:

* use traefik's X-Forwarded-* headers
* New endpoints for email verification.
  Introduce new endpoints that enable email verification.
  The first endpoint starts the email verification procedure.
  As a part of this procedure, we are sending a verification email to the user.
  The verification email contains a link for email verification.
  The second endpoint can be used to finalize email verification.
  Only users with a verified email address have access to two factor
  authentication settings.
* rbac: extend observer role by adding access to device configuration
* Aggregated Dependabot Changelogs:
  * Bumps alpine from 3.12 to 3.13.0.
  * Bumps alpine from 3.12 to 3.13.0.
  * Bumps [github.com/stretchr/testify](https://github.com/stretchr/testify) from 1.6.1 to 1.7.0.
    - [Release notes](https://github.com/stretchr/testify/releases)
    - [Commits](https://github.com/stretchr/testify/compare/v1.6.1...v1.7.0)
  * Bumps [github.com/stretchr/testify](https://github.com/stretchr/testify) from 1.6.1 to 1.7.0.
    - [Release notes](https://github.com/stretchr/testify/releases)
    - [Commits](https://github.com/stretchr/testify/compare/v1.6.1...v1.7.0)
  * Bumps [github.com/go-redis/redis/v8](https://github.com/go-redis/redis) from 8.4.8 to 8.4.10.
    - [Release notes](https://github.com/go-redis/redis/releases)
    - [Changelog](https://github.com/go-redis/redis/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/go-redis/redis/compare/v8.4.8...v8.4.10)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.4 to 1.4.5.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.4...v1.4.5)
  * Bumps golang from 1.14-alpine3.12 to 1.15.7-alpine3.12.
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.4 to 1.4.5.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.4...v1.4.5)
  * Bumps alpine from 3.13.0 to 3.13.1.
  * Bumps alpine from 3.13.0 to 3.13.1.
  * Bumps [github.com/go-redis/redis/v8](https://github.com/go-redis/redis) from 8.4.10 to 8.4.11.
    - [Release notes](https://github.com/go-redis/redis/releases)
    - [Changelog](https://github.com/go-redis/redis/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/go-redis/redis/compare/v8.4.10...v8.4.11)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.5 to 1.4.6.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.5...1.4.6)
  * Bumps alpine from 3.13.1 to 3.13.2.
  * Bumps golang from 1.15.7-alpine3.12 to 1.16.0-alpine3.12.
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.5 to 1.4.6.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.5...1.4.6)
  * Bumps alpine from 3.13.1 to 3.13.2.
  * Bumps [github.com/sirupsen/logrus](https://github.com/sirupsen/logrus) from 1.7.0 to 1.8.0.
    - [Release notes](https://github.com/sirupsen/logrus/releases)
    - [Changelog](https://github.com/sirupsen/logrus/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/sirupsen/logrus/compare/v1.7.0...v1.8.0)
  * Bumps [github.com/go-redis/redis/v8](https://github.com/go-redis/redis) from 8.4.11 to 8.7.1.
    - [Release notes](https://github.com/go-redis/redis/releases)
    - [Changelog](https://github.com/go-redis/redis/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/go-redis/redis/compare/v8.4.11...v8.7.1)
  * Bumps [github.com/sirupsen/logrus](https://github.com/sirupsen/logrus) from 1.7.0 to 1.8.0.
    - [Release notes](https://github.com/sirupsen/logrus/releases)
    - [Changelog](https://github.com/sirupsen/logrus/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/sirupsen/logrus/compare/v1.7.0...v1.8.0)
  * Bumps golang from 1.15.7-alpine3.12 to 1.16.2-alpine3.12.
  * Bumps golang from 1.16.0-alpine3.12 to 1.16.2-alpine3.12.
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.6 to 1.5.0.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/1.4.6...v1.5.0)
  * Bumps [github.com/sirupsen/logrus](https://github.com/sirupsen/logrus) from 1.8.0 to 1.8.1.
    - [Release notes](https://github.com/sirupsen/logrus/releases)
    - [Changelog](https://github.com/sirupsen/logrus/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/sirupsen/logrus/compare/v1.8.0...v1.8.1)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.6 to 1.5.0.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/1.4.6...v1.5.0)
  * Bumps [github.com/sirupsen/logrus](https://github.com/sirupsen/logrus) from 1.8.0 to 1.8.1.
    - [Release notes](https://github.com/sirupsen/logrus/releases)
    - [Changelog](https://github.com/sirupsen/logrus/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/sirupsen/logrus/compare/v1.8.0...v1.8.1)

#### workflows (1.4.0)

New changes in workflows since 1.3.0:

* Update workflow definitions for
  provisioning/decomissioning devices in deviceconfig service
  ([MEN-4383](https://tracker.mender.io/browse/MEN-4383), [MEN-4429](https://tracker.mender.io/browse/MEN-4429))
* New workflow deploy_device_configuration
  ([MEN-4383](https://tracker.mender.io/browse/MEN-4383), [MEN-4429](https://tracker.mender.io/browse/MEN-4429))
* Configuration deployment triggers device update check
  ([MEN-4383](https://tracker.mender.io/browse/MEN-4383), [MEN-4429](https://tracker.mender.io/browse/MEN-4429))
* Aggregated Dependabot Changelogs:
  * Bumps alpine from 3.12 to 3.13.0.
  * Bumps [github.com/stretchr/testify](https://github.com/stretchr/testify) from 1.6.1 to 1.7.0.
    - [Release notes](https://github.com/stretchr/testify/releases)
    - [Commits](https://github.com/stretchr/testify/compare/v1.6.1...v1.7.0)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.4 to 1.4.5.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.4...v1.4.5)

#### workflows-enterprise (1.4.0)

New changes in workflows-enterprise since 1.3.0:

* Update workflow definitions for
  provisioning/decomissioning devices in deviceconfig service
  ([MEN-4383](https://tracker.mender.io/browse/MEN-4383), [MEN-4429](https://tracker.mender.io/browse/MEN-4429))
* New workflow deploy_device_configuration
  ([MEN-4383](https://tracker.mender.io/browse/MEN-4383), [MEN-4429](https://tracker.mender.io/browse/MEN-4429))
* Configuration deployment triggers device update check
  ([MEN-4383](https://tracker.mender.io/browse/MEN-4383), [MEN-4429](https://tracker.mender.io/browse/MEN-4429))
* Fix password reset button text
* Add workflow for sending password verification email
* New workflow contact_support for handling inbound email
  requests to Mender support
* New workflow clear_tenant_tokens for puriging tenant JWTs
* Aggregated Dependabot Changelogs:
  * Bumps alpine from 3.12 to 3.13.0.
  * Bumps alpine from 3.12 to 3.13.0.
  * Bumps [github.com/stretchr/testify](https://github.com/stretchr/testify) from 1.6.1 to 1.7.0.
    - [Release notes](https://github.com/stretchr/testify/releases)
    - [Commits](https://github.com/stretchr/testify/compare/v1.6.1...v1.7.0)
  * Bumps [github.com/stretchr/testify](https://github.com/stretchr/testify) from 1.6.1 to 1.7.0.
    - [Release notes](https://github.com/stretchr/testify/releases)
    - [Commits](https://github.com/stretchr/testify/compare/v1.6.1...v1.7.0)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.4 to 1.4.5.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.4...v1.4.5)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.4 to 1.4.5.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.4...v1.4.5)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.5 to 1.4.6.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.5...1.4.6)
  * Bumps alpine from 3.13.0 to 3.13.1.
  * Bumps alpine from 3.13.1 to 3.13.2.


## meta-mender dunfell-v2021.03

_Released 03.05.2021_

### Statistics

A total of 29 lines added, 23 removed (delta 6)

| Developers with the most changesets | |
|---|---|
| Lluis Campos | 5 (62.5%) |
| Kristian Amlie | 2 (25.0%) |
| Leon Anavi | 1 (12.5%) |

| Developers with the most changed lines | |
|---|---|
| Kristian Amlie | 16 (47.1%) |
| Lluis Campos | 12 (35.3%) |
| Leon Anavi | 6 (17.6%) |

| Developers with the most lines removed | |
|---|---|
| Lluis Campos | 2 (8.7%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 7 (87.5%) |
| Konsulko Group | 1 (12.5%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 28 (82.4%) |
| Konsulko Group | 6 (17.6%) |

| Employers with the most hackers (total 3) | |
|---|---|
| Northern.tech | 2 (66.7%) |
| Konsulko Group | 1 (33.3%) |


### Changelogs

#### meta-mender (dunfell-v2021.03)

New changes in meta-mender since dunfell-v2021.01:

* Fix Mender installation from a USB stick for BIOS
* Fixes build warnings: "MENDER_CONNECT_..." is not a
  recognized MENDER_ variable
* mender-connect: Correct ShellCommand key in config file
* mender-connect.conf: Remove unnecessary field ServerURL


## meta-mender zeus-v2021.02

_Released 02.22.2021_

### Statistics

A total of 887 lines added, 368 removed (delta 519)

| Developers with the most changesets | |
|---|---|
| Lluis Campos | 22 (40.0%) |
| Kristian Amlie | 18 (32.7%) |
| Fabio Tranchitella | 14 (25.5%) |
| Ole Petter Orhagen | 1 (1.8%) |

| Developers with the most changed lines | |
|---|---|
| Fabio Tranchitella | 407 (42.0%) |
| Lluis Campos | 379 (39.2%) |
| Kristian Amlie | 162 (16.7%) |
| Ole Petter Orhagen | 20 (2.1%) |

| Developers with the most lines removed | |
|---|---|
| Ole Petter Orhagen | 20 (5.4%) |

| Developers with the most signoffs (total 7) | |
|---|---|
| Lluis Campos | 7 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 55 (100.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 968 (100.0%) |

| Employers with the most signoffs (total 7) | |
|---|---|
| Northern.tech | 7 (100.0%) |

| Employers with the most hackers (total 4) | |
|---|---|
| Northern.tech | 4 (100.0%) |

### Changelogs

#### meta-mender (zeus-v2021.02)

New changes in meta-mender since zeus-v2020.12:

* Make DBus support optional in Mender client with `PACKAGECONFIG`.
  It defaults to on, but can be turned off with:
  ```
  PACKAGECONFIG_remove = "dbus"
  ```
  Backported to dunfell, modifying the PACKAGECONFIG defaults and amending
  the test. ([MEN-4014](https://tracker.mender.io/browse/MEN-4014))
* mender-client: Add DBus busconfig files.
  ([MEN-4030](https://tracker.mender.io/browse/MEN-4030))
* mender-client: The self-signed Mender server certificate, if
  present, is copied to ca-certificates in addition to
  `MENDER_CERT_LOCATION` to be trusted by other services running in the
  device. ([MEN-4273](https://tracker.mender.io/browse/MEN-4273))
* mender-client: fix QA Issue: invalid PACKAGECONFIG: inventory-network-scripts
* Rename mender-shell to mender-connect
  ([MEN-4292](https://tracker.mender.io/browse/MEN-4292))
* Add mender-binary-delta 1.1.1 and 1.2.0.
* Add the MENDER_CONNECT_SHELL to meta-mender-core, defaults to /bin/sh
* Add recipe mender-connect 1.0.0
* Add recipe mender-client 2.5.0
* Add recipe mender-artifact 3.5.0
* Add mender-artifact 3.4.1 recipe.
* Add mender-client 2.3.2 and 2.4.2 recipes.
* Fix broken demo certificate in production recipes.
* mender-connect: Correct ShellCommand key in config file


## meta-mender warrior-v2021.02

_Released 02.22.2021_

### Statistics

A total of 272 lines added, 180 removed (delta 92)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 13 (43.3%) |
| Lluis Campos | 12 (40.0%) |
| Fabio Tranchitella | 5 (16.7%) |

| Developers with the most changed lines | |
|---|---|
| Lluis Campos | 202 (64.3%) |
| Kristian Amlie | 77 (24.5%) |
| Fabio Tranchitella | 35 (11.1%) |

| Developers with the most signoffs (total 8) | |
|---|---|
| Lluis Campos | 8 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 30 (100.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 314 (100.0%) |

| Employers with the most signoffs (total 8) | |
|---|---|
| Northern.tech | 8 (100.0%) |

| Employers with the most hackers (total 3) | |
|---|---|
| Northern.tech | 3 (100.0%) |

### Changelogs

#### meta-mender (warrior-v2021.02)

New changes in meta-mender since warrior-v2020.12:

* Make DBus support optional in Mender client with `PACKAGECONFIG`.
  It defaults to on, but can be turned off with:
  ```
  PACKAGECONFIG_remove = "dbus"
  ```
  Backported to dunfell, modifying the PACKAGECONFIG defaults and amending
  the test.
  Backported to warrior, removing the test.
  ([MEN-4014](https://tracker.mender.io/browse/MEN-4014))
* mender-client: Add DBus busconfig files.
  ([MEN-4030](https://tracker.mender.io/browse/MEN-4030))
* mender-client: The self-signed Mender server certificate, if
  present, is copied to ca-certificates in addition to
  `MENDER_CERT_LOCATION` to be trusted by other services running in the
  device. ([MEN-4273](https://tracker.mender.io/browse/MEN-4273))
* mender-client: fix QA Issue: invalid PACKAGECONFIG: inventory-network-scripts
* Rename mender-shell to mender-connect
  ([MEN-4292](https://tracker.mender.io/browse/MEN-4292))
* Add mender-binary-delta 1.1.1 and 1.2.0.
* Add the MENDER_CONNECT_SHELL to meta-mender-core, defaults to /bin/sh
* Add recipe mender-connect 1.0.0
* Add recipe mender 2.5.0
* Add recipe mender-artifact 3.5.0
* Add mender-artifact 3.4.1 recipe.
* Add mender 2.3.2 and 2.4.2 recipes.
* Fix broken demo certificate in production recipes.
* mender-connect: Correct ShellCommand key in config file


## meta-mender dunfell-v2021.01

_Released 01.26.2021_

### Statistics

A total of 959 lines added, 405 removed (delta 554)

| Developers with the most changesets | |
|---|---|
| Lluis Campos | 28 (43.1%) |
| Kristian Amlie | 21 (32.3%) |
| Fabio Tranchitella | 14 (21.5%) |
| Drew Moseley | 1 (1.5%) |
| Ole Petter Orhagen | 1 (1.5%) |

| Developers with the most changed lines | |
|---|---|
| Lluis Campos | 439 (41.6%) |
| Fabio Tranchitella | 408 (38.6%) |
| Kristian Amlie | 186 (17.6%) |
| Ole Petter Orhagen | 20 (1.9%) |
| Drew Moseley | 3 (0.3%) |

| Developers with the most lines removed | |
|---|---|
| Ole Petter Orhagen | 20 (4.9%) |

| Developers with the most signoffs (total 2) | |
|---|---|
| Lluis Campos | 2 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 65 (100.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 1056 (100.0%) |

| Employers with the most signoffs (total 2) | |
|---|---|
| Northern.tech | 2 (100.0%) |

| Employers with the most hackers (total 5) | |
|---|---|
| Northern.tech | 5 (100.0%) |


### Changelogs

#### meta-mender (dunfell-v2021.01)

New changes in meta-mender since dunfell-v2020.12:

* Make DBus support optional in Mender client with `PACKAGECONFIG`.
  It defaults to on, but can be turned off with:
  ```
  PACKAGECONFIG_remove = "dbus"
  ```
  Backported to dunfell, modifying the PACKAGECONFIG defaults and amending
  the test. ([MEN-4014](https://tracker.mender.io/browse/MEN-4014))
* mender-client: Add DBus busconfig files.
  ([MEN-4030](https://tracker.mender.io/browse/MEN-4030))
* mender-client: The self-signed Mender server certificate, if
  present, is copied to ca-certificates in addition to
  `MENDER_CERT_LOCATION` to be trusted by other services running in the
  device. ([MEN-4273](https://tracker.mender.io/browse/MEN-4273))
* meta-mender-demo: install mender-shell
  ([MEN-4187](https://tracker.mender.io/browse/MEN-4187))
* Revert "mender: Reestablish labels on the root filesystems."
* mender-client: fix QA Issue: invalid PACKAGECONFIG: inventory-network-scripts
* mender-shell: generate and install mender-shell.conf with
  required fields. `ServerURL` can be configured setting yocto variable
  `MENDER_SERVER_URL`, same as used by mender-client recipe. If a
  `mender-shell.conf` file is found in the `SRC_URI` the contents will be
  merged. ([MEN-4242](https://tracker.mender.io/browse/MEN-4242))
* mender-shell: Add `User` to generated mender-shell.conf. The
  value of it is configured using `MENDER_SHELL_USER` variable, which
  defaults to `nobody` for meta-mender-core and `root` for
  meta-mender-demo.
  ([MEN-4242](https://tracker.mender.io/browse/MEN-4242))
* Rename mender-shell to mender-connect
  ([MEN-4292](https://tracker.mender.io/browse/MEN-4292))
* mender-raspberrypi: Make kernel settings conditional
* Remove mender-binary-delta 1.0.0, 1.0.1, and 1.1.0.
  All three of these have turned out to be incompatible with
  libubootenv, which is used on dunfell and later Yocto branches.
* Add mender-binary-delta 1.1.1 and 1.2.0.
* Add the MENDER_CONNECT_SHELL to meta-mender-core, defaults to /bin/sh
* Add recipe mender-connect 1.0.0
* Add recipe mender-client 2.5.0
* Add recipe mender-artifact 3.5.0
* Add mender-artifact 3.4.1 recipe.
* Add mender-client 2.3.2 and 2.4.2 recipes.
* Fix broken demo certificate in production recipes.
* Aggregated Dependabot Changelogs:
  * Bumps alpine from 3.7 to 3.12.0.
  * Bumps [ubi-reader](https://github.com/jrspruitt/ubi_reader) from 0.6.5 to 0.7.0.
    - [Release notes](https://github.com/jrspruitt/ubi_reader/releases)
    - [Commits](https://github.com/jrspruitt/ubi_reader/commits)
  * Bumps [requests](https://github.com/psf/requests) from 2.22.0 to 2.24.0.
    - [Release notes](https://github.com/psf/requests/releases)
    - [Changelog](https://github.com/psf/requests/blob/master/HISTORY.md)
    - [Commits](https://github.com/psf/requests/compare/v2.22.0...v2.24.0)
  * Bumps [pytest-html](https://github.com/pytest-dev/pytest-html) from 2.0.1 to 2.1.1.
    - [Release notes](https://github.com/pytest-dev/pytest-html/releases)
    - [Changelog](https://github.com/pytest-dev/pytest-html/blob/master/CHANGES.rst)
    - [Commits](https://github.com/pytest-dev/pytest-html/compare/v2.0.1...v2.1.1)
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 5.3.2 to 6.1.1.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/5.3.2...6.1.1)
  * Bumps [paramiko](https://github.com/paramiko/paramiko) from 2.7.1 to 2.7.2.
    - [Release notes](https://github.com/paramiko/paramiko/releases)
    - [Changelog](https://github.com/paramiko/paramiko/blob/master/NEWS)
    - [Commits](https://github.com/paramiko/paramiko/compare/2.7.1...2.7.2)
  * Bumps alpine from 3.12.0 to 3.12.1.
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 6.1.1 to 6.1.2.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/6.1.1...6.1.2)
  * Bumps [requests](https://github.com/psf/requests) from 2.24.0 to 2.25.0.
    - [Release notes](https://github.com/psf/requests/releases)
    - [Changelog](https://github.com/psf/requests/blob/master/HISTORY.md)
    - [Commits](https://github.com/psf/requests/compare/v2.24.0...v2.25.0)
  * Bumps [pytest-html](https://github.com/pytest-dev/pytest-html) from 2.1.1 to 3.0.0.
    - [Release notes](https://github.com/pytest-dev/pytest-html/releases)
    - [Changelog](https://github.com/pytest-dev/pytest-html/blob/master/CHANGES.rst)
    - [Commits](https://github.com/pytest-dev/pytest-html/compare/v2.1.1...v3.0.0)
  * Bumps [pytest-html](https://github.com/pytest-dev/pytest-html) from 3.0.0 to 3.1.0.
    - [Release notes](https://github.com/pytest-dev/pytest-html/releases)
    - [Changelog](https://github.com/pytest-dev/pytest-html/blob/master/CHANGES.rst)
    - [Commits](https://github.com/pytest-dev/pytest-html/compare/v3.0.0...v3.1.0)
  * Bumps alpine from 3.12.1 to 3.12.2.
  * Bumps [pytest-html](https://github.com/pytest-dev/pytest-html) from 3.1.0 to 3.1.1.
    - [Release notes](https://github.com/pytest-dev/pytest-html/releases)
    - [Changelog](https://github.com/pytest-dev/pytest-html/blob/master/CHANGES.rst)
    - [Commits](https://github.com/pytest-dev/pytest-html/compare/v3.1.0...v3.1.1)
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 6.1.2 to 6.2.0.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/6.1.2...6.2.0)
  * Bumps alpine from 3.12.2 to 3.12.3.
  * Bumps [psutil](https://github.com/giampaolo/psutil) from 5.7.2 to 5.8.0.
    - [Release notes](https://github.com/giampaolo/psutil/releases)
    - [Changelog](https://github.com/giampaolo/psutil/blob/master/HISTORY.rst)
    - [Commits](https://github.com/giampaolo/psutil/compare/release-5.7.2...release-5.8.0)
  * Bumps [requests](https://github.com/psf/requests) from 2.25.0 to 2.25.1.
    - [Release notes](https://github.com/psf/requests/releases)
    - [Changelog](https://github.com/psf/requests/blob/master/HISTORY.md)
    - [Commits](https://github.com/psf/requests/compare/v2.25.0...v2.25.1)
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 6.2.0 to 6.2.1.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/6.2.0...6.2.1)


## mender-convert 2.2.2

_Released 01.21.2021_

### Statistics

A total of 73 lines added, 40 removed (delta 33)

| Developers with the most changesets | |
|---|---|
| Lluis Campos | 4 (28.6%) |
| Ole Petter Orhagen | 4 (28.6%) |
| Kristian Amlie | 3 (21.4%) |
| Drew Moseley | 2 (14.3%) |
| Mirza Krak | 1 (7.1%) |

| Developers with the most changed lines | |
|---|---|
| Lluis Campos | 37 (49.3%) |
| Drew Moseley | 20 (26.7%) |
| Ole Petter Orhagen | 11 (14.7%) |
| Kristian Amlie | 6 (8.0%) |
| Mirza Krak | 1 (1.3%) |

| Developers with the most lines removed | |
|---|---|
| Mirza Krak | 1 (2.5%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 14 (100.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 75 (100.0%) |

| Employers with the most hackers (total 5) | |
|---|---|
| Northern.tech | 5 (100.0%) |

### Changelogs

#### mender-convert (2.2.2)

New changes in mender-convert since 2.2.1:

* Package latest released Mender-client by default
  ([QA-214](https://tracker.mender.io/browse/QA-214))
* Use separate chown and chgrp commands when creating rootfs overlay.
* Better parameter checks for read-only options.
* Fix error when removing empty directories in rootfs/boot


## mender-convert 2.3.1

_Released 16.04.2021_

### Statistics

| Developers with the most changesets | |
|---|---|
| Ole Petter Orhagen | 4 (80.0%) |
| Lluis Campos | 1 (20.0%) |

| Developers with the most changed lines | |
|---|---|
| Lluis Campos | 9 (64.3%) |
| Ole Petter Orhagen | 5 (35.7%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 5 (100.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 14 (100.0%) |

| Employers with the most hackers (total 2) | |
|---|---|
| Northern.tech | 2 (100.0%) |

### Changelogs

#### mender-convert (2.3.1)

New changes in mender-convert since 2.3.0:

* The standard RasperryPi configuration now comes with UBoot 2020.01 as
  the default. ([MEN-4395](https://tracker.mender.io/browse/MEN-4395))
* [raspberrypi_config] Enable UART in U-Boot config.txt
  ([MEN-4567](https://tracker.mender.io/browse/MEN-4567))


## mender-convert 2.3.0

_Released 01.20.2021_

### Statistics

A total of 858 lines added, 378 removed (delta 480)

| Developers with the most changesets | |
|---|---|
| Lluis Campos | 31 (53.4%) |
| Kristian Amlie | 9 (15.5%) |
| Drew Moseley | 7 (12.1%) |
| Ole Petter Orhagen | 6 (10.3%) |
| Nils Olav Kvelvane Johansen | 2 (3.4%) |
| Fabio Tranchitella | 1 (1.7%) |
| Mirza Krak | 1 (1.7%) |
| Alin Alexandru | 1 (1.7%) |

| Developers with the most changed lines | |
|---|---|
| Lluis Campos | 642 (71.0%) |
| Kristian Amlie | 125 (13.8%) |
| Drew Moseley | 51 (5.6%) |
| Ole Petter Orhagen | 36 (4.0%) |
| Nils Olav Kvelvane Johansen | 22 (2.4%) |
| Fabio Tranchitella | 16 (1.8%) |
| Alin Alexandru | 11 (1.2%) |
| Mirza Krak | 1 (0.1%) |

| Developers with the most lines removed | |
|---|---|
| Mirza Krak | 1 (0.3%) |

| Developers with the most signoffs (total 1) | |
|---|---|
| Lluis Campos | 1 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 57 (98.3%) |
| INNOBYTE | 1 (1.7%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 893 (98.8%) |
| INNOBYTE | 11 (1.2%) |

| Employers with the most signoffs (total 1) | |
|---|---|
| Northern.tech | 1 (100.0%) |

| Employers with the most hackers (total 8) | |
|---|---|
| Northern.tech | 7 (87.5%) |
| INNOBYTE | 1 (12.5%) |

### Changelogs

#### mender-convert (2.3.0)

New changes in mender-convert since 2.2.0:

* Fix inadvertent fstab change of fstype field.
* package: Create partitions as ext4.
* grub-efi: Fix inability to upgrade to a different kernel.
* Fix massive root filesystem corruption under some build conditions.
* Add support for overlay hooks
* beaglebone: Implement workaround for broken U-Boot and kernel.
  ([MEN-3952](https://tracker.mender.io/browse/MEN-3952))
* beaglebone: Remove U-Boot integration, which has not worked
  for a long time. U-Boot will still be used for booting, but GRUB will
  be used for integration with Mender, by chainloading via UEFI.
  ([MEN-3952](https://tracker.mender.io/browse/MEN-3952))
* Support overriding default image compression
* Do not compress output image for uncompressed input image
* Package latest released Mender-client by default
  ([QA-214](https://tracker.mender.io/browse/QA-214))
* Use separate chown and chgrp commands when creating rootfs overlay.
* Support installing mender-shell addon. Not installed by
  default, it can be configured using MENDER_ADDON_SHELL_INSTALL and
  MENDER_ADDON_SHELL_VERSION variables.
  ([MEN-4097](https://tracker.mender.io/browse/MEN-4097))
* Set mender-shell version to master
  ([MEN-4097](https://tracker.mender.io/browse/MEN-4097))
* Create demo configuration for Mender Shell addon in
  bootstrap-rootfs-overlay-demo-server.sh script
  ([MEN-4097](https://tracker.mender.io/browse/MEN-4097))
* Better parameter checks for read-only options.
* Use unique work directories when building with docker.
* Fix error when removing empty directories in rootfs/boot
* Use numeric uid and gid for better cross-compatibility.
* Now it is possible to write multiple device types in the config file using a space seperated string. Filenames for files in the deploy dir will contain all the device names seperated with +.
  ([MEN-3361](https://tracker.mender.io/browse/MEN-3361))
* Now it is possible to to select a custom filename for the deployed files by using a DEPLOY_IMAGE_NAME string in the config file.
* Set mender-connect version to latest
  ([MEN-4200](https://tracker.mender.io/browse/MEN-4200))
* Aggregated Dependabot Changelogs:
  * Bumps [tests/mender-image-tests](https://github.com/mendersoftware/mender-image-tests) from `986bd6e` to `5f88854`.
    - [Release notes](https://github.com/mendersoftware/mender-image-tests/releases)
    - [Commits](https://github.com/mendersoftware/mender-image-tests/compare/986bd6e3e932af1432ca74f4f9f0ec5a85ed7e66...5f8885448d946ee2fed099aa541e5f8c277b20c9)
  * Bump tests/mender-image-tests from `986bd6e` to `5f88854`
  * Bumps [tests/mender-image-tests](https://github.com/mendersoftware/mender-image-tests) from `5f88854` to `55c846d`.
    - [Release notes](https://github.com/mendersoftware/mender-image-tests/releases)
    - [Commits](https://github.com/mendersoftware/mender-image-tests/compare/5f8885448d946ee2fed099aa541e5f8c277b20c9...55c846d681c21045a8fa839c40dff0f07c2cc512)
  * Bumps [tests/mender-image-tests](https://github.com/mendersoftware/mender-image-tests) from `55c846d` to `cab12eb`.
    - [Release notes](https://github.com/mendersoftware/mender-image-tests/releases)
    - [Commits](https://github.com/mendersoftware/mender-image-tests/compare/55c846d681c21045a8fa839c40dff0f07c2cc512...cab12eb11c7b3aea8ae2b383037de1aae04a02b7)
  * Bump tests/mender-image-tests from `55c846d` to `cab12eb`


## Mender 2.6.0

_Released 01.20.2021_

### Statistics

A total of 95469 lines added, 31085 removed (delta 64384)

| Developers with the most changesets | |
|---|---|
| Fabio Tranchitella | 369 (30.2%) |
| Manuel Zedel | 296 (24.2%) |
| Alf-Rune Siqveland | 189 (15.5%) |
| Lluis Campos | 79 (6.5%) |
| Kristian Amlie | 76 (6.2%) |
| Peter Grzybowski | 63 (5.2%) |
| Krzysztof Jaskiewicz | 56 (4.6%) |
| Marcin Chalczynski | 36 (2.9%) |
| Ole Petter Orhagen | 33 (2.7%) |
| Armin Schlegel | 9 (0.7%) |

| Developers with the most changed lines | |
|---|---|
| Alf-Rune Siqveland | 31621 (31.1%) |
| Fabio Tranchitella | 25795 (25.4%) |
| Manuel Zedel | 21536 (21.2%) |
| Peter Grzybowski | 7415 (7.3%) |
| Krzysztof Jaskiewicz | 5404 (5.3%) |
| Kristian Amlie | 3868 (3.8%) |
| Marcin Chalczynski | 2044 (2.0%) |
| Lluis Campos | 1926 (1.9%) |
| Ole Petter Orhagen | 1239 (1.2%) |
| Michael Clelland | 234 (0.2%) |

| Developers with the most signoffs (total 1) | |
|---|---|
| Ole Petter Orhagen | 1 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 1116 (91.3%) |
| RnDity | 92 (7.5%) |
| armin.schlegel@gmx.de | 9 (0.7%) |
| TouchTunes Music Corporation | 3 (0.2%) |
| k.rohn@outlook.de | 1 (0.1%) |
| Styne13@users.noreply.github.com | 1 (0.1%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 93646 (92.2%) |
| RnDity | 7448 (7.3%) |
| armin.schlegel@gmx.de | 230 (0.2%) |
| Styne13@users.noreply.github.com | 165 (0.2%) |
| TouchTunes Music Corporation | 92 (0.1%) |
| k.rohn@outlook.de | 1 (0.0%) |

| Employers with the most signoffs (total 1) | |
|---|---|
| Northern.tech | 1 (100.0%) |

| Employers with the most hackers (total 18) | |
|---|---|
| Northern.tech | 12 (66.7%) |
| RnDity | 2 (11.1%) |
| armin.schlegel@gmx.de | 1 (5.6%) |
| Styne13@users.noreply.github.com | 1 (5.6%) |
| TouchTunes Music Corporation | 1 (5.6%) |
| k.rohn@outlook.de | 1 (5.6%) |

### Changelogs

#### auditlogs (1.0.0)

* First release of auditlogs

#### deployments (2.2.0)

New changes in deployments since 2.1.0:

* Vendor mender-artifact with `clears_artifact_provides` support.
  ([MEN-3480](https://tracker.mender.io/browse/MEN-3480))
* document artifact_provides and artifact_depends in API docs
  ([MEN-4051](https://tracker.mender.io/browse/MEN-4051))
* document artifact_provides and artifact_depends in API docs
  ([MEN-4051](https://tracker.mender.io/browse/MEN-4051))
* include clears_artifact_provides in Artifact objects
  ([MEN-4050](https://tracker.mender.io/browse/MEN-4050))
* add the possibility of creating deployments for all accepted devices
* Aggregated Dependabot Changelogs:
  * Bumps [github.com/urfave/cli](https://github.com/urfave/cli) from 1.22.4 to 1.22.5.
    - [Release notes](https://github.com/urfave/cli/releases)
    - [Changelog](https://github.com/urfave/cli/blob/master/docs/CHANGELOG.md)
    - [Commits](https://github.com/urfave/cli/compare/v1.22.4...v1.22.5)
  * Bump github.com/urfave/cli from 1.22.4 to 1.22.5
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.35.8 to 1.35.33.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.35.8...v1.35.33)
  * Bump github.com/aws/aws-sdk-go from 1.35.8 to 1.35.33
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.2 to 1.4.4.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.2...v1.4.4)
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.35.33 to 1.36.2.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.35.33...v1.36.2)
  * Bump github.com/aws/aws-sdk-go from 1.35.33 to 1.36.2
  * Bump go.mongodb.org/mongo-driver from 1.4.2 to 1.4.4
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.36.2 to 1.36.7.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.36.2...v1.36.7)
  * Bump github.com/aws/aws-sdk-go from 1.36.2 to 1.36.7
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.36.7 to 1.36.12.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.36.7...v1.36.12)
  * Bump github.com/aws/aws-sdk-go from 1.36.7 to 1.36.12
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.36.12 to 1.36.15.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.36.12...v1.36.15)
  * Bump github.com/aws/aws-sdk-go from 1.36.12 to 1.36.15
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.36.15 to 1.36.23.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.36.15...v1.36.23)
  * Bump github.com/aws/aws-sdk-go from 1.36.15 to 1.36.23

#### deployments-enterprise (2.2.0)

New changes in deployments-enterprise since 2.1.0:

* Vendor mender-artifact with `clears_artifact_provides` support.
  ([MEN-3480](https://tracker.mender.io/browse/MEN-3480))
* document artifact_provides and artifact_depends in API docs
  ([MEN-4051](https://tracker.mender.io/browse/MEN-4051))
* document artifact_provides and artifact_depends in API docs
  ([MEN-4051](https://tracker.mender.io/browse/MEN-4051))
* include clears_artifact_provides in Artifact objects
  ([MEN-4050](https://tracker.mender.io/browse/MEN-4050))
* include clears_artifact_provides in Artifact objects
  ([MEN-4050](https://tracker.mender.io/browse/MEN-4050))
* add the possibility of creating deployments for all accepted devices
* Aggregated Dependabot Changelogs:
  * Bumps [github.com/urfave/cli](https://github.com/urfave/cli) from 1.22.4 to 1.22.5.
    - [Release notes](https://github.com/urfave/cli/releases)
    - [Changelog](https://github.com/urfave/cli/blob/master/docs/CHANGELOG.md)
    - [Commits](https://github.com/urfave/cli/compare/v1.22.4...v1.22.5)
  * Bumps [github.com/urfave/cli](https://github.com/urfave/cli) from 1.22.4 to 1.22.5.
    - [Release notes](https://github.com/urfave/cli/releases)
    - [Changelog](https://github.com/urfave/cli/blob/master/docs/CHANGELOG.md)
    - [Commits](https://github.com/urfave/cli/compare/v1.22.4...v1.22.5)
  * Bump github.com/urfave/cli from 1.22.4 to 1.22.5
  * Bump github.com/urfave/cli from 1.22.4 to 1.22.5
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.35.8 to 1.35.33.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.35.8...v1.35.33)
  * Bump github.com/aws/aws-sdk-go from 1.35.8 to 1.35.33
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.35.33 to 1.35.35.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.35.33...v1.35.35)
  * Bump github.com/aws/aws-sdk-go from 1.35.33 to 1.35.35
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.35.8 to 1.35.33.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.35.8...v1.35.33)
  * Bump github.com/aws/aws-sdk-go from 1.35.8 to 1.35.33
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.2 to 1.4.4.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.2...v1.4.4)
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.35.33 to 1.36.2.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.35.33...v1.36.2)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.2 to 1.4.4.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.2...v1.4.4)
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.35.35 to 1.36.2.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.35.35...v1.36.2)
  * Bump github.com/aws/aws-sdk-go from 1.35.35 to 1.36.2
  * Bump github.com/aws/aws-sdk-go from 1.35.33 to 1.36.2
  * Bump go.mongodb.org/mongo-driver from 1.4.2 to 1.4.4
  * Bump go.mongodb.org/mongo-driver from 1.4.2 to 1.4.4
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.36.2 to 1.36.7.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.36.2...v1.36.7)
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.36.2 to 1.36.7.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.36.2...v1.36.7)
  * Bump github.com/aws/aws-sdk-go from 1.36.2 to 1.36.7
  * Bump github.com/aws/aws-sdk-go from 1.36.2 to 1.36.7
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.36.7 to 1.36.12.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.36.7...v1.36.12)
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.36.7 to 1.36.12.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.36.7...v1.36.12)
  * Bump github.com/aws/aws-sdk-go from 1.36.7 to 1.36.12
  * Bump github.com/aws/aws-sdk-go from 1.36.7 to 1.36.12
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.36.12 to 1.36.15.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.36.12...v1.36.15)
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.36.12 to 1.36.15.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.36.12...v1.36.15)
  * Bump github.com/aws/aws-sdk-go from 1.36.12 to 1.36.15
  * Bump github.com/aws/aws-sdk-go from 1.36.12 to 1.36.15
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.36.15 to 1.36.23.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.36.15...v1.36.23)
  * Bumps [github.com/aws/aws-sdk-go](https://github.com/aws/aws-sdk-go) from 1.36.15 to 1.36.23.
    - [Release notes](https://github.com/aws/aws-sdk-go/releases)
    - [Changelog](https://github.com/aws/aws-sdk-go/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/aws/aws-sdk-go/compare/v1.36.15...v1.36.23)
  * Bump github.com/aws/aws-sdk-go from 1.36.15 to 1.36.23
  * Bump github.com/aws/aws-sdk-go from 1.36.15 to 1.36.23

#### deviceauth (2.5.0)

New changes in deviceauth since 2.4.0:

* New query parameter id for GET /api/management/v1/devices
* add internal end-point to retrieve the count of devices
  ([MEN-3923](https://tracker.mender.io/browse/MEN-3923))
* New command for warning tenants approaching their device limit
* propagate device identity using workflows
  ([MEN-3979](https://tracker.mender.io/browse/MEN-3979))
* ignore tenant claim in single tenant setup
  ([MEN-3972](https://tracker.mender.io/browse/MEN-3972))
* New device auth query endpoint POST /api/management/v2/devauth/devices/search
* Aggregated Dependabot Changelogs:
  * Bumps [github.com/urfave/cli](https://github.com/urfave/cli) from 1.22.4 to 1.22.5.
    - [Release notes](https://github.com/urfave/cli/releases)
    - [Changelog](https://github.com/urfave/cli/blob/master/docs/CHANGELOG.md)
    - [Commits](https://github.com/urfave/cli/compare/v1.22.4...v1.22.5)
  * Bump github.com/urfave/cli from 1.22.4 to 1.22.5
  * Bumps [github.com/go-redis/redis/v8](https://github.com/go-redis/redis) from 8.3.1 to 8.4.2.
    - [Release notes](https://github.com/go-redis/redis/releases)
    - [Changelog](https://github.com/go-redis/redis/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/go-redis/redis/compare/v8.3.1...v8.4.2)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.2 to 1.4.4.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.2...v1.4.4)
  * Bump go.mongodb.org/mongo-driver from 1.4.2 to 1.4.4
  * Bump github.com/go-redis/redis/v8 from 8.3.1 to 8.4.2
  * Bumps [github.com/go-redis/redis/v8](https://github.com/go-redis/redis) from 8.4.2 to 8.4.4.
    - [Release notes](https://github.com/go-redis/redis/releases)
    - [Changelog](https://github.com/go-redis/redis/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/go-redis/redis/compare/v8.4.2...v8.4.4)
  * Bump github.com/go-redis/redis/v8 from 8.4.2 to 8.4.4
  * Bumps [github.com/go-redis/redis/v8](https://github.com/go-redis/redis) from 8.4.4 to 8.4.8.
    - [Release notes](https://github.com/go-redis/redis/releases)
    - [Changelog](https://github.com/go-redis/redis/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/go-redis/redis/compare/v8.4.4...v8.4.8)
  * Bump github.com/go-redis/redis/v8 from 8.4.4 to 8.4.8

#### deviceconnect (1.0.0)

* First release of deviceconnect

#### gui (2.6.0)

New changes in gui since 2.5.0:

* added additional password validation to prevent email reuse
  ([MEN-3948](https://tracker.mender.io/browse/MEN-3948))
* added security measures to prevent clickjacking
* isolated single authset handling to prevent confusing authstate notifications
  ([MEN-3988](https://tracker.mender.io/browse/MEN-3988))
* implemented auditloglist to reflect user & deployment changes
* fixed a navigation issue that prevented deployment report navigation
* fixed an error caused by showing timeframe selection for a longer time
* removed sorting limitations for device id column
  ([MEN-3879](https://tracker.mender.io/browse/MEN-3879))
* disabled sorting for status column in devices list
  ([MEN-3969](https://tracker.mender.io/browse/MEN-3969))
* allowed setting equality filters through url to ease navigation
  ([MEN-3991](https://tracker.mender.io/browse/MEN-3991))
* fixed an issue that prevented admin access to user management settings
* added possibility to update credit card in organization settings
  ([MEN-3823](https://tracker.mender.io/browse/MEN-3823))
* fixed an issue that lead certain update module configurations to crash the app
* switched device attributes from local deducation to backend retrieval
* Update "Connect a device" onboarding dialog
  ([MEN-3999](https://tracker.mender.io/browse/MEN-3999))
* device remote shell/terminal
  ([MEN-4091](https://tracker.mender.io/browse/MEN-4091))
* fixed an error that prevented phased dynamic deployments + scheduled single device deployments
  ([MEN-4122](https://tracker.mender.io/browse/MEN-4122))
* fixed deployment creation not using single devices as deployment name
  ([MEN-4182](https://tracker.mender.io/browse/MEN-4182))
* fixed an issue that prevented deployment device count from being shown in single device deployments
* ensured settings show also after stripe initialization
  ([MEN-4275](https://tracker.mender.io/browse/MEN-4275))
* fixed cookie paths to work with ui redirect to subpath
* Rename Retry deployment to Recreate deployment.
* fix page number on rowsPerPage change
  ([MEN-4364](https://tracker.mender.io/browse/MEN-4364))
* fixed an issue that prevented existing user roles from being removed
* fixed an issue that prevented loading dynamic group devices when navigating to device groups
* Aggregated Dependabot Changelogs:
  * Bumps [file-loader](https://github.com/webpack-contrib/file-loader) from 6.0.0 to 6.1.0.
    - [Release notes](https://github.com/webpack-contrib/file-loader/releases)
    - [Changelog](https://github.com/webpack-contrib/file-loader/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/file-loader/compare/v6.0.0...v6.1.0)
  * Bumps [less](https://github.com/less/less.js) from 3.11.3 to 3.12.2.
    - [Release notes](https://github.com/less/less.js/releases)
    - [Changelog](https://github.com/less/less.js/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/less/less.js/commits)
  * Bumps [copy-webpack-plugin](https://github.com/webpack-contrib/copy-webpack-plugin) from 6.0.3 to 6.1.0.
    - [Release notes](https://github.com/webpack-contrib/copy-webpack-plugin/releases)
    - [Changelog](https://github.com/webpack-contrib/copy-webpack-plugin/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/copy-webpack-plugin/compare/v6.0.3...v6.1.0)
  * Bump file-loader from 6.0.0 to 6.1.0
  * Bump less from 3.11.3 to 3.12.2
  * Bump copy-webpack-plugin from 6.0.3 to 6.1.0
  * Bumps [less-loader](https://github.com/webpack-contrib/less-loader) from 6.1.1 to 7.0.1.
    - [Release notes](https://github.com/webpack-contrib/less-loader/releases)
    - [Changelog](https://github.com/webpack-contrib/less-loader/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/less-loader/compare/v6.1.1...v7.0.1)
  * Bump less-loader from 6.1.1 to 7.0.1
  * Bumps node from 14.9.0-alpine to 14.10.1-alpine.
  * Bumps [lint-staged](https://github.com/okonet/lint-staged) from 10.2.11 to 10.3.0.
    - [Release notes](https://github.com/okonet/lint-staged/releases)
    - [Commits](https://github.com/okonet/lint-staged/compare/v10.2.11...v10.3.0)
  * Bumps [@babel/core](https://github.com/babel/babel/tree/HEAD/packages/babel-core) from 7.10.2 to 7.11.6.
    - [Release notes](https://github.com/babel/babel/releases)
    - [Changelog](https://github.com/babel/babel/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel/commits/v7.11.6/packages/babel-core)
  * Bump @babel/core from 7.10.2 to 7.11.6
  * Bump lint-staged from 10.2.11 to 10.3.0
  * Bump node from 14.9.0-alpine to 14.10.1-alpine
  * Bumps [eslint-plugin-react](https://github.com/yannickcr/eslint-plugin-react) from 7.20.1 to 7.20.6.
    - [Release notes](https://github.com/yannickcr/eslint-plugin-react/releases)
    - [Changelog](https://github.com/yannickcr/eslint-plugin-react/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/yannickcr/eslint-plugin-react/compare/v7.20.1...v7.20.6)
  * Bumps [html-webpack-plugin](https://github.com/jantimon/html-webpack-plugin) from 4.3.0 to 4.4.1.
    - [Release notes](https://github.com/jantimon/html-webpack-plugin/releases)
    - [Changelog](https://github.com/jantimon/html-webpack-plugin/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/jantimon/html-webpack-plugin/compare/v4.3.0...v4.4.1)
  * Bumps [copy-webpack-plugin](https://github.com/webpack-contrib/copy-webpack-plugin) from 6.1.0 to 6.1.1.
    - [Release notes](https://github.com/webpack-contrib/copy-webpack-plugin/releases)
    - [Changelog](https://github.com/webpack-contrib/copy-webpack-plugin/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/copy-webpack-plugin/compare/v6.1.0...v6.1.1)
  * Bumps [autoprefixer](https://github.com/postcss/autoprefixer) from 9.8.4 to 9.8.6.
    - [Release notes](https://github.com/postcss/autoprefixer/releases)
    - [Changelog](https://github.com/postcss/autoprefixer/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/postcss/autoprefixer/compare/9.8.4...9.8.6)
  * Bumps [victory](https://github.com/formidablelabs/victory) from 35.0.8 to 35.0.9.
    - [Release notes](https://github.com/formidablelabs/victory/releases)
    - [Changelog](https://github.com/FormidableLabs/victory/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/formidablelabs/victory/compare/v35.0.8...v35.0.9)
  * Bumps node from 14.10.1-alpine to 14.11.0-alpine.
  * Bump node from 14.10.1-alpine to 14.11.0-alpine
  * Bump eslint-plugin-react from 7.20.1 to 7.20.6
  * Bump copy-webpack-plugin from 6.1.0 to 6.1.1
  * Bump autoprefixer from 9.8.4 to 9.8.6
  * Bump victory from 35.0.8 to 35.0.9
  * Bump html-webpack-plugin from 4.3.0 to 4.4.1
  * Bumps [eslint-plugin-react](https://github.com/yannickcr/eslint-plugin-react) from 7.20.6 to 7.21.2.
    - [Release notes](https://github.com/yannickcr/eslint-plugin-react/releases)
    - [Changelog](https://github.com/yannickcr/eslint-plugin-react/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/yannickcr/eslint-plugin-react/commits)
  * Bumps [eslint-plugin-import](https://github.com/benmosher/eslint-plugin-import) from 2.22.0 to 2.22.1.
    - [Release notes](https://github.com/benmosher/eslint-plugin-import/releases)
    - [Changelog](https://github.com/benmosher/eslint-plugin-import/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/benmosher/eslint-plugin-import/compare/v2.22.0...v2.22.1)
  * Bumps [enzyme-adapter-react-16](https://github.com/enzymejs/enzyme/tree/HEAD/packages/enzyme-adapter-react-16) from 1.15.4 to 1.15.5.
    - [Release notes](https://github.com/enzymejs/enzyme/releases)
    - [Changelog](https://github.com/enzymejs/enzyme/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/enzymejs/enzyme/commits/enzyme-adapter-react-16@1.15.5/packages/enzyme-adapter-react-16)
  * Bumps [universal-cookie](https://github.com/reactivestack/cookies) from 4.0.3 to 4.0.4.
    - [Release notes](https://github.com/reactivestack/cookies/releases)
    - [Changelog](https://github.com/reactivestack/cookies/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/reactivestack/cookies/compare/v4.0.3...v4.0.4)
  * Bump universal-cookie from 4.0.3 to 4.0.4
  * Bump enzyme-adapter-react-16 from 1.15.4 to 1.15.5
  * Bump eslint-plugin-import from 2.22.0 to 2.22.1
  * Bump eslint-plugin-react from 7.20.6 to 7.21.2
  * Bumps [mini-css-extract-plugin](https://github.com/webpack-contrib/mini-css-extract-plugin) from 0.11.2 to 0.11.3.
    - [Release notes](https://github.com/webpack-contrib/mini-css-extract-plugin/releases)
    - [Changelog](https://github.com/webpack-contrib/mini-css-extract-plugin/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/mini-css-extract-plugin/compare/v0.11.2...v0.11.3)
  * Bumps [eslint](https://github.com/eslint/eslint) from 7.9.0 to 7.10.0.
    - [Release notes](https://github.com/eslint/eslint/releases)
    - [Changelog](https://github.com/eslint/eslint/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/eslint/eslint/compare/v7.9.0...v7.10.0)
  * Bumps [yarn](https://github.com/yarnpkg/yarn) from 1.22.5 to 1.22.10.
    - [Release notes](https://github.com/yarnpkg/yarn/releases)
    - [Changelog](https://github.com/yarnpkg/yarn/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/yarnpkg/yarn/compare/v1.22.5...1.22.10)
  * Bumps [jwt-decode](https://github.com/auth0/jwt-decode) from 2.2.0 to 3.0.0.
    - [Release notes](https://github.com/auth0/jwt-decode/releases)
    - [Changelog](https://github.com/auth0/jwt-decode/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/auth0/jwt-decode/compare/v2.2.0...v3.0.0)
  * Bumps node from 14.11.0-alpine to 14.12.0-alpine.
  * Bump node from 14.11.0-alpine to 14.12.0-alpine
  * Bump jwt-decode from 2.2.0 to 3.0.0
  * Bump yarn from 1.22.5 to 1.22.10
  * Bump eslint from 7.9.0 to 7.10.0
  * Bump mini-css-extract-plugin from 0.11.2 to 0.11.3
  * Bumps [copy-webpack-plugin](https://github.com/webpack-contrib/copy-webpack-plugin) from 6.1.1 to 6.2.1.
    - [Release notes](https://github.com/webpack-contrib/copy-webpack-plugin/releases)
    - [Changelog](https://github.com/webpack-contrib/copy-webpack-plugin/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/copy-webpack-plugin/compare/v6.1.1...v6.2.1)
  * Bumps [jest](https://github.com/facebook/jest) from 26.4.2 to 26.5.3.
    - [Release notes](https://github.com/facebook/jest/releases)
    - [Changelog](https://github.com/facebook/jest/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/facebook/jest/compare/v26.4.2...v26.5.3)
  * Bumps [eslint-plugin-react](https://github.com/yannickcr/eslint-plugin-react) from 7.21.2 to 7.21.4.
    - [Release notes](https://github.com/yannickcr/eslint-plugin-react/releases)
    - [Changelog](https://github.com/yannickcr/eslint-plugin-react/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/yannickcr/eslint-plugin-react/compare/v7.21.2...v7.21.4)
  * Bumps node from 14.12.0-alpine to 14.13.1-alpine.
  * Bumps nginx from 1.19.2-alpine to 1.19.3-alpine.
  * Bump nginx from 1.19.2-alpine to 1.19.3-alpine
  * Bump node from 14.12.0-alpine to 14.13.1-alpine
  * Bump eslint-plugin-react from 7.21.2 to 7.21.4
  * Bump jest from 26.4.2 to 26.5.3
  * Bump copy-webpack-plugin from 6.1.1 to 6.2.1
  * Bumps [url-loader](https://github.com/webpack-contrib/url-loader) from 4.1.0 to 4.1.1.
    - [Release notes](https://github.com/webpack-contrib/url-loader/releases)
    - [Changelog](https://github.com/webpack-contrib/url-loader/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/url-loader/compare/v4.1.0...v4.1.1)
  * Bumps [file-loader](https://github.com/webpack-contrib/file-loader) from 6.1.0 to 6.1.1.
    - [Release notes](https://github.com/webpack-contrib/file-loader/releases)
    - [Changelog](https://github.com/webpack-contrib/file-loader/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/file-loader/compare/v6.1.0...v6.1.1)
  * Bumps [@babel/core](https://github.com/babel/babel/tree/HEAD/packages/babel-core) from 7.11.6 to 7.12.3.
    - [Release notes](https://github.com/babel/babel/releases)
    - [Changelog](https://github.com/babel/babel/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel/commits/v7.12.3/packages/babel-core)
  * Bumps node from 14.13.1-alpine to 14.14.0-alpine.
  * Bump @babel/core from 7.11.6 to 7.12.3
  * Bump file-loader from 6.1.0 to 6.1.1
  * Bump url-loader from 4.1.0 to 4.1.1
  * Bump node from 14.13.1-alpine to 14.14.0-alpine
  * Bumps [react-dropzone](https://github.com/react-dropzone/react-dropzone) from 11.2.0 to 11.2.1.
    - [Release notes](https://github.com/react-dropzone/react-dropzone/releases)
    - [Commits](https://github.com/react-dropzone/react-dropzone/compare/v11.2.0...v11.2.1)
  * Bumps [resolve-url-loader](https://github.com/bholloway/resolve-url-loader) from 3.1.1 to 3.1.2.
    - [Release notes](https://github.com/bholloway/resolve-url-loader/releases)
    - [Commits](https://github.com/bholloway/resolve-url-loader/compare/3.1.1...3.1.2)
  * Bumps node from 14.14.0-alpine to 15.0.1-alpine.
  * Bump resolve-url-loader from 3.1.1 to 3.1.2
  * Bump react-dropzone from 11.2.0 to 11.2.1
  * Bump node from 14.14.0-alpine to 15.0.1-alpine
  * Bumps [react-ga](https://github.com/react-ga/react-ga) from 3.1.2 to 3.2.0.
    - [Release notes](https://github.com/react-ga/react-ga/releases)
    - [Commits](https://github.com/react-ga/react-ga/compare/v3.1.2...v3.2.0)
  * Bump react-ga from 3.1.2 to 3.2.0
  * Bumps [@babel/preset-react](https://github.com/babel/babel/tree/HEAD/packages/babel-preset-react) from 7.10.4 to 7.12.1.
    - [Release notes](https://github.com/babel/babel/releases)
    - [Changelog](https://github.com/babel/babel/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel/commits/v7.12.1/packages/babel-preset-react)
  * Bumps [react-idle-timer](https://github.com/supremetechnopriest/react-idle-timer) from 4.3.6 to 4.5.0.
    - [Release notes](https://github.com/supremetechnopriest/react-idle-timer/releases)
    - [Changelog](https://github.com/SupremeTechnopriest/react-idle-timer/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/supremetechnopriest/react-idle-timer/compare/4.3.6...4.5.0)
  * Bumps [@mdi/js](https://github.com/Templarian/MaterialDesign-JS) from 5.6.55 to 5.8.55.
    - [Release notes](https://github.com/Templarian/MaterialDesign-JS/releases)
    - [Commits](https://github.com/Templarian/MaterialDesign-JS/compare/v5.6.55...v5.8.55)
  * Bump @mdi/js from 5.6.55 to 5.8.55
  * Bump react-idle-timer from 4.3.6 to 4.5.0
  * Bump @babel/preset-react from 7.10.4 to 7.12.1
  * Bumps node from 15.0.1-alpine to 15.1.0-alpine.
  * Bumps nginx from 1.19.3-alpine to 1.19.4-alpine.
  * Bump nginx from 1.19.3-alpine to 1.19.4-alpine
  * Bump node from 15.0.1-alpine to 15.1.0-alpine
  * Bumps [postcss](https://github.com/postcss/postcss) from 8.1.4 to 8.1.6.
    - [Release notes](https://github.com/postcss/postcss/releases)
    - [Changelog](https://github.com/postcss/postcss/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/postcss/postcss/compare/8.1.4...8.1.6)
  * Bump postcss from 8.1.4 to 8.1.6
  * Bumps node from 15.1.0-alpine to 15.2.0-alpine.
  * Bumps [cypress-localstorage-commands](https://github.com/javierbrea/cypress-localstorage-commands) from 1.2.3 to 1.2.4.
    - [Release notes](https://github.com/javierbrea/cypress-localstorage-commands/releases)
    - [Changelog](https://github.com/javierbrea/cypress-localstorage-commands/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/javierbrea/cypress-localstorage-commands/compare/v1.2.3...v1.2.4)
  * Bumps [jwt-decode](https://github.com/auth0/jwt-decode) from 2.2.0 to 3.1.1.
    - [Release notes](https://github.com/auth0/jwt-decode/releases)
    - [Changelog](https://github.com/auth0/jwt-decode/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/auth0/jwt-decode/compare/v2.2.0...v3.1.1)
  * Bumps [cypress](https://github.com/cypress-io/cypress) from 5.4.0 to 5.6.0.
    - [Release notes](https://github.com/cypress-io/cypress/releases)
    - [Changelog](https://github.com/cypress-io/cypress/blob/develop/.releaserc.base.js)
    - [Commits](https://github.com/cypress-io/cypress/compare/v5.4.0...v5.6.0)
  * Bumps [eslint-plugin-cypress](https://github.com/cypress-io/eslint-plugin-cypress) from 2.11.1 to 2.11.2.
    - [Release notes](https://github.com/cypress-io/eslint-plugin-cypress/releases)
    - [Commits](https://github.com/cypress-io/eslint-plugin-cypress/compare/v2.11.1...v2.11.2)
  * Bumps [less-loader](https://github.com/webpack-contrib/less-loader) from 7.0.2 to 7.1.0.
    - [Release notes](https://github.com/webpack-contrib/less-loader/releases)
    - [Changelog](https://github.com/webpack-contrib/less-loader/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/less-loader/compare/v7.0.2...v7.1.0)
  * Bump node from 15.1.0-alpine to 15.2.0-alpine
  * Bump jwt-decode from 2.2.0 to 3.1.1 in /tests/e2e_tests
  * Bump eslint-plugin-cypress from 2.11.1 to 2.11.2
  * Bump less-loader from 7.0.2 to 7.1.0
  * Bump cypress from 5.4.0 to 5.6.0 in /tests/e2e_tests
  * Bump cypress-localstorage-commands from 1.2.3 to 1.2.4 in /tests/e2e_tests
  * Bumps [react](https://github.com/facebook/react/tree/HEAD/packages/react) from 16.13.1 to 16.14.0.
    - [Release notes](https://github.com/facebook/react/releases)
    - [Changelog](https://github.com/facebook/react/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/facebook/react/commits/v16.14.0/packages/react)
  * Bump react from 16.13.1 to 16.14.0
  * Bumps cypress/included from 5.4.0 to 5.6.0.
  * Bump cypress/included from 5.4.0 to 5.6.0 in /tests/e2e_tests
  * Bumps [autoprefixer](https://github.com/postcss/autoprefixer) from 10.0.1 to 10.0.2.
    - [Release notes](https://github.com/postcss/autoprefixer/releases)
    - [Changelog](https://github.com/postcss/autoprefixer/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/postcss/autoprefixer/compare/10.0.1...10.0.2)
  * Bumps [mini-css-extract-plugin](https://github.com/webpack-contrib/mini-css-extract-plugin) from 1.2.1 to 1.3.1.
    - [Release notes](https://github.com/webpack-contrib/mini-css-extract-plugin/releases)
    - [Changelog](https://github.com/webpack-contrib/mini-css-extract-plugin/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/mini-css-extract-plugin/compare/v1.2.1...v1.3.1)
  * Bumps [css-loader](https://github.com/webpack-contrib/css-loader) from 5.0.0 to 5.0.1.
    - [Release notes](https://github.com/webpack-contrib/css-loader/releases)
    - [Changelog](https://github.com/webpack-contrib/css-loader/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/css-loader/compare/v5.0.0...v5.0.1)
  * Bump css-loader from 5.0.0 to 5.0.1
  * Bump mini-css-extract-plugin from 1.2.1 to 1.3.1
  * Bump autoprefixer from 10.0.1 to 10.0.2
  * Bumps [react-dom](https://github.com/facebook/react/tree/HEAD/packages/react-dom) from 16.13.1 to 16.14.0.
    - [Release notes](https://github.com/facebook/react/releases)
    - [Changelog](https://github.com/facebook/react/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/facebook/react/commits/v16.14.0/packages/react-dom)
  * Bumps [react-big-calendar](https://github.com/jquense/react-big-calendar) from 0.28.2 to 0.28.6.
    - [Release notes](https://github.com/jquense/react-big-calendar/releases)
    - [Changelog](https://github.com/jquense/react-big-calendar/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/jquense/react-big-calendar/compare/v0.28.2...v0.28.6)
  * Bumps [@babel/preset-env](https://github.com/babel/babel/tree/HEAD/packages/babel-preset-env) from 7.12.1 to 7.12.7.
    - [Release notes](https://github.com/babel/babel/releases)
    - [Changelog](https://github.com/babel/babel/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel/commits/v7.12.7/packages/babel-preset-env)
  * Bumps node from 15.2.0-alpine to 15.2.1-alpine.
  * Bumps [jwt-decode](https://github.com/auth0/jwt-decode) from 3.1.1 to 3.1.2.
    - [Release notes](https://github.com/auth0/jwt-decode/releases)
    - [Changelog](https://github.com/auth0/jwt-decode/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/auth0/jwt-decode/compare/v3.1.1...v3.1.2)
  * Bump jwt-decode from 3.1.1 to 3.1.2 in /tests/e2e_tests
  * Bump node from 15.2.0-alpine to 15.2.1-alpine
  * Bump @babel/preset-env from 7.12.1 to 7.12.7
  * Bump react-big-calendar from 0.28.2 to 0.28.6
  * Bump react-dom from 16.13.1 to 16.14.0
  * Bumps [lint-staged](https://github.com/okonet/lint-staged) from 10.5.1 to 10.5.2.
    - [Release notes](https://github.com/okonet/lint-staged/releases)
    - [Commits](https://github.com/okonet/lint-staged/compare/v10.5.1...v10.5.2)
  * Bumps [@babel/preset-react](https://github.com/babel/babel/tree/HEAD/packages/babel-preset-react) from 7.12.5 to 7.12.7.
    - [Release notes](https://github.com/babel/babel/releases)
    - [Changelog](https://github.com/babel/babel/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel/commits/v7.12.7/packages/babel-preset-react)
  * Bumps [@material-ui/core](https://github.com/mui-org/material-ui/tree/HEAD/packages/material-ui) from 4.11.0 to 4.11.1.
    - [Release notes](https://github.com/mui-org/material-ui/releases)
    - [Changelog](https://github.com/mui-org/material-ui/blob/v4.11.1/CHANGELOG.md)
    - [Commits](https://github.com/mui-org/material-ui/commits/v4.11.1/packages/material-ui)
  * Bumps [buffer](https://github.com/feross/buffer) from 6.0.0 to 6.0.3.
    - [Release notes](https://github.com/feross/buffer/releases)
    - [Commits](https://github.com/feross/buffer/compare/v6.0.0...v6.0.3)
  * Bumps nginx from 1.19.4-alpine to 1.19.5-alpine.
  * Bumps node from 15.2.1-alpine to 15.3.0-alpine.
  * Bump lint-staged from 10.5.1 to 10.5.2
  * Bump @babel/preset-react from 7.12.5 to 7.12.7
  * Bump @material-ui/core from 4.11.0 to 4.11.1
  * Bump node from 15.2.1-alpine to 15.3.0-alpine
  * Bump buffer from 6.0.0 to 6.0.3
  * Bump nginx from 1.19.4-alpine to 1.19.5-alpine
  * Bumps cypress/included from 5.6.0 to 6.0.0.
  * Bump cypress/included from 5.6.0 to 6.0.0 in /tests/e2e_tests
  * Bumps [eslint](https://github.com/eslint/eslint) from 7.12.1 to 7.14.0.
    - [Release notes](https://github.com/eslint/eslint/releases)
    - [Changelog](https://github.com/eslint/eslint/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/eslint/eslint/compare/v7.12.1...v7.14.0)
  * Bumps [postcss](https://github.com/postcss/postcss) from 8.1.6 to 8.1.10.
    - [Release notes](https://github.com/postcss/postcss/releases)
    - [Changelog](https://github.com/postcss/postcss/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/postcss/postcss/compare/8.1.6...8.1.10)
  * Bumps [@babel/core](https://github.com/babel/babel/tree/HEAD/packages/babel-core) from 7.12.3 to 7.12.9.
    - [Release notes](https://github.com/babel/babel/releases)
    - [Changelog](https://github.com/babel/babel/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel/commits/v7.12.9/packages/babel-core)
  * Bumps [react-dropzone](https://github.com/react-dropzone/react-dropzone) from 11.2.3 to 11.2.4.
    - [Release notes](https://github.com/react-dropzone/react-dropzone/releases)
    - [Commits](https://github.com/react-dropzone/react-dropzone/compare/v11.2.3...v11.2.4)
  * Bump react-dropzone from 11.2.3 to 11.2.4
  * Bump @babel/core from 7.12.3 to 7.12.9
  * Bump postcss from 8.1.6 to 8.1.10
  * Bump eslint from 7.12.1 to 7.14.0
  * Bumps [webpack](https://github.com/webpack/webpack) from 5.4.0 to 5.9.0.
    - [Release notes](https://github.com/webpack/webpack/releases)
    - [Commits](https://github.com/webpack/webpack/compare/v5.4.0...v5.9.0)
  * Bumps [prettier](https://github.com/prettier/prettier) from 2.1.2 to 2.2.1.
    - [Release notes](https://github.com/prettier/prettier/releases)
    - [Changelog](https://github.com/prettier/prettier/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/prettier/prettier/compare/2.1.2...2.2.1)
  * Bumps [react-ga](https://github.com/react-ga/react-ga) from 3.2.0 to 3.3.0.
    - [Release notes](https://github.com/react-ga/react-ga/releases)
    - [Commits](https://github.com/react-ga/react-ga/compare/v3.2.0...v3.3.0)
  * Bump react-ga from 3.2.0 to 3.3.0
  * Bump prettier from 2.1.2 to 2.2.1
  * Bump webpack from 5.4.0 to 5.9.0
  * Bumps [postcss-loader](https://github.com/webpack-contrib/postcss-loader) from 4.0.4 to 4.1.0.
    - [Release notes](https://github.com/webpack-contrib/postcss-loader/releases)
    - [Changelog](https://github.com/webpack-contrib/postcss-loader/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/postcss-loader/compare/v4.0.4...v4.1.0)
  * Bump postcss-loader from 4.0.4 to 4.1.0
  * Bumps [autoprefixer](https://github.com/postcss/autoprefixer) from 10.0.2 to 10.0.4.
    - [Release notes](https://github.com/postcss/autoprefixer/releases)
    - [Changelog](https://github.com/postcss/autoprefixer/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/postcss/autoprefixer/compare/10.0.2...10.0.4)
  * Bumps [babel-loader](https://github.com/babel/babel-loader) from 8.1.0 to 8.2.2.
    - [Release notes](https://github.com/babel/babel-loader/releases)
    - [Changelog](https://github.com/babel/babel-loader/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel-loader/compare/v8.1.0...v8.2.2)
  * Bumps [core-js](https://github.com/zloirock/core-js) from 3.6.5 to 3.8.0.
    - [Release notes](https://github.com/zloirock/core-js/releases)
    - [Changelog](https://github.com/zloirock/core-js/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/zloirock/core-js/compare/v3.6.5...v3.8.0)
  * Bump babel-loader from 8.1.0 to 8.2.2
  * Bump autoprefixer from 10.0.2 to 10.0.4
  * Bump core-js from 3.6.5 to 3.8.0
  * Bumps [jwt-decode](https://github.com/auth0/jwt-decode) from 3.0.0 to 3.1.2.
    - [Release notes](https://github.com/auth0/jwt-decode/releases)
    - [Changelog](https://github.com/auth0/jwt-decode/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/auth0/jwt-decode/compare/v3.0.0...v3.1.2)
  * Bumps [validator](https://github.com/chriso/validator.js) from 13.1.17 to 13.5.1.
    - [Release notes](https://github.com/chriso/validator.js/releases)
    - [Changelog](https://github.com/validatorjs/validator.js/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/chriso/validator.js/compare/13.1.17...13.5.1)
  * Bump jwt-decode from 3.0.0 to 3.1.2
  * Bump validator from 13.1.17 to 13.5.1
  * Bumps [core-js](https://github.com/zloirock/core-js) from 3.8.0 to 3.8.1.
    - [Release notes](https://github.com/zloirock/core-js/releases)
    - [Changelog](https://github.com/zloirock/core-js/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/zloirock/core-js/compare/v3.8.0...v3.8.1)
  * Bumps [mini-css-extract-plugin](https://github.com/webpack-contrib/mini-css-extract-plugin) from 1.3.1 to 1.3.2.
    - [Release notes](https://github.com/webpack-contrib/mini-css-extract-plugin/releases)
    - [Changelog](https://github.com/webpack-contrib/mini-css-extract-plugin/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/mini-css-extract-plugin/compare/v1.3.1...v1.3.2)
  * Bumps [@cypress/skip-test](https://github.com/cypress-io/cypress-skip-test) from 2.5.0 to 2.5.1.
    - [Release notes](https://github.com/cypress-io/cypress-skip-test/releases)
    - [Commits](https://github.com/cypress-io/cypress-skip-test/compare/v2.5.0...v2.5.1)
  * Bumps [cypress-localstorage-commands](https://github.com/javierbrea/cypress-localstorage-commands) from 1.2.4 to 1.2.5.
    - [Release notes](https://github.com/javierbrea/cypress-localstorage-commands/releases)
    - [Changelog](https://github.com/javierbrea/cypress-localstorage-commands/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/javierbrea/cypress-localstorage-commands/compare/v1.2.4...v1.2.5)
  * Bumps cypress/included from 6.0.0 to 6.0.1.
  * Bump mini-css-extract-plugin from 1.3.1 to 1.3.2
  * Bump @cypress/skip-test from 2.5.0 to 2.5.1 in /tests/e2e_tests
  * Bump cypress-localstorage-commands from 1.2.4 to 1.2.5 in /tests/e2e_tests
  * Bump cypress/included from 6.0.0 to 6.0.1 in /tests/e2e_tests
  * Bump core-js from 3.8.0 to 3.8.1
  * Bumps [webpack](https://github.com/webpack/webpack) from 5.9.0 to 5.10.0.
    - [Release notes](https://github.com/webpack/webpack/releases)
    - [Commits](https://github.com/webpack/webpack/compare/v5.9.0...v5.10.0)
  * Bump webpack from 5.9.0 to 5.10.0
  * Bumps [lint-staged](https://github.com/okonet/lint-staged) from 10.5.2 to 10.5.3.
    - [Release notes](https://github.com/okonet/lint-staged/releases)
    - [Commits](https://github.com/okonet/lint-staged/compare/v10.5.2...v10.5.3)
  * Bumps [eslint-plugin-prettier](https://github.com/prettier/eslint-plugin-prettier) from 3.1.4 to 3.2.0.
    - [Release notes](https://github.com/prettier/eslint-plugin-prettier/releases)
    - [Changelog](https://github.com/prettier/eslint-plugin-prettier/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/prettier/eslint-plugin-prettier/compare/v3.1.4...v3.2.0)
  * Bumps [postcss](https://github.com/postcss/postcss) from 8.1.10 to 8.1.14.
    - [Release notes](https://github.com/postcss/postcss/releases)
    - [Changelog](https://github.com/postcss/postcss/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/postcss/postcss/compare/8.1.10...8.1.14)
  * Bump lint-staged from 10.5.2 to 10.5.3
  * Bump postcss from 8.1.10 to 8.1.14
  * Bump eslint-plugin-prettier from 3.1.4 to 3.2.0
  * Bumps [ini](https://github.com/isaacs/ini) from 1.3.5 to 1.3.7.
    - [Release notes](https://github.com/isaacs/ini/releases)
    - [Commits](https://github.com/isaacs/ini/compare/v1.3.5...v1.3.7)
  * Bumps [ini](https://github.com/isaacs/ini) from 1.3.5 to 1.3.8.
    - [Release notes](https://github.com/isaacs/ini/releases)
    - [Commits](https://github.com/isaacs/ini/compare/v1.3.5...v1.3.8)
  * Bumps [@babel/preset-env](https://github.com/babel/babel/tree/HEAD/packages/babel-preset-env) from 7.12.7 to 7.12.10.
    - [Release notes](https://github.com/babel/babel/releases)
    - [Changelog](https://github.com/babel/babel/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel/commits/v7.12.10/packages/babel-preset-env)
  * Bumps [webpack](https://github.com/webpack/webpack) from 5.10.0 to 5.10.1.
    - [Release notes](https://github.com/webpack/webpack/releases)
    - [Commits](https://github.com/webpack/webpack/compare/v5.10.0...v5.10.1)
  * Bumps [cypress-localstorage-commands](https://github.com/javierbrea/cypress-localstorage-commands) from 1.2.5 to 1.3.1.
    - [Release notes](https://github.com/javierbrea/cypress-localstorage-commands/releases)
    - [Changelog](https://github.com/javierbrea/cypress-localstorage-commands/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/javierbrea/cypress-localstorage-commands/compare/v1.2.5...v1.3.1)
  * Bumps [uuid](https://github.com/uuidjs/uuid) from 8.3.1 to 8.3.2.
    - [Release notes](https://github.com/uuidjs/uuid/releases)
    - [Changelog](https://github.com/uuidjs/uuid/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/uuidjs/uuid/compare/v8.3.1...v8.3.2)
  * Bumps node from 15.3.0-alpine to 15.4.0-alpine.
  * Bumps cypress/included from 6.0.1 to 6.1.0.
  * Bump cypress/included from 6.0.1 to 6.1.0 in /tests/e2e_tests
  * Bump node from 15.3.0-alpine to 15.4.0-alpine
  * Bump uuid from 8.3.1 to 8.3.2 in /tests/e2e_tests
  * Bump cypress-localstorage-commands from 1.2.5 to 1.3.1 in /tests/e2e_tests
  * Bump @babel/preset-env from 7.12.7 to 7.12.10
  * Bump ini from 1.3.5 to 1.3.8 in /tests/e2e_tests
  * Bump webpack from 5.10.0 to 5.10.1
  * Bump ini from 1.3.5 to 1.3.7
  * Bumps [autoprefixer](https://github.com/postcss/autoprefixer) from 10.0.4 to 10.1.0.
    - [Release notes](https://github.com/postcss/autoprefixer/releases)
    - [Changelog](https://github.com/postcss/autoprefixer/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/postcss/autoprefixer/compare/10.0.4...10.1.0)
  * Bumps [@babel/preset-react](https://github.com/babel/babel/tree/HEAD/packages/babel-preset-react) from 7.12.7 to 7.12.10.
    - [Release notes](https://github.com/babel/babel/releases)
    - [Changelog](https://github.com/babel/babel/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel/commits/v7.12.10/packages/babel-preset-react)
  * Bumps nginx from 1.19.5-alpine to 1.19.6-alpine.
  * Bump nginx from 1.19.5-alpine to 1.19.6-alpine
  * Bump autoprefixer from 10.0.4 to 10.1.0
  * Bump @babel/preset-react from 7.12.7 to 7.12.10
  * Bumps node from 15.4.0-alpine to 15.5.0-alpine.
  * Bump node from 15.4.0-alpine to 15.5.0-alpine
  * Bumps [@testing-library/jest-dom](https://github.com/testing-library/jest-dom) from 5.11.6 to 5.11.8.
    - [Release notes](https://github.com/testing-library/jest-dom/releases)
    - [Changelog](https://github.com/testing-library/jest-dom/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/testing-library/jest-dom/compare/v5.11.6...v5.11.8)
  * Bump @testing-library/jest-dom from 5.11.6 to 5.11.8
  * Bumps [core-js](https://github.com/zloirock/core-js) from 3.8.1 to 3.8.2.
    - [Release notes](https://github.com/zloirock/core-js/releases)
    - [Changelog](https://github.com/zloirock/core-js/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/zloirock/core-js/compare/v3.8.1...v3.8.2)
  * Bump core-js from 3.8.1 to 3.8.2
  * Bumps [@testing-library/dom](https://github.com/testing-library/dom-testing-library) from 7.29.0 to 7.29.1.
    - [Release notes](https://github.com/testing-library/dom-testing-library/releases)
    - [Changelog](https://github.com/testing-library/dom-testing-library/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/testing-library/dom-testing-library/compare/v7.29.0...v7.29.1)
  * Bumps [msgpack5](https://github.com/mcollina/msgpack5) from 4.2.1 to 5.0.0.
    - [Release notes](https://github.com/mcollina/msgpack5/releases)
    - [Commits](https://github.com/mcollina/msgpack5/commits/v5.0.0)
  * Bumps [eslint](https://github.com/eslint/eslint) from 7.16.0 to 7.17.0.
    - [Release notes](https://github.com/eslint/eslint/releases)
    - [Changelog](https://github.com/eslint/eslint/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/eslint/eslint/compare/v7.16.0...v7.17.0)
  * Bumps [html-webpack-plugin](https://github.com/jantimon/html-webpack-plugin) from 4.5.0 to 4.5.1.
    - [Release notes](https://github.com/jantimon/html-webpack-plugin/releases)
    - [Changelog](https://github.com/jantimon/html-webpack-plugin/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/jantimon/html-webpack-plugin/compare/v4.5.0...v4.5.1)
  * Bump html-webpack-plugin from 4.5.0 to 4.5.1
  * Bump eslint from 7.16.0 to 7.17.0
  * Bump @testing-library/dom from 7.29.0 to 7.29.1
  * Bumps [webpack](https://github.com/webpack/webpack) from 5.11.0 to 5.11.1.
    - [Release notes](https://github.com/webpack/webpack/releases)
    - [Commits](https://github.com/webpack/webpack/compare/v5.11.0...v5.11.1)
  * Bumps [eslint-plugin-prettier](https://github.com/prettier/eslint-plugin-prettier) from 3.3.0 to 3.3.1.
    - [Release notes](https://github.com/prettier/eslint-plugin-prettier/releases)
    - [Changelog](https://github.com/prettier/eslint-plugin-prettier/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/prettier/eslint-plugin-prettier/compare/v3.3.0...v3.3.1)
  * Bump eslint-plugin-prettier from 3.3.0 to 3.3.1
  * Bump webpack from 5.11.0 to 5.11.1
  * Bumps [msw](https://github.com/mswjs/msw) from 0.24.2 to 0.25.0.
    - [Release notes](https://github.com/mswjs/msw/releases)
    - [Changelog](https://github.com/mswjs/msw/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/mswjs/msw/compare/v0.24.2...v0.25.0)
  * Bumps [postcss](https://github.com/postcss/postcss) from 8.2.1 to 8.2.2.
    - [Release notes](https://github.com/postcss/postcss/releases)
    - [Changelog](https://github.com/postcss/postcss/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/postcss/postcss/compare/8.2.1...8.2.2)
  * Bumps [less](https://github.com/less/less.js) from 3.12.2 to 3.13.1.
    - [Release notes](https://github.com/less/less.js/releases)
    - [Changelog](https://github.com/less/less.js/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/less/less.js/compare/v3.12.2...v3.13.1)
  * Bumps [axios](https://github.com/axios/axios) from 0.21.0 to 0.21.1.
    - [Release notes](https://github.com/axios/axios/releases)
    - [Changelog](https://github.com/axios/axios/blob/v0.21.1/CHANGELOG.md)
    - [Commits](https://github.com/axios/axios/compare/v0.21.0...v0.21.1)
  * Bumps [eslint-plugin-react](https://github.com/yannickcr/eslint-plugin-react) from 7.21.5 to 7.22.0.
    - [Release notes](https://github.com/yannickcr/eslint-plugin-react/releases)
    - [Changelog](https://github.com/yannickcr/eslint-plugin-react/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/yannickcr/eslint-plugin-react/compare/v7.21.5...v7.22.0)
  * Bump axios from 0.21.0 to 0.21.1
  * Bump eslint-plugin-react from 7.21.5 to 7.22.0
  * Bumps [less-loader](https://github.com/webpack-contrib/less-loader) from 7.1.0 to 7.2.1.
    - [Release notes](https://github.com/webpack-contrib/less-loader/releases)
    - [Changelog](https://github.com/webpack-contrib/less-loader/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/less-loader/compare/v7.1.0...v7.2.1)
  * Bump msgpack5 from 4.2.1 to 5.0.0
  * Bumps [webpack](https://github.com/webpack/webpack) from 5.11.1 to 5.12.1.
    - [Release notes](https://github.com/webpack/webpack/releases)
    - [Commits](https://github.com/webpack/webpack/compare/v5.11.1...v5.12.1)
  * Bumps [react-idle-timer](https://github.com/supremetechnopriest/react-idle-timer) from 4.5.0 to 4.5.1.
    - [Release notes](https://github.com/supremetechnopriest/react-idle-timer/releases)
    - [Changelog](https://github.com/SupremeTechnopriest/react-idle-timer/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/supremetechnopriest/react-idle-timer/compare/4.5.0...4.5.1)
  * Bumps [autoprefixer](https://github.com/postcss/autoprefixer) from 10.2.0 to 10.2.1.
    - [Release notes](https://github.com/postcss/autoprefixer/releases)
    - [Changelog](https://github.com/postcss/autoprefixer/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/postcss/autoprefixer/compare/10.2.0...10.2.1)
  * Bumps [@testing-library/react](https://github.com/testing-library/react-testing-library) from 11.2.2 to 11.2.3.
    - [Release notes](https://github.com/testing-library/react-testing-library/releases)
    - [Changelog](https://github.com/testing-library/react-testing-library/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/testing-library/react-testing-library/compare/v11.2.2...v11.2.3)
  * Bump @testing-library/react from 11.2.2 to 11.2.3
  * Bump autoprefixer from 10.2.0 to 10.2.1
  * Bump react-idle-timer from 4.5.0 to 4.5.1
  * Bump webpack from 5.11.1 to 5.12.1
  * Bumps [webpack](https://github.com/webpack/webpack) from 5.12.1 to 5.12.3.
    - [Release notes](https://github.com/webpack/webpack/releases)
    - [Commits](https://github.com/webpack/webpack/compare/v5.12.1...v5.12.3)
  * Bumps [postcss](https://github.com/postcss/postcss) from 8.2.3 to 8.2.4.
    - [Release notes](https://github.com/postcss/postcss/releases)
    - [Changelog](https://github.com/postcss/postcss/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/postcss/postcss/compare/8.2.3...8.2.4)
  * Bumps [less](https://github.com/less/less.js) from 4.0.0 to 4.1.0.
    - [Release notes](https://github.com/less/less.js/releases)
    - [Changelog](https://github.com/less/less.js/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/less/less.js/compare/v4.0.0...v4.1.0)
  * Bumps node from 15.5.0-alpine to 15.5.1-alpine.
  * Bump node from 15.5.0-alpine to 15.5.1-alpine
  * Bump less from 4.0.0 to 4.1.0
  * Bump postcss from 8.2.3 to 8.2.4
  * Bump webpack from 5.12.1 to 5.12.3

#### integration (2.6.0)

New changes in integration since 2.5.0:

* New compose file to optionally add deviceconnect service to the backend
* New compose file to optionally add deviceconnect service to the backend
* demo script, include docker-compose.connect.yml by default
  ([MEN-4357](https://tracker.mender.io/browse/MEN-4357))
* Add auditlogs and deviceconnect to production templates
* Add auditlogs 1.0.0.
* Upgrade deployments to 2.2.0.
* Upgrade deployments-enterprise to 2.2.0.
* Upgrade deviceauth to 2.5.0.
* Add deviceconnect 1.0.0.
* Upgrade gui to 2.6.0.
* Upgrade inventory to 2.2.0.
* Upgrade inventory-enterprise to 2.2.0.
* Upgrade mender to 2.5.0.
* Upgrade mender-api-gateway-docker to 2.4.0.
* Upgrade mender-artifact to 3.5.0.
* Upgrade mender-cli to 1.6.0.
* Add mender-connect 1.0.0.
* Upgrade tenantadm to 3.0.0.
* Upgrade useradm to 1.13.0.
* Upgrade useradm-enterprise to 1.13.0.
* Upgrade workflows to 1.3.0.
* Upgrade workflows-enterprise to 1.3.0.
* Aggregated Dependabot Changelogs:
  * Bumps [stripe](https://github.com/stripe/stripe-python) from 2.50.0 to 2.51.0.
    - [Release notes](https://github.com/stripe/stripe-python/releases)
    - [Changelog](https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/stripe/stripe-python/compare/v2.50.0...v2.51.0)
  * Bump stripe from 2.50.0 to 2.51.0 in /backend-tests
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 6.0.1 to 6.0.2.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/6.0.1...6.0.2)
  * Bumps [docker-compose](https://github.com/docker/compose) from 1.26.2 to 1.27.2.
    - [Release notes](https://github.com/docker/compose/releases)
    - [Changelog](https://github.com/docker/compose/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/docker/compose/compare/1.26.2...1.27.2)
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 6.0.1 to 6.0.2.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/6.0.1...6.0.2)
  * Bump pytest from 6.0.1 to 6.0.2 in /tests/requirements
  * Bump docker-compose from 1.26.2 to 1.27.2 in /tests/requirements
  * Bump pytest from 6.0.1 to 6.0.2 in /backend-tests
  * Bumps [docker-compose](https://github.com/docker/compose) from 1.27.2 to 1.27.3.
    - [Release notes](https://github.com/docker/compose/releases)
    - [Changelog](https://github.com/docker/compose/blob/1.27.3/CHANGELOG.md)
    - [Commits](https://github.com/docker/compose/compare/1.27.2...1.27.3)
  * Bump docker-compose from 1.27.2 to 1.27.3 in /tests/requirements
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 6.0.2 to 6.1.0.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/6.0.2...6.1.0)
  * Bumps [docker-compose](https://github.com/docker/compose) from 1.27.3 to 1.27.4.
    - [Release notes](https://github.com/docker/compose/releases)
    - [Changelog](https://github.com/docker/compose/blob/1.27.4/CHANGELOG.md)
    - [Commits](https://github.com/docker/compose/compare/1.27.3...1.27.4)
  * Bumps [cryptography](https://github.com/pyca/cryptography) from 3.1 to 3.1.1.
    - [Release notes](https://github.com/pyca/cryptography/releases)
    - [Changelog](https://github.com/pyca/cryptography/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pyca/cryptography/compare/3.1...3.1.1)
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 6.0.2 to 6.1.0.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/6.0.2...6.1.0)
  * Bumps [stripe](https://github.com/stripe/stripe-python) from 2.51.0 to 2.53.0.
    - [Release notes](https://github.com/stripe/stripe-python/releases)
    - [Changelog](https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/stripe/stripe-python/compare/v2.51.0...v2.53.0)
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 6.1.0 to 6.1.1.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/6.1.0...6.1.1)
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 6.1.0 to 6.1.1.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/6.1.0...6.1.1)
  * Bumps [stripe](https://github.com/stripe/stripe-python) from 2.53.0 to 2.54.0.
    - [Release notes](https://github.com/stripe/stripe-python/releases)
    - [Changelog](https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/stripe/stripe-python/compare/v2.53.0...v2.54.0)
  * Bumps python from 3.8 to 3.9.0.
  * Bump python from 3.8 to 3.9.0 in /backend-tests/docker
  * Bumps [stripe](https://github.com/stripe/stripe-python) from 2.54.0 to 2.55.0.
    - [Release notes](https://github.com/stripe/stripe-python/releases)
    - [Changelog](https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/stripe/stripe-python/compare/v2.54.0...v2.55.0)
  * Bumps [pillow](https://github.com/python-pillow/Pillow) from 7.2.0 to 8.0.0.
    - [Release notes](https://github.com/python-pillow/Pillow/releases)
    - [Changelog](https://github.com/python-pillow/Pillow/blob/master/CHANGES.rst)
    - [Commits](https://github.com/python-pillow/Pillow/compare/7.2.0...8.0.0)
  * Bumps [pyotp](https://github.com/pyotp/pyotp) from 2.4.0 to 2.4.1.
    - [Release notes](https://github.com/pyotp/pyotp/releases)
    - [Changelog](https://github.com/pyauth/pyotp/blob/develop/Changes.rst)
    - [Commits](https://github.com/pyotp/pyotp/compare/v2.4.0...v2.4.1)
  * Bumps [cryptography](https://github.com/pyca/cryptography) from 3.1.1 to 3.2.
    - [Release notes](https://github.com/pyca/cryptography/releases)
    - [Changelog](https://github.com/pyca/cryptography/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pyca/cryptography/compare/3.1.1...3.2)
  * Bumps [pillow](https://github.com/python-pillow/Pillow) from 8.0.0 to 8.0.1.
    - [Release notes](https://github.com/python-pillow/Pillow/releases)
    - [Changelog](https://github.com/python-pillow/Pillow/blob/master/CHANGES.rst)
    - [Commits](https://github.com/python-pillow/Pillow/compare/8.0.0...8.0.1)
  * Bumps [cryptography](https://github.com/pyca/cryptography) from 3.2 to 3.2.1.
    - [Release notes](https://github.com/pyca/cryptography/releases)
    - [Changelog](https://github.com/pyca/cryptography/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pyca/cryptography/compare/3.2...3.2.1)
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 6.1.1 to 6.1.2.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/6.1.1...6.1.2)
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 6.1.1 to 6.1.2.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/6.1.1...6.1.2)
  * Bumps [requests](https://github.com/psf/requests) from 2.24.0 to 2.25.0.
    - [Release notes](https://github.com/psf/requests/releases)
    - [Changelog](https://github.com/psf/requests/blob/master/HISTORY.md)
    - [Commits](https://github.com/psf/requests/compare/v2.24.0...v2.25.0)
  * Bumps [pytest-html](https://github.com/pytest-dev/pytest-html) from 2.1.1 to 3.0.0.
    - [Release notes](https://github.com/pytest-dev/pytest-html/releases)
    - [Changelog](https://github.com/pytest-dev/pytest-html/blob/master/CHANGES.rst)
    - [Commits](https://github.com/pytest-dev/pytest-html/compare/v2.1.1...v3.0.0)
  * Bump pytest-html from 2.1.1 to 3.0.0 in /tests/requirements
  * Bump requests from 2.24.0 to 2.25.0 in /tests/requirements
  * Bumps [requests](https://github.com/psf/requests) from 2.24.0 to 2.25.0.
    - [Release notes](https://github.com/psf/requests/releases)
    - [Changelog](https://github.com/psf/requests/blob/master/HISTORY.md)
    - [Commits](https://github.com/psf/requests/compare/v2.24.0...v2.25.0)
  * Bumps [pytest-html](https://github.com/pytest-dev/pytest-html) from 2.1.1 to 3.0.0.
    - [Release notes](https://github.com/pytest-dev/pytest-html/releases)
    - [Changelog](https://github.com/pytest-dev/pytest-html/blob/master/CHANGES.rst)
    - [Commits](https://github.com/pytest-dev/pytest-html/compare/v2.1.1...v3.0.0)
  * Bumps [pymongo](https://github.com/mongodb/mongo-python-driver) from 3.11.0 to 3.11.1.
    - [Release notes](https://github.com/mongodb/mongo-python-driver/releases)
    - [Changelog](https://github.com/mongodb/mongo-python-driver/blob/master/doc/changelog.rst)
    - [Commits](https://github.com/mongodb/mongo-python-driver/compare/3.11.0...3.11.1)
  * Bumps [pymongo](https://github.com/mongodb/mongo-python-driver) from 3.11.0 to 3.11.1.
    - [Release notes](https://github.com/mongodb/mongo-python-driver/releases)
    - [Changelog](https://github.com/mongodb/mongo-python-driver/blob/master/doc/changelog.rst)
    - [Commits](https://github.com/mongodb/mongo-python-driver/compare/3.11.0...3.11.1)
  * Bumps [pytest-html](https://github.com/pytest-dev/pytest-html) from 3.0.0 to 3.1.0.
    - [Release notes](https://github.com/pytest-dev/pytest-html/releases)
    - [Changelog](https://github.com/pytest-dev/pytest-html/blob/master/CHANGES.rst)
    - [Commits](https://github.com/pytest-dev/pytest-html/compare/v3.0.0...v3.1.0)
  * Bumps [pymongo](https://github.com/mongodb/mongo-python-driver) from 3.11.1 to 3.11.2.
    - [Release notes](https://github.com/mongodb/mongo-python-driver/releases)
    - [Changelog](https://github.com/mongodb/mongo-python-driver/blob/3.11.2/doc/changelog.rst)
    - [Commits](https://github.com/mongodb/mongo-python-driver/compare/3.11.1...3.11.2)
  * Bumps [pytest-html](https://github.com/pytest-dev/pytest-html) from 3.0.0 to 3.1.0.
    - [Release notes](https://github.com/pytest-dev/pytest-html/releases)
    - [Changelog](https://github.com/pytest-dev/pytest-html/blob/master/CHANGES.rst)
    - [Commits](https://github.com/pytest-dev/pytest-html/compare/v3.0.0...v3.1.0)
  * Bumps [pymongo](https://github.com/mongodb/mongo-python-driver) from 3.11.1 to 3.11.2.
    - [Release notes](https://github.com/mongodb/mongo-python-driver/releases)
    - [Changelog](https://github.com/mongodb/mongo-python-driver/blob/3.11.2/doc/changelog.rst)
    - [Commits](https://github.com/mongodb/mongo-python-driver/compare/3.11.1...3.11.2)
  * Bumps [stripe](https://github.com/stripe/stripe-python) from 2.55.0 to 2.55.1.
    - [Release notes](https://github.com/stripe/stripe-python/releases)
    - [Changelog](https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/stripe/stripe-python/compare/v2.55.0...v2.55.1)
  * Bumps [cryptography](https://github.com/pyca/cryptography) from 3.2.1 to 3.3.1.
    - [Release notes](https://github.com/pyca/cryptography/releases)
    - [Changelog](https://github.com/pyca/cryptography/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pyca/cryptography/compare/3.2.1...3.3.1)
  * Bumps [pytest-html](https://github.com/pytest-dev/pytest-html) from 3.1.0 to 3.1.1.
    - [Release notes](https://github.com/pytest-dev/pytest-html/releases)
    - [Changelog](https://github.com/pytest-dev/pytest-html/blob/master/CHANGES.rst)
    - [Commits](https://github.com/pytest-dev/pytest-html/compare/v3.1.0...v3.1.1)
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 6.1.2 to 6.2.0.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/6.1.2...6.2.0)
  * Bumps python from 3.9.0 to 3.9.1.
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 6.1.2 to 6.2.0.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/6.1.2...6.2.0)
  * Bumps [pytest-html](https://github.com/pytest-dev/pytest-html) from 3.1.0 to 3.1.1.
    - [Release notes](https://github.com/pytest-dev/pytest-html/releases)
    - [Changelog](https://github.com/pytest-dev/pytest-html/blob/master/CHANGES.rst)
    - [Commits](https://github.com/pytest-dev/pytest-html/compare/v3.1.0...v3.1.1)
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 6.2.0 to 6.2.1.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/6.2.0...6.2.1)
  * Bumps [requests](https://github.com/psf/requests) from 2.25.0 to 2.25.1.
    - [Release notes](https://github.com/psf/requests/releases)
    - [Changelog](https://github.com/psf/requests/blob/master/HISTORY.md)
    - [Commits](https://github.com/psf/requests/compare/v2.25.0...v2.25.1)
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 6.2.0 to 6.2.1.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/6.2.0...6.2.1)
  * Bumps [requests](https://github.com/psf/requests) from 2.25.0 to 2.25.1.
    - [Release notes](https://github.com/psf/requests/releases)
    - [Changelog](https://github.com/psf/requests/blob/master/HISTORY.md)
    - [Commits](https://github.com/psf/requests/compare/v2.25.0...v2.25.1)
  * Bumps [pillow](https://github.com/python-pillow/Pillow) from 8.0.1 to 8.1.0.
    - [Release notes](https://github.com/python-pillow/Pillow/releases)
    - [Changelog](https://github.com/python-pillow/Pillow/blob/master/CHANGES.rst)
    - [Commits](https://github.com/python-pillow/Pillow/compare/8.0.1...8.1.0)
  * Bump pillow from 8.0.1 to 8.1.0 in /backend-tests

#### inventory (2.2.0)

New changes in inventory since 2.1.0:

* new device API end-point to replace inventory attributes
  ([MEN-4001](https://tracker.mender.io/browse/MEN-4001))
* new API end-point to return the list of filterable attributes
  ([MEN-3510](https://tracker.mender.io/browse/MEN-3510))
* Aggregated Dependabot Changelogs:
  * Bumps [github.com/urfave/cli](https://github.com/urfave/cli) from 1.22.4 to 1.22.5.
    - [Release notes](https://github.com/urfave/cli/releases)
    - [Changelog](https://github.com/urfave/cli/blob/master/docs/CHANGELOG.md)
    - [Commits](https://github.com/urfave/cli/compare/v1.22.4...v1.22.5)
  * Bump github.com/urfave/cli from 1.22.4 to 1.22.5
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.2 to 1.4.4.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.2...v1.4.4)
  * Bump go.mongodb.org/mongo-driver from 1.4.2 to 1.4.4

#### inventory-enterprise (2.2.0)

New changes in inventory-enterprise since 2.1.0:

* new device API end-point to replace inventory attributes
  ([MEN-4001](https://tracker.mender.io/browse/MEN-4001))
* new API end-point to return the list of filterable attributes
  ([MEN-3510](https://tracker.mender.io/browse/MEN-3510))
* optional redis cache to get filterable attributes
  ([MEN-3510](https://tracker.mender.io/browse/MEN-3510))
* Aggregated Dependabot Changelogs:
  * Bumps [github.com/go-redis/redis/v8](https://github.com/go-redis/redis) from 8.3.2 to 8.3.3.
    - [Release notes](https://github.com/go-redis/redis/releases)
    - [Changelog](https://github.com/go-redis/redis/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/go-redis/redis/compare/v8.3.2...v8.3.3)
  * Bump github.com/go-redis/redis/v8 from 8.3.2 to 8.3.3
  * Bumps [github.com/urfave/cli](https://github.com/urfave/cli) from 1.22.4 to 1.22.5.
    - [Release notes](https://github.com/urfave/cli/releases)
    - [Changelog](https://github.com/urfave/cli/blob/master/docs/CHANGELOG.md)
    - [Commits](https://github.com/urfave/cli/compare/v1.22.4...v1.22.5)
  * Bumps [github.com/urfave/cli](https://github.com/urfave/cli) from 1.22.4 to 1.22.5.
    - [Release notes](https://github.com/urfave/cli/releases)
    - [Changelog](https://github.com/urfave/cli/blob/master/docs/CHANGELOG.md)
    - [Commits](https://github.com/urfave/cli/compare/v1.22.4...v1.22.5)
  * Bump github.com/urfave/cli from 1.22.4 to 1.22.5
  * Bump github.com/urfave/cli from 1.22.4 to 1.22.5
  * Bumps [github.com/go-redis/redis/v8](https://github.com/go-redis/redis) from 8.3.3 to 8.4.0.
    - [Release notes](https://github.com/go-redis/redis/releases)
    - [Changelog](https://github.com/go-redis/redis/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/go-redis/redis/compare/v8.3.3...v8.4.0)
  * Bump github.com/go-redis/redis/v8 from 8.3.3 to 8.4.0
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.2 to 1.4.4.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.2...v1.4.4)
  * Bumps [github.com/go-redis/redis/v8](https://github.com/go-redis/redis) from 8.4.0 to 8.4.2.
    - [Release notes](https://github.com/go-redis/redis/releases)
    - [Changelog](https://github.com/go-redis/redis/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/go-redis/redis/compare/v8.4.0...v8.4.2)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.2 to 1.4.4.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.2...v1.4.4)
  * Bump github.com/go-redis/redis/v8 from 8.4.0 to 8.4.2
  * Bump go.mongodb.org/mongo-driver from 1.4.2 to 1.4.4
  * Bump go.mongodb.org/mongo-driver from 1.4.2 to 1.4.4
  * Bumps [github.com/go-redis/redis/v8](https://github.com/go-redis/redis) from 8.4.2 to 8.4.4.
    - [Release notes](https://github.com/go-redis/redis/releases)
    - [Changelog](https://github.com/go-redis/redis/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/go-redis/redis/compare/v8.4.2...v8.4.4)
  * Bump github.com/go-redis/redis/v8 from 8.4.2 to 8.4.4
  * Bumps [github.com/go-redis/redis/v8](https://github.com/go-redis/redis) from 8.4.4 to 8.4.8.
    - [Release notes](https://github.com/go-redis/redis/releases)
    - [Changelog](https://github.com/go-redis/redis/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/go-redis/redis/compare/v8.4.4...v8.4.8)
  * Bump github.com/go-redis/redis/v8 from 8.4.4 to 8.4.8

#### mender (2.5.0)

New changes in mender since 2.4.0:

* Fix rootfs-image-v2 commit in standalone mode when upgrade fails
* Add --reboot-exit-code parameter to "install" command.
* Fixed wrong error produced by rootfs-image commit
* Gracefully shutdown on SIGTERM
* implement "show-provides" command on client
  ([MEN-3074](https://tracker.mender.io/browse/MEN-3074))
* add inventory script to list the artifact provides data
  ([MEN-3073](https://tracker.mender.io/browse/MEN-3073))
* add support for software version flags in artifact generators
  ([MEN-3481](https://tracker.mender.io/browse/MEN-3481))
* Support for `clears_artifact_provides` field in Artifacts.
  ([MEN-3075](https://tracker.mender.io/browse/MEN-3075))
* switch to the new PUT endpoint to update inventory attributes
  ([MEN-4001](https://tracker.mender.io/browse/MEN-4001))
* Add Glib's GIO dependency for D-Bus interface. It can be
  opt-out using `nodbus` at compile time.
  ([MEN-4032](https://tracker.mender.io/browse/MEN-4032))
* Add support for probing the U-Boot environment separator
  ([MEN-3970](https://tracker.mender.io/browse/MEN-3970))
* Allow to load private key from the Security configuration section
  ([MEN-3924](https://tracker.mender.io/browse/MEN-3924))
* artifact-gen: Improve error message when mender-artifact is not found.
  ([MEN-4044](https://tracker.mender.io/browse/MEN-4044))
* Fix: Do not switch boot partitions on installation errors on the
  active partition.
  ([MEN-3980](https://tracker.mender.io/browse/MEN-3980))
* Correctly log the error message from the server on failed update
  download attempts.
* mender-inventory-geo: Set connection timeout to 10s.
* Decrease the verbosity of 'Authorization requests failed' errors in
  the log output.
* service API to register object interfaces over System DBus
  ([MEN-4009](https://tracker.mender.io/browse/MEN-4009))
* Add DBus support to AuthManager implementing WithDBus
* implement DBus signal ValidJwtTokenAvailable
  ([MEN-4017](https://tracker.mender.io/browse/MEN-4017))
* Add an inventory script for reporting the update-modules currently
  installed on a device.
* Add busconfig file for DBus API to install steps.
  ([MEN-4030](https://tracker.mender.io/browse/MEN-4030))
* Replace the current progressbar with a minimalistic and less verbose implementation.
* The 'inventory-geo-script' now has a separate install target:
  'install-inventory-network-scripts'. Note however that it is still installed by
  the default 'install-inventory-scripts' target.
* When available, enable D-Bus interface by default
* Exit with code 0 on a received SIGTERM signal.
  ([MEN-4170](https://tracker.mender.io/browse/MEN-4170))
* Add passphrase-file global option.
* Fix error parsing response for getting tenant token on setup
  ([MEN-4245](https://tracker.mender.io/browse/MEN-4245))
* Extend the D-Bus API to return the server URL
  ([MEN-4360](https://tracker.mender.io/browse/MEN-4360))
* Aggregated Dependabot Changelogs:
  * Bumps [github.com/mendersoftware/openssl](https://github.com/mendersoftware/openssl) from 1.0.9 to 1.0.10.
    - [Release notes](https://github.com/mendersoftware/openssl/releases)
    - [Commits](https://github.com/mendersoftware/openssl/compare/v1.0.9...v1.0.10)
  * Bump github.com/mendersoftware/openssl from 1.0.9 to 1.0.10
  * Bumps [github.com/mendersoftware/openssl](https://github.com/mendersoftware/openssl) from 1.0.10 to 1.1.0.
    - [Release notes](https://github.com/mendersoftware/openssl/releases)
    - [Commits](https://github.com/mendersoftware/openssl/compare/v1.0.10...v1.1.0)
  * Bump github.com/mendersoftware/openssl from 1.0.10 to 1.1.0

#### mender-api-gateway-docker (2.4.0)

New changes in mender-api-gateway-docker since 2.3.0:

* expose the management end-point to verify the user's plan
  ([MEN-3953](https://tracker.mender.io/browse/MEN-3953))
* restore ALLOWED_ORIGIN_HOSTS regex match when checking Origin
  ([MEN-4118](https://tracker.mender.io/browse/MEN-4118))

#### mender-artifact (3.5.0)

New changes in mender-artifact since 3.4.0:

* Fix segfault on mender-artifact dump for v2 Artifacts
  ([MEN-3967](https://tracker.mender.io/browse/MEN-3967))
* Change rootfs_image_checksum over to use namespaced provides
  ([MEN-3482](https://tracker.mender.io/browse/MEN-3482))
* Implement `clears_artifact_provides` field in Artifact
  format. This field can be used to control how Artifacts modify the
  record of existing software on the device. For example, a rootfs-image
  update can erase the record of other software on the device, whereas a
  single-file update can preserve the records. See the Mender
  documentation for more information on how to use this, or refer to
  `Documentation/artifact-format-v3.md` in the mender-artifact
  repository for the reference.
  ([MEN-3479](https://tracker.mender.io/browse/MEN-3479))
* Add `--print0-cmdline` argument to `dump` command.
  Works exactly like `--print-cmdline` but prints null bytes between
  arguments instead of spaces. This mirrors the `-print0` argument of
  find and complements the `-0` argument of xargs.
  ([MEN-3483](https://tracker.mender.io/browse/MEN-3483))
* use sudo for snapshots if required.
  ([MEN-3987](https://tracker.mender.io/browse/MEN-3987))
* Add progress indication to the mender-artifact read and write
  commands. So now progress is reported on the terminal TTY when reading and
  writing Artifacts.
* run fsck on fs image created via SSH snapshot
  ([MEN-4362](https://tracker.mender.io/browse/MEN-4362))
* Aggregated Dependabot Changelogs:
  * Bumps [github.com/pkg/errors](https://github.com/pkg/errors) from 0.8.1 to 0.9.1.
    - [Release notes](https://github.com/pkg/errors/releases)
    - [Commits](https://github.com/pkg/errors/compare/v0.8.1...v0.9.1)
  * Bumps alpine from 3.9 to 3.12.0.
  * Bump alpine from 3.9 to 3.12.0
  * Bump github.com/pkg/errors from 0.8.1 to 0.9.1
  * Bumps [github.com/klauspost/pgzip](https://github.com/klauspost/pgzip) from 1.2.3 to 1.2.4.
    - [Release notes](https://github.com/klauspost/pgzip/releases)
    - [Commits](https://github.com/klauspost/pgzip/compare/v1.2.3...v1.2.4)
  * Bump github.com/klauspost/pgzip from 1.2.3 to 1.2.4
  * Bumps [github.com/klauspost/pgzip](https://github.com/klauspost/pgzip) from 1.2.4 to 1.2.5.
    - [Release notes](https://github.com/klauspost/pgzip/releases)
    - [Commits](https://github.com/klauspost/pgzip/compare/v1.2.4...v1.2.5)
  * Bump github.com/klauspost/pgzip from 1.2.4 to 1.2.5
  * Bumps alpine from 3.12.0 to 3.12.1.
  * Bump alpine from 3.12.0 to 3.12.1
  * Bumps alpine from 3.12.1 to 3.12.2.
  * Bump alpine from 3.12.1 to 3.12.2
  * Bumps alpine from 3.12.2 to 3.12.3.
  * Bump alpine from 3.12.2 to 3.12.3
  * Bumps [github.com/urfave/cli](https://github.com/urfave/cli) from 1.22.4 to 1.22.5.
    - [Release notes](https://github.com/urfave/cli/releases)
    - [Changelog](https://github.com/urfave/cli/blob/master/docs/CHANGELOG.md)
    - [Commits](https://github.com/urfave/cli/compare/v1.22.4...v1.22.5)

#### mender-cli (1.6.0)

New changes in mender-cli since 1.5.0:

* Fix login with password, and improve the configuration file handling
* Add 'artifact list' command to list Artifacts on the Mender server
* Prompt for the users username if not provided on the CLI
* Add '--version' option to display the current mender-cli version
* New CLI command "terminal" to access a device's remote terminal
* mender-cli requires now golang 1.15 or newer
* Aggregated Dependabot Changelogs:
  * Bumps golang from 1.14-alpine3.12 to 1.15.1-alpine3.12.
  * Bump golang from 1.14-alpine3.12 to 1.15.1-alpine3.12
  * Bumps golang from 1.15.1-alpine3.12 to 1.15.2-alpine3.12.
  * Bump golang from 1.15.1-alpine3.12 to 1.15.2-alpine3.12
  * Bumps [github.com/cheggaaa/pb/v3](https://github.com/cheggaaa/pb) from 3.0.4 to 3.0.5.
    - [Release notes](https://github.com/cheggaaa/pb/releases)
    - [Commits](https://github.com/cheggaaa/pb/compare/v3.0.4...v3.0.5)
  * Bump github.com/cheggaaa/pb/v3 from 3.0.4 to 3.0.5
  * Bumps golang from 1.15.2-alpine3.12 to 1.15.3-alpine3.12.
  * Bumps [github.com/spf13/cobra](https://github.com/spf13/cobra) from 1.0.0 to 1.1.1.
    - [Release notes](https://github.com/spf13/cobra/releases)
    - [Changelog](https://github.com/spf13/cobra/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/spf13/cobra/compare/v1.0.0...v1.1.1)
  * Bump golang from 1.15.2-alpine3.12 to 1.15.3-alpine3.12
  * Bump github.com/spf13/cobra from 1.0.0 to 1.1.1
  * Bumps golang from 1.15.3-alpine3.12 to 1.15.4-alpine3.12.
  * Bump golang from 1.15.3-alpine3.12 to 1.15.4-alpine3.12
  * Bumps golang from 1.15.4-alpine3.12 to 1.15.5-alpine3.12.
  * Bump golang from 1.15.4-alpine3.12 to 1.15.5-alpine3.12
  * Bumps golang from 1.15.5-alpine3.12 to 1.15.6-alpine3.12.
  * Bump golang from 1.15.5-alpine3.12 to 1.15.6-alpine3.12

#### mender-connect (1.0.0)

* First release of mender-connect

#### tenantadm (3.0.0)

New changes in tenantadm since 2.1.0:

* credit card update endpoints
* enhance /billing end-point to retrieve current subscription
  ([MEN-3821](https://tracker.mender.io/browse/MEN-3821))
* Aggregated Dependabot Changelogs:
  * Bumps [github.com/sirupsen/logrus](https://github.com/sirupsen/logrus) from 1.6.0 to 1.7.0.
    - [Release notes](https://github.com/sirupsen/logrus/releases)
    - [Changelog](https://github.com/sirupsen/logrus/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/sirupsen/logrus/compare/v1.6.0...v1.7.0)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.0 to 1.4.2.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.0...v1.4.2)
  * Bump github.com/sirupsen/logrus from 1.6.0 to 1.7.0
  * Bump go.mongodb.org/mongo-driver from 1.4.0 to 1.4.2
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.2 to 1.4.3.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.2...v1.4.3)
  * Bump go.mongodb.org/mongo-driver from 1.4.2 to 1.4.3
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.3 to 1.4.4.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.3...v1.4.4)
  * Bump go.mongodb.org/mongo-driver from 1.4.3 to 1.4.4

#### useradm (1.13.0)

New changes in useradm since 1.12.0:

* GET /users accepts query parameters for filtering users
* new API end-point logout
  ([MEN-3943](https://tracker.mender.io/browse/MEN-3943))
* remove JWT all user tokens but the current one on password change
  ([MEN-3950](https://tracker.mender.io/browse/MEN-3950))
* Allow JWT to be passed as a cookie
  ([MEN-4042](https://tracker.mender.io/browse/MEN-4042))
* Add last login timestamp to user object
* Aggregated Dependabot Changelogs:
  * Bumps [github.com/urfave/cli](https://github.com/urfave/cli) from 1.22.4 to 1.22.5.
    - [Release notes](https://github.com/urfave/cli/releases)
    - [Changelog](https://github.com/urfave/cli/blob/master/docs/CHANGELOG.md)
    - [Commits](https://github.com/urfave/cli/compare/v1.22.4...v1.22.5)
  * Bump github.com/urfave/cli from 1.22.4 to 1.22.5
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.2 to 1.4.3.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.2...v1.4.3)
  * Bump go.mongodb.org/mongo-driver from 1.4.2 to 1.4.3
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.3 to 1.4.4.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.3...v1.4.4)
  * Bump go.mongodb.org/mongo-driver from 1.4.3 to 1.4.4

#### useradm-enterprise (1.13.0)

New changes in useradm-enterprise since 1.12.0:

* GET /users accepts query parameters for filtering users
* new API end-point logout
  ([MEN-3943](https://tracker.mender.io/browse/MEN-3943))
* remove JWT all user tokens but the current one on password change
  ([MEN-3950](https://tracker.mender.io/browse/MEN-3950))
* Useradm reports audit logs on create/delete user and updating
  roles
* , new management end-point to verify user's plan
  ([MEN-3275](https://tracker.mender.io/browse/MEN-3275), [MEN-3953](https://tracker.mender.io/browse/MEN-3953))
* Allow JWT to be passed as a cookie
  ([MEN-4042](https://tracker.mender.io/browse/MEN-4042))
* Add last login timestamp to user object
* introduce "REMOTE_TERMINAL" permission
* Add the Remote Terminal RBAC role
* Aggregated Dependabot Changelogs:
  * Bumps [github.com/urfave/cli](https://github.com/urfave/cli) from 1.22.4 to 1.22.5.
    - [Release notes](https://github.com/urfave/cli/releases)
    - [Changelog](https://github.com/urfave/cli/blob/master/docs/CHANGELOG.md)
    - [Commits](https://github.com/urfave/cli/compare/v1.22.4...v1.22.5)
  * Bumps [github.com/urfave/cli](https://github.com/urfave/cli) from 1.22.4 to 1.22.5.
    - [Release notes](https://github.com/urfave/cli/releases)
    - [Changelog](https://github.com/urfave/cli/blob/master/docs/CHANGELOG.md)
    - [Commits](https://github.com/urfave/cli/compare/v1.22.4...v1.22.5)
  * Bump github.com/urfave/cli from 1.22.4 to 1.22.5
  * Bump github.com/urfave/cli from 1.22.4 to 1.22.5
  * Bumps [github.com/go-redis/redis/v8](https://github.com/go-redis/redis) from 8.3.2 to 8.4.0.
    - [Release notes](https://github.com/go-redis/redis/releases)
    - [Changelog](https://github.com/go-redis/redis/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/go-redis/redis/compare/v8.3.2...v8.4.0)
  * Bump github.com/go-redis/redis/v8 from 8.3.2 to 8.4.0
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.2 to 1.4.3.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.2...v1.4.3)
  * Bump go.mongodb.org/mongo-driver from 1.4.2 to 1.4.3
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.3 to 1.4.4.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.3...v1.4.4)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.3 to 1.4.4.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.3...v1.4.4)
  * Bumps [github.com/go-redis/redis/v8](https://github.com/go-redis/redis) from 8.4.0 to 8.4.2.
    - [Release notes](https://github.com/go-redis/redis/releases)
    - [Changelog](https://github.com/go-redis/redis/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/go-redis/redis/compare/v8.4.0...v8.4.2)
  * Bump github.com/go-redis/redis/v8 from 8.4.0 to 8.4.2
  * Bump go.mongodb.org/mongo-driver from 1.4.3 to 1.4.4
  * Bump go.mongodb.org/mongo-driver from 1.4.3 to 1.4.4
  * Bumps [github.com/go-redis/redis/v8](https://github.com/go-redis/redis) from 8.4.2 to 8.4.4.
    - [Release notes](https://github.com/go-redis/redis/releases)
    - [Changelog](https://github.com/go-redis/redis/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/go-redis/redis/compare/v8.4.2...v8.4.4)
  * Bump github.com/go-redis/redis/v8 from 8.4.2 to 8.4.4
  * Bumps [github.com/go-redis/redis/v8](https://github.com/go-redis/redis) from 8.4.4 to 8.4.8.
    - [Release notes](https://github.com/go-redis/redis/releases)
    - [Changelog](https://github.com/go-redis/redis/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/go-redis/redis/compare/v8.4.4...v8.4.8)
  * Bump github.com/go-redis/redis/v8 from 8.4.4 to 8.4.8

#### workflows (1.3.0)

New changes in workflows since 1.2.0:

* add support for JSON body in HTTP tasks
  ([MEN-4110](https://tracker.mender.io/browse/MEN-4110))
* New properties: `requires` for Tasks, `skippped` for TaskResult
* Add support for default values in expressions
* Update workflow definitions to allow services' addresses override
* Add retryDelaySeconds property to speficy retry delays in tasks
* Aggregated Dependabot Changelogs:
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.0 to 1.4.3.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.0...v1.4.3)
  * Bump golang from 1.14-alpine3.12 to 1.15.4-alpine3.12
  * Bump go.mongodb.org/mongo-driver from 1.4.0 to 1.4.3
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.3 to 1.4.4.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.3...v1.4.4)
  * Bump go.mongodb.org/mongo-driver from 1.4.3 to 1.4.4

#### workflows-enterprise (1.3.0)

New changes in workflows-enterprise since 1.2.0:

* Change welcome email to contain self-service password reset link.
* add support for JSON body in HTTP tasks
  ([MEN-4110](https://tracker.mender.io/browse/MEN-4110))
* New properties: `requires` for Tasks, `skippped` for TaskResult
* Add support for default values in expressions
* Update workflow definitions to allow services' addresses override
* Add retryDelaySeconds property to speficy retry delays in tasks
* Aggregated Dependabot Changelogs:
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.0 to 1.4.3.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.0...v1.4.3)
  * Bump golang from 1.14-alpine3.12 to 1.15.4-alpine3.12
  * Bump go.mongodb.org/mongo-driver from 1.4.0 to 1.4.3
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.3 to 1.4.4.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.3...v1.4.4)
  * Bumps [go.mongodb.org/mongo-driver](https://github.com/mongodb/mongo-go-driver) from 1.4.3 to 1.4.4.
    - [Release notes](https://github.com/mongodb/mongo-go-driver/releases)
    - [Commits](https://github.com/mongodb/mongo-go-driver/compare/v1.4.3...v1.4.4)
  * Bump go.mongodb.org/mongo-driver from 1.4.3 to 1.4.4
  * Bump go.mongodb.org/mongo-driver from 1.4.3 to 1.4.4


## mender-binary-delta 1.2.0

_Released 01.11.2021_

### Changelogs

#### mender-binary-delta (1.2.0)

New changes in mender-binary-delta since 1.1.0:

* Improve error message when mender-artifact is not found.
  ([MEN-4044](https://tracker.mender.io/browse/MEN-4044))
* Mender-binary-delta and its Artifact generator now supports
  the new "Provides" fields for individial application software names.
  ([MEN-3483](https://tracker.mender.io/browse/MEN-3483), [MEN-3484](https://tracker.mender.io/browse/MEN-3484))
* The format of the Artifact checksum field has been changed
  in mender-artifact 3.5.0, from `rootfs_image_checksum` to
  `rootfs-image.checksum`, to conform to the namespaced "Provides"
  fields. Mender-binary-delta now supports this new field. This should
  not have any practical effect, but will cause meta data of delta
  Artifacts to look different.
  ([MEN-3483](https://tracker.mender.io/browse/MEN-3483), [MEN-3484](https://tracker.mender.io/browse/MEN-3484))
* Probe U-Boot env before use to support libubootenv fw tools
  ([MEN-4246](https://tracker.mender.io/browse/MEN-4246))


## mender-binary-delta 1.1.1

_Released 01.11.2021_

### Changelogs

#### mender-binary-delta (1.1.1)

New changes in mender-binary-delta since 1.1.0:

* Probe U-Boot env before use to support libubootenv fw tools
  ([MEN-4246](https://tracker.mender.io/browse/MEN-4246))


## meta-mender zeus-v2020.12

_Released 12.16.2020_

### Statistics

A total of 676 lines added, 2800 removed (delta -2124)

| Developers with the most changesets | |
|---|---|
| Lluis Campos | 12 (34.3%) |
| Kristian Amlie | 9 (25.7%) |
| Ole Petter Orhagen | 6 (17.1%) |
| Drew Moseley | 3 (8.6%) |
| Kasper Føns | 2 (5.7%) |
| Fabio Tranchitella | 2 (5.7%) |
| Peter Grzybowski | 1 (2.9%) |

| Developers with the most changed lines | |
|---|---|
| Ole Petter Orhagen | 1826 (56.0%) |
| Lluis Campos | 1329 (40.7%) |
| Kristian Amlie | 84 (2.6%) |
| Fabio Tranchitella | 12 (0.4%) |
| Drew Moseley | 6 (0.2%) |
| Kasper Føns | 5 (0.2%) |
| Peter Grzybowski | 1 (0.0%) |

| Developers with the most lines removed | |
|---|---|
| Ole Petter Orhagen | 1274 (45.5%) |
| Lluis Campos | 838 (29.9%) |
| Kristian Amlie | 22 (0.8%) |
| Drew Moseley | 2 (0.1%) |

| Developers with the most signoffs (total 5) | |
|---|---|
| Lluis Campos | 3 (60.0%) |
| Kristian Amlie | 2 (40.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 33 (94.3%) |
| Chora | 2 (5.7%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 3258 (99.8%) |
| Chora | 5 (0.2%) |

| Employers with the most signoffs (total 5) | |
|---|---|
| Northern.tech | 5 (100.0%) |

| Employers with the most hackers (total 7) | |
|---|---|
| Northern.tech | 6 (85.7%) |
| Chora | 1 (14.3%) |

### Changelogs

#### meta-mender (zeus-v2020.12)

New changes in meta-mender since zeus-v2020.10:

* Disable filesystem journal on read-only-rootfs, which
  sometimes causes unstable rootfs checksum together with fsck.
  ([MEN-3912](https://tracker.mender.io/browse/MEN-3912))
* mender: Fix broken patch for mender-systemd-machine-id.
* Remove recipe mender-client 2.3.0
* Add recipe mender-client 2.3.1
* Remove recipe mender-client 2.4.0
* Add recipe mender-client 2.4.1
* New Mender-client configuration option: 'inventory-network-scripts'.
  This option, if enabled, installs the inventory-network-scripts in the client.
  This is enabled as an option, because the inventory-geo script relies on a
  third-party network service to figure out the geographic location of the device,
  which may not be something that everyone wants installed on their devices. The
  feature is enabled in the standard 'PACKAGECONFIG' for the Mender-client, and is
  included unless overridded. To remove it, add
  'PACKAGECONFIG_remove_pn-mender-client = "inventory-network-scripts"' to your
  local.conf file.
* mender-client: Do not keep resizing if a little space is left unused
  ([MEN-4176](https://tracker.mender.io/browse/MEN-4176))
* mender-client: Ensure growfs works on GPT filesystems
  ([MEN-4176](https://tracker.mender.io/browse/MEN-4176))
* mender-client: Update LICENSE to include OpenSSL
* Add a recipe for building 'mender-connect', remote shell support.
  ([MEN-4083](https://tracker.mender.io/browse/MEN-4083))
* meta-mender-demo: install mender-connect
  ([MEN-4187](https://tracker.mender.io/browse/MEN-4187))
* mender-connect: generate and install mender-connect.conf with
  required fields. `ServerURL` can be configured setting yocto variable
  `MENDER_SERVER_URL`, same as used by mender-client recipe. If a
  `mender-connect.conf` file is found in the `SRC_URI` the contents will be
  merged. ([MEN-4242](https://tracker.mender.io/browse/MEN-4242))
* mender-connect: Add `User` to generated mender-connect.conf. The
  value of it is configured using `MENDER_CONNECT_USER` variable, which
  defaults to `nobody` for meta-mender-core and `root` for
  meta-mender-demo.
  ([MEN-4242](https://tracker.mender.io/browse/MEN-4242))


## meta-mender warrior-v2020.12

_Released 12.16.2020_

### Statistics

A total of 750 lines added, 94 removed (delta 656)

| Developers with the most changesets | |
|---|---|
| Lluis Campos | 8 (33.3%) |
| Kristian Amlie | 7 (29.2%) |
| Ole Petter Orhagen | 5 (20.8%) |
| Kasper Føns | 2 (8.3%) |
| Drew Moseley | 1 (4.2%) |
| Peter Grzybowski | 1 (4.2%) |

| Developers with the most changed lines | |
|---|---|
| Lluis Campos | 534 (68.0%) |
| Ole Petter Orhagen | 166 (21.1%) |
| Kristian Amlie | 76 (9.7%) |
| Kasper Føns | 5 (0.6%) |
| Drew Moseley | 3 (0.4%) |
| Peter Grzybowski | 1 (0.1%) |

| Developers with the most lines removed | |
|---|---|
| Kristian Amlie | 13 (13.8%) |
| Drew Moseley | 2 (2.1%) |

| Developers with the most signoffs (total 2) | |
|---|---|
| Lluis Campos | 2 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 22 (91.7%) |
| Chora | 2 (8.3%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 780 (99.4%) |
| Chora | 5 (0.6%) |

| Employers with the most signoffs (total 2) | |
|---|---|
| Northern.tech | 2 (100.0%) |

| Employers with the most hackers (total 6) | |
|---|---|
| Northern.tech | 5 (83.3%) |
| Chora | 1 (16.7%) |

### Changelogs

#### meta-mender (warrior-v2020.12)

New changes in meta-mender since warrior-v2020.10:

* Disable `64bit` ext4 filesystem feature.
  ([MEN-3513](https://tracker.mender.io/browse/MEN-3513))
* Disable filesystem journal on read-only-rootfs, which
  sometimes causes unstable rootfs checksum together with fsck.
  ([MEN-3912](https://tracker.mender.io/browse/MEN-3912))
* mender: Fix broken patch for mender-systemd-machine-id.
* Remove recipe mender-client 2.3.0
* Add recipe mender-client 2.3.1
* Remove recipe mender-client 2.4.0
* Add recipe mender-client 2.4.1
* New Mender-client configuration option: 'inventory-network-scripts'.
  This option, if enabled, installs the inventory-network-scripts in the client.
  This is enabled as an option, because the inventory-geo script relies on a
  third-party network service to figure out the geographic location of the device,
  which may not be something that everyone wants installed on their devices. The
  feature is enabled in the standard 'PACKAGECONFIG' for the Mender-client, and is
  included unless overridded. To remove it, add
  'PACKAGECONFIG_remove_pn-mender-client = "inventory-network-scripts"' to your
  local.conf file.
* mender-client: Do not keep resizing if a little space is left unused
  ([MEN-4176](https://tracker.mender.io/browse/MEN-4176))
* mender-client: Ensure growfs works on GPT filesystems
  ([MEN-4176](https://tracker.mender.io/browse/MEN-4176))
* mender-client: Update LICENSE to include OpenSSL
* Add a recipe for building 'mender-connect', remote shell support.
  ([MEN-4083](https://tracker.mender.io/browse/MEN-4083))
* meta-mender-demo: install mender-connect
  ([MEN-4187](https://tracker.mender.io/browse/MEN-4187))
* mender-connect: generate and install mender-connect.conf with
  required fields. `ServerURL` can be configured setting yocto variable
  `MENDER_SERVER_URL`, same as used by mender-client recipe. If a
  `mender-connect.conf` file is found in the `SRC_URI` the contents will be
  merged. ([MEN-4242](https://tracker.mender.io/browse/MEN-4242))
* mender-connect: Add `User` to generated mender-connect.conf. The
  value of it is configured using `MENDER_CONNECT_USER` variable, which
  defaults to `nobody` for meta-mender-core and `root` for
  meta-mender-demo.
  ([MEN-4242](https://tracker.mender.io/browse/MEN-4242))


## meta-mender dunfell-v2020.12

_Released 12.08.2020_

### Statistics

A total of 547 lines added, 1726 removed (delta -1179)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 7 (38.9%) |
| Ole Petter Orhagen | 5 (27.8%) |
| Lluis Campos | 3 (16.7%) |
| Kasper Føns | 2 (11.1%) |
| Drew Moseley | 1 (5.6%) |

| Developers with the most changed lines | |
|---|---|
| Ole Petter Orhagen | 1823 (87.5%) |
| Kristian Amlie | 143 (6.9%) |
| Lluis Campos | 111 (5.3%) |
| Kasper Føns | 5 (0.2%) |
| Drew Moseley | 2 (0.1%) |

| Developers with the most lines removed | |
|---|---|
| Ole Petter Orhagen | 1275 (73.9%) |

| Developers with the most signoffs (total 2) | |
|---|---|
| Kristian Amlie | 2 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 16 (88.9%) |
| Chora | 2 (11.1%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 2079 (99.8%) |
| Chora | 5 (0.2%) |

| Employers with the most signoffs (total 2) | |
|---|---|
| Northern.tech | 2 (100.0%) |

| Employers with the most hackers (total 5) | |
|---|---|
| Northern.tech | 4 (80.0%) |
| Chora | 1 (20.0%) |

### Changelogs

#### meta-mender (dunfell-v2020.12)

New changes in meta-mender since dunfell-v2020.11:

* mender: Reestablish labels on the root filesystems.
* New Mender-client configuration option: 'inventory-network-scripts'.
  This option, if enabled, installs the inventory-network-scripts in the client.
  This is enabled as an option, because the inventory-geo script relies on a
  third-party network service to figure out the geographic location of the device,
  which may not be something that everyone wants installed on their devices. The
  feature is enabled in the standard 'PACKAGECONFIG' for the Mender-client, and is
  included unless overridded. To remove it, add
  'PACKAGECONFIG_remove_pn-mender-client = "inventory-network-scripts"' to your
  local.conf file.
* mender-client: Do not keep resizing if a little space is left unused
  ([MEN-4176](https://tracker.mender.io/browse/MEN-4176))
* mender-client: Ensure growfs works on GPT filesystems
  ([MEN-4176](https://tracker.mender.io/browse/MEN-4176))
* mender-client: Update LICENSE to include OpenSSL
* mender-client: Include OpenSSL license from 2.4.x onwards.
* Add a recipe for building 'mender-connect', remote shell support.
  ([MEN-4083](https://tracker.mender.io/browse/MEN-4083))
* Fix a parsing issue where `inherit` could not be used with
  variables that had been defined with overrides that depended on
  `MENDER_FEATURES_ENABLE`. One example would be:
  ```
  MYVAR_mender-grub = "grub-efi"
  inherit ${MYVAR}
  ```


## meta-mender dunfell-v2020.11

_Released 11.16.2020_

### Statistics

A total of 6 lines added, 1067 removed (delta -1061)

| Developers with the most changesets | |
|---|---|
| Ole Petter Orhagen | 3 (50.0%) |
| Lluis Campos | 2 (33.3%) |
| Drew Moseley | 1 (16.7%) |

| Developers with the most changed lines | |
|---|---|
| Lluis Campos | 922 (86.4%) |
| Ole Petter Orhagen | 142 (13.3%) |
| Drew Moseley | 3 (0.3%) |

| Developers with the most lines removed | |
|---|---|
| Lluis Campos | 921 (86.3%) |
| Ole Petter Orhagen | 138 (12.9%) |
| Drew Moseley | 2 (0.2%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 6 (100.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 1067 (100.0%) |

| Employers with the most hackers (total 3) | |
|---|---|
| Northern.tech | 3 (100.0%) |

### Changelogs

#### meta-mender (dunfell-v2020.11)

New changes in meta-mender since dunfell-v2020.10:

* mender: Fix broken patch for mender-systemd-machine-id.
* Remove recipe mender-client 2.3.0
* Add recipe mender-client 2.3.1
* Remove recipe mender-client 2.4.0
* Add recipe mender-client 2.4.1
* Aggregated Dependabot Changelogs:
  * Bumps [tests/acceptance/image-tests](https://github.com/mendersoftware/mender-image-tests) from `457ea99` to `713c563`.
    - [Release notes](https://github.com/mendersoftware/mender-image-tests/releases)
    - [Commits](https://github.com/mendersoftware/mender-image-tests/compare/457ea99937642ec29da53a9a2d30a51067cf8dc0...713c56364b79a18ad86e6731b1a602f0f3d9d233)
  * Bump tests/acceptance/image-tests from `457ea99` to `713c563`


## mender-convert 2.2.1

_Released 11.05.2020_

### Statistics

A total of 144 lines added, 96 removed (delta 48)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 6 (60.0%) |
| Ole Petter Orhagen | 2 (20.0%) |
| Lluis Campos | 2 (20.0%) |

| Developers with the most changed lines | |
|---|---|
| Kristian Amlie | 119 (81.0%) |
| Lluis Campos | 23 (15.6%) |
| Ole Petter Orhagen | 5 (3.4%) |

| Developers with the most lines removed | |
|---|---|
| Ole Petter Orhagen | 3 (3.1%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 10 (100.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 147 (100.0%) |

| Employers with the most hackers (total 3) | |
|---|---|
| Northern.tech | 3 (100.0%) |

### Changelogs

#### mender-convert (2.2.1)

New changes in mender-convert since 2.2.0:

* grub-efi: Fix inability to upgrade to a different kernel.
* Fix massive root filesystem corruption under some build conditions.
* beaglebone: Implement workaround for broken U-Boot and kernel.
  ([MEN-3952](https://tracker.mender.io/browse/MEN-3952))
* beaglebone: Remove U-Boot integration, which has not worked
  for a long time. U-Boot will still be used for booting, but GRUB will
  be used for integration with Mender, by chainloading via UEFI.
  ([MEN-3952](https://tracker.mender.io/browse/MEN-3952))
* Install the latest Mender-client release (2.4.1) by default.


## Mender client 2.4.1

_Released 11.03.2020_

### Statistics

A total of 397 lines added, 161 removed (delta 236)

| Developers with the most changesets | |
|---|---|
| Ole Petter Orhagen | 4 (36.4%) |
| Peter Grzybowski | 3 (27.3%) |
| Lluis Campos | 3 (27.3%) |
| Fabio Tranchitella | 1 (9.1%) |

| Developers with the most changed lines | |
|---|---|
| Ole Petter Orhagen | 314 (77.0%) |
| Peter Grzybowski | 51 (12.5%) |
| Lluis Campos | 42 (10.3%) |
| Fabio Tranchitella | 1 (0.2%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 11 (100.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 408 (100.0%) |

| Employers with the most hackers (total 4) | |
|---|---|
| Northern.tech | 4 (100.0%) |

### Changelogs

#### mender (2.4.1)

New changes in mender since 2.4.0:

* Add support for probing the U-Boot environment separator
  ([MEN-3970](https://tracker.mender.io/browse/MEN-3970))
* Fix: Do not switch boot partitions on installation errors on the
  active partition.
  ([MEN-3980](https://tracker.mender.io/browse/MEN-3980))
* Allow to load private key from the Security configuration section
  ([MEN-3924](https://tracker.mender.io/browse/MEN-3924))


## Mender client 2.3.1

_Released 11.03.2020_

### Statistics

A total of 211 lines added, 26 removed (delta 185)

| Developers with the most changesets | |
|---|---|
| Ole Petter Orhagen | 5 (55.6%) |
| Lluis Campos | 3 (33.3%) |
| Fabio Tranchitella | 1 (11.1%) |

| Developers with the most changed lines | |
|---|---|
| Ole Petter Orhagen | 179 (80.6%) |
| Lluis Campos | 42 (18.9%) |
| Fabio Tranchitella | 1 (0.5%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 9 (100.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 222 (100.0%) |

| Employers with the most hackers (total 3) | |
|---|---|
| Northern.tech | 3 (100.0%) |

### Changelogs

#### mender (2.3.1)

New changes in mender since 2.3.0:

* Add support for probing the U-Boot environment separator
  ([MEN-3970](https://tracker.mender.io/browse/MEN-3970))
* Fix: Do not switch boot partitions on installation errors on the
  active partition.
  ([MEN-3980](https://tracker.mender.io/browse/MEN-3980))



## meta-mender dunfell-v2020.10

_Released 10.13.2020_

### Statistics

A total of 334 lines added, 431 removed (delta -97)

| Developers with the most changesets | |
|---|---|
| Drew Moseley | 17 (53.1%) |
| Kristian Amlie | 8 (25.0%) |
| Lluis Campos | 2 (6.2%) |
| Ole Petter Orhagen | 2 (6.2%) |
| Fabio Tranchitella | 2 (6.2%) |
| Peter Grzybowski | 1 (3.1%) |

| Developers with the most changed lines | |
|---|---|
| Drew Moseley | 315 (65.9%) |
| Kristian Amlie | 129 (27.0%) |
| Ole Petter Orhagen | 15 (3.1%) |
| Fabio Tranchitella | 12 (2.5%) |
| Lluis Campos | 6 (1.3%) |
| Peter Grzybowski | 1 (0.2%) |

| Developers with the most lines removed | |
|---|---|
| Drew Moseley | 114 (26.5%) |

| Developers with the most signoffs (total 5) | |
|---|---|
| Lluis Campos | 5 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 32 (100.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 478 (100.0%) |

| Employers with the most signoffs (total 5) | |
|---|---|
| Northern.tech | 5 (100.0%) |

| Employers with the most hackers (total 6) | |
|---|---|
| Northern.tech | 6 (100.0%) |

### Changelogs

#### meta-mender (dunfell-v2020.10)

New changes in meta-mender since dunfell-v2020.09:

* Disable filesystem journal on read-only-rootfs, which
  sometimes causes unstable rootfs checksum together with fsck.
  ([MEN-3912](https://tracker.mender.io/browse/MEN-3912))
* mender: Make Mender settings conditional.
* meta-mender-demo: Make Mender settings conditional.
* meta-mender-raspberrypi-demo: Make Mender settings conditional.
* meta-mender-qemu: Make Mender settings conditional.
* tests/mender: Make Mender settings conditional.
* mender-grub: Rework to use conditional includes.
* mender-uboot: Conditionally include settings.
* mender: Only include full mender-setup if features are enabled.
* mender-binary-delta: Only add SRC_URI entries for existing binaries.
* grub-mender-grubenv: Cleanup PROVIDES and RPROVIDES.
* mender: Switch from include to require.
* Fix PACKAGECONFIG not propagating RDEPENDS properly.


## meta-mender zeus-v2020.10

_Released 10.05.2020_

### Statistics

A total of 86545 lines added, 31 removed (delta 86514)

| Developers with the most changesets | |
|---|---|
| Drew Moseley | 5 (27.8%) |
| Lluis Campos | 4 (22.2%) |
| Peter Grzybowski | 2 (11.1%) |
| Daniel Selvan D | 1 (5.6%) |
| Kristian Amlie | 1 (5.6%) |
| Mirza Krak | 1 (5.6%) |
| Kasper Føns | 1 (5.6%) |
| Kurt Kiefer | 1 (5.6%) |
| Marek Belisko | 1 (5.6%) |
| Ossian Riday | 1 (5.6%) |

| Developers with the most changed lines | |
|---|---|
| Lluis Campos | 86467 (99.9%) |
| Marek Belisko | 47 (0.1%) |
| Peter Grzybowski | 10 (0.0%) |
| Drew Moseley | 9 (0.0%) |
| Kurt Kiefer | 7 (0.0%) |
| Kristian Amlie | 4 (0.0%) |
| Ossian Riday | 3 (0.0%) |
| Kasper Føns | 2 (0.0%) |
| Daniel Selvan D | 1 (0.0%) |
| Mirza Krak | 1 (0.0%) |

| Developers with the most signoffs (total 1) | |
|---|---|
| Kristian Amlie | 1 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 13 (72.2%) |
| kekiefer@gmail.com | 1 (5.6%) |
| danilselvan@gmail.com | 1 (5.6%) |
| ossian.riday@gmail.com | 1 (5.6%) |
| Chora | 1 (5.6%) |
| open-nandra | 1 (5.6%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 86491 (99.9%) |
| open-nandra | 47 (0.1%) |
| kekiefer@gmail.com | 7 (0.0%) |
| ossian.riday@gmail.com | 3 (0.0%) |
| Chora | 2 (0.0%) |
| danilselvan@gmail.com | 1 (0.0%) |

| Employers with the most signoffs (total 1) | |
|---|---|
| Northern.tech | 1 (100.0%) |

| Employers with the most hackers (total 10) | |
|---|---|
| Northern.tech | 5 (50.0%) |
| open-nandra | 1 (10.0%) |
| kekiefer@gmail.com | 1 (10.0%) |
| ossian.riday@gmail.com | 1 (10.0%) |
| Chora | 1 (10.0%) |
| danilselvan@gmail.com | 1 (10.0%) |

### Changelogs

#### meta-mender (zeus-v2020.10)

New changes in meta-mender since zeus-v2020.07:

* []MBR systems don't have a backup header, so always return true
  ([MEN-3761](https://tracker.mender.io/browse/MEN-3761))
* u-boot: Fix raspberrypi-cm3 u-boot hang
* mender-client: fix install of systemd-machine-id.service
* initramfs-module-install-efi: Ensure variable changes are reflected on rebuild
* mender-commercial: Cleanup BBFILES.
* Warn when detecting U-Boot version without script '=' support.
  ([MEN-3851](https://tracker.mender.io/browse/MEN-3851))
* Add mender-client 2.4.0 recipe.
* OpenSSL: qemu: set SECLEVEL=2 in /etc/ssl/openssl.cnf
  ([MEN-3730](https://tracker.mender.io/browse/MEN-3730))
* Fixed key extraction by skipping new lines in defconfig.
  The `add_kconfig_option_with_depends.py` file throws `Not sure how to
  handle Kconfig option that doesn't start with 'CONFIG_'` when the
  provided defconfig file contains blank lines. It has been fixed by
  checking for empty lines before processing for keys.
* Add recipe go 1.14 from dunfell
* Use golang 1.14 in meta-mender-core layer to support Ed25519
  public keys for signing and transport in the Mender client.


## meta-mender warrior-v2020.10

_Released 10.05.2020_

### Statistics

A total of 86487 lines added, 100 removed (delta 86387)

| Developers with the most changesets | |
|---|---|
| Drew Moseley | 7 (46.7%) |
| Lluis Campos | 3 (20.0%) |
| Peter Grzybowski | 1 (6.7%) |
| Mirza Krak | 1 (6.7%) |
| Kristian Amlie | 1 (6.7%) |
| Michael Davis | 1 (6.7%) |
| Kasper Føns | 1 (6.7%) |

| Developers with the most changed lines | |
|---|---|
| Lluis Campos | 86463 (99.9%) |
| Drew Moseley | 92 (0.1%) |
| Peter Grzybowski | 9 (0.0%) |
| Kristian Amlie | 4 (0.0%) |
| Kasper Føns | 2 (0.0%) |
| Mirza Krak | 1 (0.0%) |
| Michael Davis | 1 (0.0%) |

| Developers with the most lines removed | |
|---|---|
| Drew Moseley | 73 (73.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 13 (86.7%) |
| Election Systems & Software | 1 (6.7%) |
| Chora | 1 (6.7%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 86569 (100.0%) |
| Chora | 2 (0.0%) |
| Election Systems & Software | 1 (0.0%) |

| Employers with the most signoffs (total 0) | |
|---|---|

| Employers with the most hackers (total 7) | |
|---|---|
| Northern.tech | 5 (71.4%) |
| Chora | 1 (14.3%) |
| Election Systems & Software | 1 (14.3%) |

### Changelogs

#### meta-mender (warrior-v2020.10)

New changes in meta-mender since warrior-v2020.07:

* initramfs-module-install-efi: Ensure variable changes are reflected on rebuild
* mender-grub: Dynamically determine mender_grub_storage_device.
* mender-grub: Add regexp module.
* Deprecate MENDER_GRUB_STORAGE_DEVICE variable.
* mender: Add sanity check to ensure partuuid with X86.
* vexpress: Remove nonexistent kernel config options that issue warnings.
* mender-commercial: Cleanup BBFILES.
* mender: Add additonal x86 arch to partuuid sanity check
* Warn when detecting U-Boot version without script '=' support.
  ([MEN-3851](https://tracker.mender.io/browse/MEN-3851))
* Add mender-client 2.4.0 recipe.
* OpenSSL: qemu: set SECLEVEL=2 in /etc/ssl/openssl.cnf
  ([MEN-3730](https://tracker.mender.io/browse/MEN-3730))
* Add recipe go 1.14 from dunfell
* Use golang 1.14 in meta-mender-core layer to support Ed25519
  public keys for signing and transport in the Mender client.


## meta-mender thud-v2020.10

_Released 10.05.2020_

### Statistics

A total of 82 lines added, 38 removed (delta 44)

| Developers with the most changesets | |
|---|---|
| Drew Moseley | 7 (43.8%) |
| Lluis Campos | 3 (18.8%) |
| Gaurav Kalra | 2 (12.5%) |
| Matthew Beckler | 2 (12.5%) |
| Joerg Hofrichter | 1 (6.2%) |
| Kristian Amlie | 1 (6.2%) |

| Developers with the most changed lines | |
|---|---|
| Drew Moseley | 55 (63.2%) |
| Lluis Campos | 16 (18.4%) |
| Kristian Amlie | 10 (11.5%) |
| Gaurav Kalra | 2 (2.3%) |
| Matthew Beckler | 2 (2.3%) |
| Joerg Hofrichter | 2 (2.3%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 11 (68.8%) |
| Packet Power LLC | 2 (12.5%) |
| National Instruments | 1 (6.2%) |
| gvkalra@gmail.com | 1 (6.2%) |
| SM Instruments Inc. | 1 (6.2%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 81 (93.1%) |
| Packet Power LLC | 2 (2.3%) |
| National Instruments | 2 (2.3%) |
| gvkalra@gmail.com | 1 (1.1%) |
| SM Instruments Inc. | 1 (1.1%) |

| Employers with the most signoffs (total 1) | |
|---|---|
| Northern.tech | 1 (100.0%) |

| Employers with the most hackers (total 7) | |
|---|---|
| Northern.tech | 3 (42.9%) |
| Packet Power LLC | 1 (14.3%) |
| National Instruments | 1 (14.3%) |
| gvkalra@gmail.com | 1 (14.3%) |
| SM Instruments Inc. | 1 (14.3%) |

### Changelogs

#### meta-mender (thud-v2020.10)

New changes in meta-mender since thud-v2019.12:

* grub-mender-grubenv: Fix broken debug-log PACKAGECONFIG.
* grub-efi: Respect MENDER_BOOT_PART_MOUNT_LOCATION
* mender-grub: Set EFI_PROVIDER to grub-efi.
* remove stray '-' in IMAGE_NAME
* systemd-boot: Respect MENDER_BOOT_PART_MOUNT_LOCATION
* Add mender 2.2.0b1 recipe
* Add mender-artifact 3.3.0b1 recipe
* In demo mode, put demo certificate in same directory as Debian package.
  ([MEN-3048](https://tracker.mender.io/browse/MEN-3048))
* mender-helpers: Error out if copying different files to boot part.
* Improve warning when multiple DTB files are in KERNEL_DEVICETREE
* Add MENDER_DTB_NAME_FORCE to mender-vars.json to avoid unrecognized variable warning
* rpi: fix rootfs cmdline trailing space
* Add mender 2.2.1 recipe
* Add mender-artifact 3.3.1 recipe
* Remove mender 2.2.0b1 recipe
* Remove mender-artifact 3.3.0b1 recipe


## meta-mender sumo-v2020.10

_Released 10.05.2020_

### Statistics

A total of 52 lines added, 60 removed (delta -8)

| Developers with the most changesets | |
|---|---|
| Drew Moseley | 5 (45.5%) |
| Lluis Campos | 2 (18.2%) |
| Matthew Beckler | 2 (18.2%) |
| Gaurav Kalra | 1 (9.1%) |
| Kristian Amlie | 1 (9.1%) |

| Developers with the most changed lines | |
|---|---|
| Lluis Campos | 49 (55.1%) |
| Drew Moseley | 27 (30.3%) |
| Kristian Amlie | 10 (11.2%) |
| Matthew Beckler | 2 (2.2%) |
| Gaurav Kalra | 1 (1.1%) |

| Developers with the most lines removed | |
|---|---|
| Lluis Campos | 35 (58.3%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 8 (72.7%) |
| Packet Power LLC | 2 (18.2%) |
| SM Instruments Inc. | 1 (9.1%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 86 (96.6%) |
| Packet Power LLC | 2 (2.2%) |
| SM Instruments Inc. | 1 (1.1%) |

| Employers with the most hackers (total 5) | |
|---|---|
| Northern.tech | 3 (60.0%) |
| Packet Power LLC | 1 (20.0%) |
| SM Instruments Inc. | 1 (20.0%) |

### Changelogs

#### meta-mender (sumo-v2020.10)

New changes in meta-mender since sumo-v2019.12:

* grub-mender-grubenv: Fix broken debug-log PACKAGECONFIG.
* grub-efi: Respect MENDER_BOOT_PART_MOUNT_LOCATION
* mender-grub: Set EFI_PROVIDER to grub-efi.
* systemd-boot: Respect MENDER_BOOT_PART_MOUNT_LOCATION
* Add mender 2.2.0b1 recipe
* Add mender-artifact 3.3.0b1 recipe
* In demo mode, put demo certificate in same directory as Debian package.
  ([MEN-3048](https://tracker.mender.io/browse/MEN-3048))
* Improve warning when multiple DTB files are in KERNEL_DEVICETREE
* Add MENDER_DTB_NAME_FORCE to mender-vars.json to avoid unrecognized variable warning
* rpi: fix rootfs cmdline trailing space
* Add mender 2.2.1 recipe
* Add mender-artifact 3.3.1 recipe
* Remove mender 2.2.0b1 recipe
* Remove mender-artifact 3.3.0b1 recipe


## meta-mender rocko-v2020.10

_Released 10.05.2020_

### Statistics

A total of 201 lines added, 147 removed (delta 54)

| Developers with the most changesets | |
|---|---|
| Lluis Campos | 6 (46.2%) |
| Kristian Amlie | 6 (46.2%) |
| Ole Petter Orhagen | 1 (7.7%) |

| Developers with the most changed lines | |
|---|---|
| Kristian Amlie | 157 (55.5%) |
| Ole Petter Orhagen | 113 (39.9%) |
| Lluis Campos | 13 (4.6%) |

| Developers with the most lines removed | |
|---|---|
| Ole Petter Orhagen | 82 (55.8%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 13 (100.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 283 (100.0%) |

| Employers with the most hackers (total 3) | |
|---|---|
| Northern.tech | 3 (100.0%) |

### Changelogs

#### meta-mender (rocko-v2020.10)

New changes in meta-mender since rocko-v2019.08:

* Add meta-mender-commercial layer.
  This will host our mender-binary-delta Update Module.
* Update recipe for mender-binary-delta pre-release v0.1.1
* `FILESEXTRAPATHS_prepend_pn-mender-binary-delta` now needs
  to point to the folder containing `arm`, `aarch64` and `x86_64`, not the folder
  containing the binary.
* Update recipe for mender-binary-delta beta release v1.0.0b1
* Update recipe for mender-binary-delta final release v1.0.0
* Add mender 2.2.1 recipe
* Add mender-artifact 3.3.1 recipe
* Remove mender 2.1.0b1 recipe
* Remove mender-artifact 3.1.0b1 recipe
* Removes the tests covering Mender-Artifact version 1.
  ([MEN-2156](https://tracker.mender.io/browse/MEN-2156))


## meta-mender dunfell-v2020.09

_Released 09.17.2020_

### Statistics

A total of 70 lines added, 136 removed (delta -66)

| Developers with the most changesets | |
|---|---|
| Drew Moseley | 5 (26.3%) |
| Peter Grzybowski | 3 (15.8%) |
| Lluis Campos | 2 (10.5%) |
| Kurt Kiefer | 2 (10.5%) |
| Daniel Selvan D | 1 (5.3%) |
| Kristian Amlie | 1 (5.3%) |
| Ole Petter Orhagen | 1 (5.3%) |
| Marek Belisko | 1 (5.3%) |
| Mirza Krak | 1 (5.3%) |
| Kasper Føns | 1 (5.3%) |

| Developers with the most changed lines | |
|---|---|
| Marek Belisko | 64 (36.2%) |
| Drew Moseley | 45 (25.4%) |
| Peter Grzybowski | 35 (19.8%) |
| Lluis Campos | 12 (6.8%) |
| Kurt Kiefer | 9 (5.1%) |
| Kristian Amlie | 4 (2.3%) |
| Ossian Riday | 3 (1.7%) |
| Kasper Føns | 2 (1.1%) |
| Daniel Selvan D | 1 (0.6%) |
| Ole Petter Orhagen | 1 (0.6%) |

| Developers with the most lines removed | |
|---|---|
| Marek Belisko | 64 (47.1%) |
| Drew Moseley | 34 (25.0%) |
| Lluis Campos | 6 (4.4%) |

| Developers with the most signoffs (total 1) | |
|---|---|
| Kristian Amlie | 1 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 13 (68.4%) |
| kekiefer@gmail.com | 2 (10.5%) |
| danilselvan@gmail.com | 1 (5.3%) |
| ossian.riday@gmail.com | 1 (5.3%) |
| Chora | 1 (5.3%) |
| open-nandra | 1 (5.3%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 98 (55.4%) |
| open-nandra | 64 (36.2%) |
| kekiefer@gmail.com | 9 (5.1%) |
| ossian.riday@gmail.com | 3 (1.7%) |
| Chora | 2 (1.1%) |
| danilselvan@gmail.com | 1 (0.6%) |

| Employers with the most signoffs (total 1) | |
|---|---|
| Northern.tech | 1 (100.0%) |

| Employers with the most hackers (total 11) | |
|---|---|
| Northern.tech | 6 (54.5%) |
| open-nandra | 1 (9.1%) |
| kekiefer@gmail.com | 1 (9.1%) |
| ossian.riday@gmail.com | 1 (9.1%) |
| Chora | 1 (9.1%) |
| danilselvan@gmail.com | 1 (9.1%) |

### Changelogs

#### meta-mender (dunfell-v2020.09)

New changes in meta-mender since dunfell-v2020.07:

* []MBR systems don't have a backup header, so always return true
  ([MEN-3761](https://tracker.mender.io/browse/MEN-3761))
* Fix error that no recipe provides bcm2835-bootfiles.
* mender-client: fix install of systemd-machine-id.service
* initramfs-module-install-efi: Ensure variable changes are reflected on rebuild
* vexpress: Remove nonexistent kernel config options that issue warnings.
* mender-commercial: Cleanup BBFILES.
* libubootenv: Drop bbappend file
* libubootenv: add RPROVIDES for u-boot-default-env
* Add mender-client 2.4.0 recipe.
* OpenSSL: qemu: set SECLEVEL=2 in /etc/ssl/openssl.cnf
  ([MEN-3730](https://tracker.mender.io/browse/MEN-3730))
* Fixed key extraction by skipping new lines in defconfig.
  The `add_kconfig_option_with_depends.py` file throws `Not sure how to
  handle Kconfig option that doesn't start with 'CONFIG_'` when the
  provided defconfig file contains blank lines. It has been fixed by
  checking for empty lines before processing for keys.
* Add mender-client 2.4.0 recipe.


## mender-convert 2.2.0

_Released 09.16.2020_

### Statistics

A total of 436 lines added, 56 removed (delta 380)

| Developers with the most changesets | |
|---|---|
| Drew Moseley | 12 (44.4%) |
| Lluis Campos | 7 (25.9%) |
| Dell Green | 2 (7.4%) |
| Kristian Amlie | 2 (7.4%) |
| Marek Belisko | 1 (3.7%) |
| Peter Grzybowski | 1 (3.7%) |
| Ole Petter Orhagen | 1 (3.7%) |
| Purushotham Nayak | 1 (3.7%) |

| Developers with the most changed lines | |
|---|---|
| Dell Green | 309 (70.9%) |
| Drew Moseley | 53 (12.2%) |
| Lluis Campos | 25 (5.7%) |
| Ole Petter Orhagen | 14 (3.2%) |
| Marek Belisko | 13 (3.0%) |
| Purushotham Nayak | 11 (2.5%) |
| Peter Grzybowski | 8 (1.8%) |
| Kristian Amlie | 3 (0.7%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 23 (85.2%) |
| Ideaworks Ltd | 2 (7.4%) |
| Cisco Systems, Inc. | 1 (3.7%) |
| open-nandra | 1 (3.7%) |

| Top lines changed by employer | |
|---|---|
| Ideaworks Ltd | 309 (70.9%) |
| Northern.tech | 103 (23.6%) |
| open-nandra | 13 (3.0%) |
| Cisco Systems, Inc. | 11 (2.5%) |

| Employers with the most hackers (total 8) | |
|---|---|
| Northern.tech | 5 (62.5%) |
| Ideaworks Ltd | 1 (12.5%) |
| open-nandra | 1 (12.5%) |
| Cisco Systems, Inc. | 1 (12.5%) |

### Changelogs

#### mender-convert (2.2.0)

New changes in mender-convert since 2.1.0:

* Fix missed log messages.
* Unmount filesystem images before creating full image.
* Fix incorrect file ownership on artifact_info file
* Extract debian package contents with sudo.
* Probing of kernel and initrd now handles multiple instances and symlinks
  ([MEN-3640](https://tracker.mender.io/browse/MEN-3640))
* Fix error when partitions numbers are not sequential
* chmod 600 on mender.conf
  ([MEN-3762](https://tracker.mender.io/browse/MEN-3762))
* Partition UUID support added for gpt/dos partition tables for deterministic booting
  ([MEN-3725](https://tracker.mender.io/browse/MEN-3725))
* mender-convert-modify: Use sudo to copy DTBs.
* raspberrypi: Do not overwrite existing kernel.
* mender-convert-modify: Check is selinux is configured in enforce mode and force rootfs-relabel
* Account for root ownership of overlay files.
* Cleanup more bootloader files.
* Allow for custom options when creating filesystems.
* Allow for custom option when mounting filesystems.
* Update mender-artifact to 3.4.0
* Warn user when converting read-only file systems that would
  result in unstable checksums, making the image incompatible with Mender
  Delta updates.
  ([MEN-3912](https://tracker.mender.io/browse/MEN-3912))
* Update mender client to 2.4.0


## Mender 2.5.0

_Released 09.11.2020_

### Statistics

A total of 64300 lines added, 23895 removed (delta 40405)

| Developers with the most changesets | |
|---|---|
| Manuel Zedel | 297 (30.5%) |
| Fabio Tranchitella | 199 (20.4%) |
| Alf-Rune Siqveland | 146 (15.0%) |
| Marcin Chalczynski | 138 (14.2%) |
| Lluis Campos | 49 (5.0%) |
| Peter Grzybowski | 41 (4.2%) |
| Krzysztof Jaskiewicz | 29 (3.0%) |
| Kristian Amlie | 26 (2.7%) |
| Ole Petter Orhagen | 23 (2.4%) |
| Michael Clelland | 11 (1.1%) |

| Developers with the most changed lines | |
|---|---|
| Alf-Rune Siqveland | 19875 (28.8%) |
| Marcin Chalczynski | 13236 (19.2%) |
| Fabio Tranchitella | 12574 (18.2%) |
| Manuel Zedel | 11331 (16.4%) |
| Krzysztof Jaskiewicz | 4638 (6.7%) |
| Peter Grzybowski | 3620 (5.3%) |
| Ole Petter Orhagen | 1558 (2.3%) |
| Lluis Campos | 757 (1.1%) |
| Kristian Amlie | 694 (1.0%) |
| Michael Clelland | 525 (0.8%) |

| Developers with the most lines removed | |
|---|---|
| Felix Breuer | 7 (0.0%) |
| Torben Hohn | 5 (0.0%) |
| Mirza Krak | 3 (0.0%) |

| Developers with the most signoffs (total 5) | |
|---|---|
| Kurt Kiefer | 2 (40.0%) |
| Fabio Tranchitella | 2 (40.0%) |
| Ole Petter Orhagen | 1 (20.0%) |

| Developers with the most reviews (total 6) | |
|---|---|
| Bastian Germann | 6 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 796 (81.7%) |
| RnDity | 167 (17.1%) |
| Linutronix GmbH | 6 (0.6%) |
| matt@madison.systems | 2 (0.2%) |
| f.breuer94@gmail.com | 1 (0.1%) |
| peron.clem@gmail.com | 1 (0.1%) |
| Wifx | 1 (0.1%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 50941 (73.9%) |
| RnDity | 17874 (25.9%) |
| Linutronix GmbH | 71 (0.1%) |
| matt@madison.systems | 7 (0.0%) |
| f.breuer94@gmail.com | 7 (0.0%) |
| peron.clem@gmail.com | 2 (0.0%) |
| Wifx | 2 (0.0%) |

| Employers with the most signoffs (total 5) | |
|---|---|
| Northern.tech | 3 (60.0%) |
| kekiefer@gmail.com | 2 (40.0%) |

| Employers with the most hackers (total 18) | |
|---|---|
| Northern.tech | 11 (61.1%) |
| RnDity | 2 (11.1%) |
| Linutronix GmbH | 1 (5.6%) |
| matt@madison.systems | 1 (5.6%) |
| f.breuer94@gmail.com | 1 (5.6%) |
| peron.clem@gmail.com | 1 (5.6%) |
| Wifx | 1 (5.6%) |

### Changelogs

#### deployments (2.1.0)

New changes in deployments since 2.0.0:

* Remove mongodb write/read concerns, let the connection string set them
* override file name in artifact download links
  ([MEN-3417](https://tracker.mender.io/browse/MEN-3417))
* New endpoint to deploy to group of devices
  `POST /deployments/group/:name`
  ([MEN-3411](https://tracker.mender.io/browse/MEN-3411))
* New internal health check and liveliness endpoints
  `GET /api/internal/v1/deployments/health`
  `GET /api/internal/v1/deployments/alive`
  ([MEN-3024](https://tracker.mender.io/browse/MEN-3024))

#### deployments-enterprise (2.1.0)

New changes in deployments-enterprise since 2.0.0:

* Remove mongodb write/read concerns, let the connection string set them
* override file name in artifact download links
  ([MEN-3417](https://tracker.mender.io/browse/MEN-3417))
* New endpoint to deploy to group of devices
  `POST /deployments/group/:name`
  ([MEN-3411](https://tracker.mender.io/browse/MEN-3411))
* New internal health check and liveliness endpoints
  `GET /api/internal/v1/deployments/health`
  `GET /api/internal/v1/deployments/alive`
  ([MEN-3024](https://tracker.mender.io/browse/MEN-3024))

#### deviceauth (2.4.0)

New changes in deviceauth since 2.3.0:

* internal API end-point to delete tenant limits
  ([MC-4040](https://tracker.mender.io/browse/MC-4040))
* Add support for ED25519 and ECDSA public keys in auth requests
  ([MEN-3728](https://tracker.mender.io/browse/MEN-3728))
* New internal health check and liveliness endpoints
  `GET /api/internal/v1/deviceauth/health`
  `GET /api/internal/v1/deviceauth/alive`
  ([MEN-3024](https://tracker.mender.io/browse/MEN-3024))
* device preauthorization: in case of conflict return conflicting device
  ([MEN-3813](https://tracker.mender.io/browse/MEN-3813))

#### gui (2.5.0)

New changes in gui since 2.4.0:

* added roles management to settings to allow adding group based roles
* fixed identity attribute filtering on authorized devices
  ([MEN-3517](https://tracker.mender.io/browse/MEN-3517))
* enabled automatic selection on filter autocomplete
  ([MEN-3518](https://tracker.mender.io/browse/MEN-3518))
* ensured onboarding tooltip shows up after custom artifact is uploaded
* add cancel subscription form in organization page
  ([MEN-3306](https://tracker.mender.io/browse/MEN-3306))
* fixed an issue that caused unexpected deployment device states to crash the deployment report
* fixed an issue that prevented exists filter from working
* combined bulk device actions in speed dial on device selection
  this allows easier device accepting, rejecting or group membership changes
* fixed settings availability in OS & onprem-enterprise deployments
* reintroduced ungrouped group
* switched group based deployment to use corresponding api endpoint
  this reduced the need to retrieve all group devices in the UI
* adjusted group creation dialog to focus on device selection outside of dialog
* Add upgrade page for trial users
* added sorting capabilities to device lists
* enabled dual rbac roles for groups to align with new rbac role in backend
* added cancellation option for artifact upload & generation
* fixed authorization header in userapi calls
* Add livechat widget component
* Aggregated Dependabot Changelogs:
  * Bumps node from 12.14.0-alpine to 14.4.0-alpine.
  * Bumps nginx from 1.17-alpine to 1.19.0-alpine.
  * Bumps [eslint](https://github.com/eslint/eslint) from 7.1.0 to 7.2.0.
    - [Release notes](https://github.com/eslint/eslint/releases)
    - [Changelog](https://github.com/eslint/eslint/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/eslint/eslint/compare/v7.1.0...v7.2.0)
  * Bumps [victory](https://github.com/formidablelabs/victory) from 34.3.10 to 34.3.11.
    - [Release notes](https://github.com/formidablelabs/victory/releases)
    - [Changelog](https://github.com/FormidableLabs/victory/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/formidablelabs/victory/compare/v34.3.10...v34.3.11)
  * Bumps [css-loader](https://github.com/webpack-contrib/css-loader) from 3.5.3 to 3.6.0.
    - [Release notes](https://github.com/webpack-contrib/css-loader/releases)
    - [Changelog](https://github.com/webpack-contrib/css-loader/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/css-loader/compare/v3.5.3...v3.6.0)
  * Bump node from 12.14.0-alpine to 14.4.0-alpine
  * Bump victory from 34.3.10 to 34.3.11
  * Bump nginx from 1.17-alpine to 1.19.0-alpine
  * Bump eslint from 7.1.0 to 7.2.0
  * Bump css-loader from 3.5.3 to 3.6.0
  * Bumps [moment](https://github.com/moment/moment) from 2.26.0 to 2.27.0.
    - [Release notes](https://github.com/moment/moment/releases)
    - [Changelog](https://github.com/moment/moment/blob/develop/CHANGELOG.md)
    - [Commits](https://github.com/moment/moment/compare/2.26.0...2.27.0)
  * Bumps [validator](https://github.com/chriso/validator.js) from 13.0.0 to 13.1.1.
    - [Release notes](https://github.com/chriso/validator.js/releases)
    - [Changelog](https://github.com/validatorjs/validator.js/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/chriso/validator.js/compare/13.0.0...13.1.1)
  * Bumps [eslint](https://github.com/eslint/eslint) from 7.2.0 to 7.3.0.
    - [Release notes](https://github.com/eslint/eslint/releases)
    - [Changelog](https://github.com/eslint/eslint/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/eslint/eslint/compare/v7.2.0...v7.3.0)
  * Bump eslint from 7.2.0 to 7.3.0
  * Bump validator from 13.0.0 to 13.1.1
  * Bump moment from 2.26.0 to 2.27.0
  * Bumps [eslint-plugin-import](https://github.com/benmosher/eslint-plugin-import) from 2.21.2 to 2.22.0.
    - [Release notes](https://github.com/benmosher/eslint-plugin-import/releases)
    - [Changelog](https://github.com/benmosher/eslint-plugin-import/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/benmosher/eslint-plugin-import/compare/v2.21.2...v2.22.0)
  * Bumps [webpack-cli](https://github.com/webpack/webpack-cli) from 3.3.11 to 3.3.12.
    - [Release notes](https://github.com/webpack/webpack-cli/releases)
    - [Changelog](https://github.com/webpack/webpack-cli/blob/v3.3.12/CHANGELOG.md)
    - [Commits](https://github.com/webpack/webpack-cli/compare/v3.3.11...v3.3.12)
  * Bumps [eslint](https://github.com/eslint/eslint) from 7.3.0 to 7.3.1.
    - [Release notes](https://github.com/eslint/eslint/releases)
    - [Changelog](https://github.com/eslint/eslint/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/eslint/eslint/compare/v7.3.0...v7.3.1)
  * Bumps [eslint-plugin-react](https://github.com/yannickcr/eslint-plugin-react) from 7.20.0 to 7.20.1.
    - [Release notes](https://github.com/yannickcr/eslint-plugin-react/releases)
    - [Changelog](https://github.com/yannickcr/eslint-plugin-react/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/yannickcr/eslint-plugin-react/compare/v7.20.0...v7.20.1)
  * Bump eslint-plugin-import from 2.21.2 to 2.22.0
  * Bump eslint from 7.3.0 to 7.3.1
  * Bump eslint-plugin-react from 7.20.0 to 7.20.1
  * Bump webpack-cli from 3.3.11 to 3.3.12
  * Bumps [copy-webpack-plugin](https://github.com/webpack-contrib/copy-webpack-plugin) from 6.0.2 to 6.0.3.
    - [Release notes](https://github.com/webpack-contrib/copy-webpack-plugin/releases)
    - [Changelog](https://github.com/webpack-contrib/copy-webpack-plugin/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/webpack-contrib/copy-webpack-plugin/compare/v6.0.2...v6.0.3)
  * Bumps [lint-staged](https://github.com/okonet/lint-staged) from 10.2.10 to 10.2.11.
    - [Release notes](https://github.com/okonet/lint-staged/releases)
    - [Commits](https://github.com/okonet/lint-staged/compare/v10.2.10...v10.2.11)
  * Bumps [autoprefixer](https://github.com/postcss/autoprefixer) from 9.8.0 to 9.8.4.
    - [Release notes](https://github.com/postcss/autoprefixer/releases)
    - [Changelog](https://github.com/postcss/autoprefixer/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/postcss/autoprefixer/compare/9.8.0...9.8.4)
  * Bumps [@babel/preset-env](https://github.com/babel/babel/tree/HEAD/packages/babel-preset-env) from 7.10.2 to 7.10.4.
    - [Release notes](https://github.com/babel/babel/releases)
    - [Changelog](https://github.com/babel/babel/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel/commits/v7.10.4/packages/babel-preset-env)
  * Bump autoprefixer from 9.8.0 to 9.8.4
  * Bump @babel/preset-env from 7.10.2 to 7.10.4
  * Bump copy-webpack-plugin from 6.0.2 to 6.0.3
  * Bump lint-staged from 10.2.10 to 10.2.11
  * Bumps [react-big-calendar](https://github.com/intljusticemission/react-big-calendar) from 0.25.0 to 0.26.0.
    - [Release notes](https://github.com/intljusticemission/react-big-calendar/releases)
    - [Changelog](https://github.com/jquense/react-big-calendar/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/intljusticemission/react-big-calendar/compare/v0.25.0...v0.26.0)
  * Bumps [superagent](https://github.com/visionmedia/superagent) from 5.2.2 to 5.3.1.
    - [Release notes](https://github.com/visionmedia/superagent/releases)
    - [Changelog](https://github.com/visionmedia/superagent/blob/master/HISTORY.md)
    - [Commits](https://github.com/visionmedia/superagent/compare/v5.2.2...v5.3.1)
  * Bumps node from 14.4.0-alpine to 14.5.0-alpine.
  * Bumps [@babel/plugin-proposal-class-properties](https://github.com/babel/babel/tree/HEAD/packages/babel-plugin-proposal-class-properties) from 7.10.1 to 7.10.4.
    - [Release notes](https://github.com/babel/babel/releases)
    - [Changelog](https://github.com/babel/babel/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel/commits/v7.10.4/packages/babel-plugin-proposal-class-properties)
  * Bumps [lodash](https://github.com/lodash/lodash) from 4.17.15 to 4.17.19.
    - [Release notes](https://github.com/lodash/lodash/releases)
    - [Commits](https://github.com/lodash/lodash/compare/4.17.15...4.17.19)
  * Bumps nginx from 1.19.0-alpine to 1.19.1-alpine.
  * Bumps [victory](https://github.com/formidablelabs/victory) from 34.3.11 to 35.0.5.
    - [Release notes](https://github.com/formidablelabs/victory/releases)
    - [Changelog](https://github.com/FormidableLabs/victory/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/formidablelabs/victory/compare/v34.3.11...v35.0.5)
  * Bumps [elliptic](https://github.com/indutny/elliptic) from 6.5.2 to 6.5.3.
    - [Release notes](https://github.com/indutny/elliptic/releases)
    - [Commits](https://github.com/indutny/elliptic/compare/v6.5.2...v6.5.3)
  * Bump react-big-calendar from 0.25.0 to 0.26.0
  * Bump superagent from 5.2.2 to 5.3.1
  * Bump node from 14.4.0-alpine to 14.5.0-alpine
  * Bump @babel/plugin-proposal-class-properties from 7.10.1 to 7.10.4
  * Bump lodash from 4.17.15 to 4.17.19
  * Bump nginx from 1.19.0-alpine to 1.19.1-alpine
  * Bump victory from 34.3.11 to 35.0.5
  * Bump elliptic from 6.5.2 to 6.5.3
  * Bumps node from 14.5.0-alpine to 14.7.0-alpine.
  * Bumps [react-dropzone](https://github.com/react-dropzone/react-dropzone) from 11.0.1 to 11.0.2.
    - [Release notes](https://github.com/react-dropzone/react-dropzone/releases)
    - [Commits](https://github.com/react-dropzone/react-dropzone/compare/v11.0.1...v11.0.2)
  * Bump react-dropzone from 11.0.1 to 11.0.2
  * Bump node from 14.5.0-alpine to 14.7.0-alpine
  * Bumps [react-ga](https://github.com/react-ga/react-ga) from 3.0.0 to 3.1.2.
    - [Release notes](https://github.com/react-ga/react-ga/releases)
    - [Commits](https://github.com/react-ga/react-ga/compare/v3.0.0...v3.1.2)
  * Bumps [victory](https://github.com/formidablelabs/victory) from 34.3.11 to 35.0.8.
    - [Release notes](https://github.com/formidablelabs/victory/releases)
    - [Changelog](https://github.com/FormidableLabs/victory/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/formidablelabs/victory/compare/v34.3.11...v35.0.8)
  * Bumps [@mdi/js](https://github.com/Templarian/MaterialDesign-JS) from 5.3.45 to 5.4.55.
    - [Release notes](https://github.com/Templarian/MaterialDesign-JS/releases)
    - [Commits](https://github.com/Templarian/MaterialDesign-JS/compare/v5.3.45...v5.4.55)
  * Bumps [@stripe/stripe-js](https://github.com/stripe/stripe-js) from 1.7.0 to 1.8.0.
    - [Release notes](https://github.com/stripe/stripe-js/releases)
    - [Commits](https://github.com/stripe/stripe-js/compare/v1.7.0...v1.8.0)
  * Bumps node from 14.7.0-alpine to 14.8.0-alpine.
  * Bumps nginx from 1.19.1-alpine to 1.19.2-alpine.
  * Bump nginx from 1.19.1-alpine to 1.19.2-alpine
  * Bump node from 14.7.0-alpine to 14.8.0-alpine
  * Bump victory from 34.3.11 to 35.0.8
  * Bump react-ga from 3.0.0 to 3.1.2
  * Bump @stripe/stripe-js from 1.7.0 to 1.8.0
  * Bump @mdi/js from 5.3.45 to 5.4.55
  * Bumps [@mdi/js](https://github.com/Templarian/MaterialDesign-JS) from 5.4.55 to 5.5.55.
    - [Release notes](https://github.com/Templarian/MaterialDesign-JS/releases)
    - [Commits](https://github.com/Templarian/MaterialDesign-JS/compare/v5.4.55...v5.5.55)
  * Bump @mdi/js from 5.4.55 to 5.5.55
  * Bumps [axios](https://github.com/axios/axios) from 0.19.2 to 0.20.0.
    - [Release notes](https://github.com/axios/axios/releases)
    - [Changelog](https://github.com/axios/axios/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/axios/axios/compare/v0.19.2...v0.20.0)
  * Bumps [react-dropzone](https://github.com/react-dropzone/react-dropzone) from 11.0.2 to 11.0.3.
    - [Release notes](https://github.com/react-dropzone/react-dropzone/releases)
    - [Commits](https://github.com/react-dropzone/react-dropzone/compare/v11.0.2...v11.0.3)
  * Bumps [@babel/preset-env](https://github.com/babel/babel/tree/HEAD/packages/babel-preset-env) from 7.10.4 to 7.11.0.
    - [Release notes](https://github.com/babel/babel/releases)
    - [Changelog](https://github.com/babel/babel/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel/commits/v7.11.0/packages/babel-preset-env)
  * Bumps [jest-resolve](https://github.com/facebook/jest/tree/HEAD/packages/jest-resolve) from 26.0.1 to 26.4.0.
    - [Release notes](https://github.com/facebook/jest/releases)
    - [Changelog](https://github.com/facebook/jest/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/facebook/jest/commits/v26.4.0/packages/jest-resolve)
  * Bump jest-resolve from 26.0.1 to 26.4.0
  * Bump @babel/preset-env from 7.10.4 to 7.11.0
  * Bump react-dropzone from 11.0.2 to 11.0.3
  * Bump axios from 0.19.2 to 0.20.0
  * Bumps node from 14.8.0-alpine to 14.9.0-alpine.
  * Bumps [eslint](https://github.com/eslint/eslint) from 7.3.1 to 7.7.0.
    - [Release notes](https://github.com/eslint/eslint/releases)
    - [Changelog](https://github.com/eslint/eslint/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/eslint/eslint/compare/v7.3.1...v7.7.0)
  * Bumps [@babel/preset-react](https://github.com/babel/babel/tree/HEAD/packages/babel-preset-react) from 7.10.1 to 7.10.4.
    - [Release notes](https://github.com/babel/babel/releases)
    - [Changelog](https://github.com/babel/babel/blob/main/CHANGELOG.md)
    - [Commits](https://github.com/babel/babel/commits/v7.10.4/packages/babel-preset-react)
  * Bumps [yarn](https://github.com/yarnpkg/yarn) from 1.22.4 to 1.22.5.
    - [Release notes](https://github.com/yarnpkg/yarn/releases)
    - [Changelog](https://github.com/yarnpkg/yarn/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/yarnpkg/yarn/compare/v1.22.4...v1.22.5)
  * Bump @babel/preset-react from 7.10.1 to 7.10.4
  * Bump yarn from 1.22.4 to 1.22.5
  * Bump eslint from 7.3.1 to 7.7.0
  * Bump node from 14.8.0-alpine to 14.9.0-alpine
  * Bumps [enzyme-adapter-react-16](https://github.com/enzymejs/enzyme/tree/HEAD/packages/enzyme-adapter-react-16) from 1.15.2 to 1.15.4.
    - [Release notes](https://github.com/enzymejs/enzyme/releases)
    - [Changelog](https://github.com/enzymejs/enzyme/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/enzymejs/enzyme/commits/enzyme-adapter-react-16@1.15.4/packages/enzyme-adapter-react-16)
  * Bump enzyme-adapter-react-16 from 1.15.2 to 1.15.4

#### integration (2.5.0)

New changes in integration since 2.4.0:

* docker compose: minio now restart on-failure
* Restore docker-compose.storage.s3.yml
* upgrade MongoDB from version 3.6 to version 4.4 (latest stable)
* Upgrade deployments to 2.1.0.
* Upgrade deployments-enterprise to 2.1.0.
* Upgrade deviceauth to 2.4.0.
* Upgrade gui to 2.5.0.
* Upgrade inventory to 2.1.0.
* Upgrade inventory-enterprise to 2.1.0.
* Upgrade mender to 2.4.0.
* Upgrade mender-api-gateway-docker to 2.3.0.
* Upgrade mender-cli to 1.5.0.
* Add mtls-ambassador 1.0.0.
* Upgrade tenantadm to 2.1.0.
* Upgrade useradm to 1.12.0.
* Upgrade useradm-enterprise to 1.12.0.
* Upgrade workflows to 1.2.0.
* Upgrade workflows-enterprise to 1.2.0.
* Aggregated Dependabot Changelogs:
  * Bumps [requests](https://github.com/psf/requests) from 2.22.0 to 2.23.0.
    - [Release notes](https://github.com/psf/requests/releases)
    - [Changelog](https://github.com/psf/requests/blob/master/HISTORY.md)
    - [Commits](https://github.com/psf/requests/compare/v2.22.0...v2.23.0)
  * Bumps [stripe](https://github.com/stripe/stripe-python) from 2.42.0 to 2.48.0.
    - [Release notes](https://github.com/stripe/stripe-python/releases)
    - [Changelog](https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/stripe/stripe-python/compare/v2.42.0...v2.48.0)
  * Bumps [pillow](https://github.com/python-pillow/Pillow) from 7.0.0 to 7.1.2.
    - [Release notes](https://github.com/python-pillow/Pillow/releases)
    - [Changelog](https://github.com/python-pillow/Pillow/blob/master/CHANGES.rst)
    - [Commits](https://github.com/python-pillow/Pillow/compare/7.0.0...7.1.2)
  * Bumps [pytest-html](https://github.com/pytest-dev/pytest-html) from 2.0.1 to 2.1.1.
    - [Release notes](https://github.com/pytest-dev/pytest-html/releases)
    - [Changelog](https://github.com/pytest-dev/pytest-html/blob/master/CHANGES.rst)
    - [Commits](https://github.com/pytest-dev/pytest-html/compare/v2.0.1...v2.1.1)
  * Bumps [docker-compose](https://github.com/docker/compose) from 1.25.4 to 1.26.0.
    - [Release notes](https://github.com/docker/compose/releases)
    - [Changelog](https://github.com/docker/compose/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/docker/compose/compare/1.25.4...1.26.0)
  * Bumps [requests](https://github.com/psf/requests) from 2.22.0 to 2.23.0.
    - [Release notes](https://github.com/psf/requests/releases)
    - [Changelog](https://github.com/psf/requests/blob/master/HISTORY.md)
    - [Commits](https://github.com/psf/requests/compare/v2.22.0...v2.23.0)
  * Bumps [pytest-html](https://github.com/pytest-dev/pytest-html) from 2.0.1 to 2.1.1.
    - [Release notes](https://github.com/pytest-dev/pytest-html/releases)
    - [Changelog](https://github.com/pytest-dev/pytest-html/blob/master/CHANGES.rst)
    - [Commits](https://github.com/pytest-dev/pytest-html/compare/v2.0.1...v2.1.1)
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 5.3.4 to 5.4.3.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/5.3.4...5.4.3)
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 5.3.4 to 5.4.3.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/5.3.4...5.4.3)
  * : Bump pytest from 5.3.4 to 5.4.3 in /backend-tests
  * Bump pytest from 5.3.4 to 5.4.3 in /tests/requirements
  * Bumps [cryptography](https://github.com/pyca/cryptography) from 2.8 to 2.9.2.
    - [Release notes](https://github.com/pyca/cryptography/releases)
    - [Changelog](https://github.com/pyca/cryptography/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pyca/cryptography/compare/2.8...2.9.2)
  * Bumps [paramiko](https://github.com/paramiko/paramiko) from 2.6.0 to 2.7.1.
    - [Release notes](https://github.com/paramiko/paramiko/releases)
    - [Changelog](https://github.com/paramiko/paramiko/blob/master/NEWS)
    - [Commits](https://github.com/paramiko/paramiko/compare/2.6.0...2.7.1)
  * Bump cryptography from 2.8 to 2.9.2 in /backend-tests
  * Bump paramiko from 2.6.0 to 2.7.1 in /tests/requirements
  * Bumps [pillow](https://github.com/python-pillow/Pillow) from 7.1.2 to 7.2.0.
    - [Release notes](https://github.com/python-pillow/Pillow/releases)
    - [Changelog](https://github.com/python-pillow/Pillow/blob/master/CHANGES.rst)
    - [Commits](https://github.com/python-pillow/Pillow/compare/7.1.2...7.2.0)
  * Bumps [docker-compose](https://github.com/docker/compose) from 1.26.0 to 1.26.2.
    - [Release notes](https://github.com/docker/compose/releases)
    - [Changelog](https://github.com/docker/compose/blob/1.26.2/CHANGELOG.md)
    - [Commits](https://github.com/docker/compose/compare/1.26.0...1.26.2)
  * Bump docker-compose from 1.26.0 to 1.26.2 in /tests/requirements
  * Bump pillow from 7.1.2 to 7.2.0 in /backend-tests
  * Bumps [requests](https://github.com/psf/requests) from 2.23.0 to 2.24.0.
    - [Release notes](https://github.com/psf/requests/releases)
    - [Changelog](https://github.com/psf/requests/blob/master/HISTORY.md)
    - [Commits](https://github.com/psf/requests/compare/v2.23.0...v2.24.0)
  * Bumps [requests](https://github.com/psf/requests) from 2.23.0 to 2.24.0.
    - [Release notes](https://github.com/psf/requests/releases)
    - [Changelog](https://github.com/psf/requests/blob/master/HISTORY.md)
    - [Commits](https://github.com/psf/requests/compare/v2.23.0...v2.24.0)
  * Bump requests from 2.23.0 to 2.24.0 in /tests/requirements
  * Bump requests from 2.23.0 to 2.24.0 in /backend-tests
  * Bumps [cryptography](https://github.com/pyca/cryptography) from 2.9.2 to 3.0.
    - [Release notes](https://github.com/pyca/cryptography/releases)
    - [Changelog](https://github.com/pyca/cryptography/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pyca/cryptography/compare/2.9.2...3.0)
  * Bumps [stripe](https://github.com/stripe/stripe-python) from 2.48.0 to 2.49.0.
    - [Release notes](https://github.com/stripe/stripe-python/releases)
    - [Changelog](https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/stripe/stripe-python/compare/v2.48.0...v2.49.0)
  * Bumps [pymongo](https://github.com/mongodb/mongo-python-driver) from 3.10.1 to 3.11.0.
    - [Release notes](https://github.com/mongodb/mongo-python-driver/releases)
    - [Changelog](https://github.com/mongodb/mongo-python-driver/blob/master/doc/changelog.rst)
    - [Commits](https://github.com/mongodb/mongo-python-driver/compare/3.10.1...3.11.0)
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 5.4.3 to 6.0.1.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/5.4.3...6.0.1)
  * Bumps [pyotp](https://github.com/pyotp/pyotp) from 2.3.0 to 2.4.0.
    - [Release notes](https://github.com/pyotp/pyotp/releases)
    - [Changelog](https://github.com/pyauth/pyotp/blob/master/Changes.rst)
    - [Commits](https://github.com/pyotp/pyotp/compare/v2.3.0...v2.4.0)
  * Bumps [pymongo](https://github.com/mongodb/mongo-python-driver) from 3.10.1 to 3.11.0.
    - [Release notes](https://github.com/mongodb/mongo-python-driver/releases)
    - [Changelog](https://github.com/mongodb/mongo-python-driver/blob/master/doc/changelog.rst)
    - [Commits](https://github.com/mongodb/mongo-python-driver/compare/3.10.1...3.11.0)
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 5.4.3 to 6.0.1.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/5.4.3...6.0.1)
  * Bumps [stripe](https://github.com/stripe/stripe-python) from 2.49.0 to 2.50.0.
    - [Release notes](https://github.com/stripe/stripe-python/releases)
    - [Changelog](https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/stripe/stripe-python/compare/v2.49.0...v2.50.0)
  * Bump stripe from 2.49.0 to 2.50.0 in /backend-tests
  * Bumps [cryptography](https://github.com/pyca/cryptography) from 3.0 to 3.1.
    - [Release notes](https://github.com/pyca/cryptography/releases)
    - [Changelog](https://github.com/pyca/cryptography/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pyca/cryptography/compare/3.0...3.1)
  * Bumps [paramiko](https://github.com/paramiko/paramiko) from 2.7.1 to 2.7.2.
    - [Release notes](https://github.com/paramiko/paramiko/releases)
    - [Changelog](https://github.com/paramiko/paramiko/blob/master/NEWS)
    - [Commits](https://github.com/paramiko/paramiko/compare/2.7.1...2.7.2)
  * Bump paramiko from 2.7.1 to 2.7.2 in /tests/requirements
  * Bump cryptography from 3.0 to 3.1 in /backend-tests

#### inventory (2.1.0)

New changes in inventory since 2.0.0:

* New endpoints for managing devices' group in bulk.
* Add $nin ("not in") operator for searching devices
* Add status query parameter to GET /groups
* New internal health check and liveliness endpoints
  `GET /api/internal/v1/inventory/health`
  `GET /api/internal/v1/inventory/alive`
  ([MEN-3024](https://tracker.mender.io/browse/MEN-3024))

#### inventory-enterprise (2.1.0)

New changes in inventory-enterprise since 2.0.0:

* New endpoints for managing devices' group in bulk.
* RBAC dynamic groups
  ([MEN-3626](https://tracker.mender.io/browse/MEN-3626))
* Introduce the $regex filter operator
* Add $nin ("not in") operator for searching devices
* Add status query parameter to GET /groups
* New internal health check and liveliness endpoints
  `GET /api/internal/v1/inventory/health`
  `GET /api/internal/v1/inventory/alive`
  ([MEN-3024](https://tracker.mender.io/browse/MEN-3024))

#### mender (2.4.0)

New changes in mender since 2.3.0:

* keystore: use openssl bindings
  Switch the code that signs the server's authentication request
  to use openssl. This allows to use ssl_engines, which permit to
  use PKCS#11 or TPMs as keystore.
* vendor: switch openssl bindings to github.com/Linutronix/golang-openssl
  spacemonkeygo/openssl depends on spacelog, which increases binary
  size by about 2MB due to using reflect.
  Switch to a fork which has the logger removed.
  This patch can hopefully be reverted someday, when the logger
  removal has been mainlined.
* Log state-script stderr as info, not error
  ([MEN-3316](https://tracker.mender.io/browse/MEN-3316))
* mender-inventory-geo script to return geo localization data
* Add support for libubootenv as boot loader user space tools
  provider. ([MEN-3684](https://tracker.mender.io/browse/MEN-3684))
* Remove Server config warn on mender setup command
  ([MEN-3652](https://tracker.mender.io/browse/MEN-3652))
* Fix broken logging to syslogger.
  ([MEN-3676](https://tracker.mender.io/browse/MEN-3676))
* chmod 600 on config file
  ([MEN-3762](https://tracker.mender.io/browse/MEN-3762))
* mender-device-identity: skip dummyX interfaces
* mender.service: update to run after network-online.target
* Switch to OpenSSL for all server communication.
  ([MEN-3730](https://tracker.mender.io/browse/MEN-3730))
* keystore: support ed25519 keys
* Add the ability to configure the client with a client certificate and
  private key in order to enable mTLS in the client communication setup.
  ([MEN-3115](https://tracker.mender.io/browse/MEN-3115))

#### mender-api-gateway-docker (2.3.0)

New changes in mender-api-gateway-docker since 2.2.0:

* Return valid JSON documents as error pages' payloads
* , expose password-reset end-points without auth
  ([MEN-3544](https://tracker.mender.io/browse/MEN-3544), [MEN-3546](https://tracker.mender.io/browse/MEN-3546))

#### mender-cli (1.5.0)

New changes in mender-cli since 1.4.0:

* Add: Make the server flag default to hosted Mender
* Add: Bash auto-completion functionality
* Add: Zsh auto-completion support
* Add: Configuration file functionality
  This adds the possibility to add the username and password to a configuration
  file, in which the 'mender-cli' tool will look if no password or username is set
  on the CLI. The configuration file is expected to be JSON.
  The configuration file can be located in one of:
  * /etc/mender-cli
  * $HOME
  * . (directory where binary is run from)
  and must be named like:
  ```console
  .mender-clirc.json
  ```
  This helps usage, in that now, in order to login, a user with a configuration
  file can do:
  ```console
  $ mender-cli login
  ```
  as opposed to:
  ```console
  $ mender-cli --username foo --password bar --server bar.com
  ```
  The parameters which are configurable from the config file are:
  * username
  * password
  * server

#### mtls-ambassador (1.0.0)

* support ecdsa and ed25519
* management token refresh

#### tenantadm (2.1.0)

New changes in tenantadm since 2.0.0:

* new management end-point to request tenant's cancellation
  ([MEN-3305](https://tracker.mender.io/browse/MEN-3305))
* Remove mongodb write/read concerns, let the connection string set them
* introduce a new end-point to create trial tenants
  ([MEN-3613](https://tracker.mender.io/browse/MEN-3613))
* new end-points to upgrade a trial tenant to a paid plan
  ([MEN-3615](https://tracker.mender.io/browse/MEN-3615))
* internal API end-point to update tenants
  ([MC-4040](https://tracker.mender.io/browse/MC-4040))
* Store marketing consent from the sign up form in stripe
* OAuth2 signup support for GitHub and Google
* add support for the + character in the email address
  ([MEN-1969](https://tracker.mender.io/browse/MEN-1969))
* New internal health check and liveliness endpoints
  `GET /api/internal/v1/tenantadm/health`
  `GET /api/internal/v1/tenantadm/alive`
  ([MEN-3024](https://tracker.mender.io/browse/MEN-3024))

#### useradm (1.12.0)

New changes in useradm since 1.11.0:

* Remove mongodb write concern, let the connection string set them
* add support for the + character in the email address
  ([MEN-1969](https://tracker.mender.io/browse/MEN-1969))
* New internal health check and liveliness endpoints
  `GET /api/internal/v1/useradm/health`
  `GET /api/internal/v1/useradm/alive`
  ([MEN-3024](https://tracker.mender.io/browse/MEN-3024))

#### useradm-enterprise (1.12.0)

New changes in useradm-enterprise since 1.11.0:

* Remove mongodb write concern, let the connection string set them
* Remove mongodb write concern, let the connection string set them
* Separate RBAC of visibility and deployments.
  ([MEN-3629](https://tracker.mender.io/browse/MEN-3629))
* OAuth2: Login using GitHub and Google account
* add support for the + character in the email address
  ([MEN-1969](https://tracker.mender.io/browse/MEN-1969))
* add support for the + character in the email address
  ([MEN-1969](https://tracker.mender.io/browse/MEN-1969))
* New internal health check and liveliness endpoints
  `GET /api/internal/v1/useradm/health`
  `GET /api/internal/v1/useradm/alive`
  ([MEN-3024](https://tracker.mender.io/browse/MEN-3024))

#### workflows (1.2.0)

New changes in workflows since 1.1.0:

* add support for sending html (mime/alternative) messages
  ([MEN-3509](https://tracker.mender.io/browse/MEN-3509))
* Add Go Template processing of http task's request body
* Add support for yaml workflow definitions
* New internal health check endpoint
  `GET /api/internal/v1/workflows/health`
  ([MEN-3024](https://tracker.mender.io/browse/MEN-3024))

#### workflows-enterprise (1.2.0)

New changes in workflows-enterprise since 1.1.0:

* Add new workflow cancel_tenant to send cancellation request email
  ([MEN-3305](https://tracker.mender.io/browse/MEN-3305))
* add support for sending html (mime/alternative) messages
  ([MEN-3509](https://tracker.mender.io/browse/MEN-3509))
* Add Go Template processing of http task's request body
* Add support for yaml workflow definitions
* new workflow send_password_reset_email for password resets
  ([MEN-3545](https://tracker.mender.io/browse/MEN-3545))
* New internal health check endpoint
  `GET /api/internal/v1/workflows/health`
  ([MEN-3024](https://tracker.mender.io/browse/MEN-3024))


## Mender 2.4.1

_Released 09.01.2020_

### Statistics

A total of 41 lines added, 40 removed (delta 1)

| Developers with the most changesets | |
|---|---|
| Lluis Campos | 3 (100.0%) |

| Developers with the most changed lines | |
|---|---|
| Lluis Campos | 44 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 3 (100.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 44 (100.0%) |

| Employers with the most hackers (total 1) | |
|---|---|
| Northern.tech | 1 (100.0%) |

### Changelogs

#### integration (2.4.1)

New changes in integration since 2.4.0:

* Upgrade inventory to 2.0.1.
* Upgrade inventory-enterprise to 2.0.1.
* Aggregated Dependabot Changelogs:
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 5.3.4 to 5.4.3.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/5.3.4...5.4.3)
  * Bumps [paramiko](https://github.com/paramiko/paramiko) from 2.6.0 to 2.7.1.
    - [Release notes](https://github.com/paramiko/paramiko/releases)
    - [Changelog](https://github.com/paramiko/paramiko/blob/master/NEWS)
    - [Commits](https://github.com/paramiko/paramiko/compare/2.6.0...2.7.1)
  * Bumps [pymongo](https://github.com/mongodb/mongo-python-driver) from 3.10.1 to 3.11.0.
    - [Release notes](https://github.com/mongodb/mongo-python-driver/releases)
    - [Changelog](https://github.com/mongodb/mongo-python-driver/blob/master/doc/changelog.rst)
    - [Commits](https://github.com/mongodb/mongo-python-driver/compare/3.10.1...3.11.0)
  * Bumps [pytest](https://github.com/pytest-dev/pytest) from 5.4.3 to 6.0.1.
    - [Release notes](https://github.com/pytest-dev/pytest/releases)
    - [Changelog](https://github.com/pytest-dev/pytest/blob/master/CHANGELOG.rst)
    - [Commits](https://github.com/pytest-dev/pytest/compare/5.4.3...6.0.1)
  * Bumps [docker-compose](https://github.com/docker/compose) from 1.25.4 to 1.26.0.
    - [Release notes](https://github.com/docker/compose/releases)
    - [Changelog](https://github.com/docker/compose/blob/master/CHANGELOG.md)
    - [Commits](https://github.com/docker/compose/compare/1.25.4...1.26.0)
  * Bumps [requests](https://github.com/psf/requests) from 2.22.0 to 2.23.0.
    - [Release notes](https://github.com/psf/requests/releases)
    - [Changelog](https://github.com/psf/requests/blob/master/HISTORY.md)
    - [Commits](https://github.com/psf/requests/compare/v2.22.0...v2.23.0)
  * Bumps [pytest-html](https://github.com/pytest-dev/pytest-html) from 2.0.1 to 2.1.1.
    - [Release notes](https://github.com/pytest-dev/pytest-html/releases)
    - [Changelog](https://github.com/pytest-dev/pytest-html/blob/master/CHANGES.rst)
    - [Commits](https://github.com/pytest-dev/pytest-html/compare/v2.0.1...v2.1.1)
  * Bumps [docker-compose](https://github.com/docker/compose) from 1.26.0 to 1.26.2.
    - [Release notes](https://github.com/docker/compose/releases)
    - [Changelog](https://github.com/docker/compose/blob/1.26.2/CHANGELOG.md)
    - [Commits](https://github.com/docker/compose/compare/1.26.0...1.26.2)
  * Bumps [requests](https://github.com/psf/requests) from 2.23.0 to 2.24.0.
    - [Release notes](https://github.com/psf/requests/releases)
    - [Changelog](https://github.com/psf/requests/blob/master/HISTORY.md)
    - [Commits](https://github.com/psf/requests/compare/v2.23.0...v2.24.0)

#### inventory-enterprise (2.0.1)

New changes in inventory-enterprise since 2.0.0:

* Bugfix: Rejected devices remain listed in static
  groups, even after rejection.
  ([MEN-3793](https://tracker.mender.io/browse/MEN-3793))


## meta-mender warrior-v2020.07

_Released 07.29.2020_

### Statistics

A total of 171 lines added, 54 removed (delta 117)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 4 (50.0%) |
| Lluis Campos | 1 (12.5%) |
| Ossian Riday | 1 (12.5%) |
| Trevor Woerner | 1 (12.5%) |
| Garrett Brown | 1 (12.5%) |

| Developers with the most changed lines | |
|---|---|
| Garrett Brown | 147 (71.7%) |
| Kristian Amlie | 51 (24.9%) |
| Ossian Riday | 3 (1.5%) |
| Lluis Campos | 2 (1.0%) |
| Trevor Woerner | 2 (1.0%) |

| Developers with the most lines removed | |
|---|---|
| Kristian Amlie | 33 (61.1%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 5 (62.5%) |
| twoerner@gmail.com | 1 (12.5%) |
| Aclima Inc. | 1 (12.5%) |
| ossian.riday@gmail.com | 1 (12.5%) |

| Top lines changed by employer | |
|---|---|
| Aclima Inc. | 147 (71.7%) |
| Northern.tech | 53 (25.9%) |
| ossian.riday@gmail.com | 3 (1.5%) |
| twoerner@gmail.com | 2 (1.0%) |

| Employers with the most hackers (total 5) | |
|---|---|
| Northern.tech | 2 (40.0%) |
| Aclima Inc. | 1 (20.0%) |
| ossian.riday@gmail.com | 1 (20.0%) |
| twoerner@gmail.com | 1 (20.0%) |

### Changelogs

#### meta-mender (warrior-v2020.07)

New changes in meta-mender since warrior-v2020.06:

* Fix boot failure on ARM UEFI devices because of missing
  `regexp` module. A typical error log looks like this:
  ```
  Welcome to GRUB!
  ```
* Fix EFI boot partition corruption with mtools 4.0.19
* uboot_auto_configure: build U-Boot the same way Yocto does
* Add mender_2.3.0 and mender-artifact_3.4.0 recipes.
* Add mender-2.2.1 and mender-artifact-3.3.1 recipes.
* Add mender-binary-delta-1.1.0 release.
* MBR systems don't have a backup header, so always return true
  ([MEN-3761](https://tracker.mender.io/browse/MEN-3761))


## meta-mender dunfell-v2020.07

_Released 07.28.2020_

### Statistics

A total of 895 lines added, 2274 removed (delta -1379)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 26 (83.9%) |
| Peter Grzybowski | 1 (3.2%) |
| Lluis Campos | 1 (3.2%) |
| Corey Cothrum | 1 (3.2%) |
| Ole Petter Orhagen | 1 (3.2%) |
| Trevor Woerner | 1 (3.2%) |

| Developers with the most changed lines | |
|---|---|
| Kristian Amlie | 2435 (96.4%) |
| Corey Cothrum | 72 (2.8%) |
| Ole Petter Orhagen | 14 (0.6%) |
| Peter Grzybowski | 2 (0.1%) |
| Lluis Campos | 2 (0.1%) |
| Trevor Woerner | 2 (0.1%) |

| Developers with the most lines removed | |
|---|---|
| Kristian Amlie | 1459 (64.2%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 29 (93.5%) |
| twoerner@gmail.com | 1 (3.2%) |
| contact@coreycothrum.com | 1 (3.2%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 2453 (97.1%) |
| contact@coreycothrum.com | 72 (2.8%) |
| twoerner@gmail.com | 2 (0.1%) |

| Employers with the most hackers (total 6) | |
|---|---|
| Northern.tech | 4 (66.7%) |
| contact@coreycothrum.com | 1 (16.7%) |
| twoerner@gmail.com | 1 (16.7%) |

### Changelogs

#### meta-mender (dunfell-v2020.07)

New changes in meta-mender since zeus-v2020.06:

* uboot_auto_configure: build U-Boot the same way Yocto does
* Fix error message about `CONFIG_ENV_OFFSET` being wrong,
  such as:
  ```
  ERROR: u-boot-fw-utils-mender-auto-provided-1.0-r0 do_configure: U-Boot configuration rpi_4_config has setting:
  CONFIG_ENV_OFFSET=0x400000
  CONFIG_ENV_OFFSET_REDUND=0x800000
  but Mender expects:
  CONFIG_ENV_OFFSET=0x800000
  Please fix U-Boot’s configuration file.
  ```
* add support for separate A/B kernel partitions
* Add MENDER_EXTRA_PARTS_SIZES_MB variable
* U-Boot auto-configuration: Better algorithm for removing
  options from defconfig files. This increases board compatibility.
* Start using libubootenv for U-Boot environment manipulation.
  This deprecates the u-boot-fw-utils tools, which have been removed
  from upstream. The functionality and command line API is the same.
* `libubootenv` is now used instead of `u-boot-fw-utils`. If
  you have a "fw-utils" type recipe in your layer, you probably need to
  remove it, particularly if it references `u-boot-mender-common.inc`.
* Patch broken UBI support in libubootenv_0.2.
* chmod 600 on mender.conf
  ([MEN-3762](https://tracker.mender.io/browse/MEN-3762))
* Add mender-2.2.1 and mender-artifact-3.3.1 recipes.
* Add mender-2.3.0 and mender-artifact-3.4.0 recipes.
* Add mender-binary-delta-1.1.0 release.
* Remove mender-client recipes that are incompatible with dunfell.
  ([MEN-3764](https://tracker.mender.io/browse/MEN-3764))
* Fix incorrect BOOTENV_SIZE value being used in libubootenv
  recipe. The symptom of this was a non-working set of `fw_printenv` and
  `fw_setenv` tools:
  ```
  root@raspberrypi4:~# fw_printenv
  Cannot read environment, using default
  Cannot read default environment from file
  ```
  ([MEN-3834](https://tracker.mender.io/browse/MEN-3834))
* Fix fsck running on every boot in dunfell.

## meta-mender zeus-v2020.07

_Released 07.16.2020_

### Statistics

A total of 203 lines added, 1050 removed (delta -847)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 15 (83.3%) |
| Trevor Woerner | 1 (5.6%) |
| Ole Petter Orhagen | 1 (5.6%) |
| Lluis Campos | 1 (5.6%) |

| Developers with the most changed lines | |
|---|---|
| Kristian Amlie | 1145 (98.5%) |
| Ole Petter Orhagen | 14 (1.2%) |
| Trevor Woerner | 2 (0.2%) |
| Lluis Campos | 2 (0.2%) |

| Developers with the most lines removed | |
|---|---|
| Kristian Amlie | 862 (82.1%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 17 (94.4%) |
| twoerner@gmail.com | 1 (5.6%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 1161 (99.8%) |
| twoerner@gmail.com | 2 (0.2%) |

| Employers with the most hackers (total 4) | |
|---|---|
| Northern.tech | 3 (75.0%) |
| twoerner@gmail.com | 1 (25.0%) |

### Changelogs

#### meta-mender (zeus-v2020.07)

New changes in meta-mender since zeus-v2020.06:

* Fix error message about `CONFIG_ENV_OFFSET` being wrong,
  such as:
  ```
  ERROR: u-boot-fw-utils-mender-auto-provided-1.0-r0 do_configure: U-Boot configuration rpi_4_config has setting:
  CONFIG_ENV_OFFSET=0x400000
  CONFIG_ENV_OFFSET_REDUND=0x800000
  but Mender expects:
  CONFIG_ENV_OFFSET=0x800000
  Please fix U-Boot’s configuration file.
  ```
* add support for separate A/B kernel partitions
* U-Boot auto-configuration: Better algorithm for removing
  options from defconfig files. This increases board compatibility.
* uboot_auto_configure: build U-Boot the same way Yocto does
* Add mender-2.2.1 and mender-artifact-3.3.1 recipes.
* Add mender-2.3.0 and mender-artifact-3.4.0 recipes.
* Add mender-binary-delta-1.1.0 release.


## mender-convert 2.1.0

_Released 07.16.2020_

### Statistics

A total of 845 lines added, 251 removed (delta 594)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 21 (36.2%) |
| Drew Moseley | 14 (24.1%) |
| Ole Petter Orhagen | 14 (24.1%) |
| Nate Baker | 3 (5.2%) |
| Marek Belisko | 2 (3.4%) |
| Lluis Campos | 2 (3.4%) |
| Dell Green | 1 (1.7%) |
| Sylvain | 1 (1.7%) |

| Developers with the most changed lines | |
|---|---|
| Ole Petter Orhagen | 450 (52.9%) |
| Kristian Amlie | 203 (23.9%) |
| Drew Moseley | 80 (9.4%) |
| Marek Belisko | 66 (7.8%) |
| Nate Baker | 30 (3.5%) |
| Dell Green | 18 (2.1%) |
| Lluis Campos | 3 (0.4%) |
| Sylvain | 1 (0.1%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 51 (87.9%) |
| bakern@gmail.com | 3 (5.2%) |
| open-nandra | 2 (3.4%) |
| TideWise Ltda. | 1 (1.7%) |
| Ideaworks Ltd | 1 (1.7%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 736 (86.5%) |
| open-nandra | 66 (7.8%) |
| bakern@gmail.com | 30 (3.5%) |
| Ideaworks Ltd | 18 (2.1%) |
| TideWise Ltda. | 1 (0.1%) |

| Employers with the most hackers (total 8) | |
|---|---|
| Northern.tech | 4 (50.0%) |
| open-nandra | 1 (12.5%) |
| bakern@gmail.com | 1 (12.5%) |
| Ideaworks Ltd | 1 (12.5%) |
| TideWise Ltda. | 1 (12.5%) |

### Changelogs

#### mender-convert (2.1.0)

New changes in mender-convert since 2.1.0b1:

* Fix incorrect file ownership on artifact_info file
* Extract debian package contents with sudo.
* Fix missed log messages.
* Unmount filesystem images before creating full image.
* Upgrade to Mender 2.3.0 and mender-artifact 3.4.0.

New changes in mender-convert since 2.0.1:

* Use consistent compression and archive naming.
* Upgrade to GRUB 2.04.
* Add detection of problematic versions of U-Boot and kernel.
  ([MEN-2404](https://tracker.mender.io/browse/MEN-2404))
* Added color to the terminal log messages
* Added hooks to Mender convert
  This extends the current functionality of the platform_ function
  functionality into using hooks, so that each modification step can be called
  from multiple configuration files.
  The valid hooks are:
   * PLATFORM_MODIFY_HOOKS
   * PLATFORM_PACKAGE_HOOKS
   * USER_LOCAL_MODIFY_HOOKS
  and can be appended to as a regular bash array.
* Add COMFILE Pi config
* Add support for GPT partition tables
  ([MEN-2151](https://tracker.mender.io/browse/MEN-2151))
* Don't truncate output diskimage while writing partitions.
* configs: Added ubuntu x86-64 hdd defconfig
* Print improved error diagnostics before exiting on an error
* Add the state scripts version file.
* Ensure overlay files are owned by root.
* Setting of version variable now works if project added as a git submodule
  ([MEN-3475](https://tracker.mender.io/browse/MEN-3475))
* configs: Added generic x86-64 hdd defconfig
* Added automatic decompression of input images, so that the convert
  tool now accepts compressed input images in the formats: lzma, gzip, and zip.
  The images will also be recompressed to the input format automatically.
  ([MEN-3052](https://tracker.mender.io/browse/MEN-3052))
* add 'rootwait' to bootargs
* grubenv: Handle debug command prompt when running as EFI app.
* utilize regexp to dynamically set mender_grub_storage_device
* Remove kernel_devicetree from EFI path.
  This information is not used when loading via UEFI, instead it is
  queried directly from the UEFI provider.
* Fix 404 download errors when trying to run `docker-build`.
* Upgrade mender-client to 2.3.0b1 and mender-artifact to
  3.4.0b1.


## Mender 2.4.0

_Released 07.15.2020_

### Statistics

A total of 61736 lines added, 31536 removed (delta 30200)

| Developers with the most changesets | |
|---|---|
| Manuel Zedel | 279 (25.2%) |
| Fabio Tranchitella | 195 (17.6%) |
| Lluis Campos | 117 (10.6%) |
| Alf-Rune Siqveland | 96 (8.7%) |
| Ole Petter Orhagen | 95 (8.6%) |
| Marcin Chalczynski | 95 (8.6%) |
| Krzysztof Jaskiewicz | 75 (6.8%) |
| Peter Grzybowski | 74 (6.7%) |
| Kristian Amlie | 57 (5.1%) |
| Michael Clelland | 9 (0.8%) |

| Developers with the most changed lines | |
|---|---|
| Alf-Rune Siqveland | 14542 (20.0%) |
| Manuel Zedel | 12578 (17.3%) |
| Fabio Tranchitella | 12100 (16.7%) |
| Peter Grzybowski | 9860 (13.6%) |
| Marcin Chalczynski | 7617 (10.5%) |
| Lluis Campos | 6680 (9.2%) |
| Krzysztof Jaskiewicz | 5938 (8.2%) |
| Ole Petter Orhagen | 1876 (2.6%) |
| Kristian Amlie | 907 (1.2%) |
| Sam Baxter | 333 (0.5%) |

| Developers with the most lines removed | |
|---|---|
| Manuel Zedel | 2200 (7.0%) |
| Mirza Krak | 3 (0.0%) |

| Developers with the most signoffs (total 9) | |
|---|---|
| Manuel Zedel | 7 (77.8%) |
| Ole Petter Orhagen | 2 (22.2%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 928 (83.8%) |
| RnDity | 170 (15.4%) |
| iZotope | 5 (0.5%) |
| developer@lights0123.com | 1 (0.1%) |
| Wifx | 1 (0.1%) |
| andreas@fatal.se | 1 (0.1%) |
| aduskett@gmail.com | 1 (0.1%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 58695 (80.8%) |
| RnDity | 13555 (18.7%) |
| iZotope | 333 (0.5%) |
| developer@lights0123.com | 10 (0.0%) |
| aduskett@gmail.com | 6 (0.0%) |
| Wifx | 2 (0.0%) |
| andreas@fatal.se | 2 (0.0%) |

| Employers with the most signoffs (total 9) | |
|---|---|
| Northern.tech | 9 (100.0%) |

| Employers with the most hackers (total 17) | |
|---|---|
| Northern.tech | 10 (58.8%) |
| RnDity | 2 (11.8%) |
| iZotope | 1 (5.9%) |
| developer@lights0123.com | 1 (5.9%) |
| aduskett@gmail.com | 1 (5.9%) |
| Wifx | 1 (5.9%) |
| andreas@fatal.se | 1 (5.9%) |

### Changelogs

#### create-artifact-worker (1.0.1)

New changes in create-artifact-worker since 1.0.1b1:

* increase download and upload time-outs to 15 minutes
  ([MEN-3539](https://tracker.mender.io/browse/MEN-3539))
* handle multiple device types as comma-separated values
  ([MEN-3771](https://tracker.mender.io/browse/MEN-3771))

New changes in create-artifact-worker since 1.0.0:

* Limit the workflows create-artifact-worker can process

#### deployments (2.0.0)

New changes in deployments since 2.0.0b1:

* Remove mongodb write/read concerns, let the connection string set them

New changes in deployments since 1.9.0:

* New devices API endpoint POST /deployments/next
* Introduce new flow for creating deployments and selecting
  deployments for the devices. Device deployments are no longer created
  on deployment creation. Device deployments are being created when the
  devices are asking for the deployment.
* New method for listing IDs of devices being part of particular deployment.
* GET /deployments returns total count in the header
* add configuration option to enable/disable path-style AWS S3 URIs
  ([MEN-2499](https://tracker.mender.io/browse/MEN-2499))

#### deployments-enterprise (2.0.0)

New changes in deployments-enterprise since 2.0.0b1:

* Remove mongodb write/read concerns, let the connection string set them

New changes in deployments-enterprise since 1.9.0:

* api: New method for endpoint POST /device/deployments/next
* Support for artifacts provides/depends attributes
* New devices API endpoint POST /deployments/next
* api/http: introduce endpoint for creating dynamic deplyment
* Introduce new flow for creating deployments and selecting
  deployments for the devices. Device deployments are no longer created
  on deployment creation. Device deployments are being created when the
  devices are asking for the deployment.
* New method for listing IDs of devices being part of particular deployment.
* introduce new deployment status - scheduled
  Deployment status is "scheduled" when the deployment
  contains at least one phase, the first phase contains
  start_ts field and the deployment didn't start yet.
  Changes:
  - introduce new deployment status scheduled;
  - adjust status calculation;
* GET /deployments returns total count in the header
* add configuration option to enable/disable path-style AWS S3 URIs
  ([MEN-2499](https://tracker.mender.io/browse/MEN-2499))

#### deviceauth (2.3.0)

New changes in deviceauth since 2.2.0:

* Remove DEVICEAUTH_MAX_DEVICES_LIMIT_DEFAULT configuration option
* propagate-inventory-statuses command added

#### gui (2.4.0)

New changes in gui since 2.4.0b1:

* fixed an issue that caused unexpected deployment device states to crash the deployment report
* fixed settings availability in OS & onprem-enterprise deployments
* fixed check for group creation on mixed filter scopes & added short explanation

New changes in gui since 2.3.0:

* added artifact metadata to payload view if present
* made recent update times easier to read for devices & deployments
* prevented a redirect after deployment creation
* fixed an issue that would let the user list crash after user removal
* let mender plan be reflected in settings & billing page
* made scheduling deployments an enterprise plan only feature
* made phased deployments an enterprise plan only feature
* ensured deployment report is closed on abort to prevent UI crash
* made artifact dependencies available in expanded artifact details component
* fixed an issue that kept the header information from updating after login
* fixed an issue that prevented deployments from being possible
* reverted limit to 10 most popular device inventory attributes
* Docker HEALTHCHECK added
  ([MEN-2855](https://tracker.mender.io/browse/MEN-2855))
* refactored group creation dialog to support device additions
* added support for non-expandable device lists
  + improved rendering speed for device lists
* fixed an issue the broke the device auth state refresh on auth update
* added possibility to enable retries for deployments on deployment creation
* added filtering as you type based on client side store data
* added filtering possibility to pending & rejected device lists
* fixed a bug that prevented pagination in non-accepted device lists
* fixed page setting through custom entry in device lists
* allowed filters to be stored & using v2 inventory API
* allowed filtered to also use pagination
* improved device retrieval performance on group & filter changes
* prevented an error that could crash the ui when a device hasn't received status information
* added recently used device filters functionality
* fixed an issue that prevented device identity attributes from being populated
* fixed an error that prevented device lists from updating after authset dismissal
* fixed deb package installation instructions not containing package version
* improved deployments view to show scheduled deployments as well
* fixed an issue that could have prevented the deployment report from opening
* fixed a bug that prevented a group from being added after deletion
* fixed an issue that prevented group creation in short succession
* reduced device calls made in deployment report
  by reusing existing device information if possible
* Make GUI aware that we have a pre-converted image for Raspberry Pi 4.
* refactored deployment counting to use count header, reducing request load
* fixed an issue that might prevent OS users from changing their settings
* fixed identity attribute filtering on authorized devices
  ([MEN-3517](https://tracker.mender.io/browse/MEN-3517))
* enabled automatic selection on filter autocomplete
  ([MEN-3518](https://tracker.mender.io/browse/MEN-3518))
* ensured onboarding tooltip shows up after custom artifact is uploaded

#### integration (2.4.0)

New changes in integration since 2.4.0b1:

* Restore docker-compose.storage.s3.yml
* Upgrade create-artifact-worker to 1.0.1.
* Upgrade deployments to 2.0.0.
* Upgrade deployments-enterprise to 2.0.0.
* Upgrade deviceauth to 2.3.0.
* Upgrade gui to 2.4.0.
* Upgrade inventory to 2.0.0.
* Upgrade inventory-enterprise to 2.0.0.
* Upgrade mender to 2.3.0.
* Upgrade mender-api-gateway-docker to 2.2.0.
* Upgrade mender-artifact to 3.4.0.
* Upgrade mender-cli to 1.4.0.
* Upgrade tenantadm to 2.0.0.
* Upgrade useradm to 1.11.0.
* Upgrade useradm-enterprise to 1.11.0.
* Upgrade workflows to 1.1.0.
* Upgrade workflows-enterprise to 1.1.0.

New changes in integration since 2.3.0:

* Fix broken artifact creation in the UI.
  ([MEN-3166](https://tracker.mender.io/browse/MEN-3166))
* device-auth: call mender-workflows-server
  ([MEN-2963](https://tracker.mender.io/browse/MEN-2963))
* use workflows-server in tenantadm
  ([MEN-2965](https://tracker.mender.io/browse/MEN-2965))
* Update backend images to use version mender-master
  Introducing a new versioning schema, from this release on the Docker
  images for the backend repositories will be published in their
  corresponding registries following the Mender product version.
  This means tags `<service>:mender-<mender-version>` instead of the old
  tags `<service>:<service-version>`, which will eventually be deprecated.
  ([MEN-3466](https://tracker.mender.io/browse/MEN-3466))
* Upgrade create-artifact-worker to 1.0.1b1.
* Upgrade deployments to 2.0.0b1.
* Upgrade deployments-enterprise to 2.0.0b1.
* Upgrade deviceauth to 2.3.0b1.
* Upgrade gui to 2.4.0b1.
* Upgrade inventory to 2.0.0b1.
* Add inventory-enterprise 2.0.0b1.
* Upgrade mender to 2.3.0b1.
* Upgrade mender-api-gateway-docker to 2.2.0b1.
* Upgrade mender-artifact to 3.4.0b1.
* Upgrade mender-cli to 1.4.0b1.
* Upgrade tenantadm to 2.0.0b1.
* Upgrade useradm to 1.11.0b1.
* Upgrade useradm-enterprise to 1.11.0b1.
* Upgrade workflows to 1.1.0b1.
* Add workflows-enterprise 1.1.0b1.

#### inventory (2.0.0)

New changes in inventory since 1.7.0:

* New v2/filters/search endpoint.

#### inventory-enterprise (2.0.0)

* Introduced inventory-enterprise.

#### mender (2.3.0)

New changes in mender since 2.2.0:

* Fix "State transition loop detected" when retrying status update.
* Remove text/template dependency from the cli library reducing
  mender client binary size by approximately 20%
* Renamed systemd mender.service -> mender-client.service
  ([MEN-2948](https://tracker.mender.io/browse/MEN-2948))
* Fixes various logging nitpicks
* Deprecated the log-modules cli commandline flag
  ([MEN-3251](https://tracker.mender.io/browse/MEN-3251))
* Make the system logger respect the global log level
  ([MEN-3135](https://tracker.mender.io/browse/MEN-3135))
* Make the system logger write to the LOG_USER facility by default
* Fix Stat_t.Dev/Rdev type assumption
* Send Provides in the deployments API call
  ([MEN-2587](https://tracker.mender.io/browse/MEN-2587))
* Report function caller on all logs when loglevel=Debug

#### mender-api-gateway-docker (2.2.0)

New changes in mender-api-gateway-docker since 2.2.0b1:

* Return valid JSON documents as error pages' payloads
* Fix Artifact upload timeout bug

New changes in mender-api-gateway-docker since 2.1.0:

* RBAC: per device group restrictions support
  ([MEN-3240](https://tracker.mender.io/browse/MEN-3240))
* Increased timeouts to handle longer requests processing.

#### mender-artifact (3.4.0)

New changes in mender-artifact since 3.3.0:

* Accept suffix '.img' for mender-artifact modifiable images
* Fix: Update `rootfs_image_checksum` provide when repacking Artifact.
* Improved error message when an update-module is missing
  ([MEN-3007](https://tracker.mender.io/browse/MEN-3007))
* Bugfix: ignored signals no longer cause a signal-loop
  ([MEN-3276](https://tracker.mender.io/browse/MEN-3276))
* Add ability for artifact install to create directories
* Enabled autocompletion of mender-artifact sub-commands in bash & zsh
  Now, following the instructions in the Readme file, auto-completion of
  mender-artifact commands can be enabled by the user, such that writing:
  mender-artifact <TAB>
  results in:
  ```
  ➜ mender-artifact git:(bashexpansion) ✗ mender-artifact
  cat          -- cat [artifact|sdimg|uefiimg]:<filepath>
  cp           -- cp <src> <dst>
  dump         -- Dump contents from Artifacts
  help      h  -- Shows a list of commands or help for one command
  install      -- install -m <permissions> <hostfile> [artifact|sdimg|uefiimg]
  modify       -- Modifies image or artifact file.
  read         -- Reads artifact file.
  rm           -- rm [artifact|sdimg|uefiimg]:<filepath>
  sign         -- Signs existing artifact file.
  validate     -- Validates artifact file.
  write        -- Writes artifact file.
  ```
  and
  ```
  ➜ mender-artifact git:(bashexpansion) ✗ mender-artifact write
  help          h  -- Shows a list of commands or help for one command
  module-image     -- Writes Mender artifact for an update module
  rootfs-image     -- Writes Mender artifact containing rootfs image
  ```
  for sub-commands.
* The Artifact parser now fails when no 'device-type' is found in a payload.
* Disallow writes of UpdateModule Artifacts with no 'device-type' flag
* Return an error code if CLI read <artifact> fails
* Disallow parsing ArtifactV2 with empty device type field
* Display all CLI commands and flags sorted alplhabetically
* Missing a required CLI flag will now return an error
* Indexed the CLI commands by category
  This should make it easier to distinguish the large number of CLI commands
  depending on their intended usage.
  The two categories added are:
  * Artifact creation and validation
  * Artifact modification
  And should help to roughly set the commands apart depending on if they are
  intended to work with a standard Artifact, either creating it or validating it.
  The second category is intended for modification of already existing artifacts,
  such as adding or removing files, signing or modifying the Artifact name.
* Add(cli): Print the urfave/cli error on error

#### mender-cli (1.4.0)

New changes in mender-cli since 1.3.0:

* Support for two factor authentication token for login
  ([MEN-3176](https://tracker.mender.io/browse/MEN-3176))
* Change the name of the two-factor auth option.

#### tenantadm (2.0.0)

New changes in tenantadm since 2.0.0b1:

* Remove mongodb write/read concerns, let the connection string set them

New changes in tenantadm since 1.1.0:

* docs/internal: extend tenant object with "plan" field
* Use workflows instead of conductor for API orchestration
* New database schema (1.4.0), avoid the creation of multiple (inactive) organization with the same username
* Make create-org plan default to enterprise
* Make device limits configurable and set enterprise default: no limit
* Fix: Delete all tenants' users on tenant deletion

#### useradm (1.11.0)

New changes in useradm since 1.11.0b1:

* Remove mongodb write concern, let the connection string set them

New changes in useradm since 1.10.0:

* Routine version update to stay in sync with Enterprise.

#### useradm-enterprise (1.11.0)

New changes in useradm-enterprise since 1.11.0b1:

* Remove mongodb write concern, let the connection string set them

New changes in useradm-enterprise since 1.10.0:

* extend UserUpdate endpoint with array of roles
  ([MEN-3451](https://tracker.mender.io/browse/MEN-3451))
* Allow updating of roles via UpdateUser
  ([MEN-3452](https://tracker.mender.io/browse/MEN-3452))
* RBAC: per device group restrictions support
  ([MEN-3240](https://tracker.mender.io/browse/MEN-3240))
* set-roles command creates default roles
* Roles management API calls
  ([MEN-3447](https://tracker.mender.io/browse/MEN-3447))

#### workflows (1.1.0)

New changes in workflows since 1.0.0:

* decommision and provision device workflows
  ([MEN-2963](https://tracker.mender.io/browse/MEN-2963))
* replace all values in processJobString
  ([MEN-2965](https://tracker.mender.io/browse/MEN-2965))
* list-jobs comand, extra logging and go fmt

#### workflows-enterprise (1.1.0)

* Introduced workflows-enterprise.


## mender-binary-delta 1.1.0

_Released 07.15.2020_

#### mender-binary-delta (1.1.0)

New changes in mender-binary-delta since 1.0.1:

* Make the CLI artifact-name argument optional
  ([MEN-2642](https://tracker.mender.io/browse/MEN-2642))
* Now the binary delta tools supports depends and provides
  ([MEN-2642](https://tracker.mender.io/browse/MEN-2642))
* Add the ability to write transitional artifacts
  ([MEN-2948](https://tracker.mender.io/browse/MEN-2948))


## meta-mender zeus-v2020.06

_Released 06.12.2020_

### Statistics

A total of 7169 lines added, 4936 removed (delta 2233)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 79 (41.4%) |
| Ole Petter Orhagen | 33 (17.3%) |
| Lluis Campos | 22 (11.5%) |
| Drew Moseley | 19 (9.9%) |
| Marcin Pasinski | 10 (5.2%) |
| Mirza Krak | 9 (4.7%) |
| Alf-Rune Siqveland | 4 (2.1%) |
| Joerg Hofrichter | 3 (1.6%) |
| Marek Belisko | 2 (1.0%) |
| Gaurav Kalra | 2 (1.0%) |

| Developers with the most changed lines | |
|---|---|
| Kristian Amlie | 3006 (33.1%) |
| Ole Petter Orhagen | 2699 (29.7%) |
| Joerg Hofrichter | 1522 (16.8%) |
| Marcin Pasinski | 1016 (11.2%) |
| Drew Moseley | 275 (3.0%) |
| Mirza Krak | 244 (2.7%) |
| Marek Belisko | 163 (1.8%) |
| Lluis Campos | 101 (1.1%) |
| Alf-Rune Siqveland | 19 (0.2%) |
| Joris Offouga | 16 (0.2%) |

| Developers with the most lines removed | |
|---|---|
| Kristian Amlie | 839 (17.0%) |
| Joris Offouga | 16 (0.3%) |

| Developers with the most signoffs (total 4) | |
|---|---|
| Maciej Borzecki | 2 (50.0%) |
| Kristian Amlie | 1 (25.0%) |
| Drew Moseley | 1 (25.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 176 (92.1%) |
| National Instruments | 3 (1.6%) |
| walkbase | 2 (1.0%) |
| Packet Power LLC | 2 (1.0%) |
| open-nandra | 2 (1.0%) |
| BayLibre | 1 (0.5%) |
| alex.misch901@gmail.com | 1 (0.5%) |
| guillaume.kh.alt@gmail.com | 1 (0.5%) |
| SM Instruments Inc. | 1 (0.5%) |
| offougajoris@gmail.com | 1 (0.5%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 7360 (81.1%) |
| National Instruments | 1522 (16.8%) |
| open-nandra | 163 (1.8%) |
| offougajoris@gmail.com | 16 (0.2%) |
| walkbase | 8 (0.1%) |
| Packet Power LLC | 2 (0.0%) |
| BayLibre | 1 (0.0%) |
| alex.misch901@gmail.com | 1 (0.0%) |
| guillaume.kh.alt@gmail.com | 1 (0.0%) |
| SM Instruments Inc. | 1 (0.0%) |

| Employers with the most signoffs (total 4) | |
|---|---|
| Northern.tech | 2 (50.0%) |
| RnDity | 2 (50.0%) |

| Employers with the most hackers (total 17) | |
|---|---|
| Northern.tech | 7 (41.2%) |
| National Instruments | 1 (5.9%) |
| open-nandra | 1 (5.9%) |
| offougajoris@gmail.com | 1 (5.9%) |
| walkbase | 1 (5.9%) |
| Packet Power LLC | 1 (5.9%) |
| BayLibre | 1 (5.9%) |
| alex.misch901@gmail.com | 1 (5.9%) |
| guillaume.kh.alt@gmail.com | 1 (5.9%) |
| SM Instruments Inc. | 1 (5.9%) |


### Changelogs

#### meta-mender (zeus-v2020.06)

New changes in meta-mender since warrior-v2020.06:

* Removes the tests covering Mender-Artifact version 1.
  ([MEN-2156](https://tracker.mender.io/browse/MEN-2156))
* Add mender 2.1.1 and mender-artifact 3.2.0b1 recipes.
* Update recipe for mender-binary-delta beta release v1.0.0b1
* Remove mender-2.0.x and older, and mender-artifact 3.0.x
  and older.
* mender-setup: do not add systemd options to fstab without mender-systemd
* Enable Artifact Depends and Provides for Yocto builds
  Enables the ability to set:
  * Artifact Depends
  * Artifact Provides
  * Artifact Name Depends
  * Artifact Provides Group
  * Artifact Depends Groups
  In the Mender Artifact from the Yocto build,
  through the build variables:
  MENDER_ARTIFACT_NAME_DEPENDS -- List of names
  MENDER_ARTIFACT_PROVIDES -- Key:Value
  MENDER_ARTIFACT_DEPENDS -- Key:Value
  MENDER_ARTIFACT_PROVIDES_GROUP -- Name
  MENDER_ARTIFACT_DEPENDS_GROUPS -- List of names
  ([MEN-1670](https://tracker.mender.io/browse/MEN-1670))
* Add mender-artifact 3.2.0 and remove beta.
* Upgrade client acceptance tests to Python3
* Update recipe for mender-binary-delta final release v1.0.0
* mender-setup: allow setting fstab options for the boot partition
* mender-image: Add DEPENDS to include WKS_FILE_DEPENDS.
* Update uboot_auto_patch script to be compatible with U-Boot 2019.10
* Add mender 2.1.2 recipe
* Add mender-artifact 3.1.1 recipe
* Add mender-artifact 3.2.1 recipe
* Add mender-binar-delta 1.0.1 recipe
* Add 'datatar' as an image type.
* Upgrade to new grub-mender-grubenv.
* Remove outdated grub-mender-grubenv_1.3.0 recipe.
* systemd-boot: Respect MENDER_BOOT_PART_MOUNT_LOCATION
* grub-efi: Respect MENDER_BOOT_PART_MOUNT_LOCATION
* mender-grub: Set EFI_PROVIDER to grub-efi.
* mender-helpers: Error out if copying different files to boot part.
* demo: Support systemd Predictable Network Names.
* grub-mender-grubenv: Fix broken debug-log PACKAGECONFIG.
* mender-part-images: Added handling for extra partitions
* mender-artifact: make it available in SDK
* remove stray '-' in IMAGE_NAME
* Fix failure in boot log when `MENDER_EXTRA_PARTS` is used.
  `mender-growfs-data` and `MENDER_EXTRA_PARTS` are mutually exclusive,
  so set the default of `mender-growfs-data` to off if
  `MENDER_EXTRA_PARTS` is being used.
* Improve warning when multiple DTB files are in KERNEL_DEVICETREE
* In demo mode, put demo certificate in same directory as Debian package.
  ([MEN-3048](https://tracker.mender.io/browse/MEN-3048))
* Add mender 2.2.0b1 recipe
* Add mender-artifact 3.3.0b1 recipe
* mender: Add signature/secure-boot support.
* Remove mender-artifact 3.1 recipes (EOL).
* Add MENDER_DTB_NAME_FORCE to mender-vars.json to avoid unrecognized variable warning
* rpi: fix rootfs cmdline trailing space
* mender-helper: Added handling for MENDER_EXTRA_PARTS_FSTAB
* Improve dependency logic to not require U-Boot unconditionally on ARM.
  This will help when not using `mender-grub`, and instead using
  Barebox, for example.
* Make sure partitions are marked for fsck'ing by default.
* Follow e2fsprogs version bump from 1.44 to 1.45.
* Follow systemd feature rename from time-epoch to set-time-epoch.
* systemd-conf: Fix missing FILES section which is mandatory on zeus.
* Work around missing LSB support in zeus.
  This is a very intrusive change, which creates the `/lib64` symlink on
  the root filesystem for 64-bit systems. This symlink is normally
  missing when building with Yocto, but was provided by the LSB package
  previously. The directory is necessary to remain compatible with
  software built outside of Yocto. The Mender demo artifact, as well as
  the binary delta update module are examples of such components.
  If the link turns out to conflict with another package, it should be
  possible to work around the problem by adding this to the other
  package, either in the original `.bb` file or a `.bbappend` file:
  ```
  RPROVIDES_${PN} += "lsb-ld"
  ```
* Enable CONFIG_EFI_STUB on kernels when booting with UEFI on ARM.
* Add mender 2.2.0 recipe and remove beta
* Add mender-artifact 3.3.0 recipe and remove beta
* Add mender 2.1.3 recipe
* raspberrypi4: update U-Boot patches to apply to 2019.07 version
  ([MEN-3262](https://tracker.mender.io/browse/MEN-3262))
* Renamed mender -> mender-client
  This renaming was done to conform with the new naming introduced. This helps
  seperate Mender (the product), from Mender-client, which is a part of the
  aforementioned product.
  The renaming is due in parts:
  * The 'mender.service' systemd recipe is now named 'mender-client.service'
  * The bitbake recipes are now renamed from 'mender%.bb' to 'mender-client%.bb'
  * The Mender feature 'mender-install' is now 'mender-client-install'
  * The mender directory holding the mender-client recipe is also renamed 'mender-client'
* Upgrade to U-Boot 2020.01 and GRUB 2.04 to fix Beaglebone support.
* Updated the LIC_FILES_CHECKSUM after removing dependencies
  ([MEN-3251](https://tracker.mender.io/browse/MEN-3251))
* mender-grub: Dynamically determine mender_grub_storage_device.
* mender-grub: Add regexp module.
* Deprecate MENDER_GRUB_STORAGE_DEVICE variable.
* raspberrypi: add state script to update boot firmware
  Raspberry Pi boards have a set of boot firmware files that are
  located on the vfat boot part, and these files are not updated
  when you perform an update of the root filesystem.
  Occasionally there will be changes to the Raspberry Pi software stack
  that requires that these files are update. Typically there is something
  in the Linux kernel that requires something that is in the boot
  firmware. This means that to update the Linux kernel you must also
  update the boot firmware files.
  Above is really sub-optimal design of the Raspberry Pi boards but a
  limitation that we must live with.
  Note that the DTB files are also part of "boot firmware" and included in
  the state script update.
  The provided state-script can be enabled by adding the following to e.g
  local.conf:
      INHERIT += "rpi-update-firmware"
  The ArtifactInstall_Leave_50 script can be overriden to customize what
  files to update, e.g only DTB files. By default all files on the boot
  part will be updated including config.txt and cmdline.txt.
  NOTE! Updating the boot firmware files can not be done atomically and the
  files are not roll-backed even though an rootfs rollback is performed. Conclusion,
  this is an risky operating which could brick your device.
* Fix infinite loop which would eat all available memory
  on the build host, when using U-Boot v2020.01 or later together with
  the auto-patcher.
  ([MEN-3265](https://tracker.mender.io/browse/MEN-3265))
* Updated the LIC_FILES_CHECKSUM after removing dependencies
  ([MEN-3251](https://tracker.mender.io/browse/MEN-3251))
* mender: Add sanity check for partuuid and uboot.
* grubenv: Handle debug command prompt when running as EFI
  app.
* write GPT partition table before resize of data part
  ([MEN-3366](https://tracker.mender.io/browse/MEN-3366))
* raspberrypi: busybox compatibility for boot firmware state script
* grub: Move dynamic storage handling into grub-mender-grubenv repository.
* U-Boot versions from v2020.01 onwards have moved several C
  code defines into Kconfig, which may require changes in board specific
  patches. Specifically, `CONFIG_ENV_SIZE`, `CONFIG_ENV_OFFSET` and
  `CONFIG_ENV_OFFSET_REDUND` now need to be defined in the board's
  `defconfig` file. In addition, the redundant environment now need to
  be specifically enabled, using the new switch,
  `CONFIG_SYS_REDUNAND_ENVIRONMENT`. If you are using
  `MENDER_UBOOT_AUTO_CONFIGURE=1`, then this is handled automatically,
  but if not you will need to add this to your board's `defconfig` file:
  ```
  CONFIG_SYS_REDUNAND_ENVIRONMENT=y
  CONFIG_ENV_SIZE=0x20000
  CONFIG_ENV_OFFSET=0x800000
  CONFIG_ENV_OFFSET_REDUND=0x1000000
  ```
  Note that the values may differ from the values you actually need,
  these are just the defaults from the meta-mender Yocto
  layer. `CONFIG_ENV_SIZE` need to match the `MENDER_ENV_SIZE` Bitbake
  variable, and `CONFIG_ENV_OFFSET` and `CONFIG_ENV_OFFSET_REDUND`
  should (usually) be 1x and 2x the `MENDER_PARTITION_ALIGNMENT`
  variable. If the values are not as expected, then you will get an
  error during the compile stage.
* Fix OOM issue on the build host if certain configuration
  options are missing from the defconfig file.
  ([MEN-3476](https://tracker.mender.io/browse/MEN-3476))
* grub-mender-grubenv: Remove kernel_devicetree.
  The only way to use GRUB 2.04 on ARM is via UEFI, and the
  kernel_devicetree information is not used when loading via UEFI,
  instead it is queried directly from the UEFI provider.
* Make sure that mender-grow-data.service only runs once.
* Boot no longer blocks while the data part is resized, and
  instead this is a background process.
* Add OpenSSL as dependency for Git versions of the Mender client.
* Fix U-Boot auto-patcher sometimes adding two conflicting
  options to the defconfig file.
  ([MEN-3514](https://tracker.mender.io/browse/MEN-3514))
* Add mender-client_2.3.0b1 and mender-artifact_3.4.0b1 recipes.
  To use the Beta recipes, add this to `local.conf`:
  ```
  PREFERRED_VERSION_pn-mender-client = "2.3.0b1"
  PREFERRED_VERSION_pn-mender-artifact = "3.4.0b1"
  PREFERRED_VERSION_pn-mender-artifact-native = "3.4.0b1"
  ```
* Add mender-binary-delta_1.1.0b1 recipe.
  To use the beta, add this to `local.conf`:
  ```
  PREFERRED_VERSION_pn-mender-binary-delta = "1.1.0b1"
  ```
* Disable `64bit` ext4 filesystem feature.
  ([MEN-3513](https://tracker.mender.io/browse/MEN-3513))
* Remove mender-client < 2.2, and mender-artifact < 3.3 recipes.


## meta-mender warrior-v2020.06

_Released 06.08.2020_

### Statistics

A total of 166 lines added, 163 removed (delta 3)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 6 (35.3%) |
| Ole Petter Orhagen | 5 (29.4%) |
| Mirza Krak | 4 (23.5%) |
| Drew Moseley | 2 (11.8%) |

| Developers with the most changed lines | |
|---|---|
| Mirza Krak | 123 (48.2%) |
| Kristian Amlie | 121 (47.5%) |
| Drew Moseley | 6 (2.4%) |
| Ole Petter Orhagen | 5 (2.0%) |

| Developers with the most lines removed | |
|---|---|
| Kristian Amlie | 83 (50.9%) |

| Developers with the most signoffs (total 1) | |
|---|---|
| Lluis Campos | 1 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 17 (100.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 255 (100.0%) |

| Employers with the most signoffs (total 1) | |
|---|---|
| Northern.tech | 1 (100.0%) |

| Employers with the most hackers (total 4) | |
|---|---|
| Northern.tech | 4 (100.0%) |

### Changelogs

#### meta-mender (warrior-v2020.06)

New changes in meta-mender since warrior-v2020.05:

* Make sure that mender-grow-data.service only runs once.
* Boot no longer blocks while the data part is resized, and
  instead this is a background process.
* Add OpenSSL as dependency for Git versions of the Mender client.
* Add mender_2.3.0b1 and mender-artifact_3.4.0b1 recipes.
  To use the Beta recipes, add this to `local.conf`:
  ```
  PREFERRED_VERSION_pn-mender = "2.3.0b1"
  PREFERRED_VERSION_pn-mender-artifact = "3.4.0b1"
  PREFERRED_VERSION_pn-mender-artifact-native = "3.4.0b1"
  ```
* Add mender-binary-delta_1.1.0b1 recipe.
  To use the beta, add this to `local.conf`:
  ```
  PREFERRED_VERSION_pn-mender-binary-delta = "1.1.0b1"
  ```


## mender-convert 2.0.1

_Released 05.28.2020_

### Statistics

A total of 49 lines added, 36 removed (delta 13)

| Developers with the most changesets | |
|---|---|
| Nate Baker | 3 (42.9%) |
| Kristian Amlie | 2 (28.6%) |
| Lluis Campos | 1 (14.3%) |
| Mirza Krak | 1 (14.3%) |

| Developers with the most changed lines | |
|---|---|
| Nate Baker | 30 (42.3%) |
| Mirza Krak | 25 (35.2%) |
| Kristian Amlie | 14 (19.7%) |
| Lluis Campos | 2 (2.8%) |

| Developers with the most lines removed | |
|---|---|
| Mirza Krak | 22 (61.1%) |

| Developers with the most signoffs (total 3) | |
|---|---|
| Mirza Krak | 3 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 4 (57.1%) |
| bakern@gmail.com | 3 (42.9%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 41 (57.7%) |
| bakern@gmail.com | 30 (42.3%) |

| Employers with the most signoffs (total 3) | |
|---|---|
| Northern.tech | 3 (100.0%) |

| Employers with the most hackers (total 4) | |
|---|---|
| Northern.tech | 3 (75.0%) |
| bakern@gmail.com | 1 (25.0%) |

### Changelogs

#### mender-convert (2.0.1)

New changes in mender-convert since 2.0.0:

* Don't truncate output diskimage while writing partitions.
* Fix 404 download errors when trying to run `docker-build`.


## meta-mender warrior-v2020.05

_Released 05.05.2020_

### Statistics

A total of 7 lines added, 7 removed (delta 0)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 3 (42.9%) |
| Ole Petter Orhagen | 2 (28.6%) |
| Mirza Krak | 1 (14.3%) |
| Guillaume Khayat | 1 (14.3%) |

| Developers with the most changed lines | |
|---|---|
| Kristian Amlie | 4 (50.0%) |
| Ole Petter Orhagen | 2 (25.0%) |
| Mirza Krak | 1 (12.5%) |
| Guillaume Khayat | 1 (12.5%) |

| Developers with the most lines removed | |
|---|---|
| Kristian Amlie | 1 (14.3%) |

| Developers with the most signoffs (total 2) | |
|---|---|
| Kristian Amlie | 2 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 6 (85.7%) |
| guillaume.kh.alt@gmail.com | 1 (14.3%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 7 (87.5%) |
| guillaume.kh.alt@gmail.com | 1 (12.5%) |

| Employers with the most signoffs (total 2) | |
|---|---|
| Northern.tech | 2 (100.0%) |

| Employers with the most hackers (total 4) | |
|---|---|
| Northern.tech | 3 (75.0%) |
| guillaume.kh.alt@gmail.com | 1 (25.0%) |

### Changelogs

#### meta-mender (warrior-v2020.05)

New changes in meta-mender since warrior-v2020.04:

* grubenv: Handle debug command prompt when running as EFI
  app.
* raspberrypi: busybox compatibility for boot firmware state script
* grub: Move dynamic storage handling into grub-mender-grubenv repository.
* write GPT partition table before resize of data part
  ([MEN-3366](https://tracker.mender.io/browse/MEN-3366))


## meta-mender warrior-v2020.04

_Released 04.08.2020_

### Statistics

A total of 206 lines added, 47 removed (delta 159)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 2 (28.6%) |
| Mirza Krak | 1 (14.3%) |
| Lluis Campos | 1 (14.3%) |
| Ole Petter Orhagen | 1 (14.3%) |
| Alf-Rune Siqveland | 1 (14.3%) |
| Drew Moseley | 1 (14.3%) |

| Developers with the most changed lines | |
|---|---|
| Kristian Amlie | 115 (47.7%) |
| Mirza Krak | 70 (29.0%) |
| Drew Moseley | 42 (17.4%) |
| Lluis Campos | 7 (2.9%) |
| Alf-Rune Siqveland | 6 (2.5%) |
| Ole Petter Orhagen | 1 (0.4%) |

| Developers with the most lines removed | |
|---|---|
| Drew Moseley | 35 (74.5%) |

| Developers with the most signoffs (total 1) | |
|---|---|
| Kristian Amlie | 1 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 7 (100.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 241 (100.0%) |

| Employers with the most signoffs (total 1) | |
|---|---|
| Northern.tech | 1 (100.0%) |

| Employers with the most hackers (total 6) | |
|---|---|
| Northern.tech | 6 (100.0%) |

### Changelogs

#### meta-mender (warrior-v2020.04)

New changes in meta-mender since warrior-v2020.03:

* mender-grub: Dynamically determine mender_grub_storage_device.
* mender-grub: Add regexp module.
* Deprecate MENDER_GRUB_STORAGE_DEVICE variable.
* Updated the LIC_FILES_CHECKSUM after removing dependencies
  ([MEN-3251](https://tracker.mender.io/browse/MEN-3251))
* raspberrypi: add state script to update boot firmware
  Raspberry Pi boards have a set of boot firmware files that are
  located on the vfat boot part, and these files are not updated
  when you perform an update of the root filesystem.
  Occasionally there will be changes to the Raspberry Pi software stack
  that requires that these files are update. Typically there is something
  in the Linux kernel that requires something that is in the boot
  firmware. This means that to update the Linux kernel you must also
  update the boot firmware files.
  Above is really sub-optimal design of the Raspberry Pi boards but a
  limitation that we must live with.
  Note that the DTB files are also part of "boot firmware" and included in
  the state script update.
  The provided state-script can be enabled by adding the following to e.g
  local.conf:
      INHERIT += "rpi-update-firmware"
  The ArtifactInstall_Leave_50 script can be overriden to customize what
  files to update, e.g only DTB files. By default all files on the boot
  part will be updated including config.txt and cmdline.txt.
  NOTE! Updating the boot firmware files can not be done atomically and the
  files are not roll-backed even though an rootfs rollback is performed. Conclusion,
  this is an risky operating which could brick your device.


## meta-mender warrior-v2020.03

_Released 03.09.2020_

### Statistics

A total of 182 lines added, 157 removed (delta 25)

| Developers with the most changesets | |
|---|---|
| Drew Moseley | 5 (38.5%) |
| Kristian Amlie | 4 (30.8%) |
| Lluis Campos | 3 (23.1%) |
| Joris Offouga | 1 (7.7%) |

| Developers with the most changed lines | |
|---|---|
| Drew Moseley | 244 (75.5%) |
| Lluis Campos | 43 (13.3%) |
| Kristian Amlie | 20 (6.2%) |
| Joris Offouga | 16 (5.0%) |

| Developers with the most lines removed | |
|---|---|
| Lluis Campos | 23 (14.6%) |
| Joris Offouga | 16 (10.2%) |
| Kristian Amlie | 4 (2.5%) |

| Developers with the most signoffs (total 1) | |
|---|---|
| Kristian Amlie | 1 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 12 (92.3%) |
| offougajoris@gmail.com | 1 (7.7%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 307 (95.0%) |
| offougajoris@gmail.com | 16 (5.0%) |

| Employers with the most signoffs (total 1) | |
|---|---|
| Northern.tech | 1 (100.0%) |

| Employers with the most hackers (total 4) | |
|---|---|
| Northern.tech | 3 (75.0%) |
| offougajoris@gmail.com | 1 (25.0%) |

### Changelogs

#### meta-mender (warrior-v2020.03)

New changes in meta-mender since warrior-v2020.02.2:

* systemd: move network configurations to systemd-conf
* Add 'datatar' as an image type.
* Remove outdated grub-mender-grubenv_1.3.0 recipe.
* Upgrade to new grub-mender-grubenv.
* mender: Add signature/secure-boot support.
* Add mender 2.2.0 recipe and remove beta
* Add mender-artifact 3.3.0 recipe and remove beta
* Add mender 2.1.3 recipe
* Improve dependency logic to not require U-Boot unconditionally on ARM.
  This will help when not using `mender-grub`, and instead using
  Barebox, for example.


## mender-convert 2.0.0

_Released 03.06.2020_

### Statistics

A total of 3745 lines added, 4597 removed (delta -852)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 34 (30.4%) |
| Lluis Campos | 25 (22.3%) |
| Ole Petter Orhagen | 22 (19.6%) |
| Mirza Krak | 19 (17.0%) |
| Drew Moseley | 10 (8.9%) |
| Fabio Tranchitella | 1 (0.9%) |
| Alf-Rune Siqveland | 1 (0.9%) |

| Developers with the most changed lines | |
|---|---|
| Mirza Krak | 6195 (81.8%) |
| Kristian Amlie | 442 (5.8%) |
| Ole Petter Orhagen | 410 (5.4%) |
| Lluis Campos | 237 (3.1%) |
| Drew Moseley | 168 (2.2%) |
| Alf-Rune Siqveland | 103 (1.4%) |
| Fabio Tranchitella | 21 (0.3%) |

| Developers with the most lines removed | |
|---|---|
| Mirza Krak | 1369 (29.8%) |

| Developers with the most signoffs (total 1) | |
|---|---|
| Kristian Amlie | 1 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 112 (100.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 7576 (100.0%) |

| Employers with the most signoffs (total 1) | |
|---|---|
| Northern.tech | 1 (100.0%) |

| Employers with the most hackers (total 7) | |
|---|---|
| Northern.tech | 7 (100.0%) |

### Changelogs

#### mender-convert (2.0.0)

New changes in mender-convert since 2.0.0b1:

* Upgrade to GRUB 2.04.
* Add detection of problematic versions of U-Boot and kernel.
  ([MEN-2404](https://tracker.mender.io/browse/MEN-2404))
* Added hooks to Mender convert
  This extends the current functionality of the platform_ function
  functionality into using hooks, so that each modification step can be called
  from multiple configuration files.
  The valid hooks are:
   * PLATFORM_MODIFY_HOOKS
   * PLATFORM_PACKAGE_HOOKS
   * USER_LOCAL_MODIFY_HOOKS
  and can be appended to as a regular bash array.
* Use consistent compression and archive naming.
* Update to Mender 2.3.0 components
* Added color to the terminal log messages

New changes in mender-convert since 1.2.2:

* remove mender-convert (version 1)
* add mender-convert (version 2)
  ([MEN-2608](https://tracker.mender.io/browse/MEN-2608))
* Allow mender_local_config in current directory to be ignored by git.
* bbb: Add support for eMMC as boot media.
* configs: Support multiple config files on command line.
* Fix "yellow" HDMI output on Raspbian Buster
  ([MEN-2685](https://tracker.mender.io/browse/MEN-2685))
* scripts: Refactor to support different Mender server options.
* Add support for Ubuntu Server images on Raspberry Pi 3
* README: Clarify server types as alternatives.
* modify: Add an extra function user_local_modify for end users to populate.
* mender: Rename mender.service to mender-client.service
* Add Raspberry Pi 0 WiFi support
  ([MEN-2788](https://tracker.mender.io/browse/MEN-2788))
* Implement MENDER_COPY_BOOT_GAP feature
  ([MEN-2784](https://tracker.mender.io/browse/MEN-2784))
* Raspberry Pi 3: Update U-Boot to 2019.01
* Raspberry Pi 0 WiFi: Update U-Boot to 2019.01
* Raspberry Pi: Add U-Boot version to image boot partition
* Add support for Raspberry Pi 4 Model B
* Make sure artifacts are owned by same user as the launch directory.
* Changed the calculation of occupied space on the rootfs
  partition to a more accurate formula.
* Add support for controlling rootfs size with `IMAGE_*` variables.
  * `IMAGE_ROOTFS_SIZE` - The base size of the rootfs. The other two
    variables modify this value
  * `IMAGE_ROOTFS_EXTRA_SIZE` - The amount of free space to add to the
    base size of the rootfs
  * `IMAGE_OVERHEAD_FACTOR` - Factor determining the amount of free
    space to add to the base size of the rootfs
  The final size will be the largest of the two calculations. Please see
  the `mender_convert_config` file comments for more information.
* Add lzma compression option for `MENDER_COMPRESS_DISK_IMAGE`.
* Bump mender-artifact version to 3.2.1.
* Turn off default ext4 filesystem feature `metadata_csum`.
  This feature is not supported by tools on Ubuntu 16.04.
* Change the output filename naming scheme to mender.img
  ([MEN-3051](https://tracker.mender.io/browse/MEN-3051))
* mender-convert: Rename variables for consistency with meta-mender.
* Fix certain kernels hanging on boot. In particular, recent
  versions of Debian for Beaglebone was affected, but several other
  boards using UEFI may also have been affected.
* Make device_type specific to each Raspberry Pi model.
  ([MEN-3165](https://tracker.mender.io/browse/MEN-3165))
* Switch to Mender 2.3.0b1 components.


## Mender 2.3.0

_Released 03.05.2020_

### Statistics

A total of 59423 lines added, 38146 removed (delta 21277)

| Developers with the most changesets | |
|---|---|
| Manuel Zedel | 244 (27.4%) |
| Lluis Campos | 198 (22.2%) |
| Alf-Rune Siqveland | 78 (8.8%) |
| Ole Petter Orhagen | 74 (8.3%) |
| Fabio Tranchitella | 68 (7.6%) |
| Marcin Chalczynski | 65 (7.3%) |
| Kristian Amlie | 63 (7.1%) |
| Krzysztof Jaskiewicz | 48 (5.4%) |
| Peter Grzybowski | 29 (3.3%) |
| Ole Herman Schumacher Elgesem | 7 (0.8%) |

| Developers with the most changed lines | |
|---|---|
| Manuel Zedel | 16299 (23.8%) |
| Alf-Rune Siqveland | 14970 (21.8%) |
| Fabio Tranchitella | 10359 (15.1%) |
| Lluis Campos | 6985 (10.2%) |
| Ole Petter Orhagen | 5027 (7.3%) |
| Kristian Amlie | 4122 (6.0%) |
| Marcin Chalczynski | 4013 (5.9%) |
| Krzysztof Jaskiewicz | 3884 (5.7%) |
| Peter Grzybowski | 1785 (2.6%) |
| Eystein Måløy Stenberg | 425 (0.6%) |

| Developers with the most lines removed | |
|---|---|
| Lluis Campos | 2513 (6.6%) |
| Kristian Amlie | 771 (2.0%) |
| Eystein Måløy Stenberg | 419 (1.1%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 769 (86.3%) |
| RnDity | 114 (12.8%) |
| f.breuer94@gmail.com | 2 (0.2%) |
| prashanthjbabu@gmail.com | 2 (0.2%) |
| risca@dalakolonin.se | 2 (0.2%) |
| sam.vr.lewis@gmail.com | 1 (0.1%) |
| open-nandra | 1 (0.1%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 60220 (87.9%) |
| RnDity | 7962 (11.6%) |
| f.breuer94@gmail.com | 323 (0.5%) |
| prashanthjbabu@gmail.com | 12 (0.0%) |
| sam.vr.lewis@gmail.com | 10 (0.0%) |
| risca@dalakolonin.se | 4 (0.0%) |
| open-nandra | 1 (0.0%) |

| Employers with the most hackers (total 19) | |
|---|---|
| Northern.tech | 11 (57.9%) |
| RnDity | 3 (15.8%) |
| f.breuer94@gmail.com | 1 (5.3%) |
| prashanthjbabu@gmail.com | 1 (5.3%) |
| sam.vr.lewis@gmail.com | 1 (5.3%) |
| risca@dalakolonin.se | 1 (5.3%) |
| open-nandra | 1 (5.3%) |

### Changelogs

#### deployments (1.9.0)

New changes in deployments since 1.8.1:

* run migrations on startup like other services do
  ([MC-1144](https://tracker.mender.io/browse/MC-1144))
* fix device count for get deployment id
* Set a timeout (5 seconds) for CreateBucket at start up
* index deployments database
  ([MEN-2019](https://tracker.mender.io/browse/MEN-2019))
* store: Migrate to official MongoDB driver

#### deployments-enterprise (1.9.0)

New changes in deployments-enterprise since 1.8.1:

* Disallow empty batches in phased rollouts
  Previously there was a possibility to end up with an empty batch, due
  to the formula used in the calculation for the number of devices which
  is based on extracting a percentage number of devices from the total. Thus
  if the total is so small, that a percentage below some number rounds to zero,
  the batch would be empty. Now that same input will return an error.
  ([MEN-2810](https://tracker.mender.io/browse/MEN-2810))
* FIX: Concurrent updates to phase device counter are made atomic
* run migrations on startup like other services do
  ([MC-1144](https://tracker.mender.io/browse/MC-1144))
* fix device count for get deployment id
* Migration to official mongodb driver
* Set a timeout (5 seconds) for CreateBucket at start up
* index deployments database
  ([MEN-2019](https://tracker.mender.io/browse/MEN-2019))

#### deviceauth (2.2.0)

New changes in deviceauth since 2.1.0:

* Return device id to a POST /devauth/devices call
  ([MEN-2605](https://tracker.mender.io/browse/MEN-2605))
* additional mongodb index added
* store/mongo: migrate to official mongodb driver

#### gui (2.3.0)

New changes in gui since 2.3.0b1:

* ensured deployment report is closed on abort to prevent UI crash

New changes in gui since 2.2.1:

* fixed empty userData on edit, causing blank ui fields in settings & header
* fixed persistence of helptip dismissal during onboarding
* fixed regression: filtered on device-type before deployment
* ensured device groups are sorted when retrieved from backend
* added device status inidicator in devicelist
* added billing information page to display current & past billing status
* included inprogress deployments in progress visualisation
* fixed device filtering by url parameter
* fixed deployment device list pagination & device id display
* made deployments refresh more frequently if appropriate
* made selected device id show up when settings dialog is opened
* fixed an issue that caused the proper error to be hidden when an artifact could not be changed
* adjusted deployment report to improve release name readability
* fixed an issue that broke the deployments list alignment
* made releaseslist sortable
* enabled release filtering by name, description & device types
* added additional onboarding steps to ease update artifact generation
* fixed an issue that prevented the staying logged in functionality from working
* prevented a redirect after deployment creation

#### integration (2.3.0)

New changes in integration since 2.3.0b1:

* Fix broken artifact creation in the UI.
  ([MEN-3166](https://tracker.mender.io/browse/MEN-3166))
* Upgrade create-artifact-worker to 1.0.0.
* Upgrade deployments to 1.9.0.
* Upgrade deployments-enterprise to 1.9.0.
* Upgrade deviceauth to 2.2.0.
* Upgrade gui to 2.3.0.
* Upgrade inventory to 1.7.0.
* Upgrade mender to 2.2.0.
* Upgrade mender-api-gateway-docker to 2.1.0.
* Upgrade mender-artifact to 3.3.0.
* Upgrade mender-cli to 1.3.0.
* Upgrade mender-conductor to 1.6.0.
* Upgrade mender-conductor-enterprise to 1.6.0.
* Upgrade tenantadm to 1.1.0.
* Upgrade useradm to 1.10.0.
* Upgrade useradm-enterprise to 1.10.0.
* Upgrade workflows to 1.0.0.

New changes in integration since 2.2.1:

* Fix issue when demo script exists abruptly on user request
  for logs. The issue only showed up when the folder name contained "-"
  or "." characters.
* Add enterprise enabling flag to enterprise composition GUI
  container, so that the enterprise features are shown in the Frontend.
* Fix - Make sure the demo-script subprocess has a stdin fd
  ([MEN-2836](https://tracker.mender.io/browse/MEN-2836))
* Fix - Create explicit exitcond for the demo setup fixture
  ([MEN-2836](https://tracker.mender.io/browse/MEN-2836))
* Change Enterprise Docker links to registry.mender.io.
  This will be our gateway to serve the Enterprise images, not Docker
  Hub. Those who are using Enterprise will need to log into this
  gateway:
  ```
  docker login -u $USERNAME registry.mender.io
  ```
  where `$USERNAME` is the username given to you from Northern.tech. You
  will be prompted for the password.
* Verify that empty batches returns a 400 error
  Added a test for verifying that deployments-enterprise returns a 400 error
  in case of the number of devices in a batch being empty due to rounding
  errors in relation to the formula used for determining the number of devices
  in a batch. ([MEN-2838](https://tracker.mender.io/browse/MEN-2838))
* Backend Integration tests always print "tests failed"; fix.
* Remove the Python dependency in the demo script
  Remove the Python dependency in the demo script, to decrease the dependency
  surface of the demo script.
  Now the Mender-Artifact and Mender versions are parsed from the
  docker-compose.client.yml and other-components.yml files through a simple AWK
  script instead.
  ([MEN-2817](https://tracker.mender.io/browse/MEN-2817))
* Unskip the Pre-Auth tests
  ([MEN-1797](https://tracker.mender.io/browse/MEN-1797))
* Enable logging for minio
  ([MEN-2922](https://tracker.mender.io/browse/MEN-2922))
* [tests/run.sh] Enable passing on quoted arguments to pytest
* Run workflows with automigrate in production
  ([QA-139](https://tracker.mender.io/browse/QA-139))
* workflows server fixing demo command
  ([QA-139](https://tracker.mender.io/browse/QA-139))
* Upgrade elasticsearch to version 6
  ([MEN-2985](https://tracker.mender.io/browse/MEN-2985))
* Fix setup for running without SSL termination
* Add create-artifact-worker 1.0.0b1.
* Upgrade deployments to 1.9.0b1.
* Upgrade deployments-enterprise to 1.9.0b1.
* Upgrade deviceauth to 2.2.0b1.
* Upgrade gui to 2.3.0b1.
* Upgrade inventory to 1.7.0b1.
* Upgrade mender to 2.2.0b1.
* Upgrade mender-api-gateway-docker to 2.1.0b1.
* Upgrade mender-artifact to 3.3.0b1.
* Upgrade mender-cli to 1.3.0b1.
* Upgrade mender-conductor to 1.6.0b1.
* Upgrade mender-conductor-enterprise to 1.6.0b1.
* Upgrade tenantadm to 1.1.0b1.
* Upgrade useradm to 1.10.0b1.
* Upgrade useradm-enterprise to 1.10.0b1.
* Add workflows 1.0.0b1.

#### inventory (1.7.0)

New changes in inventory since 1.6.0:

* support for new mongo-driver
  ([MEN-2454](https://tracker.mender.io/browse/MEN-2454), [MEN-2801](https://tracker.mender.io/browse/MEN-2801))

#### mender (2.2.0)

New changes in mender since 2.2.0b1:

* Remove text/template dependency from the cli library reducing
  mender client binary size by approximately 20%
* Fix "State transition loop detected" when retrying status update.

New changes in mender since 2.1.2:

* mender setup cli command and new CLI package
  ([MEN-2418](https://tracker.mender.io/browse/MEN-2418), [MEN-2806](https://tracker.mender.io/browse/MEN-2806))
* Fix UBI device size calculation
* store: Save artifact provides for dependency verifications
* app: Verify artifact (version >= 3) dependencies with current artifact
* store/app{standalone}: Artifact dependency checking for artifact v3
* app/store{standalone}: Unit tests Artifact v3 depends and provides
* Enable the usage of the full Mender-Artifact version 3 format
  ([MEN-2642](https://tracker.mender.io/browse/MEN-2642))
* support: modules-artifact-gen: Fix typo in default name of output file
* Rename --mender-professional flag to --hosted-mender
* Add --quiet flag and remove --run-daemon option and confirm device
* Now the client stores Artifact provides parameters across reboots in
  standalone mode. Previously this data was ignored, and hence upgrading with an
  Artifact with provides parameters these were lost.
  ([MEN-2969](https://tracker.mender.io/browse/MEN-2969))
* Set default device type to hostname for interactive setup
* New command: `snapshot dump` to dump current rootfs
* Skip special device "rootfs" when determining rootfs type
* Report 'Unknown' rootfs type if we can't detect it
* Optimize rootfs-update image writes
  ([MEN-2939](https://tracker.mender.io/browse/MEN-2939))
* Make `single-file-artifact-gen` script POSIX compliant.
  ([MEN-3049](https://tracker.mender.io/browse/MEN-3049))
* Fix segfault when running `mender setup` on a read-only
  filesystem.
* Fix crash when specified certificate can't be opened.
  Both the `ServerCertificate` setting and the system certificates are
  now optional, in the sense that the client will run without them.
  However, the client will not be able to connect without the right
  certificates, so the main usecase of this change is to have a workable
  client that will roll back if connections can't be made, instead of
  exiting. ([MEN-3047](https://tracker.mender.io/browse/MEN-3047))
* Add warning message when server certificate can't be parsed.
* snapshot: Added watchdog timer to keep system from freezing
* snapshot: Add compression options to speed up transfer
* Improved error message when an update-module is missing
  ([MEN-3007](https://tracker.mender.io/browse/MEN-3007))
* snapshot: New flag `--source` specifying the source
  filesystem to snapshot

#### mender-api-gateway-docker (2.1.0)

New changes in mender-api-gateway-docker since 2.0.0:

* ssl_trusted_certificate added
* SSL termination can be turned off via environment variable

#### mender-artifact (3.3.0)

New changes in mender-artifact since 3.2.1:

* Adds API for returning all Artifact provides and depends
  ([MEN-2549](https://tracker.mender.io/browse/MEN-2549))
* Enables Artifact Provides and Depends for write rootfs-img
  Previously, the `write rootfs-image` command did not have the ability
  to set Provides and Depends in the artifact. This was only enabled for
  the `write module-image` command. Now the `rootfs-image` update can
  also set Provides and Depends. However, please note that meta-data
  and augmented Provides and Depends still are unsupported.
  ([MEN-2812](https://tracker.mender.io/browse/MEN-2812))
* Fix bug that destroys Artifact if any copy/modify command
  is used on a non-rootfs-image Artifact.
  ([MEN-2592](https://tracker.mender.io/browse/MEN-2592))
* The `modify` subcommand has gained the `-k`/`--key`
  argument to automatically sign the Artifact after modification.
  ([MEN-2592](https://tracker.mender.io/browse/MEN-2592))
* Remove superfluous "Files" header from `read` output.
* Fix incorrect help string for signed artifacts.
  If no key was provided, it said that the signature verification
  failed, but it should instruct the user to provide a key.
* Fix state scripts being lost when modifying artifact.
* One can now use `mender-artifact modify` to change artifact
  Depends, Provides and Meta-data attributes. See the help screen for
  more information.
  ([MEN-1669](https://tracker.mender.io/browse/MEN-1669))
* `mender-artifact modify --name` argument renamed to
  `--artifact-name` to match the rest of the tool's flags. The old flag
  is still kept for compatibility.
  ([MEN-1669](https://tracker.mender.io/browse/MEN-1669))
* Make artifact install respect the given file permissions
  ([MEN-2880](https://tracker.mender.io/browse/MEN-2880))
* Added the writing of the `rootfs_image_checksum` provide parameter as
  a default to `rootfs-image` Artifacts. This means that now, the
  `rootfs_image_checksum` will be written as a provide parameter to the Mender
  client's database upon an update with the given Artifact. Please note that for
  older clients (i.e. <= 2.1.x) this will not work, and the functionality should
  be disabled by the user through the `--no-checksum-provide` flag when writing a
  rootfs-image Artifact.
  ([MEN-2956](https://tracker.mender.io/browse/MEN-2956))
* Create artifact from device snapshot

#### mender-cli (1.3.0)

New changes in mender-cli since 1.2.0:

* Build and publish Mac OS X binary for `mender-cli`

#### mender-conductor (1.6.0)

New changes in mender-conductor since 1.5.0:

* Bugfixes for send_email conductor worker
* Prepare ES6 enabled conductor image
  ([MC-1296](https://tracker.mender.io/browse/MC-1296), [MEN-2987](https://tracker.mender.io/browse/MEN-2987))

#### mender-conductor-enterprise (1.6.0)

New changes in mender-conductor-enterprise since 1.5.0:

* Bugfixes for prepare_org_welcome_email conductor worker

#### tenantadm (1.1.0)

New changes in tenantadm since 1.0.0:

* stripe-go library updated
* api/http: New endpoint for creating inactive organization.
* Endpoint for removing inactive organization
* api/http: management endpoint for activating organization and updating org CC info
* store: Update to official mongodb driver

#### useradm (1.10.0)

New changes in useradm since 1.9.1:

* store/mongo: handle mongodb client creation error

#### useradm-enterprise (1.10.0)

New changes in useradm-enterprise since 1.9.1:

* Support for older Google authenticators on iOS, trimming secret length
* FIX: Create user panics when tenant-id is not specified
* store/mongo: handle mongodb client creation error

#### workflows (1.0.0)

* Refactor repo and added metadata endpoints
* docker: Initialized docker files workflows
* fixing entrypoint to match other services
  ([QA-139](https://tracker.mender.io/browse/QA-139))
* default mongo url fix
  ([MEN-3060](https://tracker.mender.io/browse/MEN-3060))


## Mender 2.2.2

_Released 03.05.2020_

### Statistics

A total of 2128 lines added, 207 removed (delta 1921)

| Developers with the most changesets | |
|---|---|
| Manuel Zedel | 13 (65.0%) |
| Kristian Amlie | 5 (25.0%) |
| Michael Clelland | 1 (5.0%) |
| Lluis Campos | 1 (5.0%) |

| Developers with the most changed lines | |
|---|---|
| Manuel Zedel | 2008 (93.6%) |
| Kristian Amlie | 118 (5.5%) |
| Lluis Campos | 18 (0.8%) |
| Michael Clelland | 2 (0.1%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 20 (100.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 2146 (100.0%) |

| Employers with the most hackers (total 4) | |
|---|---|
| Northern.tech | 4 (100.0%) |

### Changelogs

#### gui (2.2.2)

New changes in gui since 2.2.1:

* fix: removed superfluous " around tenant token in device config code
* Fix for changing page length for pagination of rejected and preauth devices
* fixed deploymentdevicelist lacking device identity information
* fixed device list refresh after page length change in deployment devicelist
* fixed an issue that prevented the staying logged in functionality from working

#### integration (2.2.2)

New changes in integration since 2.2.1:

* Upgrade gui to 2.2.2.
* Upgrade mender to 2.1.3.

#### mender (2.1.3)

New changes in mender since 2.1.2:

* Fix crash when specified certificate can't be opened.
  Both the `ServerCertificate` setting and the system certificates are
  now optional, in the sense that the client will run without them.
  However, the client will not be able to connect without the right
  certificates, so the main usecase of this change is to have a workable
  client that will roll back if connections can't be made, instead of
  exiting. ([MEN-3047](https://tracker.mender.io/browse/MEN-3047))
* Add warning message when server certificate can't be parsed.


## meta-mender warrior-v2020.02.2

_Released 02.18.2020_

### Statistics

A total of 26 lines added, 7 removed (delta 19)

| Developers with the most changesets | |
|---|---|
| Matthew Beckler | 2 (40.0%) |
| Gaurav Kalra | 1 (20.0%) |
| Joerg Hofrichter | 1 (20.0%) |
| Drew Moseley | 1 (20.0%) |

| Developers with the most changed lines | |
|---|---|
| Drew Moseley | 21 (80.8%) |
| Matthew Beckler | 2 (7.7%) |
| Joerg Hofrichter | 2 (7.7%) |
| Gaurav Kalra | 1 (3.8%) |

| Developers with the most signoffs (total 1) | |
|---|---|
| Kristian Amlie | 1 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Packet Power LLC | 2 (40.0%) |
| National Instruments | 1 (20.0%) |
| SM Instruments Inc. | 1 (20.0%) |
| Northern.tech | 1 (20.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 21 (80.8%) |
| Packet Power LLC | 2 (7.7%) |
| National Instruments | 2 (7.7%) |
| SM Instruments Inc. | 1 (3.8%) |

| Employers with the most signoffs (total 1) | |
|---|---|
| Northern.tech | 1 (100.0%) |

| Employers with the most hackers (total 4) | |
|---|---|
| Northern.tech | 1 (25.0%) |
| Packet Power LLC | 1 (25.0%) |
| National Instruments | 1 (25.0%) |
| SM Instruments Inc. | 1 (25.0%) |

### Changelogs

#### meta-mender (warrior-v2020.02.2)

New changes in meta-mender since warrior-v2020.02:

* mender-helpers: Error out if copying different files to boot part.
* Improve warning when multiple DTB files are in KERNEL_DEVICETREE
* Add MENDER_DTB_NAME_FORCE to mender-vars.json to avoid unrecognized variable warning
* rpi: fix rootfs cmdline trailing space


## meta-mender warrior-v2020.02

_Released 02.12.2020_

### Statistics

A total of 69 lines added, 42 removed (delta 27)

| Developers with the most changesets | |
|---|---|
| Drew Moseley | 7 (43.8%) |
| Kristian Amlie | 6 (37.5%) |
| Lluis Campos | 1 (6.2%) |
| Gaurav Kalra | 1 (6.2%) |
| Benjamin Byholm | 1 (6.2%) |

| Developers with the most changed lines | |
|---|---|
| Drew Moseley | 36 (45.6%) |
| Kristian Amlie | 25 (31.6%) |
| Lluis Campos | 10 (12.7%) |
| Benjamin Byholm | 7 (8.9%) |
| Gaurav Kalra | 1 (1.3%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 14 (87.5%) |
| walkbase | 1 (6.2%) |
| gvkalra@gmail.com | 1 (6.2%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 71 (89.9%) |
| walkbase | 7 (8.9%) |
| gvkalra@gmail.com | 1 (1.3%) |

| Employers with the most hackers (total 5) | |
|---|---|
| Northern.tech | 3 (60.0%) |
| walkbase | 1 (20.0%) |
| gvkalra@gmail.com | 1 (20.0%) |

### Changelogs

#### meta-mender (warrior-v2020.02)

New changes in meta-mender since warrior-v2019.12:

* mender-setup: allow setting fstab options for the boot partition
* grub-mender-grubenv: Fix broken debug-log PACKAGECONFIG.
* grub-efi: Respect MENDER_BOOT_PART_MOUNT_LOCATION
* mender-grub: Set EFI_PROVIDER to grub-efi.
* remove stray '-' in IMAGE_NAME
* systemd-boot: Respect MENDER_BOOT_PART_MOUNT_LOCATION
* Add mender 2.2.0b1 recipe
* Add mender-artifact 3.3.0b1 recipe
* In demo mode, put demo certificate in same directory as Debian package.
  ([MEN-3048](https://tracker.mender.io/browse/MEN-3048))


## meta-mender thud-v2019.12

_Released 12.17.2019_

### Statistics

A total of 597 lines added, 366 removed (delta 231)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 17 (39.5%) |
| Lluis Campos | 10 (23.3%) |
| Drew Moseley | 9 (20.9%) |
| Mirza Krak | 4 (9.3%) |
| Ole Petter Orhagen | 1 (2.3%) |
| Joerg Hofrichter | 1 (2.3%) |
| Pierre-Jean Texier | 1 (2.3%) |

| Developers with the most changed lines | |
|---|---|
| Kristian Amlie | 370 (48.2%) |
| Drew Moseley | 140 (18.3%) |
| Ole Petter Orhagen | 113 (14.7%) |
| Lluis Campos | 83 (10.8%) |
| Mirza Krak | 58 (7.6%) |
| Pierre-Jean Texier | 2 (0.3%) |
| Joerg Hofrichter | 1 (0.1%) |

| Developers with the most lines removed | |
|---|---|
| Ole Petter Orhagen | 82 (22.4%) |

| Developers with the most signoffs (total 1) | |
|---|---|
| Kristian Amlie | 1 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 41 (95.3%) |
| KONCEPTO | 1 (2.3%) |
| National Instruments | 1 (2.3%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 764 (99.6%) |
| KONCEPTO | 2 (0.3%) |
| National Instruments | 1 (0.1%) |

| Employers with the most signoffs (total 1) | |
|---|---|
| Northern.tech | 1 (100.0%) |

| Employers with the most hackers (total 7) | |
|---|---|
| Northern.tech | 5 (71.4%) |
| KONCEPTO | 1 (14.3%) |
| National Instruments | 1 (14.3%) |

### Changelogs

#### meta-mender (thud-v2019.12)

New changes in meta-mender since thud-v2019.08:

* Add meta-mender-commercial layer.
  This will host our mender-binary-delta Update Module.
* Update recipe for mender-binary-delta pre-release v0.1.1
* u-boot-fw-utils: set PACKAGE_ARCH as MACHINE_ARCH
* Add mender-2.1.0 and mender-artifact-3.1.0.
* Fix "set_image_size" errors when large files are installed
  in /data directory (staging area for data partition filesystem image)
* mender-systemd: Maintain persistent machine-id across updates.
* Start using Git SHA based grub-mender-grubenv versions.
* Add grub-mender-grubenv 1.3.0 recipe.
* Add support for initramfs when booting using GRUB.
* grub-mender-grubenv: Setup debug option to drop to grub prompt.
* Fix initramfs builds when using meta-mender layer
* mender: Scan for devices with the live installer
* `FILESEXTRAPATHS_prepend_pn-mender-binary-delta` now needs
  to point to the folder containing `arm`, `aarch64` and `x86_64`, not the folder
  containing the binary.
* Update recipe for mender-binary-delta beta release v1.0.0b1
* Update recipe for mender-binary-delta final release v1.0.0
* Fix incorrect boot partition type for EFI boot partitions.
* Fix issue where U-boot is not able to find a valid DTB on Raspberry Pi boards
* Add mender 2.1.1 and mender-artifact 3.2.0b1 recipes.
* Add mender-artifact 3.2.0 and remove beta.
* mender-image: Add DEPENDS to include WKS_FILE_DEPENDS.
* Add mender 2.1.2 recipe
* Add mender-artifact 3.1.1 recipe
* Add mender-artifact 3.2.1 recipe
* Add mender-binar-delta 1.0.1 recipe
* Removes the tests covering Mender-Artifact version 1.
  ([MEN-2156](https://tracker.mender.io/browse/MEN-2156))


## meta-mender sumo-v2019.12

_Released 12.17.2019_

### Statistics

A total of 353 lines added, 241 removed (delta 112)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 10 (34.5%) |
| Lluis Campos | 9 (31.0%) |
| Drew Moseley | 6 (20.7%) |
| Ole Petter Orhagen | 1 (3.4%) |
| Joerg Hofrichter | 1 (3.4%) |
| Mirza Krak | 1 (3.4%) |
| Ajith P V | 1 (3.4%) |

| Developers with the most changed lines | |
|---|---|
| Kristian Amlie | 168 (34.4%) |
| Drew Moseley | 130 (26.6%) |
| Ole Petter Orhagen | 113 (23.1%) |
| Lluis Campos | 41 (8.4%) |
| Mirza Krak | 35 (7.2%) |
| Joerg Hofrichter | 1 (0.2%) |
| Ajith P V | 1 (0.2%) |

| Developers with the most lines removed | |
|---|---|
| Ole Petter Orhagen | 82 (34.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 27 (93.1%) |
| National Instruments | 1 (3.4%) |
| ajithpv@outlook.com | 1 (3.4%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 487 (99.6%) |
| National Instruments | 1 (0.2%) |
| ajithpv@outlook.com | 1 (0.2%) |

| Employers with the most hackers (total 7) | |
|---|---|
| Northern.tech | 5 (71.4%) |
| National Instruments | 1 (14.3%) |
| ajithpv@outlook.com | 1 (14.3%) |

### Changelogs

#### meta-mender (sumo-v2019.12)

New changes in meta-mender since sumo-v2019.08:

* Add meta-mender-commercial layer.
  This will host our mender-binary-delta Update Module.
* Update recipe for mender-binary-delta pre-release v0.1.1
* `FILESEXTRAPATHS_prepend_pn-mender-binary-delta` now needs
  to point to the folder containing `arm`, `aarch64` and `x86_64`, not the folder
  containing the binary.
* Update recipe for mender-binary-delta beta release v1.0.0b1
* Update recipe for mender-binary-delta final release v1.0.0
* mender-image: Add DEPENDS to include WKS_FILE_DEPENDS.
* mender: Use += rather than _append for IMAGE_FSTYPES.
* mender-systemd: Maintain persistent machine-id across updates.
* Add 'datatar' as an image type.
* Fix issue where U-boot is not able to find a valid DTB on Raspberry Pi boards
* Add mender-2.1.0 and mender-artifact-3.1.0.
* Add mender 2.1.1 and mender-artifact 3.2.0b1 recipes.
* Add mender-artifact 3.2.0 and remove beta.
* Add mender 2.1.2 recipe
* Add mender-artifact 3.1.1 recipe
* Add mender-artifact 3.2.1 recipe
* Add mender-binar-delta 1.0.1 recipe
* Removes the tests covering Mender-Artifact version 1.
  ([MEN-2156](https://tracker.mender.io/browse/MEN-2156))


## mender-convert 1.2.2

_Released 12.11.2019_

### Statistics

A total of 9 lines added, 10 removed (delta -1)

| Developers with the most changesets | |
|---|---|
| Lluis Campos | 2 (100.0%) |

| Developers with the most changed lines | |
|---|---|
| Lluis Campos | 10 (100.0%) |

| Developers with the most lines removed | |
|---|---|
| Lluis Campos | 1 (10.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 2 (100.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 10 (100.0%) |

| Employers with the most hackers (total 1) | |
|---|---|
| Northern.tech | 1 (100.0%) |

### Changelogs

#### mender-convert (1.2.2)

New changes in mender-convert since 1.2.1:

* Upgrade client and mender-artifact to 2.1.2 and 3.2.1, respectively


## meta-mender warrior-v2019.12

_Released 12.10.2019_

### Statistics

A total of 13 lines added, 8 removed (delta 5)

| Developers with the most changesets | |
|---|---|
| Lluis Campos | 3 (50.0%) |
| Drew Moseley | 2 (33.3%) |
| Joerg Hofrichter | 1 (16.7%) |

| Developers with the most changed lines | |
|---|---|
| Lluis Campos | 6 (46.2%) |
| Drew Moseley | 6 (46.2%) |
| Joerg Hofrichter | 1 (7.7%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 5 (83.3%) |
| National Instruments | 1 (16.7%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 12 (92.3%) |
| National Instruments | 1 (7.7%) |

| Employers with the most hackers (total 3) | |
|---|---|
| Northern.tech | 2 (66.7%) |
| National Instruments | 1 (33.3%) |

### Changelogs

#### meta-mender (warrior-v2019.12)

New changes in meta-mender since warrior-v2019.11:

* Update recipe for mender-binary-delta final release v1.0.0
* mender-image: Add DEPENDS to include WKS_FILE_DEPENDS.
* Add mender 2.1.2 recipe
* Add mender-artifact 3.1.1 recipe
* Add mender-artifact 3.2.1 recipe
* Add mender-binary-delta 1.0.1 recipe


## mender-binary-delta 1.0.1

_Released 12.06.2019_

### Changelogs

#### mender-binary-delta (1.0.1)

New changes in mender-binary-delta since 1.0.0:

* MEN-2928: Fix: Enable file-systems larger than approx 2-GiGs
  ([MEN-2928](https://tracker.mender.io/browse/MEN-2928))


## Mender 2.2.1

_Released 12.05.2019_

### Statistics

A total of 1571 lines added, 1337 removed (delta 234)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 18 (33.3%) |
| Manuel Zedel | 14 (25.9%) |
| Peter Grzybowski | 8 (14.8%) |
| Lluis Campos | 6 (11.1%) |
| Ole Petter Orhagen | 4 (7.4%) |
| Michael Clelland | 2 (3.7%) |
| Eystein Måløy Stenberg | 1 (1.9%) |
| Sam Lewis | 1 (1.9%) |

| Developers with the most changed lines | |
|---|---|
| Kristian Amlie | 853 (34.2%) |
| Peter Grzybowski | 820 (32.9%) |
| Ole Petter Orhagen | 477 (19.1%) |
| Manuel Zedel | 235 (9.4%) |
| Lluis Campos | 91 (3.7%) |
| Sam Lewis | 10 (0.4%) |
| Michael Clelland | 4 (0.2%) |
| Eystein Måløy Stenberg | 2 (0.1%) |

| Developers with the most lines removed | |
|---|---|
| Kristian Amlie | 674 (50.4%) |
| Manuel Zedel | 71 (5.3%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 53 (98.1%) |
| sam.vr.lewis@gmail.com | 1 (1.9%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 2482 (99.6%) |
| sam.vr.lewis@gmail.com | 10 (0.4%) |

| Employers with the most hackers (total 8) | |
|---|---|
| Northern.tech | 7 (87.5%) |
| sam.vr.lewis@gmail.com | 1 (12.5%) |

### Changelogs

#### deployments (1.8.1)

New changes in deployments since 1.8.0:

* run migrations on startup like other services do
  ([MC-1144](https://tracker.mender.io/browse/MC-1144))
* index deployments database
  ([MEN-2019](https://tracker.mender.io/browse/MEN-2019))
* added unit tests: indices created.
  ([MEN-2019](https://tracker.mender.io/browse/MEN-2019))

#### deployments-enterprise (1.8.1)

New changes in deployments-enterprise since 1.8.0:

* run migrations on startup like other services do
  ([MC-1144](https://tracker.mender.io/browse/MC-1144))
* index deployments database
  ([MEN-2019](https://tracker.mender.io/browse/MEN-2019))
* added unit tests: indices created.
  ([MEN-2019](https://tracker.mender.io/browse/MEN-2019))

#### gui (2.2.1)

New changes in gui since 2.2.0:

* fixed empty userData on edit, causing blank ui fields in settings & header
* fixed persistence of helptip dismissal during onboarding
* fixed regression: filtered on device-type before deployment
* ensured device groups are sorted when retrieved from backend

#### integration (2.2.1)

New changes in integration since 2.2.0:

* Upgrade deployments to 1.8.1.
* Upgrade deployments-enterprise to 1.8.1.
* Upgrade gui to 2.2.1.
* Upgrade mender to 2.1.2.
* Upgrade mender-artifact to 3.2.1.
* Upgrade useradm to 1.9.1.
* Upgrade useradm-enterprise to 1.9.1.

#### mender (2.1.2)

New changes in mender since 2.1.1:

* Fix UBI device size calculation

#### mender-artifact (3.2.1)

New changes in mender-artifact since 3.2.0:

* Make artifact install respect the given file permissions
  ([MEN-2880](https://tracker.mender.io/browse/MEN-2880))

#### useradm-enterprise (1.9.1)

New changes in useradm-enterprise since 1.9.0:

* Support for older Google authenticators on iOS, trimming secret length
* Two factor authentication API docs
  ([MEN-2884](https://tracker.mender.io/browse/MEN-2884))


## Mender 2.1.1

_Released 12.05.2019_

### Statistics

A total of 1219 lines added, 421 removed (delta 798)

| Developers with the most changesets | |
|---|---|
| Lluis Campos | 12 (30.0%) |
| Kristian Amlie | 11 (27.5%) |
| Ole Petter Orhagen | 11 (27.5%) |
| Krzysztof Jaskiewicz | 1 (2.5%) |
| Manuel Zedel | 1 (2.5%) |
| Sam Lewis | 1 (2.5%) |
| Peter Grzybowski | 1 (2.5%) |
| Pierre-Jean Texier | 1 (2.5%) |
| Ajith P Venugopal | 1 (2.5%) |

| Developers with the most changed lines | |
|---|---|
| Ole Petter Orhagen | 551 (43.4%) |
| Kristian Amlie | 478 (37.7%) |
| Lluis Campos | 145 (11.4%) |
| Krzysztof Jaskiewicz | 78 (6.1%) |
| Sam Lewis | 10 (0.8%) |
| Peter Grzybowski | 4 (0.3%) |
| Manuel Zedel | 1 (0.1%) |
| Pierre-Jean Texier | 1 (0.1%) |
| Ajith P Venugopal | 1 (0.1%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 36 (90.0%) |
| KONCEPTO | 1 (2.5%) |
| sam.vr.lewis@gmail.com | 1 (2.5%) |
| ajithpv@outlook.com | 1 (2.5%) |
| RnDity | 1 (2.5%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 1179 (92.9%) |
| RnDity | 78 (6.1%) |
| sam.vr.lewis@gmail.com | 10 (0.8%) |
| KONCEPTO | 1 (0.1%) |
| ajithpv@outlook.com | 1 (0.1%) |

| Employers with the most hackers (total 9) | |
|---|---|
| Northern.tech | 5 (55.6%) |
| RnDity | 1 (11.1%) |
| sam.vr.lewis@gmail.com | 1 (11.1%) |
| KONCEPTO | 1 (11.1%) |
| ajithpv@outlook.com | 1 (11.1%) |

### Changelogs

#### deviceauth (2.0.1)

New changes in deviceauth since 2.0.0:

* additional mongodb index added

#### gui (2.1.1)

New changes in gui since 2.1.0:

* Fixed faulty fallback file definition in nginx config

#### integration (2.1.1)

New changes in integration since 2.1.0:

* Fix issue when demo script exists abruptly on user request
  for logs. The issue only showed up when the folder name contained "-"
  or "." characters.
* Fix - Make sure the demo-script subprocess has a stdin fd
  ([MEN-2836](https://tracker.mender.io/browse/MEN-2836))
* Fix - Create explicit exitcond for the demo setup fixture
  ([MEN-2836](https://tracker.mender.io/browse/MEN-2836))
* Upgrade deviceauth to 2.0.1.
* Upgrade gui to 2.1.1.
* Upgrade mender to 2.1.2.
* Upgrade mender-artifact to 3.1.1.

#### mender (2.1.2)

New changes in mender since 2.1.0:

* module/single-file: fix rollback state by correctly defining filename
* Check for -f option in stat command
* Set hard limit(10) for client update status report retries
  This fixes an issue where the maxSendingAttemps in
  updateReportRetry state could be set real high, since it is calculated
  as UpdatePollIntervalSeconds / RetryPollIntervalSeconds. This adds a
  hard upper limit of 10 retries for the client in any case.
  ([MEN-2676](https://tracker.mender.io/browse/MEN-2676))
* Fix UBI device size calculation

#### mender-artifact (3.1.1)

New changes in mender-artifact since 3.1.0:

* fix erroneously report of "-dirty" in the version
  string. ([MEN-2800](https://tracker.mender.io/browse/MEN-2800))
* Fix: mender-artifact modify did not clean up the temp-files created
  ([MEN-2758](https://tracker.mender.io/browse/MEN-2758))
* Fix build-contained Makefile: image was missing make install
* Make artifact install respect the given file permissions
  ([MEN-2880](https://tracker.mender.io/browse/MEN-2880))


## meta-mender warrior-v2019.11

_Released 10.30.2019_

### Statistics

A total of 11 lines added, 4 removed (delta 7)

| Developers with the most changesets | |
|---|---|
| Benjamin Byholm | 1 (33.3%) |
| Lluis Campos | 1 (33.3%) |
| Alf-Rune Siqveland | 1 (33.3%) |

| Developers with the most changed lines | |
|---|---|
| Lluis Campos | 6 (54.5%) |
| Alf-Rune Siqveland | 4 (36.4%) |
| Benjamin Byholm | 1 (9.1%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 2 (66.7%) |
| walkbase | 1 (33.3%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 10 (90.9%) |
| walkbase | 1 (9.1%) |

| Employers with the most hackers (total 3) | |
|---|---|
| Northern.tech | 2 (66.7%) |
| walkbase | 1 (33.3%) |

### Changelogs

#### meta-mender (warrior-v2019.11)

New changes in meta-mender since warrior-v2019.10.2:

* mender-setup: do not add systemd options to fstab without mender-systemd


## mender-convert 1.2.1

_Released 10.24.2019_

### Statistics

A total of 27 lines added, 18 removed (delta 9)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 2 (40.0%) |
| Mirza Krak | 2 (40.0%) |
| Simon Guigui | 1 (20.0%) |

| Developers with the most changed lines | |
|---|---|
| Kristian Amlie | 13 (46.4%) |
| Simon Guigui | 13 (46.4%) |
| Mirza Krak | 2 (7.1%) |

| Developers with the most lines removed | |
|---|---|
| Simon Guigui | 1 (5.6%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 4 (80.0%) |
| fyhertz@gmail.com | 1 (20.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 15 (53.6%) |
| fyhertz@gmail.com | 13 (46.4%) |

| Employers with the most hackers (total 3) | |
|---|---|
| Northern.tech | 2 (66.7%) |
| fyhertz@gmail.com | 1 (33.3%) |

### Changelogs

#### mender-convert (1.2.1)

New changes in mender-convert since 1.2.0:

* Fix "yellow" HDMI output on Raspbian Buster
  ([MEN-2685](https://tracker.mender.io/browse/MEN-2685))
* Upgrade client and mender-artifact to 2.1.1 and 3.2.0, respectively.
* Fix some race conditions when running multiple instances of mender-convert in parallel


## meta-mender warrior-v2019.10.2

_Released 10.23.2019_

### Changelogs

#### meta-mender (warrior-v2019.10.2)

New changes in mender-artifact since warrior-v2019.10:

* Add mender-artifact 3.2.0 and remove beta.


## Mender 2.2.0

_Released 10.23.2019_

### Statistics

A total of 20171 lines added, 15470 removed (delta 4701)

| Developers with the most changesets | |
|---|---|
| Manuel Zedel | 142 (37.5%) |
| Marcin Chalczynski | 57 (15.0%) |
| Krzysztof Jaskiewicz | 43 (11.3%) |
| Kristian Amlie | 38 (10.0%) |
| Lluis Campos | 33 (8.7%) |
| Michael Clelland | 33 (8.7%) |
| Ole Petter Orhagen | 24 (6.3%) |
| Alf-Rune Siqveland | 3 (0.8%) |
| Peter Grzybowski | 2 (0.5%) |
| Marcin Pasinski | 1 (0.3%) |

| Developers with the most changed lines | |
|---|---|
| Krzysztof Jaskiewicz | 10092 (40.4%) |
| Manuel Zedel | 5779 (23.1%) |
| Marcin Chalczynski | 2974 (11.9%) |
| Ole Petter Orhagen | 1942 (7.8%) |
| Kristian Amlie | 1539 (6.2%) |
| Michael Clelland | 1289 (5.2%) |
| Lluis Campos | 805 (3.2%) |
| Alf-Rune Siqveland | 546 (2.2%) |
| Eystein Måløy Stenberg | 9 (0.0%) |
| Peter Grzybowski | 5 (0.0%) |

| Developers with the most lines removed | |
|---|---|
| Krzysztof Jaskiewicz | 692 (4.5%) |
| Lluis Campos | 39 (0.3%) |
| Eystein Måløy Stenberg | 2 (0.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 277 (73.1%) |
| RnDity | 100 (26.4%) |
| KONCEPTO | 1 (0.3%) |
| ajithpv@outlook.com | 1 (0.3%) |

| Top lines changed by employer | |
|---|---|
| RnDity | 13066 (52.3%) |
| Northern.tech | 11915 (47.7%) |
| KONCEPTO | 1 (0.0%) |
| ajithpv@outlook.com | 1 (0.0%) |

| Employers with the most hackers (total 13) | |
|---|---|
| Northern.tech | 9 (69.2%) |
| RnDity | 2 (15.4%) |
| KONCEPTO | 1 (7.7%) |
| ajithpv@outlook.com | 1 (7.7%) |

### Changelogs

#### deployments (1.8.0)

New changes in deployments since 1.7.1:

* Fix "unexpected EOF" errors when the source of the artifact
  is a slow network stream.
* Fix spurious upload errors due to wrong EOF handling.
* Fix inability to resume partial migration.

#### deployments-enterprise (1.8.0)

New changes in deployments-enterprise since 1.8.0b1:

* Disallow empty batches in phased rollouts
  Previously there was a possibility to end up with an empty batch, due
  to the formula used in the calculation for the number of devices which
  is based on extracting a percentage number of devices from the total. Thus
  if the total is so small, that a percentage below some number rounds to zero,
  the batch would be empty. Now that same input will return an error.
  ([MEN-2810](https://tracker.mender.io/browse/MEN-2810))

#### deviceauth (2.1.0)

New changes in deviceauth since 2.1.0b1:

* additional mongodb index added

New changes in deviceauth since 2.0.0:

* Add support for default tenant token.
  It can be used to allow devices that don't have a tenant token to be
  allowed into a specific tenant's list of devices. Enable it either
  using the `DEVICEAUTH_DEFAULT_TENANT_TOKEN` environment variable, or
  the `default_tenant_token` setting in `config.yaml`.
  ([MEN-2705](https://tracker.mender.io/browse/MEN-2705), [MEN-2706](https://tracker.mender.io/browse/MEN-2706))

#### gui (2.2.0)

New changes in gui since 2.2.0b1:

* disabled onboarding steps in enterprise environments
* added frontend validation to disable empty batches in phased deployments
  ([MEN-2820](https://tracker.mender.io/browse/MEN-2820))
* prevented an error in finished deployments view
* fixed phased deployment progress calculation
* added support for raspberrypi4 during onboarding
* moved retry deployment to use createdeployment dialog for review
* Fixed a bug that broke the pagination in the finished deployments list
* added 2fa setup validation step
* added possibility to select previous deployment patterns
* disabled browser suggestions on autoselects
* added starttime column to deployments list in enterprise

New changes in gui since 2.1.0:

* limited height of large select lists to prevent them from hiding input
* ensured artifact & group sort order during deployment scheduling
* added closed feature notifications to show in open source UI
* Updated deployment creation UI to wizard for phased deployments

#### integration (2.2.0)

New changes in integration since 2.2.0b1:

* Fix - Create explicit exitcond for the demo setup fixture
  ([MEN-2836](https://tracker.mender.io/browse/MEN-2836))
* Change Enterprise Docker links to registry.mender.io.
  This will be our gateway to serve the Enterprise images, not Docker
  Hub. Those who are using Enterprise will need to log into this
  gateway:
  ```
  docker login -u $USERNAME registry.mender.io
  ```
  where `$USERNAME` is the username given to you from Northern.tech. You
  will be prompted for the password.
* Add enterprise enabling flag to enterprise composition GUI
  container, so that the enterprise features are shown in the Frontend.
* Upgrade deployments to 1.8.0.
* Upgrade deployments-enterprise to 1.8.0.
* Upgrade deviceauth to 2.1.0.
* Upgrade gui to 2.2.0.
* Upgrade mender-artifact to 3.2.0.
* Upgrade mender-conductor to 1.5.0.
* Upgrade mender-conductor-enterprise to 1.5.0.
* Upgrade tenantadm to 1.0.0.
* Upgrade useradm to 1.9.0.
* Upgrade useradm-enterprise to 1.9.0.
* Fix - Make sure the demo-script subprocess has a stdin fd
  ([MEN-2836](https://tracker.mender.io/browse/MEN-2836))

New changes in integration since 2.1.0:

* remove default conductor config file
* Fix error: `No such container: integration-2.1.0b1_mender-useradm_1`
* Introduced `enterprise.yml` template in production
  directory to install an Enterprise backend server.
* The old `template` directory has been replaced with a
  dedicated `production` directory, and templates are now provided as
  single files with the `.template` suffix instead. These should be
  copied to their non-`.template` location before being used. The `run`
  script should no longer be copied, and if it already exists in the
  `production` directory before merging this change, it should be
  removed before attempting to merge or rebase.
* The `prod.yml` file has been moved into a `config`
  subfolder. Users with downstream repositories need to move their
  `prod.yml` as well.
* Enable tenantadm as an Enterprise release component.
* Enable tenantadm as an Enterprise release component.
* Fix issue when demo script exists abruptly on user request
  for logs. The issue only showed up when the folder name contained "-"
  or "." characters.
* Upgrade deployments to 1.8.0b1.
* Upgrade deployments-enterprise to 1.8.0b1.
* Upgrade deviceauth to 2.1.0b1.
* Upgrade gui to 2.2.0b1.
* Upgrade mender to 2.1.1.
* Upgrade mender-artifact to 3.2.0b1.
* Upgrade mender-conductor to 1.5.0b1.
* Upgrade mender-conductor-enterprise to 1.5.0b1.
* Upgrade tenantadm to 1.0.0b1.
* Upgrade useradm to 1.9.0b1.
* Upgrade useradm-enterprise to 1.9.0b1.

#### mender (2.1.1)

New changes in mender since 2.1.0:

* module/single-file: fix rollback state by correctly defining filename
* Check for -f option in stat command
* Set hard limit(10) for client update status report retries
  This fixes an issue where the maxSendingAttemps in
  updateReportRetry state could be set real high, since it is calculated
  as UpdatePollIntervalSeconds / RetryPollIntervalSeconds. This adds a
  hard upper limit of 10 retries for the client in any case.
  ([MEN-2676](https://tracker.mender.io/browse/MEN-2676))

#### mender-artifact (3.2.0)

New changes in mender-artifact since 3.1.0:

* 'mender-artifact cp' now requires '-' in order to read stdin
  ([MEN-2745](https://tracker.mender.io/browse/MEN-2745))
* Fix error where files larger than the buffer used by
  io.Copy() was not buffered when mender-artifact cp read from stdin.
  This means that now, ``` mender-artfact cp - mender.artifact:/in/img/path```
  will successfully copy larger files.
* fix erroneously report of "-dirty" in the version
  string. ([MEN-2800](https://tracker.mender.io/browse/MEN-2800))
* Fix build-contained Makefile: image was missing make install
* Update the type-info documentation in the version 3 artifact format
  This commit updates the description of the values allowed in the type-info
  headers in the version 3 of the artifact format. Formerly only the key
  `rootfs-image-checksum` was allowed, while now, any key is allowed, with
  the only allowed value types being string, or array of strings.
* Allow `--compression` to be specified after command.
  This allows it to be appended to the command, which makes it usable
  with `--` style arguments to Update Module Artifact generators.
* Enable typeinfo artifact-depends/provides string and []string values
  Previously the artifact-depends key in the type-info header was restricted
  to contain a single key `rootfs-image-checksum`. This restriction has now
  been lifted, and the key can now contain arbitrary string, and []string values.
* Fix: mender-artifact modify did not clean up the
  temp-files created
  ([MEN-2758](https://tracker.mender.io/browse/MEN-2758))
* Mender-Artifact format version 1 is hereby no longer supported,
  and neither reading or writing the version 1 of the format is no longer
  supported. Please move to using a newer version.
  ([MEN-2156](https://tracker.mender.io/browse/MEN-2156))
* mender-artifact will now fail to validate a signed Artifact
  if no validation key is specified. No behaviour change for unsigned
  Artifacts. ([MEN-2802](https://tracker.mender.io/browse/MEN-2802))

#### mender-conductor (1.5.0)

New changes in mender-conductor since 1.4.0:

* update conductor from 2.2.0 to 2.11.0; fix configuration
* startup script modified
* copy default configuration into the image

#### mender-conductor-enterprise (1.5.0)

New changes in mender-conductor-enterprise since 1.4.0:

* update task configs to work with conductor 2.11.0
* fixing U+2014 'EM DASH' character
  ([MC-1016](https://tracker.mender.io/browse/MC-1016))


## mender-binary-delta 1.0.0

_Released 10.16.2019_


## meta-mender warrior-v2019.10

_Released 10.10.2019_

### Statistics

A total of 2540 lines added, 1428 removed (delta 1112)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 74 (46.8%) |
| Lluis Campos | 27 (17.1%) |
| Drew Moseley | 18 (11.4%) |
| Mirza Krak | 15 (9.5%) |
| Ole Petter Orhagen | 7 (4.4%) |
| Pierre-Jean Texier | 5 (3.2%) |
| Paul Barker | 3 (1.9%) |
| Dell Green | 2 (1.3%) |
| Dan Walkes | 1 (0.6%) |
| Bryan Matthews | 1 (0.6%) |

| Developers with the most changed lines | |
|---|---|
| Kristian Amlie | 1898 (58.0%) |
| Drew Moseley | 333 (10.2%) |
| Mirza Krak | 317 (9.7%) |
| Ole Petter Orhagen | 282 (8.6%) |
| Lluis Campos | 273 (8.3%) |
| Tim Froehlich | 46 (1.4%) |
| Dell Green | 43 (1.3%) |
| Dan Walkes | 40 (1.2%) |
| Pierre-Jean Texier | 14 (0.4%) |
| Bryan Matthews | 9 (0.3%) |

| Developers with the most signoffs (total 6) | |
|---|---|
| Kristian Amlie | 3 (50.0%) |
| Drew Moseley | 2 (33.3%) |
| Mirza Krak | 1 (16.7%) |

| Developers with the most report credits (total 2) | |
|---|---|
| Drew Moseley | 1 (50.0%) |
| Denis Mosolov | 1 (50.0%) |

| Developers who gave the most report credits (total 2) | |
|---|---|
| Kristian Amlie | 2 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 141 (89.2%) |
| KONCEPTO | 5 (3.2%) |
| Beta Five Ltd | 3 (1.9%) |
| Ideaworks Ltd | 2 (1.3%) |
| Konsulko Group | 1 (0.6%) |
| GreenEggs AB | 1 (0.6%) |
| manuel@linux-home.at | 1 (0.6%) |
| Arch Systems Inc. | 1 (0.6%) |
| Trellis-Logic | 1 (0.6%) |
| Reach Technologies Inc | 1 (0.6%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 3103 (94.8%) |
| Arch Systems Inc. | 46 (1.4%) |
| Ideaworks Ltd | 43 (1.3%) |
| Trellis-Logic | 40 (1.2%) |
| KONCEPTO | 14 (0.4%) |
| Reach Technologies Inc | 9 (0.3%) |
| Beta Five Ltd | 8 (0.2%) |
| Konsulko Group | 8 (0.2%) |
| GreenEggs AB | 1 (0.0%) |
| manuel@linux-home.at | 1 (0.0%) |

| Employers with the most signoffs (total 6) | |
|---|---|
| Northern.tech | 6 (100.0%) |

| Employers with the most hackers (total 15) | |
|---|---|
| Northern.tech | 5 (33.3%) |
| Arch Systems Inc. | 1 (6.7%) |
| Ideaworks Ltd | 1 (6.7%) |
| Trellis-Logic | 1 (6.7%) |
| KONCEPTO | 1 (6.7%) |
| Reach Technologies Inc | 1 (6.7%) |
| Beta Five Ltd | 1 (6.7%) |
| Konsulko Group | 1 (6.7%) |
| GreenEggs AB | 1 (6.7%) |
| manuel@linux-home.at | 1 (6.7%) |

### Changelogs

#### meta-mender (warrior-v2019.10)

New changes in meta-mender since thud-v2019.09:

* part-images: add missing u-boot:deploy dependency for ARM
* Add mender 1.6.1 and 1.7.0 recipes.
* Add mender-artifact 2.3.1 and 2.4.0 recipes.
* Remove unsupported mender 1.5.x series.
* Fix data directory not being empty on rootfs.
  ([MEN-2290](https://tracker.mender.io/browse/MEN-2290))
* Add grub-mender-grubenv 1.2.1 recipe.
* Fix grub-editenv invocation on platforms where it is called
  grub2-editenv.
* Add grub-mender-grubenv 1.3.0 recipe.
* Add support for initramfs when booting using GRUB.
* mender-helpers.bbclass: Add NVMe support
* Set inventory poll interval default to 8h
  ([MEN-2214](https://tracker.mender.io/browse/MEN-2214))
* mender artifact bbclass image name override variable added.
  ([MEN-2333](https://tracker.mender.io/browse/MEN-2333))
* grub: ensure "test" module is builtin
* Added bitbake variable to add optional swap partition
  ([MEN-2361](https://tracker.mender.io/browse/MEN-2361))
* Start using Git SHA based grub-mender-grubenv versions.
* Adapt to new flags in mender-artifact-3.0.0.
* Some core update modules can now be installed by adding
  `modules` to the `PACKAGECONFIG` variable of `mender`. They are
  included by default when using the meta-mender-demo layer.
  ([MEN-2383](https://tracker.mender.io/browse/MEN-2383))
* Install `mender-data-dir.service` to create `/data/mender` directory.
* Extended MENDER_DATA_PART_FSTYPE to allow it to be used to
  specify the filesystem to be generated. Added support to build the data
  partition as btrfs, and for setting mkfs and fstab options
* Change variable to access ubi dataimg, points now to the symlink to prevent yocto rebuild error when timestamp/name of ubimg have changed
* linux-raspberrypi-rt: Add mender settings for the PREEMPT_RT kernel.
* Add mender-2.0.0b1 and mender-artifact-3.0.0b1.
* Add new liblzma dependency for the client.
* Add missing build dep on "xz" in Mender Artifact recipes for
  3.0.x versions
* Fix error message `Incorrect Usage: flag provided but not defined: -f`
* Fix mender 2.0.x and mender-artifact 3.0.x recipes to use the
  correct branches when fetching the source.
* mender: Do not exclude missing directories.
* Upgrade default state script version to version 3.
* Add recipe for mender-2.0.0 and mender-artifact-3.0.0.
* Enable mender v2 and mender-artifact v3 by default.
* Add recipes for mender-1.7.1 and mender-artifact-2.4.1.
* Fix build failing in do_image_ubimg task
* Demo images now include Yocto LSB package.
  ([MEN-2421](https://tracker.mender.io/browse/MEN-2421))
* grub-mender-grubenv: Fix broken 'debug-pause' `PACKAGECONFIG`.
* QEMU: Add inventory script for Docker IP and open port 80.
  ([MEN-2574](https://tracker.mender.io/browse/MEN-2574))
* u-boot-mender: Add define for MENDER_STORAGE_DEVICE
* mender: Add support for a bootimg FSTYPE.
* This new define is to allow builds when no dtb is produced or the dtb is
* Remap port 85 on host to 85 in qemu
* Ensure that artifact and partition images' checksums are equal.
  ([MEN-2597](https://tracker.mender.io/browse/MEN-2597))
* Add recipes for mender 2.0.1 and mender-artifact 3.0.1
* mender: Setup Live installer with HDDIMG
* rpi: Fix several assignment bugs regarding `MENDER_BOOTLOADER_DEFAULT`.
* mender-systemd: Maintain persistent machine-id across updates.
* Add MENDER_UBOOT_CONFIG_SYS_MMC_ENV_PART variable which can
  be used to specify MMC partitions other than the user partition like
  mmcblk0boot0 and mmcblk0boot1 for u-boot environment storage.
* grub-mender-grubenv: Setup debug option to drop to grub prompt.
* mender: Scan for devices with the live installer
* Add mender 2.1.0b1 and mender-artifact 3.1.0b1 recipes.
  Part of Mender 2.1.0 Beta release.
* Remove outdated mender-1.6.x and mender-artifact-2.3.x recipes.
* layer.conf: set high layer priority
  Set a high layer prio to ensure that meta-mender-demo addons (e.g psplash)
  are always prioritized above the depended layers (e.g meta-boundary).
* Add meta-mender-commercial layer.
  This will host our mender-binary-delta Update Module.
* Update recipe for mender-binary-delta pre-release v0.1.1
* u-boot-fw-utils: set PACKAGE_ARCH as MACHINE_ARCH
* example-state-scripts: use show-artifact instead of parsing file
* Fix incorrect boot partition type for EFI boot partitions.
* Fix initramfs builds when using meta-mender layer
* Fix "set_image_size" errors when large files are installed
  in /data directory (staging area for data partition filesystem image)
* Add mender-2.1.0 and mender-artifact-3.1.0.
* Enable dynamic resizing of the data partition
  Enable dynamic resize of the data partition on first boot. Meaning that it will
  grow the mounted filesystem to full size of the underlying block device. This is
  done through enabling systemd's growfs feature. Hereforth the feature is enabled
  by default when inheriting from 'mender-full'. The feature can be disabled using
  MENDER_FEATURES_DISABLE_append = " mender-growfs-data".
  Updated commit message:
  ([MEN-2337](https://tracker.mender.io/browse/MEN-2337))
* `FILESEXTRAPATHS_prepend_pn-mender-binary-delta` now needs
  to point to the folder containing `arm`, `aarch64` and `x86_64`, not the folder
  containing the binary.
* meta-mender layers updated to Yocto warrior
* Splits the mender.conf configuration file into a transient
  configuration /etc/mender/mender.conf and a persistent congiguration in
  /data/mender/mender.conf. This split is enabled by default, and it can
  be opt-out by adding `PACKAGECONFIG_remove = "split-mender-config"` to
  local.conf. ([MEN-2757](https://tracker.mender.io/browse/MEN-2757))
* Add a new recipe mender-migrate-configuration to ease the
  migration of devices with single mender.conf to the new setup of split
  configuration files. To build an updgrade for such device, add the
  recipe with `IMAGE_INSTALL_append = " mender-migrate-configuration"`,
  disable the split feature (for this update only) with
  `PACKAGECONFIG_remove = " split-mender-config"`, and specify which
  parameters to migrate (at least the partition parameters) with
  `MENDER_PERSISTENT_CONFIGURATION_VARS = "RootfsPartA RootfsPartB"`.
  ([MEN-2757](https://tracker.mender.io/browse/MEN-2757))
* Fix issue where U-boot is not able to find a valid DTB on Raspberry Pi boards
* add support for Raspberry Pi 4
* Removes the tests covering Mender-Artifact version 1.
  ([MEN-2156](https://tracker.mender.io/browse/MEN-2156))
* Add mender 2.1.1 and mender-artifact 3.2.0b1 recipes.
* Update recipe for mender-binary-delta beta release v1.0.0b1


## mender-convert 1.2.0

_Released 09.17.2019_

### Statistics

A total of 268 lines added, 100 removed (delta 168)

| Developers with the most changesets | |
|---|---|
| Mirza Krak | 10 (32.3%) |
| Lluis Campos | 9 (29.0%) |
| Simon Ensslen | 3 (9.7%) |
| Simon Gamma | 3 (9.7%) |
| Manuel Zedel | 2 (6.5%) |
| Eystein Måløy Stenberg | 2 (6.5%) |
| Mario Kozjak | 1 (3.2%) |
| Marek Belisko | 1 (3.2%) |

| Developers with the most changed lines | |
|---|---|
| Mirza Krak | 199 (65.5%) |
| Manuel Zedel | 36 (11.8%) |
| Lluis Campos | 35 (11.5%) |
| Simon Ensslen | 15 (4.9%) |
| Eystein Måløy Stenberg | 10 (3.3%) |
| Simon Gamma | 7 (2.3%) |
| Mario Kozjak | 1 (0.3%) |
| Marek Belisko | 1 (0.3%) |

| Developers with the most signoffs (total 1) | |
|---|---|
| Yevgeniy Nurseitov | 1 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 23 (74.2%) |
| Griesser AG | 3 (9.7%) |
| github@survive.ch | 3 (9.7%) |
| kozjakm1@gmail.com | 1 (3.2%) |
| open-nandra | 1 (3.2%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 280 (92.1%) |
| Griesser AG | 15 (4.9%) |
| github@survive.ch | 7 (2.3%) |
| kozjakm1@gmail.com | 1 (0.3%) |
| open-nandra | 1 (0.3%) |

| Employers with the most signoffs (total 1) | |
|---|---|
| enurseitov@gmail.com | 1 (100.0%) |

| Employers with the most hackers (total 8) | |
|---|---|
| Northern.tech | 4 (50.0%) |
| Griesser AG | 1 (12.5%) |
| github@survive.ch | 1 (12.5%) |
| kozjakm1@gmail.com | 1 (12.5%) |
| open-nandra | 1 (12.5%) |

### Changelogs

#### mender-convert (1.2.0)

New changes in mender-convert since 1.2.0b1:

* Update mender-convert to use Mender final release v2.1.0

New changes in mender-convert since 1.1.1:

* Expand existing environment '$PATH' variable instead of replacing it
* Use same environment '$PATH' variable when using sudo
* Fail the docker build when mandatory build-arg 'mender_client_version' is not set.
* Update Dockerfile to use latest stable mender-artifact, v2.4.0
* Use mender-artfact v3. Requires rebuild of device-image-shell container.
* Use LZMA for smaller Artifact size (but slower generation).
* Update mender-convert to use final Mender v2.0 release
* shrink expanded rootfs when running "from_raw_disk_image"
* rpi: Bump u-boot version to fix booting on rpi0w after raspi-config resize partition
  ([MEN-2436](https://tracker.mender.io/browse/MEN-2436))
* Instruct U-Boot to be able to boot either a compressed or an uncompressed kernel. This is very useful e.g. when switching from Debian (Raspbian) created using mender-convert to a Yocto based environment that does not compress the Kernel by default.
* Implement feature (mender-convert needs option to build without server)
  ([MEN-2590](https://tracker.mender.io/browse/MEN-2590))
* Since mender-convert now automatically resizes the input image, there is an additional step that is executed.
* parameterize target architecture when creating Docker container
* Update mender-convert to for Mender v2.0.1 release
* Support for RockPro64 board
* Fix console not being available on HDMI on Raspberry Pi in Raspbian Buster.
  ([MEN-2673](https://tracker.mender.io/browse/MEN-2673))
* only install servert.crt.demo if --demo-host-ip/-i is set
* add ServerCertificate entry in mender.conf if servert.crt was installed
  ([MEN-2640](https://tracker.mender.io/browse/MEN-2640))
* install /etc/mender/script/version file
* Update mender-convert to use Mender beta release v2.1.0b1


## meta-mender thud-v2019.09

_Released 09.17.2019_

### Statistics

A total of 224 lines added, 78 removed (delta 146)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 5 (55.6%) |
| Lluis Campos | 3 (33.3%) |
| Pierre-Jean Texier | 1 (11.1%) |

| Developers with the most changed lines | |
|---|---|
| Kristian Amlie | 159 (71.0%) |
| Lluis Campos | 63 (28.1%) |
| Pierre-Jean Texier | 2 (0.9%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 8 (88.9%) |
| KONCEPTO | 1 (11.1%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 222 (99.1%) |
| KONCEPTO | 2 (0.9%) |

| Employers with the most hackers (total 3) | |
|---|---|
| Northern.tech | 2 (66.7%) |
| KONCEPTO | 1 (33.3%) |

### Changelogs

#### meta-mender (thud-v2019.09)

New changes in meta-mender since thud-v2019.08:

* Add mender-2.1.0 and mender-artifact-3.1.0.
* `FILESEXTRAPATHS_prepend_pn-mender-binary-delta` now needs
  to point to the folder containing `armhf` and `x86_64`, not the folder
  containing the binary.
  ([MEN-2702](https://tracker.mender.io/browse/MEN-2702))
* u-boot-fw-utils: set PACKAGE_ARCH as MACHINE_ARCH
* Update recipe for mender-binary-delta pre-release v0.1.1
* Add meta-mender-commercial layer.
  This will host our mender-binary-delta Update Module.


## Mender 2.1.0

_Released 09.16.2019_

### Statistics

A total of 12953 lines added, 8330 removed (delta 4623)

| Developers with the most changesets | |
|---|---|
| Manuel Zedel | 285 (57.2%) |
| Kristian Amlie | 72 (14.5%) |
| Lluis Campos | 41 (8.2%) |
| Ole Petter Orhagen | 27 (5.4%) |
| Michael Clelland | 26 (5.2%) |
| Marcin Chalczynski | 15 (3.0%) |
| Peter Grzybowski | 7 (1.4%) |
| Eystein Måløy Stenberg | 5 (1.0%) |
| Aleksei Vegner | 5 (1.0%) |
| Mirza Krak | 4 (0.8%) |

| Developers with the most changed lines | |
|---|---|
| Manuel Zedel | 8905 (57.5%) |
| Kristian Amlie | 2093 (13.5%) |
| Ole Petter Orhagen | 1478 (9.5%) |
| Michael Clelland | 1358 (8.8%) |
| Lluis Campos | 849 (5.5%) |
| Marcin Chalczynski | 344 (2.2%) |
| Mirza Krak | 179 (1.2%) |
| Aleksei Vegner | 66 (0.4%) |
| Oleksandr Miliukov | 63 (0.4%) |
| Andreas Henriksson | 49 (0.3%) |

| Developers with the most lines removed | |
|---|---|
| Michael Clelland | 278 (3.3%) |
| Krzysztof Jaskiewicz | 24 (0.3%) |
| Aleksei Vegner | 7 (0.1%) |
| Dirk Siegmund | 2 (0.0%) |

| Developers with the most signoffs (total 3) | |
|---|---|
| Ole Petter Orhagen | 2 (66.7%) |
| Kristian Amlie | 1 (33.3%) |

| Developers with the most report credits (total 1) | |
|---|---|
| Cedric Veilleux | 1 (100.0%) |

| Developers who gave the most report credits (total 1) | |
|---|---|
| Kristian Amlie | 1 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 469 (94.2%) |
| RnDity | 18 (3.6%) |
| alexey.vegner@yandex.ru | 5 (1.0%) |
| andreas@fatal.se | 3 (0.6%) |
| Systems Engineering & Assessment Ltd | 1 (0.2%) |
| M-Way Solutions | 1 (0.2%) |
| siegmund@beckmann-gmbh.de | 1 (0.2%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 14973 (96.7%) |
| RnDity | 371 (2.4%) |
| alexey.vegner@yandex.ru | 66 (0.4%) |
| andreas@fatal.se | 49 (0.3%) |
| Systems Engineering & Assessment Ltd | 12 (0.1%) |
| siegmund@beckmann-gmbh.de | 9 (0.1%) |
| M-Way Solutions | 4 (0.0%) |

| Employers with the most signoffs (total 3) | |
|---|---|
| Northern.tech | 3 (100.0%) |

| Employers with the most hackers (total 16) | |
|---|---|
| Northern.tech | 9 (56.2%) |
| RnDity | 2 (12.5%) |
| alexey.vegner@yandex.ru | 1 (6.2%) |
| andreas@fatal.se | 1 (6.2%) |
| Systems Engineering & Assessment Ltd | 1 (6.2%) |
| siegmund@beckmann-gmbh.de | 1 (6.2%) |
| M-Way Solutions | 1 (6.2%) |


### Changelogs

#### deployments (1.7.1)

New changes in deployments since 1.7.0:

* Fix "unexpected EOF" errors when the source of the artifact
  is a slow network stream.
* Fix spurious upload errors due to wrong EOF handling.
* Fix inability to resume partial migration.

#### gui (2.1.0)

New changes in gui since 2.1.0b1:

* added 2fa login functionality
* onboarding: Don't require Enter after copy/paste operation.
* added copyable version information tooltip in left navbar
* fixed an issue that could lead to help tooltips sometimes not showing
* fixed a problem that could cause a crash of the device lists
* onboarding: Don't require Enter after copy/paste operation.
* Fix installation of mender-artifact missing sudo in onboarding.
* Fix sudo password messing up commands in onboarding.
  ([MEN-2700](https://tracker.mender.io/browse/MEN-2700))

New changes in gui since 2.0.1:

* Device list times no longer change on expansion
  ([MEN-2366](https://tracker.mender.io/browse/MEN-2366))
* Fix onboarding install instructions for HM and demo server
  ([MEN-2571](https://tracker.mender.io/browse/MEN-2571))
* newly uploaded releases are now autoselected to ease deployment
* total artifact size in a release is now shown instead of signing state
* Updated Help pages with new structure and content for Update Modules
* show total artifact size in ui + clarify uncompressed size
* long device inventory texts are no longer cut off + visible on hover

#### integration (2.1.0)

New changes in integration since 2.1.0b1:

* Fix error: `No such container: integration-2.1.0b1_mender-useradm_1`
* Upgrade deployments to 1.7.1.
* Upgrade gui to 2.1.0.
* Upgrade mender to 2.1.0.
* Upgrade mender-artifact to 3.1.0.
* Upgrade mender-cli to 1.2.0.
* Upgrade mender-conductor to 1.4.0.
* Upgrade mender-conductor-enterprise to 1.4.0.
* Upgrade useradm to 1.8.0.

New changes in integration since 2.0.1:

* Disable virtual QEMU client by default.
  A client can be launched by giving the `--client` argument to the
  `demo` script, either at the same time as launching the servers, or
  later after the servers have already been launched.
  ([MEN-2363](https://tracker.mender.io/browse/MEN-2363))
* Automate upload of demo application artifact in demo server
  ([MEN-2433](https://tracker.mender.io/browse/MEN-2433))
* Fix Mender version not showing up in production.
  ([MEN-2690](https://tracker.mender.io/browse/MEN-2690))
* Allow demo script to run with existing demo user
  ([MEN-2682](https://tracker.mender.io/browse/MEN-2682))
* demo: Fix broken detection with no arguments and `--help` argument.
* Fixes for demo wget to work on Alpine Linux using latest download
  ([MEN-2654](https://tracker.mender.io/browse/MEN-2654))
* Adding deployments enterprise _REV
  ([MEN-2652](https://tracker.mender.io/browse/MEN-2652))
* Upgrade deployments to 1.7.1b1.
* Upgrade gui to 2.1.0b1.
* Upgrade mender to 2.1.0b1.
* Upgrade mender-artifact to 3.1.0b1.
* Upgrade mender-cli to 1.2.0b1.
* Upgrade mender-conductor to 1.4.0b1.
* Upgrade mender-conductor-enterprise to 1.4.0b1.
* Upgrade useradm to 1.8.0b1.
* Unify demo scripts by removing all except the one called 'demo'.
  ([MEN-2571](https://tracker.mender.io/browse/MEN-2571))

#### mender (2.1.0)

New changes in mender since 2.0.1:

* rootfs-image-v2: Make sure to follow the spec regarding `stream-next`.
  We should to read the final empty entry to make sure the client does
  not block.
* Restore error code 2 behavior when there is nothing to commit.
* Fix read error masking in installer.chunkedCopy(...) func
* Update vendored dependencies for client.
* When set, HTTP proxy settings in http_proxy/https_proxy environment variables are respected now.
* module-artifact-gen: Fix inability to specify more than one device_type.
* Make all errors checked or explicitly ignored
  All possible errors must be checked across all code base.
  If an error is intentionally ignored it should be done explicitly.
* add state-scripts example scripts to wait for network connectivity
  before trying to connect to the Mender server.
  ([MEN-2457](https://tracker.mender.io/browse/MEN-2457))
* Artifact gen: Support argument passthrough to `mender-artifact`.
  Use `--` to signal that remaining arguments should be passed directly
  to `mender-artifact`.
* Make the device type file location configurable
* Make channel receiving user signals buffered
  The commit fixes improper usage of signal.Notify(...) func from Go stdlib.
  A channel must be buffered to properly receive signals:
  https://golang.org/pkg/os/signal/#Notify
  Also there is no need to reallocate channel and defer signal.Stop(...)
  each time user signal is received. Thus less resources are used.
* standalone: Fix artifact committing not working after upgrading from 1.x.
  ([MEN-2465](https://tracker.mender.io/browse/MEN-2465))
* Print warning on an invalid server certificate.
  ([MEN-2378](https://tracker.mender.io/browse/MEN-2378))
* add state-script example to preserve ssh keys accross updates
  ([MEN-2457](https://tracker.mender.io/browse/MEN-2457))
* Fix `/bin/lsb_release` not being picked up by inventory script.
* Fix misspells in comments and error messages
* Make sure ARM64 is included in bootloader integration inventory.
* Added example to retain systemd network configuration.
* single-file module: Make sure permissions are preserved.
  Also make sure that backup preserves permissions.
* add state-script example to utilize dbus to broadcast
  Mender states ([MEN-2457](https://tracker.mender.io/browse/MEN-2457))
* Provide command line interface to force inventory update.
  ([MEN-2131](https://tracker.mender.io/browse/MEN-2131))

#### mender-artifact (3.1.0)

New changes in mender-artifact since 3.0.1:

* Fix non-rootfs Artifacts being destroyed when signing them.
  ([MEN-2573](https://tracker.mender.io/browse/MEN-2573))
* The mender-artifact tool now checks whether the required
  external binaries can be found on the system, and if not, returns an appropriate
  error message.
  ([MEN-2180](https://tracker.mender.io/browse/MEN-2180))
* Fix name modify command for rootfs-image Artifacts
  ([MEN-2488](https://tracker.mender.io/browse/MEN-2488))
* Remove documentation for artifact format v1, which is now unsupported.
* `mender-convert` modify for Update Module Artifacts will only
  work for options that change the headers or meta-data of the Artifact;
  curently only the Artifact name.
  ([MEN-2487](https://tracker.mender.io/browse/MEN-2487))
* Enable signing of artifacts larger than 1MiB
  ([MEN-2631](https://tracker.mender.io/browse/MEN-2631))
* Fix "unexpected EOF" errors when the source of the artifact
  is a slow network stream.
* Fix spurious upload errors due to wrong EOF handling.
* checking if fsck is on path and returing error if not.
* Add `dump` command to mender-artifact.
  It takes an artifact as input, some optional dumping directories, and
  writes the various raw files from the artifact into those directories.
  The parameter `--print-cmdline` can be used to generate a command line
  which can be used to recreate the same artifact from the dumped files.
  ([MEN-2580](https://tracker.mender.io/browse/MEN-2580))
* Added a build step for macOS to the Travis build.
* `mender-artifact modify` does not support anymore signing the
  Artifact after the modification. Use `mender-convert sign` after the
  modification to sign the Artifact.
  ([MEN-2486](https://tracker.mender.io/browse/MEN-2486))

#### mender-cli (1.2.0)

New changes in mender-cli since 1.1.0:

* Store login token in XDG Basedir Spec Cache-directory
  ([MEN-2387](https://tracker.mender.io/browse/MEN-2387))

#### mender-conductor (1.4.0)

New changes in mender-conductor since 1.3.1:

* upgrading python client to the latest version (2.12.4)
* Timestamp added to send_email worker
* email-sender: fixed bug with wrong state reporting

#### mender-conductor-enterprise (1.4.0)

New changes in mender-conductor-enterprise since 1.3.1:

* MC-637 updating settings for prepare_org_welcome_email conductor task
* upgrading python client to the latest version (2.12.4)

#### useradm (1.8.0)

New changes in useradm since 1.7.0:

* unauthorized for empty username logins
  ([MEN-2375](https://tracker.mender.io/browse/MEN-2375))


## meta-mender rocko-v2019.08

_Released 09.02.2019_

### Statistics

A total of 89 lines added, 121 removed (delta -32)

| Developers with the most changesets | |
|---|---|
| Lluis Campos | 8 (44.4%) |
| Kristian Amlie | 5 (27.8%) |
| Drew Moseley | 3 (16.7%) |
| Ole Petter Orhagen | 1 (5.6%) |
| Jonas Norling | 1 (5.6%) |

| Developers with the most changed lines | |
|---|---|
| Lluis Campos | 116 (63.7%) |
| Kristian Amlie | 51 (28.0%) |
| Drew Moseley | 13 (7.1%) |
| Ole Petter Orhagen | 1 (0.5%) |
| Jonas Norling | 1 (0.5%) |

| Developers with the most lines removed | |
|---|---|
| Lluis Campos | 71 (58.7%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 17 (94.4%) |
| GreenEggs AB | 1 (5.6%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 181 (99.5%) |
| GreenEggs AB | 1 (0.5%) |

| Employers with the most hackers (total 5) | |
|---|---|
| Northern.tech | 4 (80.0%) |
| GreenEggs AB | 1 (20.0%) |

### Changelogs

#### meta-mender (rocko-v2019.08)

New changes in meta-mender since rocko-v2019.05:

* Fix build failing in do_image_ubimg task
* Demo images now include Yocto LSB package.
  ([MEN-2421](https://tracker.mender.io/browse/MEN-2421))
* QEMU: Add inventory script for Docker IP and open port 80.
  ([MEN-2574](https://tracker.mender.io/browse/MEN-2574))
* u-boot-mender: Add define for MENDER_STORAGE_DEVICE
* Add recipes for mender 2.0.1 and mender-artifact 3.0.1
* Remap port 85 on host to 85 in qemu
* Add mender 2.1.0b1 and mender-artifact 3.1.0b1 recipes.
  Part of Mender 2.1.0 Beta release.


## meta-mender sumo-v2019.08

_Released 09.02.2019_

### Statistics

A total of 93 lines added, 124 removed (delta -31)

| Developers with the most changesets | |
|---|---|
| Lluis Campos | 7 (36.8%) |
| Kristian Amlie | 6 (31.6%) |
| Drew Moseley | 4 (21.1%) |
| Ole Petter Orhagen | 1 (5.3%) |
| Jonas Norling | 1 (5.3%) |

| Developers with the most changed lines | |
|---|---|
| Lluis Campos | 111 (59.7%) |
| Kristian Amlie | 57 (30.6%) |
| Drew Moseley | 16 (8.6%) |
| Ole Petter Orhagen | 1 (0.5%) |
| Jonas Norling | 1 (0.5%) |

| Developers with the most lines removed | |
|---|---|
| Lluis Campos | 71 (57.3%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 18 (94.7%) |
| GreenEggs AB | 1 (5.3%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 185 (99.5%) |
| GreenEggs AB | 1 (0.5%) |

| Employers with the most hackers (total 5) | |
|---|---|
| Northern.tech | 4 (80.0%) |
| GreenEggs AB | 1 (20.0%) |

### Changelogs

#### meta-mender (sumo-v2019.08)

New changes in meta-mender since sumo-v2019.05:

* Fix build failing in do_image_ubimg task
* Demo images now include Yocto LSB package.
  ([MEN-2421](https://tracker.mender.io/browse/MEN-2421))
* QEMU: Add inventory script for Docker IP and open port 80.
  ([MEN-2574](https://tracker.mender.io/browse/MEN-2574))
* u-boot-mender: Add define for MENDER_STORAGE_DEVICE
* Add recipes for mender 2.0.1 and mender-artifact 3.0.1
* Remap port 85 on host to 85 in qemu
* Add mender 2.1.0b1 and mender-artifact 3.1.0b1 recipes.
  Part of Mender 2.1.0 Beta release.


## meta-mender thud-v2019.08

_Released 08.13.2019_

### Statistics

A total of 125 lines added, 109 removed (delta 16)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 6 (42.9%) |
| Lluis Campos | 3 (21.4%) |
| Drew Moseley | 2 (14.3%) |
| Paul Barker | 2 (14.3%) |
| Ole Petter Orhagen | 1 (7.1%) |

| Developers with the most changed lines | |
|---|---|
| Drew Moseley | 87 (42.6%) |
| Lluis Campos | 85 (41.7%) |
| Kristian Amlie | 27 (13.2%) |
| Paul Barker | 4 (2.0%) |
| Ole Petter Orhagen | 1 (0.5%) |

| Developers with the most lines removed | |
|---|---|
| Lluis Campos | 79 (72.5%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 12 (85.7%) |
| Beta Five Ltd | 2 (14.3%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 200 (98.0%) |
| Beta Five Ltd | 4 (2.0%) |

| Employers with the most hackers (total 5) | |
|---|---|
| Northern.tech | 4 (80.0%) |
| Beta Five Ltd | 1 (20.0%) |

### Changelogs

#### meta-mender (thud-v2019.08)

New changes in meta-mender since thud-v2019.07:

* Add mender 2.1.0b1 and mender-artifact 3.1.0b1 recipes.
  Part of Mender 2.1.0 Beta release.
* mender: Setup Live installer with HDDIMG
* rpi: Fix several assignment bugs regarding `MENDER_BOOTLOADER_DEFAULT`.
* Remap port 85 on host to 85 in qemu


## mender-convert 1.1.1

_Released 07.01.2019_

### Statistics

A total of 26 lines added, 23 removed (delta 3)

| Developers with the most changesets | |
|---|---|
| Mirza Krak | 2 (40.0%) |
| Lluis Campos | 1 (20.0%) |
| Adam Podogrocki | 1 (20.0%) |
| Marek Belisko | 1 (20.0%) |

| Developers with the most changed lines | |
|---|---|
| Mirza Krak | 19 (47.5%) |
| Adam Podogrocki | 17 (42.5%) |
| Lluis Campos | 3 (7.5%) |
| Marek Belisko | 1 (2.5%) |

| Developers with the most lines removed | |
|---|---|
| Mirza Krak | 14 (60.9%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 3 (60.0%) |
| RnDity | 1 (20.0%) |
| open-nandra | 1 (20.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 22 (55.0%) |
| RnDity | 17 (42.5%) |
| open-nandra | 1 (2.5%) |

| Employers with the most hackers (total 4) | |
|---|---|
| Northern.tech | 2 (50.0%) |
| RnDity | 1 (25.0%) |
| open-nandra | 1 (25.0%) |


### Changelogs

#### mender-convert (1.1.1)

New changes in mender-convert since 1.1.0:

* rpi: Bump u-boot version to fix booting on rpi0w after raspi-config resize partition
  ([MEN-2436](https://tracker.mender.io/browse/MEN-2436))
* shrink expanded rootfs when running "from_raw_disk_image"
* Update mender-convert to for Mender v2.0.1 release


## meta-mender thud-v2019.07

_Released 07.01.2019_

### Statistics

A total of 64 lines added, 20 removed (delta 44)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 6 (46.2%) |
| Lluis Campos | 3 (23.1%) |
| Drew Moseley | 3 (23.1%) |
| Jonas Norling | 1 (7.7%) |

| Developers with the most changed lines | |
|---|---|
| Kristian Amlie | 52 (81.2%) |
| Lluis Campos | 6 (9.4%) |
| Drew Moseley | 5 (7.8%) |
| Jonas Norling | 1 (1.6%) |

| Developers with the most report credits (total 1) | |
|---|---|
| Drew Moseley | 1 (100.0%) |

| Developers who gave the most report credits (total 1) | |
|---|---|
| Kristian Amlie | 1 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 12 (92.3%) |
| GreenEggs AB | 1 (7.7%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 63 (98.4%) |
| GreenEggs AB | 1 (1.6%) |

| Employers with the most hackers (total 4) | |
|---|---|
| Northern.tech | 3 (75.0%) |
| GreenEggs AB | 1 (25.0%) |


### Changelogs

#### meta-mender (thud-v2019.07)

New changes in meta-mender since thud-v2019.05:

* Fix build failing in do_image_ubimg task
* Demo images now include Yocto LSB package.
  ([MEN-2421](https://tracker.mender.io/browse/MEN-2421))
* QEMU: Add inventory script for Docker IP and open port 80.
  ([MEN-2574](https://tracker.mender.io/browse/MEN-2574))
* grub-mender-grubenv: Fix broken 'debug-pause' `PACKAGECONFIG`.
* u-boot-mender: Add define for MENDER_STORAGE_DEVICE
* Add recipes for mender 2.0.1 and mender-artifact 3.0.1


## Mender 2.0.1

_Released 06.24.2019_

### Statistics

A total of 622 lines added, 284 removed (delta 338)

| Developers with the most changesets | |
|---|---|
| Manuel Zedel | 13 (48.1%) |
| Kristian Amlie | 8 (29.6%) |
| Michael Clelland | 2 (7.4%) |
| Oleksandr Miliukov | 2 (7.4%) |
| Eystein Måløy Stenberg | 1 (3.7%) |
| Lluis Campos | 1 (3.7%) |

| Developers with the most changed lines | |
|---|---|
| Kristian Amlie | 403 (60.0%) |
| Manuel Zedel | 185 (27.5%) |
| Oleksandr Miliukov | 61 (9.1%) |
| Lluis Campos | 13 (1.9%) |
| Michael Clelland | 6 (0.9%) |
| Eystein Måløy Stenberg | 4 (0.6%) |

| Developers with the most lines removed | |
|---|---|
| Michael Clelland | 2 (0.7%) |

| Developers with the most report credits (total 1) | |
|---|---|
| Cedric Veilleux | 1 (100.0%) |

| Developers who gave the most report credits (total 1) | |
|---|---|
| Kristian Amlie | 1 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 27 (100.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 672 (100.0%) |

| Employers with the most hackers (total 6) | |
|---|---|
| Northern.tech | 6 (100.0%) |


### Changelogs

#### gui (2.0.1)

New changes in gui since 2.0.0:

* long device inventory texts are no longer cut off + visible on hover
* updated dependencies
* Bugfix for innaccurate offline devices on dashboard
* Bugfix to ensure pending device checkboxes work as expected
* Prevented blank page on no result release search
  ([MEN-2572](https://tracker.mender.io/browse/MEN-2572))

#### integration (2.0.1)

New changes in integration since 2.0.0:

* Upgrade gui to 2.0.1.
* Upgrade mender to 2.0.1.
* Upgrade mender-artifact to 3.0.1.
* Upgrade mender-conductor to 1.3.1.
* Upgrade mender-conductor-enterprise to 1.3.1.

#### mender (2.0.1)

New changes in mender since 2.0.0:

* module-artifact-gen: Fix inability to specify more than one device_type.
* single-file module: Make sure permissions are preserved.
  Also make sure that backup preserves permissions.
* Artifact gen: Support argument passthrough to `mender-artifact`.
  Use `--` to signal that remaining arguments should be passed directly
  to `mender-artifact`.
* Restore error code 2 behavior when there is nothing to commit.

#### mender-artifact (3.0.1)

New changes in mender-artifact since 3.0.0:

* Fix non-rootfs Artifacts being destroyed when signing them.
  ([MEN-2573](https://tracker.mender.io/browse/MEN-2573))

#### mender-conductor (1.3.1)

New changes in mender-conductor since 1.3.0:

* Timestamp added to send_email worker
* email-sender: fixed bug with wrong state reporting


## meta-mender rocko-v2019.05

_Released 05.15.2019_

### Statistics

A total of 14 lines added, 12 removed (delta 2)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 2 (40.0%) |
| Mirza Krak | 1 (20.0%) |
| Ajith P Venugopal | 1 (20.0%) |
| Lluis Campos | 1 (20.0%) |

| Developers with the most changed lines | |
|---|---|
| Kristian Amlie | 9 (64.3%) |
| Ajith P Venugopal | 2 (14.3%) |
| Lluis Campos | 2 (14.3%) |
| Mirza Krak | 1 (7.1%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 4 (80.0%) |
| ajithpv@outlook.com | 1 (20.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 12 (85.7%) |
| ajithpv@outlook.com | 2 (14.3%) |

| Employers with the most hackers (total 4) | |
|---|---|
| Northern.tech | 3 (75.0%) |
| ajithpv@outlook.com | 1 (25.0%) |


### Changelogs

#### meta-mender (rocko-v2019.05)

New changes in meta-mender since rocko-v2019.04:

* Fix mender 2.0.x and mender-artifact 3.0.x recipes to use the
  correct branches when fetching the source.
* Add missing build dependency on "xz" in Mender Artifact recipe for 3.0.0b1 version
* Add recipes for mender-1.7.1 and mender-artifact-2.4.1.
* Add recipes for mender-2.0.0 and mender-artifact-3.0.0.
  Note that these recipes are not enabled by default in thud. If you
  want to use them, you have to add this to your build configuration:
  ```
  PREFERRED_VERSION_pn-mender = "2.%"
  PREFERRED_VERSION_pn-mender-artifact = "3.%"
  PREFERRED_VERSION_pn-mender-artifact-native = "3.%"
  ```
* Fix GRUB start-up on x86 by renaming "boot.efi" to "bootia32.efi"


## meta-mender sumo-v2019.05

_Released 05.15.2019_

### Statistics

A total of 13 lines added, 11 removed (delta 2)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 2 (50.0%) |
| Lluis Campos | 1 (25.0%) |
| Ajith P Venugopal | 1 (25.0%) |

| Developers with the most changed lines | |
|---|---|
| Kristian Amlie | 9 (69.2%) |
| Lluis Campos | 2 (15.4%) |
| Ajith P Venugopal | 2 (15.4%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 3 (75.0%) |
| ajithpv@outlook.com | 1 (25.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 11 (84.6%) |
| ajithpv@outlook.com | 2 (15.4%) |

| Employers with the most hackers (total 3) | |
|---|---|
| Northern.tech | 2 (66.7%) |
| ajithpv@outlook.com | 1 (33.3%) |


### Changelogs

#### meta-mender (sumo-v2019.05)

New changes in meta-mender since sumo-v2019.04:

* Add missing build dependency on "xz" in Mender Artifact recipe for 3.0.0b1 version
* Fix mender 2.0.x and mender-artifact 3.0.x recipes to use the
  correct branches when fetching the source.
* Add recipes for mender-1.7.1 and mender-artifact-2.4.1.
* Add recipes for mender-2.0.0 and mender-artifact-3.0.0.
  Note that these recipes are not enabled by default in thud. If you
  want to use them, you have to add this to your build configuration:
  ```
  PREFERRED_VERSION_pn-mender = "2.%"
  PREFERRED_VERSION_pn-mender-artifact = "3.%"
  PREFERRED_VERSION_pn-mender-artifact-native = "3.%"
  ```


## mender-convert 1.1.0

_Released 05.08.2019_

### Statistics

A total of 1512 lines added, 996 removed (delta 516)

| Developers with the most changesets | |
|---|---|
| Mirza Krak | 19 (27.5%) |
| Adam Podogrocki | 16 (23.2%) |
| Eystein Måløy Stenberg | 13 (18.8%) |
| Lluis Campos | 9 (13.0%) |
| Marek Belisko | 4 (5.8%) |
| Simon Gamma | 3 (4.3%) |
| Max Bruckner | 1 (1.4%) |
| Adrian Cuzman | 1 (1.4%) |
| Dominik Adamski | 1 (1.4%) |
| Mika Tuupola | 1 (1.4%) |

| Developers with the most changed lines | |
|---|---|
| Adam Podogrocki | 853 (48.8%) |
| Eystein Måløy Stenberg | 359 (20.5%) |
| Mirza Krak | 301 (17.2%) |
| Lluis Campos | 186 (10.6%) |
| Marek Belisko | 37 (2.1%) |
| Simon Gamma | 7 (0.4%) |
| Max Bruckner | 1 (0.1%) |
| Adrian Cuzman | 1 (0.1%) |
| Dominik Adamski | 1 (0.1%) |
| Mika Tuupola | 1 (0.1%) |

| Developers with the most lines removed | |
|---|---|
| Mirza Krak | 164 (16.5%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 41 (59.4%) |
| RnDity | 17 (24.6%) |
| open-nandra | 4 (5.8%) |
| github@survive.ch | 3 (4.3%) |
| max@maxbruckner.de | 1 (1.4%) |
| adriancuzman@gmail.com | 1 (1.4%) |
| tuupola@appelsiini.net | 1 (1.4%) |
| denismosolov@gmail.com | 1 (1.4%) |

| Top lines changed by employer | |
|---|---|
| RnDity | 854 (48.9%) |
| Northern.tech | 846 (48.4%) |
| open-nandra | 37 (2.1%) |
| github@survive.ch | 7 (0.4%) |
| max@maxbruckner.de | 1 (0.1%) |
| adriancuzman@gmail.com | 1 (0.1%) |
| tuupola@appelsiini.net | 1 (0.1%) |
| denismosolov@gmail.com | 1 (0.1%) |

| Employers with the most hackers (total 11) | |
|---|---|
| Northern.tech | 3 (27.3%) |
| RnDity | 2 (18.2%) |
| open-nandra | 1 (9.1%) |
| github@survive.ch | 1 (9.1%) |
| max@maxbruckner.de | 1 (9.1%) |
| adriancuzman@gmail.com | 1 (9.1%) |
| tuupola@appelsiini.net | 1 (9.1%) |
| denismosolov@gmail.com | 1 (9.1%) |


### Changelogs

#### mender-convert (1.1.0)

New changes in mender-convert since 1.1.0b1:

* Expand existing environment '$PATH' variable instead of replacing it
* Use same environment '$PATH' variable when using sudo
* Fail the docker build when mandatory build-arg 'mender_client_version' is not set.
* Update Dockerfile to use latest stable mender-artifact, v2.4.0
* Use mender-artfact v3. Requires rebuild of device-image-shell container.
* Use LZMA for smaller Artifact size (but slower generation).
* Update mender-convert to use final Mender v2.0 release

New changes in mender-convert since 1.0.0:

* Fix syntax error when calling "mender-convert raw-disk-image-shrink-rootfs"
* Experimental device emulation environment
* Create repartitioned Mender compliant image from Yocto image for qemu x86-64
  ([MEN-2207](https://tracker.mender.io/browse/MEN-2207))
* Add commits check to mender-convert repo
  ([MEN-2282](https://tracker.mender.io/browse/MEN-2282))
* Provide systemd service for Raspberry Pi boards to resize data partition
  ([MEN-2254](https://tracker.mender.io/browse/MEN-2254))
* Install Mender related files to Mender image based on Yocto image for qemu x86-64
  ([MEN-2207](https://tracker.mender.io/browse/MEN-2207))
* Check a Linux ext4 file system before resizing 'primary' partition
  ([MEN-2242](https://tracker.mender.io/browse/MEN-2242))
* compile mender during docker image creation
* Switch to 1.6.0 Mender client as default for docker environment
* Add license check to mender-convert repo
  ([MEN-2282](https://tracker.mender.io/browse/MEN-2282))
* Use a toolchain tuned for ARMv6 architecture to maintain support for Raspberry Pi Zero
  ([MEN-2399](https://tracker.mender.io/browse/MEN-2399))
* Fix docker-mender-convert for paths with spaces
* Add version option for mender convert
  ([MEN-2257](https://tracker.mender.io/browse/MEN-2257))
* Fix permission denied error in when calling "mender-convert raw-disk-image-shrink-rootfs"
* Give container access to host's kernel modules
  ([MEN-2255](https://tracker.mender.io/browse/MEN-2255))
* Support compiling Mender client in mender-convert container.
* Document missing options in the scripts
  ([MEN-2248](https://tracker.mender.io/browse/MEN-2248))
* Store sector size in raw/mender disk image related arrays
  ([MEN-2242](https://tracker.mender.io/browse/MEN-2242))
* Avoid duplicate content in cmdline.txt
* rpi: update to 2018.07 U-boot
  ([MEN-2198](https://tracker.mender.io/browse/MEN-2198))
* Add --storage-total-size-mb option to mender-convert tool
  ([MEN-2242](https://tracker.mender.io/browse/MEN-2242))
* Make tool ready for handling input images containing 3 partitions
  ([MEN-2207](https://tracker.mender.io/browse/MEN-2207))
* Allow to use "--demo" flag with any given server type
* Use local (checked out) version of mender-convert inside container
* Support passing mender-convert arguments to docker-mender-convert directly
* remove expert commands
* Refactor mender-convert to use make install target
  ([MEN-2411](https://tracker.mender.io/browse/MEN-2411))
* Improve documentation
* Set production/demo intervals conditionally
  ([MEN-2248](https://tracker.mender.io/browse/MEN-2248))
* Optimizations to speed up conversion, utilizing sparse
  images.
* remove dependency on gcc6
* Install GRUB bootloader to Mender image based on Yocto image for qemu x86-64
  ([MEN-2207](https://tracker.mender.io/browse/MEN-2207))


## meta-mender thud-v2019.05

_Released 05.07.2019_

### Statistics

A total of 323 lines added, 204 removed (delta 119)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 15 (68.2%) |
| Drew Moseley | 3 (13.6%) |
| Lluis Campos | 2 (9.1%) |
| Mirza Krak | 2 (9.1%) |

| Developers with the most changed lines | |
|---|---|
| Kristian Amlie | 396 (91.7%) |
| Mirza Krak | 17 (3.9%) |
| Drew Moseley | 16 (3.7%) |
| Lluis Campos | 3 (0.7%) |

| Developers with the most lines removed | |
|---|---|
| Mirza Krak | 13 (6.4%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 22 (100.0%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 432 (100.0%) |

| Employers with the most hackers (total 4) | |
|---|---|
| Northern.tech | 4 (100.0%) |


### Changelogs

#### meta-mender (thud-v2019.05)

New changes in meta-mender since thud-v2019.03:

* Add missing build dep on "xz" in Mender Artifact recipes for
  3.0.x versions
* Add recipes for mender-1.7.1 and mender-artifact-2.4.1.
* mender: Do not exclude missing directories.
* Add recipes for mender-2.0.0 and mender-artifact-3.0.0.
  Note that these recipes are not enabled by default in thud. If you
  want to use them, you have to add this to your build configuration:
  ```
  PREFERRED_VERSION_pn-mender = "2.%"
  PREFERRED_VERSION_pn-mender-artifact = "3.%"
  PREFERRED_VERSION_pn-mender-artifact-native = "3.%"
  ```
* Fix error message `Incorrect Usage: flag provided but not defined: -f`
* Add new liblzma dependency for the client.
* linux-raspberrypi-rt: Add mender settings for the PREEMPT_RT kernel.
* Fix mender 2.0.x and mender-artifact 3.0.x recipes to use the
  correct branches when fetching the source.


## Mender 2.0.0

_Released 05.07.2019_

### Statistics

A total of 52848 lines added, 37382 removed (delta 15466)

| Developers with the most changesets | |
|---|---|
| Manuel Zedel | 233 (34.0%) |
| Kristian Amlie | 190 (27.7%) |
| Marcin Chalczynski | 57 (8.3%) |
| Lluis Campos | 55 (8.0%) |
| Michael Clelland | 52 (7.6%) |
| Krzysztof Jaskiewicz | 39 (5.7%) |
| Ole Petter Orhagen | 19 (2.8%) |
| Eystein Måløy Stenberg | 10 (1.5%) |
| Oleksandr Miliukov | 8 (1.2%) |
| Adam Podogrocki | 4 (0.6%) |

| Developers with the most changed lines | |
|---|---|
| Manuel Zedel | 25958 (42.7%) |
| Kristian Amlie | 19328 (31.8%) |
| Krzysztof Jaskiewicz | 4561 (7.5%) |
| Marcin Chalczynski | 3028 (5.0%) |
| Ole Petter Orhagen | 2865 (4.7%) |
| Michael Clelland | 2299 (3.8%) |
| Lluis Campos | 1488 (2.4%) |
| Michael Zimmermann | 415 (0.7%) |
| Jeremy Trimble | 220 (0.4%) |
| Adam Podogrocki | 188 (0.3%) |

| Developers with the most lines removed | |
|---|---|
| Krzysztof Jaskiewicz | 2866 (7.7%) |
| Manuel Zedel | 312 (0.8%) |

| Developers with the most signoffs (total 4) | |
|---|---|
| Kristian Amlie | 4 (100.0%) |

| Developers with the most report credits (total 3) | |
|---|---|
| Mario Kozjak | 2 (66.7%) |
| Jeremy Trimble | 1 (33.3%) |

| Developers who gave the most report credits (total 3) | |
|---|---|
| Kristian Amlie | 3 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 574 (83.8%) |
| RnDity | 100 (14.6%) |
| Two Six Labs, LLC | 3 (0.4%) |
| andreas@fatal.se | 2 (0.3%) |
| Systems Engineering & Assessment Ltd | 1 (0.1%) |
| jgitlin@goboomtown.com | 1 (0.1%) |
| pannen@gmail.com | 1 (0.1%) |
| yongjhih@gmail.com | 1 (0.1%) |
| grandcentrix GmbH | 1 (0.1%) |
| Election Systems & Software | 1 (0.1%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 52156 (85.8%) |
| RnDity | 7777 (12.8%) |
| grandcentrix GmbH | 415 (0.7%) |
| Two Six Labs, LLC | 220 (0.4%) |
| Systems Engineering & Assessment Ltd | 117 (0.2%) |
| andreas@fatal.se | 75 (0.1%) |
| yongjhih@gmail.com | 42 (0.1%) |
| Election Systems & Software | 16 (0.0%) |
| pannen@gmail.com | 3 (0.0%) |
| jgitlin@goboomtown.com | 1 (0.0%) |

| Employers with the most signoffs (total 4) | |
|---|---|
| Northern.tech | 4 (100.0%) |

| Employers with the most hackers (total 21) | |
|---|---|
| Northern.tech | 10 (47.6%) |
| RnDity | 3 (14.3%) |
| grandcentrix GmbH | 1 (4.8%) |
| Two Six Labs, LLC | 1 (4.8%) |
| Systems Engineering & Assessment Ltd | 1 (4.8%) |
| andreas@fatal.se | 1 (4.8%) |
| yongjhih@gmail.com | 1 (4.8%) |
| Election Systems & Software | 1 (4.8%) |
| pannen@gmail.com | 1 (4.8%) |
| jgitlin@goboomtown.com | 1 (4.8%) |


### Changelogs

#### deployments (1.7.0)

New changes in deployments since 1.7.0b1:

* artifact object extended with optional "size" field
* Update to latest mender-artifact dependency.

New changes in deployments since 1.6.0:

* Adjust go test files to reflect changes in API
  ([MEN-2309](https://tracker.mender.io/browse/MEN-2309))
* Updated the vendor dependency on mender-artifact
* Update deployments service with mender artifact v3 format changes
  ([MEN-2309](https://tracker.mender.io/browse/MEN-2309))
* The Dockerfile has been changed to build using the multi-stage container build
  pattern, and now builds the deployments binary in one build step, and then
  copies the binary over to the production environment based on alpine:3.6. This
  change should help keep builds consistent across all services.

#### deviceauth (2.0.0)

New changes in deviceauth since 1.7.0:

* Devauth management API v1 and admission API removed.

#### gui (2.0.0)

New changes in gui since 2.0.0b1:

* Device list times no longer change on expansion
  ([MEN-2366](https://tracker.mender.io/browse/MEN-2366))
* show total artifact size in ui + clarify uncompressed size

New changes in gui since 1.7.0:

* Allow to accept multiple pending devices at one time
* schedule a new deployment to all devices within a group, except just the first 100
* Bugfix: Ensure "already installed" displays correctly in deployment report
* Update to deviceauth API v2 and use device authsets for admit-on-request flow
* Fixed single device selection in the device list UI, which could remove device selection otherwise
* show ungrouped devices in a visibly separated list entry
* more device identity attributes are now able to select, depending on their popularity
* fix an issue that prevented deployments to filtered devices
* more device identity attributes are now able to select, depending on their popularity
* multiple payloads in an artifact are now shown in the artifact list
* schedule a new deployment to all devices within a group, except just the first 100
* Fixed bug where finished deployments continue to display "in progress" when report is kept open
* multiple payloads in an artifact are now shown in the artifact list
* Allow click-to-retry for deployments with failures
* Allow to accept multiple pending devices at one time
* introduced devices information on the dashboard
* Fixed bug where finished deployments continue to display "in progress" when report is kept open
* Make Artifact selector more scalable with autocomplete
* introduced devices information on the dashboard

#### integration (2.0.0)

New changes in integration since 2.0.0b1:

* Upgrade deployments to 1.7.0.
* Upgrade deviceauth to 2.0.0.
* Upgrade gui to 2.0.0.
* Upgrade inventory to 1.6.0.
* Upgrade mender to 2.0.0.
* Upgrade mender-api-gateway-docker to 2.0.0.
* Upgrade mender-artifact to 3.0.0.
* Upgrade mender-conductor to 1.3.0.
* Upgrade mender-conductor-enterprise to 1.3.0.
* Resolve docker credentials problems in integration
  ([MEN-2408](https://tracker.mender.io/browse/MEN-2408))

New changes in integration since 1.7.0:

* Add statistics generator script, and start doing statistics
  on code development for each release.
  ([MEN-2206](https://tracker.mender.io/browse/MEN-2206))
* logo pushed as in the case of mendersoftware/mender repo
* Upgrade deployments to 1.7.0b1.
* Upgrade deviceauth to 2.0.0b1.
* Upgrade gui to 2.0.0b1.
* Upgrade inventory to 1.6.0b1.
* Upgrade mender to 2.0.0b1.
* Upgrade mender-artifact to 3.0.0b1.
* Upgrade mender-conductor to 1.3.0b1.
* Upgrade mender-conductor-enterprise to 1.3.0b1.
* Ignore author's own signoff when generating release statistics.
* Integration tests for client DB migration.
  ([MEN-2311](https://tracker.mender.io/browse/MEN-2311))
* update conductor dependencies - elasticsearch and redis
* Fix docker version detection
* Added integration test for an Artifact without any compression.
  ([MEN-2224](https://tracker.mender.io/browse/MEN-2224))
* docker-compose: add mender-conductor to mender-device-auth dependencies

#### inventory (1.6.0)

New changes in inventory since 1.5.0:

* Allow filter with ":"

#### mender (2.0.0)

New changes in mender since 2.0.0b1:

* Version files are now allowed to contain a newline character. Also
  some minor changes, as readVersion now accepts an io.Reader, and files are
  opened outside of the function. This means that the error message is now
  consistent for all the uses of readVersion.
  ([MEN-2318](https://tracker.mender.io/browse/MEN-2318))
* file-install modules: Don't destroy original before we know we have a backup.
* Fix File Install UM to not wipe out dest_dir on single file installs
* standalone: Fix artifact committing not working after upgrading from 1.x.
  ([MEN-2465](https://tracker.mender.io/browse/MEN-2465))
* Deprecate old file-install Update Module and create instead
  two new ones: single-file-install and file-tree-install. These have a
  simpler logic and clearer scope. See for details.
  ([MEN-2442](https://tracker.mender.io/browse/MEN-2442))
* Don't push network interfaces without a mac address to inventory
* Disallow installing file trees on root destination dir for
  File Install Update Module
* Make sure ARM64 is included in bootloader integration inventory.
* Mender no longer misidentifies LVM volumes.
  ([MEN-2302](https://tracker.mender.io/browse/MEN-2302))
* Update modules: Implement `NeedsArtifactReboot` -> `Automatic`.
  ([MEN-2011](https://tracker.mender.io/browse/MEN-2011))

New changes in mender since 1.7.0:

* Bugfix: State-script error code in Sync-Enter causes infinite loop
  ([MEN-2195](https://tracker.mender.io/browse/MEN-2195))
* Allow rootfsPartA and rootfsPartB to be symlinks
* Rewrite AuthorizeWaitState to fix an infinite loop bug
  ([MEN-2195](https://tracker.mender.io/browse/MEN-2195))
* Modify design for exec.Cmd stdout/stderr logging
* Place UM generator scripts in a dedicated folder
  ([MEN-2371](https://tracker.mender.io/browse/MEN-2371))
* Write Update Module to do file(s) install
  ([MEN-2371](https://tracker.mender.io/browse/MEN-2371))
* Set StateScriptTimeout default to 1h
  ([MEN-2409](https://tracker.mender.io/browse/MEN-2409))
* Add source-installation instructions to README.md.
* Add `rootfs-image-v2` as a demonstration of how to
  reimplement Mender's `rootfs-image` update type as an update module.
  It's also useful as inspiration if users want to make their own
  slightly tweaked rootfs-image type.
  ([MEN-2392](https://tracker.mender.io/browse/MEN-2392))
* Swapped definition of StateScriptRetryTimeout and
  StateScriptRetryInterval for the names to represent what they are
  actually doing. This change breaks compatibility with current usage of
  these configurable parameters. See documentation for correct usage.
  ([MEN-2409](https://tracker.mender.io/browse/MEN-2409))
* Updated the copyright year to 2019 in LICENSE.
* Write update module for doing container setup
  ([MEN-2232](https://tracker.mender.io/browse/MEN-2232))
* Add example update modules for shell commands and pkg installs.
* Remove misleading warning message when ServerCert is missing.
* Remove jq dependency for file-install Update Module
* Implement initial version of update modules.
  ([MEN-2000](https://tracker.mender.io/browse/MEN-2000))
* Add support for Mender Artifact format version 3.
  ([MEN-2000](https://tracker.mender.io/browse/MEN-2000))
* Artifact name is now stored in the local database, and
  `/etc/mender/artifact_info` acts only as a fallback if no name has
  been stored yet. This is typically the case for devices provisioned
  directly from a disk image. Scripts should use the client
  `-show-artifact` argument instead of parsing the file.
  ([MEN-2000](https://tracker.mender.io/browse/MEN-2000))
* `-rootfs` argument has been removed and replaced with the
  `-install` argument, which works the same way.
  ([MEN-2000](https://tracker.mender.io/browse/MEN-2000))
* Mender now runs a stripped down set of state scripts when
  installing artifacts in standalone mode, and the `-f` flag is no
  longer required to install such artifacts, nor is it valid. The
  scripts that run are:
  * `Download` scripts
  * `ArtifactInstall` scripts
  * `ArtifactCommit` scripts
  * `ArtifactRollback` scripts
  * `ArtifactFailure` scripts
  Reboot scripts do not run, so these must be handled manually in
  standalone mode.
  ([MEN-2000](https://tracker.mender.io/browse/MEN-2000))
* Behavior change: `ArtifactCommit_Error` scripts now run
  after an `ArtifactCommit_Leave` script has returned an error.
  ([MEN-2000](https://tracker.mender.io/browse/MEN-2000))
* Bugfix in killing mechanism for State Scripts
  timing out ([MEN-2409](https://tracker.mender.io/browse/MEN-2409))
* Update vendored dependency net/http2 to latest version
* Support installing most files using Makefile `install` target.
  The device_type file is not supported, since it is highly hardware
  specific. Also the configuration will be very bare bones, and will
  require changes unless Hosted Mender is being used.
  ([MEN-2383](https://tracker.mender.io/browse/MEN-2383))
* Make output from `-show-artifact` easier to consume by limiting logging.
* Fix state logic for the case of actual wait
  ([MEN-2195](https://tracker.mender.io/browse/MEN-2195))
* Properly fail the update when writes to the underlying storage fail.
  ([MEN-2285](https://tracker.mender.io/browse/MEN-2285))
* Work around occasional OOM bug in mmc driver.
  ([MEN-2285](https://tracker.mender.io/browse/MEN-2285))
* Make sure state directory is created if it doesn't exist.

#### mender-artifact (3.0.0)

New changes in mender-artifact since 3.0.0b1:

* checking if fsck is on path and returing error if not.
* Fix name modify command for rootfs-image Artifacts
  ([MEN-2488](https://tracker.mender.io/browse/MEN-2488))
* `mender-convert` modify for Update Module Artifacts will only
  work for options that change the headers or meta-data of the Artifact;
  curently only the Artifact name.
  ([MEN-2487](https://tracker.mender.io/browse/MEN-2487))
* `mender-artifact modify` does not support anymore signing the
  Artifact after the modification. Use `mender-convert sign` after the
  modification to sign the Artifact.
  ([MEN-2486](https://tracker.mender.io/browse/MEN-2486))

New changes in mender-artifact since 2.4.0:

* add support for uncompressed updates
  ([MEN-2224](https://tracker.mender.io/browse/MEN-2224))
* mender-artifact tool now supports removing a file in either an sdimg,
  or in a Mender Artifact, with the rm command.
  ([MEN-2331](https://tracker.mender.io/browse/MEN-2331))
* FIX: mender-artifact cat now cleans up resources on write-errors.
* Implement reading and writing support for update modules.
  ([MEN-2004](https://tracker.mender.io/browse/MEN-2004))
* Change rootfs-image `-u` argument to `-f`.
  Similarly, change `--update` to `--file`.
  ([MEN-2286](https://tracker.mender.io/browse/MEN-2286))
* Due to some faulty logic in modify.go:modifyArtifact, the sdimg's
  provided were modified, but not repacked. This fix updates the logic, and added
  a test specifically for sdimg, as they we're non-existent.
  ([MEN-2294](https://tracker.mender.io/browse/MEN-2294))
* fixes issue when binary dependencies are not in PATH
  ([MEN-2180](https://tracker.mender.io/browse/MEN-2180))
* Validate the data update files names in payload filename
  ([MEN-2319](https://tracker.mender.io/browse/MEN-2319))
* Mender-artifactV3: Bump the artifact-version protocol to version 3.
* Report a human readable error in case the artifact payload is not ext4.
* Add support for compressing artifacts using LZMA.

#### mender-conductor (1.3.0)

New changes in mender-conductor since 1.2.0:

* upgrade conductor to the latest version (2.2.0)
* Timestamp changed to ISO8601

#### mender-conductor-enterprise (1.3.0)

New changes in mender-conductor-enterprise since 1.2.0:

* Debug logging added to email preparer
* Version update from 1.8.1 to 1.8.9 for python conductor client
* Complete time format added in entrypoint script
* Bugfix for email preparer


## meta-mender rocko-v2019.04

_Released 04.25.2019_

### Statistics

A total of 582 lines added, 209 removed (delta 373)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 19 (67.9%) |
| Lluis Campos | 5 (17.9%) |
| Drew Moseley | 1 (3.6%) |
| Ole Petter Orhagen | 1 (3.6%) |
| Stoyan Bogdanov | 1 (3.6%) |
| Mirza Krak | 1 (3.6%) |

| Developers with the most changed lines | |
|---|---|
| Kristian Amlie | 575 (85.2%) |
| Lluis Campos | 56 (8.3%) |
| Mirza Krak | 21 (3.1%) |
| Drew Moseley | 14 (2.1%) |
| Stoyan Bogdanov | 8 (1.2%) |
| Ole Petter Orhagen | 1 (0.1%) |

| Developers with the most lines removed | |
|---|---|
| Lluis Campos | 35 (16.7%) |

| Developers with the most signoffs (total 2) | |
|---|---|
| Maciej Borzecki | 1 (50.0%) |
| Drew Moseley | 1 (50.0%) |

| Developers with the most report credits (total 1) | |
|---|---|
| Denis Mosolov | 1 (100.0%) |

| Developers who gave the most report credits (total 1) | |
|---|---|
| Kristian Amlie | 1 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 27 (96.4%) |
| Konsulko Group | 1 (3.6%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 667 (98.8%) |
| Konsulko Group | 8 (1.2%) |

| Employers with the most signoffs (total 2) | |
|---|---|
| Northern.tech | 1 (50.0%) |
| RnDity | 1 (50.0%) |

| Employers with the most hackers (total 6) | |
|---|---|
| Northern.tech | 5 (83.3%) |
| Konsulko Group | 1 (16.7%) |


### Changelogs

#### meta-mender (rocko-v2019.04)

New changes in meta-mender since rocko-v2018.11.2:

* allow IMAGE_BOOTLOADER_BOOTSECTOR_OFFSET to be aligend to 512 bytes
  ([MEN-1845](https://tracker.mender.io/browse/MEN-1845))
* Fix missing wpa_supplicant in Raspberry Pi demo images.
* Add mender 1.6.1 and 1.7.0 recipes.
* Add mender-artifact 2.3.1 and 2.4.0 recipes.
* mender-helpers.bbclass: Add NVMe support
* Adapt to new flags in mender-artifact-3.0.0.
* Some core update modules can now be installed by adding
  `modules` to the `PACKAGECONFIG` variable of `mender`. They are
  included by default when using the meta-mender-demo layer.
  ([MEN-2383](https://tracker.mender.io/browse/MEN-2383))
* Install `mender-data-dir.service` to create `/data/mender` directory.
* Add mender-2.0.0b1 and mender-artifact-3.0.0b1.
* Add canary value to U-Boot env to catch bootloader/user-space mismatch.
* Fix error message `Incorrect Usage: flag provided but not defined: -f`


## meta-mender sumo-v2019.04

_Released 04.25.2019_

### Statistics

A total of 545 lines added, 720 removed (delta -175)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 17 (63.0%) |
| Lluis Campos | 4 (14.8%) |
| Mirza Krak | 2 (7.4%) |
| Drew Moseley | 1 (3.7%) |
| Manuel Dipolt | 1 (3.7%) |
| Ole Petter Orhagen | 1 (3.7%) |
| Stoyan Bogdanov | 1 (3.7%) |

| Developers with the most changed lines | |
|---|---|
| Mirza Krak | 551 (47.4%) |
| Kristian Amlie | 533 (45.8%) |
| Lluis Campos | 55 (4.7%) |
| Drew Moseley | 14 (1.2%) |
| Stoyan Bogdanov | 8 (0.7%) |
| Manuel Dipolt | 1 (0.1%) |
| Ole Petter Orhagen | 1 (0.1%) |

| Developers with the most lines removed | |
|---|---|
| Mirza Krak | 550 (76.4%) |
| Lluis Campos | 36 (5.0%) |

| Developers with the most signoffs (total 1) | |
|---|---|
| Drew Moseley | 1 (100.0%) |

| Developers with the most report credits (total 1) | |
|---|---|
| Denis Mosolov | 1 (100.0%) |

| Developers who gave the most report credits (total 1) | |
|---|---|
| Kristian Amlie | 1 (100.0%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 25 (92.6%) |
| Konsulko Group | 1 (3.7%) |
| manuel@linux-home.at | 1 (3.7%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 1154 (99.2%) |
| Konsulko Group | 8 (0.7%) |
| manuel@linux-home.at | 1 (0.1%) |

| Employers with the most signoffs (total 1) | |
|---|---|
| Northern.tech | 1 (100.0%) |

| Employers with the most hackers (total 7) | |
|---|---|
| Northern.tech | 5 (71.4%) |
| Konsulko Group | 1 (14.3%) |
| manuel@linux-home.at | 1 (14.3%) |


### Changelogs

#### meta-mender (sumo-v2019.04)

New changes in meta-mender since sumo-v2018.12:

* mender-helpers.bbclass: Add NVMe support
* add 'rootwait' to bootargs
* Fix data directory not being empty on rootfs.
  ([MEN-2290](https://tracker.mender.io/browse/MEN-2290))
* Adapt to new flags in mender-artifact-3.0.0.
* Some core update modules can now be installed by adding
  `modules` to the `PACKAGECONFIG` variable of `mender`. They are
  included by default when using the meta-mender-demo layer.
  ([MEN-2383](https://tracker.mender.io/browse/MEN-2383))
* Install `mender-data-dir.service` to create `/data/mender` directory.
* Change variable to access ubi dataimg, points now to the symlink to prevent yocto rebuild error when timestamp/name of ubimg have changed
* Add mender-2.0.0b1 and mender-artifact-3.0.0b1.
* Add canary value to U-Boot env to catch bootloader/user-space mismatch.
* Fix error message `Incorrect Usage: flag provided but not defined: -f`


## meta-mender thud-v2019.03

_Released 03.28.2019_

### Statistics

A total of 358 lines added, 95 removed (delta 263)

| Developers with the most changesets | |
|---|---|
| Kristian Amlie | 12 (75.0%) |
| Lluis Campos | 2 (12.5%) |
| Manuel Dipolt | 1 (6.2%) |
| Mirza Krak | 1 (6.2%) |

| Developers with the most changed lines | |
|---|---|
| Kristian Amlie | 350 (97.8%) |
| Lluis Campos | 6 (1.7%) |
| Manuel Dipolt | 1 (0.3%) |
| Mirza Krak | 1 (0.3%) |

| Top changeset contributors by employer | |
|---|---|
| Northern.tech | 15 (93.8%) |
| manuel@linux-home.at | 1 (6.2%) |

| Top lines changed by employer | |
|---|---|
| Northern.tech | 357 (99.7%) |
| manuel@linux-home.at | 1 (0.3%) |

| Employers with the most hackers (total 4) | |
|---|---|
| Northern.tech | 3 (75.0%) |
| manuel@linux-home.at | 1 (25.0%) |


### Changelogs

#### meta-mender (thud-v2019.03)

New changes in meta-mender since thud-v2019.02:

* Some core update modules can now be installed by adding
  `modules` to the `PACKAGECONFIG` variable of `mender`. They are
  included by default when using the meta-mender-demo layer.
  ([MEN-2383](https://tracker.mender.io/browse/MEN-2383))
* Install `mender-data-dir.service` to create `/data/mender` directory.
* Change variable to access ubi dataimg, points now to the symlink to prevent yocto rebuild error when timestamp/name of ubimg have changed
* grub: ensure "test" module is builtin
* Add mender-2.0.0b1 and mender-artifact-3.0.0b1.
* Adapt to new flags in mender-artifact-3.0.0.


## meta-mender thud-v2019.02

### Statistics

A total of 11 lines added, 2 removed (delta 9)

| Developers with the most changesets |           |
|-------------------------------------|-----------|
| Kristian Amlie                      | 2 (50.0%) |
| Moritz Fischer                      | 1 (25.0%) |
| Stoyan Bogdanov                     | 1 (25.0%) |

| Developers with the most changed lines |           |
|----------------------------------------|-----------|
| Stoyan Bogdanov                        | 8 (72.7%) |
| Kristian Amlie                         | 2 (18.2%) |
| Moritz Fischer                         | 1 (9.1%)  |

| Developers with the most report credits (total 1) |            |
|---------------------------------------------------|------------|
| Denis Mosolov                                     | 1 (100.0%) |

| Developers who gave the most report credits (total 1) |            |
|-------------------------------------------------------|------------|
| Kristian Amlie                                        | 1 (100.0%) |

| Top changeset contributors by employer |           |
|----------------------------------------|-----------|
| Northern.tech                          | 2 (50.0%) |
| Konsulko Group                         | 1 (25.0%) |
| Ettus Research                         | 1 (25.0%) |

| Top lines changed by employer |           |
|-------------------------------|-----------|
| Konsulko Group                | 8 (72.7%) |
| Northern.tech                 | 2 (18.2%) |
| Ettus Research                | 1 (9.1%)  |

| Employers with the most hackers (total 3) |           |
|-------------------------------------------|-----------|
| Konsulko Group                            | 1 (33.3%) |
| Northern.tech                             | 1 (33.3%) |
| Ettus Research                            | 1 (33.3%) |

### Changelogs

_Released 02.08.2019_

#### meta-mender (thud-v2019.02)

New changes in meta-mender since thud-v2019.01:

* mender-helpers.bbclass: Add NVMe support


## meta-mender thud-v2019.01

_Released 01.04.2019_

### Statistics

A total of 80 lines added, 103 removed (delta -23)

| Developers with the most changesets |           |
|-------------------------------------|-----------|
| Kristian Amlie                      | 4 (66.7%) |
| Ole Petter Orhagen                  | 1 (16.7%) |
| Mirza Krak                          | 1 (16.7%) |

| Developers with the most changed lines |             |
|----------------------------------------|-------------|
| Kristian Amlie                         | 158 (92.9%) |
| Mirza Krak                             | 11 (6.5%)   |
| Ole Petter Orhagen                     | 1 (0.6%)    |

| Developers with the most lines removed |            |
|----------------------------------------|------------|
| Kristian Amlie                         | 34 (33.0%) |

| Top changeset contributors by employer |            |
|----------------------------------------|------------|
| Northern.tech                          | 6 (100.0%) |

| Top lines changed by employer |              |
|-------------------------------|--------------|
| Northern.tech                 | 170 (100.0%) |

| Employers with the most hackers (total 3) |            |
|-------------------------------------------|------------|
| Northern.tech                             | 3 (100.0%) |


### Changelogs

#### meta-mender (thud-v2019.01)

New changes in meta-mender since thud-v2018.12:

* part-images: add missing u-boot:deploy dependency for ARM
* Add grub-mender-grubenv 1.2.1 recipe.
* Fix grub-editenv invocation on platforms where it is called
  grub2-editenv.
* Fix data directory not being empty on rootfs.
  ([MEN-2290](https://tracker.mender.io/browse/MEN-2290))


## meta-mender sumo-v2018.12

_Released 12.14.2018_

### Statistics

A total of 31 lines added, 39 removed (delta -8)

| Developers with the most changesets |            |
|-------------------------------------|------------|
| Kristian Amlie                      | 3 (100.0%) |

| Developers with the most changed lines |             |
|----------------------------------------|-------------|
| Kristian Amlie                         | 56 (100.0%) |

| Developers with the most lines removed |           |
|----------------------------------------|-----------|
| Kristian Amlie                         | 8 (20.5%) |

| Developers with the most signoffs (total 3) |            |
|---------------------------------------------|------------|
| Kristian Amlie                              | 3 (100.0%) |

| Top changeset contributors by employer |            |
|----------------------------------------|------------|
| Northern.tech                          | 3 (100.0%) |

| Top lines changed by employer |             |
|-------------------------------|-------------|
| Northern.tech                 | 56 (100.0%) |

| Employers with the most signoffs (total 3) |            |
|--------------------------------------------|------------|
| Northern.tech                              | 3 (100.0%) |

| Employers with the most hackers (total 1) |            |
|-------------------------------------------|------------|
| Northern.tech                             | 1 (100.0%) |

### Changelogs

#### meta-mender (sumo-v2018.12)

New changes in meta-mender since sumo-v2018.11.2:

* Fix missing wpa_supplicant in Raspberry Pi demo images.
* Add mender 1.6.1 and 1.7.0 recipes.
* Add mender-artifact 2.3.1 and 2.4.0 recipes.


## meta-mender thud-v2018.12

_Released 12.13.2018_

### Statistics

A total of 3145 lines added, 2930 removed (delta 215)

| Developers with the most changesets |            |
|-------------------------------------|------------|
| Kristian Amlie                      | 76 (73.1%) |
| Drew Moseley                        | 9 (8.7%)   |
| Michael Davis                       | 5 (4.8%)   |
| Adam Podogrocki                     | 3 (2.9%)   |
| Mirza Krak                          | 2 (1.9%)   |
| Marcin Pasinski                     | 2 (1.9%)   |
| David Bensoussan                    | 2 (1.9%)   |
| Dominik Adamski                     | 1 (1.0%)   |
| Leon Anavi                          | 1 (1.0%)   |
| Ole Petter Orhagen                  | 1 (1.0%)   |

| Developers with the most changed lines |              |
|----------------------------------------|--------------|
| Kristian Amlie                         | 3919 (70.7%) |
| Mirza Krak                             | 635 (11.5%)  |
| Adam Podogrocki                        | 512 (9.2%)   |
| Michael Davis                          | 228 (4.1%)   |
| Drew Moseley                           | 113 (2.0%)   |
| Marcin Pasinski                        | 82 (1.5%)    |
| Eystein Måløy Stenberg                 | 41 (0.7%)    |
| Dominik Adamski                        | 4 (0.1%)     |
| David Bensoussan                       | 2 (0.0%)     |
| Leon Anavi                             | 2 (0.0%)     |

| Developers with the most lines removed |             |
|----------------------------------------|-------------|
| Mirza Krak                             | 616 (21.0%) |
| Adam Podogrocki                        | 293 (10.0%) |
| Marcin Pasinski                        | 72 (2.5%)   |
| Drew Moseley                           | 24 (0.8%)   |

| Developers with the most signoffs (total 107) |            |
|-----------------------------------------------|------------|
| Kristian Amlie                                | 77 (72.0%) |
| Drew Moseley                                  | 10 (9.3%)  |
| Michael Davis                                 | 5 (4.7%)   |
| Adam Podogrocki                               | 3 (2.8%)   |
| Mirza Krak                                    | 2 (1.9%)   |
| Marcin Pasinski                               | 2 (1.9%)   |
| David Bensoussan                              | 2 (1.9%)   |
| Leon Anavi                                    | 1 (0.9%)   |
| Thomas Preston                                | 1 (0.9%)   |
| Ole Petter Orhagen                            | 1 (0.9%)   |

| Developers with the most report credits (total 2) |           |
|---------------------------------------------------|-----------|
| Michael Davis                                     | 1 (50.0%) |
| Stoyan Bogdanov                                   | 1 (50.0%) |

| Developers who gave the most report credits (total 2) |           |
|-------------------------------------------------------|-----------|
| Drew Moseley                                          | 1 (50.0%) |
| Leon Anavi                                            | 1 (50.0%) |

| Top changeset contributors by employer |            |
|----------------------------------------|------------|
| Northern.tech                          | 91 (87.5%) |
| Election Systems & Software            | 5 (4.8%)   |
| RnDity                                 | 4 (3.8%)   |
| Synapticon                             | 2 (1.9%)   |
| Konsulko Group                         | 1 (1.0%)   |
| Codethink Ltd.                         | 1 (1.0%)   |

| Top lines changed by employer |              |
|-------------------------------|--------------|
| Northern.tech                 | 4791 (86.5%) |
| RnDity                        | 516 (9.3%)   |
| Election Systems & Software   | 228 (4.1%)   |
| Synapticon                    | 2 (0.0%)     |
| Konsulko Group                | 2 (0.0%)     |
| Codethink Ltd.                | 2 (0.0%)     |

| Employers with the most signoffs (total 107) |            |
|----------------------------------------------|------------|
| Northern.tech                                | 93 (86.9%) |
| RnDity                                       | 5 (4.7%)   |
| Election Systems & Software                  | 5 (4.7%)   |
| Synapticon                                   | 2 (1.9%)   |
| Konsulko Group                               | 1 (0.9%)   |
| Codethink Ltd.                               | 1 (0.9%)   |

| Employers with the most hackers (total 12) |           |
|--------------------------------------------|-----------|
| Northern.tech                              | 6 (50.0%) |
| RnDity                                     | 2 (16.7%) |
| Election Systems & Software                | 1 (8.3%)  |
| Synapticon                                 | 1 (8.3%)  |
| Konsulko Group                             | 1 (8.3%)  |
| Codethink Ltd.                             | 1 (8.3%)  |

### Changelogs

#### meta-mender (thud-v2018.12)

New changes in meta-mender since sumo-v2018.11.2:

* Add mender-artifact 2.4.0b1 recipe.
* Make mkfs.ubifs and ubinize arguments a bit more customizable.
  The new variables `MENDER_FLASH_MINIMUM_IO_UNIT` and
  `MENDER_MAXIMUM_LEB_COUNT` have been introduced, which maps directly
  to the corresponding arguments of the two tools.
* Beaglebone builds no longer compatible with builds from sumo and older.
  The reason is that bootloader switched to GRUB. The old build type can
  be restored by removing `mender-grub` and adding `mender-uboot` to
  `DISTRO_FEATURES` using the `MENDER_FEATURES` variables.
* Fix `IMAGE_ROOTFS_EXCLUDE_PATH` failing when listing a non-existent path.
* Increase default u-boot MTD partition size to 1MiB.
* Fix inability to patch old u-boot variants of MTDPARTS and
  MTDIDS correctly.
  ([MEN-1849](https://tracker.mender.io/browse/MEN-1849))
* Add mender 1.7.0b1 recipe.
* Fix images not being modifiable by mender-artifact in thud and later.
* Add mender 1.5.1 recipe.
* Add mender 1.6.0 recipe.
* Add mender-artifact 2.3.0 recipe.
* Remove support for `loadaddr` variable and
  `CONFIG_LOADADDR` config setting in U-Boot. This only affects boards
  that use U-Boot as a first stage bootloader in order to use UEFI to
  load GRUB as the second stage bootloader. For most boards it should
  not be problematic, since most support `kernel_addr_r`. If there is
  a problem however, it might be necessary to forward port [this
  patch](https://github.com/mendersoftware/meta-mender/blob/b39aa8aeecdf2b8cce3dbcce25ec044073568348/meta-mender-core/recipes-bsp/u-boot/patches/0007-distro_bootcmd-Switch-bootefi-to-use-loadaddr-by-def.patch)
  to the U-Boot version in question.
* Fix boot directory being excluded from thud images
* Add some debug functionality to GRUB booting process.
  To use it, enable either or both of `debug-log` and `debug-pause` in
  `PACKAGECONFIG` for `grub-mender-grubenv`. The former enables debug
  logging in GRUB, which can be tweaked further by setting the
  `DEBUG_LOG_CATEGORY` variable. The latter pauses the boot process at
  strategic points during the boot, so that screen output can be
  captured before it is cleared or scrolls by.
* Fix build error when using any hard drive besides sda/hda, such as sdb.
* Images partitioned with GPT or MSDOS partition tables are
  now padded up to the nearest alignment specified in
  `MENDER_PARTITION_ALIGNMENT`. Previously the last block might be
  shorter.
* Remove meta-mender-orangepi and meta-mender-toradex-nxp
  as these will be moved to meta-mender-community for the next stable
  branch (thud)
* Make sure mtdimg is not truncated, but has its full length.
* Enable EXTERNALSRC to be used with u-boot-fw-utils-mender-auto-provided.
* Allow disabling auto-generated /etc/fstab
* mender: Enable systemd in mender-systemd FEATURE handling.
  As long as `mender-systemd` feature is enabled, it is no longer
  necessary to include the block:
  ```
  DISTRO_FEATURES_append = " systemd"
  VIRTUAL-RUNTIME_init_manager = "systemd"
  DISTRO_FEATURES_BACKFILL_CONSIDERED = "sysvinit"
  VIRTUAL-RUNTIME_initscripts = ""
  ```
* Add canary value to U-Boot env to catch bootloader/user-space mismatch.
* GRUB: Fix error about devicetree command not being found.
* Change default storage on x86 to memory card (mmcblk0).
* Reduce partitioning overhead by default.
  The current value of 4 * alignment is excessive, since we now take
  alignment into account when calculating rootfs size. Instead, only
  count overhead lost to partition table, which is 2 * alignment.
* mender: Allow overrides for MENDER_STORAGE_TOTAL_SIZE_MB_DEFAULT.
* Allow boot partition to be populated with normal package recipes.
* Fix `MENDER_GRUB_STORAGE_DEVICE` variable not being respected.
  ([MEN-2048](https://tracker.mender.io/browse/MEN-2048))
* GRUB: Make kernel console argument configurable using "console_bootargs".
  One can set this variable in some "xx_*_grub.cfg" script with an index
  lower than 10, in the grub-mender-grubenv recipe.
* uboot_auto_patch: Switch kernel address from `loadaddr`
  back to `kernel_addr_r`. This was discussed with U-Boot developers and
  is the proper address variable going forward.
* Fix incorrect Flash bad PEB calculation which led to wrong total image size.
  ([MEN-1849](https://tracker.mender.io/browse/MEN-1849))
* Add mender 1.6.1 and 1.7.0 recipes.
* Add mender-artifact 2.3.1 and 2.4.0 recipes.
* Auto-select correct `MENDER_STORAGE_DEVICE_BASE` scheme.
  This should rarely need to be set by anyone anymore.
* Fix confusing warning flood when MENDER_MTDIDS is unset in a UBI build.
* Switch image names from containing `MACHINE` to containing
  `MENDER_DEVICE_TYPE`. So for example, if you have a build for the
  raspberrypi3 machine type, with device type of "prod_rpi3", the image
  will now be called `core-image-minimal-prod_rpi3.sdimg` instead of
  `core-image-minimal-raspberrypi3.sdimg`.
* Fix console logging for systemd on QEMU.
* Fix build error when using GRUB and /dev/mmcblk storage device.
* Add specific patches for u-boot-toradex_2016.11.
  ([MEN-1849](https://tracker.mender.io/browse/MEN-1849))
* grub: Remove restriction that the core.img be at sector 1
* mender-uboot: Use hex for dev/part numbers in U-Boot.
* Delete all components from pre-1.5 Mender releases.
  Remove Mender 1.4.0 and 1.4.1 and Mender artifact 2.2.0.
* Introduce support for a standardized boot method on ARM
  using UEFI and GRUB. The UEFI boot standard is fully supported on ARM
  in theory, but few board manufacturers implement it in practice.
  Therefore U-Boot is still utilized, but acts only as a UEFI loader,
  and hence no U-Boot integration is needed. All boot scripts are then
  handled by GRUB, which needs no patching.
  ([MEN-1595](https://tracker.mender.io/browse/MEN-1595), [MEN-1659](https://tracker.mender.io/browse/MEN-1659))
* Add support for PARTUUID in grub-mender-grubenv script.
* Remove colibri-imx7-mender MACHINE type, replaced by colibri-imx7.
* Fix regression that removed boot flag from boot partition.
* Fix regression that caused Beaglebone to not boot.
* QEMU: Always try to run with KVM enabled, only fall back to emulation.
* Fix license checksum sometimes failing in
  `u-boot-fw-utils-mender-auto-provided` recipe when U-Boot fork has a
  slightly different README file.
* Add PARTUUID generation and integration
* Change default bootloader to GRUB on all non-UBI platforms.
  U-Boot will still be used on ARM platforms to provide UEFI that GRUB
  can use, but it will not be used for Mender integration. To opt out,
  and keep using traditional U-Boot integration, remove `mender-grub`,
  and add `mender-uboot` using the `MENDER_FEATURES` variables.
* Fixed support for raspberrypi3-64 and aarch64
* mender-uboot: Allow multi-digit partition/device nums.
* Add mender 1.6.0b1 and mender-artifact 2.3.0b1 recipes.
* Remove obsolete mender pre-1.4 and mender-artifact pre-2.2 recipes.
* Fix regression in QEMU launching after changing image name in 897195ddc3f.
* Replaced default yocto cfg file for grub pre configuration by the proper cfg file without redundant and erroneous search command.
* rpi: update U-boot patch to get rid of warning
* Fix incorrect license tag for mender-artifact recipe.
  Little practical difference, since they are all permissive licenses.
* Fix missing wpa_supplicant in Raspberry Pi demo images.
* GRUB: Pass kernel arguments from bootargs variable instead of hard coded.
  This allows it to be overridden or modified by adding a script snippet
  which sets the variable.
  Also log kernel messages to both screen and serial port by default,
  and have systemd log to serial port (last "console" argument,
  apparently it cannot log to both).
* Add support for GPT BIOS images
* Boot script recipe for demoing OTA updates


## mender-convert 1.0.0

_Released 12.13.2018_

### Statistics

A total of 4848 lines added, 1459 removed (delta 3389)

| Developers with the most changesets |            |
|-------------------------------------|------------|
| Adam Podogrocki                     | 32 (45.1%) |
| Dominik Adamski                     | 18 (25.4%) |
| Eystein Måløy Stenberg              | 13 (18.3%) |
| Mirza Krak                          | 6 (8.5%)   |
| Mika Tuupola                        | 1 (1.4%)   |
| Pierre-Jean Texier                  | 1 (1.4%)   |

| Developers with the most changed lines |              |
|----------------------------------------|--------------|
| Adam Podogrocki                        | 4297 (87.0%) |
| Eystein Måløy Stenberg                 | 324 (6.6%)   |
| Dominik Adamski                        | 241 (4.9%)   |
| Mirza Krak                             | 74 (1.5%)    |
| Mika Tuupola                           | 1 (0.0%)     |
| Pierre-Jean Texier                     | 1 (0.0%)     |

| Developers with the most lines removed |           |
|----------------------------------------|-----------|
| Mirza Krak                             | 33 (2.3%) |

| Developers with the most signoffs (total 70) |            |
|----------------------------------------------|------------|
| Adam Podogrocki                              | 31 (44.3%) |
| Dominik Adamski                              | 18 (25.7%) |
| Eystein Måløy Stenberg                       | 13 (18.6%) |
| Mirza Krak                                   | 6 (8.6%)   |
| Mika Tuupola                                 | 1 (1.4%)   |
| Pierre-Jean Texier                           | 1 (1.4%)   |

| Top changeset contributors by employer |            |
|----------------------------------------|------------|
| RnDity                                 | 50 (70.4%) |
| Northern.tech                          | 19 (26.8%) |
| tuupola@appelsiini.net                 | 1 (1.4%)   |
| Lafon Technologies                     | 1 (1.4%)   |

| Top lines changed by employer |              |
|-------------------------------|--------------|
| RnDity                        | 4538 (91.9%) |
| Northern.tech                 | 398 (8.1%)   |
| tuupola@appelsiini.net        | 1 (0.0%)     |
| Lafon Technologies            | 1 (0.0%)     |

| Employers with the most signoffs (total 70) |            |
|---------------------------------------------|------------|
| RnDity                                      | 49 (70.0%) |
| Northern.tech                               | 19 (27.1%) |
| tuupola@appelsiini.net                      | 1 (1.4%)   |
| Lafon Technologies                          | 1 (1.4%)   |

| Employers with the most hackers (total 6) |           |
|-------------------------------------------|-----------|
| RnDity                                    | 2 (33.3%) |
| Northern.tech                             | 2 (33.3%) |
| tuupola@appelsiini.net                    | 1 (16.7%) |
| Lafon Technologies                        | 1 (16.7%) |

### Changelogs

#### mender-convert (1.0.0)

Initial release of mender-convert! Some developer versions were tested along the
way, so here is the changelog since then:

* Make tool ready for handling input images containing 3 partitions
  ([MEN-2207](https://tracker.mender.io/browse/MEN-2207))
* Support passing mender-convert arguments to docker-mender-convert directly
* Switch to 1.6.0 Mender client as default for docker environment
* Use local (checked out) version of mender-convert inside container
* Support compiling Mender client in mender-convert container.
* compile mender during docker image creation
* Install GRUB bootloader to Mender image based on Yocto image for qemu x86-64
  ([MEN-2207](https://tracker.mender.io/browse/MEN-2207))
* fix image paths printed at end of conversion
* Docker environment for running mender-convert
* Create repartitioned Mender compliant image from Yocto image for qemu x86-64
  ([MEN-2207](https://tracker.mender.io/browse/MEN-2207))
* Avoid duplicate content in cmdline.txt
* Install Mender related files to Mender image based on Yocto image for qemu x86-64
  ([MEN-2207](https://tracker.mender.io/browse/MEN-2207))
* Increase default server retry interval from 1 to 30 seconds.
* Add version option for mender convert
  ([MEN-2257](https://tracker.mender.io/browse/MEN-2257))


## Mender 1.7.0

_Released 12.13.2018_

### Release statistics
A total of 25446 lines added, 6653 removed (delta 18793)

| Developers with the most changesets |             |
|-------------------------------------|-------------|
| Marcin Chalczynski                  | 104 (34.0%) |
| Krzysztof Jaskiewicz                | 71 (23.2%)  |
| Kristian Amlie                      | 47 (15.4%)  |
| Michael Clelland                    | 36 (11.8%)  |
| Maciej Mrowiec                      | 14 (4.6%)   |
| Ole Petter Orhagen                  | 7 (2.3%)    |
| Alf-Rune Siqveland                  | 6 (2.0%)    |
| Don Cross                           | 5 (1.6%)    |
| Eystein Måløy Stenberg              | 4 (1.3%)    |
| Marcin Pasinski                     | 3 (1.0%)    |

| Developers with the most changed lines |              |
|----------------------------------------|--------------|
| Michael Clelland                       | 9832 (35.8%) |
| Kristian Amlie                         | 6660 (24.3%) |
| Marcin Chalczynski                     | 5180 (18.9%) |
| Krzysztof Jaskiewicz                   | 3594 (13.1%) |
| Alf-Rune Siqveland                     | 1184 (4.3%)  |
| Maciej Mrowiec                         | 367 (1.3%)   |
| Ole Petter Orhagen                     | 207 (0.8%)   |
| Don Cross                              | 186 (0.7%)   |
| Tobias Klauser                         | 56 (0.2%)    |
| Mirza Krak                             | 55 (0.2%)    |

| Developers with the most lines removed |           |
|----------------------------------------|-----------|
| Tobias Klauser                         | 51 (0.8%) |
| Eystein Måløy Stenberg                 | 28 (0.4%) |

| Developers with the most signoffs (total 310) |             |
|-----------------------------------------------|-------------|
| Marcin Chalczynski                            | 104 (33.5%) |
| Krzysztof Jaskiewicz                          | 71 (22.9%)  |
| Kristian Amlie                                | 48 (15.5%)  |
| Michael Clelland                              | 36 (11.6%)  |
| Maciej Mrowiec                                | 14 (4.5%)   |
| Ole Petter Orhagen                            | 8 (2.6%)    |
| Alf-Rune Siqveland                            | 6 (1.9%)    |
| Don Cross                                     | 5 (1.6%)    |
| Eystein Måløy Stenberg                        | 4 (1.3%)    |
| Marcin Pasinski                               | 3 (1.0%)    |

| Top changeset contributors by employer |             |
|----------------------------------------|-------------|
| RnDity                                 | 175 (57.2%) |
| Northern.tech                          | 122 (39.9%) |
| cosinekitty@gmail.com                  | 5 (1.6%)    |
| Amarula Solutions                      | 1 (0.3%)    |
| jgitlin@goboomtown.com                 | 1 (0.3%)    |
| tklauser@distanz.ch                    | 1 (0.3%)    |
| Election Systems & Software            | 1 (0.3%)    |

| Top lines changed by employer |               |
|-------------------------------|---------------|
| Northern.tech                 | 18415 (67.1%) |
| RnDity                        | 8774 (32.0%)  |
| cosinekitty@gmail.com         | 186 (0.7%)    |
| tklauser@distanz.ch           | 56 (0.2%)     |
| Election Systems & Software   | 16 (0.1%)     |
| Amarula Solutions             | 2 (0.0%)      |
| jgitlin@goboomtown.com        | 1 (0.0%)      |

| Employers with the most signoffs (total 310) |             |
|----------------------------------------------|-------------|
| RnDity                                       | 175 (56.5%) |
| Northern.tech                                | 126 (40.6%) |
| cosinekitty@gmail.com                        | 5 (1.6%)    |
| tklauser@distanz.ch                          | 1 (0.3%)    |
| Election Systems & Software                  | 1 (0.3%)    |
| Amarula Solutions                            | 1 (0.3%)    |
| jgitlin@goboomtown.com                       | 1 (0.3%)    |

| Employers with the most hackers (total 17) |            |
|--------------------------------------------|------------|
| Northern.tech                              | 10 (58.8%) |
| RnDity                                     | 2 (11.8%)  |
| cosinekitty@gmail.com                      | 1 (5.9%)   |
| tklauser@distanz.ch                        | 1 (5.9%)   |
| Election Systems & Software                | 1 (5.9%)   |
| Amarula Solutions                          | 1 (5.9%)   |
| jgitlin@goboomtown.com                     | 1 (5.9%)   |


### Changelogs

#### deployments (1.6.0)

New changes in deployments since 1.5.0:

* Change image download link validity to 24h from 1h.
* Change image download link validity to 24h from 1h.
  ([MEN-2054](https://tracker.mender.io/browse/MEN-2054))

#### deviceauth (1.7.0)

New changes in deviceauth since 1.7.0b1:

* document management API v2

New changes in deviceauth since 1.6.0:

* do not synchronize data with device admission service
* docs: introduce version 2 of the management API
* fix database migration
* fix database migration
* management API v2 endpoint for getting devices
* v2 of GET /devices/<id>
* actually run migration 1.5.0
* actually run migration 1.5.0
* API v2 POST /devices endpoint (for preauthorizing devices)
* v2 of GET /devices/<id>

#### gui (1.7.0)

New changes in gui since 1.7.0b1:

* Fixed bug where finished deployments continue to display "in progress" when report is kept open

New changes in gui since 1.6.0:

* Update node modules
* Introduce new tabbed deployment layout
* Added 'Copy to clipboard' function to error messages throughout UI
* Add a date range filter to past deployments tab
* Add "copy link to device" button on expanded device view
* Add group filter to past devices tab
* Make Artifact selector more scalable with auto-complete
* Bugfix: Ensure "already installed" displays correctly in deployment report
* Allow click-to-retry for deployments with failures
* Update to deviceauth API v2 and use device authsets for admit-on-request flow

#### integration (1.7.0)

New changes in integration since 1.7.0b1:

* Upgrade deployments to 1.6.0.
* Upgrade deviceauth to 1.7.0.
* Upgrade gui to 1.7.0.
* Upgrade inventory to 1.5.0.
* Upgrade mender to 1.7.0.
* Upgrade mender-api-gateway-docker to 1.6.0.
* Upgrade mender-artifact to 2.4.0.
* Upgrade mender-cli to 1.1.0.
* Upgrade mender-conductor to 1.2.0.
* Upgrade mender-conductor-enterprise to 1.2.0.
* Upgrade useradm to 1.7.0.
* Add statistics generator script, and start doing statistics
  on code development for each release.
  ([MEN-2206](https://tracker.mender.io/browse/MEN-2206))

New changes in integration since 1.6.0:

* Increase bandwidth limit to 3 MB/s per device for demo setup.
* remove admission service from the setup
* remove admission service from the setup
* client: Use KVM automatically if available. Remove "./demo --kvm" option.
* Fix docker version detection
* Upgrade deployments to 1.6.0b1.
* Upgrade deviceauth to 1.7.0b1.
* Upgrade gui to 1.7.0b1.
* Upgrade inventory to 1.5.0b1.
* Upgrade mender to 1.7.0b1.
* Upgrade mender-api-gateway-docker to 1.6.0b1.
* Upgrade mender-artifact to 2.4.0b1.
* Upgrade mender-cli to 1.1.0b1.
* Upgrade mender-conductor to 1.2.0b1.
* Upgrade mender-conductor-enterprise to 1.2.0b1.
* Upgrade useradm to 1.7.0b1.

#### mender (1.7.0)

New changes in mender since 1.7.0b1:

* Allow rootfsPartA and rootfsPartB to be symlinks

New changes in mender since 1.6.0:

* FIX: Enabling compiling ppc64le
* Fix active partition detection when using non-native
  filesystems.
* Add inventory scripts for rootfs type and bootloader integration.
  ([MEN-2059](https://tracker.mender.io/browse/MEN-2059))
* New feature: Fail-over Mender server(s)
  ([MEN-1972](https://tracker.mender.io/browse/MEN-1972))
* New inventory script for "os" attribute, installed by default.
  ([MEN-2060](https://tracker.mender.io/browse/MEN-2060))
* Mender client now loads configuration settings from
  both /etc/mender/mender.conf and (if it exists)
  /var/lib/mender/mender.conf. The second file is located
  on the data partition, so it allows any subset of configuration
  changes to survive upgrades.
  ([MEN-2073](https://tracker.mender.io/browse/MEN-2073))
* Print a message to the mender log when the
  mender client has confirmed the authenticity of an
  artifact's digital signature.
  ([MEN-2152](https://tracker.mender.io/browse/MEN-2152))
* Fix update check not working under BusyBox.
  ([MEN-2159](https://tracker.mender.io/browse/MEN-2159))
* Add Community Code of Conduct
* Detect if inactive part is mounted and unmount
  ([MEN-2084](https://tracker.mender.io/browse/MEN-2084))
* Improve error message when running mender as non-root user
  ([MEN-2083](https://tracker.mender.io/browse/MEN-2083))

#### mender-api-gateway-docker (1.6.0)

New changes in mender-api-gateway-docker since 1.5.0:

* nginx conf: redirect /api/management/v1/admission calls to devicauth service
* redirection to /ui/ fixed
* use exact openresty version (1.13.6.2-0-alpine) instead of floating tag (alpine)
* json access logs format option is added

#### mender-artifact (2.4.0)

New changes in mender-artifact since 2.3.0:

* FIX: mender-artifact cp no longer renames the artifact.
* FIX: remove leftover tmp files from mender-artifact cp.
* FIX: mender-artifact no longer changes the names of the updates in an artifact
* Updated the JSON format of header-info version 3.
* A command of the form
  "mender-artifact validate unsigned.mender -k public.key"
  was incorrectly succeeding for an unsigned artifact when a public key
  was supplied. Supplying a public key indicates that the caller requires
  the artifact to contain a signature that matches that key.
  Now this command fails (exits with a nonzero value) as expected.
  ([MEN-2155](https://tracker.mender.io/browse/MEN-2155))
* FIX: Renaming a file across devices now works.
  ([MEN-2166](https://tracker.mender.io/browse/MEN-2166))
* FIX: mender-artifact cat,cp,modify etc no longer removes the update.
  Previously an update present in a directory, with the same name as the
  update present in an update would be removed as a result of what the
  functions thought was tmp-files.
  ([MEN-2171](https://tracker.mender.io/browse/MEN-2171))
* Fixed a bug that caused a command like
  "mender-artifact cat signed.mender:/etc/mender/artifact_info"
  to fail with the error:
  "failed to open the partition reader: err: error validating signature"
  There was a similar problem with the "cp" command, and also
  the "modify" command when no "-k" was present to replace the
  existing signature.

#### mender-conductor-enterprise (1.2.0)

New changes in mender-conductor-enterprise since 1.1.0:

* Latest template from Ralph.

#### useradm (1.7.0)

New changes in useradm since 1.6.0:

* Recover from unsuccessful attempt to create user.
* Enable common logging stack adding request access log and response timings.


## Mender 1.6.1

_Released 12.13.2018_

### Statistics

A total of 4690 lines added, 96 removed (delta 4594)

| Developers with the most changesets |            |
|-------------------------------------|------------|
| Kristian Amlie                      | 21 (75.0%) |
| Ole Petter Orhagen                  | 3 (10.7%)  |
| Marcin Pasinski                     | 2 (7.1%)   |
| Josh Gitlin                         | 1 (3.6%)   |
| Don Cross                           | 1 (3.6%)   |

| Developers with the most changed lines |              |
|----------------------------------------|--------------|
| Kristian Amlie                         | 4649 (99.1%) |
| Ole Petter Orhagen                     | 30 (0.6%)    |
| Don Cross                              | 8 (0.2%)     |
| Marcin Pasinski                        | 5 (0.1%)     |
| Josh Gitlin                            | 1 (0.0%)     |

| Developers with the most lines removed |          |
|----------------------------------------|----------|
| Marcin Pasinski                        | 3 (3.1%) |

| Developers with the most signoffs (total 28) |            |
|----------------------------------------------|------------|
| Kristian Amlie                               | 21 (75.0%) |
| Ole Petter Orhagen                           | 3 (10.7%)  |
| Marcin Pasinski                              | 2 (7.1%)   |
| Josh Gitlin                                  | 1 (3.6%)   |
| Don Cross                                    | 1 (3.6%)   |

| Top changeset contributors by employer |            |
|----------------------------------------|------------|
| Northern.tech                          | 26 (92.9%) |
| cosinekitty@gmail.com                  | 1 (3.6%)   |
| jgitlin@goboomtown.com                 | 1 (3.6%)   |

| Top lines changed by employer |              |
|-------------------------------|--------------|
| Northern.tech                 | 4684 (99.8%) |
| cosinekitty@gmail.com         | 8 (0.2%)     |
| jgitlin@goboomtown.com        | 1 (0.0%)     |

| Employers with the most signoffs (total 28) |            |
|---------------------------------------------|------------|
| Northern.tech                               | 26 (92.9%) |
| cosinekitty@gmail.com                       | 1 (3.6%)   |
| jgitlin@goboomtown.com                      | 1 (3.6%)   |

| Employers with the most hackers (total 5) |           |
|-------------------------------------------|-----------|
| Northern.tech                             | 3 (60.0%) |
| cosinekitty@gmail.com                     | 1 (20.0%) |
| jgitlin@goboomtown.com                    | 1 (20.0%) |

### Changelogs

#### integration (1.6.1)

New changes in integration since 1.6.0:

* Upgrade deviceadm to 1.4.1.
* Upgrade mender to 1.6.1.
* Upgrade mender-artifact to 2.3.1.
* Add statistics generator script, and start doing statistics
  on code development for each release.
  ([MEN-2206](https://tracker.mender.io/browse/MEN-2206))
* Fix docker version detection

#### mender (1.6.1)

New changes in mender since 1.6.0:

* Fix update check not working under BusyBox.
  ([MEN-2159](https://tracker.mender.io/browse/MEN-2159))
* Print a message to the mender log when the
  mender client has confirmed the authenticity of an
  artifact's digital signature.
  ([MEN-2152](https://tracker.mender.io/browse/MEN-2152))

#### mender-artifact (2.3.1)

New changes in mender-artifact since 2.3.0:

* FIX: Renaming a file across devices now works.
  ([MEN-2166](https://tracker.mender.io/browse/MEN-2166))
* FIX: mender-artifact cat,cp,modify etc no longer removes the update.
  Previously an update present in a directory, with the same name as the
  update present in an update would be removed as a result of what the
  functions thought was tmp-files.
  ([MEN-2171](https://tracker.mender.io/browse/MEN-2171))



## meta-mender sumo-v2018.11.2

_Released 11.16.2018_

#### meta-mender (sumo-v2018.11.2)

New changes in meta-mender since sumo-v2018.11:

* Add mender 1.7.0b1 recipe.
* Add mender-artifact 2.4.0b1 recipe.


## meta-mender sumo-v2018.11

_Released 11.12.2018_

#### meta-mender (sumo-v2018.11)

New changes in meta-mender since sumo-v2018.10:

* QEMU: Always try to run with KVM enabled, only fall back to emulation.


## meta-mender sumo-v2018.10

_Released 10.03.2018_

#### meta-mender (sumo-v2018.10)

New changes in meta-mender since sumo-v2018.09:

* Make sure mtdimg is not truncated, but has its full length.
* Add specific patches for u-boot-toradex_2016.11.
  ([MEN-1849](https://tracker.mender.io/browse/MEN-1849))
* Fix incorrect Flash bad PEB calculation which led to wrong total image size.
  ([MEN-1849](https://tracker.mender.io/browse/MEN-1849))
* Make mkfs.ubifs and ubinize arguments a bit more customizable.
  The new variables `MENDER_FLASH_MINIMUM_IO_UNIT` and
  `MENDER_MAXIMUM_LEB_COUNT` have been introduced, which maps directly
  to the corresponding arguments of the two tools.
* Fix inability to patch old u-boot variants of MTDPARTS and
  MTDIDS correctly.
  ([MEN-1849](https://tracker.mender.io/browse/MEN-1849))
* Fix confusing warning flood when MENDER_MTDIDS is unset in a UBI build.


## meta-mender sumo-v2018.09

_Released 09.13.2018_

#### meta-mender (sumo-v2018.09)

New changes in meta-mender since sumo-v2018.08:

* Fix regression in QEMU launching after changing image name in 897195ddc3f.
* GRUB: Pass kernel arguments from bootargs variable instead of hard coded.
  This allows it to be overridden or modified by adding a script snippet
  which sets the variable.
  Also log kernel messages to both screen and serial port by default,
  and have systemd log to serial port (last "console" argument,
  apparently it cannot log to both).
* Introduce support for a standardized boot method on ARM
  using UEFI and GRUB. The UEFI boot standard is fully supported on ARM
  in theory, but few board manufacturers implement it in practice.
  Therefore U-Boot is still utilized, but acts only as a UEFI loader,
  and hence no U-Boot integration is needed. All boot scripts are then
  handled by GRUB, which needs no patching.
  ([MEN-1595](https://tracker.mender.io/browse/MEN-1595), [MEN-1659](https://tracker.mender.io/browse/MEN-1659))
* Auto-select correct `MENDER_STORAGE_DEVICE_BASE` scheme.
  This should rarely need to be set by anyone anymore.
* Add some debug functionality to GRUB booting process.
  To use it, enable either or both of `debug-log` and `debug-pause` in
  `PACKAGECONFIG` for `grub-mender-grubenv`. The former enables debug
  logging in GRUB, which can be tweaked further by setting the
  `DEBUG_LOG_CATEGORY` variable. The latter pauses the boot process at
  strategic points during the boot, so that screen output can be
  captured before it is cleared or scrolls by.
* GRUB: Fix error about devicetree command not being found.
* Images partitioned with GPT or MSDOS partition tables are
  now padded up to the nearest alignment specified in
  `MENDER_PARTITION_ALIGNMENT`. Previously the last block might be
  shorter.
* Fix build error when using GRUB and /dev/mmcblk storage device.
* Fix build error when using any hard drive besides sda/hda, such as sdb.
* Fix `IMAGE_ROOTFS_EXCLUDE_PATH` failing when listing a non-existent path.
* Fix `MENDER_GRUB_STORAGE_DEVICE` variable not being respected.
  ([MEN-2048](https://tracker.mender.io/browse/MEN-2048))
* Allow disabling auto-generated /etc/fstab
* Boot script recipe for demoing OTA updates
* mender: Allow overrides for MENDER_STORAGE_TOTAL_SIZE_MB_DEFAULT.
* mender-uboot: Use hex for dev/part numbers in U-Boot.
* Add mender 1.5.1 recipe.
* Add mender 1.6.0 recipe.
* Add mender-artifact 2.3.0 recipe.


## Mender 1.6.0

_Released 09.18.2018_

#### deviceauth (1.6.0)

New changes in deviceauth since 1.5.0:

* Device object returned by API exposes new boolean attribute: "decommissioning" signifying devices that are currently going through removal process.

#### gui (1.6.0)

New changes in gui since 1.6.0b1:

* Added 'Copy to clipboard' function to error messages throughout UI
* Introduce new tabbed deployment layout
* Update node modules
* Bugfix: Ensure "already installed" displays correctly in deployment report

New changes in gui since 1.5.0:

* Add preauthorize devices section
* Cleaned up URL for filtering device list by ID or group:
  ([MEN-1875](https://tracker.mender.io/browse/MEN-1875))
* Add a global setting to store and use user-selected device identity attribute throughout UI
* Fixup: Add a link to mender docs for enabling wifi in hosted image

#### integration (1.6.0)

New changes in integration since 1.6.0b1:

* Upgrade deviceauth to 1.6.0.
* Upgrade gui to 1.6.0.
* Upgrade inventory to 1.4.1.
* Upgrade mender to 1.6.0.
* Upgrade mender-artifact to 2.3.0.
* Upgrade mender-cli to 1.0.1.
* Upgrade mender-conductor to 1.1.0.
* Upgrade mender-conductor-enterprise to 1.1.0.
* Upgrade useradm to 1.6.0.

New changes in integration since 1.5.0:

* Add mender-cli as a versioned repository under the Mender umbrella.
* Upgrade deviceauth to 1.6.0b1.
* Upgrade gui to 1.6.0b1.
* Upgrade inventory to 1.4.1b1.
* Upgrade mender to 1.6.0b1.
* Upgrade mender-artifact to 2.3.0b1.
* Upgrade mender-cli to 1.0.1b1.
* Upgrade mender-conductor to 1.1.0b1.
* Upgrade mender-conductor-enterprise to 1.1.0b1.
* Upgrade useradm to 1.6.0b1.
* demo: suppress warning on newer docker-compose versions
* consolidate to single mongodb server instance
* Change mongo definitions to map the correct path. /data is being mapped, but /data/db needs to.
* test_security.py: Ignore return code of grep.
* use common mongodb server instance with tenantadm

#### mender (1.6.0)

New changes in mender since 1.6.0b1:

* Fix active partition detection when using non-native
  filesystems.
* New inventory script for "os" attribute, installed by default.
  ([MEN-2060](https://tracker.mender.io/browse/MEN-2060))
* FIX: Enabling compiling ppc64le
* Add inventory scripts for rootfs type and bootloader integration.
  ([MEN-2059](https://tracker.mender.io/browse/MEN-2059))

New changes in mender since 1.5.0:

* FIXED: HTTP error 401 is not handled by all states
  ([MEN-1854](https://tracker.mender.io/browse/MEN-1854))
* ArtifactReboot_Enter scripts are no longer rerun
  if interrupted by an unexpected reboot. It will be treated
  as if Mender itself rebooted.
* Enable user to force an update-check locally
  The user can now force an update check by either running mender with the
  -check-update option, or send a signal [SIGUSR1] to the running mender process.
  ([MEN-1905](https://tracker.mender.io/browse/MEN-1905))
* Add automatic check for canary value in U-Boot environment
  to try to detect if there is a problem in the environment setup of
  U-Boot and/or the u-boot-fw-utils tools.
* Mender client key generator script
* log active partition before and after reboot.
  ([MEN-1880](https://tracker.mender.io/browse/MEN-1880))

#### mender-artifact (2.3.0)

New changes in mender-artifact since 2.3.0b1:

* FIX: mender-artifact cp no longer renames the artifact.
* FIX: remove leftover tmp files from mender-artifact cp.
* FIX: mender-artifact no longer changes the names of the updates in an artifact

New changes in mender-artifact since 2.2.0:

* Add boot partition as a modify candidate for artifact cp
* Add mtools as a dependency before installing from source, and in travis
* Testify/require files added to the vendor directory
* Small cleanup of license text. No legal difference, just
  makes it easier for the tooling.
* Install function added
* Added uefiimg as an option to the cp and cat commands
* modify any file using the mender-artifact tool
  ([MEN-1741](https://tracker.mender.io/browse/MEN-1741))
* add testify/require to vendor
* modify any file using the mender-artifact tool
  ([MEN-1741](https://tracker.mender.io/browse/MEN-1741))
* Mender-artifact can now copy to and read from the data partition
  ([MEN-1953](https://tracker.mender.io/browse/MEN-1953))
* run fsck before modifying image.
  ([MEN-1798](https://tracker.mender.io/browse/MEN-1798))

#### mender-conductor (1.1.0)

New changes in mender-conductor since 1.0.0:

* Extend logging with messages from conductor client library to stdout.
* Update conductor client library to 1.8.9


## meta-mender sumo-v2018.08

_Released 08.03.2018_

#### meta-mender (sumo-v2018.08)

New changes in meta-mender since sumo-v2018.07:

* Add mender 1.6.0b1 and mender-artifact 2.3.0b1 recipes.
* Fixed support for raspberrypi3-64 and aarch64
* Fix incorrect license tag for mender-artifact recipe.
  Little practical difference, since they are all permissive licenses.
* mender-uboot: Allow multi-digit partition/device nums.
* Fix license checksum sometimes failing in
  `u-boot-fw-utils-mender-auto-provided` recipe when U-Boot fork has a
  slightly different README file.


## meta-mender sumo-v2018.07

_Released 07.12.2018_

#### meta-mender (sumo-v2018.07)
* Warn when mender.conf settings conflict with Bitbake variables.
* Make sure that new-style "enp" network devices get DHCP address in demo.
* Delete all components from pre-1.3 Mender releases.
  All pre-1.3 releases are EOL.
* Rename IMAGE_BOOTLOADER* variables to MENDER_IMAGE_BOOTLOADER*.
* Fix lockfile error due to using system lock directory.
* Licence checksum updated in mender-artifact
* mender: Allow for forcing a specific KERNEL_IMAGETYPE.
* mender-uboot: Add MENDER_UBOOT_POST_SETUP_COMMANDS config point.
* Fix occasional inode corruption issue when re-launching a
  previously launched and saved QEMU image.
* QEMU: Limit client setup steps to run on first boot only.
* mender-qemu: increase qemu memory size to 256MiB.
* Let colibri-imx7 and vf boards be handled by automatic patching.
* Fixed issue with build due to unknown image linux-firmware-raspbian-bcm43430
* Fix mender not building if build and host architecture is the same.
* meta-mender-orangepi: Fix up u-boot
* Fix Linux kernel hanging when loaded via U-Boot/UEFI/GRUB
  on vexpress-qemu*.
  ([MEN-1657](https://tracker.mender.io/browse/MEN-1657))
* Add mender-1.3.1 and mender-artifact-2.1.2 recipes.
* Implement `IMAGE_ROOTFS_EXCLUDE_PATH` support. It works the
  following way: It contains a space separated list of directories,
  relative to the rootfs root (no beginning slash), and any directory
  specified will be omitted from the rootfs. If the directory ends in a
  slash, only the contents will be omitted, not the directory itself
  (useful for mount points). One can then set
  `do_image_<imagetype>[respect_exclude_path] = "1"` for certain image
  builders to prevent the exclusion and then add them back as separate
  partitions there.
* Support for `MENDER_DATA_PART_DIR` has been removed. Use
  recipe files to add files directly to the `/data` directory instead.
* mender: Create bmap files.
* tests: Filter out the data partition as the latest build artifact.
* example-state-scripts: Explicitly return 0 from scripts.
* uboot_auto_patch: Simplify definition placement at the expense of beauty.
  The resulting patch is uglier because the definitions go into a cross
  platform section which is not appropriate for upstream submission. But
  it does fix the case where unwanted ifdefs were "hiding" the added
  definitions.
* rpi_0_w: Setup Mender required defconfigs
* Implement GRUB and x86-64 support.
  ([MEN-1430](https://tracker.mender.io/browse/MEN-1430), [MEN-1432](https://tracker.mender.io/browse/MEN-1432), [MEN-1433](https://tracker.mender.io/browse/MEN-1433), [MEN-1434](https://tracker.mender.io/browse/MEN-1434), [MEN-1435](https://tracker.mender.io/browse/MEN-1435), [MEN-1436](https://tracker.mender.io/browse/MEN-1436))
* Implement qemux86-64 machine target.
  ([MEN-1430](https://tracker.mender.io/browse/MEN-1430), [MEN-1432](https://tracker.mender.io/browse/MEN-1432), [MEN-1433](https://tracker.mender.io/browse/MEN-1433), [MEN-1434](https://tracker.mender.io/browse/MEN-1434), [MEN-1435](https://tracker.mender.io/browse/MEN-1435), [MEN-1436](https://tracker.mender.io/browse/MEN-1436))
* mender: Conditionally add /uboot mount only for SDCards.
* Increased the demo mender-retry-polling interval
  ([MEN-1006](https://tracker.mender.io/browse/MEN-1006))
* meta-mender-toradex-nxp: Adapt colibri-imx7-mender to U-Boot autopatching
* Fix 'depends upon non-existent task' error in U-Boot recipes without auto patching.
* Use timedatectl, if available, to determine with time is synchronized.
* mender upgraded to 1.4.0.
* mender-artifact upgraded to 2.2.0.
* mender-qemu: More robust detection of MACHINE setting.
* beaglebone: Rename to beaglebone-yocto.
* Add mtdimg image type.
  The mtdimg type is an image type meant to be flashed to the entire
  Flash device, unlike the ubimg, which should only be flashed to the
  ubi area of the mtd device. Either one can be used depending on need.
  vexpress-nor image, used in QEMU, was also changed to take advantage
  of the new mtdimg image.
  ([MEN-1597](https://tracker.mender.io/browse/MEN-1597))
* Add LAYERSERIES_COMPAT settings to all Mender layers.
* Replace `MENDER_PARTITION_ALIGNMENT_KB` with
  `MENDER_PARTITION_ALIGNMENT`, which is in bytes.
* Rename `MENDER_STORAGE_RESERVED_RAW_SPACE` to
  `MENDER_RESERVED_SPACE_BOOTLOADER_DATA`, to better reflect what it is
  used for.
* Enable wifi in the raspberry-pi demo image by default.
  ([MEN-1804](https://tracker.mender.io/browse/MEN-1804))
* mender: Only create vfat boot partition if size is non-zero
* meta-mender-toradex-nxp: increase layer priority to 91
* Fix creating ubifs image.
* tests: Respect user set SSTATE_DIR and DL_DIR variables.
* Make sure auto provided fw-utils use virtual/bootloader setting if present.
* QEMU: Raise systemd service timeout so that it boots properly on slow hosts.
* Fix fstab sometimes not containing boot partition entry.
* Fix build error if `IMAGE_FSTYPES` contains the same entry more than once.
* Implement x86 BIOS support together with GRUB.
  It can be enabled by inheriting the `mender-full-bios` class, or by
  enabling the `mender-grub` and `mender-bios` features using
  `MENDER_FEATURES_ENABLE`.
  ([MEN-1845](https://tracker.mender.io/browse/MEN-1845))
* Client container init scripts are modified to accept MAC address for qemu through env var, `RANDOM_MAC`.
* added layer dependency on mender layer
* uboot_auto_configure: Fail immediately if a define cannot be added.
  Better than failing later at runtime, where the problem is much harder
  to debug.
* Warn on unused MENDER_.* variables
  ([MEN-1603](https://tracker.mender.io/browse/MEN-1603))
* uboot_auto_patch: Switch kernel address from `kernel_addr_r` to `loadaddr`.
* Remove unused IMAGE_UENV_TXT_FILE variable.
* Add U-Boot auto patching support for Flash based devices.
  The autopatcher will use UBI as storage medium for both the
  filesystems and the U-Boot environment. Mender requires a minimum of
  configuration: the `MENDER_MTDIDS` needs to be set for the board, and
  will normally go in the `conf/machine/<MACHINE>.conf` file for the
  board in question. See documentation for variables `MENDER_MTDIDS`,
  `MENDER_IS_IN_MTDID` and `MENDER_MTDPARTS` for more information.
  ([MEN-1597](https://tracker.mender.io/browse/MEN-1597))
* Partition alignment (`MENDER_PARTITION_ALIGNMENT`) on Flash
  devices using UBI is now aligned to the UBI LEB size, which in general
  is not a multiple of KiB.
  ([MEN-1597](https://tracker.mender.io/browse/MEN-1597))
* Add Mender 1.4.1 recipe.
* Clear IMAGE_NAME_SUFFIX for all image types.
* Fix "No rule to make target 'envtools'" error in some U-Boot builds.
* Pregenerate SSH keys for all QEMU images.
* Since the "beaglebone" machine name has changed in upstream
  to "beaglebone-yocto", add "beaglebone" to the
  `MENDER_DEVICE_TYPES_COMPATIBLE` default, so that older devices can
  upgrade even if they have the old device type.
* mender: Copy data partition images to the deploy dir.
* mender: Append to fstab rather than replacing it.
* Fix failed uboot.env install when mender-uboot feature is disabled.
* tests: Also check ARTIFACTIMG_FSTYPE for compatible images.
* uboot_auto_patch: Update to support U-Boot v2018.05.
* uboot_auto_patch: Add support for new Kconfig based
  defines.
* mender-uboot: Add MENDER_UBOOT_PRE_SETUP_COMMANDS config point.
* Add Mender 1.5.0 Beta recipe.
* Add mender-1.4.0b1 and mender-artifact-2.2.0b1 recipes.
* Add 'dataimg' as an image type.
  It contains the data partition filesystem which is normally part of
  the complete partitioned image. To enable it, add `dataimg` to
  `IMAGE_FSTYPES`.
  ([MEN-1879](https://tracker.mender.io/browse/MEN-1879))
* mender: Use only the basename to load DTBs.
* Add Mender 1.5.0 recipe.
* Document SDIMG_ROOTFS_TYPE settings for Raspberry Pi.
* Change rootfs size calculation so it takes alignment into account.
  This should fix a few corner cases, where the filesystems may all fit
  in terms of bytes, but still would not actually fit because of
  partition alignment.
* Added new state script to wait for time sync to complete.
* Drop creation of `authtentoken` file, which is unneeded now.
* Added basic support for orangepi boards
* mender: Cleanup IMAGE_FSTYPES.
* uboot_auto_configure: Handle tabs in defines correctly.


## meta-mender rocko-v2018.07

_Released 07.10.2018_

#### meta-mender (rocko-v2018.07)
* Clear IMAGE_NAME_SUFFIX for all image types.
* Use timedatectl, if available, to determine with time is synchronized.
* Change rootfs size calculation so it takes alignment into account.
  This should fix a few corner cases, where the filesystems may all fit
  in terms of bytes, but still would not actually fit because of
  partition alignment.
  Backported to Morty. MENDER_PARTITION_ALIGNMENT_KB instead
  of MENDER_PARTITION_ALIGNMENT.
* Fix Linux kernel hanging when loaded via U-Boot/UEFI/GRUB
  on vexpress-qemu*.
  ([MEN-1657](https://tracker.mender.io/browse/MEN-1657))
* Fix occasional inode corruption issue when re-launching a
  previously launched and saved QEMU image.
* QEMU: Limit client setup steps to run on first boot only.
* tests: Filter out the data partition as the latest build artifact.
* Licence checksum updated in mender-artifact
* Fixed issue with build due to unknown image linux-firmware-raspbian-bcm43430
* tests: Respect user set SSTATE_DIR and DL_DIR variables.
* Warn when mender.conf settings conflict with Bitbake variables.
* example-state-scripts: Explicitly return 0 from scripts.
* Client container init scripts are modified to accept MAC address for qemu through env var, `RANDOM_MAC`.
* tests: Also check ARTIFACTIMG_FSTYPE for compatible images.
* meta-mender-core: Clean spaces out of UBOOT_MACHINE.


## meta-mender rocko-v2018.06

_Released 06.05.2018_

#### meta-mender rocko-v2018.06
* Add Mender 1.5.0 recipe.
* Add Mender 1.4.1 recipe.
* Enable wifi in the raspberry-pi demo image by default.
  ([MEN-1804](https://tracker.mender.io/browse/MEN-1804))


## Mender v1.5.0

_Released 06.07.2018_

#### integration (1.5.0)
* Add mender-cli as a versioned repository under the Mender umbrella.
* Upgrade deployments to 1.5.0.
* Upgrade deviceadm to 1.4.0.
* Upgrade deviceauth to 1.5.0.
* Upgrade gui to 1.5.0.
* Upgrade inventory to 1.4.0.
* Upgrade mender to 1.5.0.
* Upgrade mender-api-gateway-docker to 1.5.0.
* Add mender-cli 1.0.0.
* Add mender-conductor 1.0.0.
* Add mender-conductor-enterprise 1.0.0.
* Upgrade useradm to 1.5.0.

#### mender (1.5.0)
* FIXED: HTTP error 401 is not handled by all states
  ([MEN-1854](https://tracker.mender.io/browse/MEN-1854))
* Mender client key generator script


## Mender v1.4.2

_Released 06.07.2018_

#### gui (1.4.1)
* Fix elusive bug which sometimes caused GUI to restart over
  and over due to not finding uglifyjs.

#### integration (1.4.2)
* Upgrade gui to 1.4.1.


## Mender v1.4.1

_Released 06.04.2018_

#### integration (1.4.1)
* Switched to using Intel x86_64 hardware accelerated client
  instead of ARM emulator.
* Add --kvm option to demo scripts to run client VM hardware accelerated.
* Switch default client container type to qemux86-64.
* Upgrade mender to 1.4.1.

#### mender (1.4.1)
* FIXED: Log writes not flushed from memory
  ([MEN-1726](https://tracker.mender.io/browse/MEN-1726))
* Regenerate keys on all key errors, not just when keys are missing.
  ([MEN-1823](https://tracker.mender.io/browse/MEN-1823))
* Mender client key generator script


## meta-mender rocko-v2018.05

_Released 05.09.2018_

## meta-mender rocko-v2018.05
* mender: Copy data partition images to the deploy dir.
* Fix mender not building if build and host architecture is the same.
* Increased the demo mender-retry-polling interval
  ([MEN-1006](https://tracker.mender.io/browse/MEN-1006))
* Fix failed uboot.env install when mender-uboot feature is disabled.
* Implement GRUB and x86-64 support.
  ([MEN-1430](https://tracker.mender.io/browse/MEN-1430), [MEN-1432](https://tracker.mender.io/browse/MEN-1432), [MEN-1433](https://tracker.mender.io/browse/MEN-1433), [MEN-1434](https://tracker.mender.io/browse/MEN-1434), [MEN-1435](https://tracker.mender.io/browse/MEN-1435), [MEN-1436](https://tracker.mender.io/browse/MEN-1436))
* Implement qemux86-64 machine target.
  ([MEN-1430](https://tracker.mender.io/browse/MEN-1430), [MEN-1432](https://tracker.mender.io/browse/MEN-1432), [MEN-1433](https://tracker.mender.io/browse/MEN-1433), [MEN-1434](https://tracker.mender.io/browse/MEN-1434), [MEN-1435](https://tracker.mender.io/browse/MEN-1435), [MEN-1436](https://tracker.mender.io/browse/MEN-1436))
* Make sure auto provided fw-utils use virtual/bootloader setting if present.
* Add Mender 1.5.0 Beta recipe.
* mender: Use only the basename to load DTBs.
* mender: Conditionally add /uboot mount only for SDCards.
* Make sure that new-style "enp" network devices get DHCP address in demo.
* mender: Allow for forcing a specific KERNEL_IMAGETYPE.
* Remove unused IMAGE_UENV_TXT_FILE variable.


## Mender v1.5.0b1

_Released 05.15.2018_

#### deployments (1.5.0b1)
* display number of devices targeted when listing deployments
* possible to upload artifacts to specific tenant via internal API
  ([MEN-1775](https://tracker.mender.io/browse/MEN-1775))
* add ability to filter on deployment creation timestamps

#### deviceauth (1.5.0b1)
* trigger device provisioning workflow only if the device is not currently accepted
* device count endpoint handles preauthorized devices
* moved to globalsign/mgo

#### gui (1.5.0b1)
* Fix bug where recent deployment stats were being called repeatedly on dashboard
* Display version in UI
* Redesign Devices sections, added Rejected devices tab
* Display a dialog after first deployment as part of onboarding
* Move main navigation to be left aligned

#### integration (1.5.0b1)
* Switched to using Intel x86_64 hardware accelerated client
  instead of ARM emulator.
* Make the integration version available to the UI
  ([MEN-1767](https://tracker.mender.io/browse/MEN-1767))
* mender-conductor container is now based on
  github.com/mendersoftware/mender-conductor repository.
* Add --kvm option to demo scripts to run client VM hardware accelerated.
* Introduce optional mender-conductor container based on
  github.com/mendersoftware/mender-conductor-enterprise, for Enterprise
  installations.
* migrate to setup with mender-conductor-enterprise image
* Switch default client container type to qemux86-64.
* Upgrade deployments to 1.5.0b1.
* Upgrade deviceadm to 1.4.0b1.
* Upgrade deviceauth to 1.5.0b1.
* Upgrade gui to 1.5.0b1.
* Upgrade inventory to 1.4.0b1.
* Upgrade mender to 1.5.0b1.
* Upgrade mender-api-gateway-docker to 1.5.0b1.
* Add mender-conductor 1.0.0b1.
* Add mender-conductor-enterprise 1.0.0b1.
* Upgrade useradm to 1.5.0b1.
* migrate to setup with mender-conductor image

#### mender (1.5.0b1)
* Regenerate keys on all key errors, not just when keys are missing.
  ([MEN-1823](https://tracker.mender.io/browse/MEN-1823))
* cli: New client option to show installed artifact name
  ([MEN-1806](https://tracker.mender.io/browse/MEN-1806))
* Spontaneous-reboot hardening of the client
  ([MEN-1187](https://tracker.mender.io/browse/MEN-1187))
* FIXED: Log writes not flushed from memory
  ([MEN-1726](https://tracker.mender.io/browse/MEN-1726))
* Allow multiple digit partition numbers.
* log request-id in case of bad API requests
  ([MEN-1738](https://tracker.mender.io/browse/MEN-1738))
* Abort upgrade if artifact name is not retrievable from artifact_info
  ([MEN-1824](https://tracker.mender.io/browse/MEN-1824))

#### mender-api-gateway-docker (1.5.0b1)
* Allow cross-origin requests from hostnames listed in ALLOWED_HOSTS
* When a client exceeds its rate limit gateway returns 429 (Too
  Many Requests) instead of 503 (Service Temporarily Unavailable)

#### useradm (1.5.0b1)
* New internal endpoint for deleting authentication tokens.


## Mender v1.4.0

_Released 03.20.2018_

#### integration (1.4.0)
* Upgrade deployments to 1.4.0.
* Upgrade deviceadm to 1.3.0.
* Upgrade deviceauth to 1.4.0.
* Upgrade gui to 1.4.0.
* Upgrade inventory to 1.3.0.
* Upgrade mender to 1.4.0.
* Upgrade mender-api-gateway-docker to 1.4.0.
* Upgrade mender-artifact to 2.2.0.
* Upgrade useradm to 1.4.0.

#### mender (1.4.0)
* Allow multiple digit partition numbers.


## meta-mender rocko-v2018.03

_Released 03.19.2018_

#### meta-mender rocko-v2018.03
* mender upgraded to 1.4.0.
* mender-artifact upgraded to 2.2.0.
* Document SDIMG_ROOTFS_TYPE settings for Raspberry Pi.
* Fix creating ubifs image.
* mender-qemu: increase qemu memory size to 256MiB.
* meta-mender-toradex-nxp: increase layer priority to 91


## meta-mender rocko-v2018.02

_Released 02.02.2018_

#### meta-mender rocko-v2018.02
* mender: Append to fstab rather than replacing it.
* Add mender-1.4.0b1 and mender-artifact-2.2.0b1 recipes.
* Fix 'depends upon non-existent task' error in U-Boot recipes without auto patching.
* Add mender-1.3.1 and mender-artifact-2.1.2 recipes.
* QEMU: Raise systemd service timeout so that it boots properly on slow hosts.
* Added new state script to wait for time sync to complete.
* Fix "No rule to make target 'envtools'" error in some U-Boot builds.
* Pregenerate SSH keys for all QEMU images.


## Mender v1.4.0b1

_Released 02.09.2018_

#### deployments (1.4.0b1)
* updated aws-go-sdk to v1.12.27
* delete artifact from storage if parsing failed

#### deviceadm (1.3.0b1)
* PUT /devices/{id}/status (internal)

#### gui (1.4.0b1)
* Add checkbox option to remain logged in
* add progress bar for individual devices updates
  ([MEN-1558](https://tracker.mender.io/browse/MEN-1558))
* make it possible to decommission a device that has never sent inventory
* add request ID to snackbar
* Added deployments in progress to header bar
* Add Device notifications to top bar
* Fix for showing incorrect device IDs
  ([MEN-1536](https://tracker.mender.io/browse/MEN-1536))

#### integration (1.4.0b1)
* Upgrade Conductor to 1.8.1
* replace dynomite with redis
* fix http 404 on decommissioning
* Update integration version references to 1.4.x.
* Upgrade deployments to 1.4.0b1.
* Upgrade deviceadm to 1.3.0b1.
* Upgrade deviceauth to 1.4.0b1.
* Upgrade gui to 1.4.0b1.
* Upgrade inventory to 1.3.0b1.
* Upgrade mender to 1.4.0b1.
* Upgrade mender-api-gateway-docker to 1.4.0b1.
* Upgrade mender-artifact to 2.2.0b1.
* Upgrade useradm to 1.4.0b1.
* replace dynomite with redis

#### inventory (1.3.0b1)
* Get all devices in a group with a single api-call.
  ([MEN-811](https://tracker.mender.io/browse/MEN-811))

#### mender (1.4.0b1)
* Report update status for scripts and states
  ([MEN-1015](https://tracker.mender.io/browse/MEN-1015))
* Print detailed logs about authorization errors.
  ([MEN-1660](https://tracker.mender.io/browse/MEN-1660), [MEN-1661](https://tracker.mender.io/browse/MEN-1661))
* mender-device-identity: Check if file exists before reading
  Mender on orangepi fails to run because identity script exit with error like:
  /usr/share/mender/identity/mender-device-identity
  cat: can't open '/sys/class/net/bonding_masters/type': Not a directory
  Add check before reading type to avoid problems.
* Remove trailing slash from server URL configuration.
  ([MEN-1620](https://tracker.mender.io/browse/MEN-1620))

#### mender-artifact (2.2.0b1)
* Fix ECDSA failures while signing and verifying artifact.
  ([MEN-1470](https://tracker.mender.io/browse/MEN-1470))
* Fix broken header checksum verification.
  ([MEN-1412](https://tracker.mender.io/browse/MEN-1412))
* Add modify existing images and artifacts functionality.
  ([MEN-1213](https://tracker.mender.io/browse/MEN-1213))
* Artifact version 3 format documentation
  ([MEN-1667](https://tracker.mender.io/browse/MEN-1667))
* Mender-Artifact now returns an error code to the os on cli errors
  ([MEN-1328](https://tracker.mender.io/browse/MEN-1328))
* mender-artifact now fails with whitespace in the artifact-name
  ([MEN-1355](https://tracker.mender.io/browse/MEN-1355))

#### mender-api-gateway-docker (1.4.0b1)
* reload-when-hosts-changed: silence cmp output
* From now on it is possible to set rate limit per IP address
  for the API using environment variables.
  There are two variables:
  RATE_LIMIT_GLOBAL_RATE=limit - number of request per second
  RATE_LIMIT_GLOBAL_BURST=burst - burst parameter defines
  how many requests a client can make in excess
  of the rate specified by the limit.
  Both parameters, limit and burst, should be numbers.
* entrypoint: include mender-gui in monitored DNS names


## meta-mender rocko-v2018.01

_Released 01.04.2018_

* meta-mender-core: Allow dtbos in KERNEL_DEVICETREE

## meta-mender rocko-v2017.12

_Released 12.20.2017_

* mender-artifact: Fix build failure due to poky golang source directory changes.
* Catch up with latest poky U-Boot v2017.05.
* Fix build failure after poky switched to checking out Go
  sources under the full GOPATH.
* rpi-u-boot-scr: Switch to boot.cmd.in style recipe.
* sato: Set NETWORK_MANAGER to systemd.
* Update example-state-scripts to use standard logging.
* Add Mender 1.3.0b1 recipe.
* Work around bug in libpseudo regarding file owners on data partition.
* Add machine configuration for Mender on colibri-imx7
* u-boot: update mender_boot_part_name when mender_boot_part changes
* Remove meta-mender-beaglebone layer. This layer is not
  needed anymore for compiling for Beaglebone and should be removed from
  all build configurations.
  ([MEN-1387](https://tracker.mender.io/browse/MEN-1387))
* Add example recipe to show how to deploy files into Mender persistent data partition
* mender-artifact: Fix build failure due to poky golang support changes.
* meta-mender-raspberrypi: increase layer priority to 10
* Fix bug where MENDER_DEVICE_TYPES_COMPATIBLE would only accept one entry.
* mender: Adjust patches for U-Boot v2017.09
* mender: Use GO environment variable to launch the compiler
* Implement heuristic automatic patching of U-Boot.
  It can be turned on and off by setting `MENDER_UBOOT_AUTO_CONFIGURE`
  to `1` and `0`, respectively, in a `u-boot.bbappend` file. It is on by
  default. If the automatic patching is unsuccessful, there is a special
  bitbake target that can be used to extract the generated patch and use
  it as a basis for a manual patch. It can be invoked with `bitbake -c
  save_mender_auto_configured_patch <u-boot-recipe>`, where
  `<u-boot-recipe>` is either `u-boot` or the fork of U-Boot that your
  board uses. ([MEN-1387](https://tracker.mender.io/browse/MEN-1387))
* Bump mender and mender-artifact to version 1.1.0 and 2.0.0, respectively.
* Remove recipes for Mender 1.0.x series.
* Add Mender 1.3.0 build recipe.


## meta-mender pyro-v2017.12

_Released 12.20.2017_

* Fix bug where MENDER_DEVICE_TYPES_COMPATIBLE would only accept one entry.
* Add Mender 1.3.0 build recipe.
* u-boot: update mender_boot_part_name when mender_boot_part changes
* Update example-state-scripts to use standard logging.
* meta-mender-raspberrypi: increase layer priority to 10
* sato: Set NETWORK_MANAGER to systemd.
* Add machine configuration for Mender on colibri-imx7


## Mender v1.3.0

_Released 12.21.2017_

#### integration (1.3.0)
* Upgrade deployments to 1.3.0.
* Upgrade deviceadm to 1.2.0.
* Upgrade deviceauth to 1.3.0.
* Upgrade gui to 1.3.0.
* Upgrade inventory to 1.2.0.
* Upgrade mender to 1.3.0.
* Upgrade mender-api-gateway-docker to 1.3.0.
* Upgrade useradm to 1.3.0.

#### mender (1.3.0)
* Remove trailing slash from server URL configuration.
  ([MEN-1620](https://tracker.mender.io/browse/MEN-1620))


## meta-mender pyro-v2017.11

_Released 11.14.2017_

* Add Mender 1.3.0b1 recipe.
* Upstream image has grown significantly, increase to 608MB sdimg.
  The noticeably non-round number is to make sure the calculated rootfs
  size is divisible by the partition alignment.


## Mender v1.3.0b1

_Released 11.14.2017_

#### deployments (1.3.0b1)
* docs: dump expire parameter from artifact download endpoint
* deployments/controller: handle substate field in device status updates
* images: make artifact download links valid for 15 minutes only
* deployments: descending sort by created time when listing deployments
* deployments/controller: status report substate field length limited to 200 characters
* Additional MongoDB configuration options: mongo_ssl, mongo_ssl_skipverify, mongo_username, mongo_password
* docs/management: return device state and substate in device deployment info
* limits: add GET /limits/storage management endpoint
* deployments: make artifact download links valid for 1 hour only
* Prevent artifacts with invalid checksums from
  being uploaded to the server.
  ([MEN-1412](https://tracker.mender.io/browse/MEN-1412))
* docs/internal: spec for GET /tenants/:id/limits/storage
* Additional MongoDB configuration options: mongo_ssl, mongo…
* docs: document that expire on /artifacts/{id}/download is silently ignored
* POST /api/v1/internal/tenants ep
* docs/devices: add optional substate field in status ported

#### deviceadm (1.2.0b1)
* middleware: accommodate changes in request{id,log} middleware and enable request logger update
* Additional MongoDB configuration options: mongo_ssl, mongo_ssl_skipverify, mongo_username, mongo_password
* Additional MongoDB configuration options: mongo_ssl, mongo…
* store/mongo: move single tenant migration to separate func
* main: add 'migrate [--tenant=<tenant ID>]' command

#### deviceauth (1.3.0b1)
* GET /devices/count?status endpoint
* devauth: only one accepted authset
  When accepting an auth set, reject all other accepted auth sets of a particular
  device. This way we make sure that only one auth set is accepted at a time. In
  case when key rotation is used, old key cannot be used to obtain the token.
  ([MEN-1417](https://tracker.mender.io/browse/MEN-1417))
* store/mongo: properly setup context for migrations in multi tenant
* api/http: support for internal endpoint for setting per-tenant limits
  Add support for PUT operation on a new internal endpoint
  `/api/internal/v1/devauth/tenant/:id/limits/:name`. The endpoint is used for
  setting per tenant limits.
* store/mongo: make UpdateAuthSet() operate on multiple auth sets
* store, store/mongo: add collection for keeping 'Limits'
* devauth: ignore store.ErrAuthSetNotFound when rejecting auth sets during accept
* devauth: set Authorization field in  device decommissioning requests
* devauth: support for saving per-tenant limits
* devauth: log a message when the token is does not have a mender.device claim
* docs: include Authorization header in spec of authset status PUT endpoint
* Additional MongoDB configuration options: mongo_ssl, mongo_ssl_skipverify, mongo_username, mongo_password
* migrate --tenant=... cli
* store/mongo: raise store.ErrAuthSetNotFound when no auth sets were updated
* model: add Limit wrapper, add predefined limit name - max_device_count
* jwt: add mender.device claim, type bool, defaults to false
* docs/internal: remove 404 status on PUT /tenant/:id/limits/max-device-count
* middleware: repacking of logger and request ID to context is no longer needed
* docs: add spec for GET /limits/max_devices
* devauth: set and verify mender.device claim
  Device tokens given out by deviceauth service will now have 'mender.device'
  claim set to true. Tokens without the claim will fail verification and will be
  rejected. Device is expected to request a new token.
* client/orchestrator: pass 'authorization' parameter in device decommission request

#### gui (1.3.0b1)
* Fix logout issues, only timeout user when inactive
* Fix for showing incorrect device IDs
  ([MEN-1536](https://tracker.mender.io/browse/MEN-1536))
* Added onboarding helptips that toggle on/off per user
* Added API connection error messaging and timeouts to Deployments tab
* Added API timeouts and disconnection error retry messages to devices and artifacts tabs
* disable decommissioning button while request is in progress
* API connection error and retry for deployments on dashboard

#### integration (1.3.0b1)
* compose, template: set mender-inventory command to `server --automigrate`
  Ensure that inventory service starts in daemon mode and automatically applies DB
  migrations.
* Fix Missing restart policy for some containers in
  docker-compose setup.
  ([MEN-1556](https://tracker.mender.io/browse/MEN-1556))
* Update conductor to 1.7.7
* allow access to https://localhost in test environment
* Update conductor to 1.7.7
* Upgrade deployments to 1.3.0b1.
* Upgrade deviceadm to 1.2.0b1.
* Upgrade deviceauth to 1.3.0b1.
* Upgrade gui to 1.3.0b1.
* Upgrade inventory to 1.2.0b1.
* Upgrade mender to 1.3.0b1.
* Upgrade mender-api-gateway-docker to 1.3.0b1.
* Upgrade useradm to 1.3.0b1.
* conductor: include Authorization header in decommissioning workflow

#### inventory (1.2.0b1)
* main: add server [--automigrate] command, drop previous command line flags
  Command line invocation and parameters are changed. See --help output for
  details.
  `server` subcommand will start the services in 'daemon' mode (sans the forking
  part). Optional `--automigrate` argument enables automatic DB migration,
  otherwise then a migration is needed the service will exit logging an error.
* Additional MongoDB configuration options: mongo_ssl, mongo_ssl_skipverify, mongo_username, mongo_password
* main: add 'migrate [--tenant=<tenant ID>]' command
* middleware: accommodate changes in request{id,log} middleware and enable request logger update
* dockerfile: update entrypoint to match currently supported command line arguments
* Additional MongoDB configuration options: mongo_ssl, mongo…

#### mender (1.3.0b1)
* Mender now logs whatever a state-script outputs to stderr
  ([MEN-1349](https://tracker.mender.io/browse/MEN-1349))
* mender-device-identity: only collect MAC from ARPHRD_ETHER types
* Fix 'unexpected EOF' error when downloading large updates.
  ([MEN-1511](https://tracker.mender.io/browse/MEN-1511))
* Implement ability for client to resume a download from
  where it left off if the connection is broken.
  ([MEN-1511](https://tracker.mender.io/browse/MEN-1511))
* Improve error messages for state scripts errors.
  Rely on the full error description instead of just the error code.
* Fix compile for ARM64.
* set return code = 2, when there is nothing to commit
* Added retry-later functionality on top of the state-script functionality
* Correctly fail state script execution if stderr can not be opened.
  It would not be impossible to continue execution in this case, but it
  is bad to lose log output, and not being able to open stderr is a
  pretty uncommon case that might indicate a more serious issue like
  resource starvation.

#### mender-api-gateway-docker (1.3.0b1)
* Introduce static content caching for /ui routing.
* Make browser side UI caching configurable though CACHE_UI env. Disabled by default.
* Include request time in gateway access logs.
* nginx: separate HTTP and HTTPS server scopes, redirect all HTTP requests to HTTPS
* nginx: align gateway URLs with useradm API
* Introduce static content caching for /ui routing.
* deployments service routing
* gateway dns cache reloading for improved recovery from service restarts
  ([MEN-1227](https://tracker.mender.io/browse/MEN-1227))
* Include request time in gateway access logs.

#### useradm (1.3.0b1)
* docs: add undocumented X-Original-URI, X-Original-Method on internal /auth/verify
* store/mongo: TenantDataStore uses a store with automigrations enabled
* commands: add 'migrate [--tenant=<id>]' command
* middleware: accommodate changes in request{id,log} middleware and enable request logger update
* jwt: add mender.user claim, bool
  Add 'mender.user' claim to tokens given out bu useradm. The claim indicates that
  the token is assigned to a user and a 'sub' claim corresponds to user ID.
* store/mongo: With*() helpers return a new instance of store with correct property modified
* docs: spec for an endpoint for setting up tenants
* commands: propagate new user to tenantadm
  ([MEN-1311](https://tracker.mender.io/browse/MEN-1311))
* store/mongo: move migration of single tenant to separate func
* api/http: update internal URLs, align them with API URL schema
  Internal URLs are now available with /api/internal/v1/useradm/ prefix
* store: introduce tenant keeper
* docs: align internal URLs with API URL scheme
* useradm: add mender.user claim to given out tokens
  Append 'mender.user' claim to all given out tokens. All tokens that do not have
  this claim will fail verification and be rejected forcing the user to log in again.
* set correct header when sending token
* useradm: add CreateTenant operation
* api/http: add endpoint for creating tenants


## Mender v1.2.2

_Released 11.14.2017_

#### deployments (1.2.2)
* deployments: descending sort by created time when listing deployments

#### integration (1.2.2)
* Upgrade deployments to 1.2.2.
* Upgrade gui to 1.2.1.
* Upgrade mender-api-gateway-docker to 1.2.1.
* Fix Missing restart policy for some containers in
  docker-compose setup.
  ([MEN-1556](https://tracker.mender.io/browse/MEN-1556))

#### mender-api-gateway-docker (1.2.1)
* nginx: separate HTTP and HTTPS server scopes, redirect all HTTP requests to HTTPS


## Mender v1.2.1

_Released 10.02.2017_

#### deployments (1.2.1)
* Prevent artifacts with invalid checksums from
  being uploaded to the server.
  ([MEN-1412](https://tracker.mender.io/browse/MEN-1412))

#### integration (1.2.1)
* Upgrade deployments to 1.2.1.
* Upgrade mender to 1.2.1.
* Upgrade mender-artifact to 2.1.1.

#### mender (1.2.1)
* Improve error messages for state scripts errors.
  Rely on the full error description instead of just the error code.
* Fix checksum not being verified for headers, only
  payload. ([MEN-1412](https://tracker.mender.io/browse/MEN-1412))

#### mender-artifact (2.1.1)
* Fix broken header checksum verification.
  ([MEN-1412](https://tracker.mender.io/browse/MEN-1412))


## Mender v1.2.0

_Released 09.05.2017_

#### deployments (1.2.0)
* Deployment creation process changed. From now on artifacts are
  assigned to device deployments on update request handling.
* Return 422 - Unprocessable Entity on attempt of creating deployment without artifacts
* Deployments no longer require inventory to create deployments.
* New optional array field: 'artifacts' in deployment object returned by API containing list of artifact ids used by deployment.

#### deviceauth (1.2.0)
* Introduce 'server' subcommand that is also default command. Supports '--automigrate' parameter to enable automatic database version migration on startup.
* Increase orchestrater request timeout to 30s

#### gui (1.2.0)
* Bugfix for multiplying GET devices requests
* Add ‘create user’ functionality
* Change root API url to docker.mender.io
* Removed user creation UI incl password strength check (#231)
* Added user management edit functionality
* Updated node modules
* Remove shortened device IDs, now useless due to incremental SHAs
* create deployment from single device ([MEN-1233](https://tracker.mender.io/browse/MEN-1233))
* Allow user to remove artifacts via the GUI
* Added self user management

#### integration (1.2.0)
* Move interactive flags for client container to main docker file.
  Makes it available for debugging on all client containers, not just
  dev containers.
* allow access to https://localhost in test environment

#### mender (1.2.0)
* Refactored all store implementations into /store
* Improve error message when manifest field/file cannot be read.
* Fixed format check to conform to the expected artifact-file-format
  ([MEN-1289](https://tracker.mender.io/browse/MEN-1289))
* installer: improve incompatible image error message
* Client will not run state scripts from cmd-line except when forced.
  ([MEN-1235](https://tracker.mender.io/browse/MEN-1235))
* Fixed behaviour when no sys-cert is available on the system.
  ([MEN-1151](https://tracker.mender.io/browse/MEN-1151))
* Mender now logs whatever a state-script outputs to stderr
  ([MEN-1349](https://tracker.mender.io/browse/MEN-1349))
* Fix misleading version being displayed for non-tagged builds.
  ([MEN-1178](https://tracker.mender.io/browse/MEN-1178))
* Changed the errormessage to more closely reflect the issue.
  ([MEN-1215](https://tracker.mender.io/browse/MEN-1215))
* Removed the DeviceKey option in menderConfig.
* Fix - Now throws an error when committing nothing.
  ([MEN-505](https://tracker.mender.io/browse/MEN-505))
* Introduction of state script feature. State scripts can be
  used to execute scripts at various stages of Mender's execution. See
  documentation for more information.
* Introduce experimental support for writing to UBI volumes
* Logs an error when device_type file not found.
  ([MEN-505](https://tracker.mender.io/browse/MEN-505))
* remove no longer referenced client certificate code

#### mender-api-gateway-docker (1.2.0)
* Return additional headers for improved security: X-XSS-Protection, Cache-Control, Pragma. ([MEN-1316](https://tracker.mender.io/browse/MEN-1316))
* Validate Origin header if present. ([MEN-1287](https://tracker.mender.io/browse/MEN-1287))
* Add a configurable Host whitelist to gateway configuration, denying requests with unknown Hosts. Configured through ALLOWED_HOSTS env var on gateway startup. ([MEN-1262](https://tracker.mender.io/browse/MEN-1262))

#### mender-artifact (2.1.0)
* Sign existing artifacts using mender-artifact CLI
  ([MEN-1220](https://tracker.mender.io/browse/MEN-1220))
* Improve error message when private signing key can't be loaded.
* Fix misleading version being displayed for non-tagged builds.
  ([MEN-1178](https://tracker.mender.io/browse/MEN-1178))
* Mender-Artifact now returns an error code to the os on cli errors
  ([MEN-1328](https://tracker.mender.io/browse/MEN-1328))
* mender-artifact now fails with whitespace in the artifact-name
  ([MEN-1355](https://tracker.mender.io/browse/MEN-1355))

#### useradm (1.2.0)
* Improve log messages when opening connection to MongoDB.
* Additional MongoDB configuration options: mongo_ssl, mongo_ssl_skipverify, mongo_username, mongo_password
* Remove 'initial user' login logic, including 'POST /users/initial' API. Now initial user need to be created by administrator using cli ([MEN-1034](https://tracker.mender.io/browse/MEN-1034))
* New cli subcommand for creating users: 'useradm create-user. ([MEN-1034](https://tracker.mender.io/browse/MEN-1034))
* New API for listing users: 'GET https://localhost/api/management/v1/useradm/users' and 'GET https://localhost/api/management/v1/useradm/users/:userid'
* New API for creating additional users: 'POST https://localhost/api/management/v1/useradm/users'
* New API for editing user email and password: 'PUT https://localhost/api/management/v1/useradm/users/:userid'
* New API for removing user: 'DELETE https://localhost/api/management/v1/useradm/users/:userid'


## Mender v1.1.0

_Released 06.16.2017_

#### gui

* Remove shortened device IDs, now useless due to incremental SHAs
* Fix for [MEN-1233](https://tracker.mender.io/browse/MEN-1233) - create deployment from single device

#### mender

* Fix misleading version being displayed for non-tagged builds. ([MEN-1178](https://tracker.mender.io/browse/MEN-1178))


## Mender v1.1.0 Beta 1

_Released 05.24.2017_

#### deployments
* Increase file upload request validity when pushing artifact to remote file storage.
* Update artifact handling reflecting changes in mender-artifact.
* Support for signed images introduced, but with no signature
  verification yet. ([MEN-1022](https://tracker.mender.io/browse/MEN-1022))
* Add device decommissioning support in the deployments service.
* Update artifact description when updating artifact data.
* images/s3: unmarshal S3 errors when uploading image
* Artifact upload error handling fixed.
* Update artifact description when updating artifact data. ([MEN-1093](https://tracker.mender.io/browse/MEN-1093))
* travis: bump required Go version to 1.8

#### deviceadm
* Support for listing device authentication data sets with device ID
  filter using GET /devices?device_id=<devid>

#### deviceauth
* New feature: decommissioning device
* devauth: improve logging when rejecting or giving out tokens
* Decommission device endpoint implemented (without
  decommission job submit).
* api/management: management API is publicly available, update misleading description
* api: add tenant_token as an optional attribute in authentication request

#### gui
* Artifact signed field and improvements ([MEN-230](https://tracker.mender.io/browse/MEN-230))
* Bugfix: hide placeholder when past deployments is not empty ([MEN-229](https://tracker.mender.io/browse/MEN-229))
* Device blocking & decommissioning ([MEN-226](https://tracker.mender.io/browse/MEN-226))
* Implement pagination UI on pending & in progress deployment lists ([MEN-222](https://tracker.mender.io/browse/MEN-222))

#### integration
* Upgrade all server components to 1.1 series
* Upgrade client to 1.1
* Upgrade mender-artifact to 2.0

#### inventory
* No changes

#### mender-api-gateway-docker
* nginx: log and pass X-MEN-RequestID

#### mender-artifact
* Switch default artifact format version to 2. ([MEN-1183](https://tracker.mender.io/browse/MEN-1183))
* Add CLI support for signing and verifying images.
* Add implementation of RSA and ECDSA signatures.
* Fix returning and printing errors form artifact library.
* Fix overwriting artifact if new one is invalid.
* Add basic signing functionality and rewrite the library.

#### mender
* Add support for using signed mender-artifact library.
* Add support for verifying artifact signature. ([MEN-1020](https://tracker.mender.io/browse/MEN-1020))

#### useradm
* Added `create-user` and `server` commands to useradm. Running
  `useradm server` will start useradm service (just like running `useradm` did),
  also if no command is passed `server` is used a default. `create-user` will add
  given user to DB. Examples: `useradm create-user --username foo@bar.com
  --password foobarbarbar` (creates a user with username foo@bar.com and password
  foobar...), `useradm create-user --username foo@bar.com` (same as before, but
  password is read from terminal). See `--help` for details.


## Mender v1.0.1
_Released 04.05.2017_

### Notable changes

#### deployments

* Update artifact description when updating artifact data. (MEN-1093)
* Fix log flag not being set for device deployment after log been uploaded.
  (MEN-1078)

#### gui

* Bugfix: open correct deployment report dialog from dashboard
* Update node modules, add drag+drop artifact, allow edit
  artifact description
* Move user token from local storage to cookie, add react-cookie module (#217)
* Update node modules, add drag+drop & cookie functionality (#219)
* Replace artifact upload dialog with drag-and-drop
* Remove cookie when receiving unauthorized response
* Edit artifact description in UI

#### mender

* Fix bug that caused the update not to be retried after failing during
  previous attempt (#193)

---

## Mender v1.0.0 
_Released 02.20.2017_

---
