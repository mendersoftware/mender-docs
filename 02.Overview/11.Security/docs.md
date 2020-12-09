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

A Device, running the Mender client, communicates with the Mender server in order
to authorize, get updates, update inventory data, and deliver status information.

Communication between the client and server happens via a REST API over a
TLS-encrypted channel. The Mender client relies on the operating system’s root
Certificate Authorities (CAs) to verify the server identity by default. You can
also configure the client to use a specific certificate for chain validation,
e.g. when using self-signed certificates.

This ensures that the Mender client will only connect to a verified server, and
no man-in-the-middle attack is possible.


### No open ports on the Device

The client initiates all communication by connecting to the server, so
*no open ports* are required on the device in order to use Mender. As long as
the Mender client can connect to the server over HTTPS, you can schedule updates.


### Client authentication

Each Device has a unique public and private RSA key with a default length of
3072 bits.  You can generate this offline and provision it with the Device
storage, otherwise the Mender client will automatically generate a key pair
when it launches for the first time. Once generated, private key cannot be
changed or retrieved by means of API calls. If you decide to re-generate the
keys on the Device, it will require going through the authorization process
again. The client passes the public key in authorization requests to the server and
you can see the public key of a Device in the Mender UI.

You can find more information in the
[Device authentication](../13.Device-authentication/docs.md)
and
[Preauthorizing devices](../../08.Server-integration/02.Preauthorizing-devices/docs.md)
sections.


### Software Artifact verification

The Mender client has the ability to verify that the update comes from a
trusted source. This is an additional layer of security, independent of the
communication channel. If Artifact signature verification is enabled, the
client needs to have access to the public part of the keypair used for signing
the Artifacts.  To enable Artifact signature verification, configure the path
of the public key file using the
[ArtifactVerifyKey](../../03.Client-installation/06.Configuration-file/50.Configuration-options/docs.md#artifactverifykey)
configuration option of the Mender client.

You can find more information in the
[Sign & Verify](../../06.Artifact-creation/07.Sign-and-verify/docs.md) section.


## User authentication and authorization

As a user, you interact with your Devices either via API calls issued to the
Mender server, or via the web UI. In both cases, the connection is HTTPS
encrypted with TLS. To authenticate with the Mender server, a user must log in
by presenting a valid email address and password, as well as a Two Factor
authentication code (if available in the plan and enabled). The client
(e.g. web UI) used to log in then receives a JWT token with a default expiration
time of one week.

As an additional layer of security, Mender Enterprise supports [Role Based Access
Control](../12.Role.Based.Access.Control/docs.md) to limit authorization of users.

## Hardware security

The Mender client can utilize private keys stored in [Hardware Security
Modules (HSM)](https://en.wikipedia.org/wiki/Hardware_security_module) or in
[Trusted Platform Modules (TPM)](https://en.wikipedia.org/wiki/Trusted_Platform_Module).
This is an additional layer of security which eliminates storage of private keys
(secrets) as plain text files on the device, making it harder for an attacker
to gain access to keys to impersonate devices.

<!--AUTOVERSION: "Starting with the Mender Client %,"/ignore-->
Starting with the Mender Client 2.4.0, the client uses OpenSSL for cryptographic
operations, which enables usage of
<!--AUTOVERSION: "www.openssl.org/docs/man%"/ignore-->
[OpenSSL Engine's](https://www.openssl.org/docs/man1.1.1/man1/engine.html) as
abstractions for HSM.

For the Mender client to be able to utilize an HSM, OpenSSL must first be
configured appropriately, and this is normally vendor specific. Please see
the following tutorial for vendor specific instructions:
- [Secure IoT with Mender and NXP EdgeLock SE050](https://hub.mender.io/t/secure-iot-with-mender-and-nxp-edgelock-se050/2744)

The Mender client supports [PKCS#11](https://tools.ietf.org/html/rfc7512), or
any other HSM access methods that are supported by
<!--AUTOVERSION: "www.openssl.org/docs/man%"/ignore-->
[OpenSSL Engine's](https://www.openssl.org/docs/man1.1.1/man1/engine.html). See
[Mender client configuration sections](https://docs.mender.io/client-installation/configuration-file/configuration-options#httpsclient) for additional details.

Currently, Mender supports hardware security engines for SSL handshake, mTLS,
and authentication request signing.

## Remote Terminal

With Mender, you can start an interactive shell to any accepted device by clicking "Launch a new Terminal" in the UI.
The name of the feature is [Remote Terminal](../../02.Overview/14.Remote.Terminal/docs.md).
Remote Terminal is an optional feature.
One part of the Remote terminal configuration is the username of the user on the device for whom the shell will be created.
Using Remote Terminal you can execute any command the user on the device can execute.
Like with any other operation, the Mender backend will allow only authenticated Mender users to access the Remote Terminal.
You can apply additional restrictions on which Mender users can access Remote Terminal using RBAC.
The [mender-shell](https://github.com/mendersoftware/mender-shell), part of the Remote Terminal that is running on the device,
obtains device token through DBus API. It is the same token Mender client is using.
<!--AUTOVERSION: "https://tools.ietf.org/html/rfc6455#section-%"/ignore-->
The mender-shell uses [Encrypted WebSocket connections](https://tools.ietf.org/html/rfc6455#section-11.1.2) to communicate with the server.
In general, the security impact of enabling Remote Terminal is similar to the one when enabling SSH.
The connection to the device is secure, but there are no limitations on what command the user can execute,
except for the user permissions on the device.
There are also some important differences between enabling Remote Terminal and enabling SSH server on the device.
Remote Terminal does not opens or listens on any port and the connection is initiated by the device.
