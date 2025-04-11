---
title: Requirements
taxonomy:
    category: docs
---

## Working with Firewalls
The following URLs and access types need outgoing permissions in firewalls in order for Mender to work correctly:

[ui-tabs position="top-left" active="0" theme="default" ]
[ui-tab title="Hosted Mender US"]

**Hosted Mender access**: Devices, APIs and browser access
* `https://hosted.mender.io`
* `https://*.hosted.mender.io`

**Artifact storage access**: Devices, APIs and browser access
* `https://s3.amazonaws.com/hosted-mender-artifacts`
* `https://hosted-mender-artifacts.s3.amazonaws.com`
* `https://c271964d41749feb10da762816c952ee.r2.cloudflarestorage.com`

[/ui-tab]
[ui-tab title="Hosted Mender EU"]

**Hosted Mender access**: Devices, APIs and browser access
* `https://eu.hosted.mender.io`
* `https://*.eu.hosted.mender.io`

**Artifact storage access**: Devices, APIs and browser access
* `https://mender.blob.core.windows.net/artifacts`
* `https://c271964d41749feb10da762816c952ee.r2.cloudflarestorage.com`

[/ui-tab]
[ui-tab title="on-premise installation"]

**Mender access**: Devices, APIs and browser access
* `https://mender.example.com` - Use the same address you specify it in the [Server Installation Section](../../08.Server-installation/)

**Artifact storage access**: Devices, APIs and browser access

[ui-tabs position="top-left" active="0" theme="default" ]
[ui-tab title="Amazon S3"]
Permit access to the following URLs:
* `https://s3.amazonaws.com/<my-example-artifact-storage>` - Amazon S3 Path-style request
* `https://<my-example-artifact-storage>.s3.amazonaws.com` - Amazon S3 Virtual-hosted-style request
[/ui-tab]
[ui-tab title="Storage Proxy"]
Permit access to your 
Storage proxy URL defined in [Storage Setup Section](../../08.Server-installation/04.Production-installation-with-kubernetes/02.Storage/docs.md)
* `https://artifacts.example.com` or simply:
* `https://mender.example.com`
[/ui-tab]
[/ui-tabs]

[/ui-tab]
[/ui-tabs]


## Amazon S3 IAM policies

!!! Only required for on-premise installation

A minimum policy set to use an Amazon S3 bucket to store Mender Artifacts is:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "s3:GetAccessPoint",
                "s3:ListAllMyBuckets"
            ],
            "Effect": "Allow",
            "Resource": "*"
        },
        {
            "Action": [
                "s3:*"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::BUCKET-NAME"
        },
        {
            "Action": [
                "s3:*"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::BUCKET-NAME/*"
        },
    ]
}
```

## Root CAs used in hosted Mender

The following are the Root Certificate Authorities (CAs) that currently trust
the certificates of hosted Mender servers:

[ui-tabs position="top-left" active="0" theme="default" ]
[ui-tab title="Hosted Mender US"]

**Hosted Mender access**: Devices, APIs and browser access
* `https://hosted.mender.io`
  * Root CA: Amazon Root CA 1 - [provider's information](https://www.amazontrust.com/repository/) - [PEM](AmazonRootCA1.pem) - [DER](AmazonRootCA1.cer) - [sha256](AmazonRootCA1.sha256)
  * Not Before: `May 25 12:00:00 2015 GMT`
  * Not After: `Dec 31 01:00:00 2037 GMT`

**Artifact storage access**: Devices, APIs and browser access
* `https://s3.amazonaws.com/hosted-mender-artifacts`
  * Root CA: Amazon Root CA 1 - [provider's information](https://www.amazontrust.com/repository/) - [PEM](AmazonRootCA1.pem) - [DER](AmazonRootCA1.cer) - [sha256](AmazonRootCA1.sha256)
  * Not Before: `May 25 12:00:00 2015 GMT`
  * Not After: `Dec 31 01:00:00 2037 GMT`
* `https://hosted-mender-artifacts.s3.amazonaws.com`
  * Root CA: Amazon Root CA 1 - [provider's information](https://www.amazontrust.com/repository/) - [PEM](AmazonRootCA1.pem) - [DER](AmazonRootCA1.cer) - [sha256](AmazonRootCA1.sha256)
  * Not Before: `May 25 12:00:00 2015 GMT`
  * Not After: `Dec 31 01:00:00 2037 GMT`
* `https://c271964d41749feb10da762816c952ee.r2.cloudflarestorage.com`
  * Root CA: GTS Root R4 - [provider's information](https://pki.goog/repository/) - [PEM](r4.pem) - [DER](r4.crt) - [sha256](r4.sha256)
  * Not Before: `Jun 22 00:00:00 2016 GMT`
  * Not After: `Jun 22 23:59:59 2036 GMT`


[/ui-tab]
[ui-tab title="Hosted Mender EU"]

**Hosted Mender access**: Devices, APIs and browser access
* `https://eu.hosted.mender.io`
  * Root CA: ISRG Root X1 - [provider's information](https://letsencrypt.org/certificates/) - [PEM](isrgrootx1.pem) - [DER](isrgrootx1.der) - [sha256](isrgrootx1.sha256)
  * Not Before: `Jun 04 00:00:00 2015 GMT`
  * Not After : `Jun 04 23:59:59 2035 GMT`


**Artifact storage access**: Devices, APIs and browser access
* `https://mender.blob.core.windows.net/artifacts`
  * Root CA: DigiCert Global Root G2 - [provider's information](https://www.digicert.com/kb/digicert-root-certificates.htm) - [PEM](DigiCertGlobalRootG2.crt.pem) - [DER](DigiCertGlobalRootG2.crt) - [sha256](DigiCertGlobalRootG2.sha256)
  * Not Before: `Aug 01 00:00:00 2013 GMT`
  * Not After : `Jan 15 23:59:59 2038 GMT`

* `https://c271964d41749feb10da762816c952ee.r2.cloudflarestorage.com`
  * Root CA: GTS Root R4 - [provider's information](https://pki.goog/repository/) - [PEM](r4.pem) - [DER](r4.crt) - [sha256](r4.sha256)
  * Not Before: `Jun 22 00:00:00 2016 GMT`
  * Not After: `Jun 22 23:59:59 2036 GMT`

[/ui-tab]
[/ui-tabs]

! Warning: The CA Chains are subject to change from the provider without notice
! for security reasons (renewal, revokation). Please ensure that your devices
! are able to update their Root CA store.  

!! We don't recommend pinning the Root CA in your devices.  

!!!! We do recommend using the Root CA store of the device's OS and keeping it up-to-date.

