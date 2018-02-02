---
title: Image configuration
taxonomy:
    category: docs
---

In this section we look at the configuration that can be modified due to requirements from a certain build or device.


## Configuring the image for read-only rootfs

!!! This is an experimental feature for now, and thus we do not recommend using it in a production setup. Nevertheless we recommend testing this feature as Mender will gradually move to support read-only rootfs by default in the future.

To build an image containing read-only rootfs add the following changes to the `conf/local.conf` file:

```bash
 IMAGE_FEATURES = "read-only-rootfs"
```

What is more, at the moment, there is a patch required to fix the resolver issue:

```bash
diff --git a/meta/recipes-core/systemd/systemd_234.bb b/meta/recipes-core/systemd/systemd_234.bb
index 4132cdf..7d61a53 100644
--- a/meta/recipes-core/systemd/systemd_234.bb
+++ b/meta/recipes-core/systemd/systemd_234.bb
@@ -273,6 +273,9 @@ do_install() {
 	else
 		sed -i -e "s%^L! /etc/resolv.conf.*$%L! /etc/resolv.conf - - - - ../run/systemd/resolve/resolv.conf%g" ${D}${exec_prefix}/lib/tmpfiles.d/etc.conf
 		ln -s ../run/systemd/resolve/resolv.conf ${D}${sysconfdir}/resolv-conf.systemd
+		if ${@bb.utils.contains('IMAGE_FEATURES', 'read-only-rootfs', 'true', 'false', d)}; then
+			ln -s ../run/systemd/resolve/resolv.conf ${D}${sysconfdir}/resolv.conf
+		fi
 	fi
 	install -Dm 0755 ${S}/src/systemctl/systemd-sysv-install.SKELETON ${D}${systemd_unitdir}/systemd-sysv-install

@@ -471,6 +474,12 @@ CONFFILES_${PN} = "${sysconfdir}/machine-id \
                 ${sysconfdir}/systemd/system.conf \
                 ${sysconfdir}/systemd/user.conf"

+FILES_MAYBE_RESOLV_CONF = "${@bb.utils.contains('PACKAGECONFIG', 'resolved', \
+                               bb.utils.contains('IMAGE_FEATURES', 'read-only-rootfs', \
+                                   '${sysconfdir}/resolv.conf', \
+                                   '', d), \
+                               '', d)}"
+
 FILES_${PN} = " ${base_bindir}/* \
                 ${datadir}/dbus-1/services \
                 ${datadir}/dbus-1/system-services \
@@ -487,6 +496,7 @@ FILES_${PN} = " ${base_bindir}/* \
                 ${sysconfdir}/xdg/ \
                 ${sysconfdir}/init.d/README \
                 ${sysconfdir}/resolv-conf.systemd \
+                ${FILES_MAYBE_RESOLV_CONF} \
                 ${rootlibexecdir}/systemd/* \
                 ${systemd_unitdir}/* \
                 ${base_libdir}/security/*.so \
```

To apply the path please run the following command (this assumes you are in `yocto/poky` directory):

