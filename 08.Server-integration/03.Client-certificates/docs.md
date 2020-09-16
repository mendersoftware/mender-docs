---
title: Client certificates
taxonomy:
    category: docs
---

Mender supports setting up a reverse proxy at the edge of the network, which can authenticate devices using TLS client certificates. Each client is equipped with a certificate signed by a CA certificate (Certificate Authority), and the edge proxy authenticates devices by verifying this signature. Authenticated devices are automatically authorized in the Mender backend, and do not need manual approval.

This is in particular useful in a mass production setting because you can sign client certificates when they are manufactured so they automatically get accepted into the Mender server when your customer turns them on, which might happen several months after manufacturing.

See [Device authentication](../../02.Overview/13.Device-authentication/docs.md) for a general overview of how device authentication works in Mender.

If you are using Hosted Mender, you can host the mTLS ambassador in your infrastructure and point it to the upstream server `https://hosted.mender.io`.
In case you need assistance or use a hosted mTLS ambassador, contact us describing your use case.

## Prerequisites


### A board integrated with Mender

You need a physical board that has already been integrated with Mender. For example, you may use one of the reference boards BeagleBone Black, Raspberry Pi 3 or Raspberry Pi 4.

If you have not yet prepared a device visit one of the following:

- [Client installation](../../03.Client-installation/chapter.md)
- [System updates: Debian family](../../04.System-updates-Debian-family/chapter.md)
- [System updates: Yocto Project](../../05.System-updates-Yocto-Project/chapter.md)

### A CLI environment for your server

