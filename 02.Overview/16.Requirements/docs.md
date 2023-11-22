---
title: Requirements
taxonomy:
    category: docs
---

## Working with Firewalls
The following URLs and access types need outgoing permissions in firewalls in order for Mender to work correctly:

[ui-tabs position="top-left" active="0" theme="default" ]
[ui-tab title="Hosted Mender US"]
**Hosted Mender access**: Devices, APIs and browser access
* `https://hosted.mender.io`
* `https://*.hosted.mender.io`

**Artifact storage access**: Devices, APIs and browser access
* `https://s3.amazonaws.com/hosted-mender-artifacts`
* `https://hosted-mender-artifacts.s3.amazonaws.com`
* `https://c271964d41749feb10da762816c952ee.r2.cloudflarestorage.com`  
    * **going into effect on December 4th, 2023 for Basic and Professional plans**

[/ui-tab]
[ui-tab title="Hosted Mender EU"]
**Hosted Mender access**: Devices, APIs and browser access
* `https://eu.hosted.mender.io`
* `https://*.eu.hosted.mender.io`

**Artifact storage access**: Devices, APIs and browser access
* `https://mender.blob.core.windows.net/artifacts`
* `https://c271964d41749feb10da762816c952ee.r2.cloudflarestorage.com`
    * **going into effect on December 4th, 2023 for Basic and Professional plans**

[/ui-tab]
[/ui-tabs]
