---
title: Security
taxonomy:
    category: docs
---

Delivering updates securely, maintaining the identity of the communication
endpoints, ensuring message authentication, together with integration
with hardware security solutions are critical factors in a secure
software update. This section gives a brief overview of how Mender
ensures a secure end-to-end update process.

## Server authentication

A Device, running the Mender Client, communicates with the Mender Server in order
to authorize, get updates, update inventory data, and deliver status information.

Communication between the Client and Server happens via a REST API over a
TLS-encrypted channel. The Mender Client relies on the operating system’s root
Certificate Authorities (CAs) to verify the server identity by default. You can
also configure the Client to use a specific certificate for chain validation,
e.g. when using self-signed certificates.

This ensures that the Mender Client will only connect to a verified server, and
no man-in-the-middle attack is possible.


### No open ports on the Device

The Client initiates all communication by connecting to the server, so
*no open ports* are required on the device in order to use Mender. As long as
the Mender Client can connect to the server over HTTPS, you can schedule updates.


### Client authentication

Each Device has a unique RSA or Elliptic Curve (P-256 or Ed25519) key pair (public
and private key). You can generate this offline and provision it with the Device
storage, otherwise the Mender Client will automatically generate an Ed25519 key pair
when it launches for the first time. Once generated, private key cannot be changed
or retrieved by means of API calls. If you decide to re-generate the keys on the
Device, it will require going through the authorization process again. The Client
passes the public key in authorization requests to the server and you can see the
public key of a Device in the Mender UI.

<!-- AUTOVERSION: "version %"/ignore -->
!!!!! Mender Client version 4.1.0 and later generates an Ed25519 key pair by
!!!!! default, while prior versions generated a 3072 bit RSA key by default.
!!!!! These have the same security level (128 bit), but the Ed25519 keys are
!!!!! smaller and more efficient.

You can find more information in the
[Device authentication](../13.Device-authentication/docs.md)
and
[Preauthorizing devices](../../08.Server-integration/02.Preauthorizing-devices/docs.md)
sections.


### Software Artifact verification

The Mender Client has the ability to verify that the update comes from a
trusted source. This is an additional layer of security, independent of the
communication channel. If Artifact signature verification is enabled, the
client needs to have access to the public part of the key pair used for signing
the Artifacts.  To enable Artifact signature verification, configure the path
of the public key file using the
[ArtifactVerifyKey](../../03.Client-installation/07.Configuration/50.Configuration-options/docs.md#artifactverifykey)
configuration option of the Mender Client.

You can find more information in the
[Sign & Verify](../../06.Artifact-creation/07.Sign-and-verify/docs.md) section.


## User authentication and authorization

As a user, you interact with your Devices either via API calls issued to the
Mender Server, or via the web UI. In both cases, the connection is HTTPS
encrypted with TLS. A user must log in to authenticate with the Mender Server
by presenting a valid email address, password, and a two-factor authentication
token if enabled. The Client receives a JWT token valid for one week if the
log-in is successful.

As an additional layer of security, Mender Enterprise supports [Role Based Access
Control](../12.Role.Based.Access.Control/docs.md) to limit authorization of users.


## Hardware security

The Mender Client can utilize private keys stored in [Hardware Security
Modules (HSM)](https://en.wikipedia.org/wiki/Hardware_security_module) or in
[Trusted Platform Modules (TPM)](https://en.wikipedia.org/wiki/Trusted_Platform_Module).
This is an additional layer of security which eliminates storage of private keys
(secrets) as plain text files on the device, making it harder for an attacker
to gain access to keys to impersonate devices.

<!--AUTOVERSION: "Starting with the Mender Client %,"/ignore-->
Starting with the Mender Client 2.4.0, the Client uses OpenSSL for cryptographic
operations, which enables usage of
<!--AUTOVERSION: "www.openssl.org/docs/man%"/ignore-->
[OpenSSL Engine's](https://www.openssl.org/docs/man1.1.1/man1/engine.html) as
abstractions for HSM.

For the Mender Client to be able to utilize an HSM, OpenSSL must first be
configured appropriately, and this is normally vendor specific. Please see
the following tutorial for vendor specific instructions:
- [Secure IoT with Mender and NXP EdgeLock SE050](https://hub.mender.io/t/secure-iot-with-mender-and-nxp-edgelock-se050/2744)

The Mender Client supports [PKCS#11](https://tools.ietf.org/html/rfc7512), or
any other HSM access methods that are supported by
<!--AUTOVERSION: "www.openssl.org/docs/man%"/ignore-->
[OpenSSL Engine's](https://www.openssl.org/docs/man1.1.1/man1/engine.html). See
[Mender Client configuration sections](https://docs.mender.io/client-installation/configuration/configuration-options#httpsclient) for additional details.

Currently, Mender supports hardware security engines for SSL handshake, mTLS,
and authentication request signing.


## Denial of Service (DoS / DDoS)

The Mender Enterprise server supports configurable API rate limits. When a device or a user is
crossing the rate limit threshold, it will receive the HTTP status code `429 Too Many Requests`.

You can configure the server to enforce these limits based on the client IP and the identity
of the API caller, either device or user. Rate limits can apply to all the API calls, or you can
customize them for specific API end-points.
