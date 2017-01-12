---
title: Building for production
taxonomy:
    category: docs
---

This section describes the steps that are specific to production builds. This is not necessary if you're just trying out Mender, but are necessary before deploying to production.


## Removal of demo layer

When building for production, we need to remove the demo layer, meta-mender-demo, because its settings are inappropriate for production devices. Assuming you are still in the `build` directory, this command will remove the demo layer:

```
bitbake-layers remove-layer ../meta-mender/meta-mender-demo
```


## Certificates

Having a certificate is necessary to make sure that the communication between the client and the server is secure, and that it is not possible for an adversary to pose as a legitimate server. You will need to use the same certificate as the API gateway uses. See the section about [administering certificates](../../Administration/Certificates) for more details.

The best way to include the certificate in the client build is to use custom bitbake layer. For the following steps it is assumed that you have such a layer already. If not you can check out how to [create your own layer](http://www.yoctoproject.org/docs/latest/mega-manual/mega-manual.html#creating-your-own-layer) in the official Yocto Project documentation, but there is also an alternative method below that doesn't need a layer.

### Using layer

Put the certificate inside your own layer, under `recipes-mender/mender/files/server.crt`. Then create the file `recipes-mender/mender/mender_%.bbappend`. Inside this file, add the following content:

```
FILESEXTRAPATHS_prepend := "${THISDIR}/files:"
SRC_URI_append = " file://server.crt"
```

This will make sure that the correct certificate is included in the build.

### Using local.conf

If you don't have a custom layer, you can also specify the certificate directly in `local.conf`. Note however, that the recommended way is to use a layer in the way described above, since it fits better with the bitbake workflow.

To add the certificate using `local.conf`, first make sure that the certificate has the name `server.crt`, and is stored somewhere accessible to the build. Then add the following to `local.conf`:

```
FILESEXTRAPATHS_prepend_pn-mender := "<DIRECTORY-CONTAINING-server.crt>:"
SRC_URI_append_pn-mender = " file://server.crt"
```

Note in particular the `:` after the directory; this is mandatory.
