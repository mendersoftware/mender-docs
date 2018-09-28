---
title: Example: Providing custom u-boot-fw-utils
taxonomy:
    category: docs
---

In this section we list a practical example of how to port a bitbake u-boot
recipe to a u-boot-fw-utils recipe. The latter is needed for Mender to operate
correctly, but is often omitted when a custom U-Boot fork is made.

For this example we assume that the U-Boot fork in question has a
`u-boot_<version>.bb` file. For our purpose we will use the stock u-boot recipe
from the Yocto Project (`u-boot_2016.03.bb` at the time of writing), and port
this to a recipe that produces the u-boot-fw-utils tools.

## Example setup

The example setup is only here for completeness' sake, to show how we did the
example, and are not relevant if you're porting a real u-boot recipe. Feel free
to proceed to the next section if this one doesn't apply to you.

First we create a new folder inside our private bitbake layer:

```bash
cd meta-my-layer
mkdir -p recipes-bsp/u-boot-my-fork
```

Then we copy the u-boot recipe from the Yocto Project:

```bash
cp ../meta/recipes-bsp/u-boot/u-boot_2016.03.bb recipes-bsp/u-boot-my-fork_2016.03.bb
```

In addition we need to change a few things inside the file. Expressed as a diff,
this is the change:

```
--- ../meta/recipes-bsp/u-boot/u-boot_2016.03.bb	2016-07-07 13:46:25.202889701 +0200
+++ recipes-bsp/u-boot-my-fork/u-boot-my-fork_2016.03.bb	2016-11-01 11:05:35.805292065 +0100
@@ -1,4 +1,5 @@
-require u-boot.inc
+require recipes-bsp/u-boot/u-boot.inc
+require recipes-bsp/u-boot/u-boot-mender.inc
 
 DEPENDS += "dtc-native"
 
```

