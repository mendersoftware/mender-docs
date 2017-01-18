---
title: Building for production
taxonomy:
    category: docs
---

This section describes the steps that are specific to production builds. This is not necessary if you're just trying out Mender, but are necessary before deploying to production.


## Removal of demo layer

When building for production, we need to remove the demo layer, `meta-mender-demo`, because its settings are inappropriate for production devices. Assuming you are still in the `build` directory, this command will remove the demo layer:

```bash
bitbake-layers remove-layer ../meta-mender/meta-mender-demo
```


## Certificates

Certificates are used to ensure the communication between the client and the server is secure, so that it is not possible for an adversary to pose as a legitimate server.

### Preparing the client certificates

The Mender client needs two certificates, one for the API gateway, and one for the storage server. This section assumes that you have followed the guide for [generating certificates](../../Administration/Certificates-and-keys#generating-new-keys-and-certificates), but is also valid if you have obtained the certificates in a different way; just make sure to adjust the paths accordingly.

Both certificates are hosted in a single file which the client reads. To prepare this file, run the following in the folder where you have your generated certificates:

```
cat ./keys-generated/api-gateway/certificate.pem ./keys-generated/storage-proxy/certificate.pem > server.crt
```

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
