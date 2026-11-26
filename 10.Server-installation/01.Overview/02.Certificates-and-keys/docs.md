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

Please refer to the [Mutual TLS section](../../../11.Server-integration/04.Mender-Gateway/10.Mutual-TLS-authentication/docs.md)
to find further details on the configuration of this feature.

### Service keys

The User Administration (`useradm`) and Device Authentication (`deviceauth`)
services sign JSON Web Tokens with a private key each. Anyone holding one of
these keys can forge tokens for users or devices. In production, create, store,
and rotate the keys yourself.

!!! If you don't provide the keys, the Mender Helm chart generates them. Use
!!! generated keys only for evaluation: they are not backed up, and with
!!! `helm template` or Argo CD they change on every render, which logs out every
!!! user and device.

#### Key files

Each service reads its keys from one Kubernetes Secret with two entries:

| Entry | Purpose |
| ----- | ------- |
| `private.pem` | Signs new tokens and verifies tokens. |
| `private-fallback.pem` | Only verifies tokens. During a rotation it holds the previous key; otherwise it holds the same key as `private.pem`. |

The services read the keys only at startup. Do not edit a Secret in place:
for every change, create a new Secret with the next revision suffix (`-v1`,
`-v2`, ...) and point the Helm chart to it. The new Secret name rolls out the
pods, and `helm rollback` restores a consistent pair of keys.

#### Generate the keys

Use a separate key for each service:

```bash
openssl genpkey -algorithm ed25519 -out useradm-private.pem
openssl genpkey -algorithm ed25519 -out deviceauth-private.pem
```

Store the keys in your secret manager. It is also your backup: the keys are not
part of the MongoDB database, so a database restore does not bring them back.

Before you create a Secret, check that every file holds a valid private key:

```bash
openssl pkey -in useradm-private.pem -noout && echo OK
openssl pkey -in deviceauth-private.pem -noout && echo OK
```

!!! The services silently ignore an empty file or a file without a PEM block,
!!! and run without that key. A missing file or a corrupted key stops the
!!! service at startup. Always run the check above.

#### Create the Secrets and configure the Helm chart

For the first installation, both entries hold the same key.

If the server already runs with keys generated by the Helm chart, reuse them as
K1 instead of generating new ones, so that users and devices stay logged in.
The chart stores them in the `rsa-useradm` and `rsa-device-auth` Secrets:

```bash
kubectl get secret rsa-useradm -o jsonpath='{.data.private\.pem}' | base64 -d > useradm-private.pem
kubectl get secret rsa-device-auth -o jsonpath='{.data.private\.pem}' | base64 -d > deviceauth-private.pem
```

Create the Secrets:

```bash
kubectl create secret generic mender-useradm-keys-v1 \
  --from-file=private.pem=useradm-private.pem \
  --from-file=private-fallback.pem=useradm-private.pem
kubectl create secret generic mender-device-auth-keys-v1 \
  --from-file=private.pem=deviceauth-private.pem \
  --from-file=private-fallback.pem=deviceauth-private.pem
```

Set the following Helm chart values:

```yaml
useradm:
  certs:
    existingSecret: mender-useradm-keys-v1
  customEnvs:
    - name: USERADM_SERVER_FALLBACK_PRIV_KEY_PATH
      value: /etc/useradm/rsa/private-fallback.pem

device_auth:
  certs:
    existingSecret: mender-device-auth-keys-v1
  customEnvs:
    - name: DEVICEAUTH_SERVER_FALLBACK_PRIV_KEY_PATH
      value: /etc/deviceauth/rsa/private-fallback.pem
```

! `useradm.customEnvs` and `device_auth.customEnvs` replace `default.customEnvs`
! for these services. If you set `default.customEnvs`, copy the entries you need
! into both lists.

#### Key lifecycle

Every operation in the table below follows the same steps:

1. Generate and check the new key, if the operation needs one.
1. Create the Secrets with the next revision suffix and the entries from the table.
1. Set `useradm.certs.existingSecret` and `device_auth.certs.existingSecret` to
   the new Secrets and run `helm upgrade` with `--wait`.
1. Delete the Secret revisions you no longer need for a rollback.

| Operation | `private.pem` | `private-fallback.pem` | When |
| --------- | ------------- | ---------------------- | ---- |
| Install | K1 | K1 | First installation. |
| Rotate | K2 | K1 | On your rotation schedule. |
| Retire | K2 | K2 | After the tokens signed by K1 that you want to keep have expired. |
| Compromise | K3 | K3 | Immediately when a key may have leaked. |

**Rotate.** Existing sessions, personal access tokens, and device tokens keep
working. While the pods roll out, a pod that does not know the new key yet
rejects tokens signed by it: devices authenticate again automatically, and some
users of the Mender UI may have to log in again.

**Retire.** Tokens signed by the old key stop working. Sessions expire after
`USERADM_JWT_EXP_TIMEOUT` and device tokens after `DEVICEAUTH_JWT_EXP_TIMEOUT`,
one week by default for both, so retire the old key at least one week after the
rotation; this also covers device tokens cached by the Device Authentication
service. [Personal access tokens](../../../11.Server-integration/01.Using-the-apis/docs.md#personal-access-tokens)
can be valid for up to `USERADM_TOKEN_MAX_EXPIRATION_SECONDS` (one year by
default), and tokens created without an expiration never expire. Personal access
tokens signed by the old key stop working when you retire it, and their owners
must create new ones. Waiting longer before you retire keeps them working, but
keeps trusting the old key for the same time.

**Compromise.** All sessions, personal access tokens, and device tokens stop
working at once. Leave all `private.id.<N>.pem` files (see
[Key identifiers](#key-identifiers)) out of the new User Administration Secret:
the service keeps accepting tokens signed by any of them. Users log in again and create new personal access tokens;
devices authenticate again automatically. If the Device Authentication service
uses the Redis cache (Mender Enterprise), it accepts cached device tokens
without checking their signature. Delete the cached tokens after the upgrade:

```bash
redis-cli --scan --pattern 'deviceauth:v1:tenant:*:tok' | xargs -r redis-cli unlink
```

Replace `deviceauth:v1` if you changed `DEVICEAUTH_REDIS_KEY_PREFIX`. With
Redis Cluster, run the command against every primary node.

!!! Until you retire the old key, users whose session was signed by it cannot
!!! log out or change their user settings: the server returns an error. Logging
!!! in again gives them a session signed by the new key.

#### Key identifiers

Earlier versions of this document described a rotation based on key files named
`private.id.<N>.pem` and the `kid` header of the user tokens. If you use such
files, keep them in the User Administration Secret: tokens carrying a matching
`kid` still verify. To retire one of these keys, leave its file out of the next
Secret revision.
