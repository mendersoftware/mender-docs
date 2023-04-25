---
title: Evaluation with Docker Compose
taxonomy:
    category: docs
    label: tutorial
---

This tutorial covers how to setup a demonstration environment of the Mender
server. This is not intended for production use, the demonstration environment
is insecure and is not optimized to run effectively.

This can be useful if you want to familiarize your self with the Mender Server
before you move on to
[Production installation](../04.Production-installation-with-kubernetes/docs.md).

## Overview

The integration environment brings together the following services:

- [Mender Device Authentication Service](https://github.com/mendersoftware/deviceauth?target=_blank)
- [Mender Device Configuration Service](https://github.com/mendersoftware/deviceconfig?target=_blank)
- [Mender Device Connect Service](https://github.com/mendersoftware/deviceconnect?target=_blank)
- [Mender Device Monitor Service](https://github.com/mendersoftware/devicemonitor?target=_blank)
- [Mender Deployments Service](https://github.com/mendersoftware/deployments?target=_blank)
- [Mender Device Inventory Service](https://github.com/mendersoftware/inventory?target=_blank)
- [Mender User Administration Service](https://github.com/mendersoftware/useradm?target=_blank)
- [Mender Workflows Service](https://github.com/mendersoftware/workflows?target=_blank)
- [Mender Reporting Service](https://github.com/mendersoftware/reporting?target=_blank)
- [Mender Create Artifact Worker](https://github.com/mendersoftware/create-artifact-worker?target=_blank)
- API Gateway based on [Traefik](https://doc.traefik.io/traefik/?target=_blank)
- [Minio](https://www.minio.io?target=_blank) object storage
- [NATS.io](https://nats.io?target=_blank) messaging system
- [OpenSearch](https://www.opensearch.org?target=_blank) storage and search engine

Services are delivered in form of Docker images, available from
official [Mender Docker repository](https://hub.docker.com/r/mendersoftware/?target=_blank).
When required, each service can be built directly from its source code. Consult
respective repositories for build instructions.

!!!!! The architecture below show the case for the Open Source Mender Server.
!!!!! For evaluation of the Mender Enterprise Server please [contact us](https://mender.io/contact-us) to gain access to the enterprise containers.

While it is possible to `docker pull` individual images and start containers
manually,
the [integration repository](https://github.com/mendersoftware/integration?target=_blank)
provides a convenient setup based on Docker Compose tool. The
`docker-compose.yml` file describes the following setup:

```
        |
        |                                            +-------------------------+
        |                                            |                         |
        |                                       +--->|  Device Authentication  |<---+
        |                                       |    |  (mender-device-auth)   |    |
        |                                       |    +-------------------------+    |
        |        +-----------------------+      |    |                         |    |
   port |        |                       |      +--->|  Inventory              |<---+     +----------------------------------+
    443 | <----> |  API Gateway          |      |    |  (mender-inventory)     |    +---> |  Workflows Engine                |
        |        |  (Traefik)            |<-----+    +-------------------------+    |     |  (mender-workflows-server)       |
        |        +-----------------------+      |    |                         |    |     |  (mender-workflows-worker)       |
        |                                       +--->|  User Administration    |    |     |  (mender-create-artifact-worker) |
        |                                       |    |  (mender-useradm)       |<---+     +----------------------------------+
        |                                       |    +-------------------------+    |
        |                                       +--->|                         |    |
        |                                       |    |  Device Config          |<---+
        |                                       |    |  (mender-deviceconfig)  |    |
        |                                       |    +-------------------------+    |
        |                                       +--->|                         |    |
        |                                       |    |  Deployments            |<---+
        |                                       |    |  (mender-deployments)   |    |
        |                                       |    +-------------------------+    |
        |                                       +--->|                         |    |
        |                                       |    |  Reporting              |<---+
        |                                       |    |  (mender-reporting)     |    |
        |                                       |    +-------------------------+    |
        |                                       +--->|                         |    |
        |                                       |    |  IoT Manager            |<---+
        |                                       |    |  (mender-iot-manager)   |    |
        |                                       |    +-------------------------+    |
        |                                       +--->|                         |    |
        |                                       |    |  Device Monitor         |<---+
        |                                       |    |  (mender-devicemonitor) |    |
        |                                       |    +-------------------------+    |
        |                                       +--->|                         |<---+
        |                                       |    |  Device Connect         |          +--------+
        |                                       |    |  (mender-deviceconnect) |<-------->|        |
        |                                       |    +-------------------------+          |  Nats  |
        |                                       +--->|                         |          |        |
        |                                            |  Minio                  |          +--------+
        |                                            |                         |
        |                                            +-------------------------+
        |
```


### Certificates and keys

In order to secure the client-server and inter-service communication,
Mender leverages public key cryptography. Several key pairs are used
and each key pair comprises of a *public key*, which in some cases has
a certificate that is shared with other services, and a *private key*,
which is kept secret by the service.
All keys are encoded in the PEM format. The public keys are shared in the
standard X.509 certificate format, `cert.crt` below,
while private keys are seen as `private.key` below.


| Component | Purpose of keys | Shares certificate or key with |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| API Gateway | Listens to a public port for `https` requests only (plain `http` is disabled). These requests can come from Mender Clients that check for- or report status about updates through the [Device APIs](../../200.Server-side-API/?target=_blank#device-apis), or from users and tools that manage deployments through the [Management APIs](../../200.Server-side-API/?target=_blank#management-apis). | **Mender Clients** and users of the **Management APIs**, including web browsers accessing the **Mender UI**. |
| User Administration | Signs and verifies JSON Web Tokens that users of the [Management APIs](../../200.Server-side-API/?target=_blank#management-apis), including end users of the Mender UI, include in their requests to authenticate themselves. | Nothing. The service gets signature verification requests from the API Gateway, so all keys are kept private to the service and not shared. |
| Device Authentication | Signs and verifies JSON Web Tokens that Mender Clients include in their requests to authenticate themselves when accessing the [Device APIs](../../200.Server-side-API/?target=_blank#device-apis). | Nothing. The service gets signature verification requests from the API Gateway, so all keys are kept private to the service and not shared. |
| Mender Client | Signs requests for JSON Web Tokens sent to the Device Authentication service. A Mender Client will request a new token when it connects to the Mender Server for the first time, and when a token expires. The Mender Client includes a token in all its communication to authenticate itself when accessing the [Device APIs](../../200.Server-side-API/?target=_blank#device-apis). | The **Device Authentication** service stores the public keys of Mender Clients. |
| Mender Artifact | Signs and verifies [Mender Artifacts](../../02.Overview/03.Artifact/docs.md). | The **Signing system** stores the private key used for signing Mender artifacts. After an artifact is signed using the private key it is verified by the **Mender Clients**. |

### Mender Client

The client does not need any special configuration regarding certificates as long as the server certificate
is signed by a Certificate Authority. The client will verify trust using its system root certificates, which
are typically provided by the `ca-certificates` package.

If the certificate is self-signed, the clients need to store the server certificate locally
(`keys-generated/cert/cert.crt`) in order to verify the server's authenticity.
Please see [the client section on building for production](../../05.Operating-System-updates-Yocto-Project/06.Build-for-production/docs.md)
for a description on how to provision new device disk images with the new certificates. In this case, it
is advisable to ensure there is a overlap between the issuance of new certificates and expiration of old
ones so all clients are able to receive an update containing the new cert before the old one expires. You
can have two valid certificates for the Mender Server concatenated in the server.crt file. When all clients
have received the updated server.crt, the server configuration can be updated to use the new certificate.
In a subsequent update, the old certificate can be removed from the client's server.crt file.

!!! The key of the Mender Client itself is automatically generated and stored at `/var/lib/mender/mender-agent.pem` the first time the Mender Client runs. We do not yet cover rotation of Mender Client keys in live installations in this document.


### Mender Server

You can either generate new certificates by following the tutorial for
[generating
certificates](../03.Installation-with-docker-compose/docs.md#certificates-and-keys),
or obtain the certificates in a different way - for example from your existing
Certificate Authority. In either case the certificates on the client and server
must be the same.

### Mutual TLS

Mender Enterprise supports setting up a reverse proxy at the edge of the network, which can authenticate devices using TLS client certificates. Each client is equipped with a certificate signed by a CA certificate (Certificate Authority), and the edge proxy authenticates devices by verifying this signature. Authenticated devices are automatically authorized in the Mender backend, and do not need manual approval.

Please refer to the [Mutual TLS section](../../08.Server-integration/03.Mutual-TLS-authentication/docs.md)
to find further details on the configuration of this feature.



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
git clone -b master https://github.com/mendersoftware/integration.git integration-master
```

<!--AUTOVERSION: "use `-b %`"/ignore-->
!!! If you want to use a pre-release version of the backend, use `-b master` in
!!! the command above.

Change directory to the cloned repository:
<!--AUTOVERSION: "integration-%"/integration -->
```bash
 cd integration-master
```

Start the demo server:

!!!!! If you are evaluating the Enterprise version and have gotten access to the registry, use the command `./demo up --enterprise-testing` which will pull the enterprise containers.


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
