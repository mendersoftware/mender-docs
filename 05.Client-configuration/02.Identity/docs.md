---
title: Identity
taxonomy:
    category: docs
---

##Definition

Formally, the definition of an identity is a set of key-value attributes.
For example, the identity of a person could be defined as:

```
ID={
Name=Tom Jones
SSN=12345678
Address=Jone's way 3, 1234 Boston
}
```

Which exact attributes are chosen to define an identity depends on the identity
scheme of a given system.	

The Mender client allows the user to define the identity attributes, which means that Mender
can adapt to the identity scheme of any environment. However, Mender imposes the following
requirements for device identities:

* the combination of the attribute values must be *unique* to each device, so that identities are not ambiguous when deploying software
* identity attributes must *never change* for the lifetime of a device, so that a device can be recognized over its lifetime

Note that device keys should not be used as part of identities, because this would make it very difficult to
rotate or regenerate keys over the lifetime of the device as it would in effect change identity.
It is important to have the ability to regenerate keys if a device gets compromised, or as a recurring proactive security measure.


##Example device identities

Even though Mender allows several attributes to make up the device identity,
most environments just use one attribute for simplicity.

The MAC address of the primary interface is a common way to satisfy the requirements for device identity,
for example:

```
ID={
MAC=56:84:7a:fe:97:99
}
```

A serial number from the device can also be used:

```
ID={
SerialNumber=PF021XD5
}
```

In some cases, several attributes are combined to make up the device identity:

```
ID={
Generation=2
Model=3
DeviceNumber=1800
}
```

The Mender client works with all of these schemes, but note that you should only use one of them.
For example, it does not make much sense to use the serial number to identify some devices, but
the MAC address to identify others.


##The Device ID

For convenience it is very useful to always have a fixed-length string that uniquely identifies a
device. Mender implements this by computing a SHA-256 checksum over the identity attributes
and this is referred to as the **Device ID** in Mender.

For example, a Device ID could look like `efd4b192a70ddfee509c0e72904ce093ea57b2782c233840b8086b699bc67d5b`.

Clearly, the Device ID is not human-friendly, so the identity attributes are also transferred and
stored by the Mender server. The Device ID is primarily used for security purposes and software-based
recognition of devices during device authentication, grouping, reporting, and similar cases.


##Implementing a device identity executable

The Mender client obtains the identity attributes by running an executable
(e.g. binary or script) named `mender-device-identity` and parsing its standard output as the identity.
The executable must be placed under the path `/usr/share/mender/identity/mender-device-identity`.

When run, it is expected to produce a set of attributes on
standard output in the following key/value format:

```
key=value\n
```

For example:

```
mac=0a:1b:3d:fe:02:33
cpuid=1234123-ABC
```

Newline characters are stripped, and it is not supported to have newline as part
of values. If such characters may exist they need to be encoded. For example,
a URL-compatible encoding `foo\nbar` becomes `foo%10bar`.

Attributes appearing multiple times will have their values merged into a list.
For example, output

```
mac=0a:1b:3d:fe:02:33
mac=0a:1b:3d:fe:02:34
cpuid=1234123-ABC
```

is conceptually merged into the following representation:

```
mac=[0a:1b:3d:fe:02:33, 0a:1b:3d:fe:02:34]
cpuid=1234123-ABC
```

! The device identity must remain unchanged throughout lifetime of the device. Thus, it is advised to use attributes that will not change or are unlikely to change in the future. Examples of such attributes are device/CPU serial numbers, interface MAC addresses, and in-factory burned EEPROM contents.


## Example device identity executables

Example scripts are provided in the [support directory in the Mender client source code repository](https://github.com/mendersoftware/mender/tree/master/support?target=_blank).
