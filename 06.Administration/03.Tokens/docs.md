---
title: Token signing keys
taxonomy:
    category: docs
---

Mender backend uses JWT tokens for device and user authentication. The tokens
are cryptographically signed and their authenticity is verified when making
requests to the backend. Tokens are handed out
by [Device Authentication](https://github.com/mendersoftware/deviceauth)
and [User Administration](https://github.com/mendersoftware/useradm) services.

Before starting mender in production, one needs to provide RSA private keys in
PEM format for both services. This can be accomplished by generating key using
openssl:

```
openssl genpkey -algorithm RSA -out key.pem -pkeyopt rsa_keygen_bits:2048
```

and mounting the keys into respective containers by adding the following entry
to compose file (replacing local key paths with paths of your own):

```
    mender-useradm:
        volumes:
            - ./keys/useradm-private.pem:/etc/useradm/rsa/private.pem

    mender-device-auth:
        volumes:
            - ./keys/deviceauth-private.pem:/etc/deviceauth/rsa/private.pem
```

It is recommended to use separate keys for `mender-useradm` and
`mender-device-auth` services.
