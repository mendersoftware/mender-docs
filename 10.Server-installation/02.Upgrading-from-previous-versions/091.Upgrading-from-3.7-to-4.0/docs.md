---
title: Upgrading to Mender Server 4.0
taxonomy:
category: docs
label: tutorial
---

This is a tutorial for upgrading the Mender Server from version 3.7 to
4.0 in production environments.

Besides the version specific guidelines below, please make sure you're following
the [suggested upgrade best practices](../docs.md) to reduce the risk of
unpredictable downtime and data loss.

## Before you start
Ensure you have the mender values file from the previous installation. 
You will need it as a base for the new installation:

<!--AUTOVERSION: "cp mender-%"/ignore -->
```bash
cp mender-3.7*.yml mender-values.yml
```

You can now start editing the `mender-values.yml` file with the following
changes.

### Current version

<!--AUTOVERSION: "Be sure that your current version is %"/ignore -->
Be sure that your current version is 3.7 (`mender-helm >= 5.9`)
and that it works, and Mender Server starts properly.

<!--AUTOVERSION: "## Migrating from %"/ignore -->
## Migrating from 3.7
The helm chart is versioned separately from the Mender releases.

<!--AUTOVERSION: "Until the helm chart version %"/ignore -->
<!--AUTOVERSION: "Mender % and %. Starting from Mender %, you have to use at least the"/ignore -->
<!--AUTOVERSION: "chart version %"/ignore -->
Until the helm chart version 5.x, the chart is compatible with both
Mender 3.6 and 3.7. Starting from Mender Server 4.0, you have to use at least the
chart version 6.0.x.
You should be aware of a few deprecations:

### Global section deprecations
The `global` section is internally dedicated to the global configuration,
for sub-charts also. So we are moving the Mender resources from the `global`
key to the `default` key. For this reason, the `global.image` key is 
moved to the `default.image` key: please make sure to comment out
your `global.image` key:
<!--AUTOVERSION: "  #   tag: mender-%"/ignore -->
```yaml
global:
  # image:
  #   tag: mender-3.7.7
```

### New repositories location
Following a migration from multiple repositories to a single Monorepo, the
Container repositories has been moved to respect the new structure.
Additionally, the `mender-x.y` tag has been replaced with the `vx.y` tag.
* Enterprise registry:
  1. removing `-enterprise` suffix;
  2. changing `/mendersoftware` to `/mender-server-enterprise`;
  3. moving the remaining components from Docker Hub to `registry.mender.io`.

* Open Source registry:
  1. moving from `docker.io/mendersoftware/deployments:mender-3.7`
  to `docker.io/mendersoftware/deployments:v4.0`.


The new repository structure is already reflected in the default `values.yaml`
file; please make sure to not override it in your `mender-values.yaml` file.

!! If you are mirroring the images, please make sure to update the mirroring
!! configuration to reflect the new repository structure.

The following table provides a comprehensive list of the changes to the docker
image references.
[ui-tabs position="top-left" active="0" theme="default" ]
[ui-tab title="Open Source"]
| Former image reference                                       | New image reference                                    |
| ------------------------------------------------------------ | ------------------------------------------------------ |
| docker.io/mendersoftware/create-artifact-worker:mender-X.Y.Z | docker.io/mendersoftware/create-artifact-worker:vX.Y.Z |
| docker.io/mendersoftware/deployments:mender-X.Y.Z            | docker.io/mendersoftware/deployments:vX.Y.Z            |
| docker.io/mendersoftware/deviceauth:mender-X.Y.Z             | docker.io/mendersoftware/deviceauth:vX.Y.Z             |
| docker.io/mendersoftware/deviceconfig:mender-X.Y.Z           | docker.io/mendersoftware/deviceconfig:vX.Y.Z           |
| docker.io/mendersoftware/deviceconnect:mender-X.Y.Z          | docker.io/mendersoftware/deviceconnect:vX.Y.Z          |
| docker.io/mendersoftware/gui:mender-X.Y.Z                    | docker.io/mendersoftware/gui:vX.Y.Z                    |
| docker.io/mendersoftware/inventory:mender-X.Y.Z              | docker.io/mendersoftware/inventory:vX.Y.Z              |
| docker.io/mendersoftware/iot-manager:mender-X.Y.Z            | docker.io/mendersoftware/iot-manager:vX.Y.Z            |
| docker.io/mendersoftware/useradm:mender-X.Y.Z                | docker.io/mendersoftware/useradm:vX.Y.Z                |
| docker.io/mendersoftware/workflows:mender-X.Y.Z              | docker.io/mendersoftware/workflows:vX.Y.Z              |
| docker.io/mendersoftware/workflows-worker:mender-X.Y.Z       | docker.io/mendersoftware/workflows:vX.Y.Z              |


