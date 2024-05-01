---
title: Evaluation with Docker Compose
taxonomy:
    category: docs
    label: tutorial
---

!!! If you are interested in evaluating Mender features as an end to end solution, please visit
!!! [Get Started](../../01.Get-started/chapter.md)

! If you are interested in setting up a Mender Server for production, visit
! [Production installation with Kubernetes](../04.Production-installation-with-kubernetes/docs.md).

This tutorial covers how to setup a demonstration environment of the Mender
server. This is not intended for production use, the demonstration environment
is insecure and is not optimized to run effectively.

This can be useful if you want to familiarize your self with the Mender Server
before you move on to
[Production installation](../04.Production-installation-with-kubernetes/docs.md).

## Requirements

The demo environment requires the following components to be available
on your system:

* [Docker Engine](https://docs.docker.com/engine/install?target=_blank)
* [Docker Compose](https://docs.docker.com/compose/install?target=_blank)
* Install the following utilities, example for Ubuntu:

    ```bash
    sudo apt install gawk curl bsdmainutils jq git
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
git clone -b 3.6.4 https://github.com/mendersoftware/integration.git integration-3.6.4
```

<!--AUTOVERSION: "use `-b %`"/ignore-->
!!! If you want to use a pre-release version of the backend, use `-b master` in
!!! the command above.

Change directory to the cloned repository:
<!--AUTOVERSION: "integration-%"/integration -->
```bash
 cd integration-3.6.4
```

Start the demo server:

```bash
./demo up
```

After a short while, depending on your network connection speed, you should see
similar output to the following:

>```bash
>Starting the Mender demo environment...
>Creating network "integrationmaster_mender" with the default driver
>Creating integrationmaster_mender-reporting-indexer_1 ...
>Creating integrationmaster_mender-gui_1               ... done
>Creating integrationmaster_minio_1                    ... done
>Creating integrationmaster_mender-mongo_1             ... done
>Creating integrationmaster_mender-opensearch_1 ... done
>Creating integrationmaster_mender-reporting-indexer_1      ... done
>Creating integrationmaster_mender-reporting_1              ... done
>Creating integrationmaster_mender-deviceconfig_1           ... done
>Creating integrationmaster_mender-iot-manager_1            ... done
>Creating integrationmaster_mender-inventory_1              ... done
>Creating integrationmaster_mender-useradm_1                ... done
>Creating integrationmaster_mender-deviceconnect_1          ... done
>Creating integrationmaster_mender-workflows-server_1       ... done
>Creating integrationmaster_mender-create-artifact-worker_1 ... done
>Creating integrationmaster_mender-workflows-worker_1       ... done
>Creating integrationmaster_mender-device-auth_1            ... done
>Creating integrationmaster_mender-api-gateway_1            ... done
>Creating integrationmaster_mender-deployments_1            ... done
>Waiting for services to become ready...
>Creating a new user...
>****************************************
>
>Username: mender-demo@example.com
>Login password: xxxxxxxxxxxx
>
>****************************************
>```

!! Please note that Docker Hub enforced limits on pulls originating
!! from anonymous users to 100 per 6 hours (see: [Docker pricing](https://www.docker.com/pricing)).
!! This means that, for reasons completely independent from Mender,
!! the above step may fail and you may have to retry after some time.

The script created a demo user, and you can login to the Mender UI by visiting
[https://localhost](https://localhost?target=_blank).

! You might get a warning from your browser that the site is not secure.
! This is because we use self-signed certificates in the demo environment and
! can be safely ignored.

### Stopping the demo

To stop the demo use Ctrl+C.
This will only stop the containers, but will not remove them.
To remove containers use commands from the section below.

### Clean up the environment

!! You will lose all state data in your Mender demo environment by running the
!! commands below, which includes devices you have authorized, software
!! uploaded, logs, deployment reports and any other changes you have made.

<!--AUTOVERSION: "integration-%"/integration -->
If you want to remove all state in your Mender demo environment and start clean,
run the following commands in the `integration-3.6.4` directory:

```bash
./demo stop
```

```bash
./demo rm -v
```

```bash
./demo up
```
