---
title: Create a Delta update Artifact
taxonomy:
    category: docs
    label: tutorial
---


This document explains how to create a binary delta artifact from two Operating System artifacts using the `mender-binary-delta-generator` CLI tool.
Generation of the delta is something you would execute on a command line of a machine running Linux.

For a step by step working example please check the [mender hub post](https://hub.mender.io/t/robust-delta-update-rootfs/1144).


### Prerequisites

This tutorial assumes:

* You have completed the [integration of the mender-binary-delta](../../05.Operating-System-updates-Yocto-Project/05.Customize-Mender/01.Delta-update-support/docs.md) into your Yocto built process
    * `mender-binary-delta-generator` is available in `PATH`
* You have installed [mender-artifact](../../10.Downloads/docs.md#mender-artifact) which is a dependency for `mender-binary-delta-generator`
* You have two Operating System artifacts available to work with


### Generating the delta - default case

Execute the steps below to generate the delta artifact:

```bash
# rootfs-v1.mender - release running on the device
# rootfs-v2.mender - new release

mender-binary-delta-generator -o delta-v1-v2.mender rootfs-v1.mender rootfs-v2.mender
```

The result (`delta-v1-v2.mender`) is a delta artifact containing only the difference between the two artifacts. Once uploaded to the Mender server, the delta artifact will be listed in the web UI under the same release as the `rootfs-v2.mender`. This is because deploying this delta on a device results in the same version as deploying `rootfs-v2.mender`.


!! A running device will only accept a delta update once at least one full system update has been deployed first.

### Generating the delta - custom compression values (Special use case only)

! Changing the parameters might be beneficial under some circumstances. However, please note that troubleshooting issues that arise as a result of using custom parameters (calling mender-binary-delta with the -D flag) are not covered by official support nor are different combinations continuously tested.

`mender-binary-delta` uses the xdelta compression tool underneath.
It is possible to pass flags to the xdelta directly.
This allows you to customize [the parameters](https://github.com/jmacd/xdelta/blob/wiki/TuningMemoryBudget.md#source-buffer-size) of the compression algorithm.
Depending on the payload of the artifact, this can influence the size of the delta and the memory requirements for encoding/decoding the delta.

The example below will generate a delta artifact using the custom xdelta flags.

```
XDELTA_FLAGS="-B524288000 -W150000 -P262144 -I62768"
mender-binary-delta-generator -o delta-v1-v2.mender -D "${XDELTA_FLAGS}" rootfs-v1.mender rootfs-v2.mender -- -- ${XDELTA_FLAGS}
```

The flags will be embedded in the artifact and passed to the algorithm on the client side also.
You can confirm the existence of the flags in the artifact with the command below.

```
mender-artifact read delta-v1-v2.mender

<Unrelated content before...>
    Metadata:
	{
	  "decoder_arguments": [
	    "-B524288000",
	    "-W150000",
	    "-P262144",
	    "-I62768"
	  ],
	  "delta_algorithm": "xdelta3",
	  "rootfs_file_size": 964689920
	}
<Unrelated content after...>
```


#### Finding the parameters

Fine tuning the parameters to your needs can be a trial and error process.
The snippet below is a best effort reference to get you started.

```
# Source buffer size          -B  Default=67108864(64M)  [16384(16K) - Unlimited]
# Input window size           -W  Default=8192    ( 8M)  [16384(16K) - 16777216(16M)]
# Instruction buffer size     -I  Default=32768(32KB)    [ min?      - 0 (Unlimited) ]
# Compression duplicates size -P  Default=262144(256KB)  P <= W, Must be power of 2

XDELTA_FLAGS="-B524288000 -W150000 -P262144 -I62768"
XDELTA_FLAGS_FOR_FILENAME=$(echo $XDELTA_FLAGS | sed 's/ //g')
mender-binary-delta-generator -o delta-v1-v2-${XDELTA_FLAGS_FOR_FILENAME}.mender -D "${XDELTA_FLAGS}" rootfs-v1.mender rootfs-v2.mender -- -- ${XDELTA_FLAGS}
```
