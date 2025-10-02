---
title: Configuration
taxonomy:
    category: docs
---
## Global variables

The `mender-monitor` daemon reads the configuration settings from the file
`/usr/share/mender-monitor/config/config.sh`. The default settings are suitable
for most use-cases, but you can adjust the following configuration variables
if you need to customize the functionalities.

### ALERT_LOG_MAX_AGE

The maximum number of seconds for which we keep the alerts in memory for flapping detection.

### ALERT_OFFLINE_STORE_MAX_COUNT

The maximum number of alerts to store if the device is offline.

### ALERT_URL

The back-end URL `mender-monitor` will send the alerts to.

### CONFIG_LOG_LEVEL

A string defining the log level; the possible values are: `FATAL`, `TRACE`, `ERROR`, `DEBUG`, `WARN` or `INFO`.

### DAEMON_LOG_FILE

The path to the daemon's log file.

### DEFAULT_ALERT_LEVEL

The default alert level.

### DEFAULT_ALERT_STORE_RESEND_INTERVAL_S

The default number of seconds in between every attempt to resend an alert in the case of failure.

### DEFAULT_DBUS_ALERT_EXPIRATION_SECONDS

The default dbus pattern expiration period, expressed as a number of seconds, if not set in the check configuration file with `DBUS_PATTERN_EXPIRATION`.

### DEFAULT_DBUS_ALERT_LEVEL

The default alert level for the D-Bus monitoring subsystem. Its default value is `CRITICAL`.

### DEFAULT_LOG_ALERT_LEVEL

The default alert level for the log monitoring subsystem.

### DEFAULT_LOG_LINES_AFTER

The default number of lines sent after a line that contained a string that matched a given pattern.

### DEFAULT_LOG_LINES_BEFORE

The default number of lines sent before a line that contained a string that matched a given pattern.

### DEFAULT_LOG_PATTERN_EXPIRATION_SECONDS

The default log pattern expiration period, expressed as a number of seconds, if not set in the check configuration file with `LOG_PATTERN_EXPIRATION`.

### DEFAULT_SERVICE_ALERT_LEVEL

The default alert level for the service monitoring subsystem.

### FLAPPING_COUNT_THRESHOLD

The number of service state changes per `FLAPPING_INTERVAL` (see above), after which we consider a service to be flapping.

### FLAPPING_INTERVAL

The time interval, expressed as a number of seconds, for which we calculate the flapping rate.

### MONITOR_D_DIRECTORY

The path to the `monitor.d` directory.

## DBus subsystem variables

These are variables you can set per check that uses the DBus subsystem, if these ones are not set, then ones starting with `DEFAULT_` from [the previous section](#global-variables) will take precedence.

### DBUS_ALERT_EXPIRATION

The dbus pattern expiration period expressed as a number of seconds. Optional, if not set, it will use the global configuration `DEFAULT_DBUS_ALERT_EXPIRATION_SECONDS`.

### DBUS_NAME

The name of the watcher.

### DBUS_PATTERN

The grep pattern to match on. An empty value will match on all notifications.
To avoid message flooding, it is required to set either `DBUS_PATTERN` or `DBUS_WATCH_EXPRESSION`.

### DBUS_WATCH_EXPRESSION

The watch pattern passed to dbus-monitor (can be empty). e.g.,  `type='signal',interface='org.freedesktop.DBus.Properties',member='PropertiesChanged',path=/org/freedesktop/UPower/devices/battery_BAT0`
To avoid message flooding, it is required to set either `DBUS_PATTERN` or `DBUS_WATCH_EXPRESSION`.

## Log subsystem variables

These are variables you can set per check that uses the Log subsystem, if these ones are not set, then ones starting with `DEFAULT_` from [the previous section](#global-variables) will take precedence.

### LOG_PATTERN

Pattern searched inside the `LOG_FILE`.

### LOG_FILE

Path to the log file to watch for a regular expression match.

### LOG_ALERT_LEVEL

The alert level for the log monitoring subsystem. If not set, `DEFAULT_LOG_ALERT_LEVEL` value will be used.

### LOG_PATTERN_EXPIRATION

The log pattern expiration period, expressed as a number of seconds. If not set the `DEFAULT_LOG_PATTERN_EXPIRATION_SECONDS` will be used.

### SERVICE_NAME

Identifier for the check definition.

## Service subsystem variables

These are variables you can set per check that uses the Service subsystem, if these ones are not set, then ones starting with `DEFAULT_` from [the previous section](#global-variables) will take precedence.

### SERVICE_NAME

It must match the name of the service you are monitoring.

### SERVICE_TYPE

It supports `systemd` or `sysV` as value.
