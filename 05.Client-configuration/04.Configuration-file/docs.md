---
title: Configuration file
taxonomy:
    category: docs
---

Much of the Mender client's configuration resides in `/etc/mender/mender.conf`
on the root filesystem. This file is JSON structured and defines various
parameters for Mender's operation. Some of the most common settings are tunable
using [Yocto
variables](../../artifacts/image-configuration/yocto-image-configuration#configuring-polling-intervals). The
remaining parameters can only be changed by providing your own `mender.conf`.


# Providing mender.conf

It is easy to provide your own `mender.conf` file. First you will need to have
your own layer. If you don't already have one see [the Yocto
Manual](http://www.yoctoproject.org/docs/latest/mega-manual/mega-manual.html#creating-your-own-layer)
for how to create one.

Inside the layer, you will need to create a `.bbappend` file for the mender
recipe. It should be placed in a location like this:
`meta-<mylayer>/recipes-mender/mender/mender_%.bbappend`. The content of the
file should be the following:

```
FILESEXTRAPATHS_prepend := "${THISDIR}/files:"
SRC_URI_append = " file://mender.conf"
```

If your layer already contains a `mender_%.bbappend` file, then add the above
contents into your file, taking care to not redefine any variables you are
already using.

Then, inside `meta-<mylayer>/recipes-mender/mender/files/mender.conf`, you can
put whatever configuration options you need, as a JSON structure. The file you
provide will be merged with other settings taken from various variables in the
build, with variables taking precedence.

Here is an example of a `mender.conf` file:

```
{
  "ServerURL": "https://mymenderserver.net",
  "ServerCertificate": "/etc/site-conf/server.crt"
}
```

Note that many mandatory entries are missing, such as `RootfsPartA` and
`RootfsPartB`. These are filled in by the Yocto build system automatically, using
the merge method described in the paragraph above. So you do not need to provide
all values, those that are not provided will take on default values.
