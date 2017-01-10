---
title: Certificates and keys
taxonomy:
    category: docs
---

In order to secure the client-server and inter-service communication,
Mender leverages public key cryptography. Several keypairs are used
and each keypair comprises of a *public key*, which is shared with
other services, and a *private key*, which is kept secret by the service.

All keys are encoded in the PEM format. The public keys are in the
standard X.509 certificate format, `cert.pem` below,
while private keys are seen as `key.pem` below.

As you can see in the [service overview](../Overview), the *API gateway*
and the *Storage proxy* listen to public ports, so they need their own
keys and certificates. In addition, the *User administration* and
*Device authentication* services sign tokens, so they also need keypairs.


## Prerequisites

You need certificates and corresponding private keys for all the services.
The best practice is to use different keys for all these
four services, as it limits the attack surface if the private key of one
service gets compromised.

You can either generate self-signed certificates or leverage an existing
CA you already trust to sign your new public keys. In either case you
need to place the certificates and keys in the appropriate place, as
described for each service below.

In case you are generating self-signed certificates, this can be done
with the `openssl` utility as follows:

```
openssl req -x509 -sha256 -nodes -days 3650 -newkey rsa:3096 -keyout private-key.pem -out certificate.pem -subj '/CN=yourdomain'
```

! This will generate a certificate which is valid for approximately 10 years; adjust the `days` parameter to change this.


## API gateway

API Gateway certificate needs to be mounted into the gateway's container. This
can be achieved using a compose file with the following entry:

```
    mender-api-gateway:
        volumes:
            - ./ssl/mender-api-gateway/cert.pem:/var/www/mendersoftware/cert/cert.pem
            - ./ssl/mender-api-gateway/key.pem:/var/www/mendersoftware/cert/key.pem

```

Where certificate and key paths need to be replaced with paths to your
certificate and key files.

! Remember to include the API gateway certificate into the Mender client build, otherwise the client will not trust the gateway and reject connections to it.

!! Make sure that the certificate matches the domain name used by other services accessing API Gateway.


## Artifact storage

The default setup described in compose file uses [Minio](https://www.minio.io/)
object storage along with a Storage Proxy service. The proxy service provides
HTTPS and traffic limiting services. This section describes configuration of
storage proxy certificates for use with HTTPS.

Storage proxy certificate needs to be mounted into the container. This can be
implemented using a `docker-compose` file with the following entry:

```
    storage-proxy:
        volumes:
            - ./ssl/storage-proxy/s3.docker.mender.io.crt:/var/www/storage-proxy/cert/cert.crt
            - ./ssl/storage-proxy/s3.docker.mender.io.key:/var/www/storage-proxy/cert/key.pem
```

Replace path to demo certificate and key with paths to your certificate and key.

Deployments service communicates with Minio object storage via storage proxy.
For this reason, `mender-deployments` service must be provisioned with a
certificate of a storage proxy for host verification purpose. This can be
implemented by adding the following entry to compose file:

```
    mender-deployments:
        volumes:
            - ./ssl/storage-proxy/s3.docker.mender.io.crt:/etc/ssl/certs/s3.docker.mender.io.crt
        environment:
            - STORAGE_BACKEND_CERT=/etc/ssl/certs/s3.docker.mender.io.crt
```

`STORAGE_BACKEND_CERT` defines a path to the certificate of storage proxy within
the container's filesystem. Deployments service will automatically load the
certificate into its trust store.

! Remember to include the Storage proxy certificate into the Mender client build, otherwise the client will not trust the storage proxy and reject connections to it.

!! Make sure that the certificate matches the domain name used by other services accessing storage proxy.


## Token signing keys

Mender backend uses JWT tokens for device and user authentication. The tokens
are cryptographically signed and their authenticity is verified when making
requests to the backend. Tokens are handed out
by [Device Authentication](https://github.com/mendersoftware/deviceauth)
and [User Administration](https://github.com/mendersoftware/useradm) services.

Before starting mender in production, one needs to provide RSA private keys in
PEM format for both services. This can be accomplished by generating key using
openssl:

```
openssl genpkey -algorithm RSA -out key.pem -pkeyopt rsa_keygen_bits:2048
```

and mounting the keys into respective containers by adding the following entry
to compose file (replacing local key paths with paths of your own):

```
    mender-useradm:
        volumes:
            - ./keys/useradm-private.pem:/etc/useradm/rsa/private.pem

    mender-device-auth:
        volumes:
            - ./keys/deviceauth-private.pem:/etc/deviceauth/rsa/private.pem
```

It is recommended to use separate keys for `mender-useradm` and
`mender-device-auth` services.
