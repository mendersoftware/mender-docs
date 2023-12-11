---
title: Device Runtime
taxonomy:
    category: docs
---


## Console access to your device

Most troubleshooting requires access to a console and a login prompt.
There are three primary methods to connect to your device for
troubleshooting. All three methods will lead to a text login with the
username of "root" and no password. Obviously these images should not
be used for production devices.


### HDMI/USB

The simplest method to connect to your device is with an HDMI display
and a USB keyboard. The Beaglebone requires a
[micro-HDMI to HDMI cable](https://elinux.org/Beagleboard:BeagleBone_Black_Accessories?target=_blank#HDMI_Cables)
or adapter. The Raspberry Pi uses a standard HDMI to HDMI cable.


### Serial Adapter

An alternative to HDMI and keyboard is to use a serial adapter; this
can provide more effective troubleshooting since it allows for easy
copy/paste/search of the console output. This does require additional
hardware.

For the Beaglebone,
[use this link as a reference](https://elinux.org/Beagleboard:BeagleBone_Black_Serial?target=_blank).

For the Raspberry Pi, please see
[this link](https://elinux.org/RPi_Serial_Connection?target=_blank) and
[this link](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/overview?target=_blank)
for more details.

On Windows, the following applications can be used to access the serial console:
* [https://teratermproject.github.io/index-en.html](https://teratermproject.github.io/index-en.html?target=_blank)
* [https://putty.org/](https://putty.org/?target=_blank)

On MacOS, [this web page](https://pbxbook.com/other/mac-ser.html?target=_blank)
lists several applications that may work.  Specifically, we have
tested
[Serial from the Mac App store](https://itunes.apple.com/us/app/serial/id877615577?mt=12?target=_blank).

On Linux, you can use
[picocom](https://github.com/npat-efault/picocom?target=_blank),
[screen](https://www.gnu.org/software/screen?target=_blank) or
[minicom](https://en.wikipedia.org/wiki/Minicom?target=_blank). These are all
available in the Ubuntu package repository. For other distributions,
the standard package install mechanism likely will have these as
well. Note that these are all console apps and may also work on MacOS
or Windows.


### SSH

The Yocto builds will have OpenSSH installed and configured by
default.


## Boot Issues

### I see a graphical environment on the HDMI monitor when booting the Beaglebone.

   This generally means that the Beaglebone was booted from
   the on-board eMMC rather than the SD-Card.  To fix this, please
   power off the system and make sure to depress switch S2 while
   powering back on (keep the button pressed for 5 seconds while the
   device starts up).

### The console is completely blank when booting the device.
   
   This generally means there is an issue with your SD Card.  Please
   try another SD Card. Also, please make sure after creating the SD
   Card it is automatically mounted when inserted in your desktop
   system. Note: if you are on Windows, you may not see multiple
   partitions as they are not Windows compatible.

### The UBoot and kernel log messages show up on the console but there is no login prompt.
   
   This likely means there was a kernel crash or some other issue with
   the system startup code. Please capture the output that is
   available and contact Mender support for more guidance.

### Attempting to login with user “root” and no password fails.

   This likely means that your image is incorrect. Please retry your SD
   Card provisioning.


## Mender Server Connection Issues

### Basic Networking Connectivity

   The primary cause of issues using Mender relate to networking. Use
   the following command to determine if your network is connected
   properly:

   ```bash
   # ping 8.8.8.8
   ```

   If you are unable to ping the above server (it is one of the Google
   DNS servers and should be online) your basic network connectivity
   is non-functional.  Please check your cabling.  Type:

   ```bash
   # ip addr
   ```

   To see what, if any, IP address was assigned to your device.

   If these steps fail, consult your local network administrator to
   understand why you are not getting internet connectivity.  Many lab
   environments are locked down and may require special site
   procedures to allow the devices to connect.

### Networking connectivity to the Mender Server

   Run the following to attempt to contact the Mender Server:

   ```bash
   # echo string | nc hosted.mender.io 443
   ```

   Note, replace *hosted.mender.io* with the URL of your server if you
   are using an on-premise installation

   The result should be a message containing "400 Bad Request". If the
   command hangs or produces any other error message, then the
   connection to the Mender Server has failed. Please consult your
   local network administrator for further troubleshooting.

### Accurate time required for certificate processing.

   Proper certificate processing requires an accurate system time. See
   [Mender Client troubleshooting](../03.Mender-Client/docs.md#certificate-expired-or-not-yet-valid)
   for more details.

## Next Steps

If the above tests all pass, then please review [Mender Client troubleshooting](../03.Mender-Client/docs.md) to help determine next steps.
