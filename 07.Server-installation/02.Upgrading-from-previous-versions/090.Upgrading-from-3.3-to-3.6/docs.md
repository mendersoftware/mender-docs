---
title: Upgrading to Mender 3.6
taxonomy:
category: docs
label: tutorial
---

This is a tutorial for upgrading the Mender Server from version 3.3 and 3.4 to
3.6 in production environments. There are no particular steps you should take,
other than take a backup and run the new version, however there are things to
look out for.

Besides the version specific guidelines below, please make sure you're following
the [suggested upgrade best practices](../docs.md) to reduce the risk of
unpredictable downtime and data loss.

## Before you start

### Current version

Be sure that your current version is either 3.3 or 3.4 and that it works, and Mender Server starts properly.

### Upgrade MongoDB to 5.0 (optional)

We recommend upgrading your MongoDB deployment from 4.4 to 5.0. Please refer to
the [official
documentation](https://www.mongodb.com/docs/manual/release-notes/5.0-upgrade-replica-set/)
for conducting the upgrade. Mender 3.3, 3.4 and 3.6 are all compatible with both
MongoDB 4.4 and 5.0.

## Migrating from 3.3

### Helm chart major upgrade

The helm chart is versioned separately from the Mender releases.
<!--AUTOVERSION: "Mender %"/ignore "blob/%"/ignore-->
During the lifetime of Mender 3.4.0, the helm chart got a major version increase with a [breaking change](https://github.com/mendersoftware/mender-helm/blob/5.0.0/mender/CHANGELOG.md#version-500).

<!--AUTOVERSION: "mendersoftware/mender	%        	%"/ignore-->
```
helm search repo mendersoftware/mender --versions

# Output
# NAME                 	CHART VERSION	APP VERSION	DESCRIPTION                                       
# mendersoftware/mender	5.3.0        	3.6.3      	Mender is a robust and secure way to update all...
# ...
# mendersoftware/mender	5.0.0        	3.4.0      	Mender is a robust and secure way to update all...
# mendersoftware/mender	4.0.3        	3.4.0      	Mender is a robust and secure way to update all...
# ...
```

<!--AUTOVERSION: "blob/%"/ignore-->
If you're not updating the helm chart changes you might stumble onto this when doing the 3.3 -> 3.6 upgrade. To fix this issue please adjust your redis configuration to the [new format](https://github.com/mendersoftware/mender-helm/blob/5.3.0/mender/values.yaml).

Redis is now configured as a global service which needs to be configured.

```
  redis:
    username: null
    password: null
    URL: ""
```

!! We strongly recommend using an external redis service provider. 
<!--AUTOVERSION: "blob/%"/ignore-->
!! As a reference, we provide redis as a dependency through a [subchart](https://github.com/mendersoftware/mender-helm/blob/5.3.0/mender/Chart.yaml#L19).
!! We do not provide support for troubleshooting issues related to problems with an internally deployed redis instance.


The service specific redis credentials which were used before the helm chart version 5 need to be removed:

```
DEVICEAUTH_REDIS_ADDR: "mender-redis:6379"
DEVICEAUTH_REDIS_USERNAME: ""
DEVICEAUTH_REDIS_PASSWORD

USERADM_REDIS_ADDR: "mender-redis:6379"
USERADM_REDIS_USERNAME: ""
USERADM_REDIS_PASSWORD: ""
```


### useradm database

Be sure that `useradm` database is clean. Especially look out for leftovers from previous
(possible single tenant installations). They can make database migrations to fail.

## Maintenance window

Be prepared for the maintenance window of approximately 15 minutes. This is the maximal
estimated migration time, as seen in the biggest databases we are dealing with.

