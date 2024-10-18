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

[Load Balancer](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer)
to expose the Mender Server outside the Kubernetes cluster.

**Required configuration**:
* Redirection from HTTP to HTTPS on the Ingress.
* Health check: if your load balancer requires it, the internal path is `/ui`
* Either a valid certificate for the `${MENDER_SERVER_DOMAIN}` must exists as a secret named `mender-ingress-tls`, or
  you already have configured the [Cert-manager](../01.Kubernetes/docs.md#installation-of-cert-manager-optional) resource
* The Mender Helm chart is deployed with the `api_gateway.env.SSL=false` option:
  ```
  api_gateway:
    env:
      SSL: false
  ```

<!--AUTOVERSION: "Starting from the Mender Helm Chart version %"/ignore -->
You can refer to your Infrastructure Provider's documentation for creating an Ingress resource.
Starting from the Mender Helm Chart version 5.1.0, a sample Ingress resource is included.

For example, here's an Ingress for the AWS EKS Provider:

<!--AUTOVERSION: "cat <<-EOF >> mender-%.yml"/integration -->
```bash
cat <<-EOF >> mender-master.yml
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

For example, here's an Ingress for Azure AKS Provider:

<!--AUTOVERSION: "cat <<-EOF >> mender-%.yml"/ignore -->
```bash
cat <<-EOF >> mender-master.yml
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

For example, here's an Ingress for the Ingress-NGinx Provider:
<!--AUTOVERSION: "cat <<-EOF >> mender-%.yml"/ignore -->
```bash
cat <<-EOF >> mender-master.yml
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

You can now update the Helm Chart with the included ingress:
<!--AUTOVERSION: "helm upgrade --install mender mender/mender -f mender-%.yml"/integration -->
```bash
helm upgrade --install mender mender/mender -f mender-master.yml
```

Alternatively, you can create your own Ingress resource. Some references:
* [Kubernetes Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
* [AWS EKS Ingress](https://docs.aws.amazon.com/eks/latest/userguide/alb-ingress.html)
* [Azure Ingress](https://learn.microsoft.com/en-us/azure/aks/ingress-basic?tabs=azure-cli)


#### Troubleshooting
Some users have reported that when using the nginx ingress controller, the troubleshoot add-on
may not work properly. If you encounter this issue, you can try using the following annotation:
```
metadata:
  annotations:
    nginx.org/client-max-body-size: 128m
    nginx.org/websocket-services: mender-api-gateway
```

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
kubectl exec $USERADM_POD -- useradm-enterprise create-user --username "demo@mender.io" --password "demodemo" --tenant-id $TENANT_ID
```
[/ui-tab]
[/ui-tabs]

## Pre-release version

<!--AUTOVERSION: "pre-release (%)"/ignore-->
To use a pre-release (master) version of the backend, please refer to [the Development section of
the
documentation](https://docs.mender.io/development/server-installation/production-installation-with-kubernetes/mender-server).
