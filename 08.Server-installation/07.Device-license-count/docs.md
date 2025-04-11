---
title: Device license count
taxonomy:
    category: docs
    label: tutorial
---

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

It saves the device count daily for future inspection and otherwise does not influence the operations of the Mender Server in any way.

For production installations with Kubernetes, the cronjob is already prepared and will be running daily
<!--AUTOVERSION: "at [3am](https://github.com/mendersoftware/mender-helm/blob/%/mender/templates/device-auth-cron-license-count.yaml)."/ignore-->
at [3am](https://github.com/mendersoftware/mender-helm/blob/master/mender/templates/device-auth-cron-license-count.yaml).

You can download the device count and licenses report from the Mender UI in the Organization view by clicking on the link "Download license report".
