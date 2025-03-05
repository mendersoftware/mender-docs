---
title: Configuration file
taxonomy:
	category: reference
---

Mender Gateway uses a JSON file for configuring the proxy and mTLS settings.
The configuration is loaded from the file `/etc/mender/mender-gateway.conf` by default,
unless otherwise specified by the `--config` command line argument.
This section provides a reference for the configuration variables.

```json
{
	"Features": {
		"ArtifactsProxy": {
			"Enabled": true,
			"GatewayURL": "https://gateway.mender.io",
			"DomainWhitelist": ["s3.amazonaws.com", "s3.my-min.io"],
			"ArtifactsCache": {
				"Enabled": true,
				"Path": "/var/cache/mender-gateway",
				"SignatureSecret": "KDbQ+Z9asYtPdRQoakM5lGs6xgkWyNx4",
				"LinkExpireDuration": "30m"
			}
		},
		"mTLS": {
			"Enabled": true,
			"CACertificate": "/var/lib/mender/ca-cert.pem",
			"MenderUsername": "gateway@mender.io",
			"MenderPassword": "password123",
			"BlacklistPath": "/var/lib/mender/mtls-blacklist.txt"
		},
		"DeviceSystem": {
			"Enabled": false,
			"SystemID": "REPLACE_WITH_YOUR_UNIQUE_SYSTEM_ID",
			"DefaultInventory": [
				{
					"Name": "region",
					"Value": "eu"
				}
			]
		}
	},
	"HTTP": {
	  "Enabled": false,
	  "Listen": ":80"
	},
	"HTTPS": {
		"Enabled": true,
		"Listen": ":443",
		"MinimumTLSVersion": "1.2",
		"ServerCertificate": "/var/lib/mender/server-cert.pem",
		"ServerKey": "/var/lib/mender/server-pkey.pem"
	},
	"UpstreamServer": {
		"URL": "https://hosted.mender.io",
		"CACertificate": "/etc/ssl/cert.pem",
		"InsecureSkipVerify": false
	}
}
```

!!! Hosted Mender is available in multiple [regions](/11.General/00.Hosted-Mender-regions/docs.md) to connect to. Make sure you select your desired one before proceeding.

<!--AUTOVERSION: "version <code>%</code>"/ignore-->
Starting from Mender Gateway version <code>1.3.0</code>, configurations can be overwritten using environment variables.
In the description below, the environment variable names are provided in the parenthesis.

### Features

#### ArtifactsProxy
<dl>
<dt>Enabled (<code>ARTIFACTS_PROXY_ENABLED</code>)</dt>
<dd>Enable the Local Artifact Proxy.</dd>

<dt>GatewayURL (<code>ARTIFACTS_PROXY_GATEWAY_URL</code>)</dt>
<dd>The self-URL to the gateway.</dd>

<dt>DomainWhitelist (<code>ARTIFACTS_PROXY_DOMAIN_WHITELIST</code>)</dt>
<dd>List of whitelisted domains to proxy Artifacts from.</dd>

<dt>ArtifactsCache</dt>
<dd>Configuration for the Artifact Cache, see below.</dd>
</dl>

