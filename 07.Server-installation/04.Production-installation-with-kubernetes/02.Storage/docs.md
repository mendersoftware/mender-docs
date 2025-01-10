---
title: Storage
taxonomy:
    category: docs
    label: tutorial
---

Mender requires an S3-compatible storage backend to store artifacts.
You can choose from a variety of S3-compatible storage solutions, based on your
requirements and infrastructure.

Production-grade S3-compatible storage solutions include:
* Amazon S3
* Google Cloud Storage
* Cloudflare R2 Storage

Mender also supports the following proprietary storage solutions:
* Azure Blob Storage

For evaluation, development, and testing purposes, you can use self-hosted,
open-source S3-compatible storage solutions. You can refer to the provider 
documentation for more information on how to install and configure the storage
solution that best fits your needs.

[ui-tabs position="top-left" active="0" theme="default" ]
[ui-tab title="Open Source"]

<!--AUTOVERSION: "! the version %"/ignore -->
! Until now, MinIO has been the default storage backend documented for
! Mender. However, the original MinIO setup using Helm has been removed from
! the documentation, as it is no longer functional as documented with
! the version 4.1.7 of the MinIO Operator. SeaweedFS is now the new
! default storage backend for the full Open Source setup from the Helm Chart
! version 6.x and later. If you whish to continue using MinIO, please consult
! the [official MinIO documentation](https://docs.min.io/) for further
! information.
! If you wish to switch to SeaweedFS, we provide a short
! [migration guide](#migration-from-minio) after installing SeaweedFS.

!! Important: The SeaweedFS setup is a community project and is not
!! recommended for production use. The following storage backends are
!! recommended for production: AWS S3, Cloudflare R2,
!! Google Cloud Storage,and Azure Blob Storage.

!! Important: The object storage provider has to be resolvable both
!! internally and externally. If you are using a private IP address,
!! you must ensure DNS resolution is working correctly.
!! For k3s, you could add this entry to the CoreDNS ConfigMap:
!! ```yaml
!!     mender.example.com:53 {
!!      errors
!!      cache 30
!!      hosts {
!!        <ip address of your machine> mender.example.com
!!      }
!!    }
!! ```
!! Note, the TLS certificate for the host `mender.example.com`
!! must be valid and trusted by clients.
!! For more information, visit the [Certificate and keys section](../../01.Overview/02.Certificates-and-keys/docs.md)

In this guide, we provide an example of how to install SeaweedFS and
integrating it into Mender.

<!--AUTOVERSION: "! Please refer to the [official SeaweedFS Helm Chart](https://github.com/seaweedfs/seaweedfs/blob/%"/ignore -->
! By default, SeaweedFS is configured to run on `amd64` nodes. To run it on
! `arm64`, you have to tweak the `nodeSelector` keys of the services.
! Please refer to the [official SeaweedFS Helm Chart](https://github.com/seaweedfs/seaweedfs/blob/master/k8s/charts/seaweedfs/values.yaml)

```bash
export STORAGE_CLASS="default"
export STORAGE_BUCKET="replace-with-your-bucket-name"

cat >seaweedfs.yml <<EOF
filer:
  s3:
    enabled: true
    enableAuth: true
    createBuckets:
      - name: "${STORAGE_BUCKET}"
  storageClass: ${STORAGE_CLASS}

s3:
  enabled: true
  enableAuth: true
EOF

helm repo add seaweedfs https://seaweedfs.github.io/seaweedfs/helm
helm repo update
helm install seaweedfs --wait -f seaweedfs.yml  seaweedfs/seaweedfs

```
Finally, export the following environment variables, needed for installing
Mender in the later steps:

```bash
export AWS_ACCESS_KEY_ID=$(kubectl get secret seaweedfs-s3-secret -o jsonpath='{.data.admin_access_key_id}' |base64 -d)
export AWS_SECRET_ACCESS_KEY=$(kubectl  get secret seaweedfs-s3-secret -o jsonpath='{.data.admin_secret_access_key}' |base64 -d)
export AWS_REGION="us-east-1"
export STORAGE_ENDPOINT="http://seaweedfs-s3:8333"
```

!!! You can inspect the SeaweedFS installation by running the following:
!!! ```bash
!!! kubectl port-forward svc/seaweedfs-s3 8333:8333 &
!!! aws s3 ls --endpoint-url="http://localhost:8333"
!!! ```

Please refer to the
[SeaweedFS official documentation](https://github.com/seaweedfs/seaweedfs)
for further information about setting up a SeaweedFS deployment.

## Migration from MinIO
If you are currently using MinIO as the storage backend for Mender, you can
migrate to SeaweedFS by following these steps:
```
# export data from MinIO
export AWS_ACCESS_KEY_ID="<your minio access key>"
export AWS_SECRET_ACCESS_KEY="<your minio secret key>"

mkdir mender-artifact-storage
# Tip: make sure you have enough disk space to store the data

aws s3 cp --recursive --endpoint-url=<your minio endpoint> s3://mender-artifact-storage/ ./mender-artifact-storage/

# import data to SeaweedFS
export AWS_ACCESS_KEY_ID=$(kubectl get secret seaweedfs-s3-secret -o jsonpath='{.data.admin_access_key_id}' |base64 -d)
export AWS_SECRET_ACCESS_KEY=$(kubectl  get secret seaweedfs-s3-secret -o jsonpath='{.data.admin_secret_access_key}' |base64 -d)

kubectl port-forward svc/seaweedfs-s3 8333:8333
aws s3 cp --recursive ./mender-artifact-storage/ --endpoint-url=http://localhost:8333 s3://mender-artifact-storage/
```

[/ui-tab]
[ui-tab title="Amazon S3"]
In this guide, we provide an example of how to use Amazon S3 
as a Mender Artifact Storage.

Create a new bucket in Amazon S3, then a IAM user and its access key with
the proper permissions to access the bucket.

You can find the required permissions in the
[Requirements section](../../../02.Overview/17.Requirements/docs.md#amazon-s3-iam-policies)

Then, export the following environment variables:

```bash
export AWS_ACCESS_KEY_ID="replace-with-your-access-key-id"
export AWS_SECRET_ACCESS_KEY="replace-with-your-secret-access-key"
export AWS_REGION="replace-with-your-aws-region"
export STORAGE_BUCKET="replace-with-your-bucket-name"
export STORAGE_ENDPOINT="https://s3.${AWS_REGION}.amazonaws.com"
```

Alternatively, you can configure and use a Service Account to access the bucket.

```bash
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_SERVICE_ACCOUNT_NAME="replace-with-your-service-account-name"
export AWS_REGION="replace-with-your-aws-region"
export STORAGE_BUCKET="replace-with-your-bucket-name"
export STORAGE_ENDPOINT="https://s3.${AWS_REGION}.amazonaws.com"
```

As a reference, here's your Helm Chart customization to make
Mender use Amazon S3 as the storage backend:

```yaml
global:
  s3:
    AWS_URI: "https://s3.<your-aws-region>.amazonaws.com"
    AWS_BUCKET: "<name-of-your-bucket>"
    AWS_REGION: "<your-aws-region>"
    AWS_ACCESS_KEY_ID: "<your-access-key-id>"
    AWS_SECRET_ACCESS_KEY: "<your-secret-access-key>"
    AWS_FORCE_PATH_STYLE: "false"
```

With a Service Account:
```yaml
global:
  s3:
    AWS_SERVICE_ACCOUNT_NAME: "<service-account-name>"
    AWS_URI: "https://s3.<your-aws-region>.amazonaws.com"
    AWS_BUCKET: "<name-of-your-bucket>"
    AWS_REGION: "<your-aws-region>"
    AWS_FORCE_PATH_STYLE: "false"
```

[/ui-tab]
[ui-tab title="Azure Blob Storage"]
In this guide, we provide an example of how to use Azure
Blob Storage as a Mender Artifact storage.

Create a new Storage Account in Azure Blob Storage, then a
Storage Container in the Storage Account.

As a reference, here's your Helm Chart customization to make
Mender use Azure Blob Storage as the storage backend:

```yaml
global:
  storage: "azure"
  azure:
    AUTH_CONNECTION_STRING: "BlobEndpoint=https://<name-of-your-storage>.blob.core.windows.net;SharedAccessSignature=..."
    CONTAINER_NAME: "<name-of-your-container>"
```

[/ui-tab]
[ui-tab title="Cloudflare R2"]
In this guide, we provide an example of how to use Cloudflare
R2 Storage as a Mender Artifact storage.

Create a new Storage Bucket in Cloudflare R2, then 
create an API Token with Object Read & Write
permission on the Bucket.

```bash
export AWS_ACCESS_KEY_ID="replace-with-your-access-key-id"
export AWS_SECRET_ACCESS_KEY="replace-with-your-secret-access-key"
export AWS_REGION="replace-with-your-aws-region"
export STORAGE_BUCKET="replace-with-your-bucket-name"
export STORAGE_ENDPOINT="https://replace-with-your-cloudflare-account-id.r2.cloudflarestorage.com"
```

[/ui-tab]
[/ui-tabs]
