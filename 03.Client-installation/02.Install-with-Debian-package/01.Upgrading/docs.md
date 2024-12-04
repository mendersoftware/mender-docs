---
title: Upgrading
taxonomy:
    category: docs
---

This page describes how to upgrade one Mender Client version to a different Mender Client version.

## Minor and patch versions

<!--AUTOVERSION: "% -> %"/ignore-->
If you are upgrading from one minor version to another, such as 3.4.0 -> 3.5.0, or from one patch
version to another patch version, such as 3.5.1 -> 3.5.2, then no manual intervention is
needed. Minor and patch versions are always backwards compatible. This follows from Semantic
Versioning, which is described in more detail on [the Compatibility
page](../../../02.Overview/15.Compatibility/docs.md).

## Major versions

New major versions may come with changes that require manual migration steps. Changes of this sort
are sometimes necessary to fix problems that cannot be dealt with in minor releases, or enable new
behaviors that conflict with existing behaviors in some way.

### Upgrade the Mender Client 4.x series to 5.x series

#### Overview

<!--AUTOVERSION: "In Mender Client %"/ignore-->
In Mender Client 5.0.0, community Update Modules have been moved from our officially supported
repository to the community repository to clarify their support level.

Below you will find the steps describing how to get the community Update Modules, installed by
default with  Mender Client 4.x, on Mender Client 5.x series. The steps will show the case for the
`deb` Update Module as an example.

On Mender Client 4.x series, both the community and Norhtern.tech supported Update Modules were
installed:
* deb
* directory
* docker
* rootfs-image
* rpm
* script
* single-file

From Mender Client 5.x series onwards, the community Update Models are removed, and only the
officially supported ones are installed by default alongside the client:
* directory
* rootfs-image
* single-file

