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

Most commonly this is caused by incorrect time setting at the device which runs the Mender client. Check this by
running `date` at the device, and make sure it is correct.

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
Also see the [documentation on certificates](../../Administration/Certificates-and-keys) for an
overview and description on how to generate new certificates.



## The partition layout of the device is not as expected

You have the Mender binary on your device and try to trigger a rootfs update but you get output similar to the following:

```bash
mender -rootfs /media/rootfs-image-mydevice.mender

ERRO[0000] exit status 1                                 module=partitions
ERRO[0000] No match between boot and root partitions.    module=main
```

The problem here is most likely that the device does not have the [partition layout Mender expects](../../Devices/Partition-layout). This could have happened if you just placed the Mender binary into your rootfs, but did not [reflash the entire storage device](../../Artifacts/Provisioning-a-new-device) with the `.sdimg.` file output from the [Yocto Project build](../../Artifacts/Building-Mender-Yocto-image). When this happens, output from `mount` and `fw_printenv` can confirm that this is the problem you are seeing. The solution is to flash your entire storage device with the `.sdimg` output from the Yocto Project build process.
