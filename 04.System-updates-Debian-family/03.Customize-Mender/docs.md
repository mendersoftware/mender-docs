---
title: Customize Mender
taxonomy:
    category: docs
---

This chapter assumes that you are familiar with [rootfs
overlays](../convert-a-mender-debian-image/customization#rootfs-overlays).

## Mender server address

If you wish to use your own Mender server instead of Hosted Mender, you will need to provide a
custom server address in the converted image. To do so, generate a new overlay using the
`bootstrap-rootfs-overlay-production-server.sh` script, and give the `--server-url` argument:

```bash
./scripts/bootstrap-rootfs-overlay-production-server.sh \
    --output-dir ${PWD}/rootfs_overlay_production \
    --server-url https://my-mender-server.com/
```

It is also possible to override the public certificate that Mender will use to authenticate the
server. To do so, add the `--server-cert` and a path to the certificate to the command above. This
is not necessary if you are using a certificate which has been signed by a public Certificate
Authority (CA).

## Configuration file

To provide a custom `mender.conf` configuration file inside the image, put the configuration file in
the `/etc/mender` directory inside [your own
layer](../convert-a-mender-debian-image/customization#rootfs-overlays). Use these commands to create
an overlay and put a custom configuration file inside the overlay:

```bash
mkdir -p rootfs_overlay_production/etc/mender
cat > rootfs_overlay_production/etc/mender/mender.conf <<EOF
{
  "ServerURL": "https://my-server.com/"
}
EOF
chmod 600 rootfs_overlay_production/etc/mender/mender.conf
sudo chown root:root rootfs_overlay_production
```

The options inside the JSON structure can be any option from [the client configuration
options](../../client-installation/configuration-file/configuration-options).

## Identity

To add your own identity script to the image, execute these commands:

```bash
SCRIPT=<PATH-TO-IDENTITY-SCRIPT>
mkdir -p rootfs_overlay_production/usr/share/mender/identity
cp $SCRIPT rootfs_overlay_production/usr/share/mender/identity/
chmod 755 rootfs_overlay_production/usr/share/mender/identity/*
sudo chown root:root rootfs_overlay_production
```

Replace `<PATH-TO-IDENTITY-SCRIPT>` with the path to your identity script. Remember that the name of
the script must be `mender-device-identity`, while the path can be arbitrary. To learn more about
how to write identity scripts, see [the Identity section](../../client-installation/identity).

## Inventory

To add your own inventory script to the image, execute these commands:

```bash
SCRIPT=<PATH-TO-INVENTORY-SCRIPT>
mkdir -p rootfs_overlay_production/usr/share/mender/inventory
cp $SCRIPT rootfs_overlay_production/usr/share/mender/inventory/
chmod 755 rootfs_overlay_production/usr/share/mender/inventory/*
sudo chown root:root rootfs_overlay_production
```

Replace `<PATH-TO-INVENTORY-SCRIPT>` with the path to your inventory script. Remember that the name
of the script must start with `mender-inventory-`, while the path can be arbitrary. To learn more
about how to write inventory scripts, see [the Inventory
section](../../client-installation/inventory).

## Update Modules

To install an Update Module in the image, execute these commands:

```bash
MODULE=<PATH-TO-UPDATE-MODULE>
mkdir -p rootfs_overlay_production/usr/share/mender/modules/v3
cp $MODULE rootfs_overlay_production/usr/share/mender/modules/v3/
chmod 755 rootfs_overlay_production/usr/share/mender/modules/v3/*
sudo chown root:root rootfs_overlay_production
```

Replace `<PATH-TO-UPDATE-MODULE>` with the path to your Update Module. To learn more about Update
Modules, visit the section ["Use an Update Module"](../../client-installation/use-an-update-module).
