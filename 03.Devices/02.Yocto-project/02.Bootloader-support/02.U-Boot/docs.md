---
title: U-Boot
taxonomy:
    category: docs
---

This section describes the steps needed to integrate with U-Boot for Yocto Project. Most steps are automated, but there are a few things that need to be in place for this to function.

!!! Please consult [the bootloader support section](../../../01.General-system-requirements/docs.md#bootloader-support) to find out if U-Boot is supported on your platform and build configuration, and whether it is enabled by default.


## Enabling U-Boot

If U-Boot integration is not already enabled, you can enable it by adding the snippet below to your build configuration. For instance, in your `local.conf`:

```
MENDER_FEATURES_ENABLE_append = " mender-uboot mender-image-sd"
MENDER_FEATURES_DISABLE_append = " mender-grub mender-image-uefi"
```

See [the documentation on features](../../../../04.Artifacts/10.Yocto-project/02.Image-configuration/01.Features/docs.md) for more information.


## Boot counter

As Mender relies on the `CONFIG_BOOTCOUNT_ENV` feature of U-Boot, which was [introduced in October 2013](http://lists.denx.de/pipermail/u-boot/2013-October/165484.html?target=_blank), Mender currently recommends **U-Boot v2014.07 or newer**.

If you have an older version of U-Boot, it is possible to apply some extra patches to make this work. Please see the section about [U-Boot versions without BOOTLIMIT support]() for more information.

## Forks of U-boot

If the project is using a board supported by upstream U-Boot, and the build is
using the `u-boot` recipe as the bootloader provider, then you can skip to [the
next section](#enabling-u-boot). You can check if the board is using a u-boot
fork with the following command (must be executed in the Yocto build directory):

```
bitbake -e core-image-minimal | egrep '^PREFERRED_PROVIDER_(virtual/bootloader|u-boot)='
```

If any variables appear, and any one of them has a value other than `u-boot` or
empty, then the build is using a U-Boot fork.

If the project is using a fork of U-Boot, some additional steps are
required. Typically this happens if one of the layers the project depends on has
its own `u-boot-<suffix>` recipe somewhere. If so you need to carry out these
steps:

1. The recipe needs to include `u-boot-mender.inc`, in order to incorporate the
   patches needed for Mender to work. This should go into the `.bb` file of the
   recipe for the U-Boot fork:

   ```bash
   require recipes-bsp/u-boot/u-boot-mender.inc
   ```

2. Mender has a dependency on `u-boot`, but the project's U-Boot likely has
   another name, therefore it is important to mark the project's fork as a
   component that provides `u-boot`. The example below shows how to add the
   needed directives in the `.bb` file of the U-Boot fork.

   ```bash
   PROVIDES += "u-boot"
   RPROVIDES_${PN} += "u-boot"
   ```

3. In the machine section of the board in question, the actual u-boot
   implementation must be selected using `PREFERRED_PROVIDER`, like this:

   ```bash
   PREFERRED_PROVIDER_u-boot = "u-boot-my-fork"
   ```

   Many machine configurations will probably have this in their setup already.

## Enabling U-Boot

To utilize Mender's integration with U-Boot, when building with the Yocto
Project you need to enable the `mender-uboot` feature using
`MENDER_FEATURES_ENABLE`. For instance, in your `local.conf`:

```bash
MENDER_FEATURES_ENABLE_append = " mender-uboot"
```

!!! If the architecture is ARM, and the `mender-full` or `mender-full-ubi` class is inherited in a Bitbake `.conf` file, then the `mender-uboot` feature is already on by default. See [the documentation on features](../../../../04.Artifacts/10.Yocto-project/02.Image-configuration/01.Features/docs.md) for more information.

This enables U-Boot integration, and also enables full automatic patching of
U-Boot.

! Automatic U-Boot patching is only available if certain criteria are met. See below.

In order for automatic U-Boot patching to be used, the build must fulfill these
criteria:

<!--AUTOVERSION: "\"%\" branch or a later branch"/ignore-->
* The build must be using the "rocko" branch or a later branch from the Yocto
  Project (Yocto Project version 2.4 or later)

* The board must be using MMC/SD card storage, or more formally: It must be
  using `sdimg` as the image type to be flashed

Unfortunately, because of the great variation in U-Boot board code, the
automatic patching process does not always succeed or produce a working boot
loader, even if the above criteria are met. The symptoms are either that one of
the `u-boot` recipes produce compile errors, or that the board does not boot
using the modified bootloader. If this happens, or if you are using an older
Yocto Project branch, there will be some manual work required in order to
produce a working integration patch.

Please see [Manual U-Boot integration]() for more
information.