Follow the steps in [set up shell variables for cURL](../01.Using-the-apis/docs.md#set-up-shell-variables-for-curl) to set up some shell variables in the terminal you will be using.

### Mender-Artifact tool

Download the `mender-artifact` tool from the [Downloads section](../../09.Downloads/docs.md).


## Generate certificates

The following sections guide you to generate and sign certificates for the server and the devices.

!!! This document aims to provide you the basics to evaluate the mTLS authentication in Mender, and you should not consider it as a basis for production-grade PKI (Public-Key infrastructure) infrastructure. If you need to create a production-grade PKI, please start reading the [OpenSSL PKI tutorial](https://pki-tutorial.readthedocs.io/en/latest/).

### Generate a CA certificate

<!--AUTOVERSION: "generate a % certificate"/ignore-->
First generate a master certificate to sign each client certificate. Start by generating a private key::

```bash
openssl ecparam -genkey -name P-256 -noout -out ca-private.key
```

!!! You can switch the "P-256" with a different curve if necessary.

Next, create a configuration file which contains information about the Certificate Authority. Execute the following command to create the file:

```bash
cat > ca-cert.conf <<EOF
[req]
distinguished_name = req_distinguished_name
prompt = no

[req_distinguished_name]
commonName=My CA
organizationName=My Organization
organizationalUnitName=My Unit
emailAddress=myusername@example.com
countryName=NO
localityName=Oslo
stateOrProvinceName=Oslo
EOF
```

Fill the fields with information about your organization, locality and contact information.

Then generate a certificate from the newly generated private key:

```bash
openssl req -new -x509 -key ca-private.key -out ca-cert.pem -config ca-cert.conf -days $((365*10))
```

! The `-days` argument specifies how long the certificate is valid, and can be adjusted if needed. The example expression gives a certificate which is valid for approximately 10 years. Since the CA certificate will only be used on the Mender server, it is usually not important that it expires, and it's better to have a long expiry time to avoid having to rotate certificates on the devices.


### Generate a server certificate

!!! Make sure the system you generate keys on is adequately secured, as it will also generate the server private key.

Use OpenSSL to generate a private key using Elliptic Curve cryptography:

```bash
openssl ecparam -genkey -name P-256 -noout -out server-private.key
```

!!! You can switch the "P-256" curve with a different curve if necessary.

Next, we create a configuration file which contains information about the server certificate. Execute the following command to create the file:

```bash
cat > server-cert.conf <<EOF
[req]
distinguished_name = req_distinguished_name
prompt = no

[req_distinguished_name]
commonName=my-server.com
organizationName=My Organization
organizationalUnitName=My Unit
emailAddress=myusername@example.com
countryName=NO
localityName=Oslo
stateOrProvinceName=Oslo
EOF
```

Fill the fields with information about your organization, locality and contact information. In particular, make sure `commonName` matches the edge proxy's domain name, which will serve as the mTLS ambassador.

Then generate a certificate request from the newly generated private key:

```bash
openssl req -new -key server-private.key -out server-cert.req -config server-cert.conf
```

### Sign the server certificate

Now that we have both a CA certificate, and a certificate request for the server, we need to sign the latter with the former. This produces a signed certificate the edge proxy will use to terminate the TLS traffic.

```bash
openssl x509 -req -CA ca-cert.pem -CAkey ca-private.key -CAcreateserial -in server-cert.req -out server-cert.pem -days $((365*2))
```

! The `-days` argument specifies how long the certificate is valid, and can be adjusted if needed. The example expression gives a certificate which is valid for approximately 2 years.


### Generate a client certificate

When preparing a client certificate for a device, the certificate key is generated on a separate system (not on the device), and then provisioned into the device storage. This way you can keep records of the public key of the device and ensure sufficient entropy during key generation, so the resulting keys are secure random.

!!! Make sure the system you generate keys on is adequately secured, as it will also generate the device private keys. You should consider securely deleting (e.g. `shred`) the *private* keys after provisioning the device if you do not truly need a record of them (you can keep the public keys).

Once again, use OpenSSL to generate a private key using Elliptic Curve cryptography:

```bash
openssl ecparam -genkey -name P-256 -noout -out device-private.key
```

!!! You can switch the "P-256" curve with a different curve if necessary.

Next, we create a configuration file which contains information about the device certificate. Execute the following command to create the file:

```bash
cat > device-cert.conf <<EOF
[req]
distinguished_name = req_distinguished_name
prompt = no

[req_distinguished_name]
commonName=my-device-hostname.com
organizationName=My Organization
organizationalUnitName=My Unit
emailAddress=myusername@example.com
countryName=NO
localityName=Oslo
stateOrProvinceName=Oslo
EOF
```

The field `commonName` is device specific, and needs to be changed for every device. Fill the rest of the fields with information about your organization, locality and contact information.

Then generate a certificate request from the newly generated private key:

```bash
openssl req -new -key device-private.key -out device-cert.req -config device-cert.conf
```


### Sign the client certificate

Now that we have both a CA certificate, and a certificate request for the device, we need to sign the latter with the former. This produces a signed certificate which the server will recognize when the client connects.

```bash
openssl x509 -req -CA ca-cert.pem -CAkey ca-private.key -CAcreateserial -in device-cert.req -out device-cert.pem -days $((365*10))
```

! The `-days` argument specifies how long the certificate is valid, and can be adjusted if needed. The example expression gives a certificate which is valid for approximately 10 years. Since the certificate will only be used by the server to authenticate devices, it is usually not desirable that it expires after a short time, since this requires certificate rotation on the devices. To manage compromised devices, it is often better to maintain a certificate blacklist on the server.

You need to repeat the generation and signing of the client certificate for each device, so these are natural steps to automate in your device provisioning workflow.


## Set up the mTLS edge proxy to authenticate devices using mTLS

The mTLS ambassador acts as an edge proxy running in front of your Mender server. The Mender client running on the devices connects to it, providing its client TLS certificate and establishing a mutual TLS authentication. If the client certificate's signature matches the certification authority recognized by the mTLS ambassador, the Mender server will automatically accept the device. The edge proxy transparently forwards all the requests from the Mender client to the Mender server. From the client's perspective, it provides the same API end-points as the upstream Mender server.

The mTLS ambassador is distributed as a Docker image and can be run on a Docker host, using docker-compose or on Kubernetes.

The following certificates are needed to start the service:

* `server.crt`, a regular HTTPS server certificate the ambassador can use to terminate the TLS connections
* `server.key`, the corresponding private key for the certificate above
* `ca.crt`, the Certification Authority's certificate used to sign the server and client certificates.

You also need to specify a username and password pair. The ambassador will use it to connect to the Mender server to authorize clients who connect using a valid certificate signed by the known CA.

To start the edge proxy, run the following command:

<!--AUTOVERSION: "registry.mender.io/mendersoftware/mtls-ambassador:%"/mtls-ambassador-->
```bash
docker run \
  -p 443:8080
  -e MTLS_MENDER_USER=mtls@mender.io \
  -e MTLS_MENDER_PASS=password \
  -e MTLS_MENDER_BACKEND=https://hosted.mender.io \
  -e MTLS_DEBUG_LOG=true \
  -v $(pwd)/server-cert.pem:/etc/mtls/certs/server/server.crt \
  -v $(pwd)/server-private.key:/etc/mtls/certs/server/server.key \
  -v $(pwd)/ca-cert.pem:/etc/ssl/certs/ca.crt \
  registry.mender.io/mendersoftware/mtls-ambassador:1.0.0
```

Replace the following values with the ones that match your configuration:

* **MTLS_MENDER_USER** and **MTLS_MENDER_PASS** are the user security credentials that allow the mTLS ambassador to connect to the Mender server and authorize new devices connecting using the mTLS authentication.
* **MTLS_MENDER_BACKEND** is the URL of the upstream Mender server; the edge proxy will forward the HTTPS requests to.
* **MTLS_DEBUG_LOG** (optional) enables verbose debugging log.
* **server.crt** and **server.key** are the paths to your server TLS certificate and key.
* **ca.crt** is the file which contains the certificate of the Certification Authority.

You can now publish the HTTPS port of the host to the Internet to let the clients connect to it.

## Enable generated key and certificate in disk image

Now that we have generated a key and certificate for the device and signed the certificate, we need to copy them to our working disk image (it typically has the `.sdimg` suffix), and enable them in the Mender configuration.

### Copy key and certificate into disk image

Find the location of the [key and certificate we generated](#generate-certificates) and copy it into place on the data partition by running the following commands:

```bash
mender-artifact install -m 600 device-private.key mender-disk-image.sdimg:/data/mender/mender-cert-private.pem
mender-artifact install -m 644 device-cert.pem mender-disk-image.sdimg:/data/mender/mender-cert.pem
```

!!! The files we just added are per device, and therefore it is natural to automate this step in your device provisioning workflow.

### Set up Mender configuration for client certificate

First, copy the existing `mender.conf` out of the disk image, so that we can edit it.

```bash
mender-artifact cp mender-disk-image.sdimg:/etc/mender/mender.conf mender.conf
```

Next, open `mender.conf` in a text editor, and add the following content:

```json
  "HttpsClient": {
    "Certificate": "/data/mender/mender-cert.pem",
    "Key": "/data/mender/mender-cert.pem"
  }
```

Make sure that the result is valid JSON, in particular that commas appear on every line except the last in a block. The snippet should be added inside the first set of curly braces in the file. For example, it might look like this in a typical `mender.conf` file:

```json
{
  "ServerURL": "https://hosted.mender.io/",
  "TenantToken": "TENANT_TOKEN",
  "HttpsClient": {
    "Certificate": "/data/mender/mender-cert.pem",
    "Key": "/data/mender/mender-cert.pem"
  }
}
```

Then copy the modified file back into the disk image:

```bash
mender-artifact cp mender.conf mender-disk-image.sdimg:/etc/mender/mender.conf
```

!!! Since this change is the same on every device, it is natural to automate this as part of the build process for the disk image. See file installation instructions for [the Debian family](../../04.System-updates-Debian-family/03.Customize-Mender/docs.md#configuration-file) or [the Yocto Project](../../05.System-updates-Yocto-Project/05.Customize-Mender/docs.md#configuration-file) for more information.


## Boot the device

Now provision the storage with this new disk image, just like you have done in the past. If you are using a SD card, insert it into your workstation and use a command similar to the following:

```bash
sudo dd if=<PATH-TO-IMAGE>.sdimg of=<DEVICE> bs=1M && sudo sync
```

Then insert the SD card back into your device and boot it.


## Verify that the device is accepted

If everything went as intended, your device shows up as `accepted` status in the Mender server. You can log in to the Mender UI to ensure your device is listed and reports inventory.

If your device is not showing up, make sure the certificates are installed correctly both on the server and on the device. Check client logs and/or server logs for error messages that can identify what is wrong. See the [troubleshooting section on connecting devices](../../201.Troubleshoot/05.Device-Runtime/docs.md#mender-server-connection-issues) in this case.
