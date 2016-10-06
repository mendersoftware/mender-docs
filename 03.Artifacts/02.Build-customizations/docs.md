---
title: Build customizations
taxonomy:
    category: docs
---

In this section we look at some customizations that can be made due to requirements from a certain build or board configuration.

## Disabling Mender as a system service

If you do not want Mender to run as a system service, and you prefer to carry out update steps manually using the command line client interface, you can disable the service that starts Mender at boot.

This is simple to accomplish by adding a `recipes-mender/mender/mender_%.bbappend` file in your Yocto Project layer, with the following content:

```
SYSTEMD_AUTO_ENABLE = "disable"
```

In this case it is also possible to avoid Mender's current dependency on systemd. If you do not wish to enable systemd in your build, instead of inheriting `mender-full` in `local.conf`, you should inherit each of the classes that `mender-full` inherits, except `mender-systemd`. Also, you do not need any daemon-related configraution items in your `conf/local.conf` as outlined in [the section on configuring the Yocto Project build](../../Artifacts/Building-Mender-Yocto-image#configuring-the-build). Currently you can use the following snippet for Mender in your `conf/local.conf` to completely disable Mender as a daemon (but please verify what `mender-full` inherits at the time you make this change):

```
INHERIT += "mender-uboot mender-image mender-install"
MACHINE = "vexpress-qemu"  # replace with the desired machine
```

! If you disable Mender running as a daemon under `systemd`, you must run all required Mender commands from the CLI or scripts. Most notably, you need to run `mender -commit` after booting into and verifying a successful deployment. When running in managed mode, any pending `mender -commit` will automatically be run by the Mender daemon after it starts. See [Modes of operation](../../Architecture/overview#modes-of-operation) for more information about the difference.
