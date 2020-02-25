---
title: Inventory
taxonomy:
    category: docs
    label: reference
---

Inventory is a set of simple key-value attributes that are useful know about a
device, similar to the [device identity attributes](../identity). However, the
device inventory attributes are not used to uniquely identify over time, they
are just informational. As such, they do not need to be unique for each device
like the device identity attributes.

The Mender client will periodically collect inventory-related data for reporting
to the Mender server. This data is obtained by running executables located in
the directory `/usr/share/mender/inventory`. The Mender client will list and run
files that are executable and have `mender-inventory-` prefix. Other files are
ignored. Each executable may be a simple shell script or a binary.

When run, the executable is expected to produce a set of attribute on its
standard output in the following key/value format:

```
attribute=value\n
```

For example, a script could produce the following output:

```
host=myhostname
ip=192.168.1.1
```

Newline characters are stripped, and it is not supported to have newline as part
of values. If such characters may exist they need to be encoded. For example, a
URL-compatible encoding `foo\nbar` becomes `foo%10bar`.

##Creating lists

Attributes appearing multiple times will have their values merged into a list.
For example, the following output

```
interface=eth0
ip_address_eth0=192.168.1.1
interface=wlan0
ip_address_wlan0=172.27.1.1
```

is conceptually merged into the following representation:

```
interface = [eth0, wlan0]
ip_address_eth0 = 192.168.1.1
ip_address_wlan0 = 172.27.1.1
```
