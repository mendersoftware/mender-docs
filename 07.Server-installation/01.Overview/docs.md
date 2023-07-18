---
title: Overview
taxonomy:
    category: docs
---

!!! For evaluation of the on-premise installation of the Mender Enterprise Server please [contact us](https://mender.io/contact-us). In the message please mention'Evaluation of the on-prem Enterprise Mender'.


Mender backend is composed of a number of microservices, each implementing a
small, well defined piece of functionality. Services are delivered in form of Docker images, available from official [Mender Docker repository](https://hub.docker.com/r/mendersoftware/?target=_blank). When required, each service can be built directly from its source code.


## Chapter structure

For the quickest way to a working local server with default configuration and keys, please read the [Evaluation](../02.Evaluation/docs.md) section. By following a list of copy-pastable steps you will end with a working server environment of your computer.

On a running mender server instance the microservices communicate together and have been set up with the correct configurations and keys. To know more about the details on the architecture and configuration please read the [Architecture](01.Architecture/docs.md) and [Certificates and keys](02.Certificates-and-keys/docs.md).

For production installations please follow the setup described in [Production installation with Kubernetes](../04.Production-installation-with-kubernetes/docs.md). It describes how to set up a scalable mender server installation in on of the big cloud providers.

## Support

[Support](https://mender.io/support) covered by the Enterprise plan is valid for:

* production versions installed with kubernetes
* component versions as defined under [Production installation with Kubernetes](../04.Production-installation-with-kubernetes/docs.md)

Following the above points will ensure a simplest working production installation regardless of the Opens Source or Enterprise server.

!!!!! Please note that the Mender Server containers comes released as part of the [Mender Product bundle](../../302.Release-information/01.Release-schedule/docs.md) and falls under the support schedule explained there.
