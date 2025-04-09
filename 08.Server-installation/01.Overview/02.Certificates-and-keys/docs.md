---
title: Certificates and keys
taxonomy:
    category: docs
    label: tutorial
---

In order to secure the client-server and inter-service communication,
Mender leverages public key cryptography. Several key pairs are used
and each key pair consists of a *public key*, which in some cases has
a certificate that is shared with other services, and a *private key*,
which is kept secret by the service.
All keys are encoded in the PEM format. The public keys are shared in the
standard X.509 certificate format, `cert.crt` below,
while private keys are seen as `private.key` below.

See the [architecture](../01.Architecture/docs.md) for schematics of the service
communication flow. An overview of the components that use keys and
for which purpose can be seen below.

| Component | Purpose of keys | Shares certificate or key with |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| API Gateway | Listens to a public port for `https` requests only (plain `http` is disabled). These requests can come from Mender Clients that check for- or report status about updates through the [Device APIs](../../../200.Server-side-API/?target=_blank#device-apis), or from users and tools that manage deployments through the [Management APIs](../../../200.Server-side-API/?target=_blank#management-apis). | **Mender Clients** and users of the **Management APIs**, including web browsers accessing the **Mender UI**. |
| User Administration | Signs and verifies JSON Web Tokens that users of the [Management APIs](../../../200.Server-side-API/?target=_blank#management-apis), including end users of the Mender UI, include in their requests to authenticate themselves. | Nothing. The service gets signature verification requests from the API Gateway, so all keys are kept private to the service and not shared. |
| Device Authentication | Signs and verifies JSON Web Tokens that Mender Clients include in their requests to authenticate themselves when accessing the [Device APIs](../../../200.Server-side-API/?target=_blank#device-apis). | Nothing. The service gets signature verification requests from the API Gateway, so all keys are kept private to the service and not shared. |
| `mender-auth` Client | Signs requests for JSON Web Tokens sent to the Device Authentication service. `mender-auth` will request a new token when it connects to the Mender Server for the first time, and when a token expires. Other Mender services which use `mender-auth`, such as `mender-update` or `mender-connect`, includes a token in all their communication to authenticate themselves when accessing the [Device APIs](../../../200.Server-side-API/?target=_blank#device-apis). | The **Device Authentication** service stores../ the public keys of Mender Clients. |
| Mender Artifact | Signs and verifies [Mender Artifacts](../../../02.Overview/03.Artifact/docs.md). | The **Signing system** stores the private key used for signing Mender artifacts. After an artifact is signed using the private key it is verified by the **Mender-update Client**. |

### Mender Client

The `mender-auth` component, part of the Mender Client, does not need any special configuration regarding certificates as long as the server certificate
is signed by a Certificate Authority. The client will verify trust using its system root certificates, which
are typically provided by the `ca-certificates` package.

If the certificate is self-signed, the clients need to store the server certificate locally
(`keys-generated/cert/cert.crt`) in order to verify the server's authenticity.
Please see [the client section on building for production](../../../05.Operating-System-updates-Yocto-Project/06.Build-for-production/docs.md)
for a description on how to provision new device disk images with the new certificates. In this case, it
is advisable to ensure there is a overlap between the issuance of new certificates and expiration of old
ones so all clients are able to receive an update containing the new cert before the old one expires. You
can have two valid certificates for the Mender Server concatenated in the server.crt file. When all clients
have received the updated server.crt, the server configuration can be updated to use the new certificate.
In a subsequent update, the old certificate can be removed from the client's server.crt file.

!!! The key of the Mender Client itself is automatically generated and stored at `/var/lib/mender/mender-agent.pem` the first time the Mender Client runs. We do not yet cover rotation of Mender Client keys in live installations in this document.


### Mutual TLS

Mender Enterprise supports setting up a reverse proxy at the edge of the network, which can authenticate devices using TLS client certificates. Each client is equipped with a certificate signed by a CA certificate (Certificate Authority), and the edge proxy authenticates devices by verifying this signature. Authenticated devices are automatically authorized in the Mender backend, and do not need manual approval.

Please refer to the [Mutual TLS section](../../../09.Server-integration/04.Mender-Gateway/10.Mutual-TLS-authentication/docs.md)
to find further details on the configuration of this feature.

### User Administration Service

The Mender User Administration Service (`useradm`) is responsible for user authorization
and authentication. Once we verify the credentials we issue a JWT and sign it with a private key.
If a malicious actor gets hold of the key, the troubles may unravel. It is a standard security
practice to rotate the keys regularly. However, when this happens, we have to be sure
we can handle JWTs that are valid and in the wild. To this end, we introduced
a well-known concept of a key identification number (kid, id),
which also allows the key rotation.

This concept allows us to always have just a single active key for signing, but at the same time
allows verification with multiple keys that we used for signing at one point in the past.

#### JWT "kid" field

Each token issued by `useradm` carries a `kid` field in the header, which allows the service to determine
the key used to sign the token (and which we have to use to verify the signature).

The tokens issued before the introduction of this field are considered to have `kid=0`
and we verify them against the default key.

We assume the id is a low non-negative integer number, where `0` has a special meaning.

#### Key id and key filename relation

The key id is only stored in the file name, and the service maintains the relation key id -- key data
with the help of a regular expression pattern, which allows the retrieval the id from the name.
For instance, if the default key resides in `/etc/useradm/rsa/private.pem`, and the pattern
is `"private\\.id\\.([0-9]*)\\.pem"`, then the file -- id mapping would be as follows:

| file path | key id |
| --------- | ------ |
| /etc/useradm/rsa/private.id.2048.pem | 2048 |
| /etc/useradm/rsa/private.id.21172.pem | 21172 |
| /etc/useradm/rsa/private.id.22899.pem | 22899 |

#### Private key rotation

To perform rotation, we have first to generate a new private key, give it an id, and then configure
the service to use it, while maintaining the old one (to support long-lived tokens, 
such as the [personal access tokens](../../../09.Server-integration/01.Using-the-apis/docs.md#personal-access-tokens)).
In the remainder of this section, we assume that the key directory is `/etc/useradm/rsa`
and the default key path is `/etc/useradm/rsa/private.pem`. Please note that the service allows
you to configure the default path, but it now has two additional roles: the directory part is implicitly
the directory where the User Administration Service looks for the keys, and the default key
is the one we use to verify the JWTs with `kid` equal to 0 or with no `kid`.

##### Generate the key

Let's choose a key of type RSA, length `2048` bits, and id `5539`. The latter being arbitrary,
positive, non-zero integer which uniquely identifies the key in the file.

```shell
openssl genrsa -out /etc/useradm/rsa/private.id.5539.pem 2048
```

In the above command, the file name format `private.id.XXXX.pem` is no accident.
This default (and configurable) pattern that allows the service to determine
where the id is in the file name. Please note that setting id to `0` can make
the old JWTs (from before the introduction of `kid`) not work anymore.

There is no limitation on the keys' type; you can use and mix all the supported types.

##### Configure the service

Once done, we can configure the User Administration Service to use the new key by setting
`USERADM_SERVER_PRIV_KEY_PATH="/etc/useradm/rsa/private.id.5539.pem"`. Please note
that we did not touch the existing default key, which (by default) rests
in `/etc/useradm/rsa/private.pem` (this is also configurable). At this point
we will sign all new JWTs with the key of id `5539` and they will carry `kid=5539`,
and all the JWTs that do not have `kid` or have `kid=0` will be verified against
the default `/etc/useradm/rsa/private.pem`.

As long as any file matches the pattern and contains a valid key
in the default directory, we use it to verify the JWTs by `kid`, while
the key pointed by `USERADM_SERVER_PRIV_KEY_PATH` signs every new token.
To retire a key, all you have to do is remove the file.
