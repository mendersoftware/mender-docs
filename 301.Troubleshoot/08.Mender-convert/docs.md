---
title: mender-convert
taxonomy:
    category: docs
---

## Build fails with The following packages have unmet dependencies and Unable to correct problems, you have held broken packages

This error indicates that the chosen versions of the Mender components for the build are incompatible or unsupported. This can happen, for example, when using `MENDER_*_VERSION` to pin versions of Mender software but using a non supported combination.

Mender Client 6.0 and newer comes with a new package that can only be installed with a supported combination of versions of the different components.

The error shall not happen when using the default `latest` versions.

The full mender-convert error follows:

<!--AUTOVERSION: "%-1+debian+trixie"/ignore "(< %)"/ignore-->
```
mender-convert-modify has finished. Cleaning up...
2026-03-11 15:03:58 [ERROR] [mender-convert] mender-convert failed
2026-03-11 15:03:58 [DEBUG] [mender-convert-modify] When running: (modules/chroot.sh:165): run_and_log_cmd():
	sudo chroot work/rootfs/ /tmp/qemu-aarch64-static /usr/bin/env env         DEBIAN_FRONTEND=noninteractive         DEVICE_TYPE=raspberrypi4_64         apt --assume-yes --fix-broken --no-remove install  mender-update=5.1.0-1+debian+trixie mender-configure=1.1.3-1+debian+trixie mender-client4=5.1.0-1+debian+trixie mender-auth=5.1.0-1+debian+trixie mender-flash=1.1.0-1+debian+trixie mender-setup=1.0.3-1+debian+trixie mender-client-version-inventory-script=6.0.0-1+debian+trixie mender-snapshot=1.0.0-1+debian+trixie
WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Reading package lists...
Building dependency tree...
Reading state information...
Solving dependencies...
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

Unsatisfied dependencies:
 mender-client-version-inventory-script : Conflicts: mender-configure (< 1.1.4) but 1.1.3-1+debian+trixie is to be installed
Error: Unable to correct problems, you have held broken packages.
Error: The following information from --solver 3.0 may provide additional context:
   Unable to satisfy dependencies. Reached two conflicting decisions:
   1. mender-client-version-inventory-script:arm64=6.0.0-1+debian+trixie is selected for install
   2. mender-client-version-inventory-script:arm64 is not selected for install because:
      1. mender-configure:arm64=1.1.3-1+debian+trixie is selected for install
      2. mender-client-version-inventory-script:arm64 Conflicts mender-configure (< 1.1.4)
         [selected mender-configure:arm64=1.1.3-1+debian+trixie]

2026-03-11 15:03:58 [ERROR] [mender-convert] mender-convert failed
2026-03-11 15:03:58 [ERROR] [mender-convert] mender-convert exit code: 100
Log file available at: /.../mender-convert/logs/convert.log.1773241320-472563
```

### How to fix

* *Recommended*: choose a supported combination of versions for the Mender software. See [Mender Client Supported Releases](../../302.Release-information/01.Supported-releases/docs.md#mender-client)

* Alternatively, make the script optional by adding the following to your `mender-convert` configuration:
```
MENDER_CLIENT_VERSION_INVENTORY_SCRIPT_INSTALL="auto"
```
