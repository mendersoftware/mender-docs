---
title: Troubleshooting File Transfer
taxonomy:
    category: docs
---


## Obtaining mender-connect logs

The `mender-connect` by default logs to the system log using `systemd`, so the easiest way to retrieve logs
is to run the following command:

```
journalctl -u mender-connect
```