! Please note that the `workflows-worker` image has been discontinued:
! the `workflows` image is now handling both the `workflows` services.

[/ui-tab]
[ui-tab title="Enterprise"]
| From                                                                  | To                                                                        |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| registry.mender.io/mendersoftware/auditlogs:mender-X.Y.Z              | registry.mender.io/mender-server-enterprise/auditlogs:vX.Y.Z              |
| docker.io/mendersoftware/create-artifact-worker:mender-X.Y.Z          | registry.mender.io/mender-server-enterprise/create-artifact-worker:vX.Y.Z |
| registry.mender.io/mendersoftware/deployments-enterprise:mender-X.Y.Z | registry.mender.io/mender-server-enterprise/deployments:vX.Y.Z            |
| registry.mender.io/mendersoftware/deviceauth-enterprise:mender-X.Y.Z  | registry.mender.io/mender-server-enterprise/deviceauth:vX.Y.Z             |
| docker.io/mendersoftware/deviceconfig:mender-X.Y.Z                    | registry.mender.io/mender-server-enterprise/deviceconfig:vX.Y.Z           |
| docker.io/mendersoftware/deviceconnect:mender-X.Y.Z                   | registry.mender.io/mender-server-enterprise/deviceconnect:vX.Y.Z          |
| registry.mender.io/mendersoftware/devicemonitor:mender-X.Y.Z          | registry.mender.io/mender-server-enterprise/devicemonitor:vX.Y.Z          |
| registry.mender.io/mendersoftware/generate-delta-worker:mender-X.Y.Z  | registry.mender.io/mender-server-enterprise/generate-delta-worker:vX.Y.Z  |
| registry.mender.io/mendersoftware/inventory-enterprise:mender-X.Y.Z   | registry.mender.io/mender-server-enterprise/inventory:vX.Y.Z              |
| docker.io/mendersoftware/iot-manager:mender-X.Y.Z                     | registry.mender.io/mender-server-enterprise/iot-manager:vX.Y.Z            |
| registry.mender.io/mendersoftware/tenantadm:mender-X.Y.Z              | registry.mender.io/mender-server-enterprise/tenantadm:vX.Y.Z              |
| registry.mender.io/mendersoftware/useradm:mender-X.Y.Z                | registry.mender.io/mender-server-enterprise/useradm:vX.Y.Z                |
| registry.mender.io/mendersoftware/workflows:mender-X.Y.Z              | registry.mender.io/mender-server-enterprise/workflows:vX.Y.Z              |
| registry.mender.io/mendersoftware/workflows-worker:mender-X.Y.Z       | registry.mender.io/mender-server-enterprise/workflows:vX.Y.Z              |

 
! Please note that the `workflows-worker` image has been discontinued:
! the `workflows` image is now handling both the `workflows` services.

[/ui-tab]
[/ui-tabs]

### Drop the "mender-" prefix in the tags names
As part of the Mender Server v4 release, we are splitting the Mender Server
from the rest of the Mender components (Mender Client, `mender-cli`,
`mender-artifact`). Therefore we are dropping the Mender bundle tags
`mender-x.y.z`. The new tags are on the form `vX.Y.Z` where X.Y.Z is the
*Mender Server* version.  
This is no longer valid:

<!--AUTOVERSION: "    tag: mender-%"/ignore -->
```yaml
# previous version no longer valid
global:
  image:
    tag: mender-3.7.7
```
<!--AUTOVERSION: "Instead the new tag is simply `v%"/ignore -->
Instead the new tag is simply `v4.0.0`:

<!--AUTOVERSION: "    tag: v%"/ignore -->
```yaml
# new version
default:
  image:
    tag: v4.0.0
```
The default values is handling this already, so you don't need to change it. 

```yaml
global:
#  image:

default:
#  image:
```


