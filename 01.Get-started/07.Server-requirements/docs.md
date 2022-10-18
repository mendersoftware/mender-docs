---
title: Requirements
taxonomy:
    category: docs
---

Mender general requirements

## Requirements

### URL Allowlist
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


## Have any questions?

If you need help or have any questions:

* Visit our community forum at [Mender Hub](https://hub.mender.io?target=_blank),
dedicated to OTA updates where you can discuss any issues you may be having.
Share and learn from other Mender users.

* Learn more about Mender by reading the rest of the documentation, for example
the [Overview](../../02.Overview/01.Introduction/docs.md),
[Troubleshoot](../../301.Troubleshoot/) or
[Mender FAQ](https://mender.io/product/faq?target=_blank) sections.
