---
title: Mender Client
taxonomy:
    category: docs
---

## Certificate expired or not yet valid

The Mender client can not connect to the server, typically the first time it tries, and emits messages like the following to syslog at the device:

```
... level=info msg="Mender state: authorize-wait -> bootstrapped" module=mender
... level=error msg="authorize failed: transient error: authorization request failed: failed to execute authorization request:
Post https://<SERVER-URI>/api/devices/v1/authentication/auth_requests: x509: certificate has expired or is not yet valid" module=state
```

This could occur in several places, and the distinguishing message is **x509: certificate has expired or is not yet valid**.
Each TLS certificate has a validity period, *Not Before* and *Not After*, and this message means that the Mender client concludes that
the current time is outside this range.

Most commonly this is caused by **incorrect time setting at the device** which runs the Mender client. Check this by
running `date` at the device, and make sure it is correct. Consult the section on [Correct clock](../../devices/system-requirements#correct-clock) 
for a more detailed discussion.

If this is not the problem, you need to verify that the certificates you are using are valid.
Replace the hostname with the one for your Mender API Gateway below and run the following command:

```bash
echo | openssl s_client -connect mender.example.com:443 2>/dev/null | openssl x509 -noout -dates
```
> notBefore=Dec 14 19:52:46 2016 GMT  
> notAfter=Dec 12 19:52:46 2026 GMT  

Also note that the storage proxy has its own certificate, and it runs on the same host as the API Gateway
on port 9000 by default. Adjust the hostname and verify the validity of its certificate with the following command:

```bash
echo | openssl s_client -connect s3.example.com:9000 2>/dev/null | openssl x509 -noout -dates
```
> notBefore=Dec 14 19:52:46 2016 GMT  
> notAfter=Dec 12 19:52:46 2026 GMT  

We can see that both these certificates are currently valid.
Also see the [documentation on certificates](../../administration/certificates-and-keys) for an
overview and description on how to generate new certificates.


## Artifact format not supported

When deploying an update with the Mender client, you see a log message similar to the following:

```
ERRO[0001] update install failed: failed to read and install update: reader: unsupported version: 2  module=state
```

The problem here is most likely that you have built [a new version of the Artifact format](../../architecture/mender-artifacts#versions)
that your Mender Client does not support. It could also be that you are building a very old version of the
Artifact format that your new version of the Mender Client does not support.

In either case the solution is to [build a different version of the Artifact format](../../artifacts/modifying-a-mender-artifact#write-a-new-artifact) that your Mender Client supports
until you have upgraded all Mender Clients and can use the corresponding latest version of the Mender Artifact format.



## The partition layout of the device is not as expected

You have the Mender binary on your device and try to trigger a rootfs update but you get output similar to the following:

```bash
mender -rootfs /media/rootfs-image-mydevice.mender

ERRO[0000] exit status 1                                 module=partitions
ERRO[0000] No match between boot and root partitions.    module=main
```

The problem here is most likely that the device does not have the [partition layout Mender expects](../../devices/partition-layout). This could have happened if you just placed the Mender binary into your rootfs, but did not [reflash the entire storage device](../../artifacts/provisioning-a-new-device) with the `.sdimg.` file output from the [Yocto Project build](../../artifacts/building-mender-yocto-image). When this happens, output from `mount` and `fw_printenv` can confirm that this is the problem you are seeing. The solution is to flash your entire storage device with the `.sdimg` output from the Yocto Project build process.