#### ArtifactsCache
<dl>
<dt>Enabled (<code>ARTIFACTS_PROXY_CACHE_ENABLED</code>)</dt>
<dd>Enable the Artifact Cache (depends on [ArtifactsProxy](#artifactsproxy)).</dd>

<dt>Path (<code>ARTIFACTS_PROXY_CACHE_PATH</code>)</dt>
<dd>Path where to store the cached Artifacts.</dd>

<dt>SignatureSecret (<code>ARTIFACTS_PROXY_CACHE_SECRET</code>)
<dd>Base64 encoded HMAC256 secret used to sign links to download artifacts from local cache.<dd>

<dt>LinkExpireDuration (<code>ARTIFACTS_PROXY_CACHE_LINK_EXPIRE_DURATION</code>)</dt>
<dd>Sets the time before a signed URL for downloading a file from the cache expires.</dd>
</dl>

#### mTLS
<dl>
<dt>Enabled (<code>MTLS_ENABLED</code>)</dt>
<dd>Enable forwarding of mutual TLS (mTLS) authentication requests.</dd>

<dt>CACertificate (<code>MTLS_CA_CERTIFICATE</code>)</dt>
<dd>Path to Certificate Authority (CA) Certificate used to sign authorized client certificates.</dd>

<dt>BlacklistPath (<code>MTLS_BLACKLIST_PATH</code>)</dt>
<dd>
Path to file listing blacklisted client certificate serial numbers.
The file is a new-line separated list of hexadecimal serial numbers.
</dd>

<dt>MenderUsername (<code>MTLS_MENDER_USERNAME</code>)</dt>
<dd>
Username (email) for the user representing the API Gateway.
This user will preauthorize devices with authorization to the gateway.
</dd>

<dt>MenderPassword (<code>MTLS_MENDER_PASSWORD</code>)</dt>
<dd>Password credential to the <em>MenderUsername</em>.</dd>
</dl>

!!!! *Mender Enterprise Only*: Using
!!!! [RBAC](../../../02.Overview/12.Role-based-access-control) you can create a new
!!!! user with a dedicated role to the user access scope to the
!!!! [preauthorization API
!!!! endpoint](https://docs.mender.io/api/#management-api-device-authentication-preauthorize) for the
!!!! gateway user.

#### DeviceSystem
<!--AUTOVERSION: "version <code>%</code>"/ignore-->
This feature requires Mender Gateway version <code>1.1.0</code>
<dl>
<dt>Enabled (<code>DEVICE_SYSTEM_ENABLED</code>)</dt>
<dd>Enable the System feature.</dd>

<dt>SystemID (<code>DEVICE_SYSTEM_ID</code>)</dt>
<dd>
Defines a unique System identifier for the devices connected to this Mender Gateway.
Devices connected to the gateway will show a special attribute named <code>mender_gateway_system_id</code> in the reported inventory data.
</dd>

##### DefaultInventory
<dl>
<dt>Name</dt>
<dd>Name of the default inventory attribute</dd>

<dt>Value</dt>
<dd>Value of the default inventory attribute</dd>
</dl>

### HTTP
<dl>
<dt>Enabled (<code>HTTP_ENABLED</code>)</dt>
<dd>Enable proxy of plain HTTP requests.</dd>

<dt>Listen (<code>HTTP_LISTEN</code>)</dt>
<dd>TCP network address to listen for incomming connections.</dd>
</dl>

! Do not enable [*HTTP*](#http) on public or untrusted networks - always use
! [*HTTPS*](#https) whenever possible.

### HTTPS
<dl>
<dt>Enabled (<code>HTTPS_ENABLED</code>)</dt>
<dd>Enable proxy of TLS-terminated HTTP requests.</dd>

<dt>Listen (<code>HTTPS_LISTEN</code>)</dt>
<dd>TCP network address to listen for incomming connections.</dd>

<dt>MinimumTLSVersion (<code>HTTPS_MINMUM_TLS_VERSION</code>)
<dd>
The minimum accepted TLS version for connecting to the gateway <code>["1.0", "1.1", "1.2", "1.3"]</code>.<br>
<!--AUTOVERSION: "version <code>%</code>"/ignore-->
This feature is available from Mender Gateway version <code>1.1.0</code>.
</dd>

<dt>ServerCertificate (<code>HTTPS_SERVER_CERTIFICATE</code>)</dt>
<dd>Path to the public server certificate representing the server.</dd>

<dt>ServerKey (<code>HTTPS_SERVER_KEY</code>)</dt>
<dd>Path to certificate key file.</dd>
</dl>

### UpstreamServer
<dl>
<dt>URL (<code>UPSTREAM_SERVER</code>)</dt>
<dd>The upstream server URL for proxying device HTTP requests.</dd>

<dt>CACertificate (<code>UPSTREAM_SERVER_CA_CERTIFICATE</code>)</dt>
<dd>
Path to trusted CA certificate bundle for the upstream server.<br>
<!--AUTOVERSION: "version <code>%</code>"/ignore-->
This configuration is available from Mender Gateway version <code>1.3.0</code>.
</dd>

<dt>InsecureSkipVerify (<code>UPSTREAM_SERVER_INSECURE_SKIP_VERIFY</code>)</dt>
<dd>Skip verification of certificate claims.</dd>
</dl>
