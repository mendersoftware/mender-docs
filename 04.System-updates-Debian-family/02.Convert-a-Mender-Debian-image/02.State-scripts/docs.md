---
title: State scripts
taxonomy:
    category: docs
---

## Add state scripts to an Artifact

To add state scripts to an Artifact with mender-convert, use the same method as for [other Artifact
customizations](../customization): The `mender_create_artifact` hook. In this hook, add `--script`
arguments to `mender-artifact` for each script you wish to add.

### Example

Take this example, which creates a `custom_config` file with a new hook:

```bash
cat <<- 'EOF' > configs/custom_config
mender_create_artifact() {
  local -r device_type="${1}"
  local -r artifact_name="${2}"
  mender_artifact=deploy/${device_type}-${artifact_name}.mender
  log_info "Running custom implementation of the 'mender_create_artifact' hook"
  log_info "Writing Mender artifact to: ${mender_artifact}"
  log_info "This can take up to 20 minutes depending on which compression method is used"
  run_and_log_cmd "mender-artifact --compression ${MENDER_ARTIFACT_COMPRESSION} \
      write rootfs-image \
      --file work/rootfs.img \
      --output-path ${mender_artifact} \
      --artifact-name ${artifact_name} \
      --device-type ${device_type} \
      --script my-state-scripts/ArtifactInstall_Enter_00" \

}
EOF
```
