---
title: Overview
taxonomy:
    category: docs
---

Mender backend is composed of a number of microservices, each implementing a
small, well defined piece of functionality.

The integration environment brings together the following services:

- [Mender Device Authentication Service](https://github.com/mendersoftware/deviceauth?target=_blank)
- [Mender Device Configuration Service](https://github.com/mendersoftware/deviceconfig?target=_blank)
- [Mender Device Connect Service](https://github.com/mendersoftware/deviceconnect?target=_blank)
- [Mender Device Monitor Service](https://github.com/mendersoftware/devicemonitor?target=_blank)
- [Mender Deployments Service](https://github.com/mendersoftware/deployments?target=_blank)
- [Mender Device Inventory Service](https://github.com/mendersoftware/inventory?target=_blank)
- [Mender User Administration Service](https://github.com/mendersoftware/useradm?target=_blank)
- [Mender Workflows Service](https://github.com/mendersoftware/workflows?target=_blank)
- [Mender Reporting Service](https://github.com/mendersoftware/reporting?target=_blank)
- [Mender Create Artifact Worker](https://github.com/mendersoftware/create-artifact-worker?target=_blank)
- API Gateway based on [Traefik](https://doc.traefik.io/traefik/?target=_blank)
- [Minio](https://www.minio.io?target=_blank) object storage
- [NATS.io](https://nats.io?target=_blank) messaging system
- [OpenSearch](https://www.opensearch.org?target=_blank) storage and search engine

Services are delivered in form of Docker images, available from
official [Mender Docker repository](https://hub.docker.com/r/mendersoftware/?target=_blank).
When required, each service can be built directly from its source code. Consult
respective repositories for build instructions.

While it is possible to `docker pull` individual images and start containers
manually,
the [integration repository](https://github.com/mendersoftware/integration?target=_blank)
provides a convenient setup based on Docker Compose tool. The
`docker-compose.yml` file describes the following setup:

```
        |
        |                                            +-------------------------+
        |                                            |                         |
        |                                       +--->|  Device Authentication  |<---+
        |                                       |    |  (mender-device-auth)   |    |
        |                                       |    +-------------------------+    |
        |        +-----------------------+      |    |                         |    |
   port |        |                       |      +--->|  Inventory              |<---+     +----------------------------------+
    443 | <----> |  API Gateway          |      |    |  (mender-inventory)     |    +---> |  Workflows Engine                |
        |        |  (Traefik)            |<-----+    +-------------------------+    |     |  (mender-workflows-server)       |
        |        +-----------------------+      |    |                         |    |     |  (mender-workflows-worker)       |
        |                                       +--->|  User Administration    |    |     |  (mender-create-artifact-worker) |
        |                                       |    |  (mender-useradm)       |<---+     +----------------------------------+
        |                                       |    +-------------------------+    |
        |                                       +--->|                         |    |
        |                                       |    |  Device Config          |<---+
        |                                       |    |  (mender-deviceconfig)  |    |
        |                                       |    +-------------------------+    |
        |                                       +--->|                         |    |
        |                                       |    |  Deployments            |<---+
        |                                       |    |  (mender-deployments)   |    |
        |                                       |    +-------------------------+    |
        |                                       +--->|                         |    |
        |                                       |    |  Reporting              |<---+
        |                                       |    |  (mender-reporting)     |    |
        |                                       |    +-------------------------+    |
        |                                       +--->|                         |    |
        |                                       |    |  IoT Manager            |<---+
        |                                       |    |  (mender-iot-manager)   |    |
        |                                       |    +-------------------------+    |
        |                                       +--->|                         |    |
        |                                       |    |  Device Monitor         |<---+
        |                                       |    |  (mender-devicemonitor) |    |
        |                                       |    +-------------------------+    |
        |                                       +--->|                         |<---+
        |                                       |    |  Device Connect         |          +--------+
        |                                       |    |  (mender-deviceconnect) |<-------->|        |
        |                                       |    +-------------------------+          |  Nats  |
        |                                       +--->|                         |          |        |
        |                                            |  Minio                  |          +--------+
        |                                            |                         |
        |                                            +-------------------------+
        |
```

# Cloud system requirements

A cloud solution can be deployed on a variety of different cloud infrastructures.
The simplest path to a working on premise Mender server instance is deploying it on the cloud system requirements with which we test with.

! Enterprise support only covers on-prem installations on the cloud system requirements defined here


<TODO: Fill with what we test on-prem>
<TODO: Needs to be defined starting from 3.3 and 3.4>
