---
title: Miscellaneous
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
Minio URL defined in [Minio Setup Section](../../07.Server-installation/04.Production-installation-with-kubernetes/04.Minio/docs.md)
* `https://artifacts.example.com`
[/ui-tab]
[/ui-tabs]


## Device license count

!!!!! Device License Count is only available in Mender Enterprise.
!!!!! Ignore this section if you are running Mender Open Source.

The Device Authentication service gathers data about devices. It also provides a command
to count the number of accepted devices and store it as licensing data: `license-count`.

```shell
# deviceauth-enterprise license-count --help
NAME:
   deviceauth-enterprise license-count - Count licenses and store the results

USAGE:
   deviceauth-enterprise license-count [arguments...]

DESCRIPTION:
   Counts the devices licenses and stores the result for later processing.
```

Its purpose is to ensure your installation is appropriately licensed and verify device counts.
It saves the device count daily for future inspection and otherwise does not influence the operations of the Mender Server in any way.

You can download the device count and licenses report from the Mender UI in the Organization view by clicking on the link "Download license report".

If you are using the Helm chart installation, the cronjob is already prepared and will be running daily <!--AUTOVERSION: "at [3am](https://github.com/mendersoftware/mender-helm/blob/%/mender/templates/device-auth-cron-license-count.yaml)."/ignore-->
at [3am](https://github.com/mendersoftware/mender-helm/blob/master/mender/templates/device-auth-cron-license-count.yaml).
