---
title: Mender Server
taxonomy:
    category: docs
---

This document details troubleshooting steps for the most common problems with the Mender Server.

## Persistent certificate errors in demo mode

Since the demo certificates are self-signed, browsers will produce relevant warnings.
For instance in Chrome, a `Your connection is not private` page will appear, with a
`NET::CERT_AUTHORITY_INVALID` error.

Typically this page comes with 'Advanced' options, allowing you to accept the certificate
and proceed anyway; demo certificates should not be an issue from then on.

It has however been observed that newer browser versions come with tighter security checks, and may unexpectedly block access to the Mender UI unconditionally. If that's the case,
the workaround is to clean browser internals related to HTTP Strict Transport Security. In Chrome:
- navigate to `chrome://net-internals/#hsts`
- type the domain `docker.mender.io` into the `Delete domain` section and confirm

Consult your browser's documentation for similar instructions.


## Cleaning up the deviceauth database after device decommissioning

It is possible that after a failed device decommissioning operation there will be some unaccessible and unnecessary data in the deviceauth database. In this case, you should clean the database manually.

Is is recommended to backup your data before performing the clean up operation.
The [Taking a full backup](../../09.Server-installation/02.Upgrading-from-previous-versions/docs.md#taking-a-full-backup) chapter provides examples and
introduces example tools provided in Mender integration repository.

To clean up the deviceauth database, run the following from within the mender-server repository:
```
docker compose run deviceauth maintenance --decommissioning-cleanup
```

## The virtual QEMU device is not showing up in demo mode


If you have trouble connecting this virtual device, please make sure your environment meets the resource requirements
to run the Mender Server. In particular, it is known that the virtual device will not
start if you do not have enough memory.

## A device shows up as pending after preauthorizing it

If you see your device gets the `pending` status after [preauthorizing it](../../10.Server-integration/02.Preauthorizing-devices/docs.md), something went wrong. Most likely there is a mismatch between the identity and public key [you preauthorized](../../10.Server-integration/02.Preauthorizing-devices/docs.md#call-the-preauthorize-api) and what your Mender Client is actually using.

To diagnose this, look for the device identity in the Device Authentication service, for example:

```bash
curl -H "Authorization: Bearer $JWT" $MENDER_SERVER_URI/api/management/v2/devauth/devices | jq '.'
```

```json

[
    {
        "id": "5afdcccf8b89f00001fc40d7",
        "identity_data": {
            "mac":"52:54:00:50:9b:84"
        },
        "auth_sets": [
            {
                "id": "5afdcccf8b89f00001fc40d6",
                "identity_data": {
                    "mac":"52:54:00:50:9b:84"
                },
                "pubkey": "-----BEGIN PUBLIC KEY-----MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEAvOsee2ivRTkpA2GNWsjd6fH4OgAYwheHkY1U9i2GaPdYbhQb4hBUFoOLhdPFx5wwEqxJ8LnJOJBYywUthv59iJy01w4RTPiTEs3A6eXGdiLO0/RqsWqK5z2KeYiCrI52oE63pY6Y0JEZBpqzs2V9WsLOn6cnQU6HzHltYIuRpzwZWTWFxAFuU+FvDvj9QmD/Y6tos0yaMhfhpgJj3Iw9uARkFAv4DVn+HeA14PPVzHD4xJPUHL6H8FMfeIylejzaOnNHn6vkrvpuMQSvvZjlkH+uV7N93kj3JxSJ2LL9oMY9EargUkT0covZPdAE0G3wwNYCAIYRclzvI1w3DZ03oK2HCveVzFkBPbCwt4/pDReVzlRbQJ6CHkZqCbipoEH0/Ucetzp9fJ3mW3jE2yH1JK8nnpprbNYOCA988s6q3ifxbR6nWkPTbG3JyZL3ythV1o7FgOcwyKh8bneHoZaOa9BnNrHkDz9uG1Xwbe6As62QyZjk2pjQswswQsh/6AvrAgMBAAE=-----END PUBLIC KEY-----",
                "status": "preauthorized",
                "ts": "2018-05-17T18:41:19.546Z"
            },
            {
                "id": "5afdcccf8b89f00001fc40d6",
                "identity_data": {
                    "mac":"52:54:00:50:9b:84"
                },
                pubkey: "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzogVU7RGDilbsoUt/DdH\nVJvcepl0A5+xzGQ50cq1VE/Dyyy8Zp0jzRXCnnu9nu395mAFSZGotZVr+sWEpO3c\nyC3VmXdBZmXmQdZqbdD/GuixJOYfqta2ytbIUPRXFN7/I7sgzxnXWBYXYmObYvdP\nokP0mQanY+WKxp7Q16pt1RoqoAd0kmV39g13rFl35muSHbSBoAW3GBF3gO+mF5Ty\n1ddp/XcgLOsmvNNjY+2HOD5F/RX0fs07mWnbD7x+xz7KEKjF+H7ZpkqCwmwCXaf0\niyYyh1852rti3Afw4mDxuVSD7sd9ggvYMc0QHIpQNkD4YWOhNiE1AB0zH57VbUYG\nUwIDAQAB\n-----END PUBLIC KEY-----\n",
                "status": "pending",
                "ts": "2018-05-17T18:41:23.342Z"
            },
        ],
        "created_ts": "2018-05-17T18:41:19.546Z",
        "updated_ts": "2018-05-17T18:41:23.342Z",
        "status": "preauthorized"
    }
]
```

In this case you can see that there are two authentication sets with the exact same device identity: `{"mac":"52:54:00:50:9b:84"}`, one `preauthorized` and one `pending`. So the device reported (see the `pending` set) the exact same identity as we preauthorized; however, there is a mismatch between the public keys.

The solution is to decommission the device and [remove all authentication sets](../../10.Server-integration/02.Preauthorizing-devices/docs.md#make-sure-there-are-no-existing-authentication-sets-for-your-device) and make sure the key used in the [preauthorize API call](../../10.Server-integration/02.Preauthorizing-devices/docs.md#call-the-preauthorize-api) matches exactly the one reported by the device, as seen in the `pending` data above.
