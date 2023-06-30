---
title: Requirements
taxonomy:
    category: docs
---

## Working with Firewalls
The following URLs and access types need outgoing permissions in firewalls in order for Hosted Mender to work correctly:

**Mender access**: Devices, APIs and browser access
* `https://mender.example.com` - Use the same address you specify it in the [Server Installation Section](../../07.Server-installation/)

**Artifact storage access**: Devices, APIs and browser access

[ui-tabs position="top-left" active="0" theme="default" ]
[ui-tab title="Amazon S3"]
Permit access to the following URLs:
* `https://s3.amazonaws.com/<my-example-artifact-storage>` - Amazon S3 Path-style request
* `https://<my-example-artifact-storage>.s3.amazonaws.com` - Amazon S3 Virtual-hosted-style request
[/ui-tab]
[ui-tab title="Minio"]
Permit access to your 
Minio URL defined in [Minio Setup Section](../../07.Server-installation/04.Production-installation-with-kubernetes/02.Minio/docs.md)
* `https://artifacts.example.com`
[/ui-tab]
[/ui-tabs]


## Amazon S3 IAM policies
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
