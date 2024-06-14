---
title: Hosted Mender - tenant migration
taxonomy:
    category: docs
---


Historically we have only had a single instance in the US.
Hosted Mender instances are now available in [multiple regions](../../11.General/00.Hosted-Mender-regions/docs.md) as a result of our expansion.
This document will describe the migration process if you currently have a fleet of devices operating in one instance and would like to move them to another one.

!! Migration between instances without risks requires support assistance and is a payed service.
!! If you wish to migrate your account please contact us on [support@mender.io](mailto:support@mender.io?subject=Tenant%20migration) with the subject **Tenant migration**.

!! Please note that this method only applies for HM mender instances and isn't applicable for on-prem migrations.

## Introduction

Going forward, the following terms will be used for clarity:
* **Old server** will represent the server that you want to move away from
* **New server** will represent the server that you want to migrate to


The following steps summarize the procedure for moving from one server to another:

1. Make a clone of the old server by contacting Northern.Tech
2. Update the device with configuration for both servers
3. Reject the device on the Old server
4. Accept the device on the New server
5. Update the with configuration for the New server only

The diagram below, describes the flow

![Migration flow](migration-flow.png)


#### 1. Make a clone of the old server by contacting Northern.Tech

If you wish to migrate your account please contact us on [support@mender.io](mailto:support@mender.io) with the title **Tenant migration**.
In that request please share you "Organization name" as registered on Hosted Mender in "Organization and billing".
We will get back to you once the tenant has been cloned and you can proceed to the next step.


#### 2. Update the device with configuration for both servers

This will largely depend on the way you create build artifacts.
Regardless of the approach the goal to update the device so it's config (`/etc/mender/mender.conf`) changes from:

```
{
    "ServerURL": "https://hosted.mender.io",
    "TenantToken": "abcdefghijklm1234567890",
    ... <Other config parameters>
}
```

to

```
{
  "Servers": [
    {
      "ServerURL": "https://hosted.mender.io"
    },
    {
      "ServerURL": "https://eu.hosted.mender.io"
    }
  ],
  "TenantToken": "abcdefghijklm1234567890",
  ... <Other config parameters>
}
```

