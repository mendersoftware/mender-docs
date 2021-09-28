---
title: Monitoring subsystems
taxonomy:
    category: docs
---

`mender-monitor` supports _monitoring subsystems_ which perform the actual
monitoring and report to the main daemon. Currently, there are three subsystems
available out-of-the-box: for services, log files and D-Bus signals, but you can
easily extend it and implement your own.

The daemon supports the following directory structure:
```bash
tree /etc/mender-monitor/
```
> ```bash
> /etc/mender-monitor
> `-- monitor.d
>     |-- available
>     |   |-- log_auth_root_session.sh
>     |   `-- service_mender-connect.sh
>     |-- dbus.sh
>     |-- enabled
>     |   |-- log_auth_root_session.sh -> /etc/mender-monitor/monitor.d/available/log_auth_root_session.sh
>     |   `-- service_mender-connect.sh -> /etc/mender-monitor/monitor.d/available/service_mender-connect.sh
>     |-- log.sh
>     `-- service.sh
> ```

In the above example, we enabled the log and service subsystems
by providing links from the `enabled` to the `available` directory.
Each file name in the latter consists of the subsystem name ("service",
"log" or "dbus"), an underscore, and a name (being an arbitrary
string of letters to distinguish between the files). The main daemon
follows links from the `enabled` directory and sources them to set
the environment for the execution of `log.sh` and `service.log`, using
the first part of a file name to decide which file from the `monitor.d`
to run. In other words: we take the first part before an underscore
of the file name from the `enabled` directory, append ".sh", prepend
with the path to monitor.d and source resulting path, executing
the subsystem check, using the contents of the file in `enabled` directory
as the environment.

The specific check's implementation is common and we store it in
the `monitor.d/<subsystem_name>.sh` files. You can easily extend
the `mender-monitor` service implementing your custom subsystems.

## Service

Service monitoring expects two variables from the files in the
`available` directory: `SERVICE_NAME` and `SERVICE_TYPE`.

For example, a `service_cron.sh` file could contain:

```bash
SERVICE_NAME="cron"
SERVICE_TYPE="systemd"
```

which means that we monitor the `cron` systemd service.

## Log

The log monitoring works similarly. The `log_auth_root_session.sh` file
from the above examples could contain:

```bash
SERVICE_NAME="auth_root_session"
LOG_PATTERN="session opened for user [a-z0-9]* by"
LOG_FILE="/var/log/auth.log"
```

where `SERVICE_NAME` is an arbitrary name used in logging and for identification,
`LOG_PATTERN` is the regular expression we are trying to match to each
line of the logs and `LOG_FILE` is the path to the log file.

The log monitoring subsystem saves the number of the last line of logs that
it parsed and starts tailing the file skipping the already seen lines.

The log monitoring subsystem uses the `grep` command to match lines to a given pattern
By default, and if supported by `grep` we use the `-P` option, which allows you to use
the [Perl-compatible regular expressions](https://www.pcre.org/).
If you have no support for `-P`, it falls back to the `-E` flag, and
eventually uses plain `grep`.

## D-Bus

The D-Bus monitoring subsystem expects three variables from the files in the
`available` directory: `DBUS_NAME`, `DBUS_PATTERN` and `DBUS_WATCH_EXPRESSION`.

For example, a file `dbus_battery.sh` could contain:

```bash
DBUS_NAME="upower"
DBUS_PATTERN=""
DBUS_WATCH_EXPRESSION="type='signal',interface='org.freedesktop.DBus.Properties',member='PropertiesChanged',path=/org/freedesktop/UPower/devices/battery_BAT0"
```

Every time a D-Bus signal matching the watch expression is received,
an alert will be triggered and sent from the monitoring subsystem.
You can adapt the configuration to any D-Bus signal and pattern based
on your use case.
