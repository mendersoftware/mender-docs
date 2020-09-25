---
title: Storage
taxonomy:
    category: docs
    label: tutorial
---

Deployments service stores mender artifact in a S3 compatible object store. This
gives the end user flexibility in using either their own storage proxy (which is the default setup)
or 3rd party services such as Amazon S3.

## Minio artifact storage

The minio service is configured to use the `/export` directory as its storage location.
It is possible to define a volume that mounts a local directory into the service
container:

```yaml
    minio:
        volumes:
            - /my/storage/location:/export
```

## S3 storage backend

It is possible to use S3 as a storage backend in place of Minio object storage.
This can be achieved using a separate compose file with the following entry:

```yaml
    mender-deployments:
        environment:
            DEPLOYMENTS_AWS_AUTH_KEY: <your-aws-access-key-id>
            DEPLOYMENTS_AWS_AUTH_SECRET: <your-aws-secret-access-key>
            DEPLOYMENTS_AWS_URI: https://s3.amazonaws.com
```
