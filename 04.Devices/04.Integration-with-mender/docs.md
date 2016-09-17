---
title: Integrating with mender
taxonomy:
    category: docs
---


## Identity

Bootstrap and authorization process requires access to device identity. Identity
information is obtained by running a user provided integration tool
`mender-device-identity`. The tool must be placed under
`/usr/share/mender/identity` path.

When run, the identity tool is expected to produce a set of attribute in it's
standard output in the following key/value format:

```
attribute=value\n
```

For instance:

```
mac=0a:1b:3d:fe:02:33
cpuid=1234123-ABC
```

New line characters are stripped. New line characters appearing as part of value
are not supported. If such characters may exist, they need to be encoded using,
for instance, a URL-compatible encoding `foo\nbar` becomes `foo%10bar`.

Attributes appearing multiple times will use the value appearing last in the
tool's output.

! Device identity remains unchanged throughout device lifetime. Thus, it is
advised to use attributes that will not change or are unlikely to change in the
future. Examples of such attributes are device/CPU serial numbers, interface MAC
addresses, in-factory burned EEPROM contents.

## Inventory

Mender client will periodically collect inventory related data for upload to the
backend. This data is obtained by running user provided tools located in
`/usr/share/mender/inventory` directory. Mender client will list and run files
that are executable and have `mender-inventory-` prefix. Other files are
ignored. Each tool may be a simple shell script or a binary.

When run, the inventory tool is expected to produce a set of attribute in it's
standard output in the following key/value format:

```
attribute=value\n
```

For instance:

```
host=foobar
ip=192.168.1.1
```

New line characters are stripped. New line characters appearing as part of value
are not supported. If such characters may exist, they need to be encoded using,
for instance, a URL-compatible encoding `foo\nbar` becomes `foo%10bar`.

Attributes appearing multiple times will have their values merged into a list.
For instance the following output:

```
interface=eth0
ip_address_eth0=192.168.1.1
interface=wlan0
ip_address_wlan0=172.27.1.1
```

is conceptually merged into such representation:

```
interface = [eth0, wlan0]
ip_address_eth0 = 192.168.1.1
ip_address_wlan0 = 172.27.1.1
```

## Examples

Example scripts are provided in mender client source code repository under
`support/`.
