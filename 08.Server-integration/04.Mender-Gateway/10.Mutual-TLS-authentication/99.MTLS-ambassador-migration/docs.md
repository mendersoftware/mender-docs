---
title: MTLS Ambassador migration guide
taxonomy:
    category: docs
---

This guide will take you through the process of migrating from the deprecated Mender mTLS Ambassador to Mender Gateway which is drop-in replacement.

## Prerequisites
1. You have a running `mender-mtls` deployment based on the Ambassador.
2. You have the required key and certificate files previously used for the ambassador.
3. You have a DNS name pointing to the `mender-mtls` service.

## Migration steps
### 1. Install Mender Gateway
Follow the [Production installation with Kubernetes guide](../03.Production-installation-with-kubernetes/docs.md) to install the Mender Gateway with mTLS support.

The new kubernetes deployment will be named `mender-mtls-gateway`.

!!!!! Make sure to use the same keys and certificates that you used for the `mender-mtls` deployment.

### 2. Verify the Load Balancer is deployed
Depending on your cloud provider, you should have a L4 Load Balancer deployed in front of the Mender Gateway service.
Take a note of the Load Balancer's IP address or DNS name.

### 3. Update your fleet DNS
Update your DNS record to point to the new Load Balancer IP address or DNS name of the Mender Gateway service.

### 4. Verification
Verify that your devices are still able to connect to the Mender Server using the new Load Balancer and the Mender Gateway service.

### 5. Cleanup
You can now cleanup the old `mender-mtls` deployment, service, and Load Balancer resources.

