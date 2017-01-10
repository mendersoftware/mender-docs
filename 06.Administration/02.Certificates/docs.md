---
title: Certificates
taxonomy:
    category: docs
---

## API Gateway

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

!! Make sure that the certificate matches the domain name used by other services accessing storage proxy.

## Generating self signed certificates

A self-signed certificate can be generated using the following snippet:

```
PASS=foo openssl req -x509 -newkey rsa:4096 -keyout key.encrypted.pem \
    -out cert.pem -days 3650 \
    -passin env:PASS -passout env:PASS \
    -subj '/CN=yourdomain'

PASS=foo openssl rsa -in key.encrypted.pem -out key.pem -passin env:PASS
```

replacing `yourdomain` with your domain name. The certificate is written to
`cert.pem` and is valid for 3650 days. Unencrypted private key is written to
`key.pem`.
