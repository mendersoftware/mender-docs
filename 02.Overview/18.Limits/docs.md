---
title: Limits
taxonomy:
  category: docs
---

This section gives an overview over important resource limits that help ensure the health and security of the Mender Server.

Many limits vary based on the [Device tier](../17.Device-tiers/docs.md) (standard or micro). Device tiers classify devices by their capabilities and use cases.

### Polling interval: Update checks

The frequency with which a Device checks for updates. This varies by device tier.

| Device Tier | Default Interval            | Configuration                                                                                               |
| ----------- | --------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Micro       | `604800 seconds` (7 days)   | [Mender MCU Client configuration](../../06.Operating-System-updates-Zephyr/04.Customize-Mender-mcu/docs.md) |
| Standard    | `1800 seconds` (30 minutes) | [Mender Client configuration](../../03.Client-installation/07.Configuration/01.Polling-intervals/docs.md)   |

! Warning: On hosted Mender, update checks are rate limited to the default interval. Checking for updates _more frequently_ than
! the default interval is considered _excessive use_ and requests exceeding the limit are throttled. [Test devices](#test-devices)
! are exempt from this rate limiting.

### Polling interval: Inventory updates

The frequency a Device can update its current inventory to the Mender Server. This varies by device tier.

| Device Tier | Default Interval          | Configuration                                                                                               |
| ----------- | ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Micro       | `604800 seconds` (7 days) | [Mender MCU Client configuration](../../06.Operating-System-updates-Zephyr/04.Customize-Mender-mcu/docs.md) |
| Standard    | `28800 seconds` (8 hours) | [Mender Client configuration](../../03.Client-installation/07.Configuration/01.Polling-intervals/docs.md)   |

! Warning: On hosted Mender, inventory updates are rate limited to the default interval. Reporting inventory _more frequently_ than
! the default interval is considered _excessive use_ and requests exceeding the limit are throttled. [Test devices](#test-devices)
! are exempt from this rate limiting.

### Test devices

A _test device_ is an accepted device that is exempt from the normal update check and inventory
poll rate limiting described above, and is allowed to poll for updates and publish inventory
frequently. This is useful when trying out Mender features (for example during a free trial) or
when testing new code as part of a CI/CD system.

See [Test devices](../08.Inventory/docs.md#test-devices) for how to designate, filter and
identify them. Test devices are counted independently of
[Device tier](../17.Device-tiers/docs.md), and are subject to the following limits.

#### Maximum number of test devices

The maximum number of accepted devices with `test_device = true` per tenant.

Default: `10`</br>
Overriding this limit is not possible

Once 10 devices with `test_device = true` are accepted into a tenant, no additional device can
be designated as a test device. The UI shows an error message, with a link to the current test
devices, if this is attempted.

#### Maximum test device changes per day

The maximum number of `test_device` changes per tenant, per day. Both designating a device as a
test device and removing that designation count towards this limit.

Default: `20`</br>
Overriding this limit is not possible

### Artifact size limits

| Tier     | Default Maximum Artifact Size | Notes                                                             |
| -------- | ----------------------------- | ----------------------------------------------------------------- |
| Micro    | 5 MiB                         | Configurable via `DEPLOYMENTS_MAX_DEPLOYMENT_ARTIFACT_SIZE_MICRO` |
| Standard | 10 GiB                        | Configurable via `DEPLOYMENTS_STORAGE_MAX_IMAGE_SIZE`             |

### Maximum number of download retries

The maximum number of times that mender-update retries continuing a download of an Artifact
that was interrupted e.g. by network issues.

Default: `10`</br>
Minimum: `1`</br>
Maximum: `10,000`

This is a Client side configuration, see [Mender Client configuration](../../03.Client-installation/07.Configuration/01.Polling-intervals/docs.md).

### Maximum size of API payload

The maximum size of API payload for all API calls unless otherwise specified affects POST API calls. If a deployment log is over this limit, it can fail to upload the log.

Default: `1 MiB`</br>
Override per service with the Mender Server environment variable: `service_REQUEST_SIZE_LIMIT` e.g. `DEPLOYMENTS_REQUEST_SIZE_LIMIT`

### Maximum size of single file uploads

The maximum size of single-file type Artifacts generated by the Mender Server with the [Generate Artifact endpoint](https://docs.mender.io/api/#management-api-deployments-generate-artifact).

Default: `256 MiB`</br>
Override with the Mender Server environment variable: `DEPLOYMENTS_STORAGE_MAX_GENERATE_DATA_SIZE`

### Maximum total size of Device inventory data store

The maximum size of a single Device inventory on the Mender Server is determined by the API upload limit

Default: `1 MiB`</br>
Overriding is done by INVENTORY_REQUEST_SIZE_LIMIT up to 10MB, which is the database limit.

### Maximum length of Deployment names

Default: `256 characters`</br>
Overriding this limit is not possible

### Maximum length of Device Group names

Default: `256 characters`</br>
Overriding this limit is not possible

### Maximum length of RBAC role names

Default: `256 characters`</br>
Overriding this limit is not possible

### Maximum length of Release names

Default: `256 characters`</br>
Overriding this limit is not possible

### Maximum length of Email addresses

Default: `256 characters`</br>
Overriding this limit is not possible

### Maximum length of Passwords

Default: `256 characters`</br>
Overriding this limit is not possible

### Maximum length of Organization names

Default: `256 characters`</br>
Overriding this limit is not possible

### Maximum length of Mender Configure strings

The maximum length of keys and values in Mender Configure Device attributes.

Default: `4096 characters`</br>
Overriding this limit is not possible

### Maximum number of active deployments

The maximum number of active and pending deployments per tenant.

Default: `No limit`</br>
Override with the Mender Server environment variable: `DEPLOYMENTS_LIMIT_MAX_ACTIVE_DEPLOYMENTS`

! Warning: This limit is set to **800** active deployments per tenant on hosted Mender.

### Maximum number of tags per Device

The maximum number of tags that can be defined per Device inventory.

Default: `20`</br>
Override with the Mender Server environment variable: `INVENTORY_LIMIT_TAGS`

### Maximum size of server-side delta Artifact

The maximum uncompressed size of the root file system in Mender Artifacts that you can use to trigger server-side binary delta generation.

Default: `5 GiB`</br>
Override with the Mender Server environment variable: `DEPLOYMENTS_SERVER_SIDE_DELTA_GENERATION_MAX_ARTIFACT_SIZE_MB`
Note that the environment variable is represented in **MiB**, and its default value is `5120`.

### Audit log retention

The duration from when an event happened until the [audit log](../20.Audit-logs/docs.md) is removed from the server.

Default: `365 days`</br>
Override with helm value `auditlogs.logRetentionSeconds`.
Note that the value is specified in seconds (365 days is 31536000 seconds).

### Maximum number of RBAC permission sets per Role

The maximum number of permission sets (e.g., User Management, Releases, Device Group Management) that can be assigned to a custom Role on the Mender Server.

Default: `15`</br>
Override with the Mender Server environment variable: `USERADM_LIMIT_PERMISSION_SETS_PER_ROLE`
