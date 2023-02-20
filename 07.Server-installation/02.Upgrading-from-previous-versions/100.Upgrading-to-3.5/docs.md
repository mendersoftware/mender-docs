---
title: Upgrading to 3.5
taxonomy:
category: docs
label: tutorial
---

This is a tutorial for upgrading the Mender Server to version 3.5 in production environments.
With the 3.5 we introduced a new element at the heart of ths system:
the so-called _reporting_ service, which came with [OpenSearch](https://opensearch.org/).
This brings an additional upgrade complication, and needs some attention.

## Before you start

### Enough disc space

Be sure to have at least `6%` free disc space, on the volume where `OpenSearch` runs.
The _disc threshold monitor_ will check this value, and in case there is more than `95%`
space used it will report errors:

```shell
[2023-02-20T16:23:14,185][WARN ][o.o.c.r.a.DiskThresholdMonitor] [4c17a7eaeccf] flood stage disk watermark [95%] exceeded on [HFJTQ-0vT0iXlgR7_n9Tuw][4c17a7eaeccf][/usr/share/opensearch/data/nodes/0] free: 21.6gb[4.8%], all indices on this node will be marked read-only
```

Where we assume the default settings. It will manifest itself with the UI reporting errors like:

```
undefined devices couldn't be loaded. Request failed with status code 503
```

### vm.max_map_count

Be sure that you possess enough `vm.max_map_count`. You need at least `262144`, and you can
change it via:

```shell
sysctl -w vm.max_map_count=262144
```

Lack in the above can result in the following log line from opensearch:

```shell
[1]: max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]
ERROR: OpenSearch did not exit normally - check the logs at /usr/share/opensearch/logs/opensearch-cluster.log
```

If that happens, free some space and restart your setup.

### Database backup

Be sure to have a fresh and working backup of your database. The perfect solution
is to have a testing environment setup where you can restore the backup, and see that
everything is in order, and try the upgrade.

### Access to all the images

Remember that during the upgrade process your orchestrator will try to download images.
Be sure that you have access to them.

## Run 3.5

Once ready, you can start the new version, and as soon as the services are healthy
and alive you can proceed to the next step: propagation of devices and deployments.

### Propagate devices

For convenience, we provide a command line tool to perform the re-indexing of all your devices.
The following table presents example usage:

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="kubernetes"]
<!--AUTOMATION: ignore -->
    # kubectl exec -it `kubectl get pods --selector=run=mender-device-auth | tail -1` -- /usr/bin/deviceauth-enterprise propagate-reporting
    INFO[2023-02-20T16:53:04Z] propagating inventory for all tenants         file=commands.go func=cmd.selectDbs line=290
    INFO[2023-02-20T16:53:04Z] propagating device data to reporting from DB: deviceauth-63f3a22bc27bbe79cfbe320a  file=commands.go func=cmd.tryPropagateReportingForDb line=497
    INFO[2023-02-20T16:53:04Z] Done with DB deviceauth-63f3a22bc27bbe79cfbe320a  file=commands.go func=cmd.tryPropagateReportingForDb line=512
    INFO[2023-02-20T16:53:04Z] all DBs processed, exiting.                   file=commands.go func=cmd.PropagateReporting line=276
[/ui-tab]
[ui-tab title="docker-compose"]
<!--AUTOMATION: ignore -->
    # docker exec -it integrationupgrade_mender-device-auth_1 /usr/bin/deviceauth-enterprise propagate-reporting
    INFO[2023-02-20T16:53:04Z] propagating inventory for all tenants         file=commands.go func=cmd.selectDbs line=290
    INFO[2023-02-20T16:53:04Z] propagating device data to reporting from DB: deviceauth-63f3a22bc27bbe79cfbe320a  file=commands.go func=cmd.tryPropagateReportingForDb line=497
    INFO[2023-02-20T16:53:04Z] Done with DB deviceauth-63f3a22bc27bbe79cfbe320a  file=commands.go func=cmd.tryPropagateReportingForDb line=512
    INFO[2023-02-20T16:53:04Z] all DBs processed, exiting.                   file=commands.go func=cmd.PropagateReporting line=276
