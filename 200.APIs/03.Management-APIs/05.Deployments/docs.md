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
*Host* : docker.mender.io  
*BasePath* : /api/management/v1/deployments  
*Schemes* : HTTPS




<a name="paths"></a>
## Paths
- [POST/artifacts](#artifacts-post)
- [GET/artifacts](#artifacts-get)
- [GET/artifacts/{id}](#artifacts-id-get)
- [PUT/artifacts/{id}](#artifacts-id-put)
- [DELETE/artifacts/{id}](#artifacts-id-delete)
- [GET/artifacts/{id}/download](#artifacts-id-download-get)
- [POST/deployments](#deployments-post)
- [GET/deployments](#deployments-get)
- [DELETE/deployments/devices/{id}](#deployments-devices-id-delete)
- [GET/deployments/{deployment_id}/devices](#deployments-deployment_id-devices-get)
- [GET/deployments/{deployment_id}/devices/{device_id}/log](#deployments-deployment_id-devices-device_id-log-get)
- [GET/deployments/{deployment_id}/statistics](#deployments-deployment_id-statistics-get)
- [PUT/deployments/{deployment_id}/status](#deployments-deployment_id-status-put)
- [GET/deployments/{id}](#deployments-id-get)


___
<a name="artifacts-post"></a>
### Upload mender artifact
```
POST /artifacts
```


#### Description
Upload medner artifact. Multipart request with meta and artifact.

Supports artifact (versions v1, v2)[https://docs.mender.io/1.1/architecture/mender-artifacts#versions].


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**FormData**|**artifact**  <br>*required*|Artifact. It has to be the last part of request.|file|
|**FormData**|**description**  <br>*optional*| |string|
|**FormData**|**size**  <br>*required*|Size of the artifact file in bytes.|integer (long)|


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
Deletes the artifact from file and artifacts storage. Deployments
in progress can not be deleted until deployment finishes.


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

|Type|Name|Description|Schema|Default|
|---|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])| |
|**Path**|**id**  <br>*required*|Artifact identifier.|string| |
|**Query**|**expire**  <br>*optional*|Link validity length in minutes. Min 1 minute, max 10080 (1 week).|integer|`60`|


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
|**500**|Internal Server Error.|[Error](#error)|


#### Produces

* `application/json`


#### Example HTTP request

##### Request body
```json
[ {
  "name" : "production",
  "artifact_name" : "Application 0.0.1",
  "devices" : [ "00a0c91e6-7dec-11d0-a765-f81d4faebf6" ]
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
|**Query**|**page**  <br>*optional*|Results page number|number (integer)|`1`|
|**Query**|**per_page**  <br>*optional*|Number of results per page|number (integer)|`20`|
|**Query**|**search**  <br>*optional*|Deployment name or description filter.|string| |
|**Query**|**status**  <br>*optional*|Deployment status filter.|enum (inprogress, finished, pending)| |


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
  "finished" : "2016-03-11T13:03:17.063+0000"
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
Aborts the deployment that is pending or in progress. For devices included in this deployment it means that:
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

|Name|Schema|
|---|---|
|**artifact_name**  <br>*required*|string|
|**created**  <br>*required*|string (date-time)|
|**finished**  <br>*optional*|string (date-time)|
|**id**  <br>*required*|string|
|**name**  <br>*required*|string|
|**status**  <br>*required*|enum (inprogress, pending, finished)|


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
|**device_type**  <br>*required*| |string|
|**finished**  <br>*optional*| |string (date-time)|
|**id**  <br>*required*|Device identifier.|string|
|**log**  <br>*required*|Availability of the device's deployment log.|boolean|
|**status**  <br>*required*| |enum (inprogress, pending, success, failure, noartifact, aborted)|


<a name="error"></a>
### Error
Error descriptor.


|Name|Description|Schema|
|---|---|---|
|**error**  <br>*optional*|Description of the error.|string|
|**request_id**  <br>*optional*|Request ID (same as in X-MEN-RequestID header).|string|


<a name="newdeployment"></a>
### NewDeployment

|Name|Schema|
|---|---|
|**artifact_name**  <br>*required*|string|
|**devices**  <br>*required*|< string > array|
|**name**  <br>*required*|string|


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





