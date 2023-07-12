---
title: Architecture
taxonomy:
    category: docs
---

!!! The Enterprise server runs different versions of the containers providing the enterprise features.
!!! For evaluation of the Mender Enterprise Server please [contact us](https://mender.io/contact-us) to gain access to the enterprise containers.

The architecture below shows the Open Source Mender Server case set up with the docker-compose evaluation.


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

Services are delivered as Docker images, available from the
official [Mender Docker repository](https://hub.docker.com/r/mendersoftware/?target=_blank).
When required, each service can be built directly from its source code. Consult the
respective repositories for build instructions.
