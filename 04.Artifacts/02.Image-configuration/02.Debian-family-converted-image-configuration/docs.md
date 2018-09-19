---
title: Image configuration for Debian systems
taxonomy:
    category: docs
---

Mender conversion script `./mender-conversion-tool.sh  make_all` can be adjusted according to production needs.

It is possible to pass the hosted Mender token as an argument:

```bash
--hosted-token <name of token for hosted.mender.io service>
```

A different address for the update server can be provided as an argument:

```bash
--production-url <url to production server>
```
It is possible to provide the authentication certificate as an argument:

```bash
--certificate <name of the certificate>
```
