---
title: Mender Server
taxonomy:
    category: docs
    label: tutorial
---

! Please note the code snippets in this section reuses the environment variables
! you set up when progressing through the tutorial, including the optional step
! of installing the Artifact Storage. Please make sure you correctly define them
! or adapt the snippet to your specific use case.

## Prerequisites

### Object storage
Please refer to the [Storage](../02.Storage/docs.md) section for more
information on how to set up an object storage service.

### Ingress Controller

You must configure an
[Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
or a
[Load Balancer](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer)
to expose the Mender Server outside the Kubernetes cluster.

**Required configuration**:
* Redirection from HTTP to HTTPS on the Ingress.
* Health check: if your load balancer requires it, the internal path is `/ui`
* Either a valid certificate for the `${MENDER_SERVER_DOMAIN}` must exists
  as a secret named `mender-ingress-tls`, or  you already have configured the
  [Cert-manager](../01.Kubernetes/docs.md#installation-of-cert-manager-optional)
  resource

<!--AUTOVERSION: "Starting from the Mender Helm Chart version %"/ignore -->
You can refer to your Infrastructure Provider's documentation for creating an Ingress resource.
Starting from the Mender Helm Chart version 5.1.0, a sample Ingress resource is included.
Starting from the Mender Helm Chart version 6.0.0, the
Ingress feature is enabled by default.

Following some Ingress examples. Please refer to 
your Infrastructure Provider's documentation for
creating an Ingress resource and for the required
annotations.

[ui-tabs position="top-left" active="0" theme="default" ]
[ui-tab title="Traefik"]
For example, here's an Ingress for the Traefik Provider, included in K3s:

<!--AUTOVERSION: "cat <<-EOF >> mender-%.yml"/integration -->
```bash
export MENDER_SERVER_DOMAIN="mender.example.com"

cat <<-EOF > mender-values.yml
ingress:
  enabled: true
  annotations:
    cert-manager.io/issuer: "letsencrypt"
  ingressClassName: traefik
  path: /
  hosts:
    - ${MENDER_SERVER_DOMAIN}
  tls:
  # this secret must exists or it can be created from a working cert-manager instance
    - secretName: mender-ingress-tls
      hosts:
        - ${MENDER_SERVER_DOMAIN}
EOF
```

[/ui-tab]
[ui-tab title="AWS EKS"]
For example, here's an Ingress for the AWS EKS Provider:

<!--AUTOVERSION: "cat <<-EOF >> mender-%.yml"/integration -->
```bash
export MENDER_SERVER_DOMAIN="mender.example.com"

cat <<-EOF > mender-values.yml
ingress:
  enabled: true
  annotations:
    cert-manager.io/issuer: "letsencrypt"
    alb.ingress.kubernetes.io/healthcheck-path: /ui/
    alb.ingress.kubernetes.io/actions.ssl-redirect: '{"Type": "redirect", "RedirectConfig":{ "Protocol": "HTTPS", "Port": "443", "StatusCode": "HTTP_301"}}'
    alb.ingress.kubernetes.io/backend-protocol: HTTP
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTP": 80}, {"HTTPS":443}]'
    alb.ingress.kubernetes.io/load-balancer-attributes: routing.http2.enabled=true,idle_timeout.timeout_seconds=600
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/ssl-policy: ELBSecurityPolicy-TLS-1-2-2017-01
    alb.ingress.kubernetes.io/target-type: ip
  ingressClassName: alb
  path: /
  extraPaths:
    - path: /
      backend:
        serviceName: ssl-redirect
        servicePort: use-annotation
  hosts:
    - ${MENDER_SERVER_DOMAIN}
  tls:
  # this secret must exists or it can be created from a working cert-manager instance
    - secretName: mender-ingress-tls
      hosts:
        - ${MENDER_SERVER_DOMAIN}
EOF
```

[/ui-tab]
[ui-tab title="Azure AKS"]

For example, here's an Ingress for Azure AKS Provider:

<!--AUTOVERSION: "cat <<-EOF >> mender-%.yml"/ignore -->
```bash
export MENDER_SERVER_DOMAIN="mender.example.com"

cat <<-EOF > mender-values.yml
ingress:
  enabled: true
cat <<-EOF >> mender-values.yml
ingress:
  enabled: true
  annotations:
    appgw.ingress.kubernetes.io/backend-protocol: http
    appgw.ingress.kubernetes.io/health-probe-path: /ui/
    appgw.ingress.kubernetes.io/request-timeout: "600"
    appgw.ingress.kubernetes.io/ssl-redirect: "true"
  ingressClassName: azure/application-gateway
  path: /
  hosts:
    - ${MENDER_SERVER_DOMAIN}
  tls:
  # this secret must exists or it can be created from a working cert-manager instance
    - secretName: mender-ingress-tls
      hosts:
        - ${MENDER_SERVER_DOMAIN}
EOF
```
[/ui-tab]
[ui-tab title="Ingress NGinx"]

For example, here's an Ingress for the Ingress-NGinx Provider:
<!--AUTOVERSION: "cat <<-EOF >> mender-%.yml"/ignore -->
```bash
export MENDER_SERVER_DOMAIN="mender.example.com"

cat <<-EOF > mender-values.yml
ingress:
  enabled: true
cat <<-EOF >> mender-values.yml
ingress:
  enabled: true
  annotations:
    nginx.ingress.kubernetes.io/proxy-body-size: "0"
    nginx.ingress.kubernetes.io/proxy-buffering: "off"
    nginx.ingress.kubernetes.io/proxy-read-timeout: "600"
    nginx.ingress.kubernetes.io/proxy-send-timeout: "600"
  path: /
  ingressClassName: nginx
  hosts:
    - ${MENDER_SERVER_DOMAIN}
  tls:
  # this secret must exists or it can be created from a working cert-manager instance
    - secretName: mender-ingress-tls
      hosts:
        - ${MENDER_SERVER_DOMAIN}
EOF
```

#### Troubleshooting
Some users have reported that when using the nginx ingress controller, the troubleshoot add-on
may not work properly. If you encounter this issue, you can try using the following annotation:
```
metadata:
  annotations:
    nginx.org/client-max-body-size: 128m
    nginx.org/websocket-services: mender-api-gateway
```

[/ui-tab]
[ui-tab title="NodePort"]

Alternatively, you could use a NodePort service to expose the Mender Server:
```
cat <<-EOF >> mender-values.yml
ingress:
  enabled: false

api_gateway:
  service:
    type: NodePort
    api_gateway:
    httpNodePort: 30080
    httpsNodePort: 30443
```

You then have to configure a custom Load Balancer to forward the traffic to the
NodePort service.

[/ui-tab]
[/ui-tabs]

#### Other Ingress Controllers
Alternatively, you can create your own Ingress resource. Some references:
* [Kubernetes Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
* [AWS EKS Ingress](https://docs.aws.amazon.com/eks/latest/userguide/alb-ingress.html)
* [Azure Ingress](https://learn.microsoft.com/en-us/azure/aks/ingress-basic?tabs=azure-cli)




### Optional: external services
The Mender Helm chart is packaged with required external services:
* [MongoDB](https://bitnami.com/stack/mongodb/helm)
* [NATS](https://nats-io.github.io/k8s/)
* [Redis](https://bitnami.com/stack/redis/helm)

Using these packages is fine for test or PoC setups.
For production setups, however, it's recommended to use external dedicated services.


## Installing the Mender Helm chart

! Please note the code snippets in this section reuses the environment variables
! you set up when progressing through the tutorial, including the optional step
! of installing the Artifact Storage. Please make sure you correctly define them
! or adapt the snippet to your specific use case.

Before installing the Mender Server on the Kubernetes cluster using the
[Mender Helm chart](https://github.com/mendersoftware/mender-helm), add the
Mender Helm Chart repository:

```bash
helm repo add mender https://charts.mender.io
helm repo update
```

You can now install the Mender Server. You also have to decide how to expose
the Mender API Gateway service. This Helm Chart includes a configurable Ingress resource
for your convenience. More sample Ingress values are detailed in the later section.

[ui-tabs position="top-left" active="0" theme="default" ]
[ui-tab title="Open Source"]
<!--AUTOVERSION: "export MENDER_VERSION_TAG=\"mender-%\""/integration "cat >mender-%.yml <<EOF"/integration "helm upgrade --install mender mender/mender -f mender-%.yml"/integration -->
```bash
export MENDER_SERVER_DOMAIN="mender.example.com"
export MENDER_SERVER_URL="https://${MENDER_SERVER_DOMAIN}"

cat <<-EOF >> mender-values.yml
global:
  s3:
    AWS_URI: "${MENDER_SERVER_URL}"
    AWS_BUCKET: "${STORAGE_BUCKET}"
    AWS_ACCESS_KEY_ID: "${AWS_ACCESS_KEY_ID}"
    AWS_SECRET_ACCESS_KEY: "${AWS_SECRET_ACCESS_KEY}"
  url: "${MENDER_SERVER_URL}"

api_gateway:
  storage_proxy:
    enabled: true
    url: "${STORAGE_ENDPOINT}"
    customRule: "PathRegexp(\`^/${STORAGE_BUCKET}\`)"

deployments:
  customEnvs:
    - name: DEPLOYMENTS_STORAGE_PROXY_URI
      value: "${MENDER_SERVER_URL}"
EOF
```
Finally, install the Mender Server:

```bash
helm upgrade --install mender mender/mender -f mender-values.yml
```
[/ui-tab]
[ui-tab title="Enterprise"]


!!!!! The following deployment requires access to the Mender Enterprise
!!!!! Container Registry. Please email [contact@mender.io](mailto:contact@mender.io) to
!!!!! receive an evaluation account.

Create the Docker registry secret:
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

```bash
cat <<-EOF >> mender-values.yml
default:
  imagePullSecrets:
    - name: my-mender-pull-secret
EOF
```

If you provide your own MongoDB, create a secret with 
with the keys: `MONGO` and `MONGO_URL` both with the
MongoDB connection string format, for example:

```bash
kubectl create secret generic mender-mongo \
  --from-literal=MONGO="mongodb://mymongouser:mymongopassword@my-mongo-host:27017/mender" \
  --from-literal=MONGO_URL="mongodb://mymongouser:mymongopassword@my-mongo-host:27017/mender"
```

Now you can configure the Mender Server:

<!--AUTOVERSION: "export MENDER_VERSION_TAG=\"mender-%\""/integration "cat >mender-%.yml <<EOF"/integration "helm upgrade --install mender mender/mender -f mender-%.yml"/integration -->
```bash
export MENDER_SERVER_DOMAIN="mender.example.com"
export MENDER_SERVER_URL="https://${MENDER_SERVER_DOMAIN}"


cat <<-EOF >> mender-values.yml
global:
  enterprise: true
  mongodb:
    existingSecret: mender-mongo
  s3:
    AWS_URI: "${STORAGE_ENDPOINT}"
    AWS_BUCKET: "${STORAGE_BUCKET}"
    AWS_REGION: "${AWS_REGION}"
    AWS_ACCESS_KEY_ID: "${AWS_ACCESS_KEY_ID}"
    AWS_SECRET_ACCESS_KEY: "${AWS_SECRET_ACCESS_KEY}"
  url: "${MENDER_SERVER_URL}"

# Disable the MongoDB subchart:
mongodb:
  enabled: false

# Enable Redis
redis:
  enabled: true

api_gateway:
  storage_proxy:
    enabled: true
    url: "${STORAGE_ENDPOINT}"
    customRule: "PathRegexp(\`^/${STORAGE_BUCKET}\`)"

deployments:
  customEnvs:
    - name: DEPLOYMENTS_STORAGE_PROXY_URI
      value: "${MENDER_SERVER_URL}"
EOF

```

Alternatively, if you don't want to use the Storage Proxy feature, and
get the artifacts directly from the Artifact Storage, you can disable it:
```bash
export MENDER_SERVER_DOMAIN="mender.example.com"
export MENDER_SERVER_URL="https://${MENDER_SERVER_DOMAIN}"

cat <<-EOF >> mender-values.yml
global:
  enterprise: true
  mongodb:
    existingSecret: mender-mongo
  s3:
    AWS_URI: "${STORAGE_ENDPOINT}"
    AWS_BUCKET: "${STORAGE_BUCKET}"
    AWS_REGION: "${AWS_REGION}"
    AWS_ACCESS_KEY_ID: "${AWS_ACCESS_KEY_ID}"
    AWS_SECRET_ACCESS_KEY: "${AWS_SECRET_ACCESS_KEY}"
  url: "${MENDER_SERVER_URL}"

# Disable the MongoDB subchart:
mongodb:
  enabled: false

# Enable Redis
redis:
  enabled: true

api_gateway:
  storage_proxy:
    enabled: false

deployments:
  customEnvs: []
EOF
```

Finally, install the Mender Server:

```bash
helm upgrade --install mender mender/mender -f mender-values.yml
```
[/ui-tab]
[/ui-tabs]

### How to select the Docker tag to use

We support the following Docker image tags:

<!--AUTOVERSION: "Moving tag for the latest development version: `mender-%`"/ignore -->
* Immutable tag for a specific bugfix version: e.g., `vX.Y.Z` (recommended)
* Moving tag for a specific minor version: e.g., `vX.Y`
* Moving tag for a major version: e.g., `vX`
* Moving tag for the latest released bugfix version: `latest`
* Moving tag for the latest development version: `main`

## Post-installation setup

### Enable replication for NATS Jetstream (Recommended)
For production setup that require high availablility, we recommend enabling replication for the NATS Jetstream work queues.
By default, NATS deploys 3 replicas, but the stream created by the workflows service does not have replication enabled and therefore has no fault tolerance.
The following snippet increases the number of replicas to 3.

!!!! Please replace `NATS_URL` in the following snippet with a URL that resolves to any of the NATS pods.

```bash
NATS_URL="nats://mender-nats" # REPLACE
kubectl run --env=NATS_URL=$NATS_URL --image=natsio/nats-box:0.14.5-nonroot \
    nats-increase-replicas -- \
    nats stream edit WORKFLOWS --force --replicas=3
```

### Create the admin user

[ui-tabs position="top-left" active="0" theme="default" ]
[ui-tab title="Open Source"]
Create the initial user using the `useradm` pod:
```bash
USERADM_POD=$(kubectl get pod -l 'app.kubernetes.io/component=useradm' -o name | head -1)
kubectl exec $USERADM_POD -- useradm create-user --username "demo@mender.io" --password "demodemo"
```
[/ui-tab]
[ui-tab title="Enterprise"]

Create the administrator user using the `tenantadm` pod:
```bash
TENANTADM_POD=$(kubectl get pod -l 'app.kubernetes.io/component=tenantadm' -o name | head -1)
TENANT_ID=$(kubectl exec $TENANTADM_POD -- tenantadm create-org --name demo --username "admin@mender.io" --password "adminadmin" --plan enterprise)
```

You can create additional users from the command line of the `useradm` pod:

```bash
USERADM_POD=$(kubectl get pod -l 'app.kubernetes.io/component=useradm' -o name | head -1)
kubectl exec $USERADM_POD -- useradm create-user --username "demo@mender.io" --password "demodemo" --tenant-id $TENANT_ID
```
[/ui-tab]
[/ui-tabs]

## Pre-release version

<!--AUTOVERSION: "pre-release (%)"/ignore-->
To use a pre-release (master) version of the backend, please refer to [the Development section of
the
documentation](https://docs.mender.io/development/server-installation/production-installation-with-kubernetes/mender-server).
