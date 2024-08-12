---
title: Release version and schedule
taxonomy:
    category: docs
---

There are two Mender release types:

* LTS (Long Term Support)
* non-LTS (Standard Support)

Our quality requirements for both release types are the same, the only difference between LTS and non-LTS releases is the support length. We maintain LTS releases through patch releases for one year from the release date. In contrast, non-LTS releases get patch releases only if an urgent vulnerability is found between the release date and the next release.

Keeping this distinction in mind helps decide which version to adopt and when to upgrade to a new version. In addition, ensure you are always using the latest available patch releases for the optimal operation of Mender.


##### Versioning

Mender users [Semantic Versioning](https://semver.org), and the version numbers are in the `MAJOR.MINOR.PATCH` format.

We increment:

* `MAJOR` version when we make incompatible API changes
* `MINOR` version when we add functionalities in a backward compatible manner
* `PATCH` version when we make backward compatible bug fixes to existing releases

!!! By design, the Mender Backend is always backward compatible with older versions of the Mender Client. Therefore, incrementing the `MAJOR` version means that the Mender Client (generally speaking, the client components) depend on a corresponding `MAJOR` version of the Management Server. However, any older Mender Client will still work with a Management Server running a more recent version.


#### Release Cadence

We release a new version every three months, either as a non-LTS or LTS release. We publish LTS releases approximately every six months, but version numbers (e.g., major or minor version bumps) may vary depending on the release's content. Check back here to learn which versions are part of an LTS release series.

We publish patch versions for older LTS releases roughly the same time we publish the new minor or major releases unless we discover an urgent vulnerability that requires an immediate fix.


##### Current LTS releases

<!-- the version number includes the patch release here, to get picked up by autoversion, but will be a minor version in the result -->
<!--AUTOVERSION: "LTS releases: %"/lts -->
At this time, we support the following LTS releases: 3.7.

| LTS         | Supported until |
| ----------- | --------------- |
| 3.7         |  2025-05        |

Mender is versioned and released as a Product bundle, and the versions mentioned here refer to the Product bundle version.

Under the version of the Product bundle, there are multiple different components with their individual versioning. To see which component versions belong to a bundle, please refer to [this JSON file](https://docs.mender.io/releases/versions.json)


##### Yocto LTS support

Our [meta-mender Yocto layer](https://github.com/mendersoftware/meta-mender) supports the latest two Yocto LTS releases, which at this time are Kirkstone (4.0) and Dunfell (3.1).
