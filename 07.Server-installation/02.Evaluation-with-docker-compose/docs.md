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
<!--AUTOVERSION: "target=_blank) >= v%"/ignore -->
* [Docker Engine](https://docs.docker.com/engine/install?target=_blank) >= v1.20
* [Docker Compose](https://docs.docker.com/compose/install?target=_blank) >= v2.23.1

In addition, add the following lines to `/etc/hosts`:

```bash
127.0.0.1 s3.docker.mender.io
127.0.0.1 docker.mender.io
```

!!! This is needed because demo certificates for the HTTPS communication are
!!! created for `s3.docker.mender.io` and `docker.mender.io`

## Manage the Mender demo instance

### Starting the demo

Clone the [mender-server](https://github.com/mendersoftware/mender-server?target=_blank)
repository which contains everything that is need to start the demo server:
```bash
git clone -b main https://github.com/mendersoftware/mender-server.git mender-server
```

Change directory to the cloned repository:
```bash
 cd mender-server
```

Start the demo server:

```bash
docker compose up -d
```

!! Please note that Docker Hub enforced limits on pulls originating
!! from anonymous users to 100 per 6 hours (see: [Docker pricing](https://www.docker.com/pricing)).
!! This means that, for reasons completely independent from Mender,
!! the above step may fail and you may have to retry after some time.

Once the server is running, you can go ahead and create the admin user:

```bash
MENDER_USERNAME=admin@docker.mender.io
MENDER_PASSWORD=PleaseReplaceWithASecurePassword
docker compose run --name create-user useradm create-user --username "$MENDER_USERNAME" --password "$MENDER_PASSWORD"
```

Open the browser and visit [https://localhost](https://localhost) to log in using the credentials configured in the above snippet.

! You might get a warning from your browser that the site is not secure.
! This is because we use self-signed certificates in the demo environment and
! can be safely ignored.

### Stopping the demo

To stop the demo server, from the `mender-server` directory, run:
```bash
docker compose stop
```
This will only stop the containers, but will not remove them.
To remove containers use commands from the section below.

### Clean up the environment

!! You will lose all state data in your Mender demo environment by running the
!! commands below, which includes devices you have authorized, software
!! uploaded, logs, deployment reports and any other changes you have made.

If you want to remove all state in your Mender demo environment and start clean,
run the following commands in the `mender-server` directory:

```bash
docker compose down -v --remove-orphans
```
