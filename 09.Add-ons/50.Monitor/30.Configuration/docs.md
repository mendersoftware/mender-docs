---
title: Configuration
taxonomy:
    category: docs
---


### Daemon config defaults

The `mender-monitor` daemon has certain
default configuration settings that you can see or tune in the `config/config.sh`
file. You do not have to change anything there, but it maybe
important for some use cases to be aware of their meaning.

| Variable name   | Value       | Description |
| --------------- | ----------- | ----------- |
|ALERT_URL| string | URL to send the alerts to |
|MONITOR_D_DIRECOTRY | string | a path to the `monitor.d` directory |
|CONFIG_LOG_LEVEL| FATAL TRACE ERROR DEBUG WARN INFO | log level |
|DAEMON_LOG_FILE| string | path for the daemon log file |
|FLAPPING_INTERVAL| positive integer | length of the time interval in seconds for which we calculate the flapping rate |
|FLAPPING_COUNT_THRESHOLD| positive integer | number of service state changes per FLAPPING_INTERVAL above which we consider a service to be flapping |
