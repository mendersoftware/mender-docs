---
title: Prepare a virtual device
taxonomy:
    category: docs
---

!!! Skip this section if you have already completed [Prepare a Raspberry Pi device](../01.Prepare-a-Raspberry-Pi-device/docs.md)

This guide we help you prepare your workstation to be able to run a virtual
device (QEMU) with Mender integrated which will connect to hosted Mender and
simulate a physical device.

You will get specific instructions tailored to your hosted Mender account on how
to start the virtual device in the hosted Mender UI during the
[Deploy an application update](../../02.Deploy-an-application-update/docs.md)
guide, as you also need to provide information about your account for it to be
able to connect. This guide is only a reference on how to interact with the
virtual device, e.g establishing a SSH session.

Example instructions from the UI:

![Upload web page](image_0.png)

## Prerequisites

To follow this guide, ensure
[Docker Engine](https://docs.docker.com/engine/install?target=_blank) is
installed.

## Step 1 - Download the Docker image for the virtual device

The virtual device with Mender integrated is shipped as a Docker container.

Download the prebuilt image from
[Docker Hub](https://hub.docker.com/r/mendersoftware/mender-client-qemu?target=blank):

```bash
docker pull mendersoftware/mender-client-qemu:latest
```

## Step 2 - Run the virtual device

Start the virtual device in detached mode:

```bash
docker run -d mendersoftware/mender-client-qemu:latest
```

Note that we did not give any information about the hosted Mender server when
starting the virtual device here, hence it will not connect to a server instance
at this stage. This will be covered later.

Verify that it started with:

```bash
docker ps
```

Example output:

>```bash
>$ docker ps
>CONTAINER ID        IMAGE                                      COMMAND             CREATED             STATUS              PORTS               NAMES
>d335f50101cb        mendersoftware/mender-client-qemu:latest   "./entrypoint.sh"   6 minutes ago       Up 6 minutes        8822/tcp            relaxed_leakey
>```

Save the `CONTAINER_ID` in a shell variable that will be used later to find
information about the running container:

```bash
CONTAINER_ID="d335f50101cb"
```

!!! Replace above value with actual result that you get.

## Step 3 - Get the IP address of the virtual device

Lookup the IP address of the virtual device (we will save it a shell variable):

```bash
IP_ADDRESS=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' "${CONTAINER_ID}")
```

Example output:

>```bash
>$ echo "${IP_ADDRESS}"
>172.17.0.3
>```

Finding the IP address is a crucial step, and it will be referenced to in later
in the documentation if you are testing deployments on a virtual device.

## Step 4 - Connect to the virtual device using SSH

Connect to the virtual device using SSH (no password for login on virtual device):

```bash
ssh -p 8822 "root@${IP_ADDRESS}"
```

You should end up with a prompt similar to this:

>```bash
> root@qemux86-64:~#
>```

Terminate the SSH session:

```
exit
```

## Step 5 - Stop the virtual device

Stop the virtual device:

```bash
docker stop "${CONTAINER_ID}"
```


## Next step

Proceed to [Deploy an application update](../../02.Deploy-an-application-update/docs.md).
