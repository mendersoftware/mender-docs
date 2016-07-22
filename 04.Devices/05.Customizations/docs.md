---
title: Customizations
taxonomy:
    category: docs
---

In this section we look at some customizations that can be made if a certain board or configuration requires Mender to be used in a non-standard way.

## Disabling Mender as a system service

If you don't want Mender to run as a system service, and you prefer to carry out update steps manually using the command line client interface, you can disable the service that starts Mender at boot.

This is simple to accomplish by adding a `recipes-mender/mender/mender_%.bbappend` file in your Yocto Project layer, with the following content:

```
SYSTEMD_AUTO_ENABLE = "disable"
```

In this case it is also possible to avoid Mender's current dependency on systemd. If you do not wish to enable systemd in your build, instead of inheriting `mender-full` in `local.conf`, you should inherit each of the classes that `mender-full` inherits, except `mender-systemd`. Currently this is the following list:

```
INHERIT += "mender-uboot mender-image mender-install"
```
