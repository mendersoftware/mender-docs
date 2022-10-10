---
title: Production installation with Kubernetes
taxonomy:
    category: docs
    label: tutorial
routes:
    canonical: /3.4/server-installation/production-installation-with-kubernetes
---

!!! You can save time by using [hosted Mender](https://hosted.mender.io?target=_blank), a secure Mender server ready to use, maintained by the Mender developers.

This is a step by step tutorial for deploying the Mender Server for production
environments, and will cover relevant security and reliability aspects of Mender
production installations.  Most of the steps are the same whether you are installing
the Open Source or Enterprise edition of the Mender Server, but some extra are
are highlighted for the latter.

You will use the [Helm chart](https://github.com/mendersoftware/mender-helm) to 
deploy to production the Mender backend services on a Kubernetes cluster.

## Index

* Prerequisites:
  * [Kubernetes](../04.Production-installation-with-kubernetes/01.Kubernetes/docs.md)
  * [Helm](../04.Production-installation-with-kubernetes/01.Kubernetes/docs.md#installation-of-helm)
* External services:
  * [MongoDB](../04.Production-installation-with-kubernetes/02.MongoDB/docs.md)
  * [NATS](../04.Production-installation-with-kubernetes/03.NATS/docs.md)
  * [S3-compatible storage layer](#s3-compatible-storage-layer)
* [Mender Server](../04.Production-installation-with-kubernetes/05.Mender-server/docs.md)

### S3-compatible storage layer

Mender stores the artifacts into an S3 API-compatible storage layer. You can provide an AWS S3
bucket or install and expose a storage service providing S3-compatible APIs over the internet.

The following open-source projects are compatible with the S3 APIs:

* [Minio](https://github.com/chrislusf/seaweedfs)
* [SeaweedFS](https://github.com/chrislusf/seaweedfs)
* [Leofs](https://github.com/leo-project/leofs)

To get started, see the instructions on [how to install Minio](../04.Production-installation-with-kubernetes/04.Minio/docs.md).
