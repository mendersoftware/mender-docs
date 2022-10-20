---
title: Network Requirements
taxonomy:
    category: docs
---

## Working with Firewalls

Corporate Firewalls must permit the following URLs to the devices and for letting Hosted Mender works correctly:

**Hosted Mender access**: Devices, APIs and browser access
* `hosted.mender.io`
* `*.hosted.mender.io`
* `eu.hosted.mender.io`
* `*.eu.hosted.mender.io`

**Artifact storage access**: Devices, APIs and browser access
* `https://s3.amazonaws.com/hosted-mender-artifacts` - Amazon S3 Path-style request
* `https://s3.amazonaws.com/hosted-mender-artifacts-eu` - Amazon S3 Path-style request
* `https://hosted-mender-artifacts.s3.amazonaws.com` - Amazon S3 Virtual-hosted-style request
* `https://hosted-mender-artifacts-eu.s3.amazonaws.com` - Amazon S3 Virtual-hosted-style request
