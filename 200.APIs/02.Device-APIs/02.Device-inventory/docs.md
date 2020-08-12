---
title: Device inventory
taxonomy:
    category: docs
api: true
template: docs
---

<a name="overview"></a>
## Overview
An API for uploading device attributes. Intended for use by devices.

Devices can upload vendor-specific attributes (software/hardware info, health checks, metrics, etc.) of various data types to the backend.


### Version information
*Version* : 1


### URI scheme
*Host* : docker.mender.io  
*BasePath* : /api/devices/v1/inventory  
*Schemes* : HTTPS




<a name="paths"></a>
## Paths
- [PATCH/device/attributes](#device-attributes-patch)


___
<a name="device-attributes-patch"></a>
### Upload a set of attributes for a device
```
PATCH /device/attributes
```


#### Description
Saves the provided attribute set for the authenticated device.
The device ID is retrieved from the authorization header.

This method has upsert semantics:
* the values of existing attributes are overwritten
* attributes uploaded for the first time are automatically created


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the Device Authentication Service.|string (Bearer [token])|
|**Body**|**attributes**  <br>*required*|A list of attribute descriptors.|< [Attribute](#attribute) > array|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Attributes were uploaded successfully.|No Content|
|**400**|Missing/malformed request parameters or body. See error for details.|[Error](#error)|
|**401**|The device is not authenticated.|No Content|
|**500**|Internal server error.|[Error](#error)|


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




<a name="definitions"></a>
## Definitions

<a name="attribute"></a>
### Attribute
Attribute descriptor.


|Name|Description|Schema|
|---|---|---|
|**description**  <br>*optional*|Attribute description.|string|
|**name**  <br>*required*|A human readable, unique attribute ID, e.g. 'device_type', 'ip_addr', 'cpu_load', etc.|string|
|**value**  <br>*required*|The current value of the attribute.<br><br>Attribute type is implicit, inferred from the JSON type.<br><br>Supported types: number, string, array of numbers, array of strings. Mixed arrays are not allowed.|string|


<a name="error"></a>
### Error
Error descriptor.


|Name|Description|Schema|
|---|---|---|
|**error**  <br>*optional*|Description of the error.|string|
|**request_id**  <br>*optional*|Request ID (same as in X-MEN-RequestID header).|string|





