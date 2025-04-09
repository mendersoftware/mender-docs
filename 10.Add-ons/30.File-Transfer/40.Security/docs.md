---
title: Security
taxonomy:
    category: docs
---

File Transfer allows only authorized users to upload or download files.
Furthermore, only accepted devices can interact with the add-on.
 
### Role Based Access Control (RBAC)

!!!!! Role Based Access Control is only available in the Mender Enterprise plan.
!!!!! See [the Mender plans page](https://mender.io/pricing/plans?target=_blank)
!!!!! for an overview of all Mender plans and features.

You can apply additional restrictions on which Mender users can access File Transfer using RBAC.
It is fully integrated in the Role Based Access Control system of Mender and accessible from the UI.

### Encrypted connections

The [mender-connect](https://github.com/mendersoftware/mender-connect),
obtains device token through DBus API. It is the same token `mender-update`, part of the Mender Client, is using.
<!--AUTOVERSION: "https://tools.ietf.org/html/rfc6455#section-%"/ignore-->
File Transfer uses [Encrypted WebSocket connections](https://tools.ietf.org/html/rfc6455#section-11.1.2) to communicate with the server.
The connection to the device is secure, but there are no additional limitations on what file can be transferred or network bandwidth used.
In essence, the File Transfer add-on provides a data passing model over a secure websocket between
a device, and the caller (may it be th UI, mender-cli or any other API consumer).

### No open ports

File Transfer does not require you to have any open, listening and bound ports
on a device. The HTTPS connection gets upgraded to a websocket, and the transaction
proceeds transparently from there on. You do not have to alter any other
packet filtering rules, as long as you have allowed traffic over HTTPS
to the Mender Server.

### Audit logs

!!!!! Audit logs is only available in the Mender Enterprise plan.
!!!!! See [the Mender plans page](https://mender.io/pricing/plans?target=_blank)
!!!!! for an overview of all Mender plans and features.

Audit logs hold a list of every file transfer event. You can access this information
in the Mender UI.

### No arbitrary transfers

Within the [Limits](../../90.Mender-Connect/docs.md#limits-configuration) configuration section you can impose
additional restrictions of the file transfer requests. Enabling the limits allows you to control
basic security implications of a file transfer:
* chroot-like restrictions of uploads and downloads to a given directory
* restrict the files you can get to certain owners/groups
* permit only the transfer of regular files
* limit the max file size
* control the average amount of data your device sends or receives per hour
