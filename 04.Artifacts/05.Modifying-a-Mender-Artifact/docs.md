---
title: Modifying a Mender Artifact
taxonomy:
    category: docs
---

A Mender Artifact is a file Mender uses to deploy updates. Please see
[Mender Artifacts](../../Architecture/Mender-Artifacts) for a more detailed
description.

When testing deployments, it is useful that the Artifact you are deploying
is different from the one that you have installed so you can see that the update is successful.
You might also want to configure certain aspects of the rootfs update after you build it,
but before deploying it.

## Prerequisites

#### tar

You need a standard `tar` utility, like the ones that are bundled with popular
Linux distributions.

#### git

The Golang compiler is integrated with `git`, so we need `git` installed
on the system. On Ubuntu this can be achieved with:

```
sudo apt-get install git
```

#### Golang compiler

Since the Mender Artifact utility is written in golang,
a Golang compiler needs to be installed and set up in order to build it.
You can find Golang download and installation instructions at
[https://golang.org/dl/](https://golang.org/dl/?target=_blank).

You should check the latest version, adjust the paths to your needs
and add the exports to your `.profile` as described when
clicking on the download link.
This is an example of installing and setting up Golang on a Linux system:

```
wget https://storage.googleapis.com/golang/go1.7.4.linux-amd64.tar.gz
```

```
sudo tar -C /usr/local -xzf go1.7.4.linux-amd64.tar.gz
```

```
export PATH=$PATH:/usr/local/go/bin
```

```
mkdir $HOME/golang && export GOPATH=$HOME/golang && cd $HOME/golang
```

After these steps, verify that Golang is correctly installed:

```
go version
```

> go version go1.7.4 linux/amd64


#### Mender Artifact utility

The Mender Artifact utility is available as open source in the
[Mender artifacts repository on GitHub](https://github.com/mendersoftware/artifacts?target=_blank).

You can download and install it with the follwoing commands:

```
go get github.com/mendersoftware/artifacts
```

```
cd $GOPATH/src/github.com/mendersoftware/artifacts/
```

```
go get ./...
```

You con now run the artifacts utility in `$GOPATH/bin/artifacts`, and make sure it works
by running:

```
$GOPATH/bin/artifacts -v
```

> artifact version 0.1


## Unpack the root file system

The Mender Artifact can be unpacked using a standard tar utility, like the
following:



## Modify the root file system

A simple way to achieve this is to loopback-mount the rootfs on your workstation
and modify the configuration files you need.

In this example we will modify  `/etc/issue` on an `ext4` file system
so you can see which rootfs image you are running just before the login prompt,
but these steps can be used for modifying any configuration file and for
several file system types.

```
sudo mkdir /mnt/rootfs
```

```
sudo mount -t ext4 -o loop <PATH-TO-ROOTFS-IMAGE>.ext4 /mnt/rootfs/
```

Now you can modify the file system found at `/mnt/rootfs`. For example,
you can change `/mnt/rootfs/etc/issue` so you can detect that a deployment
changed the system. After saving your modified files, simply unmount
the rootfs again:

```
sudo umount /mnt/rootfs
```

You need to adjust the path to the rootfs image and its type depending on the machine and file system you are building for.


## Create a new Mender Artifact

TODO: first find the original device types that the artifact is compatible with (you can also change it below, if you want).

TODO:

```
artifacts write rootfs-image -t vexpress-qemu -n test-update -u core-image-full-cmdline-vexpress-qemu.ext4 -o successful_image_update.mender
```


After deploying this rootfs image with Mender and rebooting, your configuration changes will be in effect!
