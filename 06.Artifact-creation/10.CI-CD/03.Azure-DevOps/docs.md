---
title: Azure DevOps
taxonomy:
    category: docs
    label: tutorial
---

## Stage templates
<!--AUTOVERSION: "tree/%/templates"/mender-ci-workflows-->
In addition to the [mender-ci-tools Docker image](../docs.md#mender-ci-workflows-docker-image), Mender provides [stage templates](https://github.com/mendersoftware/mender-ci-workflows/tree/master/templates/azure) for uploading Mender Artifacts and creating deployments to a group of devices.

<!--AUTOVERSION: "Mender server version % or"/ignore-->
!!!!! The templates use [Personal Access Tokens](../../../08.Server-integration/01.Using-the-apis/docs.md#personal-access-tokens) feature which is only available in Mender server version 3.4 or newer.

In this chapter we introduce the different stages and provide [examples](#pipelines-examples) on how to use them.

### Upload Mender Artifact
<!--AUTOVERSION: "tree/%/templates"/mender-ci-workflows-->
[Upload Mender Artifact](https://github.com/mendersoftware/mender-ci-workflows/tree/master/templates/azure/mender-artifact-upload.yml) stage template uploads a Mender Artifact to a Mender server.

The template has the following parameters:
- `mender_uri`: Mender server's URL (default: https://hosted.mender.io)
- `mender_pat`: Mender Personal Access Token (read the [documentation](https://docs.mender.io/server-integration/using-the-apis#personal-access-tokens) for more information)
- `mender_artifact`: Path of Mender Artifact file, relative to `$(System.DefaultWorkingDirectory)`

### Create deployment job
<!--AUTOVERSION: "tree/%/templates"/mender-ci-workflows-->
[Create deployment on Mender server](https://github.com/mendersoftware/mender-ci-workflows/tree/master/templates/azure/mender-deployment-create.yml) stage template creates a deployment on a Mender server.

The template has the following parameters:
- `mender_uri`: Mender server's URL (default: https://hosted.mender.io).
- `mender_pat`: Mender Personal Access Token (read the [documentation](https://docs.mender.io/server-integration/using-the-apis#personal-access-tokens) for more information).
- `mender_deployment_name`: Mender deployment's name.
- `mender_release_name`: Mender release's name.
- `mender_devices_list`: The list of Mender devices a deployment will be triggered to.
- `mender_deployment_group`: The name of the Mender devices group your deployment will target. One of `mender_deployment_group` or `mender_devices_list` is required. `mender_devices_list` takes the priority if both are set.

## Pipelines examples

### Build and deploy Mender Artifact
<!--AUTOVERSION: "tree/%/examples"/mender-ci-workflows-->
```bash
@build-and-deploy-mender-artifact.yml@ # https://github.com/mendersoftware/mender-ci-workflows/tree/master/examples/azure/build-and-deploy-mender-artifact.yml
```

### Build and deploy multiple Mender Artifacts
<!--AUTOVERSION: "tree/%/examples"/mender-ci-workflows-->
```bash
@build-and-deploy-multiple-artifacts.yml@ # https://github.com/mendersoftware/mender-ci-workflows/tree/master/examples/azure/build-and-deploy-multiple-artifacts.yml
```

### Build and deploy Mender Artifact to a single device
<!--AUTOVERSION: "tree/%/examples"/mender-ci-workflows-->
```bash
@deploy-to-a-single-device.yml@ # https://github.com/mendersoftware/mender-ci-workflows/tree/master/examples/azure/deploy-to-a-single-device.yml
```
