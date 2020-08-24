---
title: Client certificates
taxonomy:
    category: docs
---

Mender supports setting up an ambassador server which can authenticate devices using TLS client certificates. Each client is equipped with a certificate signed by a CA certificate (Certificate Authority), and the ambassador authenticates devices by verifying this signature. Devices that are authenticated are automatically authorized in the Mender backend, and do not need to be manually approved.

This is in particular useful in a mass production setting because you can sign client certificates when they are manufactured so they automatically get accepted into the Mender server when your customer turns them on, which might happen several months after manufacturing.

See [Device authentication](../../02.Overview/13.Device-authentication/docs.md) for a general overview of how device authentication works in Mender.


## Prerequisites


### A board integrated with Mender

You need a physical board that has already been integrated with Mender. For example, you may use one of the reference boards BeagleBone Black, Raspberry Pi 3 or Raspberry Pi 4.

If you have not yet prepared a device visit one of the following:

- [Client installation](../../03.Client-installation/chapter.md)
- [System updates: Debian family](../../04.System-updates-Debian-family/chapter.md)
- [System updates: Yocto Project](../../05.System-updates-Yocto-Project/chapter.md)

### Mender client and server connectivity

<!-- TODO, this section may need to be rewritten slightly. It's not really incorrect, but it doesn't fit perfectly either, since we will set up the ambassador. -->

Once your device boots with a newly provisioned disk image, it should already be correctly connecting to the Mender server. After booting the device you see it pending authorization in the Mender server UI, similar to the following.

![Mender UI - device pending authorization](device-pending-authorization.png)