[/ui-tab]
[/ui-tabs]

### Propagate deployments

You have to migrate deployments, in a similar way to devices, using the following command line
tool:

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="kubernetes"]
<!--AUTOMATION: ignore -->
```
# kubectl exec -it $(kubectl get pods --selector=run=mender-deployments | tail -1) -- /usr/bin/deployments-enterprise propagate-reporting
WARN[2023-02-20T16:55:39Z] 'presign.secret' not configured. Generating a random secret.  file=config.go func=config.Setup line=237
INFO[2023-02-20T16:55:39Z] propagating deployments history for all tenants  file=main.go func=main.selectDbs line=253
INFO[2023-02-20T16:55:39Z] propagating deployments data to reporting from DB: deployment_service-63f3a22bc27bbe79cfbe320a  file=main.go func=main.tryPropagateReportingForDb line=280
INFO[2023-02-20T16:55:39Z] Done with DB deployment_service-63f3a22bc27bbe79cfbe320a  file=main.go func=main.tryPropagateReportingForDb line=295
INFO[2023-02-20T16:55:39Z] all DBs processed, exiting.                   file=main.go func=main.propagateReporting line=239
```
[/ui-tab]
[ui-tab title="docker-compose"]
<!--AUTOMATION: ignore -->
```
# docker exec -it integrationupgrade_mender-deployments_1 /usr/bin/deployments-enterprise propagate-reporting
WARN[2023-02-20T16:55:39Z] 'presign.secret' not configured. Generating a random secret.  file=config.go func=config.Setup line=237
INFO[2023-02-20T16:55:39Z] propagating deployments history for all tenants  file=main.go func=main.selectDbs line=253
INFO[2023-02-20T16:55:39Z] propagating deployments data to reporting from DB: deployment_service-63f3a22bc27bbe79cfbe320a  file=main.go func=main.tryPropagateReportingForDb line=280
INFO[2023-02-20T16:55:39Z] Done with DB deployment_service-63f3a22bc27bbe79cfbe320a  file=main.go func=main.tryPropagateReportingForDb line=295
INFO[2023-02-20T16:55:39Z] all DBs processed, exiting.                   file=main.go func=main.propagateReporting line=239
```
[/ui-tab]
[/ui-tabs]

## Troubleshooting

### Environment variables

We enable the reporting service in three places: deployments, gui, deviceauth.
In case you run into problems, you can check the following:

* deployments service `DEPLOYMENTS_REPORTING_ADDR` environment variable.
 It should be similar to the default: `http://mender-reporting:8080`
* gui setting `HAVE_REPORTING=1` should be set to `1`, unless you explicitly
 want it otherwise.
* deviceauth `DEVICEAUTH_ENABLE_REPORTING=1` environment variable 
 should be set to `1`, unless you explicitly want it otherwise.

### Required components

With 3.5 we brought two additional components, which result in three
new items in the Mender stack: two for reporting, and one for opensearch.

You should see the following up and running:


[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="kubernetes"]
<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "opensearch-cluster-%"/ignore-->
```
# kubectl get pods -l 'app.kubernetes.io/name in (reporting,opensearch)'
opensearch-cluster-master-0   1/1     Running   0          66m
opensearch-cluster-master-1   1/1     Running   0          66m
opensearch-cluster-master-2   1/1     Running   0          66m
reporting-5c4bb89dd7-tzs52    1/1     Running   0          5m32s
```
[/ui-tab]
[ui-tab title="docker-compose"]
<!--AUTOMATION: ignore -->
<!--AUTOVERSION: "mendersoftware/reporting:mender-%"/ignore "mendersoftware/reporting:mender-%"/ignore "opensearchproject/opensearch:%"/ignore-->
```
# docker ps --format '{{.Image}}' | grep -e report -e search
mendersoftware/reporting:mender-3.5.x
mendersoftware/reporting:mender-3.5.x
opensearchproject/opensearch:2.4.0
```
[/ui-tab]
[/ui-tabs]

## Final steps

After the propagation of deployments and devices you should be good to go.
Give the UI a full refresh without cache, and verify that everything is in place.
