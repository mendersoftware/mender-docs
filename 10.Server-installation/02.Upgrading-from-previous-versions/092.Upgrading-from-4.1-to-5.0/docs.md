---
title: Upgrading to Mender Server 5.0
taxonomy:
category: docs
label: tutorial
---

This is a tutorial for upgrading the Mender Server from version 4.1 to 5.0 in
production environments installed with the
[Mender Helm chart](../../04.Production-installation-with-kubernetes/03.Mender-server/docs.md).

Besides the version specific guidelines below, please make sure you're following
the [suggested upgrade best practices](../docs.md) to reduce the risk of
unpredictable downtime and data loss.

## Before you start
Ensure you have the mender values file from the previous installation.
You will need it as a base for the upgrade:

```bash
cp mender-values.yml mender-values-5.0.yml
```

You can now start editing the `mender-values-5.0.yml` file with the following
changes.

### Current version

<!--AUTOVERSION: "Be sure that your current version is %"/ignore -->
Be sure that your current version is 4.1 (`mender-helm >= 8.5`)
and that it works, and Mender Server starts properly.

### Backup

The database migrations of Mender Server 5.0 can't be reverted. Take a
[full backup](../../05.Backup-and-restore/docs.md) of MongoDB and of the
Artifact storage before the upgrade. A rollback to 4.1 requires restoring
this backup.

!! The MongoDB subchart included in the Helm chart stores its data in an
!! ephemeral volume, and is meant for evaluation only. If you are using it,
!! back up the data before the upgrade:
!! ```bash
!! kubectl exec deploy/mender-mongodb -- sh -c 'mongodump -u "$MONGO_INITDB_ROOT_USERNAME" -p "$MONGO_INITDB_ROOT_PASSWORD" --authenticationDatabase admin --gzip --archive' > mender-mongodb-4.1.archive.gz
!! ```

## Migrating from 4.1

### Docker image tag
<!--AUTOVERSION: "The Helm chart version % deploys"/ignore -->
The Helm chart version 8.5 deploys Mender Server 4.1 by default. Set the new
image tag in the `mender-values-5.0.yml` file:

<!--AUTOVERSION: "    tag: v%"/ignore -->
```yaml
default:
  image:
    tag: v5.0.0
```

No other change to the values file is required.

! `helm list` and `helm history` show the `APP VERSION` of the Helm chart, not
! the version you are running. Check the image tags of the running Pods instead.

### Removed configuration
The following environment variables are removed. Remove them from
`customEnvs` or `env` in your values file, if you set them.

[ui-tabs position="top-left" active="0" theme="default" ]
[ui-tab title="Open Source"]
* `DEVICEAUTH_ENABLE_REPORTING` and `DEPLOYMENTS_REPORTING_ADDR`: the
  `reporting` service is removed.

The `deviceauth` command `propagate-reporting` is removed. Remove any custom
CronJob that runs it.
[/ui-tab]
[ui-tab title="Enterprise"]
* `DEVICEAUTH_ENABLE_TIERS`: device tiers are always enabled.
* `DEVICEAUTH_ENABLE_REPORTING`, `DEVICEMONITOR_ENABLE_REPORTING` and
  `DEPLOYMENTS_REPORTING_ADDR`: the `reporting` service is removed.

The `deviceauth` commands `propagate-reporting` and `check-device-limits` are
removed. Remove any custom CronJob that runs them.
[/ui-tab]
[/ui-tabs]

### Device provisioning events
The `deviceauth` service triggers the device provisioning in the integrations,
such as [Webhooks](../../../11.Server-integration/07.Webhooks/docs.md) and
[Azure IoT Hub](../../../11.Server-integration/05.Azure-IoT-Hub/docs.md), only
once per device. In 4.1, every time a device became accepted triggered it again.
If your integration relies on the previous behavior, restore it with:

```yaml
device_auth:
  customEnvs:
    - name: DEVICEAUTH_LEGACY_PROVISION_DEVICE
      value: "true"
```

### Device tiers always enabled (Enterprise)
Device tiers are always enabled. Devices that report the `micro` or `system`
tier count against the `max_micro_devices` and `max_system_devices` limits of
the tenant, instead of the standard device limit. Existing tenants have no such
limits, and a missing limit is treated as 0: such devices can't be accepted,
and the ones already accepted lose access to the server after the upgrade.

Before the upgrade, set the limits for all the tenants:

