---
title: Security
taxonomy:
    category: docs
---

Delivering commands securely, maintaining the identity of the communication
endpoints, ensuring endpoint authentication, are critical factors in a secure
remote command execution. This section gives a brief security overview
of the Remote Terminal add-on.

## Remote Terminal

With Mender, you can start an interactive shell to any accepted device by clicking "Launch a new Terminal" in the UI.
The name of the feature is [Remote Terminal](../10.Overview/docs.md).
Remote Terminal is an optional feature.
One part of the Remote terminal configuration is the username of the user on the device for whom the shell will be created.
Using Remote Terminal you can execute any command the user on the device can execute.
Like with any other operation, the Mender backend will allow only authenticated Mender users to access the Remote Terminal.
You can apply additional restrictions on which Mender users can access Remote Terminal using RBAC.
The [mender-shell](https://github.com/mendersoftware/mender-shell), part of the Remote Terminal that is running on the device,
obtains device token through DBus API. It is the same token Mender client is using.
<!--AUTOVERSION: "https://tools.ietf.org/html/rfc6455#section-%"/ignore-->
The mender-shell uses [Encrypted WebSocket connections](https://tools.ietf.org/html/rfc6455#section-11.1.2) to communicate with the server.
In general, the security impact of enabling Remote Terminal is similar to the one when enabling SSH.
The connection to the device is secure, but there are no limitations on what command the user can execute,
except for the user permissions on the device.
There are also some important differences between enabling Remote Terminal and enabling SSH server on the device.
Remote Terminal does not opens or listens on any port and the device initiates the connection.
