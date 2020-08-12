---
title: Deployments
taxonomy:
    category: docs
api: true
template: docs
---

<a name="overview"></a>
## Overview
An API for device firmware deployments. Intended for use by devices.

Devices can get new updates and send information about current deployment status.


### Version information
*Version* : 1


### URI scheme
*Host* : hosted.mender.io  
*BasePath* : /api/devices/v1/deployments  
*Schemes* : HTTPS




<a name="paths"></a>
## Paths
- [POST/device/deployments/next](#device-deployments-next-post)
- [GET/device/deployments/next](#device-deployments-next-get)
- [PUT/device/deployments/{id}/log](#device-deployments-id-log-put)
- [PUT/device/deployments/{id}/status](#device-deployments-id-status-put)


___
<a name="device-deployments-next-post"></a>
### Get a next update
```
POST /device/deployments/next
```


#### Description
Returns a next update to be installed on the device.
Next update will be chosen based on parameters provided in the request
body. Request body should contain artifact_provides object.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the Device Authentication Service.|string (Bearer [token])|
|**Body**|**artifact_provides**  <br>*required*|Key-value map of strings which describes the artifact(s) installed on the device and the<br>device itself. It is used to determine the next deployment. The keys device_type and<br>artifact_name are mandatory, additional free-form key-value pairs can be specified.|[artifact_provides](#device-deployments-next-post-artifact_provides)|

<a name="device-deployments-next-post-artifact_provides"></a>
**artifact_provides**

|Name|Description|Schema|
|---|---|---|
|**artifact_name**  <br>*required*|Name of the currently installed artifact.|string|
|**device_type**  <br>*required*|Device type of the device.|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Successful response.|[DeploymentInstructions](#deploymentinstructions)|
|**204**|No updates for device.|No Content|
|**400**|Invalid Request.|[Error](#error)|
|**404**|Not Found.|[Error](#error)|
|**500**|Internal Server Error.|[Error](#error)|


#### Produces

* `application/json`


#### Example HTTP response

##### Response 200
```json
{
  "id" : "w81s4fae-7dec-11d0-a765-00a0c91e6bf6",
  "artifact" : {
    "artifact_name" : "my-app-0.1",
    "source" : {
      "uri" : "https://aws.my_update_bucket.com/image_123",
      "expire" : "2016-03-11T13:03:17.063+0000"
    },
    "device_types_compatible" : [ "rspi", "rspi2", "rspi0" ]
  }
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

<a name="device-deployments-next-get"></a>
### Get a next update
```
GET /device/deployments/next
```


#### Description
Returns a next update to be installed on the device.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the Device Authentication Service.|string (Bearer [token])|
|**Query**|**artifact_name**  <br>*required*|currently installed artifact|string|
|**Query**|**device_type**  <br>*required*|Device type of device|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Successful response.|[DeploymentInstructions](#deploymentinstructions)|
|**204**|No updates for device.|No Content|
|**400**|Invalid Request.|[Error](#error)|
|**404**|Not Found.|[Error](#error)|
|**500**|Internal Server Error.|[Error](#error)|


#### Produces

* `application/json`


#### Example HTTP response

##### Response 200
```json
{
  "id" : "w81s4fae-7dec-11d0-a765-00a0c91e6bf6",
  "artifact" : {
    "artifact_name" : "my-app-0.1",
    "source" : {
      "uri" : "https://aws.my_update_bucket.com/image_123",
      "expire" : "2016-03-11T13:03:17.063+0000"
    },
    "device_types_compatible" : [ "rspi", "rspi2", "rspi0" ]
  }
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

<a name="device-deployments-id-log-put"></a>
### Upload the device deployment log
```
PUT /device/deployments/{id}/log
```


#### Description
Set the log of a selected deployment. Messages are split by line in the payload.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the Device Authentication Service.|string (Bearer [token])|
|**Path**|**id**  <br>*required*|Deployment identifier.|string|
|**Body**|**Log**  <br>*required*|Deployment log|[DeploymentLog](#deploymentlog)|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**204**|The deployment log uploaded successfully.|No Content|
|**400**|Invalid Request.|[Error](#error)|
|**404**|Not Found.|[Error](#error)|
|**500**|Internal Server Error.|[Error](#error)|


#### Produces

* `application/json`


#### Example HTTP request

##### Request body
```json
{
  "messages" : [ {
    "timestamp" : "2016-03-11T13:03:17.063+0000",
    "level" : "INFO",
    "message" : "OK"
  }, {
    "timestamp" : "2016-03-11T13:03:18.024+0000",
    "level" : "DEBUG",
    "message" : "successfully updated."
  } ]
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

<a name="device-deployments-id-status-put"></a>
### Update the device deployment status
```
PUT /device/deployments/{id}/status
```


#### Description
Updates the status of a deployment on a particular device. Final status
of the deployment is required to be set to indicate the success or failure
of the installation process. The status can not be changed when deployment
status is set to aborted. Reporting of intermediate steps such as
installing, downloading, rebooting is optional.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the Device Authentication Service.|string (Bearer [token])|
|**Path**|**id**  <br>*required*|Deployment identifier.|string|
|**Body**|**Status**  <br>*required*|Deployment status.|[Status](#device-deployments-id-status-put-status)|

<a name="device-deployments-id-status-put-status"></a>
**Status**

|Name|Description|Schema|
|---|---|---|
|**status**  <br>*required*| |enum (installing, downloading, rebooting, success, failure, already-installed)|
|**substate**  <br>*optional*|Additional state information|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**204**|Status updated successfully.|No Content|
|**400**|Invalid Request.|[Error](#error)|
|**404**|Not Found.|[Error](#error)|
|**409**|Status already set to aborted.|No Content|
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


##### Response 500
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```




<a name="definitions"></a>
## Definitions

<a name="deploymentinstructions"></a>
### DeploymentInstructions

|Name|Description|Schema|
|---|---|---|
|**artifact**  <br>*required*| |[artifact](#deploymentinstructions-artifact)|
|**id**  <br>*required*|Deployment ID (device unique)|string|

<a name="deploymentinstructions-artifact"></a>
**artifact**

|Name|Description|Schema|
|---|---|---|
|**artifact_name**  <br>*required*| |string|
|**device_types_compatible**  <br>*required*|Compatible device types|< string > array|
|**source**  <br>*required*| |[source](#deploymentinstructions-source)|

<a name="deploymentinstructions-source"></a>
**source**

|Name|Description|Schema|
|---|---|---|
|**expire**  <br>*optional*|URL expiration time|string (date-time)|
|**uri**  <br>*optional*|URL to fetch the artifact from|string (url)|


<a name="deploymentlog"></a>
### DeploymentLog

|Name|Schema|
|---|---|
|**messages**  <br>*required*|< [messages](#deploymentlog-messages) > array|

<a name="deploymentlog-messages"></a>
**messages**

|Name|Schema|
|---|---|
|**level**  <br>*required*|string|
|**message**  <br>*required*|string|
|**timestamp**  <br>*required*|string (date-time)|


<a name="error"></a>
### Error
Error descriptor.


|Name|Description|Schema|
|---|---|---|
|**error**  <br>*optional*|Description of the error.|string|
|**request_id**  <br>*optional*|Request ID (same as in X-MEN-RequestID header).|string|





