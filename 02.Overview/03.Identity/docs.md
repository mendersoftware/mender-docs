---
title: Identity
taxonomy:
    category: docs
    label: reference
---

##Definition

An identity is a set of key-value attributes.
For example, you could describe a person as:

```
ID={
Name=Tom Jones
SSN=12345678
Address=Jone's way 3, 1234 Boston
}
```

Which exact attributes make up an identity depends on the identity
scheme of a given system.

The Mender client allows the user to define the identity attributes, which means that Mender
can adapt to the identity scheme of any environment. However, Mender imposes the following
requirements for device identities:

* the combination of the attribute values must be *unique* to each device, so that identities are not ambiguous when deploying software
* identity attributes must *never change* for the lifetime of a device, so that the Mender server can recognize them reliably

Do not use device keys as part of an identity, because this will make it very difficult to
rotate or regenerate keys over the lifetime of the device (as it would in effect change identity).
It is important to have the ability to regenerate keys if a device gets compromised, or as a recurring proactive security measure.


##Example device identities

Even though Mender allows several attributes to make up the device identity,
most environments just use one attribute for simplicity.

For example, a MAC address of the primary interface satisfies the requirements for device identity:

```
ID={
MAC=56:84:7a:fe:97:99
}
```

You could also use the serial number of a device:

```
ID={
SerialNumber=PF021XD5
}
```

In some cases, several attributes form a device identity:

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
device. The Mender server implements this by assigning a unique **Device ID** to a device
as it connects to the server.

For example, a Device ID could look like `594019224d36350001fc5cc3`.

Clearly, the Device ID is not human-friendly, so the identity attributes are also transferred and
stored by the Mender server. The Device ID is primarily used for security purposes and software-based
recognition of devices during device authentication, grouping, reporting, and similar cases.


##Implement a device identity executable

The Mender client obtains the identity attributes by running an executable
(e.g. binary or script) named `mender-device-identity` and parsing its standard output as the identity.
The executable lives under `/usr/share/mender/identity/mender-device-identity`.

The executable must produce a set of attributes on
standard output in the following key/value format:

```
key=value\n
```

For example:

```
mac=0a:1b:3d:fe:02:33
cpuid=1234123-ABC
```

Newline characters are not supported and will be stripped.
If you want to include them, encode them in a URL format (`foo\nbar` becomes `foo%10bar`).

If an attribute appears multiple times, it will translate to a list.
For example, this output:

```
mac=0a:1b:3d:fe:02:33
mac=0a:1b:3d:fe:02:34
cpuid=1234123-ABC
```

will translate to:

```
mac=[0a:1b:3d:fe:02:33, 0a:1b:3d:fe:02:34]
cpuid=1234123-ABC
```

! The device identity must remain unchanged throughout lifetime of the device. Use attributes that will not change or are unlikely to change in the future. Examples of such attributes are device/CPU serial numbers, interface MAC addresses, and in-factory burned EEPROM contents.


## Example device identity executables

<!--AUTOVERSION: "mender/tree/%"/mender-->
Example scripts are provided in the [support directory in the Mender client source code repository](https://github.com/mendersoftware/mender/tree/master/support?target=_blank).

