---
title: Configuration options
taxonomy:
    category: docs
---

This section lists the Remote Terminal configuration options in `mender-connect.conf`.

#### ShellCommand

The path to a shell executable. Can be any executable file, fulfilling the following
conditions:
* is an absolute path
* exists in `/etc/shells`
* the user (see `User` below) can execute it

Example:

```
 "ShellCommand": "/bin/bash"
```

#### User

The name of a user that `mender-connect` will run the shell as. Must resolve to valid
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
If set to `false` `mender-connect` will
not touch the sessions. The value of `true` enables session expiration
handling.

##### ExpireAfter

The number of seconds aster startup of a session after which it is considered
to be expired.

##### ExpireAfterIdle

The number of seconds without activity (no input from the user) after which
`mender-connect` marks a session as expired. Note that you can specify both
`ExpireAfterIdle` and `ExpireAfter`, in which case you can think of the latter
as a "_hard limit_", i.e.: time after every `mender-connect` removes every session.

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

