---
title: Architecture
taxonomy:
    category: docs
---

!!! The Enterprise server runs different versions of the containers providing the enterprise features.
!!! For evaluation of the Mender Enterprise server please [contact us](https://mender.io/contact-us) to gain access to the enterprise containers.

The diagram below shows the different services which are part of the Mender Server architecture:

```
        |
        |                                            +-------------------------+
        |                                            |                         |
        |                                       +--->|  Device Authentication  |<---+
        |                                       |    |  (mender-deviceauth)    |    |
        |                                       |    +-------------------------+    |
        |        +-----------------------+      |    |                         |    |
   port |        |                       |      +--->|  Inventory              |<---+     +----------------------------------+
    443 | <----> |  API Gateway          |      |    |  (mender-inventory)     |    +---> |  Workflows Engine                |
        |        |  (Traefik)            |<-----+    +-------------------------+    |     |  (mender-workflows-server)       |
        |        +-----------------------+      |    |                         |    |     |  (mender-workflows-worker)       |
        |                                       +--->|  User Administration    |    |     |  (mender-create-artifact-worker) |
        |                                       |    |  (mender-useradm)       |<---+     |  *(mender-generate-delta-worker) |
        |                                       |    +-------------------------+    |     +----------------------------------+
        |                                       +--->|                         |    |
        |                                       |    |  Device Config          |<---+
        |                                       |    |  (mender-deviceconfig)  |    |
        |                                       |    +-------------------------+    |
        |                                       +--->|                         |    |
        |                                       |    |  Deployments            |<---+
        |                                       |    |  (mender-deployments)   |    |
        |                                       |    +-------------------------+    |
        |                                       +--->|                         |    |
        |                                       |    |  IoT Manager            |<---+
        |                                       |    |  (mender-iot-manager)   |    |
        |                                       |    +-------------------------+    |
        |                                       +--->|                         |    |
        |                                       |    |  * Auditlogs            |<---+
        |                                       |    |  (mender-auditlogs)     |    |
        |                                       |    +-------------------------+    |
        |                                       +--->|                         |    |
        |                                       |    |  * Tenant Admin.        |<---+
        |                                       |    |  (mender-tenantadm)     |    |
        |                                       |    +-------------------------+    |
        |                                       +--->|                         |    |
        |                                       |    |  * Device Monitor       |<---+
        |                                       |    |  (mender-devicemonitor) |    |
        |                                       |    +-------------------------+    |
        |                                       +--->|                         |<---+
        |                                       |    |  Device Connect         |          +--------+
        |                                       |    |  (mender-deviceconnect) |<-------->|        |
        |                                       |    +-------------------------+          |  Nats  |
        |                                       +--->|                         |          |        |
        |                                            |  SeaweedFS              |          +--------+
        |                                            |                         |
        |                                            +-------------------------+
        |

* Enterprise-only components
```

The Mender Server environment includes the following services:

- [Mender Create Artifact Worker](https://github.com/mendersoftware/mender-server/tree/main/backend/services/create-artifact-worker/?target=_blank)
- [Mender Deployments Service](https://github.com/mendersoftware/mender-server/tree/main/backend/services/deployments/?target=_blank)
- [Mender Device Authentication Service](https://github.com/mendersoftware/mender-server/tree/main/backend/services/deviceauth/?target=_blank)
- [Mender Device Configuration Service](https://github.com/mendersoftware/mender-server/tree/main/backend/services/deviceconfig/?target=_blank)
- [Mender Device Connect Service](https://github.com/mendersoftware/mender-server/tree/main/backend/services/deviceconnect/?target=_blank)
- [Mender Device Inventory Service](https://github.com/mendersoftware/mender-server/tree/main/backend/services/inventory/?target=_blank)
- [Mender IoT Manager Service](https://github.com/mendersoftware/mender-server/tree/main/backend/services/iot-manager/?target=_blank)
- [Mender Reporting Service](https://github.com/mendersoftware/mender-server/tree/main/backend/services/reporting/?target=_blank)
- [Mender User Administration Service](https://github.com/mendersoftware/mender-server/tree/main/backend/services/useradm/?target=_blank)
- [Mender Workflows Service](https://github.com/mendersoftware/mender-server/tree/main/backend/services/workflows/?target=_blank)
- API Gateway based on [Traefik](https://doc.traefik.io/traefik/?target=_blank)
- [SeaweedFS](https://github.com/seaweedfs/seaweedfs?target=_blank) object storage
- [NATS.io](https://nats.io?target=_blank) messaging system
- [OpenSearch](https://www.opensearch.org?target=_blank) storage and search engine

The Mender Enterprise Server includes different implementations of some of the
services, as well as some Enterprise-specific services. These are closed source.

- Mender Auditlogs Service
- Mender Create Artifact Worker
- Mender Deployments Service
- Mender Device Authentication Service
- Mender Device Configuration Service
- Mender Device Connect Service
- Mender Device Monitor Service
- Mender Generate Delta Worker
- Mender Device Inventory Service
- Mender IoT Manager Service
- Mender Reporting Service
- Mender Tenant Administration Service
- Mender User Administration Service
- Mender Workflows Service

Services are delivered as Docker images, available from the official
[Mender Docker repository](https://hub.docker.com/r/mendersoftware/?target=_blank).
When required, each service can be built directly from its source code. Consult the
[mender-server](https://github.com/mendersoftware/mender-server) repository for
build instructions.
