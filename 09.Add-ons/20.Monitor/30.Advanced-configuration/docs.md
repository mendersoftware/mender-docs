---
title: Advanced Configuration
taxonomy:
    category: docs
---

The `mender-monitor` daemon reads the configuration settings from the file
`/usr/share/mender-monitor/config/config.sh`. The default settings are suitable
for most use-cases, but you can adjust the following configuration variables
if you need to customize the functionalities:

| Variable name   | Value       | Description |
| --------------- | ----------- | ----------- |
|`ALERT_URL`|string|URL to send the alerts to|
|`MONITOR_D_DIRECOTRY`|string|a path to the `monitor.d` directory|
|`CONFIG_LOG_LEVEL`|string|log level (`FATAL`, `TRACE`, `ERROR`, `DEBUG`, `WARN` or `INFO`)|
|`DAEMON_LOG_FILE`|string|path for the daemon log file|
|`FLAPPING_INTERVAL`|integer|time interval (in seconds) for which we calculate the flapping rate|
|`FLAPPING_COUNT_THRESHOLD`|integer|number of service state changes per `FLAPPING_INTERVAL` above which we consider a service to be flapping|
|`ALERT_LOG_MAX_AGE`|integer|max number of seconds for which we keep the alerts in memory for flapping detection|
|`ALERT_OFFLINE_STORE_MAX_COUNT`|integer|maximal number of alerts to store when device is offline|
|`DEFAULT_ALERT_LEVEL`|string|default alert level|
|`DEFAULT_LOG_ALERT_LEVEL`|string|default alert level for the log monitoring subsystem|
|`DEFAULT_SERVICE_ALERT_LEVEL`|string|default alert level for the service monitoring subsystem|
|`DEFAULT_DBUS_ALERT_LEVEL`|string|default alert level for the D-Bus monitoring subsystem|
|`DEFAULT_LOG_PATTERN_EXPIRATION_SECONDS`|integer|default log pattern expiration period, if not set in the check configuration file with `LOG_PATTERN_EXPIRATION`|
|`DEFAULT_LOG_LINES_BEFORE`|integer|default number of lines sent before a line that contained a string that matched a given pattern|
|`DEFAULT_LOG_LINES_AFTER`|integer|default number of lines sent after a line that contained a string that matched a given pattern|
