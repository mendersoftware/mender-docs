---
title: Building for production
taxonomy:
    category: docs
---

This section describes the steps that are specific to production builds.
These steps are not necessary if you are just trying out Mender, but must be done before deploying to production.


## Removal of demo layer

When building for production, we need to remove the demo layer, `meta-mender-demo`, because its settings are inappropriate for production devices. Assuming you are still in the `build` directory, this command will remove the demo layer:

```bash
bitbake-layers remove-layer ../meta-mender/meta-mender-demo
```


## Certificates

Certificates are used to ensure the communication between the client and the server is secure, so that it is not possible for an adversary to pose as a legitimate server.

!! Please make sure that the clock is set correctly on your devices. Otherwise certificate verification will become unreliable. See [certificate troubleshooting](../../troubleshooting/mender-client#certificate-expired-or-not-yet-valid) for more information.


### Preparing the client certificates

You can either generate new certificates by following the guide for [generating certificates](../../administration/certificates-and-keys#generating-new-keys-and-certificates), or obtain the certificates in a different way - for example from your existing Certificate Authority. In either case the certificates on the client and server must be the same.

All certificates are hosted in a single file `server.crt` which the client reads. If you generated new certificates, this file is available at `keys-generated/certs/server.crt`.

!!! If you obtained your certificates in a different way, e.g. from your Certificate Authority, you need to concatenate the certificates from the API Gateway and Storage Proxy into one file by running a command similar to `cat api-gateway/cert.crt storage-proxy/cert.crt > server.crt`.

The `server.crt` file will be the certificate file to use on the client.

### Including the client certificates

The best way to include the certificate in the client build is to use a custom bitbake layer. For the following steps it is assumed that you have such a layer already. If not you can check out how to [create your own layer](http://www.yoctoproject.org/docs/latest/mega-manual/mega-manual.html?target=_blank#creating-your-own-layer) in the official Yocto Project documentation, and there is also an alternative method below that does not require a separate layer.

#### Using a layer

Put the certificate inside your own layer, under `recipes-mender/mender/files/server.crt`. Then create the file `recipes-mender/mender/mender_%.bbappend`. Inside this file, add the following content:

```bash
FILESEXTRAPATHS_prepend := "${THISDIR}/files:"
SRC_URI_append = " file://server.crt"
```

This will make sure that the correct certificate is included in the build.

#### Using local.conf

If you do not have a custom layer, you can also specify the certificate directly in `local.conf`. However, note that the recommended way is to use a layer in the way described above since it fits better with the bitbake workflow.

To add the certificate using `local.conf`, first make sure that the certificate has the name `server.crt`, and is stored somewhere accessible to the build. Then add the following to `local.conf`:

```bash
FILESEXTRAPATHS_prepend_pn-mender := "<DIRECTORY-CONTAINING-server.crt>:"
SRC_URI_append_pn-mender = " file://server.crt"
```

Note in particular the `:` after the directory; this is mandatory.


## Artifact signing and verification keys

The private key used for signing the Mender Artifact should be protected and kept outside of the build system, thus there are no extra steps needed to add it to any part of the build system or either Client or the Server environment. Only the public key, which is used by the Mender Client to verify the signed Artifact must be included in the Client build. 
The best way to include a public verification key in the client is to add it to your own layer. Set the name of the verification key to `artifact-verify-key.pem` and append it to `SRC_URI` of the `mender` application before building the Yocto client image. For example:

```bash
FILESEXTRAPATHS_prepend := "${THISDIR}/files:"
SRC_URI_append = " file://artifact-verify-key.pem"
```

Note that it is also possible (but not recommended) to use `local.conf`, by using [the same method as for client certificates](#using-localconf), adding `pn-mender` to the variable names.

For more information about some alternate approaches please follow [MENDER_ARTIFACT_VERIFY_KEY documentation](../Variables#mender-artifact-verify-key)).