The Update Modules `deb`, `docker`, `rpm` and `script` have been moved to
[`mender-update-modules` repository](https://github.com/mendersoftware/mender-update-modules/).

When you upgrade from Mender Client 4.x to Mender Client 5.x, you will lose the community Update
Modules that were previously installed by default. This will happen regardless of the way you're
installing the Mender Client.

For a list of all community-supported Update Modules, please see the [Update Module category in the
Mender Hub community forum](https://hub.mender.io/c/update-modules/13).

#### Install an Update Module with Yocto

Add an snippet like the following to a `mender_%.bbappend` in your layer:

<!--AUTOVERSION: "mender-update-modules/%/deb"/ignore-->
```
SRC_URI:append = " \
  https://raw.githubusercontent.com/mendersoftware/mender-update-modules/master/deb/module/deb;sha256sum=065714b581785a2d7c83b684f0d5348031c5512f21863fed38197078cb3ef6e5 \
"
FILES:${PN}:append = " \
  ${datadir}/mender/modules/v3/deb \
"
do_install:append () {
  mkdir -p ${D}/${datadir}/mender/modules/v3
  find ${WORKDIR}
  install -m 755 ${WORKDIR}/deb ${D}/${datadir}/mender/modules/v3/deb
}
```

In the example above the SHA256 checksum is generated with:

<!--AUTOVERSION: "mender-update-modules/%/deb"/ignore-->
```
curl --silent "https://raw.githubusercontent.com/mendersoftware/mender-update-modules/master/deb/module/deb" | sha256sum | awk '{print $1}'
# Outputs: 065714b581785a2d7c83b684f0d5348031c5512f21863fed38197078cb3ef6e5
```

#### Install an Update Module with `mender-convert`

Add an snippet like this one to your config file:

<!--AUTOVERSION: "mender-update-modules/%/deb"/ignore-->
```
install_update_module_deb() {
    run_and_log_cmd "mkdir -p work/rootfs/usr/share/mender/modules/v3"
    run_and_log_cmd "wget -P work/rootfs/usr/share/mender/modules/v3 https://raw.githubusercontent.com/mendersoftware/mender-update-modules/master/deb/module/deb"
    run_and_log_cmd "chmod 0755 work/rootfs/usr/share/mender/modules/v3/deb"
}
OVERLAY_MODIFY_HOOKS+=(install_update_module_deb)
```

#### Install an Update Module on a live device

Execute an snippet like this one:

<!--AUTOVERSION: "mender-update-modules/%/deb"/ignore-->
```
mkdir -p work/rootfs/usr/share/mender/modules/v3
wget -P work/rootfs/usr/share/mender/modules/v3 https://raw.githubusercontent.com/mendersoftware/mender-update-modules/master/deb/module/deb
chmod 0755 work/rootfs/usr/share/mender/modules/v3/deb
```

### Upgrade the Mender Client 3.x series to 4.x series

#### Overview

<!--AUTOVERSION: "In Mender Client %"/ignore-->
In Mender Client 4.0.0, the service was split into several smaller components. Previously the
`mender` binary tool handled everything; now there are several smaller ones with distinct roles:

* `mender-auth` for handling server communication and authentication
* `mender-setup` for handling Mender configuration setup
* `mender-snapshot` for handling snapshotting of live filesystems
* `mender-update` for handling updates.

Following that change, the Linux systemd service was also split from `mender-client` into
`mender-authd` and `mender-updated`.

<!--AUTOVERSION: "Mender Client % and later"/ignore-->
The following features and config are not available in Mender Client 4.0.0 and later:

- [Synchronized
  updates](https://docs.mender.io/3.6/overview/customize-the-update-process#synchronized-updates)
- [Update Management API](https://docs.mender.io/3.6/device-side-api/io.mender.update1)
- The
  [connectivity](https://docs.mender.io/3.6/client-installation/configuration-file/configuration-options#connectivity)
  options in the client setting. The new client does not cache connections, so these options are
  not needed anymore

<!--AUTOVERSION: "Mender Client % and later"/ignore-->
In Mender Client 4.0.0 and later the rootfs-image update type is no longer embedded in the client
codebase but is treated as any other external update module. A binary CLI tool `mender-flash` now
gets installed as part of the Mender Client to serve the needs of the external rootfs update module.

#### Upgrade using Debian packages

In the [Mender APT repositories](../../../10.Downloads/docs.md#install-using-the-apt-repository) `mender-client`
package corresponds to the Mender Client written in Go (version 3.x.y). This package is installed by default
from our [Express installation script](../../../10.Downloads/docs.md#express-installation). To upgrade from the
legacy Mender Client to the 4.x series on Debian and Ubuntu, you can install the `mender-client4` running:

<!--AUTOMATION: ignore -->
```bash
apt-get install mender-client4
```

This package will automatically install:

* a `mender-auth` package for server authentication:
  * provides the `mender-auth` binary
  * installs the `mender-authd` systemd service
* a `mender-update` package for doing updates:
  * provides the `mender-update` binary
  * installs the `mender-updated` systemd service
* the `mender-flash` tool
* the `mender-setup` tool
* the `mender-snapshot` tool

In addition, this package will also automatically remove:

* Legacy `mender-client` package:
  * removing the `mender` binary
  * disabling `mender-client` systemd service

After the upgrade, please update your scripts invoking the `mender` CLI interface to use the
correct binaries (`mender-auth` or `mender-update`).

For old Debian and Ubuntu distributions, if the Mender add-ons Debian packages (e.g.,
`mender-connect` and `mender-configure`) are already installed in the system, the upgrade
can fail with an error message similar to this:

<!--AUTOVERSION: "Conflicts: mender-client but 1:%-1+debian+buster is to be installed"/ignore-->
```
The following packages have unmet dependencies:
 mender-client4 : Conflicts: mender-client but 1:3.5.2-1+debian+buster is to be installed
E: Unable to correct problems, you have held broken packages.
```

In this case, ensure to upgrade the Mender add-ons Debian packages at the same time, for
example running:

<!--AUTOMATION: ignore -->
```bash
apt-get install mender-update mender-client4
```

#### Upgrade using Yocto

<!--AUTOVERSION: "Mender Client version % or later"/ignore "Yocto 5.0 (%)"/ignore "Yocto 4.0 (%)"/ignore-->
Mender Client version 4.0.0 or later will automatically be built on Yocto 5.0 (scarthgap) and
later. If you want to enable building of Mender Client version 4.0.0 or later while on
Yocto 4.0 (kirkstone) or older, please refer to [this specific section in our Troubleshoot
guide](../../../301.Troubleshoot/01.Yocto-project-build/docs.md#mender-client-version-4-0-0-have-been-released-but-my-build-still-uses-the-single-client-3-x-series).

#### Migration steps

Regardless of whether you are using Yocto or a Debian package, there are some migration steps which
are required. When referring to "scripts" below, we mean any Update Module, State Script, or other
script which executes on the device. All scripts that ship with Mender, and which you have not
modified, do not need to be changed, since they will be auto-updated by the package manager.

1. If any scripts call this command:
	* `mender bootstrap`
   Then they need to be changed to call `mender-auth bootstrap` instead of `mender bootstrap`.

2. If any scripts call this command:
	* `mender setup`
   Then they need to be changed to call `mender-setup` instead of `mender setup`.

<!--AUTOVERSION: "at least mender-artifact version %"/ignore-->
3. If any scripts call this command:
	* `mender snapshot`
   Then they need to be changed to call `mender-snapshot` instead of `mender snapshot`. Note that
   if you are using snapshotting through mender-artifact's "ssh" feature, then you need
   at least mender-artifact version 3.11.0.

4. If any scripts call one of these commands:
	* `mender check-update`
	* `mender commit`
	* `mender install`
	* `mender rollback`
	* `mender send-inventory`
	* `mender show-artifact`
	* `mender show-provides`
   Then they need to be changed to call `mender-update <COMMAND>` instead of `mender <COMMAND>`.

5. If any scripts call one of these commands:
	* `mender daemon`
   Then you will need several changes. Since `mender-auth` and `mender-update` are now separate
   daemons, you will need to start both of them, with `mender-auth daemon` and `mender-update
   daemon`, respectively.

6. If any scripts call either `journalctl` or `systemctl` with `mender-client` as an argument, you
   will need to change that. `mender-client` service has been replaced by two services
   `mender-authd` and `mender-updated`.
