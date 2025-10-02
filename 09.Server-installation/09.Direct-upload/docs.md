---
title: Direct Upload
taxonomy:
    category: docs
---

!!! Support for Direct Upload is available exclusively in the Mender Enterprise plan in the On Premise offering.
!!! See [the Mender plans page](https://mender.io/pricing/plans?target=_blank)
!!! for an overview of all Mender plans and features.

The Direct Upload feature provides a Mender channel to upload artifacts directly to the Mender artifact storage, processing it and putting it in the correct place and structure, without going through any other Mender component like the API gateway or deployments service.
This is an API/CLI feature only, and you can see the progress in the Mender Web UI only after the process completes successfully.
This feature drastically reduces the time to upload the Mender artifact to the Mender artifact storage, especially when uploading large artifacts (1TB for example), while also reducing the load on the Mender Server infrastructure.

## Prerequisites

<!--AUTOVERSION: "version %"/ignore-->
!!! This feature is available starting from the Mender Server version 3.6.3

* The `mender-cli` tool. You can find information about how to download it and the installation steps in the [Downloads section](../../12.Downloads/docs.md#mender-cli) from this documentation.

* To use the direct upload feature, the user must have at least the Deployments Manager and Releases Manager roles.

* Enable the feature on the server by applying the [helm charts](https://github.com/mendersoftware/mender-helm#complete-list-of-parameters) with:
    * `deployments.directUpload.enabled` to `true`
    * `deployments.directUpload.skipVerify` to `true`


## Upload process

For uploading a Mender Artifact you will need to have a session token. You can get one by running the following command:

```bash
mender-cli login
```

Or by passing the `--token` flag to the upload command. It can receive a [Personal Access Token (PAT)](../../10.Server-integration/01.Using-the-apis/docs.md#personal-access-tokens) or a Session token that can be retrieved from the Mender Web UI under "My Profile" section.

```bash
ARTIFACT_NAME="huge-artifact.mender"
SERVER_URL="https://foo.bar.com"
mender-cli artifacts --server $SERVER_URL upload --direct $ARTIFACT_NAME
```
