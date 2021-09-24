---
title: Customization
taxonomy:
    category: docs
    label: tutorial
---

-------------------------------------------------------------------------------

## Configuration Files

<!--AUTOVERSION: "blob/%/config"/mender-convert-->
The configuration files are a means to customize the conversion process for
`mender-convert`. In the `configs/` directory, there are customization scripts
which add support for board-specific configurations. A run of `mender-convert`
can include multiple configuration files, each one added with the `--config`
command-line option. The standard configuration [configs/mender_convert_config](https://github.com/mendersoftware/mender-convert/blob/master/configs/mender_convert_config) includes the defaults for the configuration options which the tool supports.

### Example

An example application of using a configuration file can be enabling `lzma`
compression for the Raspberry Pi 3:

```bash
echo 'MENDER_ARTIFACT_COMPRESSION=lzma' >> configs/custom_config
```

Call `mender-convert` and provide your custom configuration file using the
`--config` option:

```bash
MENDER_ARTIFACT_NAME=release-1 ./mender-convert \
  --disk-image input/<image-to-convert.img> \
  --config configs/raspberrypi3_config \
  --config configs/custom_config
```

### Mender demo configuration

There is an specific configuration file to set up Mender client and add-ons with
suitable values for demo, such as short polling intervals. Include this file in
your images with `--config configs/mender_convert_demo_config`:

```bash
MENDER_ARTIFACT_NAME=release-1 ./mender-convert \
  --disk-image input/<image-to-convert.img> \
  --config configs/raspberrypi3_config \
  --config configs/mender_convert_demo_config \
  --config configs/custom_config
```

Configuration files are also a means to add customization that might be
necessary for specific devices or distributions.


-------------------------------------------------------------------------------

## Hooks/Overrides

The `mender-convert` tool supports the addition of user *hooks* to override, or add to some specific
part of the modification process. There are two hook interfaces: List based hooks and function
hooks.

### List based hooks

The list based hooks modify the image contents, or post-process the binary image
after its creation (but before compression). For example, create a file
`configs/custom_config`, and add this content to it:

```bash
remove_apt_cache_from_filesystem() {
    log_info "Remove apt cache on device to save space."
    run_and_log_cmd "sudo rm -rf work/var/cache/apt"
}
PLATFORM_MODIFY_HOOKS+=(remove_apt_cache_from_filesystem)

embed_bootloader_in_image() {
    log_info "Embedding bootloader in disk image"
    run_and_log_cmd "dd if=work/bootloader.img of=${img_path} \
        seek=64 conv=notrunc status=none"
}
PLATFORM_PACKAGE_HOOKS+=(embed_bootloader_in_image)
```

When calling mender-convert, enable the hooks by using the `--config` argument to supply the
`custom_config` file:

```bash
MENDER_ARTIFACT_NAME=release-1 ./mender-convert \
  --disk-image input/<image-to-convert.img> \
  --config configs/raspberrypi3_config \
  --config configs/custom_config
```

These four variables hold lists of hooks:

* `PLATFORM_MODIFY_HOOKS` - Run after the filesystem is prepared, but before the image is created.
* `USER_LOCAL_MODIFY_HOOK` - Run after `PLATFORM_MODIFY_HOOKS`.
* `OVERLAY_MODIFY_HOOKS` - Run after overlays application.
* `PLATFORM_PACKAGE_HOOKS` - Run after image creation, but before compression and bmap
  creation.

!!! Note that the variables come with default values of `PLATFORM_MODIFY_HOOKS=(platform_modify)`,
!!! `USER_LOCAL_MODIFY_HOOKS=(user_local_modify)`, `OVERLAY_MODIFY_HOOKS=(overlay_modify)` and
!!! `PLATFORM_PACKAGE_HOOKS=(platform_package)` .
!!! This is because the `platform_modify`, `user_local_modify`, `overlay_modify` and
!!! `platform_package` function overrides were the only way to specify hooks in mender-convert 2.0.

### Function override hook

There is only one function override hook in mender-convert: `mender_create_artifact`. This is used
to override the command which creates Mender Artifacts from the rootfs image. Just define the
function in a custom config file to use the hook. A good starting point is the standard function
found in the standard configuration file `configs/mender_convert_config`.

An example of overriding the `mender_create_artifact` hook is provided below.

Create a custom configuration file with a custom implementation of `mender_create_artifact`:

```bash
cat <<- EOF >> configs/custom_config
mender_create_artifact() {
  local -r device_type="${1}"
  local -r artifact_name="${2}"
  mender_artifact=deploy/${device_type}-${artifact_name}.mender
  log_info "Running custom implementation of the 'mender_create_artifact' hook"
  log_info "Writing Mender artifact to: ${mender_artifact}"
  log_info "This can take up to 20 minutes depending on which compression method is used"
  run_and_log_cmd "mender-artifact --compression ${MENDER_ARTIFACT_COMPRESSION} \
      write rootfs-image \
      --key <path/to/private-key> \
      --file work/rootfs.img \
      --output-path ${mender_artifact} \
      --artifact-name ${artifact_name} \
      --device-type ${device_type}"
}
EOF
```

Call `mender-convert` and provide your custom configuration file using the
`--config` option:

```bash
MENDER_ARTIFACT_NAME=release-1 ./mender-convert \
  --disk-image input/<image-to-convert.img> \
  --config configs/raspberrypi3_config \
  --config configs/custom_config
```
This should trigger the provided `mender_create_artifact` implementation in `configs/custom_config`.

-------------------------------------------------------------------------------

## Rootfs overlays

The "rootfs-overlay" is a method for providing new and modified files to appear
in the output image without needing to modify the input image. Adding a file to
your "rootfs-overlay" will allow you customize the files that are included in
the output images.

!!! A Mender config file `/etc/mender/mender.conf` in an rootfs overlay will be
!!! ignored. Put your configuration file in `resources/mender.conf` instead. See
!!! section below.

### Example

One example of a overlay-rootfs addition can be found in the
`rootfs-overlay-demo` directory, which, after running the server setup script
(see [Configure the Mender client server configuration](../docs.md#configure-the-mender-client-server-configuration))
contains:

```bash
rootfs_overlay_demo
└── etc
    ├── hosts
    └── mender
        └── server.crt
```

The files and folders shown above will become a part of the final file system
available to the device on boot

If the final image needs application configurations and additions, this is the
recommended way of doing it.

When invoking mender-convert, pass the `--overlay` argument with the name of the
overlay directory:

```bash
MENDER_ARTIFACT_NAME=release-1 ./docker-mender-convert \
    --disk-image input/golden-image-1.img \
    --config configs/raspberrypi3_config \
    --overlay rootfs_overlay_demo/
```

## Mender configuration file

The Mender client configuration file `mender.conf` must be provided in
`resources/mender.conf`. `mender-convert` provides helpers to create this file,
together with bootstraping a rootfs overlay suitable for different Mender server
configurations. For example for [hosted
Mender](https://hosted.mender.io?target=_blank), use:

```bash
./scripts/bootstrap-rootfs-overlay-hosted-server.sh \
    --output-dir ${PWD}/rootfs_overlay_demo \
    --tenant-token "Paste token from https://hosted.mender.io/ui/#/settings/my-organization"
```

There are additional scripts in the `scripts/` directory to enable working with
a local demo server, or a production server.
