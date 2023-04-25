---
title: Overview
taxonomy:
    category: docs
---

Mender backend is composed of a number of microservices, each implementing a
small, well defined piece of functionality.

Services are delivered in form of Docker images, available from
official [Mender Docker repository](https://hub.docker.com/r/mendersoftware/?target=_blank).
When required, each service can be built directly from its source code. Consult
respective repositories for build instructions.


!!!!! For evaluation of the on premise installation of the Mender Enterprise Server please [contact us](https://mender.io/contact-us).
!!!!! In the message please mention the 'Evaluation of the on-prem Enterprise Mender'.


## Installation

The quickest way to evaluate an on-premise Mender Server is using the installation with Docker Compose.
This allows you to spin up an on-prem instance without worrying about too much configuration up front.

For production installations the setup with kubernetes is the recommended path.


## Support

[Support](https://mender.io/support) covered by the Enterprise plan is valid for:

* production versions installed with kubernetes
* component versions as defined under [Production installation with Kubernetes](../04.Production-installation-with-kubernetes/docs.md)

Following the above points will ensure a simplest working production installation regardless of the Opens Source or Enterprise server.

!!!!! Please note that the Mender Server containers comes released as part of the [Mender Product bundle](../../302.Release-information/01.Release-schedule/docs.md) and falls under the support schedule explained there.