```bash
export MENDER_MICRO_DEVICE_LIMIT=10
export MENDER_SYSTEM_DEVICE_LIMIT=10

kubectl run mender-tier-limits --restart=Never --image=curlimages/curl \
  --env=MICRO=${MENDER_MICRO_DEVICE_LIMIT} --env=SYSTEM=${MENDER_SYSTEM_DEVICE_LIMIT} \
  --command -- sh -c '
TENANTADM=http://mender-tenantadm:8080/api/internal/v1/tenantadm
DEVAUTH=http://mender-device-auth:8080/api/internal/v1/devauth
PAGE=1
while :; do
  IDS=$(curl -sf "${TENANTADM}/tenants?per_page=500&page=${PAGE}" | grep -o "\"id\":\"[0-9a-f]*\"" | cut -d\" -f4)
  [ -z "${IDS}" ] && break
  for TENANT_ID in ${IDS}; do
    for LIMIT in max_micro_devices:${MICRO} max_system_devices:${SYSTEM}; do
      curl -s -o /dev/null -w "${TENANT_ID} ${LIMIT} HTTP %{http_code}\n" -X PUT \
        -H "Content-Type: application/json" -d "{\"limit\": ${LIMIT#*:}}" \
        "${DEVAUTH}/tenant/${TENANT_ID}/limits/${LIMIT%%:*}"
    done
  done
  PAGE=$((PAGE + 1))
done
'
kubectl wait pod/mender-tier-limits --for=jsonpath='{.status.phase}'=Succeeded --timeout=120s
kubectl logs pod/mender-tier-limits
kubectl delete pod/mender-tier-limits
```

Every line must end with `HTTP 204`. Use `-1` for no limit.

After the upgrade, a device accepted on 4.1 that reports the `micro` or `system`
tier sends a new authentication request with its tier, which stays `pending`
while the device keeps the old `accepted` authentication set. The device can't
connect until you accept the new authentication set. You can do it from the UI,
in the authentication sets of the device, or with the following script. Run it
for each tenant, as a user allowed to manage devices:

```bash
export MENDER_SERVER_URL="https://mender.example.com"
export MENDER_USERNAME="admin@mender.io"
read -rs MENDER_PASSWORD
export MENDER_TOKEN=$(curl -sf -X POST -u "${MENDER_USERNAME}:${MENDER_PASSWORD}" \
  "${MENDER_SERVER_URL}/api/management/v1/useradm/auth/login")

PAGE=1
while :; do
  DEVICES=$(curl -sf -H "Authorization: Bearer ${MENDER_TOKEN}" \
    "${MENDER_SERVER_URL}/api/management/v2/devauth/devices?status=accepted&per_page=500&page=${PAGE}")
  [ "$(echo "${DEVICES}" | jq length)" -eq 0 ] && break
  echo "${DEVICES}" | jq -r '.[]
    | (.auth_sets | map(select(.status == "accepted")) | .[0].pubkey) as $key
    | .id as $device | .auth_sets[]
    | select(.status == "pending" and .pubkey == $key and (.tier // "standard") != "standard")
    | "\($device) \(.id)"' | while read -r DEVICE_ID AUTH_SET_ID; do
      curl -s -o /dev/null -w "${DEVICE_ID} HTTP %{http_code}\n" -X PUT \
        -H "Authorization: Bearer ${MENDER_TOKEN}" -H "Content-Type: application/json" \
        -d '{"status": "accepted"}' \
        "${MENDER_SERVER_URL}/api/management/v2/devauth/devices/${DEVICE_ID}/auth/${AUTH_SET_ID}/status"
    done
  PAGE=$((PAGE + 1))
done
```

!!! The script accepts only the authentication sets that use the same public key
!!! as the accepted one. A pending authentication set with a different key is a
!!! different device claiming the same identity: review it manually.

When you create new organizations with `tenantadm create-org`, set the limits
for all the tiers:

```bash
TENANTADM_POD=$(kubectl get pod -l 'app.kubernetes.io/component=tenantadm' -o name | head -1)
TENANT_ID=$(kubectl exec $TENANTADM_POD -- tenantadm create-org --name demo --username "admin@mender.io" --password "adminadmin" --plan enterprise \
  --device-limit -1 --micro-device-limit 10 --system-device-limit 10)
```

### Email address verification (Enterprise)
Users must verify their email address before they can create other users or
change the email address of other users; otherwise the Mender Server answers
`403 email verification is required`. Users can still log in. The users created
with Mender Server 4.1, and the administrators created with
`tenantadm create-org`, are not verified.

Verifying an email address requires the Mender Server to send emails. If your
installation doesn't send emails, disable the verification.

