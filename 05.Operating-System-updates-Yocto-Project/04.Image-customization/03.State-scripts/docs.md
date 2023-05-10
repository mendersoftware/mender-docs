---
title: State scripts
taxonomy:
    category: docs
---

## Including state scripts in Artifacts and disk images

To include state scripts in Artifacts and images, create a new Yocto recipe that
inherits `mender-state-scripts` and copies them into place in `do_compile`,
using the
[${MENDER_STATE_SCRIPTS_DIR}](../../../05.Operating-System-updates-Yocto-Project/99.Variables/docs.md#mender_state_scripts_dir)
variable. This works for both [root filesystem and Artifact
scripts](../../../06.Artifact-creation/04.State-scripts/docs.md#root-filesystem-and-artifact-scripts).

<!--AUTOVERSION: "meta-mender/tree/%"/meta-mender-->
Take a look at the
[example-state-scripts](https://github.com/mendersoftware/meta-mender/tree/master/meta-mender-demo/recipes-mender/example-state-scripts?target=_blank)
recipe to get started.

!! If you add or remove a recipe containing state scripts to a build, you need
!! to clear the `tmp` directory of the Yocto build before building a new image.
!! An alternative is to call `bitbake -c clean <recipe>` with the affected
!! recipe, but the first method is recommended since it will cover all cases,
!! regardless of recipe name. Merely changing a recipe does not require this
!! step.
