---
title: Quickstart with Raspberry Pi
taxonomy:
    category: docs
---

Quickly and easily deploy your first over-the-air (OTA) software update with Mender using a secure server we host for you. We will take you through installing Mender on your device and deploying a simple *application update* on your Raspberry Pi and Raspbian OS.


## Prerequisites

To follow this guide, you will need the following:

* A [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b?target=_blank) or [B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus?target=_blank), or a [Raspberry Pi 4 Model B](https://www.raspberrypi.org/products/raspberry-pi-4-model-b?target=_blank).
* An 8 GB or larger microSD card.
* A Raspberry Pi [universal power supply](https://www.raspberrypi.org/products/raspberry-pi-universal-power-supply?target=_blank) or a micro USB cable.
* Internet connectivity for your Raspberry Pi (either Ethernet or wifi configured)
* A Mender Professional account to access the [hosted server](https://hosted.mender.io).


### Get a Mender Professional account

Get a Mender account by [signing up here](https://mender.io/signup?target=_blank).

!!! We provide $120 free credit for you to use for evaluation. You can cancel at any time without incurring a cost while your usage remains under $120.

You can also try it on-premise, but it requires more effort getting setup. See the [on-premise instructions below](#running-mender-on-premise).


### Prepare your device

Make sure your Raspberry Pi has Raspbian OS installed. 

* Download our pre-converted Raspbian OS image from [here][raspbian-buster-lite-mender.img.xz].
* [Follow the steps from raspberry.org](https://www.raspberrypi.org/documentation/installation/installing-images?target=_blank) to install the OS image to your device and [enable SSH](https://www.raspberrypi.org/documentation/remote-access/ssh/README.md?target=_blank) on your device. This should take less than 15 minutes.

!! Note that we do not offer commercial support for these images. They are based
!! on images supported by board manufacturers, like the Raspberry Pi Foundation,
!! and provide the same software and configuration options as the original
!! images. Please use the support resources available from the board
!! manufacturer, or [contact us](mailto:contact@mender.io) if you have any
!! questions on the Mender integration.

Your first deployment is easy with 5 short steps:

<!-- The reason the Mender version below is set to "ignore" is that the Raspbian
download is built separately from the Mender product, in the mender-convert
pipeline, and this is not guaranteed to follow the latest Mender releases. It
may be skipped for some patch releases, for instance. -->
<!--AUTOVERSION: "mender-%.img.xz"/ignore "mender-%.mender"/ignore -->
[raspbian-buster-lite-mender.img.xz]: https://d4o6e0uccgv40.cloudfront.net/2019-09-26-raspbian-buster-lite/arm/2019-09-26-raspbian-buster-lite-mender-master.img.xz


### Step 1 - SSH into your Raspberry Pi device 

SSH into your device:

```bash
ssh pi@<DEVICE-IP-ADDRESS>
```

The default password for the pi account is `raspberry`.

You should now see a command prompt similar to the following:

```bash
pi@raspberrypi:~ $
```

Keep this terminal open as we will shortly use it to install the Mender client.


### Step 2 - Login to Mender Professional

Login to your [Mender Professional account](https://hosted.mender.io/ui/#/login?target=_blank), and when on the main page for the first time new users will get a tutorial in the Mender web GUI.

Go to the **Dashboard** tab and click on **Connect a device**. Then Click on **Connect my own device**. Select your Raspberry Pi model and click **Next**. You should see a screen similar to the below. Keep this open as we will use it in the next step.

![connecting a device](image_0.png)


### Step 3 - Install the Mender client on your device

Next we will install the Mender client on your device and connect it to the Mender server.

In the dialog box from step 2, click **Copy to clipboard** to copy the code to install the Mender client. Now go to the command line on your device from step 1, and **paste** the code e.g. by right-clicking in the terminal and selecting *Paste*, followed by *Enter*.

This downloads the Mender client on the device, configures and starts it.

Once the client has started, the Mender client will attempt to connect to the server and it will appear in your Pending devices tab in the server. Go ahead and **Accept** the pending device in the server. After accepting the device, it will appear on the Device groups tab on the left of Pending.

![accepting the device](image_1.png)


### Step 4 - Create a Deployment 

There is already a mender-demo Artifact available under *Releases* the first time you use Mender. It contains a small web server your device can run.

Go to the **Deployments** tab and select the target release already available and click **Create deployment** as shown below.

![create a deployment](image_3.png)

After about 30 seconds you see your finished deployment in the *Finished* tab. There should also be a tooltip to the URL of your deployed web server.

![congratulations server](image_4.png)

Once you access your device using the URL shown in the tooltip under the *Finished* tab you should see a welcome page similar to the following.

![congratulations device](image_5.png)

**Congratulations!** You have successfully deployed an application update using Mender!


### Step 5 - Modify the application

The onboarding tooltips should now take you through modifying the web page you saw in step 4, using tools to generate Mender Artifact (.mender) files.
Simply follow the tooltips to update your newly deployed application!


## Running Mender on-premise

For the easiest and fastest experience, we recommend using the hosted version of Mender for your first evaluation. You can also try the same deployment above using the on-premise version by installing a Mender demo server on a host machine, however this will take you a bit longer. You will need to install [Docker Engine](https://docs.docker.com/install/linux/docker-ce/ubuntu?target=_blank) (on device) and [Docker Compose](https://docs.docker.com/compose/install?target=_blank) in your deployment environment. 

Next, you will need to download the Mender integration environment in the working directory:

<!--AUTOVERSION: "-b % https://github.com/mendersoftware/integration.git"/integration-->
```
git clone -b 2.2.0 https://github.com/mendersoftware/integration.git integration

cd integration
```

And finally fire up the demo server environment with:

```
./demo up
```

Note that the demo up script starts the Mender services, adds a demo user with the username mender-demo@example.com, and assigns a random password in which you can change after you log in to the Mender web UI. The Mender UI can be found on [https://localhost](https://localhost?target=_blank).

After you log into the UI on the localhost you can follow steps 1 through 5 listed above. 

## Have any questions? 

If you need help and have any questions:

* Visit our community forum at [Mender Hub](https://hub.mender.io/) dedicated to OTA updates where you can discuss any issues you may be having. Share and learn from other Mender users.

* Learn more about Mender by reading the rest of the documentation. 

[Compare plans](https://mender.io/products/pricing?target=_blank) and choose a plan that fits your requirements. 

