---
title: Prerequisites
taxonomy:
    category: docs
---


## Environment variables

Setting up the mtls requires some env variables for the copy-paste commands to work.

You must set these multiple times if you run commands on different terminals.

Not all the variables are needed for all commands, but just setting them all every time is less thinking.

We suggest copying these to a temporary text file, filling them with your values and keeping them at hand while going through evaluation.


<!--AUTOVERSION: "mender-gateway:%"/mender-gateway-->
```bash
# For evaluation, define an arbitrary domain for the mtls server (we will modify `/etc/hosts` on the device).
# No external registration will take place.
export MENDER_GATEWAY_DOMAIN="local-domain-1993028.com"

# This is the IP of the pc you'll be running the mtls proxy on.
# Once the container is running this is the IP we'll be expected to communicate with it
# Is this the shell you'll be running the container on?
#    You can use `ip route get 8.8.8.8 | awk '{print $7}' | head -n 1` to get the IP
export MENDER_GATEWAY_IP=


# You need to create a separate user on your Hosted Mender instance.
# The Mender Gateway will authenticate devices on Hosted Mender as this user.
# Fill these with the credentials of your newly created user.
export MENDER_USERNAME="mtls@mender.io"
export MENDER_PASSWORD="password"

# Please check the URL if your account as this can be i.e. eu.hosted.mender.io
export UPSTREAM_SERVER_URL="https://hosted.mender.io"
# Located under Settings->Organisation and billing->Organization token once logged to the UI of Hosted Mender
export TENANT_TOKEN="U3VwZXIgTWVuZGVyIG1hbidzIHNlY3JldCB0b2tlbiE"

# Docker registry configuration
export DOCKER_REGISTRY_URL=registry.mender.io
export DOCKER_REGISTRY_USERNAME=
export DOCKER_REGISTRY_PASSWORD=

# The name and version of the mtls server container
export MENDER_GATEWAY_IMAGE=${DOCKER_REGISTRY_URL}/mendersoftware/mender-gateway:master
```


## Access to the Mender Gateway container

You need to have the correct credentials to get the enterprise container.
This section shows how to confirm correct credentials in isolation.

!!! Set the [environment variables](#environment-variables) before executing these commands.

```bash
docker logout $DOCKER_REGISTRY_URL
echo $DOCKER_REGISTRY_PASSWORD  | docker login  -u "$DOCKER_REGISTRY_USERNAME" --password-stdin $DOCKER_REGISTRY_URL
docker run --rm $MENDER_GATEWAY_IMAGE --help
```

In the success case this will print the following output:

```text
Mender Gateway
Usage: mender-gateway [flags]
Flags:
      --config FILE       Configuration JSON FILE (default "/etc/mender/mender-gateway.conf")
  -h, --help              Show this help text.
      --log-level LEVEL   Log LEVEL, <debug|info|warn|error|fatal> (default "info")
      --version           Print version and exit.
```


## PKI keys and certificates

To set up Mender Gateway in  mutual TLS mode for evaluation, you need the following keys and certificates:
* `ca-private.key` - the private key of the Certificate Authority (CA)
* `ca.crt` the self signed certificate of the Certification Authority (CA)
* `server.crt` -  the public server certificate for Mender Gateway signed by the CA
* `server.key` - the private key for `server.crt`
* `device-cert.pem` - the public client certificate for the device signed by the CA
* `device-private.key` - the private key for the `device-cert.pem`

For evaluation, we provide a list of steps to generate all those keys.
These prioritize the simple way to get to an end-to-end example and isn't intended for production.

##### Production considerations

When going to production you should know how to make security decisions on the following:
* Will I use an external or internal CA?
* Will I use the same CA for the client and the server certificates?
* What will be the domain of my Mender Gateway?


### Generating the keys

These keys are primarily intended for evaluation with docker.
If you're evaluating the kubernetes deployment, these can be used as well, but please note that they aren't following the security practices.

You need to have `openssl` present on the machine where you will be generating the keys.

Execute the following to generate all the required keys:

!!! Set the [env variables](#environment-variables) before executing these commands

```bash
openssl ecparam -genkey -name P-256 -noout -out ca-private.key
cat > ca.conf <<EOF
[req]
distinguished_name = req_distinguished_name
prompt = no
x509_extensions = v3_ca

[req_distinguished_name]
commonName=My CA
organizationName=My Organization
organizationalUnitName=My Unit
emailAddress=myusername@example.com
countryName=NO
localityName=Oslo
stateOrProvinceName=Oslo

[v3_ca]
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid:always,issuer
basicConstraints = critical, CA:true
keyUsage = critical, keyCertSign, digitalSignature
EOF

openssl req -new -x509 -key ca-private.key -out ca.crt -config ca.conf -days $((365*10))
openssl ecparam -genkey -name P-256 -noout -out server.key

cat > server.conf <<EOF
[req]
distinguished_name = req_distinguished_name
prompt = no

[req_distinguished_name]
commonName=$MENDER_GATEWAY_DOMAIN
organizationName=My Organization
organizationalUnitName=My Unit
emailAddress=myusername@example.com
countryName=NO
localityName=Oslo
stateOrProvinceName=Oslo
EOF
openssl req -new -key server.key -out server.req -config server.conf
openssl x509 -req -CA ca.crt -CAkey ca-private.key -CAcreateserial -in server.req -out server.crt -days $((365*2))
openssl ecparam -genkey -name P-256 -noout -out device-private.key
cat > device-cert.conf <<EOF
[req]
distinguished_name = req_distinguished_name
prompt = no

[req_distinguished_name]
commonName=my-device-hostname.com
organizationName=My Organization
organizationalUnitName=My Unit
emailAddress=myusername@example.com
countryName=NO
localityName=Oslo
stateOrProvinceName=Oslo
EOF
openssl req -new -key device-private.key -out device-cert.req -config device-cert.conf
openssl x509 -req -CA ca.crt -CAkey ca-private.key -CAcreateserial -in device-cert.req -out device-cert.pem -days $((365*10))
```
