---
title: GitLab CI/CD
taxonomy:
    category: docs
    label: tutorial
---

## Job templates
<!--AUTOVERSION: "tree/%/templates"/mender-ci-workflows-->
In addition to the [mender-ci-tools Docker image](../docs.md#mender-ci-workflows-docker-image), Mender provides [job templates](https://github.com/mendersoftware/mender-ci-workflows/tree/master/templates/gitlab) for uploading Mender Artifacts and creating deployments to a group of devices.

<!--AUTOVERSION: "Mender server version % or"/ignore-->
!!!!! The jobs use [Personal Access Tokens](../../../08.Server-integration/01.Using-the-apis/docs.md#personal-access-tokens) feature which is only available in Mender server version 3.4 or newer.

In this chapter we introduce the different jobs and provide [examples](#pipelines-examples) on how to use them.

### Upload Mender Artifact job
<!--AUTOVERSION: "tree/%/templates"/mender-ci-workflows-->
[.mender:upload:artifact](https://github.com/mendersoftware/mender-ci-workflows/tree/master/templates/gitlab/mender-artifact-upload.gitlab-ci.yml) job template uploads a Mender Artifact to a Mender server.

### Create deployment job
<!--AUTOVERSION: "tree/%/templates"/mender-ci-workflows-->
[.mender:create:deployment](https://github.com/mendersoftware/mender-ci-workflows/tree/master/templates/gitlab/mender-deployment-create.gitlab-ci.yml) job template creates a deployment on a Mender server.

### Setup
The job templates require the following CI variable to be set in the repository settings:

!!!!! Make sure to protect the variable accordingly

- `MENDER_SERVER_ACCESS_TOKEN`: Mender [Personal Access Token](../../../08.Server-integration/01.Using-the-apis/docs.md#personal-access-tokens)

## Pipelines examples

* [Build and deploy Mender Artifact](#build-and-deploy-mender-artifact)
* [Build and deploy multiple Mender Artifacts](#build-and-deploy-multiple-mender-artifacts)
* [Build and deploy Mender Artifact to a single device](#build-and-deploy-mender-artifact-to-a-single-device)

### Build and deploy Mender Artifact
<!--AUTOVERSION: "tree/%/examples"/mender-ci-workflows-->
```bash
@build-and-deploy-mender-artifact.gitlab-ci.yml@ # https://github.com/mendersoftware/mender-ci-workflows/tree/master/examples/gitlab/build-and-deploy-mender-artifact.gitlab-ci.yml
```

### Build and deploy multiple Mender Artifacts
<!--AUTOVERSION: "tree/%/examples"/mender-ci-workflows-->
```bash
@build-two-artifacts.gitlab-ci.yml@ # https://github.com/mendersoftware/mender-ci-workflows/tree/master/examples/gitlab/build-two-artifacts.gitlab-ci.yml
```

### Build and deploy Mender Artifact to a single device
<!--AUTOVERSION: "tree/%/examples"/mender-ci-workflows-->
```bash
@deploy-to-a-single-device.gitlab-ci.yml@ # https://github.com/mendersoftware/mender-ci-workflows/tree/master/examples/gitlab/deploy-to-a-single-device.gitlab-ci.yml
```
