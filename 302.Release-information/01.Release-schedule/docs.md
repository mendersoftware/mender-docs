---
title: Release schedule
taxonomy:
    category: docs
---

Our requirements for release quality are always the same, with only the length of support differing between non-LTS releases and LTS releases.
LTS releases are maintained through patch releases for one year, whereas non-LTS releases get patch releases only if an urgent vulnerability is found between minor releases.

The lifecycle of an LTS release begins on the release date and ends one year later at the scheduled support end date. Keeping these dates in mind helps decide which version to adopt and when to upgrade to a new version. To ensure the optimal operation of Mender within a release lifecycle, the release components should use any released patch updates once they become available.

##### Current LTS releases

<!-- the version number includes the patch release here, to get picked up by autoversion, but will be a minor version in the result -->
<!--AUTOVERSION: "LTS releases: %"/lts -->
At this time, we support the following LTS releases: 3.3.


| LTS         | Supported until |
| ----------- | --------------- |
| 3.3         |  2023-06        |
| 3.0         |  2022-07        |

#### Release Cadence

New minor version releases are released approximately every three months, either as a normal or LTS release. LTS minor releases are released every six months, but version numbers may vary depending on the content of the release. Check back here to learn which versions are part of an LTS release series.

Patch releases for LTS releases are published at the same time as a regular release is scheduled, unless an urgent vulnerability is discovered.
