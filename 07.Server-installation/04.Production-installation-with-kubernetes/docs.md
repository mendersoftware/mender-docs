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

### Platform and software dependencies


**Artifact storage:**
* Azure blob storage
* S3 compatible:
  * AWS S3
  * Cloudflare R2
  * GCP - S3 compatible API only
  * Minio


**Mongo DB:**
Mender supports MongoDB in both Standalone (single node) and Replica set mode.
We recommend using a replica set for high availability production environments,
and you can choose to host your own cluster or use the MongoDB Atlas managed
service.
* Supported versions:
  * MongoDB 5.0
  * MongoDB 4.4

!!!!! Please note that we do not provide support for troubleshooting issues with
!!!!! MongoDB not directly related to the Mender product.

**Redis:**
* Redis 6.0, 6.2
  * ElasticCache (AWS)
  * AzureCache
  * Memorystore (GCP)
  * Self hosted

**Nats:**
* NATS 2.7, 2.8, 2.9

**Whatever the supported Kubernetes version for:**
* [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/)
* [Azure Kubernetes Service (AKS)](https://azure.microsoft.com/en-au/services/kubernetes-service/)
* [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine/)
    * *Autopilot* not yet supported

**Helm CLI version:**
* 3.7

### Resources

To deploy a production-grade Mender Server, you will need Kubernetes worker nodes providing
at least 4 GB of RAM, 4 vCPUs and 10 GB for the persistent volumes.

The Mender backend is available for the x86 architecture only.
