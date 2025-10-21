---
title: Yocto Project
taxonomy:
    category: docs
---

!!!!! Mender Orchestrator is only available in the Mender Enterprise plan.
!!!!! See [the Mender plans page](https://mender.io/pricing/plans?target=_blank)
!!!!! for an overview of all Mender plans and features.

!!! Mender Orchestrator requires DeviceTier to be set to "system" for proper operation.

This guide walks you through installing Mender Orchestrator on devices using the Yocto Project build system.

See [Yocto chapter](../../../05.Operating-System-updates-Yocto-Project/) for general information.

## Prerequisites

Before integrating Mender Orchestrator into your Yocto build, ensure you have a properly configured
Yocto build environment with meta-mender layers and the Mender Orchestrator sources downloaded through
the links below.

<!--AUTOVERSION: "% recipe"/ignore -->
!!! Mender Orchestrator requires the master recipe of the Mender Client. Support for Mender Orchestrator will be released in the next feature release. See the [Yocto Project documentation](../../../05.Operating-System-updates-Yocto-Project/03.Build-for-demo/docs.md#configuring-the-build) for information on using bleeding edge versions.

### Download

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="hosted"]
Set your credentials:
```bash
HOSTED_MENDER_EMAIL=<your.email@example.com>
```

Download the source archive:
<!--AUTOVERSION: "/mender-orchestrator/yocto/%/"/mender-orchestrator "/mender-orchestrator-%.tar.xz"/mender-orchestrator -->
```bash
curl --fail -u $HOSTED_MENDER_EMAIL -o ${HOME}/mender-orchestrator-0.4.0.tar.xz https://downloads.customer.mender.io/content/hosted/mender-orchestrator/yocto/0.4.0/mender-orchestrator-0.4.0.tar.xz
```
[/ui-tab]
[ui-tab title="enterprise"]
Set your credentials:
```bash
MENDER_ENTERPRISE_USER=<your.user>
```

Download the source archive:
<!--AUTOVERSION: "/mender-orchestrator/yocto/%/"/mender-orchestrator "/mender-orchestrator-%.tar.xz"/mender-orchestrator -->
```bash
curl --fail -u $MENDER_ENTERPRISE_USER -o ${HOME}/mender-orchestrator-0.4.0.tar.xz https://downloads.customer.mender.io/content/on-prem/mender-orchestrator/yocto/0.4.0/mender-orchestrator-0.4.0.tar.xz
```
[/ui-tab]
[/ui-tabs]

## Demo layer (evaluation)

For evaluation and testing purposes, you can use the demo layer before proceeding to production setup:

```bash
bitbake-layers add-layer ../sources/meta-mender/meta-mender-demo
```

The `meta-mender-demo` layer provides a mock environment with a corresponding Topology for testing and demonstration purposes.

!!! The demo configuration is inappropriate for production devices.

## Integration


Add the `meta-mender-commercial` layer to your build:

```bash
bitbake-layers add-layer ../sources/meta-mender/meta-mender-commercial
```

Accept the commercial license by adding to your `local.conf`:

```bash
LICENSE_FLAGS_ACCEPTED:append = " commercial_mender-yocto-layer-license"
```

Point the `mender-orchestrator` recipe to the downloaded tarball:

<!--AUTOVERSION: "/mender-orchestrator-%.tar.xz"/mender-orchestrator -->
```bash
SRC_URI:pn-mender-orchestrator = "file://${HOME}/mender-orchestrator-0.4.0.tar.xz"
```

Include Mender Orchestrator in your image:

```bash
IMAGE_INSTALL:append = " mender-orchestrator"
```

Set the DeviceTier to "system":

```bash
MENDER_DEVICE_TIER = "system"
```

We also provide [mender-orchestrator-support](https://github.com/mendersoftware/mender-orchestrator-support),
an open-source repository containing Interfaces, Update Modules and Inventory scripts when
using Mender Orchestrator together with the Mender Client. To include this in your image, add:

```bash
IMAGE_INSTALL:append = " mender-orchestrator-support"
```

Your `local.conf` should now contain:

<!--AUTOVERSION: "/mender-orchestrator-%.tar.xz"/mender-orchestrator -->
```bash
LICENSE_FLAGS_ACCEPTED:append = " commercial_mender-yocto-layer-license"
SRC_URI:pn-mender-orchestrator = "file://${HOME}/mender-orchestrator-0.4.0.tar.xz"
IMAGE_INSTALL:append = " mender-orchestrator mender-orchestrator-support"
MENDER_DEVICE_TIER = "system"
```

## Production installation

For production deployments, provision a [Topology](../../03.Topology/docs.md) that defines the Components of your System.

To include your Topology file in the Yocto build, add this to your `local.conf`:

```bash
FILESEXTRAPATHS:prepend := "/path/to/local-directory-with-topology.yaml:"
SRC_URI:pn-mender-orchestrator:append = " file://topology.yaml"
```

Replace `/path/to/local-directory-with-topology.yaml` with the actual path to the directory containing your `topology.yaml` file.
