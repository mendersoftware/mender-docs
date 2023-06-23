---
title: How to make an apply-device-config script
taxonomy:
    category: docs
    label: tutorial
---

## Installation

See [this](https://hub.mender.io/t/mender-configure-update-module/3529) article on [Mender Hub](https://hub.mender.io).

## apply-device-config scripts

`apply-device-config` scripts are custom scripts, which can be installed into
the `/usr/lib/mender-configure/apply-device-config.d` directory. They are then
executed by the Configure Update Module, with the expected configuration
parameters from the Mender Server. In this way, you can extend Mender-Configure
to you needs and keep your device configuration in sync.

## How to write an apply-device-config script

`apply-device-config` scripts are simple shell (`/bin/sh`) scripts, which take
one parameter: _the JSON configuration values file_. The script is then
responsible for parsing the value from the _JSON_ configuration, and then apply
this to the system. See the examples in the [examples section](#examples) for
inspiration.

!! Scripts are always run with the entire configuration, even if there is no configuration available for this particular script. This means that you should be careful to either: use a default value, or have it simply act as a no-op, and then exit with success.

!! All scripts in `/usr/lib/mender-configure/apply-device-config.d` are run in lexicographic order.

## Examples

### Device time zone configuration

To get a feel for the main parts of a configuration script, let us dissect the time zone script:

1. [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix))

```
#!/bin/sh
```

2. Input parameter verification

```
if [ $# -ne 1 ]; then
    echo "Must be invoked with exactly one argument: The JSON configuration." 1>&2
    exit 2
fi

CONFIG="$1"

if ! [ -e "$CONFIG" ]; then
    echo "Error: $CONFIG does not exist." 1>&2
    exit 1
fi
```

3. Extract and apply the configuration

```
TIMEZONE="$(jq -r -e .timezone < "$CONFIG")"
return_code=$?
case $return_code in
    0)
        # Add new timezone
        echo $TIMEZONE >/etc/timezone
        # Remove existing symlink between localtime and timezone definition
        rm /etc/localtime
        # Reload local time as per /etc/timezone file and
        # create a symlink to a new timezone definition
        dpkg-reconfigure -f noninteractive tzdata
        exit $?
        ;;
    1)
        # Result was null, there is no timezone configuration, nothing to do.
        echo "No timezone configuration found."
        exit 0
        ;;
    *)
        exit $return_code
        ;;
esac
```

!! Note that this script relies on [`jq`](https://stedolan.github.io/jq/) to parse the _JSON_ input, which might not be present in all _Linux_ distributions by default. All scripts must have some way of parsing the input _JSON_.

### Simple wrapper which tweaks the parameters before calling a binary

```
#!/bin/sh
# Script which takes arguments from the configuration and runs COMMAND

if [ $# -ne 1 ]; then
    echo "Must be invoked with exactly one argument: The JSON configuration." 1>&2
    exit 2
fi

CONFIG="$1"

if ! [ -e "$CONFIG" ]; then
    echo "Error: $CONFIG does not exist." 1>&2
    exit 1
fi

ARGUMENTS="$(jq -r -e '."mender-demo-command-wrapper"' < "$CONFIG")"

return_code=$?
case $return_code in
    0)
        # Success, continue below.
        :
        ;;
    1)
        echo "No mender-demo-command-wrapper configuration found." >&2
        exit 0
        ;;
    *)
        exit $return_code
        ;;
esac

some-command "$ARGUMENTS"

return_code=$?
if [ $return_code -ne 0 ]; then
    echo "Applying the command with configuration $ARGUMENTS failed" >&2
fi

exit $return_code
```

### Configure your device with different interpreters

Since the scripts interpreter is controlled by the header
[shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)), you can configure your
device using any interpreter present on your device.

As an example of this, let us write a simple configuration program in _Python_,
following the three main steps outlined above:


1. [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix))

```
#!/usr/bin/python

import json
import os.path
import subprocess
import sys
```

2. Input parameter verification

```
if len(sys.argv) != 2:
    print("Must be invoked with exactly one argument: The JSON configuration.", file=sys.stderr)
    sys.exit(1)

config=sys.argv[1]

if not os.path.exists(config):
    print(f"Error: {config} does not exist.", file=sys.stderr)
    sys.exit(1)
```

3. Extract and apply the configuration

```
try:
    configJSON = json.load(config)
    timezone = configJSON["timezone"]
    # Add new timezone
    with open("/etc/timezone", "w") as f:
        f.write(timezone)
    # Remove existing symlink between localtime and timezone definition
    subprocess.run(["rm", "/etc/localtime"], check=True)
    # Reload local time as per /etc/timezone file and
    # create a symlink to a new timezone definition
    subprocess.run(["dpkg-reconfigure", "-f", "noninteractive", "tzdata"], check=True)
except json.JSONDecodeError as e:
    print(f"Failed to parse the configuration JSON, error: {e}")
    sys.exit(1)
except subprocess.CalledProcessError as e:
    print(f"Setting the timezone with timedatectl failed with error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Failed with unhandled error: {e}")
    sys.exit(1)
```
