---
title: Production installation
taxonomy:
    category: docs
---

Mender backend services can be deployed to production using a skeleton
provided in integration repository.

## Prerequisites

Before a Docker based setup can be made available, the services need to be
provided with required certificate, keys or configuration.

!!! It is recommended to use a separate `docker-compose` file for injecting deployment specific overrides and configuration. Consult [Using Compose in production](https://docs.docker.com/compose/production/) guide for details.

## Demo configuration

A `docker-compose.demo.yml` file provides example overrides and configuration
for demo backend setup. This file can be used as reference for preparing a
production deployment.

Demo overlay sets up:

- token signing keys `keys/deviceauth-private.pem` and
  `keys/useradm-private.pem`, mounts both keys to respective services
- API Gateway certificate and key from `ssl/mender-api-gateway/cert.pem` and
  `ssl/mender-api-gateway/key.pem`
- storage proxy certificate and key from `ssl/storage-proxy/s3.docker.mender.io.crt` and
  `ssl/storage-proxy/s3.docker.mender.io.key`
- makes storage proxy certificate available to `mender-deployments` service

