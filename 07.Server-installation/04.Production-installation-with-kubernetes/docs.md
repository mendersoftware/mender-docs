---
title: Production installation with Kubernetes
taxonomy:
    category: docs
    label: tutorial
---

!!! You can save time by using [hosted Mender](https://hosted.mender.io?target=_blank), a secure Mender server ready to use, maintained by the Mender developers.

!!! Hosted Mender is available in multiple [regions](/10.General/00.Hosted%20Mender%20regions/docs.md) to connect to. Make sure you select your desired one before proceeding.

This is a step by step tutorial for deploying the Mender Server for production
environments, and will cover relevant security and reliability aspects of Mender
production installations.  Most of the steps are the same whether you are installing
the Open Source or Enterprise edition of the Mender Server, but some extra are
are highlighted for the latter.

You will use the [Helm chart](https://github.com/mendersoftware/mender-helm) to 
deploy to production the Mender backend services on a Kubernetes cluster.

## System Requirements

The Mender backend supports all the
[CNCF-certified](https://landscape.cncf.io/card-mode?category=certified-kubernetes-distribution,certified-kubernetes-hosted&grouping=category)
Kubernetes distributions. We continuously test the Mender backend and the Helm
charts on the latest stable Kubernetes version and the previous one.

The following cloud distributions are validated:

- [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/)
- [Azure Kubernetes Service (AKS)](https://azure.microsoft.com/en-au/services/kubernetes-service/)
- [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine/)

The Mender backend will store the files in Persistent Volumes provisioned by Kubernetes
according to the Helm charts configurations.

To deploy a production-grade Mender backend, you will need Kubernetes worker nodes providing
at least 4 GB of RAM, 4 vCPUs and 10 GB for the persistent volumes. However, you can adjust
the memory and CPU requests to lower the requirements for development deployments and install
the Mender backend on a Kubernetes cluster with lower available resources.

The Mender backend is available for the x86 architecture only.

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
