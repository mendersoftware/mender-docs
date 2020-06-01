---
title: Deployments v2
taxonomy:
    category: docs
api: true
---

## Security of the update process

Mender allows you to update software on a fleet of devices. Delivering updates
securely, maintaining the identity of the communication endpoints, and ensuring
message authentication, are the keys to a secure software update. This section gives a brief
overview of how Mender addresses these problems.

## Communication channels

### Device -- Mender server

A device, running the Mender client, communicates with the Mender server in order
to authorize, get updates, update inventory data, and deliver status information.

Communication between the client and server happens via a REST API over a TLS-encrypted
channel. All communication uses encryption, and the client signs all requests to ensure
authenticity (see below).

The client initiates all communication in the Mender system by connecting to
the server. The client devices does not require any open ports that are listening
for incoming connections. As long as the Mender client can connect to the server
and storage proxy using TLS, you can schedule updates.


### User -- Device

As a user, you interact with your devices either via API calls issued to the Mender
server, or via the web UI. In both cases, the connection is HTTPS encrypted with TLS v1.2.
In order to access the API, you have to present a valid JWT token issued at the moment of login
with the default expire time of one week.

## Authentication of requests and devices

### Keys

Each device has a public and private RSA key with a default length of 3072 bits. 
You can generate this offline and add it to the target filesystem, or the Mender client
will automatically generate the key pair when it launches for the first time.
Once generated, the key pair cannot be changed or retrieved by means of API calls. If you
decide to re-generate the keys on the device, it will mean going through the authorization
process again. The client passes the public key in the authorization request (see below) to the server. 

The client uses the keys to cryptographically sign the requests, as we describe below.

### Signed requests and device authentication
Mender requires you to authenticate the devices before they are considered part of the fleet
(i.e., they can be updated or provide inventory data). To request authentication a device calls
the `/auth_requests` endpoint, with a POST body containing at least the following:
* identity data
* public key

The server needs to be as sure as possible the request originates from a device in 
question. To this end, client attaches an RSA PKCS#1 v1.5 signature, and the server
verifies it, based on the public key known for the device. When the verification
succeeds, the server issues a JWT token, which the device uses in all subsequent
calls.

The server rejects any call that has an invalid signature or a bad or missing JWT.

## Security of a remote software update

### Key aspects

In this section we have presented the key points for a secure update process.
In summary, these are:
* every communication channel uses encryption
* the server cryptographically checks the origin of every authorization request
* there are no open ports on a device
* calls have to carry a valid JWT token

### Managing updates

These sections cover some additional security-related concerns.

#### Unauthorized/accidental deployment

Only authorized users can interact with the Mender server, and only the server interacts with devices.
There is no way for someone without a valid JWT token or working login/password to create
a deployment. To provide an extra layer of authentication Mender Professional supports two factor
authentication. To decrease probability of unintended deployments Mender provides
a role based access control system (Mender Enterprise only).

#### Updating the wrong device

You define a deployment to target either a group of devices or a specific device. When a device
asks for an update the Mender server does the matching of artifact based on the deployment
parameters and device type. This ensures that device gets compatible artifacts.

#### Outdated software on devices

Mender provides easy to read reports showing the version of software on all devices in your fleet.
This enables you to ensure that you have installed critical updates on all required devices.

#### Bricking a device

You can understand secure updates also as a process that does not render a device unusable. Mender
assures that this will never happen by providing a roll back mechanism upon unsuccessful deployment.

#### Full rootfs, binary delta, update module

Mender supports three types of updates, each with security and robustness considerations.

The full rootfs update is the slowest but ensures that nothing of the old version remains.
The artifacts also carry the biggest payload, so it takes the longest to upload/download them.

The binary delta is a variation of full rootfs update, where only the differences from the current
version to the new version are present in the artifact payload.

Update modules let you change, for instance, a single file on a device in case there was a security
problem detected that you need to fix quickly.
