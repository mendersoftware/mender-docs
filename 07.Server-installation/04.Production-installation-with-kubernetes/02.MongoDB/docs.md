---
title: MongoDB
taxonomy:
    category: docs
    label: tutorial
---

The Mender server uses MongoDB as primary storage layer. It doesn't have any particular
requirements about the setup of the database, and can use MongoDB both in a single node
setup and as a replica set.

To install MongoDB on the Kubernetes cluster using the Helm chart, for example deploying
a replica set with two members and an arbitrer using Helm, run:

!!! On the Debian family of distributions you can install `pwgen` with `apt-get install pwgen`.
!!! On the RPM family of distributions, you can install it with `yum install pwgen`.

<!--AUTOVERSION: "tag: \"%"/ignore "--version %"/ignore -->
```bash
export MONGODB_ROOT_PASSWORD=$(pwgen 32 1)
export MONGODB_REPLICA_SET_KEY=$(pwgen 32 1)

cat >mongodb.yml <<EOF
architecture: "replicaset"
replicaCount: 2
arbiter:
  enabled: true
auth:
  rootPassword: ${MONGODB_ROOT_PASSWORD}
  replicaSetKey: ${MONGODB_REPLICA_SET_KEY}
image:
  tag: "4.4.13-debian-10-r63"
persistence:
  size: "8Gi"
EOF

helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm upgrade --install mongodb bitnami/mongodb --version 13.8.1 -f mongodb.yml
```

You can get the connection string to connect to your mongodb cluster running:

```bash
echo mongodb://root:${MONGODB_ROOT_PASSWORD}@mongodb-0.mongodb-headless.default.svc.cluster.local:27017,mongodb-1.mongodb-headless.default.svc.cluster.local:27017
```

> ```
> mongodb://root:<random-password>@mongodb-0.mongodb-headless.default.svc.cluster.local:27017,mongodb-1.mongodb-headless.default.svc.cluster.local:27017
> ```

Please refer to the [MongoDB official documentation](https://docs.mongodb.com/) for
further information about setting up a production-grade MongoDB cluster.
