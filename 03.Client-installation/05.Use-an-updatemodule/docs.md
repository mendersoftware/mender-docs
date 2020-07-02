---
title: Use an Update Module
taxonomy:
    category: docs
---

Let's assume that you need to change a single file on your devices. Performing
a full filesystem update in that case carries too much overhead both in size of
the artifact and time needed to handle it. Mender addresses this use case with
the idea of [Update Modules](../../02.Overview/15.Taxonomy/docs.md) (which we
have already mentioned [in the overview section](../../02.Overview/01.Introduction/docs.md#application-updates)).

The Update Modules are just executable files in _/usr/share/mender/modules/v3_
directory on the device (v3 is the current version of the protocol). The Mender
client executes them with defined set of parameters to [perform the update](link-to-page-with-state-machine-of-update-modules).
All update modules originate from the artifacts of [special payload and type](link-to-how-to-create-an-update-module-artifact).

The role of the client ends with the execution of the update module
in a correct moment, and with the correct arguments; the rest depends
on the implementation, Mender imposes no limits on what the update module code
can or cannot do. In order to create an update module, you need to first 
create the actual code of the module, and then create an artifact. You can
find some examples in the [mender-update-modules repository](https://github.com/mendersoftware/mender-update-modules).

Whether it is you need to install something onto your devices, update some files,
or perform some other operation of your choosing, the Update modules are
an option worth considering; they reduce the size of artifact, and time
of the deployment.
