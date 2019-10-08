---
title: Install a Mender demo server
taxonomy:
    category: docs
---

! Following this tutorial will create a demo installation of the Mender, appropriate for testing and experimenting. When you are ready to install for production, please follow the [Production installation documentation](../../administration/production-installation).


## Bring up the environment with Docker Compose

! Make sure you satisfy the [server requirements](../requirements#demo-server-requirements) before proceeding.

In a working directory, download the Mender integration
environment:

<!--AUTOVERSION: "-b %"/integration "integration-%"/integration -->
```bash
git clone -b 2.2.0b1 https://github.com/mendersoftware/integration.git integration-2.2.0b1
```

<!--AUTOVERSION: "integration-%"/integration -->
```bash
cd integration-2.2.0b1
```

! Mender currently requires two entries in your `/etc/hosts` file to work with the Docker networking (typically `127.0.0.1 s3.docker.mender.io` and `127.0.0.1 docker.mender.io`). If these entries do not exist as you run the `demo up` script (below), it will create them for you and thus might ask for your administrative password. If you want to avoid automatic creation, you can create the entries in advance; look inside the script for the details on how it is created on your host.

Mender comes with a wrapper script that brings up the environment with
Docker Compose. Running this script will pull down the images and start them:


```bash
./demo up
```

!!! If this is the first time you start the Mender server, several gigabytes of Docker images may need to be downloaded. On a 100Mbit Internet connection this may take 5 minutes.

After the Docker images have been downloaded, the `demo up` script starts the Mender services, adds a demo user with the username `mender-demo@example.com`, and assigns a random password.

Note that this password is not stored anywhere in the Mender demo environment. Make sure to **copy this password** for logins to this instance of the demo environment. You can change it after you log in to the Mender UI (below).

!!! For Mender on-premise installations, your email and password are currently only used to log in to the Mender server. You will not receive any email from Mender. However, this might change in future versions so we recommend to input your real email address.


## Open the Mender UI

For security reasons, the Mender gateway only allows secure connections using TLS,
both for communicating with devices and end users.
Your web browser will communicate directly with the gateway while using the
Mender UI and therefore the certificate the gateway is using needs to be trusted
by your web browser.

The Mender UI can now be found on [https://localhost/](https://localhost/?target=_blank) -
simply open it in your web browser and **accept the certificate**. In Chrome it should look
like the following:

![Accept certificate - Chrome](cert_accept_chrome.png)

Log in with `mender-demo@example.com` as your email and the password that was generated above.

**Congratulations!** You have the Mender server running!

__Follow the help tooltips__ in the UI to guide you through each step of deploying to a device - accepting the device, viewing information about it, uploading an Artifact file, and finally deploying your very first update to the device.

!!! If you don't see the help tooltips, there is an option to toggle them on/off from the dropdown at your user email up at the top right corner of the screen.

We strongly recommend that you complete the onboarding tutorial that comes with the UI so
that you have a basic understanding of how Mender works before moving on to [Install the Mender client](../install-the-mender-client).
