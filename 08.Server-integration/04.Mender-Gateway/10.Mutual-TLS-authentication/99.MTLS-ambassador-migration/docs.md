---
title: MTLS Ambassador migration guide
taxonomy:
    category: docs
---

This guide will take you through the process of migrating from the deprecated `mtls-ambassador` to Mender Gateway.
Mender Gateway uses a json configuration which by default is located at `/etc/mender/mender-gateway.conf`.
The following snippet shows how to generate a configuration file compatible with Mender Gateway from the corresponding configuration environment variables exposed by the `mtls-ambassador`.
```bash
cat > mender-gateway.conf <<EOF
{
  "Features": {
    "mTLS": {
      "Enabled": true,
      "MenderUsername": "${MTLS_MENDER_USER}",
      "MenderPassword": "${MTLS_MENDER_PASS}",
      "CACertificate": "${MTLS_MENDER_CERT}",
      "BlacklistPath": "${MTLS_BLACKLIST_PATH}"
    }
  },
  "HTTPS": {
    "Enabled": true,
    "Listen": "${MTLS_LISTEN:-8080}",
    "MinimumTLSVersion": "${MTLS_HTTPS_TLS_VERSION_MIN:-1.2}",
    "ServerCertificate": "${MTLS_SERVER_CERT:-/etc/mtls/certs/server/server.crt}",
    "ServerKey": "${MTLS_SERVER_KEY:-/etc/mtls/certs/server/server.key}"
  },
  "UpstreamServer": {
    "URL": "${MTLS_MENDER_BACKEND}",
    "ServerCertificate": "${MTLS_MENDER_CERT}",
    "InsecureSkipVerify": ${MTLS_InsecureSkipVerify:-false}
  }
}
EOF
```

<!--AUTOVERSION: "mender-gateway:%"/mender-gateway -->
In your container deployment, replace the image reference with `registry.mender.io/mendersoftware/mender-gateway:1.3.0` and make sure the generated config file is mounted at `/etc/mender/mender-gateway.conf`.
For example, for a kubernetes deployment you can apply the following patches to your manifests:
```bash
DEPLOYMENT_NAME="mender-mtls"
CONTAINER_NAME="mender-mtls"
kubectl create configmap mender-mtls-conf --from-file=mender-gateway.conf

cat | kubectl patch deployment.apps "$DEPLOYMENT_NAME" -f- <<EOF
{
    "spec": {
        "containers": [{
            "name": "${CONTAINER_NAME}",
            "image": "registry.mender.io/mendersoftware/mender-gateway:1.3.0",
            "volumeMounts": [{
                "mountPath": "/etc/mender/mender-gateway.conf",
                "name": "mender-gateway-conf",
                "subPath": "mender-gateway.conf",
                "readOnly": true
            }]
        }],
        "volumes": [{
            "configMap": {
                "name": "mender-gateway-conf"
            },
            "name": "mender-gateway-conf"
        }]
    }
}
EOF
```
