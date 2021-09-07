---
title: Monitor
taxonomy:
    category: docs
    label: user guide
---

!!!!! The Mender Monitor add-on package is required.
!!!!! See [the Mender features page](https://mender.io/plans/features?target=_blank)
!!!!! for an overview of all Mender plans and features.

The Mender Monitor add-on gives you instant visibility into issues
with your device fleet. It allows you to configure alerts to be sent when certain
parts of your infrastructure are malfunctioning
or need your attention.

To save bandwidth and support edge processing, Monitor is a fully
distributed solution, meaning that we send no data from the device
to the server unless triggered by an alert. Compared to classic approaches
of sending all the data about all the nodes to the server all the time,
this leads to massive bandwidth savings and allows instant local processing.

## Alerts

Each time a service is not running, or a log file contains a given pattern, or a
signal is received on a given D-Bus bus, all users that have access to the given
device on the Mender server receive an email notification. You can mute the
email notifications in the Mender Server settings.

There is one exception to the above rule: if a service is going 
up and down often enough (see above FLAPPING_INTERVAL and FLAPPING_COUNT_THRESHOLD)
we consider it to be _flapping_. When we detect this, service subsystem sends
_flapping alert_ and does not send anything else until the number of service
state changes per one FLAPPING_INTERVAL goes below FLAPPING_COUNT_THRESHOLD.

## Architecture
The Monitor add-on consists of two parts: the API to the backend that allows
you to integrate with existing solutions, and a `mender-monitor`
systemd service being a daemon that runs on the devices.
The former is a set of bash functions, which you can call 
from wrappers or use at your own discretion, while the latter
is a simple service that can easily be configured to send alerts
to the Mender Server when certain event occur.

### Running and configuring
To start monitoring daemon it is enough to run the following
command:
```bash
systemctl start mender-monitor
```
The service does normal logging which you can see with the `journalctl -u mender-monitor`
command.

### Examples
Before the detailed description of the add-on configuration and structure
in details, we present two quick-start examples.

#### Is mender-connect running?
Assume you want to monitor the state of the `mender-connect` systemd service,
and you want to receive alerts if the service is not running,
as well as an _OK_ when it is back up. In order to get this
working we will need to create a file in the _monitor.d/available_
directory:

```bash
 echo -e 'SERVICE_NAME="mender-connect"\nSERVICE_TYPE="systemd"' > /etc/mender-monitor/monitor.d/available/service_menderconnect.sh
```
 
and enable it by creating the following symbolic link:

```bash
 ln -s /etc/mender-monitor/monitor.d/available/service_menderconnect.sh /etc/mender-monitor/monitor.d/enabled/service_menderconnect.sh
```

The daemon will automatically pick the files and start checking the log file.


#### Has root user a session?
To alert new root user sessions to the device, we can check for the pattern
`Started User Manager for UID 0` in the `/var/log/syslog` file.
We will need to create the following file:

```bash
 echo -e 'SERVICE_NAME="auth"\nLOG_PATTERN='Started User Manager for UID 0'\nLOG_FILE="/var/log/syslog"' > /etc/mender-monitor/monitor.d/available/log_syslogrootsession.sh
```

and enable the check:

```bash
 ln -s /etc/mender-monitor/monitor.d/available/log_syslogrootsession.sh /etc/mender-monitor/monitor.d/enabled/log_syslogrootsession.sh
```

!!! You can also do Perl-compatible regular expressions (PCRE) pattern matching for the UID to catch users other than root, using for instance:
!!! `LOG_PATTERN='Started User Manager for UID \d+'`
!!! If your device does not support PCRE, it falls back to -E if available or plain grep if not.

## Monitoring subsystems

`mender-monitor` supports _monitoring subsystems_ which perform the actual
monitoring and report to the main daemon. Currently, there are three subsystems
available out-of-the-box: for services, log files and D-Bus signals, but you can
easily provide your own.

The daemon supports the following directory structure:
```bash
# tree /etc/mender-monitor/
/etc/mender-monitor/
`-- monitor.d
    |-- available
    |   |-- log_auth.sh
    |   |-- service_cron.sh
    |   `-- dbus_upower.sh
    |-- enabled
    |   |-- log_auth.sh -> /etc/mender-monitor/monitor.d/available/log_auth.sh
    |   |-- dbus_upower.sh -> /etc/mender-monitor/monitor.d/available/dbus_upower.sh
    |   `-- service_cron.sh -> /etc/mender-monitor/monitor.d/available/service_cron.sh
    |-- log.sh
    |-- dbus.sh
    `-- service.sh

```
In the above example we enabled the log and service subsystems,
by providing links from the `enabled` to the `available` directory.
Each file name in the latter consists of the subsystem name ("service"
, "log" or "dbus" in the above), an underscore, and a name (being an arbitrary
string of letters, to distinguish between the files). The main daemon
follows links from the `enabled` directory and sources them to set
the environment for the execution of `log.sh` and `service.log`, using
the first part of a file name to decide which file from the `monitor.d`
to run. In other words: we take the first part before an underscore
of the file name from the `enabled` directory, append ".sh", prepend
with the path to monitor.d and source resulting path, executing
the subsystem check, using the contents of the file in `enabled` directory
as the environment.

All the implementation of the specific check is common and we store
it in the `monitor.d/<subsystem_name>.sh` files. You can easily
extend it with your own subsystems.

#### Service monitoring subsystem
The service monitoring exposes two variables available from the files
in the `available` directory: `SERVICE_NAME` and `SERVICE_TYPE`.
For example and in the above, the `service_cron.sh` file contains:

```bash
SERVICE_NAME="cron"
SERVICE_TYPE="systemd"
```

which means that we monitor a systemd service responding to a name 
`cron`.

#### Log monitoring subsystem
The log monitoring works in a similar way. The `log_auth.sh` file
from the above example contains:
```bash
SERVICE_NAME="auth"
LOG_PATTERN="session opened for user [a-z0-9]* by"
LOG_FILE="/var/log/auth.log"
```

where `SERVICE_NAME` is arbitrary name used in logging and for identification,
`LOG_PATTERN` is the regular expression we are trying to match to each
line of the logs, and `LOG_FILE` is the path to the log file.

The log subsystem saves the number of the last line of logs that it parsed,
and starts tailing the file skipping the lines that it saw.

Please note that the log monitoring subsystem uses `grep` command
to match lines to a given pattern. By default, and if supported by `grep`
we use the `-P` option, which allows you to use
the [Perl-compatible regular expressions](https://www.pcre.org/).
In case you have no support for `-P`, we use `-E` flag
and if the `-E` support does not exist we use plain `grep`.

#### D-Bus monitoring subsystem

The D-Bus monitoring subsystem exposes three variables from the files in the
`available` directory: `DBUS_NAME`, `DBUS_PATTERN` and `DBUS_WATCH_EXPRESSION`.
For example, the file `dbus_battery.sh` could look like:

```bash
DBUS_NAME="upower"
DBUS_PATTERN=
DBUS_WATCH_EXPRESSION="type='signal',interface='org.freedesktop.DBus.Properties',member='PropertiesChanged',path=/org/freedesktop/UPower/devices/battery_BAT0"
```

Which means an alarm will be raised every time the upower sends a signal over
D-Bus stemming from the battery. Naturally, this can be adapted to pretty much
any pattern you require.
