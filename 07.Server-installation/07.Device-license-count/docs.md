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

Its purpose is to ensure your installation is appropriately licensed and verify device counts.
A cronjob usually runs the command
in the [kubernetes cluster](../04.Production-installation-with-kubernetes/06.Enabling-device-license-count/docs.md),
or [docker composition](../03.Installation-with-docker-compose/04.Enabling-device-license-count/docs.md).
It saves the device count daily for future inspection and otherwise does not influence the operations of the Mender Server in any way.

You can download the device count and licenses report from the Mender UI in the Organization view by clicking on the link "Download license report".
