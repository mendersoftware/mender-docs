---
title: Debian family
taxonomy:
    category: docs
---

!!!!! Mender Orchestrator is only available in the Mender Enterprise plan.
!!!!! See [the Mender plans page](https://mender.io/pricing/plans?target=_blank)
!!!!! for an overview of all Mender plans and features.

!!! Mender Orchestrator requires DeviceTier to be set to "system" for proper operation.

This page provides instructions for downloading and installing the Mender Orchestrator Debian packages.

We also provide [mender-orchestrator-support](https://github.com/mendersoftware/mender-orchestrator-support),
an open-source repository containing Interfaces, Update Modules and Inventory scripts when
using Mender Orchestrator together with the Mender Client.

See [Debian family](../../../04.Operating-System-updates-Debian-family) section for general information.
See the [Downloads page](../../../12.Downloads/chapter.md) for links to general setup instructions and additional installation methods.

## Download

Download the Debian packages by selecting your deployment type and system architecture:

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="hosted"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="Debian 13"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="armhf"]
Set your email credential:
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
```

Download the package:
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$HOSTED_MENDER_EMAIL" -O https://downloads.customer.mender.io/content/hosted/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bdebian%2Btrixie_armhf.deb
```
[/ui-tab]
[ui-tab title="arm64"]
Set your email credential:
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
```

Download the package:
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$HOSTED_MENDER_EMAIL" -O https://downloads.customer.mender.io/content/hosted/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bdebian%2Btrixie_arm64.deb
```
[/ui-tab]
[ui-tab title="amd64"]
Set your email credential:
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
```

Download the package:
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$HOSTED_MENDER_EMAIL" -O https://downloads.customer.mender.io/content/hosted/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bdebian%2Btrixie_amd64.deb
```
[/ui-tab]
[/ui-tabs]

Download the mender-orchestrator-support package:
<!--AUTOVERSION: "/mender-orchestrator-support_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$HOSTED_MENDER_EMAIL" -O https://downloads.customer.mender.io/content/hosted/mender-orchestrator/debian/0.4.0/mender-orchestrator-support_0.4.0-1%2Bdebian%2Btrixie_all.deb
```

[/ui-tab]
[ui-tab title="Debian 12"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="armhf"]
Set your email credential:
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
```

Download the package:
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$HOSTED_MENDER_EMAIL" -O https://downloads.customer.mender.io/content/hosted/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bdebian%2Bbookworm_armhf.deb
```
[/ui-tab]
[ui-tab title="arm64"]
Set your email credential:
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
```

Download the package:
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$HOSTED_MENDER_EMAIL" -O https://downloads.customer.mender.io/content/hosted/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bdebian%2Bbookworm_arm64.deb
```
[/ui-tab]
[ui-tab title="amd64"]
Set your email credential:
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
```

Download the package:
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$HOSTED_MENDER_EMAIL" -O https://downloads.customer.mender.io/content/hosted/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bdebian%2Bbookworm_amd64.deb
```
[/ui-tab]
[/ui-tabs]

Download the mender-orchestrator-support package:
<!--AUTOVERSION: "/mender-orchestrator-support_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$HOSTED_MENDER_EMAIL" -O https://downloads.customer.mender.io/content/hosted/mender-orchestrator/debian/0.4.0/mender-orchestrator-support_0.4.0-1%2Bdebian%2Bbookworm_all.deb
```

[/ui-tab]
[ui-tab title="Ubuntu 24.04"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="armhf"]
Set your email credential:
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
```

Download the package:
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$HOSTED_MENDER_EMAIL" -O https://downloads.customer.mender.io/content/hosted/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bubuntu%2Bnoble_armhf.deb
```
[/ui-tab]
[ui-tab title="arm64"]
Set your email credential:
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
```

Download the package:
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$HOSTED_MENDER_EMAIL" -O https://downloads.customer.mender.io/content/hosted/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bubuntu%2Bnoble_arm64.deb
```
[/ui-tab]
[ui-tab title="amd64"]
Set your email credential:
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
```

Download the package:
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$HOSTED_MENDER_EMAIL" -O https://downloads.customer.mender.io/content/hosted/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bubuntu%2Bnoble_amd64.deb
```
[/ui-tab]
[/ui-tabs]

Download the mender-orchestrator-support package:
<!--AUTOVERSION: "/mender-orchestrator-support_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$HOSTED_MENDER_EMAIL" -O https://downloads.customer.mender.io/content/hosted/mender-orchestrator/debian/0.4.0/mender-orchestrator-support_0.4.0-1%2Bubuntu%2Bnoble_all.deb
```

[/ui-tab]
[ui-tab title="Ubuntu 22.04"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="armhf"]
Set your email credential:
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
```

Download the package:
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$HOSTED_MENDER_EMAIL" -O https://downloads.customer.mender.io/content/hosted/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bubuntu%2Bjammy_armhf.deb
```
[/ui-tab]
[ui-tab title="arm64"]
Set your email credential:
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
```

Download the package:
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$HOSTED_MENDER_EMAIL" -O https://downloads.customer.mender.io/content/hosted/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bubuntu%2Bjammy_arm64.deb
```
[/ui-tab]
[ui-tab title="amd64"]
Set your email credential:
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
```

Download the package:
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$HOSTED_MENDER_EMAIL" -O https://downloads.customer.mender.io/content/hosted/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bubuntu%2Bjammy_amd64.deb
```
[/ui-tab]
[/ui-tabs]

Download the mender-orchestrator-support package:
<!--AUTOVERSION: "/mender-orchestrator-support_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$HOSTED_MENDER_EMAIL" -O https://downloads.customer.mender.io/content/hosted/mender-orchestrator/debian/0.4.0/mender-orchestrator-support_0.4.0-1%2Bubuntu%2Bjammy_all.deb
```

[/ui-tab]

[/ui-tabs]

[/ui-tab]
[ui-tab title="enterprise"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="Debian 13"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="armhf"]
Set your username credential:
```bash
MENDER_ENTERPRISE_USER=<your.user>
```

Download the package:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$MENDER_ENTERPRISE_USER" -O https://downloads.customer.mender.io/content/on-prem/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bdebian%2Btrixie_armhf.deb
```
[/ui-tab]
[ui-tab title="arm64"]
Set your username credential:
```bash
MENDER_ENTERPRISE_USER=<your.user>
```

Download the package:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$MENDER_ENTERPRISE_USER" -O https://downloads.customer.mender.io/content/on-prem/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bdebian%2Btrixie_arm64.deb
```
[/ui-tab]
[ui-tab title="amd64"]
Set your username credential:
```bash
MENDER_ENTERPRISE_USER=<your.user>
```

Download the package:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$MENDER_ENTERPRISE_USER" -O https://downloads.customer.mender.io/content/on-prem/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bdebian%2Btrixie_amd64.deb
```
[/ui-tab]
[/ui-tabs]

Download the mender-orchestrator-support package:
<!--AUTOVERSION: "/mender-orchestrator-support_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$MENDER_ENTERPRISE_USER" -O https://downloads.customer.mender.io/content/on-prem/mender-orchestrator/debian/0.4.0/mender-orchestrator-support_0.4.0-1%2Bdebian%2Btrixie_all.deb
```

[/ui-tab]
[ui-tab title="Debian 12"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="armhf"]
Set your username credential:
```bash
MENDER_ENTERPRISE_USER=<your.user>
```

Download the package:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$MENDER_ENTERPRISE_USER" -O https://downloads.customer.mender.io/content/on-prem/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bdebian%2Bbookworm_armhf.deb
```
[/ui-tab]
[ui-tab title="arm64"]
Set your username credential:
```bash
MENDER_ENTERPRISE_USER=<your.user>
```

Download the package:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$MENDER_ENTERPRISE_USER" -O https://downloads.customer.mender.io/content/on-prem/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bdebian%2Bbookworm_arm64.deb
```
[/ui-tab]
[ui-tab title="amd64"]
Set your username credential:
```bash
MENDER_ENTERPRISE_USER=<your.user>
```

Download the package:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$MENDER_ENTERPRISE_USER" -O https://downloads.customer.mender.io/content/on-prem/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bdebian%2Bbookworm_amd64.deb
```
[/ui-tab]
[/ui-tabs]

Download the mender-orchestrator-support package:
<!--AUTOVERSION: "/mender-orchestrator-support_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$MENDER_ENTERPRISE_USER" -O https://downloads.customer.mender.io/content/on-prem/mender-orchestrator/debian/0.4.0/mender-orchestrator-support_0.4.0-1%2Bdebian%2Bbookworm_all.deb
```

[/ui-tab]
[ui-tab title="Ubuntu 24.04"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="armhf"]
Set your username credential:
```bash
MENDER_ENTERPRISE_USER=<your.user>
```

Download the package:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$MENDER_ENTERPRISE_USER" -O https://downloads.customer.mender.io/content/on-prem/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bubuntu%2Bnoble_armhf.deb
```
[/ui-tab]
[ui-tab title="arm64"]
Set your username credential:
```bash
MENDER_ENTERPRISE_USER=<your.user>
```

Download the package:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$MENDER_ENTERPRISE_USER" -O https://downloads.customer.mender.io/content/on-prem/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bubuntu%2Bnoble_arm64.deb
```
[/ui-tab]
[ui-tab title="amd64"]
Set your username credential:
```bash
MENDER_ENTERPRISE_USER=<your.user>
```

Download the package:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$MENDER_ENTERPRISE_USER" -O https://downloads.customer.mender.io/content/on-prem/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bubuntu%2Bnoble_amd64.deb
```
[/ui-tab]
[/ui-tabs]

Download the mender-orchestrator-support package:
<!--AUTOVERSION: "/mender-orchestrator-support_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$MENDER_ENTERPRISE_USER" -O https://downloads.customer.mender.io/content/on-prem/mender-orchestrator/debian/0.4.0/mender-orchestrator-support_0.4.0-1%2Bubuntu%2Bnoble_all.deb
```

[/ui-tab]
[ui-tab title="Ubuntu 22.04"]

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="armhf"]
Set your username credential:
```bash
MENDER_ENTERPRISE_USER=<your.user>
```

