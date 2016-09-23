---
title: Create a test environment
taxonomy:
    category: docs
---

!! This tutorial should only used in an internal environment (e.g. on your workstation) for testing purposes. Several important security features need to be implemented before using Mender in production, including random generation of keys, user authentication for managing deployments and more.

Mender consists of a [server and updater client](../../Architecture/overview).
The Mender server is using the microservices design pattern, meaning that
multiple small, isolated services make up the server. The Mender updater client
is designed to run on embedded Linux devices and connects to the server
so that deployments can be managed across many devices.

In order to make it easy to test Mender as a whole, we have created a
docker compose environment that brings all of these components up
and connects them together. It even includes a service that runs a
virtual device using [Quick Emulator (QEMU)](http://qemu.org),
which is handy because it means that you can test the client without
having to configure any hardware.

! The docker compose environment currently uses internal networking, so physical devices can not currently be connected directly to this environment. We will enable this shortly, however please test with the virtual device in the meanwhile.


## Prerequisites

#### OS and web browser

We assume you are using **Ubuntu 16.04** with **Google Chrome** as web browser.
It is very likely possible to use the test environment on other platforms,
but using this platform is known to work.

#### Docker Engine and Compose

Your workstation needs a recent version of docker engine and docker compose installed
and working. ( **TODO** : overview, Install steps & links to docker compose).

#### Fast Internet connection

While bringing up the environment, several hundred megabytes of docker
images may be downloaded. We recommend using a fast Internet
connection in order to avoid long wait times.


## Bring up the environment with docker compose

**TODO** : document where to get integration/stable

In a dedicated terminal, go to the integration directory that
contains the file `docker-compose.yml`:

```
cd integration
```

!!! This terminal will be locked while Mender is running as it will output logs from all the services.

! Mender currently requires an entry `127.0.0.1 mender-artifact-storage.localhost` in your `/etc/hosts` file to work with the docker networking. This requirement is temporary and will be removed shortly. If this entry does not exist as you run the `up` script (below), it will create it for you and thus might ask for your administrative password. You can also create this entry in advance if you want to avoid automatic creation.

Mender comes with a wrapper script that brings up the environment with
docker compose. Running this script will pull down the images and start them:


```
./up
```

As the Mender services start up, you will see a lot of log messages from them in your terminal.
This includes output from the Mender virtual QEMU device, similar to the following:

> ...  
> mender-client_1             | Hit any key to stop autoboot:  0   
> mender-client_1             | 3485592 bytes read in 579 ms (5.7 MiB/s)  
> mender-client_1             | 14249 bytes read in 169 ms (82 KiB/s)  
> mender-client_1             | Kernel image @ 0x70000000 [ 0x000000 - 0x352f98 ]  
> mender-client_1             | ## Flattened Device Tree blob at 6fc00000  
> mender-client_1             |    Booting using the fdt blob at 0x6fc00000  
> mender-client_1             |    Loading Device Tree to 7fed9000, end 7fedf7a8 ... OK  
> mender-client_1             |   
> mender-client_1             | Starting kernel ...  
> mender-client_1             |   
> mender-client_1             | Booting Linux on physical CPU 0x0  
> mender-client_1             | Initializing cgroup subsys cpuset  
> ...  


After a few minutes, the logs will stop coming except for some periodic log messages
from the Mender authentication service similar to the following:

> mender-api-gateway_1        | 172.18.0.6 - - [21/Sep/2016:21:47:10 +0000] "POST /api/devices/0.1/authentication/auth_requests HTTP/2.0" 401 210 "-" "Go-http-client/2.0" "-"  
> mender-device-auth_1        | time="2016-09-21T21:47:15Z" level=error msg="unauthorized: dev auth: unauthorized" file="api_devauth.go" func="main.(*DevAuthHandler).SubmitAuthRequestHandler" http_code=401 line=142 request_id=6234a9c2-4036-4130-92c0-c92f371355f1   
> mender-device-auth_1        | {"Timestamp":"2016-09-21T21:47:15.668219512Z","StatusCode":401,"ResponseTime":6403109,"HttpMethod":"POST","RequestURI":"/api/0.1.0/auth_requests","RemoteUser":"","UserAgent":"Go-http-client/2.0"}  
> mender-device-auth_1        | time="2016-09-21T21:47:15Z" level=info msg="21/Sep/2016:21:47:15 +0000 \x1b[1;33m401\x1b[0m \x1b[36;1m6403μs\x1b[0m \"POST /api/0.1.0/auth_requests HTTP/1.0\" \x1b[1;30m- \"Go-http-client/2.0\"\x1b[0m" file=middleware.go func="accesslog.(*AccessLogMiddleware).MiddlewareFunc.func1" line=57 request_id=6234a9c2-4036-4130-92c0-c92f371355f1  

These messages show that the Mender client running inside the virtual QEMU device
is asking to be authorized to join the server. We will come back to this shortly.


## Store the Mender gateway certificate in your web browser

For security reasons, the Mender gateway only allows secure connections using TLS.
Your web browser will communicate directly with the gateway while using the
Mender UI and therefore the certificate the gateway is using needs to be trusted
by your web browser.

!! Currently Mender uses a default certificate for its gateway. This is insecure because anyone can gain access to the private key corresponding to the certificate (it is stored on the gateway and the same for all installations). This will shortly be remediated by auto-generating keys as Mender is installed.

To store the gateway certificate in your web browser, go to [https://localhost:9080/](https://localhost:9080/) and accept the certificate.
You should see a page similar to the following:

> Welcome to OpenResty!  
> ...  


## Open the Mender UI

The Mender UI can now be found on [http://localhost:8081/](http://localhost:8081/) - simply open it in the same web browser!

**TODO** image of UI.

**Congratulations!** You have the Mender server and a virtual Mender client successfully running!


## Stop the Mender services

When you are done testing Mender, simply press **Ctrl-C** in the terminal
you started Mender in, where the log output is shown. Stopping all the
services may take about a minute.

Mender can be started again with the same steps as above.


## Clean up the environment and get the latest version

!! You will lose all state data in your Mender environment by running the commands below, which includes devices you have authorized, software uploaded, logs, deployment reports and any other changes you have made.

If you want to remove any state in your Mender environment and start clean
with the latest version of Mender, you can stop Mender and run the following
commands in the same directory:

```
docker-compose rm --all -v
```

```
docker-compose pull
```

After doing this, you can start the latest version of Mender
by following the same steps as above.
