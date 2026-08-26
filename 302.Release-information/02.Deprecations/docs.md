---
title: Deprecations
taxonomy:
    category: docs
---

This document lists currently deprecated Mender APIs and features, along with their
end-of-life (EOL) dates and recommended replacements. For the deprecation process,
timelines, and grace periods, see the
[Deprecation policy](../../02.Overview/15.Compatibility-policy/docs.md#deprecation-policy-server-api).
For component versions and platform support status, see
[Supported releases](../01.Supported-releases/docs.md).


## Deprecated APIs

The endpoints below are marked as deprecated in the
[Mender Server API specification](https://docs.mender.io/api?target=_blank).
Paths are relative to the API root, i.e. `/api/management/<version>`, so
`/deployments/deployments` in the *Management v1* row is
`/api/management/v1/deployments/deployments`.

| API | Version | Deprecated since | EOL (hosted Mender) | EOL (on-premise) | Replacement |
|-----|---------|------------------|---------------------|------------------|-------------|
| `GET /deployments/artifacts` | Management v1 | 2021-10-18 | 2027-08-25 | 2027-08-25 | `GET /api/management/v2/deployments/artifacts`. The originally announced replacement, v1 `/deployments/artifacts/list`, is itself deprecated |
| `GET /deployments/artifacts/list` | Management v1 | 2025-07-22 | 2027-08-25 | 2027-08-25 | `GET /api/management/v2/deployments/artifacts`, which supports exact and prefix matching on the various fields |
| `GET /deployments/deployments` | Management v1 | 2024-10-21 | 2027-08-25 | 2027-08-25 | `GET /api/management/v2/deployments/deployments`, where the `search` parameter is replaced by `id` and `name` |
| `GET /deployments/deployments/releases` | Management v1 | 2021-05-19 | 2027-08-25 | 2027-08-25 | `GET /api/management/v2/deployments/deployments/releases`. The originally announced replacement, v1 `/deployments/releases/list`, is itself deprecated |
| `GET /deployments/deployments/releases/list` | Management v1 | 2023-09-24 | 2027-08-25 | 2027-08-25 | `GET /api/management/v2/deployments/deployments/releases`, which uses consistent field capitalization and supports advanced filters and sorting |
| `GET /deployments/deployments/{deployment_id}/devices` | Management v1 | 2021-05-19 | 2027-08-25 | 2027-08-25 | `GET /api/management/v1/deployments/deployments/{deployment_id}/devices/list`, which supports pagination |
| `GET /devauth/limits/{name}` | Management v2 | 2025-10-21 | 2027-08-25 | 2027-08-25 | `GET /api/management/v2/devauth/limits/devices`, following a change in how device limits work |
| `GET /tenantadm/user/tenant` | Management v1 | 2026-08-21 | 2027-08-25 | 2027-08-25 | `GET /api/management/v2/tenantadm/tenants/me`. The v2 response omits `tenant_token`; get it from `GET /api/management/v2/tenantadm/tenants/me/token`, which is restricted to Admin users and users who can manage all devices |
| `GET /useradm/roles` | Management v1 | 2022-03-15 | 2027-08-25 | 2027-08-25 | `GET /api/management/v2/useradm/roles` together with `GET /api/management/v2/useradm/permission_sets` |
| `POST /useradm/roles` | Management v1 | 2022-03-15 | 2027-08-25 | 2027-08-25 | `POST /api/management/v2/useradm/roles` together with `GET /api/management/v2/useradm/permission_sets` |
| `GET /useradm/roles/{id}` | Management v1 | 2022-03-15 | 2027-08-25 | 2027-08-25 | `GET /api/management/v2/useradm/roles/{id}` together with `GET /api/management/v2/useradm/permission_sets/{id}` |
| `PUT /useradm/roles/{id}` | Management v1 | 2022-03-15 | 2027-08-25 | 2027-08-25 | `PUT /api/management/v2/useradm/roles/{id}` together with `GET /api/management/v2/useradm/permission_sets/{id}` |
| `DELETE /useradm/roles/{id}` | Management v1 | 2022-03-15 | 2027-08-25 | 2027-08-25 | `DELETE /api/management/v2/useradm/roles/{id}` together with `GET /api/management/v2/useradm/permission_sets/{id}` |
| `POST /useradm/users` | Management v1 | 2026-08-21 | 2027-08-25 | 2027-08-25 | `POST /api/management/v2/useradm/users`. The v2 endpoint does not accept `password` or `send_reset_password`; new users always receive an invitation email to set their own password |
| `PUT /useradm/users/me` | Management v1 | 2026-07-24 | 2027-08-25 | 2027-08-25 | `PUT /api/management/v2/useradm/users/me`. The v2 endpoint does not accept `email` and only updates the password (together with `current_password`). To change the account email address, use `POST /api/management/v1/useradm/users/me/email-change/start` |

Hosted Mender APIs are retired 12 months after the deprecation announcement.
For on-premise releases, the version of Mender Server containing the deprecated API
remains supported for at least the same period, so the effective migration window
is the same regardless of deployment model.


## Deprecated fields

Individual request and response fields can be deprecated independently of the
endpoint that exposes them. The endpoints below remain supported; only the listed
field is deprecated.

| API | Field | Version | Deprecated since | EOL (hosted Mender) | EOL (on-premise) | Replacement |
|-----|-------|---------|------------------|---------------------|------------------|-------------|
| `POST /deployments/artifacts` | `size` (multipart form field) | Management v1 | 2020-04-06 | 2027-08-25 | 2027-08-25 | None required. The size is determined from the uploaded content |
| `GET /deployments/artifacts` and `GET /deployments/artifacts/{id}`, in the returned artifact objects | `updates[].meta_data` | Management v1, Management v2, Device v1 | 2025-10-29 | 2027-08-25 | 2027-08-25 | `updates[].metadata`, an object instead of a list of objects |
| `GET /deployments/deployments/releases/delta/jobs/{id}` | `from_release` | Management v2 | 2025-12-03 | 2027-08-25 | 2027-08-25 | `from_version`, which contains the same information |
| `GET /deployments/deployments/releases/delta/jobs/{id}` | `to_release` | Management v2 | 2025-12-03 | 2027-08-25 | 2027-08-25 | `to_version`, which contains the same information |
| `POST /useradm/tenants/{tenant_id}/users` | `propagate` | Internal v1 | 2023-07-06 | 2027-08-25 | 2027-08-25 | None required. Propagation of user information to tenantadm is permanently disabled |


## Deprecated features

| Feature | Deprecated since | EOL (hosted Mender) | EOL (on-premise) | Replacement / migration |
|---------|------------------|---------------------|------------------|-------------------------|
|         |                  |                     |                  |                         |