Download the package:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$MENDER_ENTERPRISE_USER" -O https://downloads.customer.mender.io/content/on-prem/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bubuntu%2Bjammy_armhf.deb
```
[/ui-tab]
[ui-tab title="arm64"]
Set your username credential:
```bash
MENDER_ENTERPRISE_USER=<your.user>
```

Download the package:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$MENDER_ENTERPRISE_USER" -O https://downloads.customer.mender.io/content/on-prem/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bubuntu%2Bjammy_arm64.deb
```
[/ui-tab]
[ui-tab title="amd64"]
Set your username credential:
```bash
MENDER_ENTERPRISE_USER=<your.user>
```

Download the package:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "/mender-orchestrator-core_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$MENDER_ENTERPRISE_USER" -O https://downloads.customer.mender.io/content/on-prem/mender-orchestrator/debian/0.4.0/mender-orchestrator-core_0.4.0-1%2Bubuntu%2Bjammy_amd64.deb
```
[/ui-tab]
[/ui-tabs]

Download the mender-orchestrator-support package:
<!--AUTOVERSION: "/mender-orchestrator-support_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$MENDER_ENTERPRISE_USER" -O https://downloads.customer.mender.io/content/on-prem/mender-orchestrator/debian/0.4.0/mender-orchestrator-support_0.4.0-1%2Bubuntu%2Bjammy_all.deb
```

