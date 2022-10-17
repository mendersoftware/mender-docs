---
title: Requirements
taxonomy:
    category: docs
---

Mender general requirements

## Requirements

### URL Allowlist
Corporate Firewalls must permit the following URLs to the devices and for letting Mender works correctly:

**Mender access**: Devices, APIs and browser access
* `mender.example.com` - It's the same address you specify it in the [Server Installation Section](../../07.Server-installation/)

**Artifact storage access**: Devices, APIs and browser access

[ui-tabs position="top-left" active="0" theme="default" ]
[ui-tab title="Amazon S3"]
If you use Amazon S3 for storing artifacts, you have to permit access to the following URLs:
* `https://s3.amazonaws.com/<my-example-artifact-storage>` - Amazon S3 Path-style request
* `https://<my-example-artifact-storage>.s3.amazonaws.com` - Amazon S3 Virtual-hosted-style request
[/ui-tab]
[ui-tab title="Minio"]
If you use Minio for storing artifacts, you have to permit access to your 
Minio URL defined in [Minio Setup Section](../../07.Server-installation/04.Production-installation-with-kubernetes/04.Minio/docs.md)
* `https://artifacts.example.com`
[/ui-tab]
[/ui-tabs]

