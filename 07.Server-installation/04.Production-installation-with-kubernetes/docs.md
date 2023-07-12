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

Please read the Requirements page to understand what combinations are validated by Northern.tech.Once that is clear please move on the first paragraph [Kubernetes](./01.Kubernetes).


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
* MongoDB 4.4
  * Self hosted, both single node and replica set (recommended)
  * Atlas

**Redis:**
* Redis 6.0
  * ElasticCache (AWS)
  * AzureCache
  * Momory store (GCP)
  * Self hosted


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
