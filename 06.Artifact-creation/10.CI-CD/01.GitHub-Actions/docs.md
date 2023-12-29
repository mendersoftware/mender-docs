---
title: GitHub Actions
taxonomy:
    category: docs
    label: tutorial
---

## Custom actions
Mender provides actions for uploading Mender Artifacts and creating deployments to a group of devices. Both actions are [composite](https://docs.github.com/en/actions/creating-actions/creating-a-composite-action) and require `bash` and `curl` to be available in a used container.

<!--AUTOVERSION: "Mender Server version % or"/ignore-->
!!!!! The actions use [Personal Access Tokens](../../../08.Server-integration/01.Using-the-apis/docs.md#personal-access-tokens) feature which is only available in Mender Server version 3.4 or newer.

In this chapter we introduce the different actions and provide [examples](#pipelines-examples) on how to use them.

### Upload a Mender Artifact action
`mendersoftware/mender-gh-action-upload-artifact` action uploads a Mender Artifact to a Mender Server. Find more information about the action usage in the related [documentation](https://github.com/mendersoftware/mender-gh-action-upload-artifact).

### Create a deployment action
`mendersoftware/mender-gh-action-create-deployment` action creates a deployment on a Mender Server. Find more information about the action usage in the related [documentation](https://github.com/mendersoftware/mender-gh-action-create-deployment).

### Setup
The actions require the following secret to be set in a repository settings:
- `MENDER_SERVER_ACCESS_TOKEN`: Mender [Personal Access Token](../../../08.Server-integration/01.Using-the-apis/docs.md#personal-access-tokens)

## Pipelines examples

* [Build and deploy Mender Artifact](#build-and-deploy-a-mender-artifact)
* [Build and deploy multiple Mender Artifacts](#build-and-deploy-multiple-mender-artifacts)
* [Build and deploy Mender Artifact to a single device](#build-and-deploy-a-mender-artifact-to-a-single-device)

### Build and deploy a Mender Artifact
<!--AUTOVERSION: "tree/%/examples"/mender-ci-workflows-->
```bash
@build-and-deploy-mender-artifact.yml@ # https://github.com/mendersoftware/mender-ci-workflows/tree/master/examples/github/build-and-deploy-mender-artifact.yml
```

### Build and deploy multiple Mender Artifacts
<!--AUTOVERSION: "tree/%/examples"/mender-ci-workflows-->
```bash
@build-and-deploy-multiple-artifacts.yml@ # https://github.com/mendersoftware/mender-ci-workflows/tree/master/examples/github/build-and-deploy-multiple-artifacts.yml
```

### Build and deploy a Mender Artifact to a single device
<!--AUTOVERSION: "tree/%/examples"/mender-ci-workflows-->
```bash
@deploy-to-a-single-device.yml@ # https://github.com/mendersoftware/mender-ci-workflows/tree/master/examples/github/deploy-to-a-single-device.yml
```
