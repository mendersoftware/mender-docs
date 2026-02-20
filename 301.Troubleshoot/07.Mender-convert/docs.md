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

<!--AUTOVERSION: "%-1+ubuntu"/ignore "(>= %)"/ignore-->
```
mender-convert-modify has finished. Cleaning up...
2026-02-19 15:30:09 [ERROR] [mender-convert] mender-convert failed
2026-02-19 15:30:07 [DEBUG] [mender-convert-modify] When running: (modules/chroot.sh:165): run_and_log_cmd():
        sudo chroot work/rootfs/  env         DEBIAN_FRONTEND=noninteractive         DEVICE_TYPE=qemux86-64
        apt --assume-yes --fix-broken --no-remove install  mender-update=5.1.0-1+ubuntu+jammy mender-client4=5.1.0-1+ubuntu+jammy
        mender-auth=5.1.0-1+ubuntu+jammy mender-flash=1.1.0-1+ubuntu+jammy (...)
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 mender-client-version-inventory-script : Conflicts: mender-auth (>= 5.1.0)
                                          Conflicts: mender-flash (>= 1.1.0) but 1.1.0-1+ubuntu+jammy is to be installed
                                          Conflicts: mender-update (>= 5.1.0)
E: Unable to correct problems, you have held broken packages.

2026-02-19 15:30:09 [ERROR] [mender-convert] mender-convert failed
2026-02-19 15:30:09 [ERROR] [mender-convert] mender-convert exit code: 100
Log file available at: /.../mender-convert/logs/convert.log.1771514995-354382
```

### How to fix

* *Recommended*: choose a supported combination of versions for the Mender software. See [Mender Client Supported Releases](../../302.Release-information/01.Supported-releases/docs.md#mender-client)

* Alternatively, make the script optional by adding the following to your `mender-convert` configuration:
```
MENDER_CLIENT_VERSION_INVENTORY_SCRIPT_INSTALL="auto"
```
