---
title: Minio
taxonomy:
    category: docs
    label: tutorial
---

If you already have an AWS S3 bucket which you can use, you can skip this section.

The Mender Server uses an S3-compatible storage layer to store the artifacts. Please refer to the chapter [Storage of the artifacts](../../06.Storage-of-the-artifacts) for further details about the different storage options available with the Mender Server.

<!--AUTOVERSION: "https://github.com/minio/operator/tree/%/helm/minio-operator"/ignore -->
To install Minio on the Kubernetes cluster using the
[Operator Helm chart](https://github.com/minio/operator/tree/master/helm/minio-operator),
run:

<!--AUTOVERSION: "helm install minio-operator minio/minio-operator --version % -f minio-operator.yml"/ignore -->
```bash
cat >minio-operator.yml <<EOF
tenants: {}
EOF

helm repo add minio https://operator.min.io/
helm repo update
helm install minio-operator minio/minio-operator --version 4.1.7 -f minio-operator.yml

export MINIO_ACCESS_KEY=$(pwgen 32 1)
export MINIO_SECRET_KEY=$(pwgen 32 1)

cat >minio.yml <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: minio-creds-secret
type: Opaque
data:
  accesskey: $(echo -n $MINIO_ACCESS_KEY | base64)
  secretkey: $(echo -n $MINIO_SECRET_KEY | base64)
---
apiVersion: minio.min.io/v2
kind: Tenant
metadata:
  name: minio
  labels:
    app: minio
spec:
  image: minio/minio:RELEASE.2021-06-17T00-10-46Z
  credsSecret:
    name: minio-creds-secret
  pools:
    - servers: 2
      volumesPerServer: 2
      volumeClaimTemplate:
        metadata:
          name: data
        spec:
          accessModes:
            - ReadWriteOnce
          resources:
            requests:
              storage: 10Gi
          storageClassName: "local-path"
  mountPath: /export
  requestAutoCert: false
EOF

kubectl apply -f minio.yml
```

!!! Replace `local-path` with the appropriate storage class name for your Kubernetes cluster.

As devices and users will download artifacts directly from Minio, You must configure
an [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) or a
[Load Balancer](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer)
to expose it outside the Kubernetes cluster. 

For example, to expose Minio with an Ingress, run:

```bash
export MINIO_DOMAIN_NAME="artifacts.example.com"

cat >minio-ingress.yml <<EOF
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: minio-ingress
  annotations:
    cert-manager.io/issuer: "letsencrypt"
spec:
  tls:
  - hosts:
    - ${MINIO_DOMAIN_NAME}
    secretName: minio-ingress-tls
  rules:
  - host: "${MINIO_DOMAIN_NAME}"
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: minio
            port:
              number: 80
EOF

kubectl apply -f minio-ingress.yml
```

The domain name you use to expose Minio must be resolvable from the Kubernetes cluster,
because the Mender Server will use it to perform API calls to the S3 storage layer.

Please note you need to adapt the example above to your specific cluster configuration
and use case. In this example, the ingress makes use of cert-manager to issue a TLS
certificate from Let's Encrypt. 

Please refer to the [Minio official documentation](https://docs.min.io/) for
further information about setting up a production-grade Minio deployment.
