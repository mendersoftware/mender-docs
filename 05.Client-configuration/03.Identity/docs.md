---
title: Identity
taxonomy:
    category: docs
---

##Example device identities

Even though Mender allows several attributes to make up the device identity,
most environments just use one attribute for simplicity.

For example, a MAC address of the primary interface satisfies the requirements for device identity:

```
ID={
MAC=56:84:7a:fe:97:99
}
```

Another example would be an eMMC CID:

```
ID={
# cat /sys/class/mmc_host/mmc0/mmc0\:0001/cid 
CID=90014a484247346132a4528894a9a300
}
```

You can also use the serial number of a device:

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

You cannot use Newline characters as they will be stripped.
If you want to include them, encode them in a URL format (`foo\nbar` becomes `foo%0Abar`).

If an attribute appears multiple times, the client will translate it to a list.
For example, this output:

```
mac=0a:1b:3d:fe:02:33
mac=0a:1b:3d:fe:02:34
cpuid=1234123-ABC
```

will result in the following attributes:

```
mac=[0a:1b:3d:fe:02:33, 0a:1b:3d:fe:02:34]
cpuid=1234123-ABC
```

! The device identity must remain unchanged throughout lifetime of the device. Use attributes that will not change or are unlikely to change in the future. Examples of such attributes are device/CPU serial numbers, interface MAC addresses, and in-factory burned EEPROM contents.


## Example device identity executables

<!--AUTOVERSION: "mender/tree/%"/mender-->
Example scripts are provided in the [support directory in the Mender client source code repository](https://github.com/mendersoftware/mender/tree/master/support?target=_blank).

