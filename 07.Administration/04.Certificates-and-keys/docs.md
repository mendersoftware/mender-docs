---
title: Certificates and keys
taxonomy:
    category: docs
---

In order to secure the client-server and inter-service communication,
Mender leverages public key cryptography. Several key pairs are used
and each key pair comprises of a *public key*, which in some cases has
a certificate that is shared with other services, and a *private key*,
which is kept secret by the service.
All keys are encoded in the PEM format. The public keys are shared in the
standard X.509 certificate format, `cert.crt` below,
while private keys are seen as `private.key` below.

See the [service overview](../overview) for schematics of the service
communication flow. An overview of the components that use keys and
for which purpose can be seen below.

| Component               | Purpose of keys                                                                                                                                                                                                                                                                                                                  | Shares certificate or key with                                                                                                                |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| API Gateway           | Listens to a public port for `https` requests only (plain `http` is disabled). These requests can come from Mender Clients that check for- or report status about updates through the [Device APIs](../../apis/open-source/device-apis), or from users and tools that manage deployments through the [Management APIs](../../apis/open-source/management-apis). | **Mender Clients** and users of the **Management APIs**, including web browsers accessing the **Mender UI**.                                       |
| Storage Proxy         | Listens to a public port for `https` requests only (plain `http` is disabled). The Deployment Service manages Artifacts through the Storage Proxy and Mender Clients make Artifact download requests.                                                                                                        | **Mender Clients** and **Deployment Service**.                                                                                                    |
| User Administration   | Signs and verifies JSON Web Tokens that users of the [Management APIs](../../apis/open-source/management-apis), including end users of the Mender UI, include in their requests to authenticate themselves.                                                                                                                                     | Nothing. The service gets signature verification requests from the API Gateway, so all keys are kept private to the service and not shared. |
| Device Authentication | Signs and verifies JSON Web Tokens that Mender Clients include in their requests to authenticate themselves when accessing the [Device APIs](../../apis/open-source/device-apis).                                                                                                                                                                   | Nothing. The service gets signature verification requests from the API Gateway, so all keys are kept private to the service and not shared. |
| Mender Client | Signs requests for JSON Web Tokens sent to the Device Authentication service. A Mender Client will request a new token when it connects to the Mender Server for the first time, and when a token expires. The Mender Client includes a token in all its communication to authenticate itself when accessing the [Device APIs](../../apis/open-source/device-apis).                                                                                                                                                                   | The **Device Authentication** service stores the public keys of Mender Clients. |
| Mender Artifact | Signs and verifies [Mender Artifacts](../../architecture/mender-artifacts). | The **Signing system** stores the private key used for signing Mender artifacts. After an artifact is signed using the private key it is verified by the **Mender Clients**. |


## Replacing keys and certificates

In the following we will go through how to replace all the keys and certificates
that the services use. This is very important as part of a
[Production installation](../production-installation) because each installation
must have unique keys in order to be secure, so that the private keys used are
not compromised.

In the following, we will assume you are generating new keys and corresponding
self-signed certificates. However, if you already have a CA that you use, you
can use certificates signed by that CA instead of self-signed ones. The rest
of the steps should be the exact same in both cases.

!! If your CA uses intermediate certificates, make sure they are concatenated into your cert.crt file

### Generating new keys and certificates

