---
title: NATS
taxonomy:
    category: docs
    label: tutorial
---

The Mender server uses NATS as message broker.

To install NATS on the Kubernetes cluster using the [NATS Helm Chart](https://nats-io.github.io/k8s/),
for example deploying a cluster with two NATS servers, run:

<!--AUTOVERSION: "image: \"nats:%-alpine\""/ignore -->
```bash
cat >nats.yml <<EOF
cluster:
  enabled: true
  replicas: 2
nats:
  image: "nats:2.3.1-alpine"
  jetstream:
    enabled: true

    memStorage:
      enabled: true
      size: "1Gi"

    fileStorage:
      enabled: true
      size: "2Gi"
      storageDirectory: /data/
EOF

helm repo add nats https://nats-io.github.io/k8s/helm/charts/
helm repo update
helm install nats nats/nats --version 0.8.2 -f nats.yml
```

The connection string to connect to your NATS cluster will be:

> ```
> nats://nats:4222
> ```

Please refer to the [NATS official documentation](https://docs.nats.io/) for
further information about setting up a production-grade NATS deployment.
