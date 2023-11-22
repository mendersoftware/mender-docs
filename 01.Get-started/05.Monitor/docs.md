---
title: Monitor your device
taxonomy:
  category: docs
  label: tutorial
---

!!!!! Requires the Mender Monitor add-on package.
!!!!! See [the Mender features page](https://mender.io/product/features?target=_blank)
!!!!! for an overview of all Mender plans and features.

This tutorial will walk you through how to monitor your device and its applications with
Mender. We will be using the [Monitor Add-on](../../09.Add-ons/20.Monitor/docs.md), allowing you to monitor various system parts.

## Prerequisites

To follow this tutorial and perform the examples, you will need to install the [Monitor Add-on package](../../09.Add-ons/20.Monitor/10.Installation/docs.md) and the [Demo monitors package](../../10.Downloads/docs.md#demo-monitors) on your device. 
If you have followed the [get started tutorial](../01.Preparation/docs.md) to prepare your device, the Monitor Add-on, and Demo packages should already be installed.

Verify installed dependencies on your device with:

 ```bash
 mender --version && mender-monitorctl --version
 ```
>```text
>3.5.1	runtime: go1.17.13
>Mender Monitoring control utility v1.3.0
>
>Usage: mender-monitorctl command [options]
>Use "mender-monitorctl help" for more information about available commands and options.
>```

Check installed monitoring subsystems with:

```bash
 ls -lAh /etc/mender-monitor/monitor.d | grep -v '^d'
```
>```text
> -rwxr-xr-x 1 root root 2669 Aug 17 20:09 connectivity.sh
> -rwxr-xr-x 1 root root 2298 Mar 10 09:37 dbus.sh
> -rwxr-xr-x 1 root root 2498 Aug 18 01:14 diskusage.sh
> -rwxr-xr-x 1 root root 3738 Mar 10 09:37 log.sh
> -rwxr-xr-x 1 root root 3016 Mar 10 09:37 service.sh
>```

Verify existence of check definitions with:

```bash
 ls -lAh /etc/mender-monitor/monitor.d/available/ | grep -v '^d'
```

> ```bash
> -rwxr-xr-x 1 root root 176 Aug 17 20:09 connectivity_example.sh
> -rwxr-xr-x 1 root root 173 Aug 18 01:14 diskusage_root_space.sh
> -rwxr-xr-x 1 root root 201 Aug 17 20:09 log_mender_client.sh
> -rwxr-xr-x 1 root root 203 Aug 17 20:09 log_mender_connect.sh
> -rwxr-xr-x 1 root root 297 Aug 17 20:09 log_usb_disconnect.sh
> -rw-r--r-- 1 root root  43 Jun 20 20:06 service_cron.sh
> ```

## Demo Checks


Demo Checks for the Mender Monitor Add-on, found in the [Demo monitors package](../../10.Downloads/docs.md#demo-monitors) (Debian package) or in the `examples` directory for [Yocto](../../05.Operating-System-updates-Yocto-Project/05.Customize-Mender/docs.md#monitor) serve as a starting point for quick evaluation.
Once ready, you can customize and define your own [Checks](../../09.Add-ons/20.Monitor/20.Concepts/docs.md#creating-custom-checks).

By default both mail notifications and UI alerts occur once an monitored event happens. 
While going through the examples in this tutorial, watch the email inbox of your Mender user to see that you get notified about Alerts triggered and cleared on the device. 

The default configuration for `mender-monitorctl` command requires read-write access to the `/etc/mender-monitor` directory, which on most systems means switching to super user or running with `sudo`. 
For a read-only filesystem, it is essential to establish a symbolic link to a writable directory. This symlink is required to create, modify, and enable alert checks.

### Monitor USB disconnects

This demo shows detecting USB disconnects, alerting you to potential device tampering and preventing unauthorized access

Enable the check by running:


``bash
udo mender-monitorctl enable log usb_disconnect
``

Now remove a USB device from the device (you can insert it first, e.g., a thumb drive or mouse, if you don't have any USB devices inserted). 
Once you remove the USB device, the log subsystem triggers an alert, which you can inspect in the device details in the Mender UI:

[Connectivity alarm OK](log-usb-alarm.png)

!!! Note: This Alert will remain unless a manual [alert cleaning](../../09.Add-ons/20.Monitor/40.Advanced-use-cases/docs.md#alert-cleaning ) is performed:
!!! ```bash
!!! cd /usr/share/mender-monitor
!!! source lib/monitor-lib.sh
!!! monitor_send_alert OK "Log file contains \[.*\] +usb [\w\-\.]+: USB disconnect" "\[.*\] +usb [\w\-\.]+: USB disconnect present in /var/log/kern.log" "log_usb_disconnect" LOGCONTAINS "log" "\[.*\] +usb [\w\-\.]+: USB disconnect" "/var/log/kern.log" 
!!!! ```

### Monitor disk usage

Running low on essential device resources like disk space, often due to growing log files, can disrupt the product's functionality. 
This example shows you how to monitor for high disk usage, allowing timely action to avoid downtime.

Enable the `diskusage` check for the root space partition called `root_space` by running the following command:

```bash
sudo mender-monitorctl enable diskusage root_space
```

Check the current disk usage.

```bash
df -h /

# Output:
# Filesystem      Size  Used Avail Use% Mounted on
# /dev/root       3.4G  1.4G  1.9G  42% /
```

With the check enabled an alert will be triggered when the root partition exceeds 75% (predefined threshold).
To trigger the Alert, fill up the filesystem with a large file:

```bash
fallocate -l 10G ~/large-file
```

as the disk usage goes above the 75% threshold

```bash
df -h /

# Output:
# Filesystem      Size  Used Avail Use% Mounted on
# /dev/root       3.4G  3.4G     0 100% /
```

an alert shows up in the UI.

![Disk usage alarm triggered](diskusage-alarm.png)

An _OK_ alert will be sent by the `diskusage` monitoring subsystem if this 
file is removed, and the disk space is less than the threshold.

```bash
rm ~/large-file
```


### Monitor connectivity

Ongoing connectivity issues may cause the device application to hang or malfunction, disrupting the user experience or function of the product. 
This Alert is one example of how to detect connectivity issues. 

Mender stores triggered Checks on the device. 
Therefore, even if Mender cannot send the Checks to the server immediately, you will be notified about triggered Checks once the device regains connectivity. 
This means that even during offline periods, Alterts are triggered.

Enable the `connectivity` check called `example`:

```bash
sudo mender-monitorctl enable connectivity example
```

This enabled a Check using the demo `connectivity` monitoring subsystem, which sends HTTP HEAD
requests to `example.com,` ensuring it is responding.

To trigger the Alert, let us stop the traffic to `example.com` by
redirecting the DNS resolver to localhost in `/etc/hosts`.

```bash
echo 127.0.0.1 example.com | sudo tee -a /etc/hosts
```

Which then triggers the Alert:

![Connectivity alarm triggered](connectivity-alarm.png)

And when re-enabling the route to `example.com` in `/etc/hosts`:

```bash
sudo sed -i '/example/d' /etc/hosts
```

After connection to `example.com` is restored, an _OK_ Alert will show up in the UI:

![Connectivity alarm OK](connectivity-ok.png)


### Monitor a systemd service 

Assume you want to monitor the state of a systemd service,
and you wish to receive _CRITICAL_ alerts if the service is not running,
and _OK_ alerts when it is back up. 

Create a service that will count some seconds and then fail.

```bash
cat > countdown.sh << "EOF"
#!/bin/sh
i=30
while [ $i -gt 0 ]; do
    echo "INFO: $i seconds remaining"
    i=$((i-1))
    sleep 1
done
echo "ERROR: Exiting with return 1"
exit 1
EOF

PATH_TO_SCRIPT=$(realpath countdown.sh)
chmod +x $PATH_TO_SCRIPT


cat > /etc/systemd/system/countdown.service << EOF
[Unit]
Description=Countdown Service

[Service]
Type=simple
ExecStart=$PATH_TO_SCRIPT

[Install]
WantedBy=default.target
EOF

systemctl daemon-reload
systemctl start countdown.service
```

You can confirm the countdown with `journalctl -fu countdown.service`.

Now create and enable the check for the systemd `service` monitoring subsystem:

```bash
sudo mender-monitorctl create service countdown systemd
sudo mender-monitorctl enable service countdown
```

Once the service exits, an alert is sent.

Restarting the service will send an ok Alert.

```bash
systemctl restart countdown
```

To stop the monitoring, disable and delete the check

```bash
sudo mender-monitorctl disable service countdown
sudo mender-monitorctl delete service countdown systemd
```

!!! If you want to examine the low-level architecture of mender-monitor using this example [follow this link](../../09.Add-ons/20.Monitor/50.Advanced-use-cases/docs.md#example).


### Monitor systemd services logs

You can trigger alerts when a given pattern shows in the logs of your systemd service
For this, you can create a check definition for the `log` monitoring subsystem that will
use the `journalctl` command as a source for log data and check for errors or any other pattern.

Create a service that glitches every few seconds and prints "WARNING: a glitch in the system" when it does:

```bash
cat > glitch.sh << "EOF"
#!/bin/sh
i=0
while true; do
    i=$((i+1))
    [ $(expr $i % 23) -eq 0 ] && echo "WARNING: a glitch in the system" || echo "INFO: $i seconds remaining"
    sleep 1
done
EOF


PATH_TO_SCRIPT=$(realpath glitch.sh)
chmod +x $PATH_TO_SCRIPT


cat > /etc/systemd/system/glitch.service << EOF
[Unit]
Description=Countdown Service

[Service]
Type=simple
ExecStart=$PATH_TO_SCRIPT

[Install]
WantedBy=default.target
EOF

systemctl daemon-reload
systemctl start glitch.service
```

You can confirm the countdown with `journalctl -fu glitch.service`.


Now, create and enable a check for the systemd `log` monitoring subsystem called `countdown_logs`:

```bash
sudo mender-monitorctl create log glitch "WARNING*." "@journalctl -u glitch -f"
sudo mender-monitorctl enable log glitch
```

The `log` monitoring subsystem will trigger a critical alert every time "WARNING" shows up in the logs.


```bash
sudo mender-monitorctl disable log glitch
sudo mender-monitorctl delete log glitch
```

### Monitor new root sessions

The root account has complete control over the server, making it a target for unauthorized access.
Monitoring these sessions helps in the early detection of security breaches, ensuring that any unauthorized access is quickly identified and addressed. 

First, create a check for the `log` monitoring subsystem named `auth_root_session` by running
the following command:

```bash
sudo mender-monitorctl create log auth_root_session "Started User Manager for UID 0" /var/log/auth.log
sudo mender-monitorctl enable log auth_root_session
```

Not that the check is in place, change your user to `root`:
```
sudo su
```

this will trigger an alert notifying you of the event that took place.



### Monitor Docker container restart

!!!!! Please installl and validate (`docker --version`) the existence of Docker Engine on the device.
!!!!! If missing, you can get it by following [Docker's official guide](https://docs.docker.com/engine/install/?target=_blank).


This example uses a [pseudo subsystem](../../09.Add-ons/20.Monitor/50.Advanced-use-cases/docs.md#pseudo-subsystems) and is an advanced use case where you want to optimize the creation of check for specific cases.
It is possible to achieve the same functionality with the [log subsystem](../../09.Add-ons/20.Monitor/30.Supported-subsystems/docs.md#capturing-logs-from-data-streams).


This Alert helps identify when applications running in containers managed by Docker, restart unexpectedly due to issues like intermittent connectivity. 
These restarts can be hard to notice and diagnose, especially based on customer reports alone.
By monitoring Docker daemon events, this Alert notifies you when a container restarts, making it easier to detect and address the root cause, often evident in logs or application output.


First, launch the container we want to monitor:

```bash
sudo docker run --name demo --rm -d alpine sleep infinity
```

Secondly, create the check for the `dockerevents` monitoring subsystem by running:

```bash
sudo mender-monitorctl create dockerevents container_demo_restart demo restart 1d
```

Then, enable the `dockerevents` check called `container_demo_restart` by running 
the following command:
```bash
sudo mender-monitorctl enable dockerevents container_demo_restart
```

Finally, restart the container:

```bash
sudo docker container restart demo
```

The `dockerevents` check will send the Alert and show up in the UI.
