---
title: Enabling device license count
taxonomy:
    category: docs
    label: tutorial
---

!!!!! Device License Count is only available in Mender Enterprise.
!!!!! Ignore this section if you are running Mender Open Source.

To enable the [device license count](../../07.Device-license-count/docs.md) in your cluster,
you must schedule a cronjob to run the device-count command daily. If you are using the Helm chart
installation, the cronjob is already prepared and will be running daily
<!--AUTOVERSION: "at [3am](https://github.com/mendersoftware/mender-helm/blob/%/mender/templates/device-auth-cron-license-count.yaml)."/ignore-->
at [3am](https://github.com/mendersoftware/mender-helm/blob/master/mender/templates/device-auth-cron-license-count.yaml).

Similarly, if you are running Mender without the Helm chart, you must configure
and apply the cronjob manifest
<!--AUTOVERSION: "using [device-auth-cron-license-count.yaml](https://github.com/mendersoftware/mender-helm/blob/%/mender/templates/device-auth-cron-license-count.yaml)"/ignore-->
using [device-auth-cron-license-count.yaml](https://github.com/mendersoftware/mender-helm/blob/master/mender/templates/device-auth-cron-license-count.yaml)
as a reference.