```bash
echo 'diff --git a/meta/recipes-core/systemd/systemd_234.bb b/meta/recipes-core/systemd/systemd_234.bb
index 4132cdf..7d61a53 100644
--- a/meta/recipes-core/systemd/systemd_234.bb
+++ b/meta/recipes-core/systemd/systemd_234.bb
@@ -273,6 +273,9 @@ do_install() {
 	else
 		sed -i -e "s%^L! /etc/resolv.conf.*$%L! /etc/resolv.conf - - - - ../run/systemd/resolve/resolv.conf%g" ${D}${exec_prefix}/lib/tmpfiles.d/etc.conf
 		ln -s ../run/systemd/resolve/resolv.conf ${D}${sysconfdir}/resolv-conf.systemd
+		if ${@bb.utils.contains('IMAGE_FEATURES', 'read-only-rootfs', 'true', 'false', d)}; then
+			ln -s ../run/systemd/resolve/resolv.conf ${D}${sysconfdir}/resolv.conf
+		fi
 	fi
 	install -Dm 0755 ${S}/src/systemctl/systemd-sysv-install.SKELETON ${D}${systemd_unitdir}/systemd-sysv-install

@@ -471,6 +474,12 @@ CONFFILES_${PN} = "${sysconfdir}/machine-id \
                 ${sysconfdir}/systemd/system.conf \
                 ${sysconfdir}/systemd/user.conf"

+FILES_MAYBE_RESOLV_CONF = "${@bb.utils.contains('PACKAGECONFIG', 'resolved', \
+                               bb.utils.contains('IMAGE_FEATURES', 'read-only-rootfs', \
+                                   '${sysconfdir}/resolv.conf', \
+                                   '', d), \
+                               '', d)}"
+
 FILES_${PN} = " ${base_bindir}/* \
                 ${datadir}/dbus-1/services \
                 ${datadir}/dbus-1/system-services \
@@ -487,6 +496,7 @@ FILES_${PN} = " ${base_bindir}/* \
                 ${sysconfdir}/xdg/ \
                 ${sysconfdir}/init.d/README \
                 ${sysconfdir}/resolv-conf.systemd \
+                ${FILES_MAYBE_RESOLV_CONF} \
                 ${rootlibexecdir}/systemd/* \
                 ${systemd_unitdir}/* \
                 ${base_libdir}/security/*.so \' | git apply
```

Please note that the above patch won't be needed when the appropriate fixes
will be merged to the Yocto upstream project. The status of the patch submitted
can be followed up here: [http://lists.openembedded.org/pipermail/openembedded-core/2018-January/146834.html](http://lists.openembedded.org/pipermail/openembedded-core/2018-January/146834.html?target=_blank).


## Disabling Mender as a system service

If you do not want Mender to run as a system service, and you prefer to carry out update steps manually using the command line client interface, you can disable the service that starts Mender at boot.

This is simple to accomplish by adding a `recipes-mender/mender/mender_%.bbappend` file in your Yocto Project layer, with the following content:

```bash
SYSTEMD_AUTO_ENABLE = "disable"
```

In this case it is also possible to avoid Mender's current dependency on systemd. If you do not wish to enable systemd in your build, add the following to `local.conf`:

```bash
MENDER_FEATURES_DISABLE_append = " mender-systemd"
```

Also, you do not need any daemon-related configuration items in your `local.conf` as outlined in [the section on configuring the Yocto Project build](../../artifacts/building-mender-yocto-image#configuring-the-build).

! If you disable Mender running as a daemon under `systemd`, you must run all required Mender commands from the CLI or scripts. Most notably, you need to run `mender -commit` after booting into and verifying a successful deployment. When running in managed mode, any pending `mender -commit` will automatically be run by the Mender daemon after it starts. See [Modes of operation](../../architecture/overview#modes-of-operation) for more information about the difference.


## Configuring polling intervals

You can configure how frequently the Mender client will make requests to the Mender server
as described in [Polling intervals](../../client-configuration/configuration-file/polling-intervals) before
starting the build process.

In order to do this, change the following in the file
`meta-mender/meta-mender-core/recipes-mender/mender/mender_0.1.bb`:

```bash
MENDER_UPDATE_POLL_INTERVAL_SECONDS ?= "1800"
MENDER_INVENTORY_POLL_INTERVAL_SECONDS ?= "1800"
```


## Configuring server address and port

If the client should connect to a different address than the default of `https://docker.mender.io/`, then you should specify this variable in your `local.conf`:

```bash
MENDER_SERVER_URL = "https://my-mender-server.net/"
```

Port numbers can be specified in the same way as you would in a browser, as a colon after the address followed by the number, for example `https://my-mender-server.net:8999/`.

!! Note that the `https` protocol specifier is required in the address. For security reasons, Mender does not support the plaintext `http` protocol.
