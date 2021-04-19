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

In this tutorial we will highlight some key use cases covered by the `mender-artifact` utility.


## Prerequisites

#### mender-artifact

The `mender-artifact` utility is used to create and inspect Mender Artifacts.

Download the prebuilt `mender-artifact` binary for your platform following the links
in [Downloads section](../../downloads#mender-artifact-tool).


## Changing the Mender server

If you would like to change the Mender server the devices will be using,
you can use the `mender-artifact modify` parameter:

```bash
MENDER_SERVER_URL='https://hosted.mender.io'
MENDER_TENANT_TOKEN='<YOUR-MENDER-TENANT-TOKEN>'
mender-artifact modify artifact.mender --server-uri "$MENDER_SERVER_URL" --tenant-token "$MENDER_TENANT_TOKEN"
```

!!! The `--tenant-token` parameter is only needed for multi-tenant Mender servers like [hosted Mender](https://hosted.mender.io?target=_blank). You can find it under the [My organization](https://hosted.mender.io/ui/?target=_blank#/settings/my-organization) tab.

If you are using a self-signed certificate for the Mender server (not needed for hosted Mender), you can
include it in the Artifact using the `--server-cert` parameter:

```bash
mender-artifact modify artifact.mender --server-cert server.crt
```


! Currently the `mender-artifact modify` command only supports modifying ext4 payloads.

## Reading a configuration file

The `cat` parameter will output a file in the Artifact to standard output.
For example, to see `/etc/hosts`, run the following command:

```bash
mender-artifact cat artifact.mender:/etc/hosts
```


## Modifying a configuration file

Files can be copied into and out from the Artifact using the `cp` parameter.
For example, to modify any Mender client configuration, such as the polling interval,
first copy it out:

```bash
mender-artifact cp artifact.mender:/etc/mender/mender.conf /tmp/mender.conf
```

Open `/tmp/mender.conf` and make the desired modifications.
Afterwards, write it back into the Artifact:

```bash
mender-artifact cp /tmp/mender.conf artifact.mender:/etc/mender/mender.conf
```

!!! To control the permissions on the file written to the Mender Artifact, use the `install -m<permissions>` parameter instead of `cp`.


## Create an Artifact from a raw root file system

If you have a raw root file system (e.g. `ext4`), you can create a Mender Artifact
file from it.

! The Mender client and relevant configuration must already be contained in the root file system in order for the created Mender Artifact to be usable.

To create an Artifact, use the `write` parameter:

```bash
mender-artifact write rootfs-image -t beaglebone -n release-1 -f rootfs.ext4 -o artifact.mender
```

! The Artifact name (`-n`) must correspond to the name stated *inside* the root file system at `/etc/mender/artifact_info`.

! If you are building for *older Mender Clients* that do not support the latest
version of the Artifact format, you can build an older Artifact version with the
`-v` option. For example, to build a version 2 Artifact, you can run
`mender-artifact write rootfs-image -v 2 -t beaglebone -n release-1 -f
rootfs.ext4 -o artifact.mender`. The default Artifact version is the latest one.
Also see the build variable
[MENDER_ARTIFACT_EXTRA_ARGS](../yocto-project/variables#mender_artifact_extra_args).

!!! If you would like to generate a *signed Artifact*, simply add the `-k` option with the path to your *private key*. In our example above, the full command would be `mender-artifact write rootfs-image -t beaglebone -n release-1 -f rootfs.ext4 -o artifact-signed.mender -k private.key`.

## Artifact compression

Mender Artifacts are compressed with the `gzip` algorithm by default. Mender
supports three compression algorithms: `gzip` compression, `lzma` compression
and no compression. This can be selected when creating artifacts with
`mender-artifact` command with the global flag `compression`. For example, to
select `lzma` compression instead of the default `gzip`, run the following
command:

```bash
mender-artifact --compression lzma write rootfs-image -t beaglebone -n release-1 -f rootfs.ext4 -o artifact.mender
```

Use `mender-artifact --help` to list all available compression options.

## Signing after modification

If you are signing Artifacts, the signature will become invalid whenever
you make modifications to them. See the section on [signing and verification](../signing-and-verification#an-existing-mender-artifact)
for more information.


## Compiling mender-artifact

Compiling `mender-artifact` is only necessary if you can not use the prebuilt
[mender-artifact binary for Linux][x.x.x_mender-artifact].


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

<!--AUTOVERSION: "go%"/ignore-->
```bash
wget https://dl.google.com/go/go1.11.6.linux-amd64.tar.gz
```

<!--AUTOVERSION: "go%"/ignore-->
```bash
sudo tar -C /usr/local -xzf go1.11.6.linux-amd64.tar.gz
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

<!--AUTOVERSION: "go%"/ignore-->
> go version go1.7.4 linux/amd64


#### Build dependencies

Mender Artifact tool depends on LZMA library to support compression with this algorithm on the Artifacts.

To install this build dependency for Mac OS, run the following command:
```
brew install xz
```

To install it for Ubuntu or Debian Linux:
```
apt install liblzma-dev
```

#### Compile mender-artifact

The Mender Artifact utility is available as open source in the
[Mender artifact repository on GitHub](https://github.com/mendersoftware/mender-artifact?target=_blank).

Run the following commands to download, compile and install Mender Artifact:

```bash
go get github.com/mendersoftware/mender-artifact
```

```bash
cd $GOPATH/src/github.com/mendersoftware/mender-artifact/
```

<!--AUTOVERSION: "git checkout %"/mender-artifact -->
```bash
git checkout 3.4.2
```

```bash
go get -ldflags "-X main.Version=`git describe --tags --exact-match 2>/dev/null || git rev-parse --short HEAD`" ./...
```

You can now run the `mender-artifact` utility in `$GOPATH/bin/mender-artifact`, and make sure it works
by running:

```bash
$GOPATH/bin/mender-artifact -v
```

<!--AUTOVERSION: "mender-artifact version %"/mender-artifact -->
> mender-artifact version 3.4.2

For convenience, we can also make sure the `mender-artifact` utility is in PATH:

```bash
export PATH=$PATH:$GOPATH/bin
```
