---
title: Preauthorizing devices
taxonomy:
    category: docs
---

The Mender client will implicitly authorize the Mender server to manage it if the server holds the key corresponding to the [server certificate the client was provisioned with](../../artifacts/building-for-production#including-the-client-certificates). This tutorial shows the steps required to securely automate the other direction: authorizing the Mender client to be accepted by the Mender server.

The Mender server supports [preauthorizing devices](../../architecture/device-authentication#preauthorization-flow), where you add the [identity](../../client-configuration/identity) and public key of the device to the Mender server before the device connects for the first time. This way the device is automatically authorized to receive software updates when it connects to the server for the first time. This is in particular useful in a mass production setting because you can preauthorize devices when they are manufactured so they automatically get accepted into the Mender server when your customer turns them on, which might happen several months after manufacturing.

See [Device authentication](../../architecture/device-authentication) for a general overview of how device authentication works in Mender.


## Prerequisites


### A device integrated with Mender

You need a physical device that has already been [integrated with Mender](../). For example, you may use one of the reference devices BeagleBone Black or Raspberry Pi 3.


### A disk image for your device

We assume you have either [built a disk image for your device](../../artifacts/building-mender-yocto-image) or base it off one of the [pre-built demo images](../../getting-started/download-test-images). Note that a disk image is used to provision the entire storage of the device (it contains *all* the partitions) and typically has the `.sdimg` suffix.


### The identity of your device

When preauthorizing a device you need to know its [identity](../../client-configuration/identity). This is one or more key-value attributes, depending on the identity scheme you are using. If you connect your device so it shows up as pending in the Mender server, you will see its identity in the Mender server UI (note it is *not* the ID of the device, but the key-value attributes under Identity).

By default the Mender client uses the [MAC address of the first interface](https://github.com/mendersoftware/mender/blob/master/support/mender-device-identity?target=_blank) on the device as the device identity, for example `mac=02:12:61:13:6c:42`.

### Mender client and server connectivity

Once your device boots with a newly provisioned disk image, it should already be correctly connecting to the Mender server. After booting the device you see your device pending authorization in the Mender server UI, similar to the following.

![Mender UI - device pending authorization](device-pending-authorization.png)

If your device does not show as pending authorization in the Mender server once it is booted with the disk image, you need to diagnose this issue before continuing. See [Deploy to physical devices](../../getting-started/deploy-to-physical-devices) for a tutorial on connecting your device.


### No record of your device in the Mender server

If you have previously connected the device you want to preauthorize (e.g. to test connectivity), it is important that you *decommission it from the server* or simply provision a new server. Stale device identity, key and authentication sets in the Mender server for your device may prevent you from successfully preauthorizing your device.

Also make sure to power off your device before continuing, so it does not appear as pending in your server again.


## Generate a client keypair

Before we preauthorize the device, we need its 1) identity and 2) public key. You should already know the identity of your device from the [prerequsite above](#the-identity-of-your-device).

When preauthorizing a device, device keys will be generated on a separate system and provisioned into the device storage. This way we can keep records of the public key of the device and ensure sufficient entropy during key generation, so the resulting keys are secure random.

We will use a script to generate a keypair the Mender client understands; it uses the `openssl` command to generate the keys. Download the [keygen-client](https://github.com/mendersoftware/mender/blob/master/support/keygen-client?target=_blank) script into a directory and ensure it is executable. Run it without parameters:

```bash
./keygen-client
```

The generated Mender client keypair is placed in a subdirectory `keys-client-generated`:

```bash
keys-client-generated/
├── private.key
└── public.key
```


## Preauthorize your device

Now that we have the device's identity and public key, we will use the Mender server [management REST APIs](../../apis/management-apis) to preauthorize it.


### Set up a CLI environment for your server

Open a terminal, which we will use in the following to call the Mender server's REST APIs. First set a shell varialbe with the URI of your server:
```bash
MENDER_SERVER_URI='https://hosted.mender.io'
```

!!! Adjust the variable value to the Mender server you are using.

Now obtain a management API JSON Web Token by using the [login API](../../apis/management-apis/user-administration-and-authentication#log-in-to-mender):

```bash
MENDER_SERVER_USER='myusername@example.com'
JWT=$(curl -X POST -u $MENDER_SERVER_USER $MENDER_SERVER_URI/api/management/v1/useradm/auth/login)
```

!!! Replace `myusername@example.com` with your email address used to log in at the Mender server. If you are using self-signed certificates in a demo setup you may want to skip validation with the `-k` option (this is insecure).

You should now have an API token you can use to call any of the [Mender server management APIs](../../apis/management-apis) in the `JWT` shell variable.


### Make sure there are no existing authentication sets for your device

If your device identity has previously connected to the Mender server it may be in `pending` or  `rejected` state, which may preclude us from successfully preauthorizing it.
To make sure that the device is not in an existing authentication set, we check *both* the `admission` and `devauth` services for the identity of your device.

In the same terminal, run the following commands:

```bash
curl -H "Authorization: Bearer $JWT" $MENDER_SERVER_URI/api/management/v1/admission/devices | python -m json.tool > /tmp/admission.json
curl -H "Authorization: Bearer $JWT" $MENDER_SERVER_URI/api/management/v1/devauth/devices | python -m json.tool > /tmp/devauth.json
```

!!! To make the response more readable, we use the `json.tool` module of python to indent it. If it is not available on your system you can omit this pipe or replace it with a different indentation tool (remove or replace `| python -m json.tool`).

Now open the files `/tmp/admission.json` and `/tmp/devauth.json` and search for a value of your device identity (e.g. `02:12:61:13:6c:42` if you are using MAC addresses).

If you do not get any matches in either files, great! Continue to the [next section](#call-the-preauthorize-api).

If you do have one or more matches you must first delete these existing authentication sets. Find the `id` of the authentication set and use the `DELETE` method towards the service. For example, if you find the identity in `admission.json` and you see the authentication set has `id` `5ae3a39d3cd4d40001482a95` the run the following command:

```bash
curl -H "Authorization: Bearer $JWT" -X DELETE $MENDER_SERVER_URI/api/management/v1/admission/devices/5ae3a39d3cd4d40001482a95
```

Once this is done, re-run the two commands above to generate the two `.json` files again and verify that your device identity does not exist anywhere.

### Call the preauthorize API

Set your device identity as a JSON object in a shell variable while escaping quotation marks:

```bash
DEVICE_IDENTITY_JSON_OBJECT_STRING='{\"mac\":\"02:12:61:13:6c:42\"}'
```

!!! Adjust the variable value to the actual identity of your device. If you have several identity attributes in your identity scheme, separate them with commas in JSON format inside this single object, for example `DEVICE_IDENTITY_JSON_OBJECT_STRING='{\"mac\":\"02:12:61:13:6c:42\", \"serialnumber\":\"1928819\"}'`.

Secondly, set the contents of the device public key you generated above in a second variable (with newlines written out literally):

```bash
DEVICE_PUBLIC_KEY="$(cat keys-client-generated/public.key | sed -e :a  -e 'N;s/\n/\\n/;ta')\n"
```

Then simply call the [API to preauthorize a device](../../apis/management-apis/device-admission#devices-post):

```bash
curl -H "Authorization: Bearer $JWT" -H "Content-Type: application/json" -X POST --data-binary "{ \"device_identity\" : \"$DEVICE_IDENTITY_JSON_OBJECT_STRING\", \"key\" : \"$DEVICE_PUBLIC_KEY\" }" $MENDER_SERVER_URI/api/management/v1/admission/devices
```

If there is no output from the command, this indicates it succeeded. To verify, list the currently registered authentication sets and make sure there is one for your device with the `preauthorized` status:

```bash
curl -H "Authorization: Bearer $JWT" $MENDER_SERVER_URI/api/management/v1/admission/devices | python -m json.tool
```

Your device should now be preauthorized and accepted to the Mender server once it connects with the exact same identity and key.


## Copy generated device key to disk image

TODO: This does not work because in addition to mender-agent.pem, we need to update mender-store with record of key. Suggest adding option to mender-artifact modify: https://tracker.mender.io/browse/MEN-1902

### Mount the data partition of the disk image

Now that we have generated a key for the device and preauthorized it, we need to copy the generated *private* device key to our working disk image (it typically has the `.sdimg` suffix). We copy it to its default location `/mender/mender-agent.pem` on the data partition.

!!! There is a symlink from `/var/lib/mender/mender-agent.pem` on the root file systems to `/mender/mender-agent.pem` on the data partition, which we will leave in place. If the Mender client does not find a valid key it will generate one, which is not what we want when we are preauthorizing devices.

Follow the steps in [modifying a disk image](../../artifacts/modifying-a-disk-image) to find the start sector of the `data` partiton (typically `.sdimg4`).
Usually you will run a squence of commands similar to this:

```bash
fdisk -l -u mender-disk-image.sdimg
sudo mkdir /mnt/data
sudo mount -o loop,offset=$((512*933888)) mender-disk-image.sdimg /mnt/data
```

!!! Adjust the name of your disk image (`.sdimg`) file, and make sure to use the right offset. The offset `933888` is likely not correct for your setup and you need to look at the output from `fdisk` to determine yours. See [modifying a disk image](../../artifacts/modifying-a-disk-image) for more details.


### Copy the private device key

At this point the data partiton of the disk image should be mounted on `/mnt/data`. Find the location of the [private key we generated](#generate-a-client-keypair) and copy it into place on the data partiton by running the following commands:

```bash
sudo install -m 600 keys-client-generated/private.key /mnt/data/mender-agent.pem
```

### Unmount your data partition

To ensure the device private key is written to disk, unmount the data partition with the following command:

```bash
sudo umount /mnt/data
```


## Boot the device

Now provision the storage with this new disk image, just like you have done in the past. If you are using a SD card, insert it into your workstation and use a command similar to the following:

```bash
sudo dd if=<PATH-TO-IMAGE>.sdimg of=<DEVICE> bs=1M && sudo sync
```

Then insert the SD card back into your device.