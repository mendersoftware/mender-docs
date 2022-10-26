---
title: Release & support policy
taxonomy:
    category: docs
---


####  Release Cadence

New releases are released approximately every three months, either as an LTS (Long Term Support) or a non-LTS.

####  Support policy

**LTS**
* LTS (Long Time Supported release) are maintained through patch releases for one year
* Non critical patch releases for LTS are published within a month after the latest release
* In case of an urgent vulnerability discovered, the LTS can be released earlier
* The lifecycle of an LTS begins on the release date and ends one year later - the table below lists those dates

**Non-LTS**
* If the Non-LTS is the latest release, it might get a patch releases in the exceptional case of an urgent vulnerability
* Any non-LTS which isn't the latest release version will never get patch releases


Example

```
2022-06   3.3.0     LTS is released
2022-09   3.4.0     Non-LTS is released
2022-10   3.3.1     LTS is released - a patch version of 3.3
2022-09   3.4.0     Non-LTS is released
2022-12   3.5.0     Non-LTS is released
2023-01   3.3.2     LTS is released - a patch version of 3.3
```


#### Current LTS releases

<!-- the version number includes the patch release here, to get picked up by autoversion, but will be a minor version in the result -->
<!--AUTOVERSION: "LTS releases: %"/lts -->
At this time, we support the following LTS releases: 3.3.


| LTS         | Supported until |
| ----------- | --------------- |
| 3.3         |  2023-06        |
| 3.0         |  2022-07        |
