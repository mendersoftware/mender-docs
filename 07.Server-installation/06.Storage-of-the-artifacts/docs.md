---
title: Storage of the artifacts
taxonomy:
    category: docs
    label: tutorial
routes:
    canonical: /3.4/server-installation/storage-of-the-artifacts
---

The Deployments service stores Mender artifacts in an S3 compatible object-store. This
gives the end-user flexibility in using either their storage proxy based on
[Minio](https://min.io/), the default setup, or 3rd party services such as Amazon S3.

When using an AWS S3 bucket, it is possible to configure the Deployments service to use
AWS specific settings, among the others:

* Specify the AWS S3 bucket's region
* Enable the [S3 Transfer Acceleration](https://aws.amazon.com/s3/transfer-acceleration/)

The list of the main storage-related settings for the Deployments service,
both as environment variables and config file keys, follows:

### `DEPLOYMENTS_AWS_REGION` (`aws.region`)

The AWS region the S3 bucket is located in. For Minio, this value should be
set to `us-east-1`.

Default: `us-east-1`

### `DEPLOYMENTS_AWS_BUCKET` (`aws.bucket`)

The name of the S3 bucket used to store the artifacts. For Minio, the bucket is
automatically created at start-up.

Default: `mender-artifact-storage`

### `DEPLOYMENTS_AWS_FORCE_PATH_STYLE` (`aws.force_path_style`)

AWS S3 supports two different URI styles:

* virtual-hosted (https://bucket-name.s3.region.amazonaws.com/key)
* path-style (https://s3.region.amazonaws.com/bucket-name/key)

Buckets created after September 30, 2020, will support only virtual
hosted-style requests. Path-style requests will continue to be supported
for buckets created on or before this date.

When Minio (or alternative S3 implementations) is in use, path
style URI are used.

Default: `true`

### `DEPLOYMENTS_AWS_USE_ACCELERATE` (`aws.use_accelerate`)

If set to `true`, it enables the S3 Transfer Acceleration for the operations
that support it. The AWS S3 Bucket must have the S3 Transfer Acceleration feature enabled.

Default: `false`

### `DEPLOYMENTS_AWS_URI` (`aws.uri`)

The URI to the S3 storage service. 

When using AWS S3, set to `https://s3.amazonaws.com` for the `us-east-1` region, and `https://s3.region.amazonaws.com` for the
other AWS regions. For example, for AWS S3 buckets located in Frankfurt, set to
`https://s3.eu-central-1.amazonaws.com`.

When using Minio, set to the URI Minio is exposed to the internet. Please note that the domain and protocol used to access the storage service are the
same used by the devices to download the artifacts, and the host name is included in the URL presigning algorithm. You can optionally
install a CDN in front of your Minio instance, and in this case you can use your CDN URL for this setting.

Default: `https://s3.amazonaws.com`

### `DEPLOYMENTS_AWS_ACCESS_KEY_ID` and `DEPLOYMENTS_AWS_AUTH_SECRET` (`aws.auth.key` and `aws.auth.secret`)

The credentials to access the S3 storage service.

If you are running Mender on an AWS EC2 instance, you can leave these settings empty
if a proper instance profile is attached to the EC2 instance: the service will default
to retrieving authentication credentials locally from the AWS IAM role assigned to the
EC2 instance. Please refer to the official AWS documentation for further details.

## Using Minio to store the artifacts

When using Minio, you have to specify the access key ID and the access secret key
setting the `MINIO_ACCESS_KEY` and `MINIO_SECRET_KEY` environment variables:

```yaml
minio:
    ...
    environment:
        MINIO_ACCESS_KEY: "<replace-with-random-string>"
        MINIO_SECRET_KEY: "<replace-with-another-random-string>"
```

The Minio service is configured to use the `/export` directory as its storage location.
It is possible to define a volume that mounts a local directory into the service
container:

```yaml
minio:
    ...
    volumes:
        # mount the path `/my/storage/location` as /export directory
        - /my/storage/location:/export
```

Alternatively, you can mount a preexisting Docker volume:

```yaml
minio:
    ...
    volumes:
        # mounts a docker volume named `mender-artifacts` as /export directory
        - mender-artifacts:/export:rw

volumes:
    # mender-artifacts volume
    mender-artifacts:
        # use external volume created manually
        external:
            name: mender-artifacts
```

## Using Minio Gateway to store the artifacts on third-party storage services

Minio can be used as Gateway to third-party storage services, optionally caching
the data locally. For example, using Minio Gateway, it is possible to store Mender
Artifacts on on [AWS S3](https://docs.min.io/docs/minio-gateway-for-s3.html).
Older versions supported Azure Blob Storage and Hadoop HDFS. Please refer to the
[official Minio documentation](https://docs.min.io/docs/) to configure Minio Gateway.
