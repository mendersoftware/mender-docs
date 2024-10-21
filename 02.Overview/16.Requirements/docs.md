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
* `https://mender.example.com` - Use the same address you specify it in the [Server Installation Section](../../07.Server-installation/)

**Artifact storage access**: Devices, APIs and browser access

[ui-tabs position="top-left" active="0" theme="default" ]
[ui-tab title="Amazon S3"]
Permit access to the following URLs:
* `https://s3.amazonaws.com/<my-example-artifact-storage>` - Amazon S3 Path-style request
* `https://<my-example-artifact-storage>.s3.amazonaws.com` - Amazon S3 Virtual-hosted-style request
[/ui-tab]
[ui-tab title="Storage Proxy"]
Permit access to your 
Storage proxy URL defined in [Storage Setup Section](../../07.Server-installation/04.Production-installation-with-kubernetes/02.Storage/docs.md)
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
