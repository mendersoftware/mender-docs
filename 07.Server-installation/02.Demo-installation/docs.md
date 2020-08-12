---
title: Demo installation
taxonomy:
    category: docs
    label: tutorial
---

!!! If you are interested in setting up a Mender server for production, visit
!!! [Production installation](../03.Production-installation/docs.md)

!!! If you are interested in evaluating Mender features, visit
!!! [Get Started](../../01.Get-started/chapter.md)

This tutorial covers how to setup a demonstration environment of the Mender
server. This is not intended for production use, the demonstration environment
is insecure and is not optimized to run effectively.

This can be useful if you want to familiarize your self with the Mender server
before you move on to
[Production installation](../03.Production-installation/docs.md).

## Requirements

The demo environment requires the following components to be available
on your system:

* [Docker Engine](https://docs.docker.com/engine/install?target=_blank)
* [Docker Compose](https://docs.docker.com/compose/install?target=_blank)
* Install the following utilities, example for Ubuntu:

    ```bash
    sudo apt install awk curl hexdump jq git
    ```

In addition, add the following lines to `/etc/hosts`:

```bash
127.0.0.1 s3.docker.mender.io
127.0.0.1 docker.mender.io
```

!!! This is needed because demo certificates for the HTTPS communication are
!!! created for `s3.docker.mender.io` and `docker.mender.io`

## Manage the Mender demo instance

### Starting the demo

Clone the [integration](https://github.com/mendersoftware/integration?target=_blank)
repository which contains everything that is need to start the demo server:
<!--AUTOVERSION: "-b %"/integration "integration-%"/integration -->
```bash
git clone -b master https://github.com/mendersoftware/integration.git integration-master
```

Change directory to the cloned repository:
<!--AUTOVERSION: "integration-%"/integration -->
```bash
 cd integration-master
```

Start the demo server:

```bash
./demo up
```

After a short while, depending on your network connection speed, you should see
similar output to the following:

>```bash
>Creating integration_mender-gui_1   ... done
>Creating integration_minio_1        ... done
>Creating integration_mender-mongo_1 ... done
>Creating integration_mender-workflows-server_1       ... done
>Creating integration_mender-inventory_1              ... done
>Creating integration_mender-workflows-worker_1       ... done
>Creating integration_mender-create-artifact-worker_1 ... done
>Creating integration_mender-useradm_1                ... done
>Creating integration_mender-device-auth_1            ... done
>Creating integration_storage-proxy_1                 ... done
>Creating integration_mender-deployments_1            ... done
>Creating integration_mender-api-gateway_1            ... done
>Creating a new user...
>****************************************
>
>Username: mender-demo@example.com
>Login password: xxxxxxxxxxxx
>
>****************************************
>```

The script created a demo user, and you can login to the Mender UI by visiting
[https://localhost](https://localhost?target=_blank).

! You might get a warning from your browser that that the site is not secure.
! This is because we use self-signed certificates in the demo environment and
! can be safely ignored.

### Stopping the demo

To stop the demo server run:

```bash
./demo down
```

This will stop and remove the containers with all user data, but will not remove
the images.

### Clean up the environment

!! You will lose all state data in your Mender demo environment by running the
!! commands below, which includes devices you have authorized, software
!! uploaded, logs, deployment reports and any other changes you have made.

<!--AUTOVERSION: "integration-%"/integration -->
If you want to remove all state in your Mender demo environment and start clean,
run the following commands in the `integration-master` directory:

```bash
./demo stop
```

```bash
./demo rm -v
```

```bash
./demo up
```
