---
title: Troubleshooting Remote Terminal
taxonomy:
    category: docs
---


## Obtaining mender-shell logs

Logs are usually needed in order to diagnose an issue.

The mender-shell by default logs to the system log using `systemd`, so the easiest way to retrieve logs
is to run the following command:

```
journalctl -u mender-shell
```

