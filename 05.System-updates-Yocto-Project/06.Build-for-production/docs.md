---
title: Building for production
taxonomy:
    category: docs
    label: tutorial
---

This section describes the steps that are specific to production builds for
Yocto Project. These steps are not necessary if you are trying Mender in demo
mode.

## Remove demo layer

When building for production, we need to remove the demo layer, `meta-mender-demo`, because its settings are inappropriate for production devices. Assuming you are still in the `build` directory, this command will remove the demo layer:

```bash
bitbake-layers remove-layer ../meta-mender/meta-mender-demo
```

!!! Note that in case the above does not work you might want to check the included layers with
```bash
bitbake-layers show-layers
```
and then remove the demo layer e.g.
```bash
bitbake-layers remove-layer meta-mender-demo
```

## Configure polling intervals

For security reasons, the Mender client does not require any open ports at the embedded device. Therefore, all communication between the Mender client and the server is always initiated by the client and it is important to configure the client so that the frequency of sending various requests to the server is reasonable for a given setup.

Please refer to [polling intervals](../../03.Client-installation/07.Configuration-file/01.Polling-intervals/docs.md), for information on how to choose and how to set polling intervals.

## Certificates

Certificates ensure the communication between the client and the server is
secure, so that it is not possible for an adversary to pose as a legitimate
server.

!! Please make sure your device has its clock synced correctly. Otherwise certificate
!! verification will not succeed. See
!! [certificate troubleshooting](../../301.Troubleshoot/03.Mender-Client/docs.md#certificate-expired-or-not-yet-valid)
!! for more information.


### Preparing the server certificates on the client

You can either generate new certificates by following the tutorial for
[generating
certificates](../../07.Server-installation/05.Certificates-and-keys/docs.md),
or obtain the certificates in a different way - for example from your existing
Certificate Authority. In either case the certificates on the client and server
must be the same.


Including the server certificate on the client is only necessary if the certificate is
not signed by known Certificate Authority (CA), for example if the certificate is
[self-signed](https://en.wikipedia.org/wiki/Self-signed_certificate?target=_blank).
If signed by a known CA, the remainder of this section is not necessary.

If you generated new certificates, this file is available at `keys-generated/cert/cert.crt`.

The best way to include the certificate in the client build is to use a custom
bitbake layer. The following steps assume that you already have a custom layer
included in your build. If not you can check out how to [create your own
layer](https://docs.yoctoproject.org/dev-manual/common-tasks.html?target=_blank#creating-your-own-layer)
in the official Yocto Project documentation, and there is also an alternative
method below that does not require a separate layer.

#### Using a layer

Put the certificate inside your own layer, under
`recipes-mender/mender-server-certificate/files/server.crt`. Then create the
file
`recipes-mender/mender-server-certificate/mender-server-certificate.bbappend`.
Inside this file, add the following content:

```bash
FILESEXTRAPATHS:prepend := "${THISDIR}/files:"
SRC_URI:append = " file://server.crt"
```

Next, install `mender-server-certificate` package into your image by adding to
your `conf/layer.conf` the following content:

```bash
IMAGE_INSTALL:append = " mender-server-certificate"
```

This will make sure that the correct certificate is included in the build.

#### Using local.conf

If you do not have a custom layer, you can also specify the certificate directly in `local.conf`. However, note that the recommended way is to use a layer in the way described above since it fits better with the bitbake workflow.

To add the certificate using `local.conf`, first make sure that the certificate has the name `server.crt`, and is stored somewhere accessible to the build. Then add the following to `local.conf`:

```bash
FILESEXTRAPATHS:prepend:pn-mender-server-certificate := "<DIRECTORY-CONTAINING-server.crt>:"
SRC_URI:append:pn-mender-server-certificate = " file://server.crt"
IMAGE_INSTALL:append = " mender-server-certificate"
```

Note in particular the `:` after the directory; this is mandatory.

### Updating MENDER_SERVER_URL

Please note that setting up for production will require that you explicitly set the [MENDER_SERVER_URL variable](../99.Variables/docs.md#mender_server_url) to the proper value for your server.

!!! Note that, this step is not required for the [standalone mode](../../03.Client-installation/07.Configuration-file/01.Polling-intervals/docs.md).

## Artifact signing and verification keys

The private key used for signing the Mender Artifact should be protected and kept outside of the build system,
thus there are no extra steps needed to add it to any part of the build system, Mender Client nor Server.

The Mender Client requires having the public key stored on the device to verify
the Mender Artifact signatures. The best way to include a public key in the
client is to add it to your own layer. Set the name of the verification key to
`artifact-verify-key.pem` and append it to `SRC_URI` of the `mender-client` application
before building the Yocto client image. For example:

```bash
FILESEXTRAPATHS:prepend := "${THISDIR}/files:"
SRC_URI:append = " file://artifact-verify-key.pem"
```

Note that it is also possible (but not recommended) to use `local.conf`, by using [the same method as for client certificates](#using-local-conf), adding `pn-mender-client` to the variable names.

For more information about some alternate approaches please follow the [MENDER_ARTIFACT_VERIFY_KEY documentation](../99.Variables/docs.md#mender_artifact_verify_key).
