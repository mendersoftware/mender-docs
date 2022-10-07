---
title: Overview
taxonomy:
    category: docs
routes:
    canonical: /3.3/server-installation/overview
---

Mender backend is composed of a number of microservices, each implementing a
small, well defined piece of functionality.

The integration environment brings together the following services:

- [Mender Device Authentication Service](https://github.com/mendersoftware/deviceauth?target=_blank)
- [Mender Device Configuration Service](https://github.com/mendersoftware/deviceconfig?target=_blank)
- [Mender Device Connect Service](https://github.com/mendersoftware/deviceconnect?target=_blank)
- [Mender Deployments Service](https://github.com/mendersoftware/deployments?target=_blank)
- [Mender Device Inventory Service](https://github.com/mendersoftware/inventory?target=_blank)
- [Mender User Administration Service](https://github.com/mendersoftware/useradm?target=_blank)
- [Mender Workflows Service](https://github.com/mendersoftware/workflows?target=_blank)
- [Mender Create Artifact Worker](https://github.com/mendersoftware/create-artifact-worker?target=_blank)
- API Gateway based on [Traefik](https://doc.traefik.io/traefik/?target=_blank)
- [Minio](https://www.minio.io?target=_blank) object storage
- [NATS.io](https://nats.io?target=_blank) messaging system

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
