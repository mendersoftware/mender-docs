---
title: Configuration file
taxonomy:
    category: docs
---

Much of the Mender client's configuration resides in `/etc/mender/mender.conf`
on the root filesystem. This file is JSON structured and defines various
parameters for Mender's operation.

On systems where it is desired for one or more of the configuration options
to be customized and survive future updates, there is an optional "fallback"
configuration file `/var/lib/mender/mender.conf`. Because the directory
`/var/lib/mender` is backed by persistent storage, the fallback configuration
file will not be overwritten by Mender updates.

The fallback configuration file has the same JSON format as the main configuration file.
Any setting value that appears in the main configuration file `/etc/mender/mender.conf`
will be used, whether or not the setting appears in the fallback file `/var/lib/mender/mender.conf`.
Therefore a setting in the fallback file will only be used if it does not appear
in the main file.

# Example mender.conf file

Here is an example of a `mender.conf` file:
```
{
  "RootfsPartA": "/dev/hda2",
  "RootfsPartB": "/dev/hda3",
  "ServerURL": "https://mymenderserver.net",
  "ServerCertificate": "/etc/site-conf/server.crt"
}
```

# Providing mender.conf

The mechanism for providing the configuration file and specifying the configuration values will depend on your choice of OS distribution or build system.(TODO: Links)

If you have already built an Artifact containing the rootfs, have a look at [modifying a configuration in a Mender Artifact](../../../04.Artifacts/25.Modifying-a-Mender-Artifact/docs.md#modifying-a-configuration-file).



