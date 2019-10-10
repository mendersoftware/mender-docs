---
title: Upgrading
taxonomy:
    category: docs
---

This section describes the cases where upgrading from one Yocto release to the
next requires special attention.

## Upgrades with incompatible changes

<!--AUTOVERSION: "From % to %"/ignore-->
### From thud to warrior

<!--AUTOVERSION: "meta-mender % branch"/ignore-->
The meta-mender warrior branch introduces a change for the configuration of
Mender. Now the configuration is split between a transient configuration file in
`/etc/mender/mender.conf` and a persistent configuration file in
`/data/mender/mender.conf`, see
[MEN-2757](https://tracker.mender.io/browse/MEN-2757).

A device running on a single configuration file cannot upgrade to an image built
with two configuration files feature.

There are two possibilities:

* Create an update with migration steps.

This method is preferred as it will let the device(s) take advantage of this
feature in future updates.

To enable migration please add the following to your local.conf or similar:

```bash
IMAGE_INSTALL_append = " mender-migrate-configuration"
PACKAGECONFIG_remove = "split-mender-config"
MENDER_PERSISTENT_CONFIGURATION_VARS = "RootfsPartA RootfsPartB"
MENDER_ARTIFACT_EXTRA_ARGS_append = " -v 2"
```

Build an image with above configuration and deploy it your device fleet. Once
all devices in the fleet have been updated with the migration script enabled you
can remove these changes and return to the normal workflow of generating update
Artifacts.

Note that `mender-migrate-configuration` recipe uses a state script, and it
might be needed to clean the yocto build after removing it. See note at [State
Scripts](../../artifacts/state-scripts#including-state-scripts-in-artifacts-and-disk-images)

* Permanently disable this feature.

If it is not desired to use this feature, it can be disabled by adding
`PACKAGECONFIG_remove = "split-mender-config"` to local.conf. Note that with
this option the feature will need to be disable for all future builds.
