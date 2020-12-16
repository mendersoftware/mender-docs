---
title: Configuration options
taxonomy:
    category: docs
---

This sections lists all the configuration options in `mender-shell.conf`.

#### HttpsClient

Allows you to configure a client certificate and private key.

##### Certificate

A path to the file in pem format holding the certificate.

##### Key

A path to a file holding the private key.

#### Servers

An array of json objects on the form `[{"ServerURL":
"https://mender-server.com"}, {"ServerURL": "https://mender-server2.com"},
...]`, where `ServerURL` has the same interpretation as the root [`ServerURL`
attribute](#ServerURL). If `Servers` entry is set, the configuration cannot
contain an additional `ServerURL` entry in the top level of the json
configuration. Upon an unserved request (4XX/5XX-response codes) the client
attempts the next server on the list in the given order. Please note that 
you can also use `"wss://..."` protocol in the URL.

#### ServerURL

The server URL is the basis for API requests. This needs to point to to the
server which runs the Mender server services. It should include the whole URL,
including `https://` and a trailing slash. *NOTE: This entry conflicts with
[`Servers` attribute](#Servers), i.e. the server only accepts one of these entries.*
Please note that you can also use `"wss://..."` protocol in the URL.
You have to specify at least one valid URL for a server to connect to.

#### ServerCertificate

The location of the public certificate of the server, if any. If this
certificate is missing, or the one presented by the server does not match the
one specified in this setting, mender-shell validates the server certificate using
standard certificate trust chains.

#### ShellCommand

The path to a shell executable. Can be any executable file, fulfilling the following
conditions:
* is an absolute path
* exists in `/etc/shells`
* the user (see `User` below) can execute it

Example:

```
 "Shell": "/bin/sh"
```

#### User

The name of a user that mender-shell will run the shell as. Must resolve to valid
user id and must posses a valid group id. This a mandatory field.

#### Terminal

Allows you to provide terminal settings.

##### Width

The number of characters in width.

##### Height

The number of characters in height.

Example:

```
    "Terminal": {
        "Height": 24,
        "Width": 80
    }
```

#### Sessions

User sessions settings.

##### StopExpired

Determines whether stopped sessions will be automatically expired and removed.
If set to `false` mender-shell will
not touch the sessions. The value of `true` enables session expiration
handling.

##### ExpireAfter

The number of seconds aster startup of a session after which it is considered
to be expired.

##### ExpireAfterIdle

The number of seconds without activity (no input from the user) after which
mender-shell marks a session as expired. Note that you can specify both
`ExpireAfterIdle` and `ExpireAfter`, in which case you can think of the latter
as a "_hard limit_", i.e.: time after every mender-shell removes every session.

##### MaxPerUser

The maximum number of concurrent sessions per user.

```
    "Sessions": {
      "StopExpired": false,
      "ExpireAfter": 255,
      "ExpireAfterIdle": 16,
      "MaxPerUser": 4
    }
```

