---
title: docker-compose Update Module
taxonomy:
    category: docs
    label: tutorial
---

!!! The docker-compose Update Module is included in Mender Client 6.0 or newer.
!!! You can find the source code in the [mender-container-modules repository](https://github.com/mendersoftware/mender-container-modules).

<!--AUTOVERSION: "with %"/ignore -->
!!! The docker-compose Update Module will be available in Yocto Project LTS releases supported by meta-mender, starting with scarthgap.

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

## Next steps

For information on how to create docker-compose Artifacts, see [Create a docker-compose update Artifact](../../../08.Artifact-creation/05.Create-a-docker-compose-update-Artifact).
