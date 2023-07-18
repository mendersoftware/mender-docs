---
title: Requirements and support
taxonomy:
    category: docs
    label: tutorial
---


The requirements listed below are what Northern.tech tests internally and supports for production installations of the mender server. 
Alternative versions or configurations might technically work, but are not officially supported.

### Application requirements

This refers to the specific versions of software that are required to ensure compatibility and optimal functioning of the microservices in your setup.
It represents the most 'bare-bones' set of requirements which is a necessary but not sufficient condition required to run a full production installation. 
Once can ensure the versions defined here, please move forward to the kubernetes configuration requirements.



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

    
### Kubernetes configuration requirements

!! **Please note:** In the evaluation chapter, we set up these services as part of the Mender Server to assure a quick path to a working demo setup. The same approach isn't supported for production environments. 

For production setup, the Mender server depends on available and auto scalable external service. 
The following are expected to be externally provided:
* NATS
* MongoDB
* Artifact storage


#### Hardware resources

To deploy a production-grade Mender Server, you will need Kubernetes worker nodes providing
at least 4 GB of RAM, 4 vCPUs and 10 GB for the persistent volumes.

The Mender backend is available for the x86 architecture only.


