---
title: Supported subsystems
taxonomy:
    category: docs
    label: user guide
---


## Log

The log subsystem will look for a log pattern or a data stream. 

Arguments:

* Log Pattern - the regex pattern to look for within the log content
* Log file or data stream - the source of the log content
* [Optional] Log pattern expiration  - time that needs to pass until the pattern match is considered invalidated
    * As an example, if ERROR is detected once and no new errors are detected in the next 5 seconds, monitoring will report all issues were resolved
    * If nothing is specified the [DEFAULT_LOG_PATTERN_EXPIRATION_SECONDS](../40.Configuration/docs.md#DEFAULT_LOG_PATTERN_EXPIRATION_SECONDS) is used

The log monitoring subsystem saves the number of the last line of logs that
it parsed and starts tailing the file skipping the already seen lines.

The log monitoring subsystem uses the `grep` command to match lines to a given pattern
By default, and if supported by `grep` we use the `-P` option, which allows you to use
the [Perl-compatible regular expressions](https://www.pcre.org/).
If you have no support for `-P`, it falls back to the `-E` flag, and
eventually uses plain `grep`.


### Capturing logs from log files
The general syntax to enable a check for a pattern in a specific file is as follows:

```
#                       "Subsystem"     "Check name"          "Log Pattern"      "Log file or data stream"             "[Optional] Log pattern expiration"
mender-monitorctl create    log         crasher_app             ERROR               /root/crasher.log                                  5
```


### Capturing logs from data streams

Any command that produces data on standard output can be used as the data source in which to look for patterns.

The general syntax to enable the streamline logs extension is to use `@` with the command that provides a stream of logs:

```bash
#                       "Subsystem"     "Check name"             "Log Pattern"                  "Log file or data stream"    "[Optional] Log pattern expiration"
mender-monitorctl create    log         crasher_app     ".*container kill.*name=scanner.*"          "@docker events"                        5
```


## D-Bus

Every time a D-Bus signal matching the watch expression is received, it will trigger a check that will send an alert from the monitoring subsystem. You can adapt the configuration to any D-Bus signal and pattern based on your use case.

Let's assume you want to raise an alert every time `u-power` raises a signal. To this end, you need to create the check as follows:

```bash
#                         "Subsystem"     "Check name"      "Dbus name"      "Dbus pattern"       "Dbus watch expression"                                                                                       "[Optional] Dbus alert expiration"
mender-monitorctl create     dbus          dbus_check          u-power            ""              "type='signal',interface='org.freedesktop.DBus.Properties',member='PropertiesChanged',path=/org/freedesktop/UPower/devices/battery_BAT0"   5
```

Arguments:

* Dbus name - the name of the watcher
* Dbus pattern - the grep pattern to match on (in the example above empty to match on all notifications)
* Dbus watch expression - the watch pattern passed to dbus-monitor (can be empty)
* [Optional] Dbus alert expiration  - time that needs to pass until the pattern match is considered invalidated
    * i.e. if ERROR is detected once and no new errors are detected in the next 5 seconds, monitoring will report all issues that were resolved.
    * if nothing is specified the `DEFAULT_DBUS_ALERT_EXPIRATION_SECONDS` is used.


## Service

The service subsystem is mostly useful for tracking systemd services.
It will trigger an alert if detects the systemd service isn't running.
It has a peculiarity compared to the other services where the check name is used as a parameter for the subsystem


```
#                         "Subsystem"     "Check name"          "Service type" 
mender-monitorctl create    service           cron                  systemd           
```

Arguments:

* Check name - this server both as a check name and as the name of the service to 
* Service name - the systemd service to check for 
