---
title: Demo installation
taxonomy:
    category: docs
    label: guide
---

## Mender demo

If you want to try Mender you can either do it online using demo account, or 
run it in a simple docker-based environment. This section describes the latter.
The demo setup is not very much different from the production one. In fact, they
both run the same internals, and only differ slightly in the configuration.

## Requirements

 The demo requires the following components to be available on your system: 
* Docker
* Docker Compose
* `curl`
* `hexdump`
* `jq`
* `git`
* `awk`

 In addition, you should add the following lines to `/etc/hosts`:

```bash
127.0.0.1 s3.docker.mender.io
127.0.0.1 docker.mender.io
```

## Manage the Mender demo instance

### Starting the demo

To start the demo, issue the following commands:
<!--AUTOVERSION: "-b %"/integration "integration-%"/integration -->
```bash
 git clone -b master https://github.com/mendersoftware/integration.git integration-master
```
<!--AUTOVERSION: "integration-%"/integration -->
```
 cd integration-master
 ./demo up
```
After a short while, depending on your network connection speed,
you should see the output similar to this:
```
Creating integration_mender-gui_1   ... done
Creating integration_minio_1        ... done
Creating integration_mender-mongo_1 ... done
Creating integration_mender-workflows-server_1       ... done
Creating integration_mender-inventory_1              ... done
Creating integration_mender-workflows-worker_1       ... done
Creating integration_mender-create-artifact-worker_1 ... done
Creating integration_mender-useradm_1                ... done
Creating integration_mender-device-auth_1            ... done
Creating integration_storage-proxy_1                 ... done
Creating integration_mender-deployments_1            ... done
Creating integration_mender-api-gateway_1            ... done
Creating a new user...
****************************************

Username: mender-demo@example.com
Login password: xxxxxxxxxxxx

****************************************
```
Now you have a local instance of the Mender server running. The
script also created a demo user, and you can now login to the Mender UI by
pointing your web browser to `https://localhost` (please note that the
certificate will probably not be trusted, since it is self-signed and generated
for the purpose of the demonstration).

### Stopping the demo

In order to stop the demo you can use:
```bash
./demo down
```
It will stop the containers, but will not remove the images; you have to do it by
hand.

### Next steps

You can now follow the help tooltips in the UI to guide you through each step
of deploying to a device - accepting the device, viewing information about it,
uploading an Artifact file, and finally deploying your very first update.

Now that you have a feeling of how Mender works, you can
either [signup](https://mender.io/signup) for an account
on [hosted.mender.io](https://hosted.mender.io/ui/#/login), or continue to the next
section which describes the production on-premise installation.
