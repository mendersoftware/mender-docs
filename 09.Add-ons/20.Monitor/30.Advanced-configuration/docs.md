---
title: Advanced Configuration
taxonomy:
    category: docs
---

The `mender-monitor` daemon reads the configuration settings from the file
`/usr/share/mender-monitor/config/config.sh`. The default settings are suitable
for most use-cases, but you can adjust the following configuration variables
if you need to customize the functionalities.

### ALERT_URL

The back-end URL `mender-monitor` will send the alerts to.

### MONITOR_D_DIRECTORY

The path to the `monitor.d` directory.

### CONFIG_LOG_LEVEL

A string defining the log level; the possible values are: `FATAL`, `TRACE`, `ERROR`, `DEBUG`, `WARN` or `INFO`.

### DAEMON_LOG_FILE

The path to the daemon's log file.

### FLAPPING_INTERVAL

The time interval, expressed as a number of seconds, for which we calculate the flapping rate.

### FLAPPING_COUNT_THRESHOLD

The number of service state changes per `FLAPPING_INTERVAL` (see above), after which we consider a service to be flapping.

### ALERT_LOG_MAX_AGE

The max number of seconds for which we keep the alerts in memory for flapping detection.

### ALERT_OFFLINE_STORE_MAX_COUNT

The maximum number of alerts to store if the device is offline.

### DEFAULT_ALERT_LEVEL

The default alert level.

### DEFAULT_LOG_ALERT_LEVEL

The default alert level for the log monitoring subsystem.

### DEFAULT_SERVICE_ALERT_LEVEL

The default alert level for the service monitoring subsystem.

### DEFAULT_DBUS_ALERT_LEVEL

The default alert level for the D-Bus monitoring subsystem.

### DEFAULT_LOG_PATTERN_EXPIRATION_SECONDS

The default log pattern expiration period, expreessed as a number of seconds, if not set in the check configuration file with `LOG_PATTERN_EXPIRATION`.

### DEFAULT_LOG_LINES_BEFORE

The default number of lines sent before a line that contained a string that matched a given pattern.

### DEFAULT_LOG_LINES_AFTER

The default number of lines sent after a line that contained a string that matched a given pattern.

### DEFAULT_ALERT_STORE_RESEND_INTERVAL_S

The default number of seconds in between every attempt to resend an alert in the case of failure.
