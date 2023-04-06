---
title: OpenSearch
taxonomy:
    category: docs
    label: tutorial
---

The Mender Server uses OpenSearch as a storage and search engine.

Opensearch is configured as a Mender sub-chart and it's enabled by default.
You can disable it by overriding its settings in your custom `values.yaml`:

```
opensearch:
  enabled: false
```

To install OpenSearch on a Kubernetes cluster using the Helm chart follow instructions from [Opensearch using `helm`](https://opensearch.org/docs/2.4/install-and-configure/install-opensearch/helm/):

<!--AUTOVERSION: "helm install opensearch opensearch/opensearch --version %"/ignore -->
```bash
$ helm repo add opensearch https://opensearch-project.github.io/helm-charts/
$ helm repo update
$ export OPENSEARCH_CONFIG=$(cat <<EOF
cluster.name: opensearch-cluster
network.host: 0.0.0.0
plugins.security.disabled: true
EOF
)
$ helm install opensearch opensearch/opensearch --version 2.9.0 --set "config.opensearch\\.yml=$OPENSEARCH_CONFIG"
```
