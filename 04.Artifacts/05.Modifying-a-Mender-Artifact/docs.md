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

For convenience, we can also make sure the `artifact` tool is in PATH:

```
export PATH=$PATH:$GOPATH/bin
```


## Unpack the root file system

The Mender Artifact can be unpacked using a standard tar utility,
we simply create a directory for it and unpack it.
For a BeagleBone black artifact, the commands and output
will look like the following:

```
mkdir core-image-base-beaglebone && tar -C core-image-base-beaglebone -xvf core-image-base-beaglebone.mender
```

> version  
> header.tar.gz  
> data/0000.tar.gz  

You can inspect the metadata files to learn about how they work,
but it is not recommended to modify them directly as this can
be quite error-prone. We will rather use the `artifacts` tool to make
modifications below.

The updates to be deployed are stored in the `data` subdirectory. We
can extract the first (and currently only) file there, which is the root file system,
like the following:

```
tar zxvf data/0000.tar.gz
```

> core-image-base-beaglebone.ext4  


## Modify the root file system

Once we have the file system image, a simple way to modify its contents
is to loopback-mount the rootfs on your workstation
and modify the configuration files you need in the mounted directory.

In this example we will modify  `/etc/issue` on an `ext4` file system
so you can see which rootfs image you are running just before the login prompt,
but these steps can be used for modifying any configuration file and for
several file system types.

First we make the mount directory and copy the rootfs image:

```
sudo mkdir /mnt/rootfs
```

```
cp core-image-base-beaglebone.ext4 core-image-base-beaglebone-modified.ext4
```

```
sudo mount -t ext4 -o loop core-image-base-beaglebone-modified.ext4 /mnt/rootfs/
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

#### Find required metadata from original Arifact

We would probably like to reuse some of the original Artifact metadata
for the new artifact, as for example the device types it is compatible
with is the same.

To see which metadata the original Artifact contains, you can run the
follwing command:

```
artifacts read core-image-base-beaglebone.mender
```


> Mender artifact:  
>   Name: release-1.0  
>   Format: mender  
>   Version: 1  
>   Compatible devices: '[beaglebone]'  
> 
> Updates:  
>   0000  
>   Type: 'rootfs-image'  
>   Files:  
>     core-image-base-beaglebone.ext4  
>     size: 101821440  
>     modified: 2016-12-05 17:35:21 +0100 CET  

The most important fields to note for writing a new artifact are
the *Compatible devices* and *Name*.


#### Write a new Artifact

We now have the information we need to generate a new Artifact,
including the metadata to use and modified rootfs.

In this example, we will keep the original *Compatible devices*
and *Name* of the original artifact, so only the rootfs modifications
will be different:

```
artifacts write rootfs-image -t beaglebone -n release-1.0 -u core-image-base-beaglebone-modified.ext4 -o core-image-base-beaglebone-modified.mender
```

After deploying this Artifact with Mender and rebooting, your configuration changes will be in effect!
