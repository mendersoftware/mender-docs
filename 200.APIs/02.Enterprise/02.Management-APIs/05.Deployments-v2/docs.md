---
title: Deployments v2
taxonomy:
    category: docs
api: true
template: docs
---

<a name="overview"></a>
## Overview
Version 2 of the API for deployments management.
Intended for use by the web GUI.


### Version information
*Version* : 1


### URI scheme
*Host* : docker.mender.io  
*BasePath* : /api/management/v2/deployments  
*Schemes* : HTTPS




<a name="paths"></a>
## Paths
- [POST/deployments](#deployments-post)


___
<a name="deployments-post"></a>
### Create a deployment
```
POST /deployments
```


#### Description
Deploy software to devices matching the given filter.
The artifact is auto assigned to the device from all available artifacts based on artifact name and device type.
Devices for which there are no compatible artifacts to be installed are considered finished successfully as well as receive the status of `noartifact`.
If there are no artifacts for the deployment, the deployment will not be created and the 422 Unprocessable Entity status code will be returned.
Dynamic deployments feature is available only to Enterprise users.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Body**|**deployment**  <br>*required*|New deployment that needs to be created.|[NewDeployment](#newdeployment)|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**201**|New deployment created.  <br>**Headers** :   <br>`Location` (string) : URL of the newly created deployment.|No Content|
|**400**|Bad request, see error message for details.|[Error](#error)|
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
  "filter_id" : "00a0c91e6-7dec-11d0-a765-f81d4faebf6",
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




<a name="definitions"></a>
## Definitions

<a name="error"></a>
### Error
Error descriptor.


|Name|Description|Schema|
|---|---|---|
|**error**  <br>*optional*|Description of the error.|string|
|**request_id**  <br>*optional*|Request ID (same as in X-MEN-RequestID header).|string|


<a name="newdeployment"></a>
### NewDeployment

|Name|Description|Schema|
|---|---|---|
|**artifact_name**  <br>*required*| |string|
|**filter_id**  <br>*required*|ID of a filter from inventory service.|string|
|**max_devices**  <br>*optional*|max_devices denotes a limit on a number of completed deployments (failed or successful) above which the dynamic deployment will be finished|integer|
|**name**  <br>*required*| |string|
|**phases**  <br>*optional*| |< [NewDeploymentPhase](#newdeploymentphase) > array|
|**retries**  <br>*optional*|The number of times a device can retry the deployment in case of failure, defaults to 0|integer|


<a name="newdeploymentphase"></a>
### NewDeploymentPhase

|Name|Description|Schema|
|---|---|---|
|**batch_size**  <br>*optional*|Percentage of devices to update in the phase.<br>This field is optional for the last phase.<br>The last phase will contain the rest of the devices.<br>Note that if the percentage of devices entered does not add up to a whole number of devices it is rounded down, and in the case it is rounded down to zero, a 400 error will be returned.<br>This is mostly a concern when the deployment consists of a low number of devices, like say 5 percent of 11 devices will round to zero, and an error is returned by the server.<br>In the case of dynamic deployment, the number of devices for each phase is being calculated based on the initial number of devices matching the filter.|integer|
|**start_ts**  <br>*optional*|Start date of a phase.<br>Can be skipped for the first phase of a new deployment definition ('start immediately').|string (date-time)|





