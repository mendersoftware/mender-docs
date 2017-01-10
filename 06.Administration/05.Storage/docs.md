---
title: Storage
taxonomy:
    category: docs
---

Deployments service stores mender artifact in a S3 compatible object store. This
gives the end use a flexibility in using either an own storage (default setup)
or 3rd party services like Amazon's S3.

## Minio artifact storage

Minio service is configured to use `/export` directory as its storage location.
It is possible to define a volume that mounts a local directory into the service
container:

```
    mender-deployments:
        volumes:
            - /my/storage/location:/export
```

## S3 storage backend

It is possible to use S3 as a storage backend in place of Minio object storage.
This can be achieved using a separate compose file with the following entry:

```
    mender-deployments:
        environment:
            AWS_ACCESS_KEY_ID: <your-aws-access-key-id>
            AWS_SECRET_ACCESS_KEY: <your-aws-secret-access-key>
            AWS_URI: https://s3.amazonaws.com
```