!! Make sure you removed the `ServerURL` entry from the top of the JSON configuration. [More info here](../../03.Client-installation/07.Configuration-file/50.Configuration-options/docs.md#servers).

Please check bellow for different approaches on how to achieve this:

* [Yocto](#yocto)
* [Debian](#debian)
* [Custom update module](#custom-update-module)


!! If you deploy a config file with a badly formatted json, `mender-client` on the device won't start correctly after the update.
!! The device will roll back to the previous version only after the device is restarted by other means.
!! During that server will show the deployment status as "rebooting" and after the roll back the deployment will fail.

Please make sure to test the migration with one device first before deploying it to the whole production fleet.

#### 3. Reject the device on the Old server

Once the deployment was successful and the device restarts, it will try communicating with the first server on the list.
That is the Old server.

As we want to stop the communication with the Old server, reject the device.

![reject-device](reject-device.png)

#### 4. Accept the device on the New server

As the device cannot connect to the first server on the list (Old server), it will try with the next one.
In this case, it is the New server.

#### 5. Update the with configuration for the New server only

Once the device is correctly showing on the New server the last step is to deploy the configuration containing only the New server.

```
{
    "ServerURL": "https://eu.hosted.mender.io",
    "TenantToken": "abcdefghijklm1234567890",
    ... <Other config parameters>
}
```

## Methods for changing the configuration

### Yocto

For Yocto project integrations, if you are already passing your own configuration file to the build,
as described in [Customize Mender](../../05.Operating-System-updates-Yocto-Project/05.Customize-Mender/docs.md#configuration-file), modify your `mender.conf` to include `Servers` array.

If instead you are relying on `meta-mender` to autogenerate a configuration file based on variables
you need to first capture the currently generated `mender.conf`, modify it, and use the [Customize
Mender](../../05.Operating-System-updates-Yocto-Project/05.Customize-Mender/docs.md#configuration-file) method
to inject it back into the build. The file can be captured from a live device or from yocto
`tmp/deploy/` directory (which will depend a bit on your setup).

At the end of the process you should have two mender artifacts:
* one containing the config for both Old and New server
* one containing the config for the New server only


### Debian

Similarly for Debian family integrations, if you are already passing your own configuration file with a [rootfs overlay](../../04.Operating-System-updates-Debian-family/03.Customize-Mender/docs.md#configuration-file), modify your `mender.conf` to include `Servers` array.

If instead you rely on the autogenerated `mender.conf`, capture it, modify it, and set it up in a [rootfs overlay](../../04.Operating-System-updates-Debian-family/03.Customize-Mender/docs.md#configuration-file).

The fields that need modification are:
* `ServerURL` shall be set to: `""` (empty string)
* `Servers` shall be set to: `[{ServerURL: "https://hosted.mender.io"}, {ServerURL: "https://eu.hosted.mender.io"}]`

You can do this manually with any text editor or using the `jq` command:

```
cat mender.conf | jq '
.ServerURL = "" |   # Blank existing ServerURL
.Servers = [        # Set Servers array of ServerURL(s)
  {ServerURL: "https://hosted.mender.io"},
  {ServerURL: "https://eu.hosted.mender.io"}
]' > mender.new.conf
```

At the end of the process you should have two mender artifacts:
* one containing the config for both Old and New server
* one containing the config for the New server only


### Custom Update Module

It is also possible do the migration without having to do a full rootfs update.
This can be done by deploying a custom Update Module just for this case.

!! Please note that the Update Module is provided as an example only.
!! It is not part of our internal testing pipelines.



``` bash
#!/bin/sh

set -e

STATE="$1"
FILES="$2"

case "$STATE" in
    ArtifactInstall)
        # Backup of current conf file
        cp /etc/mender/mender.conf /etc/mender/mender.old.conf

        # Modify current conf file
        cat /etc/mender/mender.conf | jq '
.ServerURL = "" |   # Blank existing ServerURL
.Servers = [        # Set Servers array of ServerURL(s)
  {ServerURL: "https://hosted.mender.io"},
  {ServerURL: "https://eu.hosted.mender.io"}
]' > /etc/mender/mender.new.conf

        # Set the new configuration
        cp -f /etc/mender/mender.new.conf /etc/mender/mender.conf
        ;;

    NeedsArtifactReboot)
        echo "Automatic"
        ;;

    SupportsRollback)
        echo "Yes"
        ;;

    ArtifactRollback)
        cp -f /etc/mender/mender.old.conf /etc/mender/mender.conf
        ;;

    Cleanup)
        # Delete used files
        rm /etc/mender/mender.old.conf /etc/mender/mender.new.conf
        ;;
esac
exit 0
```

The example includes a way to rollback if the configuration ended up unable to connect to the server (ArtifactRollback).
After the update is perform a reboot is requested (NeedsArtifactReboot) to ensure the Mender services restarts and load the new configuration.


In order to use the Update Module, it needs to be installed in the device filesystem.
To generate the artifact that installs the `migration-um-a` Update Module, the `single-artifact` Update Module can be used.

<!--AUTOVERSION: "github.com/mendersoftware/mender/blob/%/"/mender-->
Using the script [single-file-artifact-gen](https://github.com/mendersoftware/mender/blob/3.5.3/support/modules-artifact-gen/single-file-artifact-gen) makes this process easier.


### Create the Mender Artifact

Now create an Artifact with the updated `mender.conf` using the your current workflow to create

For this example, the following command will generate the artifact:

```bash
ARTIFACT_NAME="eu-migration-a"
DEVICE_TYPE="qemux86-64"
OUTPUT_PATH="eu-migration-a.mender"
DEST_DIR="/usr/share/mender/modules/v3/"
FILE="migration-um-a"
single-file-artifact-gen -n ${ARTIFACT_NAME} -t ${DEVICE_TYPE} -d ${DEST_DIR} -o ${OUTPUT_PATH} ${FILE}
```

Additionally, to trigger the `migration-um-a` Update Module, an additional artifact needs to be created. For this new artifact, the [mender-artifact](https://docs.mender.io/downloads#mender-artifact) cli tool will be used:

```bash
ARTIFACT_NAME="trigger-eu-mig-a"
DEVICE_TYPE="qemux86-64"
UPDATE_MODULE="migration-um-a"
FILE="migration-a.mender"
mender-artifact write module-image -t $DEVICE_TYPE -o $FILE -T $UPDATE_MODULE -n $ARTIFACT_NAME
````
