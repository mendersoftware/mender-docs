---
title: docker-compose Update Modules
taxonomy:
    category: docs
    label: tutorial
---

!!! The docker-compose Update Module is included in Mender Client 6.0 or newer.
!!! You can find the source code in the [mender-container-modules repository](https://github.com/mendersoftware/mender-container-modules).

## Integrate `mender-docker-compose` into the Yocto environment

Add the `meta-mender-extended` layer to your Yocto environment:

```bash
bitbake-layers add-layer ../sources/meta-mender/meta-mender-extended
```

You'll also need to add layers required for Docker support:

```bash
# Add required layers for Docker support
bitbake-layers add-layer ../sources/poky/meta-virtualization
bitbake-layers add-layer ../sources/meta-openembedded/meta-networking
bitbake-layers add-layer ../sources/meta-openembedded/meta-filesystems
```

Add the following to your `local.conf` to include `mender-docker-compose` in your build:

<!--AUTOVERSION: "/mender-container-modules/%/"/mender-container-modules -->
```bash
cat <<EOF >> conf/local.conf
# docker-compose Update Module

IMAGE_INSTALL:append = " mender-docker-compose"
DISTRO_FEATURES:append = " virtualization"
EOF
```

By default, Docker will store the container images in `/var/lib/docker`.
In order for container images to persist over rootfs updates, it's
necessary to configure Docker to use persistent storage. `meta-mender` provides
a variable, `MENDER_DOCKER_DATA_ROOT`, which will set the Docker data-root in the
`/etc/docker/daemon.json` config:

```bash
cat <<EOF >> conf/local.conf
MENDER_DOCKER_DATA_ROOT = "/data/docker"
EOF
```

Since we're now storing container images in the `/data` partition, it
might be necessary to increase the storage sizes to ensure we don't run
out of space during a docker-compose deployment, e.g.:

```bash
cat <<EOF >> conf/local.conf
MENDER_DATA_PART_SIZE_MB = "1024"
MENDER_STORAGE_TOTAL_SIZE_MB = "4096"
EOF
```

## Integrate `mender-delta-docker-compose` into the Yocto environment

!!! The delta-docker-compose Update Module is included in Mender Client 6.1 or
!!! newer for [Mender Professional](https://mender.io/product/features?target=_blank) and
!!! [Mender Enterprise](https://mender.io/product/features?target=_blank) users.

Download the `mender-delta-docker-compose` binaries following the
[instructions](../../../12.Downloads/02.Device-components/docs.md#mender-delta-docker-compose).

Follow the above instructions for integrating the `mender-docker-compose` Update
Module. On top of that, also add `meta-mender-commerical` layer to your Yocto
environment:

```bash
bitbake-layers add-layer ../sources/meta-mender/meta-mender-commercial
```

add the following to your `conf/local.conf`

<!--AUTOVERSION: "mender-delta-docker-compose-%"/mender-delta-docker-compose-->
```
LICENSE_FLAGS_ACCEPTED:append = " commercial_mender-yocto-layer-license"
SRC_URI:pn-mender-delta-docker-compose = "file://${HOME}/mender-delta-docker-compose-1.0.0.tar.xz"
```

and use

```
IMAGE_INSTALL:append = " mender-docker-compose mender-delta-docker-compose"
```

instead of listing `mender-docker-compose` only.

!!! Although the `mender-delta-docker-compose` Update Module can work alone, it is
!!! generally advised to include both Update Modules so that both full and delta
!!! `docker-compose` Artifacts can be deployed to devices.


## Next steps

For information on how to create docker-compose and delta-docker-compose
Artifacts, see [Create a docker-compose update
Artifact](../../../08.Artifact-creation/05.Create-a-docker-compose-update-Artifact).
