---
title: Certificates and keys
taxonomy:
    category: docs
---

In order to secure the client-server and inter-service communication,
Mender leverages public key cryptography. Several keypairs are used
and each keypair comprises of a *public key*, which in some cases has
a certificate that is shared with other services, and a *private key*,
which is kept secret by the service.
All keys are encoded in the PEM format. The public keys are shared in the
standard X.509 certificate format, `cert.pem` below,
while private keys are seen as `key.pem` below.

See the [service overview](../Overview) for schematics of the service
communication flow. An overview of the services that use keys and
for which purpose can be seen below.

| Service               | Purpose of keys                                                                                                                                                                                                                                                                                                                  | Shares certificate with                                                                                                                |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| API Gateway           | Listens to a public port for `https` requests only (plain `http` is disabled). These requests can come from devices that check for- or report status about updates through the [Device APIs](../../APIs/Device-APIs), or from users and tools that manage deployments through the [Management APIs](../../APIs/Management-APIs). | **Devices** and users of the **Management APIs**, including web browsers accessing the **Mender UI**.                                       |
| Storage Proxy         | Listens to a public port for `https` requests only (plain `http` is disabled). The Deployment Service manages Artifacts through the Storage Proxy and Devices make Artifact download requests.                                                                                                        | **Devices** and **Deployment Service**.                                                                                                    |
| Device Authentication | Signs and verifies JSON Web Tokens that devices include in their requests to authenticate themselves when accessing the [Device APIs](../../APIs/Device-APIs).                                                                                                                                                                   | Nothing. The service gets signature verification requests from the API Gateway, so all keys are kept private to the service and not shared. |
| User Administration   | Signs and verifies JSON Web Tokens that users of the [Management APIs](../../APIs/Management-APIs), including end users of the Mender UI, include in their requests to authenticate themselves.                                                                                                                                     | Nothing. The service gets signature verification requests from the API Gateway, so all keys are kept private to the service and not shared. |



## Replacing keys and certificates

In the following we will go through how to replace all the keys and certificates
that the services use. This is very important as part of a
[Production installation](../Production-installation) because each installation
must have unique keys in order to be secure, so that the private keys used are
not compromised.

In the following, we will assume you are generating new keys and corresponding
self-signed certificates. However, if you already have a CA that you use, you
can use certificates signed by that CA instead of self-signed ones. The rest
of the steps should be the exact same in both cases.


### Generating new keys and certificates

You need keypairs for all the services, and the best practice is to use
different keys for all these four services, as it limits the attack surface
if the private key of one service gets compromised. The API Gateway and
Storage Proxy also requires certificates in addition to keypairs.
In order to make all this key and certificate generation easier, we have
created a `keygen` script that leverages the `openssl` utility to do
the heavy lifting. It is available in
[Mender's Integration GitHub repository](https://github.com/mendersoftware/integration).

Open a terminal and go to the directory where you cloned the integration repository
as part of the [tutorial to create a test environment](../../Getting-started/Create-a-test-environment).

In order to generate the self-signed certificates, the script needs to know
what the CN (Common Name) of the two certificates should be, i.e. which URL
will the devices and users access them on. In our example, we will use
`docker.mender.io` for the API Gateway and `s3.docker.mender.io` for
the Storage Proxy.

With this knowledge, all the required keys and certificates can be generated
by running:

```
CERT_API_CN=docker.mender.io CERT_STORAGE_CN=s3.docker.mender.io ./keygen
```

! This generates keys with 128-bit security level (3072 bit RSA keys) and certificates valid for approximately 10 years. You can customize the parameters by adapting the script to your needs.

The keys and certificates are placed in a directory `keys-generated`
where you ran the script from, and each service has a sub-directory within it
as follows:

```
keys-generated/
├── api-gateway
│   ├── certificate.pem
│   └── private.pem
├── deviceauth
│   └── private.pem
├── storage-proxy
│   ├── certificate.pem
│   └── private.pem
└── useradm
    └── private.pem
```



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
Storage Proxy certificates for use with HTTPS.

Storage Proxy certificate needs to be mounted into the container. This can be
implemented using a `docker-compose` file with the following entry:

```
    storage-proxy:
        volumes:
            - ./ssl/storage-proxy/s3.docker.mender.io.crt:/var/www/storage-proxy/cert/cert.crt
            - ./ssl/storage-proxy/s3.docker.mender.io.key:/var/www/storage-proxy/cert/key.pem
```

Replace path to demo certificate and key with paths to your certificate and key.

Deployment Service communicates with Minio object storage via Storage Proxy.
For this reason, `mender-deployments` service must be provisioned with a
certificate of a Storage Proxy for host verification purpose. This can be
implemented by adding the following entry to compose file:

```
    mender-deployments:
        volumes:
            - ./ssl/storage-proxy/s3.docker.mender.io.crt:/etc/ssl/certs/s3.docker.mender.io.crt
        environment:
            - STORAGE_BACKEND_CERT=/etc/ssl/certs/s3.docker.mender.io.crt
```

`STORAGE_BACKEND_CERT` defines a path to the certificate of Storage Proxy within
the container's filesystem. Deployment service will automatically load the
certificate into its trust store.

! Remember to include the Storage Proxy certificate into the Mender client build, otherwise the client will not trust the StorageProxy and reject connections to it.

!! Make sure that the certificate matches the domain name used by other services accessing Storage Proxy.


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
