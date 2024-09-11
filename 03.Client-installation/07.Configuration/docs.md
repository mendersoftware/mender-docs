---
title: Configuration
taxonomy:
    category: docs
---

Much of the Mender client's configuration resides in `/etc/mender/mender.conf`
on the root filesystem. This file is JSON structured and defines various
parameters for Mender's operation.

On systems where one or more of the configuration options must survive future
updates, there is an optional "fallback" configuration file in
`/var/lib/mender/mender.conf`. Because the directory `/var/lib/mender` is on
persistent storage, the fallback configuration file is not overwritten by Mender
updates.

The fallback configuration file has the same JSON structure as the main
configuration file. Any value set in the main configuration file
`/etc/mender/mender.conf` is chosen, whether or not the setting appears in the
fallback file `/var/lib/mender/mender.conf`. The client only uses a setting in
the fallback file if it does not appear in the main file.

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

The mechanism for providing the configuration file and specifying the configuration values will depend on your choice of OS distribution or build system.

If you have already built an Artifact containing the rootfs, have a look at [modifying a Mender Artifact](../../06.Artifact-creation/03.Modify-an-Artifact/docs.md).


# Configuring system paths

The following table describes the different system paths that the Mender client uses and the
associated environment variables used to customize them.

| Description             | Default path        | Environment variable   |
| ----------------------- | ------------------- | ---------------------- |
| Configuration directory | `/etc/mender`       | `MENDER_CONF_DIR`      |
| Data directory          | `/usr/share/mender` | `MENDER_DATA_DIR`      |
| Persistent datastore    | `/var/lib/mender`   | `MENDER_DATASTORE_DIR` |
