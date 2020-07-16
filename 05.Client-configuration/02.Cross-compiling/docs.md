---
title: Cross-compiling
taxonomy:
    category: docs
---

By using Golang tools the Mender client can easily be cross-compiled to target
a number of different architectures.

! The Mender client must also be [integrated with your board](../../03.Devices/chapter.md), cross-compiling it is often one step in the board integration process.

This example is targeting the `armhf` architecture but is applicable to other
architectures with minor adjustments.


## Prerequisites

### A Golang environment

Follow the instructions
in the [official Golang page](https://golang.org/doc/install?target=_blank)
to create a working Golang environment.


### A cross-compiler toolchain

You will need a cross-compiler toolchain targeting your device.
If you are using Ubuntu and targeting `armhf`, install it with:

```bash
sudo apt install gcc-arm-linux-gnueabihf
```


## Compile the Mender client

First, fetch the Mender client source code:

```bash
go get github.com/mendersoftware/mender
```

Change directory to where the Mender sources are:

```bash
cd $GOPATH/src/github.com/mendersoftware/mender
```

<!--AUTOVERSION: "to use Mender %"/mender-->
Check out the version of the Mender client you want to compile; see `git tag` for available versions.
For example, to use Mender 2.3.0 run the following command:

<!--AUTOVERSION: "git checkout %"/mender-->
```bash
git checkout 2.3.0
```

Then cross-compile the `mender` binary with:

```bash
env CGO_ENABLED=1 \
    CC=arm-linux-gnueabihf-gcc \
    GOOS=linux \
    GOARCH=arm make build
```

After compilation has finished, the Mender binary is located at:

```bash
$GOPATH/src/github.com/mendersoftware/mender/mender
```

!!! The strip command for your toolchain can be used to reduce the size of the binary by removing symbols that are not needed on a production system. In our example, we can run `arm-linux-gnueabihf-strip mender`.
