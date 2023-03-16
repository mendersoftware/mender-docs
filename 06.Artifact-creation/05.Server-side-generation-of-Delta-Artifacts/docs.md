---
title: Server-side generation of Delta Artifacts
taxonomy:
    category: docs
    label: tutorial
---

Mender Enterprise supports the server-side generation of Delta Artifacts.
This document explains the prerequisites to enable this feature and how it works.


### Prerequisites

#### Hosted Mender

! The server side delta is in a beta testing stage for the enterprise plan.
! For the moment it is possible to express interest to be added to the waiting list for the testing.
! In order to do so, please contact the [Hosted Mender support team](mailto:support@mender.io).


#### On-premise installations

In case of installations in your own infrastructure, there is additional step required: setting the configuration
in the deployments service. To this end, and in order to enable the server side delta generation, you have to call
an internal endpoint like that:

```bash
TENANT_ID=your_tenant_id
curl -v -H "Content-Type: application/json;" -XPUT -d '{ "delta": { "enabled": true, "binary_delta_limits": { "jobs_in_parallel": { "max": 2 }, "queue_length": { "max": 4 } }, "binary_delta": { "timeout": 3600 } } }' http://mender-deployments:8080/api/internal/v1/deployments/tenants/${TENANT_ID}/config
```

Where `your_tenant_id` stands for the id of your tenant for which you enable the feature.

#### Requirements on a device

To support the server-side generation of Delta Artifacts, your device must report the availability of the `mender-binary-delta` Update Module to the server.
This will happen automatically if you are building your firmware using Yocto and the `meta-mender` layer.
Otherwise, create and install your own bootstrap Artifact to provide these keys:

```bash
mender-artifact write bootstrap-artifact \
    --artifact-name mender-binary-delta-provide-keys \
    --device-type <dev-type> \
    --provides "rootfs-image.update-module.mender-binary-delta.mender_update_module:mender-binary-delta" \
    --provides "rootfs-image.update-module.mender-binary-delta.version:<version>" \
    --output-path mender-binary-delta-provide-keys.mender
```

The Artifact can be installed in standalone mode or remotely deployed with the Mender server.

<!--AUTOVERSION: "mender-artifact/blob/%"/ignore-->
Additionally, to make the server-side generation of Delta Artifacts possible, the Mender Artifact of the current version of the [`rootfs-image`](https://github.com/mendersoftware/mender-artifact/blob/3.9.0/Documentation/artifact-format-v3.md#header-info) running on your device and the updated one must be available as Artifact on the Mender Server.


### Enabling the server-side generation of Delta Artifacts

You can enable this feature by selecting the option "Generate and deploy Delta Artifacts (where available)" when you create a deployment for your devices. This option will enable the server-side generation of Delta Artifacts when turned on.

![Mender logo](deployment.jpg)

When you target a device running the Mender Client and the Binary Delta Update Module (see Prerequisites above for details) with a deployment where this option is active, the Mender Server tries to look up the correct Delta Artifact from the firmware (`rootfs`) version currently running on the Device to the desired version you selected with the deployment.

If the Delta Artifact already exists, the Mender Server selects it and sends the corresponding deployment instructions to the Device. However, if the Delta Artifact does not exist, it will start a Delta Artifact generation job in the background to create it. In this case, the Device will temporarily receive a `No updates` response for the Server. The resulting Delta Artifact will be served to the Device in the next update polling cycle after the generation has finished.

Please note that if the Server cannot generate the Delta Artifact, it will automatically fall back to the non-Delta Artifact. Possible reasons are:
* the Device is not reporting the availability of the Binary Delta Update Module through the `provides` database keys;
* the Mender Artifact containing the firmware (`rootfs`) version the Device is currently running on is not available in the Mender Server.


### Configuration settings

You can customize the Delta Artifact generation settings in the Global settings of your tenant.
You can specify a timeout for the generation job; the Mender Server will serve the full image if the server-side generation of the Delta Artifact takes more than the given amount of seconds.
You can also set the xDelta3 arguments to customize the Delta generation and the compression level.
Please refer to the [Create a Delta update Artifact](../05.Create-a-Delta-update-Artifact/) chapter for more information about the available options.

![Mender logo](settings.jpg)

The settings apply to the newly generated Delta Artifacts only. Existing Delta Artifacts previously uploaded to the Mender Server won't be affected by the changes to these values.

### Server side delta generation decision

The Mender Server makes the decision to trigger the binary delta generation based on the following:

* `rootfs.version` which device reports
* `rootfs.chksum` which device reports
* existence of full rootfs artifact in the tenant account that matches exactly the two above

If and only if all of the above, together with the existence of `mender-binary-delta` reported
in available `update_modules` by a device is fulfilled the server will trigger the generation
of binary delta artifact and automatically offer it for deployment.
