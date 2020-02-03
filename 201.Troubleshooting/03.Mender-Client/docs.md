---
title: Mender Client
taxonomy:
    category: docs
---

## Obtaining client logs

Logs are usually needed in order to diagnose an issue.

The Mender client by default logs to the system log using `systemd`, so the easiest way to retrieve logs
is to run the following command:

```
journalctl -u mender
```

Please note that the default log level is Info. It is possible to increase the
verbosity by editing the Mender systemd unit file and append the `--debug` option.

### Deployment log files

In addition to system logging, Mender also writes debug logs directly to a file when
a deployment starts. This file in turn gets uploaded to the server if the
deployment fails.

By default, log files for the past 5 deployments are kept.
They are stored in `/var/lib/mender/`, named by the deployment id,
for example `deployments.0001.fcd8bca2-6dae-488e-969e-23559c674ba5.log`.


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

Most commonly this is caused by **incorrect time setting on the device** which runs the Mender client. Check this by
running `date` on the device, and make sure it is correct. Consult the section on [Correct clock](../../devices/general-system-requirements#correct-clock)
for a more detailed discussion.

To determine the status of your time synchronization, execute the following:

   ```bash
   # timedatectl status
   ```

Note that it can take some time after boot before the time
synchronization is completed. If after 5-10 minutes, the time still
has not synchronized, consult with your local network administrator
for further troubleshooting.

If this is not the problem, you need to verify that the certificates you are using are valid.
Replace the hostname with the one for your Mender API Gateway below and run the following command:

```bash
echo | openssl s_client -connect mender.example.com:443 2>/dev/null | openssl x509 -noout -dates
```
> ```
> notBefore=Dec 14 19:52:46 2016 GMT
> notAfter=Dec 12 19:52:46 2026 GMT
> ```

Also note that the storage proxy has its own certificate, and it runs on the same host as the API Gateway
on port 9000 by default. Adjust the hostname and verify the validity of its certificate with the following command:

```bash
echo | openssl s_client -connect s3.example.com:9000 2>/dev/null | openssl x509 -noout -dates
```
> ```
> notBefore=Dec 14 19:52:46 2016 GMT
> notAfter=Dec 12 19:52:46 2026 GMT
> ```

We can see that both these certificates are currently valid.
Also see the [documentation on certificates](../../administration/certificates-and-keys) for an
overview and description on how to generate new certificates.


## Certificate signed by unknown authority

The Mender client can not connect to the server, typically the first time it tries, and emits messages like the following to syslog at the device:

```
... level=info msg="Mender state: authorize-wait -> bootstrapped" module=mender
... level=error msg="authorize failed :transient error :authorisation request failed: failed do execute authorisation request:
Post https://<SERVER-URI>/api/devices/v1/authentication/auth_requests: x509: certificate signed by unknown authority" module=state
```

This could occur in several places, and the distinguishing message is **x509: certificate signed by unknown authority**.
The message shows that the Mender client rejects the Mender server's certificate because it does not trust the certificate
authority (CA).

If your server is using a certificate that is signed by an official Certificate Authority, then you likely
need to update your client's root certificate store. For example, [Mender Professional](https://mender.io/products/mender-professional?target=_blank)
uses an official CA so the only reason your client would reject this is if it does not have updated root certificates
in its system store.

On the other hand, if you set up the Mender server yourself as described in
[Production installation](../../administration/production-installation) and generated certificates as part of it,
your need to make sure that the server certificates are in `/etc/mender/server.crt` on your device.

To test that they match, run `cat /etc/mender/server.crt` on your device, and compare that to the output
of the following command, adjusting the hostnames mender.example.com / s3.example.com (ideally run on device, but can be run from elsewhere as well):

```
openssl s_client -showcerts -connect mender.example.com:443 < /dev/null 2>/dev/null | openssl x509 && openssl s_client -showcerts -connect s3.example.com:9000 < /dev/null 2>/dev/null | openssl x509
```

If these mismatch, then you need to update `/etc/mender/server.crt` on your client.
You can do this manually for testing purposes, and you should
[include the certificates in your Yocto Project build](../../artifacts/yocto-project/building-for-production#including-the-client-certificates).

## Artifact format not supported

When deploying an update with the Mender client, you see a log message similar to the following:

```
ERRO[0001] update install failed: failed to read and install update: reader: unsupported version: 2  module=state
```

The problem here is most likely that you have built [a new version of the Artifact format](../../architecture/mender-artifacts#versions)
that your Mender Client does not support. It could also be that you are building a very old version of the
Artifact format that your new version of the Mender Client does not support.

In either case the solution is to [build a different version of the Artifact format](../../artifacts/modifying-a-mender-artifact#create-an-artifact-from-a-raw-root-file-system) that your Mender Client supports
until you have upgraded all Mender Clients and can use the corresponding latest version of the Mender Artifact format.



## The partition layout of the device is not as expected

You have the Mender binary on your device and try to trigger a rootfs update but you get output similar to the following:

```bash
mender -install /media/rootfs-image-mydevice.mender

ERRO[0000] exit status 1                                 module=partitions
ERRO[0000] No match between boot and root partitions.    module=main
```

The problem here is most likely that the device does not have the [partition layout Mender expects](../../devices/general-system-requirements#partition-layout). This could have happened if you just placed the Mender binary into your rootfs, but did not [reflash the entire storage device](../../artifacts/provisioning-a-new-device) with the `.sdimg.` file output from the [Yocto Project build](../../artifacts/yocto-project/building). When this happens, output from `mount` and `fw_printenv` can confirm that this is the problem you are seeing. The solution is to flash your entire storage device with the `.sdimg` output from the Yocto Project build process.



## The Mender client uses excessive network traffic even when not deploying updates

If you are using the Mender client in demo mode, either by selecting it when running `mender setup`, or by using one of the [prebuilt Yocto images](../../downloads#disk-images) and set up with the [demo layer](../../artifacts/yocto-project/building#adding-the-meta-layers), the Mender client has more aggressive [polling intervals](../../client-configuration/configuration-file/polling-intervals) to simplify testing.

See the documentation on [building for production](../../artifacts/yocto-project/building-for-production) and [polling intervals](../../client-configuration/configuration-file/polling-intervals) to reduce the network bandwidth usage.
