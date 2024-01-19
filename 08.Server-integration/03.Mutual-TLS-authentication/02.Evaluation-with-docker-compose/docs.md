---
title: Evaluation with docker
taxonomy:
    category: docs
---

<!-- AUTOMATION: execute=if [ "$TEST_ENTERPRISE" -ne 1 ]; then echo "TEST_ENTERPRISE must be set to 1!"; exit 1; fi -->

<!-- Cleanup code: stops the mTLS ambassador if running -->
<!-- AUTOMATION: execute=function cleanup() { -->
<!-- AUTOMATION: execute=if docker ps | grep registry.mender.io/mendersoftware/mtls-ambassador -->
<!-- AUTOMATION: execute=then -->
<!-- AUTOMATION: execute=docker stop $(docker ps | grep registry.mender.io/mendersoftware/mtls-ambassador | sed 's/ .*//') -->
<!-- AUTOMATION: execute=fi -->
<!-- AUTOMATION: execute=} -->
<!-- AUTOMATION: execute=trap cleanup EXIT -->


## Prerequisites


### Environment and keys

You need to populate the [env variables](../01.Keys-and-certificates/docs.md#env-variables) and have already [generated the keys](../01.Keys-and-certificates/docs.md#generating-the-keys).


### A clean docker environment

This step is optional and ensures you don't have any surprises with the IP in the later stages.

! Please note that it will stop and remove all your docker containers even if you have some unrelated to mender.

```bash
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

## Set up the mTLS edge proxy

The steps below will run the mtls server in a docker container.
It will consume the terminal but allow you to track the logs of the running server.


! Set the [env variables](../01.Keys-and-certificates/docs.md#env-variables) and [generated the keys](../01.Keys-and-certificates/docs.md#generating-the-keys) before executing the commands below. The generated keys need to be in the current active directory when you run the commands.

To start the edge proxy, run the following command:

```bash
docker run \
  -p 443:8080 \
  -e MTLS_MENDER_USER="$MENDER_USERNAME" \
  -e MTLS_MENDER_PASS="$MENDER_PASSWORD" \
  -e MTLS_MENDER_BACKEND=$MTLS_MENDER_BACKEND \
  -e MTLS_DEBUG_LOG=true \
  -v $(pwd)/server.crt:/etc/mtls/certs/server/server.crt \
  -v $(pwd)/server.key:/etc/mtls/certs/server/server.key \
  -v $(pwd)/ca.crt:/etc/mtls/certs/tenant-ca/tenant.ca.pem \
  $MTLS_IMAGE
```

### Confirm communication with the proxy

Assuming you run the docker image on your host, the container will start listening to the host port 443.

! Set the [env variables](../01.Keys-and-certificates/docs.md#env-variables) executing the commands below.
From a different terminal execute the command below:

``` bash
openssl s_client -connect $MTLS_IP:443

# In the mtls ambassador terminal look for a line similar to:
# 2023/08/18 15:51:21 http: TLS handshake error from 192.168.88.249:46612: tls: client didn't provide a certificate
# This means you can communicate with the server correctly
```

## Configure the device to use the proxy

Now that we have generated a key and certificate for the device and signed the certificate, we need to configure the device to use the proxy.

We will use a virtual device with QEMU in docker. If you want to use a physical device, the procedure will be the same, just keep in mind you need to adjust the IP address accordingly.

! Set the [env variables](#env_variabls) and make sure you're in the directory where you [generated the keys](../01.Keys-and-certificates/docs.md#generating-the-keys).


Start the virtual client in daemon mode and confirm it's working.

```bash
docker run -d -it -p 85:85 --pull=always mendersoftware/mender-client-qemu
sleep 10
docker ps | grep 'mendersoftware/mender-client-qemu' > /dev/null && echo "Virtual client start successfully"  || echo "Container is not running or failed to start"
CONTAINER_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -aqf "ancestor=mendersoftware/mender-client-qemu"))
```

The virtual client needs to start succesfully for the below commands to work.
If you're experiencing issues, please first check that you can ssh to the virtual client succesfully.
`ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -p 8822 root@$CONTAINER_IP`

! For versions prior the Mender client 4.0 replace `mender-authd` with `mender-client`


```bash
# Update certificates to the device
scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -P 8822 device-private.key root@$CONTAINER_IP:/data/mender/mender-cert-private.pem
scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -P 8822 device-cert.pem root@$CONTAINER_IP:/data/mender/mender-cert.pem

# Stop the mender-authd service
ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -p 8822 root@$CONTAINER_IP systemctl stop mender-authd

# Create mender.conf and modified etc/hosts
cat > mender.conf << EOF
{
  "InventoryPollIntervalSeconds": 5,
  "ServerURL": "https://$MTLS_DOMAIN",
  "TenantToken": "$TENANT_TOKEN",
  "UpdatePollIntervalSeconds": 5,
  "HttpsClient": {
    "Certificate": "/data/mender/mender-cert.pem",
    "Key": "/data/mender/mender-cert-private.pem"
  }
}
EOF


cat > hosts << EOF
127.0.0.1   localhost.localdomain           localhost
$MTLS_IP    $MTLS_DOMAIN
EOF

# Copy configuration files into the device's rootfs
scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -P 8822 mender.conf root@$CONTAINER_IP:/etc/mender/mender.conf
scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -P 8822 hosts root@$CONTAINER_IP:/etc/hosts
scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -P 8822 ca.crt root@$CONTAINER_IP:/usr/local/share/ca-certificates/mender/ca.crt

# Load the certificates on the device and start the mender-authd service
ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -p 8822 root@$CONTAINER_IP update-ca-certificates
ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -p 8822 root@$CONTAINER_IP systemctl start mender-authd
```


Since this change is the same on every device, it is natural to automate this as part of the build process for the disk image. See file installation instructions for [the Debian family](../../04.Operating-System-updates-Debian-family/03.Customize-Mender/docs.md#configuration-file) or [the Yocto Project](../../05.Operating-System-updates-Yocto-Project/05.Customize-Mender/docs.md#configuration-file) for more information.

## Verify that the device is accepted

If everything went as intended, your device shows up as `accepted` status in the Mender Server. You can log in to the Mender UI to ensure your device appears on the device list and reports inventory.

If your device is not showing up, make sure you installed the certificates correctly - both on the server and on the device. Check client logs and/or server logs for error messages that can identify what is wrong. See the [troubleshooting section on connecting devices](../../301.Troubleshoot/05.Device-Runtime/docs.md#mender-server-connection-issues) in this case.
