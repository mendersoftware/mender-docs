---
title: docker-compose Update Module
taxonomy:
    category: docs
    label: tutorial
---

<!--AUTOVERSION: "Mender Client %"/ignore-->
!!! The docker-compose Update Module is included in Mender Client 6.0 or newer.
!!! You can find the source code in the [mender-container-modules repository](https://github.com/mendersoftware/mender-container-modules).

<!--AUTOVERSION: "mender-convert %"/ignore-->
!!! The docker-compose Update Module will be available in mender-convert 5.2.0 or newer.


To install the docker-compose Update Module in the converted image, set:
```bash
echo 'MENDER_DOCKER_COMPOSE_INSTALL="y"' >> configs/docker_compose_config
```

The default version is set to `latest`, meaning the latest released version. You
can manually override the version to install by setting:
```bash
# Valid values are "latest" (default), "main" or a specific version.
echo 'MENDER_DOCKER_COMPOSE_VERSION="main"' >> configs/docker_compose_config
```

The docker-compose Update Module depends on Docker and Docker Compose. The package will automatically
install the dependencies, so we recommend to increase the size of the image mounted during the
package installation.
To expand by 512MB, set:
```bash
echo 'MENDER_EXPAND_WORK_ROOTFS="512M"' >> configs/docker_compose_config
```

!!! The argument to `MENDER_EXPAND_WORK_ROOTFS` is an integer and an optional unit (example: 10K is 10*1024).
!!! See `truncate` man page for more details. Note that this does not directly affect the final image size;
!!! it only expands the root filesystem extracted from the input image to ensure there is enough space to
!!! install the packages and their dependencies. The final rootfs image size is calculated separately based
!!! on actual disk usage plus `IMAGE_ROOTFS_EXTRA_SPACE` and `IMAGE_OVERHEAD_FACTOR`.


By default, Docker will store the container images in `/var/lib/docker`. In order for container images to
persist over rootfs updates, it's necessary to configure Docker to use persistent storage. We can modify the
Docker storage by configuring the `data-root` in `/etc/docker/daemon.json`.

Before creating the config, we'll create a rootfs overlay for hosted Mender:

```bash
# choose hosting region, from either 'eu' and 'us' ('us' if nothing is specified)
./scripts/bootstrap-rootfs-overlay-hosted-server.sh \
    --output-dir input/rootfs_overlay_docker_compose \
    --region us \
    --tenant-token "Paste token from https://hosted.mender.io/ui/settings/organization"
```

!!!! See [Rootfs overlays](../../02.Convert-a-Mender-Debian-image/01.Customization/docs.md#rootfs-overlays) for more information.

We can then create the config:
```bash
sudo mkdir -p input/rootfs_overlay_docker_compose/etc/docker
cat <<EOF | sudo tee input/rootfs_overlay_docker_compose/etc/docker/daemon.json
{
   "data-root": "/data/docker"
}
EOF
sudo chmod 600 input/rootfs_overlay_docker_compose/etc/docker/daemon.json
sudo chown root:root input/rootfs_overlay_docker_compose
```

!!! `sudo` is required to modify the rootfs overlay because the bootstrap-rootfs-overlay scripts set the owner and group to root

To use the config defined in `configs/docker_compose_config` and the overlay in `input/rootfs_overlay_docker_compose`, you must include
`--config configs/docker_compose_config` and `--overlay input/rootfs_overlay_docker_compose/` as arguments when running mender-convert.

!!!! See [Customization](../../02.Convert-a-Mender-Debian-image/01.Customization) for more information.


## Next steps

For information on how to create docker-compose Artifacts, see [Create a docker-compose update Artifact](../../../08.Artifact-creation/05.Create-a-docker-compose-update-Artifact).
