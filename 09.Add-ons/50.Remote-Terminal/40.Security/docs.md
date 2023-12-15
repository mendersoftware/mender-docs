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
Remote Terminal is an optional feature.

### Local device user

One part of the Remote Terminal configuration is the username of the user on the device for whom the shell will be created.
Using Remote Terminal you can execute any command the user on the device can execute.
Like with any other operation, the Mender backend will allow only authenticated Mender users to access the Remote Terminal.

### Role Based Access Control (RBAC)

!!!!! Role Based Access Control is only available in the Mender Enterprise plan.
!!!!! See [the Mender features page](https://mender.io/product/features?target=_blank)
!!!!! for an overview of all Mender plans and features.

You can apply additional restrictions on which Mender users can access Remote Terminal using RBAC.
It is fully integrated in the Role Based Access Control system of Mender and accessible from the UI.

### Encrypted connections

The [mender-connect](https://github.com/mendersoftware/mender-connect), part of the Remote Terminal that is running on the device,
obtains device token through DBus API. It is the same token that `mender-update`, part of the Mender client, is using.
<!--AUTOVERSION: "https://tools.ietf.org/html/rfc6455#section-%"/ignore-->
Remote Terminal uses [Encrypted WebSocket connections](https://tools.ietf.org/html/rfc6455#section-11.1.2) to communicate with the server.
In general, the security impact of enabling Remote Terminal is similar to the one when enabling SSH.
The connection to the device is secure, but there are no limitations on what command the user can execute,
except for the user permissions on the device.

### No open ports

There are also some important differences between enabling Remote Terminal and enabling SSH server on the device.
Remote Terminal does not open nor listen on any port: the device initiates the connection to the server.

### Audit logs

!!!!! Audit logs is only available in the Mender Enterprise plan.
!!!!! See [the Mender features page](https://mender.io/product/features?target=_blank)
!!!!! for an overview of all Mender plans and features.

Every remote terminal invocation is saved in the audit logs. The logs
include the session start and stop events as well as the terminal output. The
audit logs are available in the Mender UI "AUDIT LOG" tab. There you can also
inspect the terminal recording by playing back the terminal session in real time
in the browser.
