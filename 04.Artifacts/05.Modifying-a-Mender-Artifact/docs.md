---
title: Modifying a Mender Artifact
taxonomy:
    category: docs
---

A Mender Artifact is a file Mender uses to deploy updates. Please see
[Mender Artifacts](../../architecture/mender-artifacts) for a more detailed
description.

When testing deployments, it is useful that the Artifact you are deploying
is different from the one that you have installed so you can see that the update is successful.
You might also want to configure certain aspects of the update after you build it,
but before deploying it.

In this tutorial we will unpack a Mender Artifact, 
recognized by its `.mender` suffix, mount the rootfs (e.g. `.ext4`) inside it,
modify it, and then create a new Mender Artifact that has these modifications
by using the `mender-artifact` utility.


## Prerequisites

#### tar

You need a standard `tar` utility, like the ones that are bundled with popular
Linux distributions.


#### mender-artifact

The `mender-artifact` utility is used to create and inspect Mender Artifacts.

You can download a [prebuilt mender-artifact Linux binary here](http://d12mp0qik9d80b.cloudfront.net/2.0.0b1-build2/mender-artifact).

!!! If you need to build `mender-artifact` from source, please see [Compiling mender-artifact](#compiling-mender-artifact).


## Unpack the root file system

The Mender Artifact can be unpacked using a standard tar utility,
we simply create a directory for it and unpack it.
Depending on the version of the artifact used, for a BeagleBone Black Artifact, the commands and output
will look like the following:

```bash
mkdir core-image-base-beaglebone && tar -C core-image-base-beaglebone -xvf core-image-base-beaglebone.mender
```

> version  
> header.tar.gz  
> data/0000.tar.gz  

The output for the version 2 should look similar to the following:

> version  
> manifest  
> manifest.sig  
> header.tar.gz  
> data/0000.tar.gz  

You can inspect the metadata files to learn about how they work,
but it is not recommended to modify them directly as this can
be quite error-prone. We will rather use the `mender-artifact` utility to make
modifications below.

The updates to be deployed are stored in the `data` subdirectory. We
can extract the first (and currently only) file there, which is the root file system,
like the following:

```bash
cd core-image-base-beaglebone && tar zxvf data/0000.tar.gz
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

```bash
sudo mkdir /mnt/rootfs
```

```bash
cp core-image-base-beaglebone.ext4 core-image-base-beaglebone-modified.ext4
```

```bash
sudo mount -t ext4 -o loop core-image-base-beaglebone-modified.ext4 /mnt/rootfs/
```

Now you can modify the file system found at `/mnt/rootfs`. For example,
you can change `/mnt/rootfs/etc/issue` so you can detect that a deployment
changed the system. After saving your modified files, simply unmount
the rootfs again:

```bash
sudo umount /mnt/rootfs
```

You need to adjust the path to the rootfs image and its type depending on the machine and file system you are building for.


## Create a new Mender Artifact

#### Find required metadata from original Artifact

We would probably like to reuse some of the original Artifact metadata
for the new Artifact, as for example the device types it is compatible
with is the same.

To see which metadata the original Artifact contains, you can run the
following command:

```bash
mender-artifact read core-image-base-beaglebone.mender
```


> Mender artifact:  
>   Name: release-1  
>   Format: mender  
>   Version: 2  
>   Compatible devices: '[beaglebone]'  
>   
> Updates:  
>   0000  
>   Type: 'rootfs-image'  
>   Files:  
>     core-image-base-beaglebone.ext4  
>     size: 105638912  
>     modified: 2016-12-20 15:36:11 +0100 CET  


The most important fields to note for writing a new Artifact are
the *Compatible devices* and *Name*.

!!! When working with a signed Artifact, you can verify the signature by providing the public verification key to the `-k` option, e.g. `mender-artifact read core-image-base-beaglebone.mender -k public.key`.


#### Write a new Artifact

We now have the information we need to generate a new Artifact,
including the metadata to use and modified rootfs.

In this example, we will keep the original *Compatible devices*
and *Name* of the original Artifact, so only the rootfs modifications
will be different:

```bash
mender-artifact write rootfs-image -t beaglebone -n release-1 -u core-image-base-beaglebone-modified.ext4 -o core-image-base-beaglebone-modified.mender
```

! The Artifact name (`-n`) must correspond to the name stated *inside* the root file system at `/etc/mender/artifact_info`, so make sure to change both places if you are modifying it.

! If you are building for *older Mender Clients* that do not support the latest version of the Artifact format, you can build an older Artifact version with the `-v` option. For example, to build a version 1 Artifact, you can run `mender-artifact write rootfs-image -v 1 -t beaglebone -n release-1 -u core-image-base-beaglebone-modified.ext4 -o core-image-base-beaglebone-modified.mender`. The default Artifact version is the latest one. Also see the build variable [MENDER_ARTIFACT_EXTRA_ARGS](../variables#mender_artifact_extra_args).

!!! If you would like to generate a *signed Artifact*, simply add the `-k` option with the path to your *private key*. In our example above, the full command would be `mender-artifact write rootfs-image -t beaglebone -n release-1 -u core-image-base-beaglebone-modified.ext4 -o core-image-base-beaglebone-signed.mender -k private.key`.

After deploying this Artifact with Mender and rebooting, your configuration changes will be in effect!


## Compiling mender-artifact

Compiling `mender-artifact` is only necessary if you can not use the prebuilt
[mender-artifact binary for Linux](http://d12mp0qik9d80b.cloudfront.net/2.0.0b1-build2/mender-artifact).


#### Install git


The Golang compiler is integrated with `git`, so we need `git` installed
on the system. On Ubuntu this can be achieved with:

```bash
sudo apt-get install git
```


#### Install the Golang compiler

Since the Mender Artifact utility is written in golang,
a Golang compiler needs to be installed and set up in order to build it.
You can find Golang download and installation instructions at
[https://golang.org/dl/](https://golang.org/dl/?target=_blank).

You should check the latest version, adjust the paths to your needs
and add the exports to your `.profile` as described when
clicking on the download link.
This is an example of installing and setting up Golang on a Linux system:

```bash
wget https://storage.googleapis.com/golang/go1.7.4.linux-amd64.tar.gz
```

```bash
sudo tar -C /usr/local -xzf go1.7.4.linux-amd64.tar.gz
```

```bash
export PATH=$PATH:/usr/local/go/bin
```

```bash
mkdir $HOME/golang && export GOPATH=$HOME/golang && cd $HOME/golang
```

After these steps, verify that Golang is correctly installed:

```bash
go version
```

> go version go1.7.4 linux/amd64


#### Compile mender-artifact

The Mender Artifact utility is available as open source in the
[Mender artifact repository on GitHub](https://github.com/mendersoftware/mender-artifact?target=_blank).

You can download and install it with the following commands:

```bash
go get github.com/mendersoftware/mender-artifact
```

```bash
cd $GOPATH/src/github.com/mendersoftware/mender-artifact/
```

```bash
go get ./...
```

You can now run the `mender-artifact` utility in `$GOPATH/bin/mender-artifact`, and make sure it works
by running:

```bash
$GOPATH/bin/mender-artifact -v
```

> mender-artifact version 0.1

For convenience, we can also make sure the `mender-artifact` utility is in PATH:

```bash
export PATH=$PATH:$GOPATH/bin
```
