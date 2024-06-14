---
title: Inventory
taxonomy:
    category: docs
---

We recommend that you first read the [overview on Inventory](../../02.Overview/08.Inventory) in order to familiarize yourself with the concept and how it is used in Mender. This tutorial is about how to change the Inventory attributes reported by the Mender client.


## Basic rules for inventory attributes

Periodically, the Mender client runs every executable file with
the `mender-inventory-` prefix from the `/usr/share/mender/inventory` directory.
It then parses each line read from the standard output of the script according
to the following format:

```
name0=value0\n
.
.
nameN=valueN\n
```
The client reports the attributes via the [device inventory service API calls](../../200.Server-side-API/?target=_blank#device-api-device-inventory-assign-attributes), by issuing **PATCH** _/device/attributes_.


### Lists of values

The client merges attributes appearing multiple times into lists.
For example, the following output from the inventory executable:

```
interface=eth0
ip_address_eth0=192.168.1.1
interface=wlan0
ip_address_wlan0=172.27.1.1
```

will lead to the following attributes:

```
interface = [eth0, wlan0]
ip_address_eth0 = 192.168.1.1
ip_address_wlan0 = 172.27.1.1
```

### Special characters

You cannot use a literal new line character in attribute names or values.
To support new lines or other special characters, use URL-style encoding.
For instance, if you want to encode:
```
multilinekey=value1\nvalue0
```
you have to use:
```
multilinekey=value1%0Avalue0
```

## Example inventory script

Let's assume you want to create a group of devices called "LinuxDevicesInKrakow".
To achieve this, obviously we need to collect the information from the device about
its localization and deliver it to the server. Your best choice to do it in a portable
manner, is to use an inventory attribute script. The following listing shows an
example of such a script, gathering information on the localization from the network.

<!--AUTOVERSION: "curl/%"/ignore-->
```bash
#!/bin/sh
#
# The example script collects geo localization information
#
err() {
 local rc=$1

 shift
 echo "${0}: $*" >&2
 exit $rc
}

# find the ip address
ip=`wget -qO /dev/stdout --header "Content-Type: text/plain;" \
     --header 'Host: ifconfig.io' --header 'User-Agent: curl/7.67.0' \
     --header 'Accept: */*' ifconfig.io | tail -1`

[ -n "${ip}" ] || err 2 "Unable to get the IP address from ifconfig.io"

# get the information, see https://www.ipvigilante.com/api-developer-docs/
geo=`wget -qO /dev/stdout https://ipvigilante.com/csv/${ip} 2>/dev/null`

[ -n "${geo}" ] || err 3 "Unable to get the geolocalization data from ipvigilante.com"

# the names of the attributes holding the localization data can be configured here
ATTR_NAME_IP="a-ip"
ATTR_NAME_CONTINENT="a-continent"
ATTR_NAME_COUNTRY="a-country"
ATTR_NAME_CITY="a-city"

echo "${geo}" | awk -v ip="${ATTR_NAME_IP}" -v continent="${ATTR_NAME_CONTINENT}" \
    -v country="${ATTR_NAME_COUNTRY}" -v city="${ATTR_NAME_CITY}" -F',' \
    ' length($NF) == 0 { exit(4) }
      { printf("%s=%s\n%s=%s\n%s=%s\n%s=%s\n",ip,$1,continent,$2,country,$3,city,$6) }
    '
```

The above example first gets the public source ip address of the IP packets originating
from the device. It then calls an API endpoint to get the geo localization data, parses
the response data, and finally prints it to standard output
in the format "attribute_name=attribute_value". You should store this script
in the `/usr/share/mender/inventory`
directory, giving it a name, for example `mender-inventory-geo.sh` and executable permissions:

```bash
chmod 700 /usr/share/mender/inventory/mender-inventory-geo.sh
```
Example output of the above script looks like this:
```
a-ip=x.x.x.x
a-continent=Europe
a-country=Poland
a-city=Krakow
```
<!--AUTOVERSION: "mender/tree/%/support"/mender-->
You can find some more useful scripts in [https://github.com/mendersoftware/mender/support](https://github.com/mendersoftware/mender/tree/3.5.3/support) directory.


## Default inventory

By default, and without any inventory scripts added, the Mender client sends the following attributes:

<!--AUTOVERSION: "client version | \"%\""/mender-->
| name | meaning | example value |
|:----:|:-------:|:-------------:|
| `device_type`  | type of the device | "raspberrypi4" |
| `artifact_name` | name of the currently installed artifact | "release-v1" |
| `mender_client_version` | client version | "3.5.3" |


## Final remarks
You should not use inventory attributes to uniquely identify a device. They are
intended  to store information,
for searching, sorting and filtering devices in the Mender Server.