The first line changes a path inside the recipe, since the include file is not
in the same directory anymore. The second adds Mender specific tweaks, as
described in [this section](../..#forks-of-u-boot).

## Preparations

Start by copying the u-boot recipe file to a new file for the fw-utils, like
this:

```bash
cd meta-my-layer/recipes-bsp/u-boot-my-fork
cp u-boot-my-fork_2016.03.bb u-boot-fw-utils-my-fork_2016.03.bb
```

## Using the fork

Then, in accordance with [this section](../../manual-u-boot-integration#u-boot-fw-utils), we add the
following to our configuration:

```bash
PREFERRED_PROVIDER_u-boot-fw-utils = "u-boot-fw-utils-my-fork"
PREFERRED_RPROVIDER_u-boot-fw-utils = "u-boot-fw-utils-my-fork"
```

For this example we add it to `local.conf`, but in a real situation it may be
more appropriate to add this to the `machine.conf` file for the board in
question.

## Adapting the recipe

Here is the complete set of changes made to the recipe, expressed as a diff. We
will go through each line and explain why they are needed.

<!--AUTOVERSION: "u-boot.git;branch=%"/ignore -->
```
--- u-boot-my-fork_2016.03.bb	2016-11-01 11:42:06.143094834 +0100
+++ u-boot-fw-utils-my-fork_2016.03.bb	2016-11-01 10:19:43.940934880 +0100
@@ -1,7 +1,10 @@
-require recipes-bsp/u-boot/u-boot.inc
-require recipes-bsp/u-boot/u-boot-mender.inc
+require recipes-bsp/u-boot/u-boot-fw-utils-mender.inc
 
-DEPENDS += "dtc-native"
+SUMMARY = "U-Boot bootloader fw_printenv/setenv utilities"
+LICENSE = "GPLv2+"
+LIC_FILES_CHKSUM = "file://Licenses/README;md5=a2c678cfd4a4d97135585cad908541c6"
+SECTION = "bootloader"
+DEPENDS = "mtd-utils"
 
 # This revision corresponds to the tag "v2016.03"
 # We use the revision in order to avoid having to fetch it from the
@@ -9,3 +12,30 @@
 SRCREV = "df61a74e6845ec9bdcdd48d2aff5e9c2c6debeaa"
 
 PV = "v2016.03+git${SRCPV}"
+
+SRC_URI = "git://git.denx.de/u-boot.git;branch=master"
+
+S = "${WORKDIR}/git"
+
+INSANE_SKIP_${PN} = "already-stripped"
+EXTRA_OEMAKE_class-target = 'CROSS_COMPILE=${TARGET_PREFIX} CC="${CC} ${CFLAGS} ${LDFLAGS}" V=1'
+
+inherit uboot-config
+
+do_compile () {
+	oe_runmake ${UBOOT_MACHINE}
+	oe_runmake env
+}
+
+do_install () {
+	install -d ${D}${base_sbindir}
+	install -d ${D}${sysconfdir}
+	install -m 755 ${S}/tools/env/fw_printenv ${D}${base_sbindir}/fw_printenv
+	install -m 755 ${S}/tools/env/fw_printenv ${D}${base_sbindir}/fw_setenv
+	install -m 0644 ${S}/tools/env/fw_env.config ${D}${sysconfdir}/fw_env.config
+}
+
+PACKAGE_ARCH = "${MACHINE_ARCH}"
+
+PROVIDES_${PN} = "u-boot-fw-utils"
+RPROVIDES_${PN} = "u-boot-fw-utils"
```

1. We remove the reference to `u-boot.inc`, because this file is only relevant
   for the main u-boot recipe, not for u-boot-fw-utils.

2. We replace `u-boot-mender.inc` with `u-boot-fw-utils-mender.inc`. This is
   because the fw-utils tools requires different tweaks, as described in [this
   section](../../manual-u-boot-integration#u-boot-fw-utils).

3. The next block of variable assignments (starting with `SUMMARY`) is added
   because this normally is provided by `u-boot.inc`, but since this file is not
   included anymore, we need to add these variables manually.

4. We next add the `SRC_URI` variable, since this also was present in
   `u-boot.inc`. Most likely this variable will already exist if the recipe was
   copied from a real fork of U-Boot, and will likely be different from our
   example. Using the one from `u-boot-my-fork_2016.03.bb` should be fine.

5. The `S` variable is added since it is missing after `u-boot.inc` was removed,
   and the build recipe expects the source directory to be structured like this.

6. `INSANE_SKIP_${PN}` is added because u-boot-fw-utils's build process strips
   the binaries automatically, and unless we add this option, Bitbake will
   complain if the binaries are already stripped.

7. `EXTRA_OEMAKE_class-target` is added because U-Boot needs these environment
   variables in order to cross compile correctly for our board. This string has
   been known to change, so if you get compile errors it's a good idea to check
   out the specific string for your version of U-Boot. Executing this search
   query in the poky repository is a good start:

   ```
   git log -p meta/recipes-bsp/u-boot/
   ```

   In the resulting pager, search for `EXTRA_OEMAKE_class-target`, and see how
   it has changed, and in which version it changed. Your string should match the
   one in poky for the same U-Boot version.

8. `inherit uboot-config` makes sure that the Bitbake variables for U-Boot are
   set correctly. Normally this is inherited by `u-boot.inc`, but we are not
   using it in this recipe.

9. The `do_compile` block is the heart of our u-boot-fw-utils recipe, and the
   key difference from the original recipe for u-boot is that we compile the
   `env` target. This will compile the fw-utils tools.

10. The `do_install` block needs to be defined because naturally, the
    u-boot-fw-utils recipe needs to have a different set of installables than
    u-boot, otherwise they would overlap. The three components needed are the
    two binary tools, `fw_printenv` and `fw_setenv`, as well as the
    configuration file, `fw_env.config`, which tells said tools where to find
    the U-Boot environment.

11. `PACKAGE_ARCH` is set to `${MACHINE_ARCH}` because this recipe will produce
    binaries that are specific to this board, and not to the architecture in
    general. This stems from the highly board specific nature of U-Boot. See
    [the official Yocto Project
    documentation](http://www.yoctoproject.org/docs/latest/mega-manual/mega-manual.html#var-PACKAGE_ARCH)
    for more information.

12. The last two `PROVIDES_${PN}` and `RPROVIDES_${PN}` variables are added to
    describe to Bitbake that this recipe provides those packages, even though it
    has a different name. This is described [here](../../manual-u-boot-integration#u-boot-fw-utils).

And that's it! This provides a working recipe for u-boot-fw-utils.

You may notice that the file looks very similar to the one that already exists
in the Yocto Project, under
`meta/recipes-bsp/u-boot/u-boot-fw-utils_2016.03.bb`, and this is indeed the
case. Much of the inspiration was taken from there, and this is a good place to
look if you hit problems and this guide doesn't provide the answer.

After the adaptation is complete, you should go through the [Integration
checklist](../../../yocto/integration-checklist) to make sure that all functionality
of the compiled tools is working.
