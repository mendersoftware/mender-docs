---
title: Certificate rotation
taxonomy:
    category: docs
---

When using a flat PKI (`Root CA → Device`), rotating client certificates requires updating the gateway and re-provisioning all devices at once. By using a two-level PKI where each device presents the full certificate chain (device cert + intermediate CA cert), you can rotate the intermediate CA without touching the gateway at all — old and new devices coexist until the rollout is complete.

## How it works

The gateway is configured to trust only the Root CA. Devices send both their device certificate and the intermediate CA that signed it during the TLS handshake. Since the Root CA stays constant, the gateway configuration never changes during a rotation.

## Setting up the PKI

### Generate the Root CA

The Root CA is long-lived and its certificate is the only thing the gateway needs.

```bash
openssl ecparam -genkey -name P-256 -noout -out root-ca.key

cat > root-ca.conf <<EOF
[req]
distinguished_name = req_distinguished_name
prompt = no
x509_extensions = v3_ca

[req_distinguished_name]
commonName=Root CA
organizationName=My Organization

[v3_ca]
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid:always,issuer
basicConstraints = critical, CA:true, pathlen:1
keyUsage = critical, keyCertSign, cRLSign
EOF

openssl req -new -x509 -key root-ca.key -out root-ca.crt -config root-ca.conf -days $((365*10))
```

### Generate the Intermediate CA

The intermediate CA signs device certificates and is the unit of rotation.

```bash
openssl ecparam -genkey -name P-256 -noout -out intermediate-ca.key

cat > intermediate-ca.conf <<EOF
[req]
distinguished_name = req_distinguished_name
prompt = no

[req_distinguished_name]
commonName=Intermediate CA v1
organizationName=My Organization
EOF

cat > intermediate-ca-ext.conf <<EOF
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid:always,issuer
basicConstraints = critical, CA:true, pathlen:0
keyUsage = critical, keyCertSign, cRLSign
EOF

openssl req -new -key intermediate-ca.key -out intermediate-ca.req -config intermediate-ca.conf
openssl x509 -req -CA root-ca.crt -CAkey root-ca.key -CAcreateserial \
  -in intermediate-ca.req -out intermediate-ca.crt \
  -extfile intermediate-ca-ext.conf -days $((365*5))
```

### Generate a device certificate and bundle the chain

Each device gets a certificate signed by the intermediate CA. The device presents both certificates (its own plus the intermediate CA) as a chain during the TLS handshake.

```bash
openssl ecparam -genkey -name P-256 -noout -out device.key

cat > device.conf <<EOF
[req]
distinguished_name = req_distinguished_name
prompt = no

[req_distinguished_name]
commonName=my-device-hostname.com
organizationName=My Organization
EOF

openssl req -new -key device.key -out device.req -config device.conf
openssl x509 -req -CA intermediate-ca.crt -CAkey intermediate-ca.key -CAcreateserial \
  -in device.req -out device.crt -days $((365*2))

# Bundle: device cert first, then the intermediate CA
cat device.crt intermediate-ca.crt > device-chain.pem
```

Provision `device-chain.pem` and `device.key` onto each device.

## Configuring the gateway

Point the gateway at the Root CA only — `MTLS_CA_CERTIFICATE` is the trust anchor for client certificates and `root-ca.crt` is the only thing it needs to verify any device chain. No intermediate CA certificate is mounted on the gateway side, which is what makes rotation possible without reconfiguration.

This example assumes you have already populated the [environment variables](../01.Keys-and-certificates/docs.md#environment-variables) and generated `server.crt`/`server.key` for the gateway's server-side TLS (see the [Keys and certificates](../01.Keys-and-certificates/docs.md) page; sign them with `root-ca.key` instead of `ca-private.key`).

```bash
sudo chown 65534 $(pwd)/server.crt $(pwd)/server.key $(pwd)/root-ca.crt
sudo chmod 0600 $(pwd)/server.key

docker run \
  -p 8443:8443 \
  -p 8080:8080 \
  --name mender-gateway \
  -e HTTPS_ENABLED="true" \
  -e HTTPS_LISTEN=":8443" \
  -e HTTP_ENABLED="true" \
  -e HTTP_LISTEN=":8080" \
  -e HTTPS_SERVER_CERTIFICATE="/etc/mender/certs/server.crt" \
  -e HTTPS_SERVER_KEY="/etc/mender/certs/server.key" \
  -e MTLS_CA_CERTIFICATE="/etc/ssl/certs/root-ca.crt" \
  -e MTLS_ENABLED="true" \
  -e MTLS_MENDER_PASSWORD="$MENDER_PASSWORD" \
  -e MTLS_MENDER_USERNAME="$MENDER_USERNAME" \
  -e UPSTREAM_SERVER_URL="$UPSTREAM_SERVER_URL" \
  -v $(pwd)/server.crt:/etc/mender/certs/server.crt \
  -v $(pwd)/server.key:/etc/mender/certs/server.key \
  -v $(pwd)/root-ca.crt:/etc/ssl/certs/root-ca.crt \
  $MENDER_GATEWAY_IMAGE --log-level debug
```

## Rotating the intermediate CA

To rotate, generate a new intermediate CA signed by the same Root CA. New devices get certificates signed by the new intermediate CA and present the new chain. Devices already in the field continue working — no gateway change required.

### Generate the new Intermediate CA

```bash
openssl ecparam -genkey -name P-256 -noout -out intermediate-ca-v2.key

cat > intermediate-ca-v2.conf <<EOF
[req]
distinguished_name = req_distinguished_name
prompt = no

[req_distinguished_name]
commonName=Intermediate CA v2
organizationName=My Organization
EOF

openssl req -new -key intermediate-ca-v2.key -out intermediate-ca-v2.req -config intermediate-ca-v2.conf
openssl x509 -req -CA root-ca.crt -CAkey root-ca.key -CAcreateserial \
  -in intermediate-ca-v2.req -out intermediate-ca-v2.crt \
  -extfile intermediate-ca-ext.conf -days $((365*5))
```

### Provision new devices with the new chain

```bash
openssl ecparam -genkey -name P-256 -noout -out device-v2.key
openssl req -new -key device-v2.key -out device-v2.req -config device.conf
openssl x509 -req -CA intermediate-ca-v2.crt -CAkey intermediate-ca-v2.key -CAcreateserial \
  -in device-v2.req -out device-v2.crt -days $((365*2))

cat device-v2.crt intermediate-ca-v2.crt > device-v2-chain.pem
```

The gateway accepts both `device-chain.pem` (v1) and `device-v2-chain.pem` (v2) because both intermediate CAs chain up to the trusted Root CA. Decommission v1 devices at your own pace.

## Verifying the chains

```bash
# Verify v1 chain
openssl verify -CAfile root-ca.crt -untrusted intermediate-ca.crt device.crt

# Verify v2 chain
openssl verify -CAfile root-ca.crt -untrusted intermediate-ca-v2.crt device-v2.crt
```
