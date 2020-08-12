---
title: Deployments
taxonomy:
    category: docs
api: true
template: docs
---

<a name="overview"></a>
## Overview
An API for deployments and artifacts management.
Intended for use by the web GUI.


### Version information
*Version* : 1


### URI scheme
*Host* : hosted.mender.io  
*BasePath* : /api/management/v1/deployments  
*Schemes* : HTTPS




<a name="paths"></a>
## Paths
- [POST/artifacts](#artifacts-post)
- [GET/artifacts](#artifacts-get)
- [POST/artifacts/generate](#artifacts-generate-post)
- [GET/artifacts/{id}](#artifacts-id-get)
- [PUT/artifacts/{id}](#artifacts-id-put)
- [DELETE/artifacts/{id}](#artifacts-id-delete)
- [GET/artifacts/{id}/download](#artifacts-id-download-get)
- [POST/deployments](#deployments-post)
- [GET/deployments](#deployments-get)
- [DELETE/deployments/devices/{id}](#deployments-devices-id-delete)
- [GET/deployments/releases](#deployments-releases-get)
- [GET/deployments/{deployment_id}/devices](#deployments-deployment_id-devices-get)
- [GET/deployments/{deployment_id}/devices/{device_id}/log](#deployments-deployment_id-devices-device_id-log-get)
- [GET/deployments/{deployment_id}/statistics](#deployments-deployment_id-statistics-get)
- [PUT/deployments/{deployment_id}/status](#deployments-deployment_id-status-put)
- [GET/deployments/{id}](#deployments-id-get)
- [GET/deployments/{id}/device_list](#deployments-id-device_list-get)
- [GET/limits/storage](#limits-storage-get)


___
<a name="artifacts-post"></a>
### Upload mender artifact
```
POST /artifacts
```


#### Description
Upload mender artifact. Multipart request with meta and artifact.

Supports artifact (versions v1, v2)[https://docs.mender.io/development/architecture/mender-artifacts#versions].


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**FormData**|**artifact**  <br>*required*|Artifact. It has to be the last part of request.|file|
|**FormData**|**description**  <br>*optional*| |string|
|**FormData**|**size**  <br>*optional*|Size of the artifact file in bytes.<br>DEPRECATED: Size is determined from uploaded content.|integer (long)|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**201**|Artifact uploaded.  <br>**Headers** :   <br>`Location` (string) : URL of the newly uploaded artifact.|No Content|
|**400**|Invalid Request.|[Error](#error)|
|**500**|Internal Server Error.|[Error](#error)|


#### Consumes

* `multipart/form-data`


#### Produces

* `application/json`


#### Example HTTP response

##### Response 400
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 500
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```
___

<a name="artifacts-get"></a>
### List known artifacts
```
GET /artifacts
```


#### Description
Returns a collection of all artifacts.


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|OK|< [Artifact](#artifact) > array|
|**500**|Internal Server Error.|[Error](#error)|


#### Produces

* `application/json`


#### Example HTTP response

##### Response 200
```json
[ {
  "name" : "Application 1.0.0",
  "description" : "Johns Monday test build",
  "device_types_compatible" : [ "Beagle Bone" ],
  "id" : "0c13a0e6-6b63-475d-8260-ee42a590e8ff",
  "signed" : false,
  "modified" : "2016-03-11T13:03:17.063493443Z",
  "info" : {
    "type_info" : {
      "type" : "rootfs"
    }
  },
  "files" : [ {
    "name" : "rootfs-image-1",
    "checksum" : "cc436f982bc60a8255fe1926a450db5f195a19ad",
    "size" : 123,
    "date" : "2016-03-11T13:03:17.063+0000"
  } ],
  "metadata" : { }
} ]
```


##### Response 500
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```
___

<a name="artifacts-generate-post"></a>
### Upload raw data to generate a new artifact
```
POST /artifacts/generate
```


#### Description
Generate a new Mender artifact from raw data and meta data. Multipart request with meta and raw file.
Supports generating single-file updates only, using the single file upload module. [https://hub.mender.io/t/single-file/486]:


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**FormData**|**args**  <br>*optional*|Type-specific arguments used to generate the artifact.|string|
|**FormData**|**description**  <br>*optional*|Description of the artifact to generate.|string|
|**FormData**|**device_types_compatible**  <br>*optional*|An array of compatible device types.|< string > array(csv)|
|**FormData**|**file**  <br>*required*|Raw file to be used to generate the artifact. It has to be the last part of request.|file|
|**FormData**|**name**  <br>*required*|Name of the artifact to generate.|string|
|**FormData**|**type**  <br>*required*|Update module used to generate the artifact.|enum (single_file)|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**201**|Artifact generation request accepted and queued for processing.  <br>**Headers** :   <br>`Location` (string) : URL of the artifact going to be generated.|No Content|
|**400**|Invalid Request.|[Error](#error)|
|**500**|Internal Server Error.|[Error](#error)|


#### Consumes

* `multipart/form-data`


#### Produces

* `application/json`


#### Example HTTP response

##### Response 400
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 500
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```
___

<a name="artifacts-id-get"></a>
### Get the details of a selected artifact
```
GET /artifacts/{id}
```


#### Description
Returns the details of a selected artifact.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**id**  <br>*required*|Artifact identifier.|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Successful response.|[Artifact](#artifact)|
|**400**|Invalid Request.|[Error](#error)|
|**404**|Not Found.|[Error](#error)|
|**500**|Internal Server Error.|[Error](#error)|


#### Produces

* `application/json`


#### Example HTTP response

##### Response 200
```json
{
  "name" : "Application 1.0.0",
  "description" : "Johns Monday test build",
  "device_types_compatible" : [ "Beagle Bone" ],
  "id" : "0c13a0e6-6b63-475d-8260-ee42a590e8ff",
  "signed" : false,
  "modified" : "2016-03-11T13:03:17.063493443Z",
  "info" : {
    "type_info" : {
      "type" : "rootfs"
    }
  },
  "files" : [ {
    "name" : "rootfs-image-1",
    "checksum" : "cc436f982bc60a8255fe1926a450db5f195a19ad",
    "size" : 123,
    "date" : "2016-03-11T13:03:17.063+0000"
  } ],
  "metadata" : { }
}
```


##### Response 400
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 404
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 500
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```
___

<a name="artifacts-id-put"></a>
### Update description of a selected artifact
```
PUT /artifacts/{id}
```


#### Description
Edit description. Artifact is not allowed to be edited if it was used
in any deployment.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**id**  <br>*required*|Artifact identifier.|string|
|**Body**|**artifact**  <br>*optional*| |[ArtifactUpdate](#artifactupdate)|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**204**|The artifact metadata updated successfully.|No Content|
|**400**|Invalid Request.|[Error](#error)|
|**404**|Not Found.|[Error](#error)|
|**422**|Unprocessable Entity.|[Error](#error)|
|**500**|Internal Server Error.|[Error](#error)|


#### Produces

* `application/json`


#### Example HTTP request

##### Request body
```json
{
  "description" : "Some description"
}
```


#### Example HTTP response

##### Response 400
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 404
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 422
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 500
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```
___

<a name="artifacts-id-delete"></a>
### Delete the artifact
```
DELETE /artifacts/{id}
```


#### Description
Deletes the artifact from file and artifacts storage.
Artifacts used by deployments in progress can not be deleted
until deployment finishes.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**id**  <br>*required*|Artifact identifier.|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**204**|The artifact deleted successfully.|No Content|
|**404**|Not Found.|[Error](#error)|
|**409**|Artifact used by active deployment.|[Error](#error)|
|**500**|Internal Server Error.|[Error](#error)|


#### Produces

* `application/json`


#### Example HTTP response

##### Response 404
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 409
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 500
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```
___

<a name="artifacts-id-download-get"></a>
### Get the download link of a selected artifact
```
GET /artifacts/{id}/download
```


#### Description
Generates signed URL for downloading artifact file. URI can be used only
with GET HTTP method. Link supports such HTTP headers: 'Range',
'If-Modified-Since', 'If-Unmodified-Since' It is valid for specified
period of time.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**id**  <br>*required*|Artifact identifier.|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Successful response.|[ArtifactLink](#artifactlink)|
|**400**|Invalid Request.|[Error](#error)|
|**404**|Not Found.|[Error](#error)|
|**500**|Internal Server Error.|[Error](#error)|


#### Produces

* `application/json`


#### Example HTTP response

##### Response 200
```json
{
  "uri" : "http://mender.io/artifact.tar.gz.mender",
  "expire" : "2016-10-29T10:45:34.000+0000"
}
```


##### Response 400
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 404
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 500
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```
___

<a name="deployments-post"></a>
### Create a deployment
```
POST /deployments
```


#### Description
Deploy software to specified devices. Artifact is auto assigned to the
device from all available artifacts based on artifact name and device type.
Devices for which there are no compatible artifacts to be installed are
considered finished successfully as well as receive status of `noartifact`.
If there is no artifacts for the deployment, deployment will not be created
and the 422 Unprocessable Entity status code will be returned.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Body**|**deployment**  <br>*required*|New deployment that needs to be created.|[NewDeployment](#newdeployment)|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**201**|New deployment created.  <br>**Headers** :   <br>`Location` (string) : URL of the newly created deployment.|No Content|
|**400**|Invalid Request.|[Error](#error)|
|**403**|Feature not available in your Plan.|[Error](#error)|
|**422**|Unprocessable Entity.|[Error](#error)|
|**500**|Internal Server Error.|[Error](#error)|


#### Produces

* `application/json`


#### Example HTTP request

##### Request body
```json
[ {
  "name" : "production",
  "artifact_name" : "Application 0.0.1",
  "devices" : [ "00a0c91e6-7dec-11d0-a765-f81d4faebf6" ],
  "phases" : [ {
    "batch_size" : 5,
    "start_ts" : "2019-07-07T21:16:17.063+0000"
  }, {
    "batch_size" : 15,
    "start_ts" : "2019-09-07T21:16:17.063+0000"
  }, {
    "start_ts" : "2019-11-07T21:16:17.063+0000"
  } ],
  "retries" : 3
} ]
```


#### Example HTTP response

##### Response 400
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 403
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 422
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 500
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```
___

<a name="deployments-get"></a>
### Find all deployments
```
GET /deployments
```


#### Description
Returns a filtered collection of deployments in the system,
including active and historical. If both 'status' and 'query' are
not specified, all devices are listed.


#### Parameters

|Type|Name|Description|Schema|Default|
|---|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])| |
|**Query**|**created_after**  <br>*optional*|List only deployments created after and equal to Unix timestamp (UTC)|number (integer)| |
|**Query**|**created_before**  <br>*optional*|List only deployments created before and equal to Unix timestamp (UTC)|number (integer)| |
|**Query**|**page**  <br>*optional*|Results page number|number (integer)|`1`|
|**Query**|**per_page**  <br>*optional*|Maximum number of results per page.|number (integer)|`20`|
|**Query**|**search**  <br>*optional*|Deployment name or description filter.|string| |
|**Query**|**status**  <br>*optional*|Deployment status filter.|enum (inprogress, finished, pending, scheduled)| |


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Successful response.  <br>**Headers** :   <br>`Link` (string) : Standard header, we support 'first', 'next', and 'prev'.|< [Deployment](#deployment) > array|
|**400**|Invalid Request.|[Error](#error)|
|**500**|Internal Server Error.|[Error](#error)|


#### Produces

* `application/json`


#### Example HTTP response

##### Response 200
```json
[ {
  "created" : "2016-02-11T13:03:17.063+0000",
  "status" : "finished",
  "name" : "production",
  "artifact_name" : "Application 0.0.1",
  "id" : "00a0c91e6-7dec-11d0-a765-f81d4faebf6",
  "finished" : "2016-03-11T13:03:17.063+0000",
  "device_count" : 10,
  "retries" : 0
} ]
```


##### Response 400
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 500
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```
___

<a name="deployments-devices-id-delete"></a>
### Remove device from all deployments
```
DELETE /deployments/devices/{id}
```


#### Description
Set 'decommissioned' status to all pending device deployments for a given device


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**id**  <br>*required*|System wide device identifier|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**204**|Device was removed|No Content|
|**500**|Internal server error.|[Error](#error)|


#### Example HTTP response

##### Response 500
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```
___

<a name="deployments-releases-get"></a>
### List releases
```
GET /deployments/releases
```


#### Description
Returns a collection of releases, allows filtering by release name.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Query**|**name**  <br>*optional*|Release name filter.|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Successful response.|< [Release](#release) > array|
|**500**|Internal Server Error.|[Error](#error)|


#### Produces

* `application/json`


#### Example HTTP response

##### Response 200
```json
[ {
  "name" : "my-app-v1.0.1",
  "artifacts" : [ {
    "name" : "my-app-v1.0.1",
    "description" : "Application v1.0.1",
    "device_types_compatible" : [ "Beagle Bone" ],
    "id" : "0c13a0e6-6b63-475d-8260-ee42a590e8ff",
    "signed" : false,
    "modified" : "2016-03-11T13:03:17.063493443Z",
    "info" : {
      "type_info" : {
        "type" : "rootfs"
      }
    },
    "files" : [ {
      "name" : "rootfs-image-1",
      "checksum" : "cc436f982bc60a8255fe1926a450db5f195a19ad",
      "size" : 23421351,
      "date" : "2016-03-11T13:03:17.063+0000"
    } ],
    "metadata" : { }
  }, {
    "name" : "my-app-v1.0.1",
    "description" : "Application v1.0.1",
    "device_types_compatible" : [ "Raspberry Pi" ],
    "id" : "0c13a0e6-6b63-475d-8260-ee42a590e8ff",
    "signed" : false,
    "modified" : "2016-03-11T13:03:17.063493443Z",
    "info" : {
      "type_info" : {
        "type" : "rootfs"
      }
    },
    "files" : [ {
      "name" : "rootfs-image-1",
      "checksum" : "cc436f982bc60a8255fe1926a450db5f195a19ad",
      "size" : 23421351,
      "date" : "2016-03-11T13:03:17.063+0000"
    } ],
    "metadata" : { }
  } ]
}, {
  "name" : "my-app-v2.0.0",
  "artifacts" : [ {
    "name" : "my-app-v2.0.0",
    "description" : "Application v2.0.0",
    "device_types_compatible" : [ "Beagle Bone" ],
    "id" : "0c13a0e6-6b63-475d-8260-ee42a590e8ff",
    "signed" : false,
    "modified" : "2016-03-11T13:03:17.063493443Z",
    "info" : {
      "type_info" : {
        "type" : "rootfs"
      }
    },
    "files" : [ {
      "name" : "rootfs-image-1",
      "checksum" : "cc436f982bc60a8255fe1926a450db5f195a19ad",
      "size" : 23421351,
      "date" : "2016-03-11T13:03:17.063+0000"
    } ],
    "metadata" : { }
  } ]
} ]
```


##### Response 500
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```
___

<a name="deployments-deployment_id-devices-get"></a>
### List devices of a deployment
```
GET /deployments/{deployment_id}/devices
```


#### Description
Returns a collection of a selected deployment's status for each assigned device.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**deployment_id**  <br>*required*|Deployment identifier.|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|OK|< [Device](#device) > array|
|**404**|Not Found.|[Error](#error)|
|**500**|Internal Server Error.|[Error](#error)|


#### Produces

* `application/json`


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : "00a0c91e6-7dec-11d0-a765-f81d4faebf6",
  "finished" : "2016-03-11T13:03:17.063+0000",
  "status" : "pending",
  "created" : "2016-02-11T13:03:17.063+0000",
  "device_type" : "Raspberry Pi 3"
} ]
```


##### Response 404
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 500
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```
___

<a name="deployments-deployment_id-devices-device_id-log-get"></a>
### Get the log of a selected device's deployment
```
GET /deployments/{deployment_id}/devices/{device_id}/log
```


#### Description
Returns the log of a selected device, collected during a particular deployment.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**deployment_id**  <br>*required*|Deployment identifier.|string|
|**Path**|**device_id**  <br>*required*|Device identifier.|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Successful response.|No Content|
|**404**|Not Found.|[Error](#error)|
|**500**|Internal Server Error.|[Error](#error)|


#### Produces

* `text/plain`


#### Example HTTP response

##### Response 404
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 500
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```
___

<a name="deployments-deployment_id-statistics-get"></a>
### Get the statistics of a selected deployment
```
GET /deployments/{deployment_id}/statistics
```


#### Description
Returns the statistics of a selected deployment statuses.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**deployment_id**  <br>*required*|Deployment identifier|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|OK|[DeploymentStatistics](#deploymentstatistics)|
|**404**|Not Found.|[Error](#error)|
|**500**|Internal Server Error.|[Error](#error)|


#### Produces

* `application/json`


#### Example HTTP response

##### Response 200
```json
{
  "success" : 3,
  "pending" : 1,
  "failure" : 0,
  "downloading" : 1,
  "installing" : 2,
  "rebooting" : 3,
  "noartifact" : 0,
  "already-installed" : 0,
  "aborted" : 0
}
```


##### Response 404
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 500
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```
___

<a name="deployments-deployment_id-status-put"></a>
### Abort the deployment
```
PUT /deployments/{deployment_id}/status
```


#### Description
Aborts the deployment that is scheduled, pending or in progress. For devices included in this deployment it means that:
- Devices that have completed the deployment (i.e. reported final status) are not affected by the abort, and their original status is kept in the deployment report.
- Devices that do not yet know about the deployment at time of abort will not start the deployment.
- Devices that are in the middle of the deployment at time of abort will finish its deployment normally, but they will not be able to change its deployment status so they will perform rollback.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**deployment_id**  <br>*required*|Deployment identifier.|string|
|**Body**|**Status**  <br>*required*|Deployment status.|[Status](#deployments-deployment_id-status-put-status)|

<a name="deployments-deployment_id-status-put-status"></a>
**Status**

|Name|Schema|
|---|---|
|**status**  <br>*required*|enum (aborted)|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**204**|Status updated successfully.|No Content|
|**400**|Invalid Request.|[Error](#error)|
|**404**|Not Found.|[Error](#error)|
|**422**|Unprocessable Entity.|[Error](#error)|
|**500**|Internal Server Error.|[Error](#error)|


#### Produces

* `application/json`


#### Example HTTP response

##### Response 400
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 404
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 422
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 500
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```
___

<a name="deployments-id-get"></a>
### Get the details of a selected deployment
```
GET /deployments/{id}
```


#### Description
Returns the details of a particular deployment.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**id**  <br>*required*|Deployment identifier.|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Successful response.|[Deployment](#deployment)|
|**404**|Not Found.|[Error](#error)|
|**500**|Internal Server Error.|[Error](#error)|


#### Produces

* `application/json`


#### Example HTTP response

##### Response 200
```json
{
  "created" : "2016-02-11T13:03:17.063+0000",
  "name" : "production",
  "artifact_name" : "Application 0.0.1",
  "id" : "00a0c91e6-7dec-11d0-a765-f81d4faebf6",
  "finished" : "2016-03-11T13:03:17.063+0000"
}
```


##### Response 404
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 500
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```
___

<a name="deployments-id-device_list-get"></a>
### Get the list of device IDs being part of static deployment.
```
GET /deployments/{id}/device_list
```


#### Description
Returns the list of device IDs for which the static deployment has been created.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**id**  <br>*required*|Deployment identifier.|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Successful response.|< string > array|
|**400**|Invalid Request.|[Error](#error)|
|**404**|Not Found.|[Error](#error)|
|**500**|Internal Server Error.|[Error](#error)|


#### Produces

* `application/json`


#### Example HTTP response

##### Response 200
```json
[ "00a0c91e6-7dec-11d0-a765-f81d4faebf6", "00a0c91e6-7dec-11d0-a765-f81d4faebf8", "00a0c91e6-7dec-11d0-a765-f81d4faebf7" ]
```


##### Response 400
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 404
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```


##### Response 500
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```
___

<a name="limits-storage-get"></a>
### Get storage limit and current storage usage
```
GET /limits/storage
```


#### Description
Get storage limit and current storage usage for currently logged in user.
If the limit value is 0 it means there is no limit for storage for logged in user.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Successful response.|[StorageLimit](#storagelimit)|
|**500**|Internal Server Error.|[Error](#error)|


#### Produces

* `application/json`


#### Example HTTP response

##### Response 200
```json
{
  "limit" : 1073741824,
  "usage" : 536870912
}
```


##### Response 500
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```




<a name="definitions"></a>
## Definitions

<a name="artifact"></a>
### Artifact
Detailed artifact.


|Name|Description|Schema|
|---|---|---|
|**description**  <br>*required*| |string|
|**device_types_compatible**  <br>*required*| |< string > array|
|**id**  <br>*required*| |string|
|**info**  <br>*optional*| |[ArtifactInfo](#artifactinfo)|
|**modified**  <br>*required*|Represents creation / last edition of any of the artifact properties.|string (date-time)|
|**name**  <br>*required*| |string|
|**signed**  <br>*optional*|Idicates if artifact is signed or not.|boolean|
|**size**  <br>*optional*|Artifact total size in bytes - the size of the actual file that will be transferred to the device (compressed).|number (integer)|
|**updates**  <br>*optional*| |< [Update](#update) > array|


<a name="artifactinfo"></a>
### ArtifactInfo
Information about artifact format and version.


|Name|Schema|
|---|---|
|**format**  <br>*optional*|string|
|**version**  <br>*optional*|integer|


<a name="artifactlink"></a>
### ArtifactLink
URL for artifact file download.


|Name|Schema|
|---|---|
|**expire**  <br>*required*|string (date-time)|
|**uri**  <br>*required*|string|


<a name="artifacttypeinfo"></a>
### ArtifactTypeInfo
Information about update type.


|Name|Schema|
|---|---|
|**type**  <br>*optional*|string|


<a name="artifactupdate"></a>
### ArtifactUpdate
Artifact information update.


|Name|Schema|
|---|---|
|**description**  <br>*optional*|string|


<a name="deployment"></a>
### Deployment

|Name|Description|Schema|
|---|---|---|
|**artifact_name**  <br>*required*| |string|
|**artifacts**  <br>*optional*| |< string > array|
|**created**  <br>*required*| |string (date-time)|
|**device_count**  <br>*required*| |integer|
|**dynamic**  <br>*optional*|Flag indicating if the deployment is dynamic or not.|boolean|
|**filter**  <br>*optional*| |[Filter](#filter)|
|**finished**  <br>*optional*| |string (date-time)|
|**id**  <br>*required*| |string|
|**initial_device_count**  <br>*optional*|In case of dynamic deployments this is a number of devices targeted initially (maching the filter at the moment of deployment creation).|integer|
|**max_devices**  <br>*optional*|max_devices denotes a limit on a number of completed deployments (failed or successful) above which the dynamic deployment will be finished.|integer|
|**name**  <br>*required*| |string|
|**phases**  <br>*optional*| |< [DeploymentPhase](#deploymentphase) > array|
|**retries**  <br>*optional*|The number of times a device can retry the deployment in case of failure, defaults to 0|integer|
|**status**  <br>*required*| |enum (scheduled, pending, inprogress, finished)|


<a name="deploymentphase"></a>
### DeploymentPhase

|Name|Description|Schema|
|---|---|---|
|**batch_size**  <br>*optional*|Percentage of devices to update in the phase.|integer|
|**device_count**  <br>*optional*|Number of devices which already requested an update within this phase.|integer|
|**id**  <br>*optional*|Phase identifier.|string|
|**start_ts**  <br>*optional*|Start date of a phase.<br>May be undefined for the first phase of a deployment.|string (date-time)|


<a name="deploymentstatistics"></a>
### DeploymentStatistics

|Name|Description|Schema|
|---|---|---|
|**aborted**  <br>*required*|Number of deployments aborted by user.|integer|
|**already-installed**  <br>*required*|Number of devices unaffected by upgrade, since they are already running the specified software version.|integer|
|**downloading**  <br>*required*|Number of deployments being downloaded.|integer|
|**failure**  <br>*required*|Number of failed deployments.|integer|
|**installing**  <br>*required*|Number of deployments devices being installed.|integer|
|**noartifact**  <br>*required*|Do not have appropriate artifact for device type.|integer|
|**pending**  <br>*required*|Number of pending deployments.|integer|
|**rebooting**  <br>*required*|Number of deployments devices are rebooting into.|integer|
|**success**  <br>*required*|Number of successful deployments.|integer|


<a name="device"></a>
### Device

|Name|Description|Schema|
|---|---|---|
|**created**  <br>*optional*| |string (date-time)|
|**device_type**  <br>*optional*| |string|
|**finished**  <br>*optional*| |string (date-time)|
|**id**  <br>*required*|Device identifier.|string|
|**log**  <br>*required*|Availability of the device's deployment log.|boolean|
|**state**  <br>*optional*|State reported by device|string|
|**status**  <br>*required*| |enum (downloading, installing, rebooting, pending, success, failure, noartifact, already-installed, aborted, decommissioned)|
|**substate**  <br>*optional*|Additional state information|string|


<a name="error"></a>
### Error
Error descriptor.


|Name|Description|Schema|
|---|---|---|
|**error**  <br>*optional*|Description of the error.|string|
|**request_id**  <br>*optional*|Request ID (same as in X-MEN-RequestID header).|string|


<a name="filter"></a>
### Filter
Inventory filter assigned to the deployment


|Name|Description|Schema|
|---|---|---|
|**id**  <br>*required*|Unique identifier of the saved filter.|string|
|**name**  <br>*required*|Name of the saved filter.|string|
|**terms**  <br>*optional*| |< [FilterPredicate](#filterpredicate) > array|


<a name="filterpredicate"></a>
### FilterPredicate
Attribute filter predicate


|Name|Description|Schema|
|---|---|---|
|**attribute**  <br>*required*|Name of the attribute to be queried for filtering.|string|
|**scope**  <br>*required*|The scope of the attribute.<br><br>Scope is a string and acts as namespace for the attribute name.|string|
|**type**  <br>*required*|Type or operator of the filter predicate.|enum ($eq, $gt, $gte, $in, $lt, $lte, $ne, $nin, $exists)|
|**value**  <br>*required*|The value of the attribute to be used in filtering.<br><br>Attribute type is implicit, inferred from the JSON type.<br><br>Supported types: number, string, array of numbers, array of strings.<br>Mixed arrays are not allowed.|string|


<a name="newdeployment"></a>
### NewDeployment

|Name|Description|Schema|
|---|---|---|
|**artifact_name**  <br>*required*| |string|
|**devices**  <br>*required*| |< string > array|
|**name**  <br>*required*| |string|
|**phases**  <br>*optional*| |< [NewDeploymentPhase](#newdeploymentphase) > array|
|**retries**  <br>*optional*|The number of times a device can retry the deployment in case of failure, defaults to 0|integer|


<a name="newdeploymentphase"></a>
### NewDeploymentPhase

|Name|Description|Schema|
|---|---|---|
|**batch_size**  <br>*optional*|Percentage of devices to update in the phase.<br>This field is optional for the last phase.<br>The last phase will contain the rest of the devices.<br>Note that if the percentage of devices entered does not<br>add up to a whole number of devices it is rounded down,<br>and in the case it is rounded down to zero, a 400 error<br>will be returned. This is mostly a concern when the deployment<br>consists of a low number of devices, like say 5 percent of 11<br>devices will round to zero, and an error is returned by the server.|integer|
|**start_ts**  <br>*optional*|Start date of a phase.<br>Can be skipped for the first phase of a new deployment definition ('start immediately').|string (date-time)|


<a name="release"></a>
### Release
Groups artifacts with the same release name into a single resource.


|Name|Description|Schema|
|---|---|---|
|**artifacts**  <br>*optional*|list of artifacts for this release.|< [Artifact](#artifact) > array|
|**name**  <br>*optional*|release name.|string|


<a name="storagelimit"></a>
### StorageLimit
Tenant account storage limit and storage usage.


|Name|Description|Schema|
|---|---|---|
|**limit**  <br>*required*|Storage limit in bytes. If set to 0 - there is no limit for storage.|integer|
|**usage**  <br>*required*|Current storage usage in bytes.|integer|


<a name="update"></a>
### Update
Single updated to be applied.


|Name|Description|Schema|
|---|---|---|
|**files**  <br>*optional*| |< [UpdateFile](#updatefile) > array|
|**meta_data**  <br>*optional*|meta_data is an object of unknown structure as this is dependent of update type (also custom defined by user)|object|
|**type_info**  <br>*optional*| |[ArtifactTypeInfo](#artifacttypeinfo)|


<a name="updatefile"></a>
### UpdateFile
Information about particular update file.


|Name|Schema|
|---|---|
|**checksum**  <br>*optional*|string|
|**date**  <br>*optional*|string (date-time)|
|**name**  <br>*optional*|string|
|**size**  <br>*optional*|integer|





