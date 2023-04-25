---
title: Enabling device license count
taxonomy:
    category: docs
    label: tutorial
---

!! Production installation with docker compose is considered deprecated for versions beyond 3.3.


!!!!! Device License Count is only available in Mender Enterprise.
!!!!! Ignore this section if you are running Mender Open Source.

To enable the [device license count](../../07.Device-license-count/docs.md) in your composition,
you must schedule a cronjob to run the device-count command daily.

Assuming you have [cron](https://man7.org/linux/man-pages/man5/crontab.5.html) available
you can create a crontab entry in the following way:

```shell
echo "7 3 * * * cd YOUR-SERVER-ROOT && docker-compose run --entrypoint /usr/bin/deviceauth-enterprise mender-device-auth license-count" | crontab -
```

where `YOUR-SERVER-ROOT` stands for the sevrer root path where all the docker compose files are present.
