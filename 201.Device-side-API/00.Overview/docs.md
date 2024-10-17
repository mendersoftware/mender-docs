---
title: Overview
taxonomy:
    category: docs
---

This section describes the Device-side API for the Mender Client. The Device-side API constitutes
the only public API of the Mender Client. The Device-side API is a thin layer which receives messages
over D-Bus, processes them, transmits them to the Mender Client, receives the results from
the client, and transmits a response on the D-Bus.

You can find the D-Bus specification and background information on how it works [here](https://www.freedesktop.org/wiki/Software/dbus/).

## Accessing the D-Bus API

### Quickstart example

As an example call, the client can be instructed to [fetch the JWT token](../../201.Device-side-API/?target=_blank#io.mender.authentication1) from the server like this:

```
dbus-send --print-reply=literal --system --dest=io.mender.AuthenticationManager \
  /io/mender/AuthenticationManager \
  io.mender.Authentication1.FetchJwtToken
```

As an example monitor, you can listen for the 
```
dbus-monitor --system "type='signal',\
  sender='io.mender.AuthenticationManager',\
  interface='io.mender.Authentication1'"
```

### Calling a D-Bus method

The easiest means to call a method exposed on D-Bus is to use the `dbus-send` tool. This is by default installed on most devices as part of the `dbus` package on Ubuntu, and `dbus-tools` on Yocto-based Linux distributions. The command is described in depth [here](https://dbus.freedesktop.org/doc/dbus-send.1.html), so we will only cover the parameters needed for accessing the Mender Client API.

A generic method invocation looks like this:
```
dbus-send --system --dest=CONNECTION \
  OBJECT_PATH \
  INTERFACE.MEMBER \
  [CONTENT]
```

The parameters are constructed as follows:
- `CONNECTION` && `OBJECT_PATH`: defined per exposed client API, see the overview section of the API documentation that you want to use.
- `INTERFACE.MEMBER`: an object can expose different methods, which are organized as hierarchically structured interfaces. The `INTERFACE.MEMBER` defines the specific method to be invoked, and is given at the top of each method detail description.
- `--system`: D-Bus supports multiple, seperate buses per system and user. To access the system wide management bus, this flag is required.

Optional:
- `--print-reply=literal`: print the resulting response to the command line. This is useful if the method is supposed to return some information such as the JWT which can be used in subsequent actions.

### Listening for a D-Bus signal

As opposed to methods which are actively invoked, signals can be emitted by an object at every point in time. To react to a signal, one therefore has to listen for it, which is called "monitoring" in a D-Bus context. This is done through `dbus-monitor`, which is described in depth [here](https://dbus.freedesktop.org/doc/dbus-monitor.1.html).

A generic monitor invocation looks like this:

```
dbus-monitor --system "type='signal', \
  sender='CONNECTION', \
  interface='INTERFACE'"
```

The parameters `CONNECTION` and `INTERFACE` have the same meaning as in the previous section on method invocation.