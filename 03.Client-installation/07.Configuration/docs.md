---
title: Configuration
taxonomy:
    category: docs
---

Much of the Mender Client's configuration resides in `/etc/mender/mender.conf`
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


# Environment variables

The following table describes the environment variables the Mender Client respects:

| Environment variable   | Description                             | Default value       |
| ---------------------- | --------------------------------------- | ------------------- |
| `MENDER_CONF_DIR`      | Configuration directory                 | `/etc/mender`       |
| `MENDER_DATA_DIR`      | Data directory                          | `/usr/share/mender` |
| `MENDER_DATASTORE_DIR` | Persistent datastore                    | `/var/lib/mender`   |
| `HTTP_PROXY`           | Proxy server to use for HTTP            | empty               |
| `HTTPS_PROXY`          | Proxy server to use for HTTPS           | empty               |
| `NO_PROXY`             | Hosts that should not go through proxy  | empty               |

The `HTTP_PROXY` and `HTTPS_PROXY` variables can specify authentication parameters using the `user:password@host` URL
format. The `NO_PROXY` variable uses a space-separated list as format and its items can be domain suffixes/wildcards
like for example `.example.com` for bypassing proxy for all `*.example.com` URLs.
