---
title: CI/CD pipelines
taxonomy:
    category: docs
---

## CI/CD pipelines

Mender provides support for application updates in the form of CI/CD pipelines to implement all kinds of specific use-cases. This section describes possible ways to integrate your workflow with Mender and most popular CI/CD providers.

### Mender CI-workflows Docker image

To help you in creating CI/CD pipelines, we created [GitHub repository](https://github.com/mendersoftware/mender-ci-workflows/) containing ready to use, battle-tested CI/CD pipeline code snippets that can be used in your workflows. Additionally, we provide [mender-ci-tools Docker image](https://hub.docker.com/r/mendersoftware/mender-ci-tools) based on Alpine Linux and providing command-line utilities,`mender-artifact` and `mender-cli` installed.

To locally inspect the Docker image, pull it with the following command:
<!--AUTOVERSION: "mendersoftware/mender-ci-tools:%"/ignore-->
```
<!--AUTOVERSION: "mendersoftware/mender-ci-tools:%"/ignore-->
docker pull mendersoftware/mender-ci-tools:master
```

The Docker image definition and CI/CD templates can be found [here](https://github.com/mendersoftware/mender-ci-workflows).


### Supported CI/CD providers

Mender currently supports three major CI/CD providers:

* [GitHub Actions](01.GitHub-Actions/docs.md)
* [GitLab CI/CD](02.GitLab-CICD/docs.md)
* [Azure DevOps](03.Azure-DevOps/docs.md)

### Creating and Signing an Mender Artifact

This scenario uses `mender-artifact` tool to package your software as a Mender Artifact. A Mender Artifact can optionally be signed, so the examples provided allow for signing the Artifact too.


The input for the scenario is the software being packaged and the output is a Mender Artifact.


You can read about artifact creation details [here](../01.Create-an-Artifact/docs.md#create-a-full-filesystem-update-artifact).


More details about signing Mender Artifacts [here](https://docs.mender.io/artifact-creation/sign-and-verify).

### Uploading an Mender Artifact

This scenario uses `mender-cli` tool to upload your Mender Artifact to the Mender server. 

The input for the scenario is the Mender Artifact generated in the previous stage, and the output is upload result.

You can read about uploading the Mender Artifact to the file storage [here](../../08.Server-integration/01.Using-the-apis/docs.md#set-up-mender-cli).

You can use [Personal Access Tokens](../../08.Server-integration/01.Using-the-apis/docs.md#personal-access-tokens) with necessary permissions to perform automated actions on Mender server on your behalf.

### Deploying an Artifact to the fleet of devices

This scenario uses the Mender server API to trigger a deployment on your fleet.

The inputs for this scenario are the device group to deploy on and previously uploaded Mender Artifact, and the output is the deployment result.
