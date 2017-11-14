---
title: Deploy to virtual devices
taxonomy:
    category: docs
---

In this tutorial we will show how to use the intuitive Mender server UI
to deploy a full rootfs image update to a virtual device which is
connected to the server. The virtual device is bundled with the
Mender server to make it easy to test Mender.

A Mender Artifact is a file format that includes metadata like the
checksum and name, as well as the actual root file system that is
deployed. See [Mender Artifacts](../../architecture/mender-artifacts) for
a complete description of this format.


## Prerequisites

The test environment should be set up and working successfully
as described in [Install a Mender demo server](../create-a-test-environment) and
you should have downloaded the virtual Artifacts listed in
[Download demo images](../download-test-images).


## Authorize the device

Open the Mender UI in the same browser as you accepted the certificate
in as part of [Install a Mender demo server](../create-a-test-environment).
It is available at [https://localhost/](https://localhost/?target=_blank).

After a minute or two, there should be a virtual device that is pending authorization.
This means that the Mender client, which runs as a daemon on the device,
is asking to join the Mender server so that the server can manage
its deployments. You can also see these requests
in the server access logs in the terminal where you started the
Mender server.

You can review the device before authorizing it to join the server.
When you are ready, simply click the **Authorize** button
in the **Devices** tab.

! There are security implications to connecting a client and server for the first time, also known as *bootstrapping*. If a client and server have not exchanged any information in advance, they need to accept each other on trust this first time, with the risk that the information the other party presents is spoofed. To mitigate this risk, the Mender client preinstalls the TLS certificate of the server when it is provisioned, as part of the Yocto Project image build. So it is not possible for a rogue server to intercept the connection from a client or pretend to be a different server, assuming server's private TLS key is securely managed. A rogue device can still spoof the information it sends to the server in order to be authorized, and this is why Mender asks you to make the authorization decision. However, the risk of letting the server manage a rogue device is much lower than the risk of a rogue server managing devices.


## See information about the device

Mender automatically collects identity and inventory information
about the connected devices. You can view this information by
clicking on a device. It should look similar to the following:

![Mender UI - Device information](device_information_1_2_0.png)


!!! Which information is collected about devices is fully configurable; see the documentation on [Identity](../../client-configuration/identity) and [Inventory](../../client-configuration/inventory) for more information.

After deploying the update below, you can verify that the `artifact_name` of the virtual device has changed.

!!! The console of the virtual device can be seen by running `docker logs $(docker ps | grep mender-client | cut -f1 -d' ')`.


## Upload the Mender Artifacts to the server

Click the **Artifacts** tab in the Mender server UI.

Then locate the two Virtual device Artifacts you downloaded in [Download demo images](../download-test-images).
Upload them both, one at the time, with drag and drop or by clicking browse.

After the upload has finished, you should see both Artifacts, they have Device types compatibility `vexpress-qemu` and two different names.

!!! All devices report which *Device type* they are as part of their inventory information, for example `vexpress-qemu` or `beaglebone`. In addition, Mender Artifacts have *Device types compatible* as part of their metadata. During a deployment, Mender makes sure that a device will only get and install an Artifact it is compatible with. This increases the robustness of Mender as it avoids situations like deploying software that is not supported by the device hardware.


## Deploy the Mender Artifact to the device

Now that we have the device connected and the Artifact
uploaded to the server, all that remains is to go to the
**Deployments** tab and click **Create a deployment**.

You will be asked which Artifact to deploy and which
group of devices to deploy it to. Select
the `release-1` Artifact and **All devices**, then
**Create deployment**.


## See the progress of the deployment

As the deployment progresses, you can click on it to view more details about the current status across all devices.
In the example below, we can see that the device is in process of installing the Artifact.

![Mender UI - Deployment progress](deployment_report_1_2_0.png)

!!! The deployment to the virtual device should take about 2-5 minutes to complete and report success or failure.


## Verify the deployment

[start_autoupdate_release-2_x.x.x]: #

Once the deployment completes, you should see it in *Past deployments*.
If the deployment fails you can view the deployment log,
which is obtained from the device, to diagnose the issue.
You can also see the state of deployments on the Dashboard.
In **Devices** you can see that `artifact_name` has now changed to `release-2_1.2.1`.

[end_autoupdate_release-2_x.x.x]: #

This shows your virtual device runs the new rootfs!


## Deploy another update

!!! For robustness and avoiding unnecessary deployments, Mender will not deploy an Artifact that is already installed on a device.  Thus, if you create another deployment with the Artifact you already deployed, Mender will see that it contains the same rootfs that is already installed and skip the deployment. It will immediately be marked as successful and moved to *Past deployments*. This is why we provide a second Artifact for you to test with.

In order to create another deployment, go to the
**Deployments** tab and click **Create a deployment** again.
This time, select the `release-2` Artifact and
deploy it to your device, using the same steps as before.

Following this, you can deploy the first Artifact again, and so forth.


## Deploy to custom groups

As you might have noticed, it is possible to create
groups in the **Devices** tab. Once you have created a
group and added one or more devices to it, you can deploy
an Artifact to that group by selecting the group instead
of *All devices* when you create a deployment.

This can be very useful in order to deploy to test devices
before production, or only deploy to devices owned by a specific customer.

! To avoid accidents, Mender only allows **a device to be in one group at the time**. If a device could be in several groups, for example test *and* production, unintended deployments and downtime could occur. Therefore, as a safety measure, Mender does not allow this.


## Deploy to physical devices

**Congratulations!** You have used the Mender server to deploy your first managed update!
If you have a Raspberry Pi 3 or BeagleBone Black, you can proceed to
[Deploy to physical devices](../deploy-to-physical-devices) to try out deploying to a
real-world device!