You need key pairs for all the services, and the best practice is to use
different keys for all these four services, as it limits the attack surface
if the private key of one service gets compromised. The API Gateway and
Storage Proxy also requires certificates in addition to key pairs.
In order to make all this key and certificate generation easier, we have
created a `keygen` script that leverages the `openssl` utility to do
the heavy lifting. It is available in
[Mender's Integration GitHub repository](https://github.com/mendersoftware/integration?target=_blank).

Open a terminal and go to the directory where you cloned the integration repository
as part of the [tutorial to create a test environment](../../getting-started/on-premise-installation/create-a-test-environment).

In order to generate the self-signed certificates, the script needs to know
what the CN (Common Name) of the two certificates should be, i.e. which URL
will the Mender Clients and users access them on. In our example, we will use
`docker.mender.io` for the API Gateway and `s3.docker.mender.io` for
the Storage Proxy.

! Make sure the CNs you use will be the same as the URLs that the Mender clients and web browsers will use to access the API Gateway and Storage Proxy. If there is a mismatch, the clients will reject the connections.

With this knowledge, all the required keys and certificates can be generated
by running:

```bash
CERT_API_CN=docker.mender.io CERT_STORAGE_CN=s3.docker.mender.io ./keygen
```

!!! This generates keys with 128-bit security level (256-bit Elliptic Curve and 3072-bit RSA keys) and certificates valid for approximately 10 years. You can customize the parameters by adapting the script to your needs.

!!! Make sure your device has the correct date/time set. If the date/time is incorrect, the certificate will not be validated. Consult the section on [Correct clock](../../devices/general-system-requirements#correct-clock) for details

The keys and certificates are placed in a directory `keys-generated`
where you ran the script from, and each service has a subdirectory within it
as follows:

```bash
keys-generated/
├── certs
│   ├── api-gateway
│   │   ├── cert.crt
│   │   └── private.key
│   ├── server.crt
│   └── storage-proxy
│       ├── cert.crt
│       └── private.key
└── keys
    ├── deviceauth
    │   └── private.key
    └── useradm
        └── private.key
```

!!! The file `certs/server.crt` is just a concatenation of all the certificates that the Mender client uses.


### Installing new keys and certificates

Now that we have the required keys and certificates, we
need to make the various services use them. This is done by
injecting them into the service containers with volume mounts in
a [Docker compose extends](https://docs.docker.com/compose/extends/?target=_blank).

We will go through the individual services below, but make
sure to **stop the Mender server** before proceeding.

!! When you replace the certificates and keys, any Mender Clients (and potentially web browsers) currently connecting to the server will reject the new certificates. Rotating server keys in live installations is not yet covered in this document.

We use the `keys-generated` directory the script created in the `integration`
directory as paths to the keys, which is shown above. If you want, you can move
the keys to a different location and adjust the steps below accordingly.


#### API Gateway

The API Gateway will use the new keys by using a docker compose file with the following entries:

```yaml
    mender-api-gateway:
        volumes:
            - ./keys-generated/certs/api-gateway/cert.crt:/var/www/mendersoftware/cert/cert.crt
            - ./keys-generated/certs/api-gateway/private.key:/var/www/mendersoftware/cert/private.key

```



#### Storage Proxy

The default setup described in compose file uses [Minio](https://www.minio.io/?target=_blank)
object storage along with a Storage Proxy service. The proxy service provides
HTTPS and traffic limiting services.

The Storage Proxy will use the new keys by using a docker compose file with the following entries:

```yaml
    storage-proxy:
        volumes:
            - ./keys-generated/certs/storage-proxy/cert.crt:/var/www/storage-proxy/cert/cert.crt
            - ./keys-generated/certs/storage-proxy/private.key:/var/www/storage-proxy/cert/private.key
```

The Deployment Service communicates with the Minio object storage via the Storage Proxy.
For this reason, the Deployment Service service must be provisioned with a
certificate of the Storage Proxy so the authenticity can be validated. This can be
implemented by adding the following entries to a compose file:

```yaml
    mender-deployments:
        volumes:
            - ./keys-generated/certs/storage-proxy/cert.crt:/etc/ssl/certs/storage-proxy.pem
        environment:
            STORAGE_BACKEND_CERT: /etc/ssl/certs/storage-proxy.pem
```

!!! `STORAGE_BACKEND_CERT` defines the path to the certificate of the Storage Proxy within the filesystem of the Deployment Service. The Deployment Service will automatically load this certificate into its trust store.


#### User Administration

The User Administration service signs and verifies JSON Web Tokens from
users of the Management APIs. As the verification
happens locally in the service only, the service does not need a certificate.

The User Administration key can be mounted with the following snippet:

```yaml
    mender-useradm:
        volumes:
            - ./keys-generated/keys/useradm/private.key:/etc/useradm/rsa/private.pem
```

The Management APIs are documented for [Open Source](../../apis/open-source/management-apis) and [Enterprise](../../apis/enterprise/management-apis).

#### Device Authentication

The Device Authentication service signs and verifies JSON Web Tokens that
Mender Clients include in their requests to authenticate themselves when accessing
the Device APIs. As the verification
happens locally in the service only, the service does not need a certificate.

The Device Authentication key can be mounted with the following snippet:

```yaml
    mender-device-auth:
        volumes:
            - ./keys-generated/keys/deviceauth/private.key:/etc/deviceauth/rsa/private.pem
```

The Device APIs are documented for [Open Source](../../apis/open-source/device-apis) and [Enterprise](../../apis/enterprise/device-apis).


#### Mender Client

The client does not need any special configuration regarding certificates as long as the server certificate
is signed by a Certificate Authority. The client will verify trust using its system root certificates, which
are typically provided by the `ca-certificates` package.

If the certificate is self-signed, then clients that are to connect to the server need to have the file with
the concatenated certificates (`keys-generated/certs/server.crt`) stored locally in order to verify
the server's authenticity. Please see [the client section on building for production](../../artifacts/yocto-project/building-for-production)
for a description on how to provision new device disk images with the new certificates. In this case, it
is advisable to ensure there is a overlap between the issuance of new certificates and expiration of old
ones so all clients are able to receive an update containing the new cert before the old one expires. You
can have two valid certificates for the Mender server concatenated in the server.crt file. When all clients
have received the updated server.crt, the server configuration can be updated to use the new certificate.
In a subsequent update, the old certificate can be removed from the client's server.crt file.

!!! The key of the Mender Client itself is automatically generated and stored at `/var/lib/mender/mender-agent.pem` the first time the Mender Client runs. We do not yet cover rotation of Mender Client keys in live installations in this document.