If your device does not show as pending authorization in the Mender server once it is booted with the disk image, you need to diagnose this issue before continuing. See the [troubleshooting section on connecting devices](../../201.Troubleshoot/05.Device-Runtime/docs.md#mender-server-connection-issues) in this case.


### A CLI environment for your server

In order to access the the Mender server API with the commands below, you need to set up some shell variables in the terminal you will be using.

Follow the steps in [set up shell variables for cURL](../01.Using-the-apis/docs.md#set-up-shell-variables-for-curl).

### Mender-Artifact tool

Download the `mender-artifact` tool from the [Downloads section](../../09.Downloads/docs.md).


## Generate certificates

In this section we will generate and sign certificates for the server and the devices.


### Generate a CA certificate

<!--AUTOVERSION: "generate a % certificate"/ignore-->
First we need to generate a master certificate which will be used to sign each client certificate. We start by generating a private key:

```bash
openssl ecparam -genkey -name P-256 -noout -out ca-private.key
```

!!! The "P-256" curve can be switched with a different curve if necessary.

Next we create a configuration file which contains information about the Certificate Authority. Execute the following command to create the file:

```bash
cat > ca-cert.conf <<EOF
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

The fields should be filled with information about your organization, locality and contact information. In particular, make sure `commonName` matches the domain name of the server which will serve as the mTLS ambassador. <!-- TODO, link to ambassador setup -->

Then generate a certificate from the newly generated private key:

```bash
openssl req -new -x509 -key ca-private.key -out ca-cert.pem -config ca-cert.conf -days $((365*10))
```

! The `-days` argument specifies how long the certificate is valid, and can be adjusted if needed. The example expression gives a certificate which is valid for approximately 10 years. Since the CA certificate will only be used on the Mender server, it is usually not important that it expires, and it's better to have a long expiry time to avoid having to rotate certificates on the devices.


### Generate a client certificate

When preparing client certificate for a device, the certificate key will be generated on a separate system (not on the device), and then provisioned into the device storage. This way we can keep records of the public key of the device and ensure sufficient entropy during key generation, so the resulting keys are secure random.

!!! Make sure the system you generate keys on is adequately secured, as it will also generate the device private keys. You should consider securely deleting (e.g. `shred`) the *private* keys after provisioning the device if you do not truly need a record of them (you can keep the public keys, of course).

We will use OpenSSL to generate a private key using Elliptic Curve cryptography:

```bash
openssl ecparam -genkey -name P-256 -noout -out device-private.key
```

!!! The "P-256" curve can be switched with a different curve if necessary.

Next we create a configuration file which contains information about the device certificate. Execute the following command to create the file:

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

The field `commonName` is device specific, and needs to be changed for every device. The rest of the fields should be filled with information about your organization, locality and contact information.

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

The generation and signing of the client certificate needs to be repeated for each device, so these are natural steps to automate in your device provisioning workflow.


<!-- TODO: EVERYTHING FROM HERE AND DOWN TO "END_OF_SERVER_PART" NEEDS TO BE REWRITTEN. Originally copied from the Pre-Authorizing document. -->

## Preauthorize your device

Now that we have the device's identity and public key, we will use the Mender server management REST APIs to preauthorize it. The APIs are documented for both [Open Source](../../200.APIs/01.Open-source/02.Management-APIs/docs.md) and [Enterprise](../../200.APIs/02.Enterprise/02.Management-APIs/docs.md).


### Make sure there are no existing authentication sets for your device

First make sure to power off your device, so it does not continuously appear as pending in your server.

We recommend that you ensure there are no records of your device in the server; open the Mender UI, then go to *Devices* to see if it is there, then *Decommission* it.

Secondly, To make sure that the device has no existing authentication sets, we check `devauth` service for the identity of your device.

In the same terminal, run the following command:

```bash
curl -H "Authorization: Bearer $JWT" $MENDER_SERVER_URI/api/management/v2/devauth/devices | jq '.' > /tmp/devauth.json
```

!!! To make the response more readable, we use the `jq` utility to decode it. If it is not available on your system you can omit this pipe or replace it with a different indentation tool (e.g `python -m json.tool`).

Now open the file `/tmp/devauth.json` and search for a value of your device identity (e.g. `02:12:61:13:6c:42` if you are using MAC addresses).

If you do not get any matches in either files, great! Continue to the [next section](#call-the-preauthorize-api).

If you do have one or more matches you must first delete these existing authentication sets. Find the `id` of the authentication set and use the `DELETE` method towards the service. For example, if you find the identity in `devauth.json` and you see the authentication set has `id` `5ae3a39d3cd4d40001482a95` the run the following command:

```bash
curl -H "Authorization: Bearer $JWT" -X DELETE $MENDER_SERVER_URI/api/management/v2/devauth/devices/5ae3a39d3cd4d40001482a95
```

Once this is done, re-run the command above to generate the `devauth.json` file again and verify that your device identity does not exist anywhere.

In the event that the decommissioning operation fails, perform a [manual database cleanup via the provided CLI command](../../201.Troubleshoot/04.Mender-Server/docs.md#cleaning-up-the-deviceauth-database-after-device-decommissioning).

### Call the preauthorize API

Set your device identity as a JSON object in a shell variable:

```bash
DEVICE_IDENTITY_JSON_OBJECT_STRING='{"mac":"02:12:61:13:6c:42"}'
```

!!! Adjust the variable value to the actual identity of your device. If you have several identity attributes in your identity scheme, separate them with commas in JSON format inside this single object, for example `DEVICE_IDENTITY_JSON_OBJECT_STRING='{"mac":"02:12:61:13:6c:42", "serialnumber":"1928819"}'`.

Secondly, set the contents of the device public key you generated above in a second variable:

```bash
DEVICE_PUBLIC_KEY="$(cat keys-client-generated/public.key | sed -e :a  -e 'N;s/\n/\\n/;ta')"
```

Then simply call the [API to preauthorize a device](../../200.APIs/01.Open-source/02.Management-APIs/02.Device-authentication/docs.md#devices-post):

```bash
curl -H "Authorization: Bearer $JWT" -H "Content-Type: application/json" -X POST -d "{ \"identity_data\" : $DEVICE_IDENTITY_JSON_OBJECT_STRING, \"pubkey\" : \"$DEVICE_PUBLIC_KEY\" }" $MENDER_SERVER_URI/api/management/v2/devauth/devices
```

If there is no output from the command, this indicates it succeeded. To verify, list the currently registered authentication sets and make sure there is one for your device with the `preauthorized` status:

```bash
curl -H "Authorization: Bearer $JWT" $MENDER_SERVER_URI/api/management/v2/devauth/devices | jq '.'
```

Your device should now be preauthorized and accepted to the Mender server once it connects with the exact same identity and key.

<!-- END_OF_SERVER_PART -->


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

Next, open `mender.conf` in any text editor, and add the following content:

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

!!! Since this change is the same on every device, it is natural to automate this as part of the build process for the disk image. See file installation instructions for [the Debian family](../../.04.System-updates-Debian-family/Customize-Mender#configuration-file) or [the Yocto Project](../../System-updates-Yocto-Project/Customize-Mender#configuration-file) for more information.


## Boot the device

Now provision the storage with this new disk image, just like you have done in the past. If you are using a SD card, insert it into your workstation and use a command similar to the following:

```bash
sudo dd if=<PATH-TO-IMAGE>.sdimg of=<DEVICE> bs=1M && sudo sync
```

Then insert the SD card back into your device and boot it.


## Verify the device is accepted

If everything went as intended, your device will get the `accepted` status in the Mender server. You can log in to the Mender UI to ensure your device is listed and reports inventory.

If your device is not showing up, make sure the certificates are installed correctly both on the server and on the device. Check client logs and/or server logs for error messages that can identify what is wrong.
