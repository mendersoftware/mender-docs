---
title: Security
taxonomy:
    category: docs
---

Delivering updates securely, maintaining the identity of the communication
endpoints, and ensuring message authentication is critical to a secure software
update. This section gives a brief overview of how Mender ensures a secure
end-to-end update process.

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
[Preauthorizing devices](../../06.Server-integration/02.Preauthorizing-devices/docs.md)
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

