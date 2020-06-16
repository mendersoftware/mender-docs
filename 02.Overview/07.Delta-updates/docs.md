---
title: Delta updates
taxonomy:
    category: docs
---

A delta update is a way of installing a full rootfs-update, with the payload
encoded as a binary differential update. This means that only the difference
between the new and the old root filesystem is transmitted to the device. A
delta update is therefore significantly smaller than a regular update. In every
other regard, this is the same as doing a full rootfs-update, with atomicity,
integrity, rollback and signature support included.

This gives significant saving in both bandwidth and install time. This is due to
the network only has to transfer a small percentage of the full file size.
Installation is also faster in general, as the delta installation will only
write the needed blocks, and not the whole update, if it is not required to.

A delta update targets a specific base-image. This means that a delta-update
only works with devices running a specific image. The Mender server resolves
which devices are available for a delta update through information about the
base-images on the devices, before you are able to deploy the update. This way,
only devices which are compatible with the delta update will receive the update.

See the [Mender hub](https://hub.mender.io?target=_blank) article on [delta
updates ](https://hub.mender.io/t/robust-delta-update-rootfs/1144?target=_blank)
for more information.
