---
title: Storage
taxonomy:
    category: docs
    label: tutorial
---

! Until now, MinIO has been the default storage backend documented for
! Mender. However, the original MinIO setup using Helm has been removed from
! the documentation, as it is no longer functional. SeaweedFS is now the new
! default storage backend for the full Open Source setup. If you whish to
! continue using MinIO, please consult the 
! [official MinIO documentation](https://docs.min.io/) for further details.

!! Important: The SeaweedFS setup is a community contribution and is not
!! recommended for production use. The following storage backends are
!! recommended for production: AWS S3, Cloudflare R2,
!! Google Cloud Storage,and Azure Blob Storage.

## Requirements
To successfully use SeaweedFS as the storage backend for Mender, you need to
ensure that the following requirements are met:

* Storage Class: The Kubernetes cluster must have a Storage Class that matches
  the one specified in the `seaweedfs.yml` file.


## Installation
To install Artifacts Storage on the Kubernetes cluster using
[SeaweedFS](https://github.com/seaweedfs/seaweedfs), run:

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

mkdir -p /tmp/mender-artifact-storage

aws s3 cp --recursive --endpoint-url=<your minio endpoint> s3://mender-artifact-storage/ /tmp/mender-artifact-storage/

# import data to SeaweedFS
export AWS_ACCESS_KEY_ID=$(kubectl get secret seaweedfs-s3-secret -o jsonpath='{.data.admin_access_key_id}' |base64 -d)
export AWS_SECRET_ACCESS_KEY=$(kubectl  get secret seaweedfs-s3-secret -o jsonpath='{.data.admin_secret_access_key}' |base64 -d)

kubectl port-forward svc/seaweedfs-s3 8333:8333
aws s3 cp --recursive /tmp/mender-artifact-storage/ --endpoint-url=http://localhost:8333 s3://mender-artifact-storage/
```
