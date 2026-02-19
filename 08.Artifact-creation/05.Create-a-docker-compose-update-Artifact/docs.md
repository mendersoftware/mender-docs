---
title: Create a docker-compose update Artifact
taxonomy:
    category: docs
    label: tutorial
---

!!! The docker-compose Update Module is included in Mender Client 6.0 or newer.
!!! The Update Module is not installed by default. It can be installed to your target devices as a Debian package or with a Yocto recipe.
!!! You can find the source code in the [mender-container-modules repository](https://github.com/mendersoftware/mender-container-modules).

This document explains how to create a docker-compose Artifact using the `gen_docker-compose` Artifact generator.
The generated Artifact contains a docker-compose manifest and the container images required to deploy an update using the docker-compose Update
Module from [mender-container-modules](https://github.com/mendersoftware/mender-container-modules). This ensures robust network transfers of container images using the Mender Client in managed mode, while also enabling Standalone mode to install container images without network access.

### Prerequisites

This tutorial assumes:

* You have installed [mender-artifact](../../12.Downloads/01.Workstation-tools/docs.md#mender-artifact) on your workstation
* You have installed `skopeo` on your workstation for downloading container images from registries

#### Install the Artifact generator

Download the Artifact generator from the repository:
<!--AUTOVERSION: "/mender-container-modules/%/"/mender-container-modules -->
```bash
curl -O https://raw.githubusercontent.com/mendersoftware/mender-container-modules/main/src/gen_docker-compose
chmod +x gen_docker-compose
```

Verify the installation:
```bash
./gen_docker-compose --help
```

### Basic usage

The simplest way to create a docker-compose Artifact is to let `gen_docker-compose` automatically download the required container images from their registries.

#### Create a docker-compose manifest

First, create a directory for your manifests and add a `docker-compose.yml` file, e.g.:

```bash
mkdir manifests
cat > manifests/docker-compose.yml << 'EOF'
services:
  webserver:
    image: nginx:alpine
    ports:
      - "8080:80"
EOF
```

#### Generate the Artifact

!!! By default, `gen_docker-compose` downloads container images for your workstation's architecture. If your workstation differs from your device architecture, you should specify the target architecture using the `--architecture` flag.

To list available architectures for the images in your manifests:

```bash
./gen_docker-compose \
    --list-architectures \
    --manifests-dir manifests/
```

Create the Artifact by for your target device by specifying the artifact name, compatible types, architecture, manifests directory, and project name:

```bash
./gen_docker-compose \
    --artifact-name docker-compose-artifact-v1 \
    --device-type raspberrypi5 \
    --architecture arm64 \
    --manifests-dir manifests/ \
    --project-name my-webserver \
    --output-path docker-compose-artifact-v1.mender
```

The tool will:
1. Parse the docker-compose manifest
2. Download container images from their registries using `skopeo`
3. Package the images and manifests into a Mender Artifact

The output shows the Artifact structure:
```
Mender Artifact:
  Name: docker-compose-artifact-v1
  Format: mender
  Version: 3
  Signature: no signature
  Compatible types: [raspberrypi5]
  Provides group:
  Depends on one of artifact(s): []
  Depends on one of group(s): []
  State scripts: []

Updates:
  - Type: docker-compose
    Provides:
      rootfs-image.mender-docker-compose.my-webserver.version: docker-compose-artifact-v1
    Depends: {}
    Clears Provides: [*mender-docker-compose_*]
    Metadata:
      {
        "project_name": "my-webserver",
        "version": "1"
      }
    Files:
      - checksum: 57a12b190c2ba23e4fd77222b1df9e1fd14f90bbe13acf64b162c5bc7c7cb98f
        modified: 2025-11-27 14:13:30 +0100 CET
        name: images.tar.gz
        size: 22092805
      - checksum: 364567786aab968bd9f54c23ba90235bfdbce8b704e2e6fbfb929513c16eecbf
        modified: 2025-11-27 14:13:28 +0100 CET
        name: manifests.tar
        size: 10240
```

The Artifact contains two files:
* **images.tar.gz** - Compressed archive of all container images required by the composition
* **manifests.tar** - Archive containing the docker-compose manifest files

### Manual image preparation

Instead of letting `gen_docker-compose` download images automatically, you can prepare the container images manually.

#### Extract images using Docker

First, pull the required images and save them as tar files:

```bash
mkdir images
docker pull nginx:alpine
docker save -o images/nginx_alpine.tar nginx:alpine
```

The filename doesn't need to follow a specific format, but it's helpful to use a descriptive name.

#### Generate the Artifact with the pre-downloaded container images

Now generate the Artifact using the `--images-dir` option:

```bash
./gen_docker-compose \
    --artifact-name docker-compose-artifact-v1 \
    --device-type raspberrypi5 \
    --manifests-dir manifests/ \
    --images-dir images/ \
    --project-name my-webserver \
    --output-path docker-compose-artifact-v1.mender
```

When `--images-dir` is specified, `gen_docker-compose` will use the provided images instead of downloading them from registries.

### Custom container registries

To use images from a private or custom registry, specify the full image path in your docker-compose manifest:

<!--AUTOVERSION: "my-service:v%"/ignore-->
```yaml
services:
  my-service:
    image: registry.example.com/my-org/my-service:v1.2.3
```

When using automatic image download with authenticated registries, you can configure credentials using either Docker or skopeo:

```bash
# Using Docker login (skopeo will use these credentials)
docker login registry.example.com

# Or authenticate directly with skopeo
skopeo login registry.example.com
```

After authenticating, `gen_docker-compose` will be able to download images from the private registry.

### Passing options to mender-artifact

Additional options can be passed directly to the underlying `mender-artifact` tool using `--`:

```bash
./gen_docker-compose \
    --artifact-name docker-compose-artifact-v1 \
    --device-type raspberrypi5 \
    --manifests-dir manifests/ \
    --project-name my-webserver \
    -- \
    --software-filesystem data \
    --depends rootfs-image.checksum:custom-value
```
