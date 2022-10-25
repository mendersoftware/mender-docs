---
title: GitHub Actions
taxonomy:
    category: reference
---

A pre-built container image `mendersoftware/mender-ci-tools` including the `mender-cli` and `mender-artifact` tools is provided. The image can be used for building Mender artifacts from GitHub Actions jobs and (optionally) uploading them to a Mender server.

## GitHub Actions

!!!!! Only modern Mender backend versions with [Personal Access Tokens](../../01.Using-the-apis/docs.md#personal-access-tokens) functionality in place are supported by the actions

### Setup
The actions require the following secret is set in a repository settings:
- `MENDER_SERVER_ACCESS_TOKEN`: Mender [Personal Access Token](../../01.Using-the-apis/docs.md#personal-access-tokens)

### Upload Artifact
`mender-gh-action-upload-artifact` action ([mendersoftware/mender-gh-action-upload-artifact@main](https://github.com/mendersoftware/mender-gh-action-upload-artifact)) uploads a Mender artifact to a Mender server.

### Create Deployment
`mender-gh-action-create-deployment` action ([mendersoftware/mender-gh-action-create-deployment@main](https://github.com/mendersoftware/mender-gh-action-create-deployment)) creates a deployment on a Mender server.

## Pipeline Examples
Pipeline eximples can be found in [mender-ci-workflows](https://github.com/mendersoftware/mender-ci-workflows/tree/master/examples/github) GitHub repository.
