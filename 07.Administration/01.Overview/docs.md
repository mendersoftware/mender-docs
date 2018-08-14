---
title: Overview
taxonomy:
    category: docs
---

Mender backend is composed of a number of microservices, each implementing a
small, well defined piece of functionality.

The integration environment, previously used
in [Create a test environment](../../getting-started/create-a-test-environment)
chapter, brings together the following services:

- [Mender Device Authentication Service](https://github.com/mendersoftware/deviceauth?target=_blank)
- [Mender Deployment Service](https://github.com/mendersoftware/deployments?target=_blank)
- [Mender Device Inventory Service](https://github.com/mendersoftware/inventory?target=_blank)
- [Mender User Administration Service](https://github.com/mendersoftware/useradm?target=_blank)
- [Mender API Gateway](https://github.com/mendersoftware/mender-api-gateway-docker?target=_blank)
- [Minio](https://www.minio.io/?target=_blank) object storage
- Storage service proxy based on [OpenResty](https://openresty.org/en/?target=_blank)

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
        |                                       +--->|  Device Authentication  |
        |                                       |    |  (mender-device-auth)   |
        |                                       |    +-------------------------+
        |        +-----------------------+      |    |                         |
   port |        |                       |      +--->|  Inventory              |
    443 | <----> |  API Gateway          |      |    |  (mender-inventory)     |
        |        |  (mender-api-gateway) |<-----+    +-------------------------+
        |        +-----------------------+      |    |                         |
        |                                       +--->|  User Administration    |
        |                                       |    |  (mender-useradm)       |
        |                                       |    +-------------------------+
        |                                       +--->|                         |
        |                                            |  Deployments            |
        |              +---------------------------->|  (mender-deployments)   |
        |              |                             +-------------------------+
        |              |
        |              |
        |              |
        |              |
        |              v
        |        +------------------+                 +---------+
   port |        |                  |                 |         |
   9000 | <----> |  Storage Proxy   |<--------------->| Minio   |
        |        |  (storage-proxy) |                 | (minio) |
        |        +------------------+                 +---------+
        |
```

For details and best practices of using `docker-compose` in production consult
the official
documentation:
[Using Compose in production](https://docs.docker.com/compose/production/?target=_blank)
