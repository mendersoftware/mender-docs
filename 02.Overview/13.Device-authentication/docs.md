---
title: Device Authentication
taxonomy:
    category: docs
    label: reference
---

You must explicitly authorize any device identified by a set of
[identity attributes](../../02.Overview/07.Identity/docs.md) before it can authenticate
with the Mender server.

This section describes the components and workflows relevant to device
authentication, and provides practical tips on navigating our APIs to
successfully authorize devices, monitor authorization status, and troubleshoot
related issues.

## Authentication service

A single service implements device authentication:

* [Device
  Authentication](https://github.com/mendersoftware/deviceauth?target=_blank)

The service exposes APIs for:

* device authorization, namely granting access to selected devices
* issuing and keeping track of authentication tokens ([JSON Web
  Token](https://jwt.io?target=_blank))
* inspecting and managing devices and their authentication credentials

## Identification and authentication

Mender identifies a **device** by a set of **identity attributes** (MAC addresses,
user-defined UIDs, etc.); think of it as an extension of a unique identifier
into a multi-attribute structure (see [Identity](../../02.Overview/07.Identity/docs.md)).

To obtain an auth token, the device sends an **authentication request**
containing the identity attributes and its current **public key**. The client signs
the request with the private key (kept secret on the device), and the server uses
the public key to verify the signature.

The combination of **identity attributes** and **public key** forms an
**authentication set**, or 'auth set' in short.

The concept takes into consideration device key rotation - a single device may
over time present different keys, and it's important to track those, and allow
the user to accept (i.e. authorize) or reject a particular identity/key
combination.

Mender keeps tracks both of a **device** as a single real-world entity, where each
device might create multiple **authentication sets**. Note
that maximum one authentication set can be accepted for a specific device at any
given time.

## Authorization Flows

Mender provides two possible authorization flows. Both involve a user's explicit
consent to authorize a device via the UI or Device Authentication API, but they differ
in the order of events and intended use cases. Below is a detailed breakdown of
each.

For details of API calls please consult the [API documentation](../../200.APIs/01.Open-source/02.Management-APIs/02.Device-authentication/docs.md).

### Authorize-on-request Flow

The simplest flow, which usually suits quick prototyping and testing best, is manual
authorization. The Mender server records every auth request for future inspection.
You can accept it via the Device Authentication API (or the UI) whenever you
see fit. When the device sends another auth request it will result in a successful
authorization.

The authorize-on-request flow therefore requires the user to accept
authentication sets one-by-one, as devices connect to the server. As such it is
not ideal for scenarios with many devices; we recommended it for
smaller or non-production installations instead.

The sequence diagram below describes the API interactions between the user,
Device, and Device Authentication within this flow:

1. The user provides the device with some identity attributes and a
   public key.
2. The device tries to authenticate, retries in a loop according to the Mender
   client's configured interval.
3. For the time being, authentication attempt fails, but the Mender server
   records the auth set for future inspection.
4. The user inspects pending authentication sets.
5. The user accepts the submitted auth set.
6. The device applies for an auth token again.
7. Device Authentication returns a valid authentication token.

| ![Authorize-on-request flow](authorize-on-req.png) |
|:--:|
|*Authorize-on-request flow*|

### Preauthorization Flow

Preauthorization is the idea of authorizing a device before it connects to
the server for the first time. This is an intuitive model analogous to creating
an account before logging in to an online service.

It allows you to authorize a particular device before it leaves the production line
by providing a pre-assigned authentication set to
the Device Authentication. When a device with the corresponding identity
attributes and public key requests authentication, the Mender server will
grant access immediately, without further user intervention.

Typically, this flow suits best a usual production use case, where you plan a release of a
potentially large batch of devices:

* You assign and track device identity attributes/keys outside of Mender.
* Manually or via script, the user preauthorizes the devices using the Device
  Authentication API.
* During the release process, you transfer identities and keys to physical
  devices.
* Upon the first authentication request for each device, the Mender server
  authenticates it, and the device gains access to all Mender APIs.

The sequence diagram below describes the API interactions between the user and
the Device Authentication within this flow:

1. The user first submits a preauthorized auth set to the Device Authentication.
2. The user makes sure the physical device contains the corresponding identity
   attributes and public key.
3. When the device activates, the client submits an authentication request containing the
   identity attributes and key.
4. The Device Authentication service returns a valid authentication token.

| ![Preauthorization flow](preauth.png) |
|:--:|
|*Preauthorization flow*|

## Authentication Token

After the Mender server authorizes a device, a subsequent authentication request
to the Device Authentication service returns an **authentication token**. The
Mender client will record the token and attach it to every API call under the HTTP
`Authorization` header.

The token does have an **expiry date** (one week period by default), but the Mender client
will obtain a fresh token automatically.
The only prerequisite is that the device authentication set is not in the
rejected state.

For details on the token format please see the relevant [documentation on
submitting an authentication request](../../200.APIs/01.Open-source/01.Device-APIs/01.Device-authentication/docs.md).

