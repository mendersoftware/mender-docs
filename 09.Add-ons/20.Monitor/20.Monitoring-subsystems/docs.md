---
title: Monitoring subsystems
taxonomy:
    category: docs
---

`mender-monitor` supports _monitoring subsystems_ which perform the actual
monitoring and report to the main daemon. Currently, there are three subsystems
available out-of-the-box: for services, log files and D-Bus signals, but you can
easily extend it and implement your own.

In addition to the present documentation, we also provide a command line tool: `mender-monitorctl` to ease the interaction with the internals
of the Monitor add-on on a device. The tool has online help which you can consult
for a summary of options and examples by running:

```bash
mender-monitorctl help
```

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

### Capturing logs from arbitrary sources

With the log subsystem you are not limited to log files only. You can get the logs
from any command. You can achieve it via so-called _log streamline extension_.
It is a simple mechanism that allows you to provide any command that produces data
on standard output to which the log monitoring will perform pattern matching and alerting.

The general syntax to enable the streamline logs extension is to use `@` character
in the `LOG_FILE`:

```bash
mender-monitorctl create log custom_logs "User logged out due to security policy: \w+" "@/opt/bin/logs-secure.sh"
```

Where `/opt/bin/logs-secure.sh` is any executable command printing to standard output.

As we saw in the [Get started](../../../01.Get-started/05.Monitor/docs.md) section
the `journalctl` command can be a source of logs, but we do not limit the mechanism
to any particular command. The only requirement is that the command prints
to standard output so that the log subsystem will parse it.

#### Docker logs

One example of a command that can output data to standard error is `docker logs`.
In case you want to get alerts based on the patterns that maybe present
in the standard error stream, you can configure the check as follows:

```bash
mender-monitorctl create log docker_logs "Exception \d+-\w+ found" "@/opt/bin/dockerlogs_wrapper"
```

where `/opt/bin/dockerlogs_wrapper` is a wrapper around the docker logs command:

```bash
cat <<EOF > /opt/bin/dockerlogs_wrapper
#!/bin/bash
docker logs my_service -f 2>&1
EOF
chmod 755 /opt/bin/dockerlogs_wrapper
```

With the above you can configure alerting based on any source.
Please note that the `-f` flag above is essential, the command that you pass
via the `@` extension, must not exit.


#### Docker events

The Log Subsystem is a base for so-called _pseudo subsystems_. One of them
is the `dockerevents` subsystem, which you can use to monitor any events as reported by `docker events`
command.

For instance, to monitor for `kill` event on a container named `scanner` you need to create a check with `mender-monitorctl`
command and enable it in the following way:

```bash
sudo mender-monitorctl create dockerevents scanner_kill scanner kill 16
sudo mender-monitorctl enable dockerevents scanner_kill
sudo systemctl restart mender-monitor
```

With the above configuration you will receive a `CRITICAL` alert if someone or something kills your scanner container.
This will lead the Mender UI to present the device in a critical monitoring state. Since there is no natural
way to recover from this situation, we are using the last and optional argument
to the `mender-monitorctl create dockerevents` command which stands for the number of seconds
after which the Mender Monitor daemon sends an automatic OK. In that way after 16s without
a `kill` event on the container the device will recover to normal state.

The resulting check uses the log monitor, as you can see with:
```bash
cat /etc/mender-monitor/monitor.d/available/log_scanner_kill.sh
```

> ```bash
> # This file was autogenerated by Monitoring Utilities based on the configuration
> SERVICE_NAME="scanner_kill"
> LOG_PATTERN=".*container kill.*name=scanner.*"
> LOG_FILE="@docker events"
> LOG_PATTERN_EXPIRATION=16
> LOG_ALERT_DESCRIPTION="Docker container scanner kill"
> LOG_ALERT_DETAILS="Alert was raised due to:%line_matching"
> LOG_ALERT_STATUS=DOCKEREVENTS_CONTAINER_RESTART
> LOG_ALERT_TYPE=docker_event
> ```

### Log pattern expiration

Once the pattern shows up in the logs, Mender Monitor add-on will send a critical alert.
Technically there would be no way out of this situation; the device would stay
in the "critical" state forever. Monitor add-on provides a way to send
the _"OK"_ alert after a period of time defined by `LOG_PATTERN_EXPIRATION`
in the check. This variable is defined either directly on the check
or by the last argument to the `mender-monitorctl create log name pattern file expiration`
command.

See also the configuration of the [DEFAULT_LOG_PATTERN_EXPIRATION_SECONDS](../30.Advanced-configuration/docs.md#DEFAULT_LOG_PATTERN_EXPIRATION_SECONDS).

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