<!--AUTOVERSION: "Starting from the Mender Helm chart version %"/ignore -->
Starting from the Mender Helm chart version 8.6.0:

```yaml
useradm:
  insecure_disable_email_verification: true
```

With earlier versions of the Helm chart:

```yaml
useradm:
  customEnvs:
    - name: USERADM_INSECURE_DISABLE_EMAIL_VERIFICATION
      value: "true"
```

! With this setting, the Mender Server doesn't check that users own their email
! address. Use it only if you control who can create users.

### Email address validation (Enterprise)
The Mender Server now checks that the domain of a user email address exists in
DNS. The `useradm` Pods must be able to resolve the domain, for example the
`mender.io` in `admin@mender.io`. Creating a user with a domain that doesn't
resolve, or from a cluster without DNS access to the Internet, fails with
`email: must be a valid email address.` (or `User is invalid` from the
`tenantadm create-org` command). Existing users are not affected.
`USERADM_INSECURE_DISABLE_EMAIL_VERIFICATION` doesn't disable this check.

The check passes when the domain has an `MX` or an `A`/`AAAA` record. If you use
an internal domain, make it resolvable from the cluster: add the record to the
DNS server the cluster uses, or configure the cluster DNS to resolve it. Refer
to the documentation of your Kubernetes distribution to customize CoreDNS. For
example, on K3s:

```bash
export MENDER_EMAIL_DOMAIN="corp.example.internal"
export MENDER_EMAIL_DOMAIN_IP="replace-with-your-mail-server-ip"

kubectl apply -f - <<EOF
apiVersion: v1
kind: ConfigMap
metadata:
  name: coredns-custom
  namespace: kube-system
data:
  mender-email-domain.server: |
    ${MENDER_EMAIL_DOMAIN}:53 {
      hosts {
        ${MENDER_EMAIL_DOMAIN_IP} ${MENDER_EMAIL_DOMAIN}
      }
    }
EOF
kubectl -n kube-system rollout restart deploy/coredns
```

### Database migrations
The database migrations run automatically, before the new Pods start, in the
`pre-upgrade` Jobs of the Helm chart. The migrations:

* set the standard device limit `0` to `-1` (no limit);
* add an index to the devices;
* Enterprise only: replace the unique index of the device authentication sets,
  and add indexes to the users.

The time the migrations take grows with the number of devices.

## Cluster capacity

The migration Jobs and the rolling update of the Deployments run next to the
running Pods. If the cluster doesn't have enough free CPU and memory for them,
the Pods stay `Pending` and `helm upgrade --wait` times out. Make sure the
cluster has free capacity, as described in the
[Resources](../../04.Production-installation-with-kubernetes/docs.md#resources)
section.

## Maintenance window

Be prepared for a maintenance window depending on your Mender setup size.
Please perform a test-run upgrade test in a protected environment first,
also to track the required maintenance window for your environment.

During the rolling update, the requests that start a workflow, for example the
provisioning of a device or the creation of an organization, can fail until all
the Pods run the new version.

## Upgrade procedure
When you have your `mender-values-5.0.yml` file ready, you can proceed with the upgrade:

```bash
helm upgrade mender mender/mender --wait --timeout 15m -f mender-values-5.0.yml
```

Verify that all the Pods run the new version:

```bash
kubectl get pods -l 'app.kubernetes.io/part-of=mender' \
  -o jsonpath='{range .items[*]}{.spec.containers[0].image}{"\n"}{end}' | sort | uniq -c
```

## Rollback
The Mender Server 4.1 starts on a database migrated to 5.0, but the data written
by 5.0, for example the devices that changed tier, is not consistent anymore.
To roll back, restore the backup taken before the upgrade, and then run:

```bash
helm rollback mender
```

## Troubleshooting
Enterprise: devices that report the `micro` or `system` tier get `401 Unauthorized` after the upgrade:

* Check the tier limits of the tenant, as described in
  [Device tiers always enabled](#device-tiers-always-enabled-enterprise).
* Accept the pending authentication set of the devices.

Accepting a device fails with `maximum number of accepted devices reached`:

* The limit of the device tier is not set, or it's reached.

Enterprise: creating a user fails with `403 email verification is required`:

* See [Email address verification](#email-address-verification-enterprise).

The `helm upgrade` command times out, and the migration Jobs or the new Pods
are `Pending` with `Insufficient cpu` or `Insufficient memory`:

* See [Cluster capacity](#cluster-capacity).
