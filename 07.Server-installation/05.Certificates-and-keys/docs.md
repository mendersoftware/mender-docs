---
title: Certificates and keys
taxonomy:
    category: docs
    label: tutorial
---

In order to secure the client-server and inter-service communication,
Mender leverages public key cryptography. Several key pairs are used
and each key pair comprises of a *public key*, which in some cases has
a certificate that is shared with other services, and a *private key*,
which is kept secret by the service.
All keys are encoded in the PEM format. The public keys are shared in the
standard X.509 certificate format, `cert.crt` below,
while private keys are seen as `private.key` below.

See the [service overview](../01.Overview/docs.md) for schematics of the service
communication flow. An overview of the components that use keys and
for which purpose can be seen below.

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
