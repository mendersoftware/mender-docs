---
title: Production installation with Kubernetes
taxonomy:
    category: docs
    label: tutorial
---

!!! You can save time by using [hosted Mender](https://hosted.mender.io?target=_blank), a secure Mender Server ready to use, maintained by the Mender developers.


This section is a step by step tutorial for deploying the Mender Server for production
environments, and will cover relevant security and reliability aspects of Mender
production installations.  Most of the steps are the same whether you are installing
the Open Source or Enterprise edition of the Mender Server, but some extra are
are highlighted for the latter.

You will use the [Helm chart](https://github.com/mendersoftware/mender-helm) to
deploy to production the Mender backend services on a Kubernetes cluster.

Please read the following Requirements and resources section to understand what combinations are validated by Northern.tech.

## Requirements and resources

The requirements listed below are what Northern.tech tests internally and supports for production installations of the mender server. Alternative providers might technically work as well, but are not officially supported.

### Hardware Requirements
Here are the hardware requirements for the Mender Server (excluding the
database and artifact storage requirements):

!! Currently, the MongoDB setup included in the Helm Chart  only supports x86_64
!! architecture. If you want to use arm64, you will need to set up an external
!! MongoDB cluster.

* Architectures: x86_64, arm64
* small size (up to 100 devices): 8 GB RAM, 4 vCPUs
* medium size (up to 1000 devices): 16 GB RAM, 8 vCPUs
* large size (up to 100K devices): 24 GB RAM, 16 vCPUs

### Platform and software dependencies


**Artifact storage:**
* Azure blob storage
* S3 compatible:
  * AWS S3
  * Cloudflare R2
  * GCP - S3 compatible API only
  * Minio
  * SeaweedFS


**Mongo DB:**
Mender supports MongoDB in both Standalone (single node) and Replica set mode.
We recommend using a replica set for high availability production environments,
and you can choose to host your own cluster or use the MongoDB Atlas managed
service.
* Supported versions:
  * MongoDB 7.0
  * MongoDB 6.0

!!!!! Please note that we do not provide support for troubleshooting issues with
!!!!! MongoDB not directly related to the Mender product.

**Redis:**
* Redis 6.0, 6.2, 7.4
  * ElasticCache (AWS)
  * AzureCache
  * Memorystore (GCP)
  * Self hosted

**Nats:**
* NATS 2.9

**Whatever the supported Kubernetes version for:**
* [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/)
* [Azure Kubernetes Service (AKS)](https://azure.microsoft.com/en-au/services/kubernetes-service/)
* [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine/)
    * *Autopilot* not yet supported

**Helm CLI version:**
* 3.10

### Resources

To deploy a production-grade Mender Server, you will need Kubernetes worker nodes providing
at least 4 GB of RAM, 4 vCPUs and 10 GB for the persistent volumes.

The Mender backend is available for the x86 and arm64 architecture only.
