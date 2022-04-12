---
title: Configuration file
taxonomy:
    category: reference
---

Mender Gateway uses a JSON file for configuring the proxy and mTLS settings. The
configuration is loaded from the file `/var/lib/mender/mender-gateway.conf` by
default, unless otherwise by the `--config` command line argument. This section
provides a reference for the configuration variables.

```json
{
    "Features": {
        "ArtifactsProxy": {
            "Enabled": true,
            "GatewayURL": "https://gateway.mender.io",
            "DomainWhitelist": ["s3.amazonaws.com", "s3.my-min.io"]
        }
        "mTLS": {
            "Enabled": true,
            "CACertificate": "/var/lib/mender/ca-cert.pem",
            "MenderUsername": "gateway@mender.io",
            "MenderPassword": "password123",
            "BlacklistPath": "/var/lib/mender/mtls-blacklist.txt"
        },
    },
    "HTTP": {
      "Enabled": false,
      "Listen": ":80"
    },
    "HTTPS": {
        "Enabled": true,
        "Listen": ":443",
        "ServerCertificate": "/var/lib/mender/server-cert.pem",
        "ServerKey": "/var/lib/mender/server-pkey.pem"
    },
    "UpstreamServer": {
        "URL": "https://hosted.mender.io",
        "InsecureSkipVerify": false
    },
    "DebugLog": false
}
```

### Features
#### ArtifactProxy

<dl>
<dt>Enabled</dt> <dd>Enable the Local Artifact Proxy.</dd>
<dt>GatewayURL</dt> <dd>The self-URL to the gateway.</dd>
<dt>DomainWhitelist</dt> <dd>List of whitelisted domains to proxy artifacts from.</dd>
</dl>

#### mTLS
<dl>
<dt>Enabled</dt> <dd>Enable forwarding of mutual TLS (mTLS) authentication requests.</dd>
<dt>CACertificate</dt> <dd>Path to Certificate Authority (CA) Certificate used
to sign authorized client certificates.</dd>
<dt>BlacklistPath</dt> <dd>Path to file listing blacklisted client certificate serial numbers.
The file is a new-line separated list of hexadecimal serial numbers.</dd>
<dt>MenderUsername</dt> <dd>Username (email) for the user representing the API Gateway.
This user will preauthorize devices with authorization to the gateway.
</dd>
<dt>MenderPassword</dt> <dd>Password credential to the <em>MenderUsername</em>.</dd>
</dl>
!!!! *Mender Enterprise Only*: Using
!!!! [RBAC](../../../02.Overview/12.Role.Based.Access.Control) you can create a new
!!!! user with a dedicated role to the user access scope to the
!!!! [preauthorization API
!!!! endpoint](https://docs.mender.io/api/#management-api-device-authentication-preauthorize) for the
!!!! gateway user.

### HTTP
<dl>
<dt>Enabled</dt> <dd>Enable proxy of plain HTTP requests.</dd>
<dt>Listen</dt> <dd>TCP network address to listen for incomming connections.</dd>
</dl>

! Do not enable [*HTTP*](#http) on public or untrusted networks - always use
! [*HTTPS*](#https) whenever possible.

### HTTPS
<dl>
<dt>Enabled</dt> <dd>Enable proxy of TLS-terminated HTTP requests.</dd>
<dt>Listen</dt> <dd>TCP network address to listen for incomming connections.</dd>
<dt>ServerCertificate</dt> <dd>Path to the public server certificate representing the server.</dd>
<dt>ServerKey</dt> <dd>Path to certificate key file.</dd>
</dl>

### UpstreamServer

<dl>
<dt>URL</dt> <dd>The upstream server URL for proxying device HTTP requests.</dd>
<dt>InsecureSkipVerify</dt> <dd>Skip verification of certificate claims.</dd>
</dl>