[/ui-tab]

[/ui-tabs]

[/ui-tab]
[/ui-tabs]


## Installation

Install the downloaded package:

<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "mender-orchestrator-core%-1"/mender-orchestrator -->
```bash
sudo dpkg -i mender-orchestrator-core_*.deb
```

The package provides the `mender-orchestrator` binary and support files for integration with Mender Client and Mender Server.

Install the mender-orchestrator-support package:

<!--AUTOVERSION: "mender-orchestrator-support%-1"/mender-orchestrator -->
```bash
sudo dpkg -i mender-orchestrator-support_*.deb
```

## Demo package (optional)

For evaluation, download and install the demo package:

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="hosted"]
<!--AUTOVERSION: "/mender-orchestrator-demo_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$HOSTED_MENDER_EMAIL" -O https://downloads.customer.mender.io/content/hosted/mender-orchestrator/debian/0.4.0/mender-orchestrator-demo_0.4.0-1%2Bdebian%2Bbookworm_all.deb
```
[/ui-tab]
[ui-tab title="enterprise"]
<!--AUTOVERSION: "/mender-orchestrator-demo_%-1"/mender-orchestrator "/mender-orchestrator/debian/%/"/mender-orchestrator -->
```bash
curl --fail -u "$MENDER_ENTERPRISE_USER" -O https://downloads.customer.mender.io/content/on-prem/mender-orchestrator/debian/0.4.0/mender-orchestrator-demo_0.4.0-1%2Bdebian%2Bbookworm_all.deb
```
[/ui-tab]
[/ui-tabs]

Install the demo package:

<!--AUTOVERSION: "mender-orchestrator-demo%-1"/mender-orchestrator -->
```bash
sudo dpkg -i mender-orchestrator-demo_*.deb
```

The demo package provides a mock environment with a corresponding Topology for testing and demonstration purposes.

!!! The demo configuration is inappropriate for production devices.

## Configuration

Set the DeviceTier to "system" in your `mender.conf`

For production deployments, provision a [Topology](../../02.Topology/docs.md) that defines the components of your system.

Create your Topology configuration file at `MENDER_ORCHESTRATOR_TOPOLOGY_DIR` (default: `/data/mender-orchestrator/topology.yaml`).