### ImagePullSecrets instead cleartext credentials: 
For improved security, the `global.image.username` and `global.image.password`
are deprecated in favor of `default:imagePullSecrets`:
with this new Helm Chart release, you have to manually create a new Docker
Registry secret, like this:
```bash
export MENDER_REGISTRY_USERNAME="replace-with-your-username"
export MENDER_REGISTRY_PASSWORD="replace-with-your-password"
export MENDER_REGISTRY_EMAIL="replace-with-your-email"

kubectl create secret docker-registry my-mender-pull-secret \
  --docker-username=${MENDER_REGISTRY_USERNAME} \
  --docker-password=${MENDER_REGISTRY_PASSWORD} \
  --docker-email=${MENDER_REGISTRY_EMAIL} \
  --docker-server=registry.mender.io
```
and reference it in the `mender-values.yaml` file:

```yaml
global:
  # image:
  #   username: "redacted"
  #   password: "redacted"
default:
  imagePullSecrets:
    - name: my-mender-pull-secret
```

### Rootless gui container
For improved security, the `gui` container is now rootles; this means that
the `gui.httpPort` is switched from `80` to the unprivileged `8090` port.
Make sure you are not overriding the `gui.httpPort` in your
`mender-values.yaml` file.

### Service Keys automatically generated
You can choose to specify the `device_auth.certs.key`,
`useradm.certs.key`, and `tenantadm.certs.key` keys in
the `mender-values.yaml` file, but it is not mandatory anymore.
If you don't specify them, the Helm Chart will generate them for you.

### NATS and MongoDB subcharts enabled by default
To facilitate the first Helm Chart installation, the MongoDB and NATS
subcharts are enabled by default:
```yaml
mongodb:
  enabled: true

nats:
  enabled: true
```
If you are using an external MongoDB or NATS instance, please make sure to 
explicitly disable them before the upgrade:
```yaml
mongodb:
  enabled: false

nats:
  enabled: false
```

### Redis subchart disabled by default
The Redis subchart is disabled by default, because it is not used in the Open
Source version. If you want to use it in the Enterprise version, please
make sure to enable it:
```yaml
redis:
  enabled: true
```

### Enterprise false by default
The Enterprise version is disabled by default. If you are using it, please
make sure to enable it:
```yaml
global:
  enterprise: true
```

### Storage Proxy enabled by default
By default, the Storage Proxy is enabled. If you don't want to use it, please
restore the previous configuration:
```yaml
api_gateway:
  storage_proxy:
    enabled: false

deployments:
  customEnvs: []
```

But if you want to use it, you have to set the `DEPLOYMENTS_STORAGE_PROXY_URI`
environment variable to the URL exposed, the bucket name in the 
API Gateway configuration, and the `s3.AWS_URI` to the storage endpoint:
```yaml
global:
  s3:
    AWS_URI: "${STORAGE_ENDPOINT:?must be set to your bucket endpoint URL}"
    AWS_FORCE_PATH_STYLE: "true"

api_gateway:
  storage_proxy:
    enabled: true
    url: "${STORAGE_ENDPOINT}"
    customRule: "PathRegexp(`^/${STORAGE_BUCKET:?must be set to your bucket name}`)"
    passHostHeader: false

deployments:
  customEnvs:
    - name: DEPLOYMENTS_STORAGE_PROXY_URI
      value: "https://${MENDER_SERVER_DOMAIN:?must be set to your server domain}"
```

where:
* `MENDER_SERVER_DOMAIN` is the domain of the Mender Server, e.g:
  `mender.example.com`
* `STORAGE_ENDPOINT` is the endpoint of the storage, e.g: 
  `https://s3.${AWS_REGION}.amazonaws.com`
* `AWS_BUCKET` is the name of the bucket, e.g: `mender-artifacts`

## Maintenance window

Be prepared for a maintenance window depending on your Mender setup size.
Please perform a test-run upgrade test in a protected environment first,
also to track the required maintenance window for your environment.

## Upgrade procedure
When you have your `mender-values.yml` file ready, you can proceed with the upgrade:

```bash
helm upgrade mender mender/mender -f mender-values.yml
```

## Troubleshooting
The `workflows-worker` and the `create-artifact-worker` are crashing with this error log:
```
failed to apply Jetstream consumer migrations: context deadline exceeded
```

* Double check the NATS url, if you are using an external NATS instance: `global.nats.URL`
  or `global.nats.existingSecret`
* Verify that both `create_artifac_worker.automigrate` and `workflows.automigrate` are set to `false`
