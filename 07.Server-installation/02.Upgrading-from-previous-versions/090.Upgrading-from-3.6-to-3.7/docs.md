---
title: Upgrading to Mender 3.7
taxonomy:
category: docs
label: tutorial
---

This is a tutorial for upgrading the Mender Server from version 3.6 to
3.7 in production environments. There are no particular steps you should take,
other than take a backup and run the new version, however there are things to
look out for.

Besides the version specific guidelines below, please make sure you're following
the [suggested upgrade best practices](../docs.md) to reduce the risk of
unpredictable downtime and data loss.

## Before you start

### Current version

Be sure that your current version is 3.6 and that it works, and Mender Server starts properly.

### Upgrade MongoDB to 5.0

If you haven't already done so, upgrade your MongoDB deployment from 4.4 to 5.0.
Please refer to the [official documentation](https://www.mongodb.com/docs/manual/release-notes/5.0-upgrade-replica-set/)
for guidance on conducting the upgrade. Mender 3.3, 3.4 and 3.6 are all compatible with both
MongoDB 4.4 and 5.0.

## Migrating from 3.6
The helm chart is versioned separately from the Mender releases.

<!--AUTOVERSION: "Until the helm chart version %"/ignore -->
Until the helm chart version 5.5.x, the chart is compatible with both Mender 3.6 and 3.7.
You should be aware of a few deprecation, though:

<!--AUTOVERSION: "### Helm Chart v% deprecations:"/ignore -->
### Helm Chart v5.4.0 deprecations:
<!--AUTOVERSION: "`global.redis.username` and `global.redis.password` are deprecated in Mender %."/ignore -->
* `global.redis.username` and `global.redis.password` are deprecated in Mender 3.7.0.
    Use redis connection string format in the `global.redis.URL`:
    * Standalone mode:
    ```
    (redis|rediss|unix)://[<user>:<password>@](<host>|<socket path>)[:<port>[/<db_number>]][?option=value]
    ```
    * Cluster mode:
    ```
    (redis|rediss|unix)[+srv]://[<user>:<password>@]<host1>[,<host2>[,...]][:<port>][?option=value]
    ```
* `device_auth.env.DEVICEAUTH_REDIS_DB`: use the new redis connection string format instead.
* `device_auth.env.DEVICEAUTH_REDIS_TIMEOUT_SEC`: use the new redis connection string format instead.
* `device_auth.env.USERADM_REDIS_DB`: use the new redis connection string format instead.
* `device_auth.env.USERADM_REDIS_TIMEOUT_SEC`: use the new redis connection string format instead.

<!--AUTOVERSION: "### Helm Chart v% deprecations:"/ignore -->
### Helm Chart v5.5.0 deprecations:
* `api_gateway.minio` is deprecated in favor of `api_gateway.storage_proxy`.
    This entry could be used, but it is no longer maintained, and could be removed
    in future releases.
    **How to upgrade**:
  * set `api_gateway.minio.enabled=false`
  * set `api_gateway.storage_proxy.enabled=true`
  * set `api_gateway.storage_proxy.url` to the external storage url that you want to map externally.
    For example `https://fleetstorage.example.com`.
    If you leave it empty, it uses the Amazon S3 external URL.


## Maintenance window

Be prepared for the maintenance window of approximately 15 minutes. This is the maximal
estimated migration time, as seen in the biggest databases we are dealing with.

## Troubleshooting
The `workflows-worker` and the `create-artifact-worker` are crashing with this error log:
```
failed to apply Jetstream consumer migrations: context deadline exceeded
```

* Double check the NATS url, if you are using an external NATS instance: `global.nats.URL`
  or `global.nats.existingSecret`
* Verify that both `create_artifac_worker.automigrate` and `workflows.automigrate` are set to `false`
