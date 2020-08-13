---
title: Device inventory
taxonomy:
    category: docs
api: true
template: docs
---

<a name="overview"></a>
## Overview
An API for device attribute management and device grouping. Intended for use by the web GUI.

Devices can upload vendor-specific attributes (software/hardware info, health checks, metrics, etc.) of various data types to the backend.

This API enables the user to:
* list devices with their attributes
* search devices by attribute value
* use the results to create and manage device groups for the purpose of deployment scheduling


### Version information
*Version* : 1


### URI scheme
*Host* : docker.mender.io  
*BasePath* : /api/management/v1/inventory  
*Schemes* : HTTPS




<a name="paths"></a>
## Paths
- [POST/devices](#devices-post)
- [GET/devices](#devices-get)
- [GET/devices?attr_name_1=foo&attr_name_2=100&...](#devices-get)
- [GET/devices/{id}](#devices-id-get)
- [DELETE/devices/{id}](#devices-id-delete)
- [GET/devices/{id}/group](#devices-id-group-get)
- [PUT/devices/{id}/group](#devices-id-group-put)
- [DELETE/devices/{id}/group/{name}](#devices-id-group-name-delete)
- [GET/groups](#groups-get)
- [GET/groups/{name}/devices](#groups-name-devices-get)


___
<a name="devices-post"></a>
### Create a device resource with the supplied set of attributes
```
POST /devices
```


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Body**|**device**  <br>*required*| |[DeviceNew](#devicenew)|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**201**|The device was successfully created.  <br>**Headers** :   <br>`Location` (string) : URI for the newly created 'Device' resource.|No Content|
|**400**|Malformed request body. See error for details.|[Error](#error)|
|**409**|Conflict - the device already exists.|[Error](#error)|
|**500**|Internal server error.|[Error](#error)|


#### Example HTTP request

##### Request body
```json
{
  "id" : "291ae0e5956c69c2267489213df4459d19ed48a806603def19d417d004a4b67e",
  "attributes" : [ {
    "name" : "ip_addr",
    "value" : "1.2.3.4",
    "description" : "IP address"
  }, {
    "name" : "mac_addr",
    "value" : "00.01:02:03:04:05",
    "description" : "MAC address"
  }, {
    "name" : "ports",
    "value" : [ "8080", "8081" ],
    "description" : "Open ports"
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

<a name="devices-get"></a>
### List devices
```
GET /devices
```


#### Description
Returns a paged collection of devices and their attributes.
Accepts optional search and sort parameters.

**Searching**
Searching by attributes values is accomplished by appending attribute
name/value pairs to the query string, e.g.:

```
GET /devices?attr_name_1=foo&
             attr_name_2=100&
             ...
```


#### Parameters

|Type|Name|Description|Schema|Default|
|---|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])| |
|**Query**|**has_group**  <br>*optional*|If present, limits the results only to devices assigned/not assigned to a group.|boolean| |
|**Query**|**page**  <br>*optional*|Starting page.|number (integer)|`1`|
|**Query**|**per_page**  <br>*optional*|Number of results per page.|number (integer)|`10`|
|**Query**|**sort**  <br>*optional*|Supports sorting the device list by attribute values.<br><br>The parameter is formatted as a list of attribute names and sort directions, e.g.:<br><br>'?sort=attr1:asc, attr2:desc'<br><br>will sort by 'attr1' ascending, and then by 'attr2' descending. 'desc' is the default<br>sort direction, and can be omitted.|string| |


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Successful response.  <br>**Headers** :   <br>`Link` (string) : Standard header, used for page navigation.<br><br>Supported relation types are 'first', 'next' and 'prev'.|< [Device](#device) > array|
|**400**|Missing or malformed request parameters. See error for details.|[Error](#error)|
|**500**|Internal error.|[Error](#error)|


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : "291ae0e5956c69c2267489213df4459d19ed48a806603def19d417d004a4b67e",
  "attributes" : [ {
    "name" : "ip_addr",
    "value" : "1.2.3.4",
    "description" : "IP address"
  }, {
    "name" : "mac_addr",
    "value" : "00.01:02:03:04:05",
    "description" : "MAC address"
  }, {
    "name" : "ports",
    "value" : [ "8080", "8081" ],
    "description" : "Open ports"
  } ],
  "updated_ts" : "2016-10-03T16:58:51.639Z"
}, {
  "id" : "76f40e5956c699e327489213df4459d1923e1a806603def19d417d004a4a3ef",
  "attributes" : [ {
    "name" : "mac",
    "value" : "00:01:02:03:04:05",
    "description" : "MAC address"
  } ],
  "updated_ts" : "2016-10-04T18:24:21.432Z"
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

<a name="devices-id-get"></a>
### Get a selected device
```
GET /devices/{id}
```


#### Description
Returns the details of the selected devices, including its attributes.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**id**  <br>*required*|Device identifier.|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Successful response - the device was found.|[Device](#device)|
|**404**|The device was not found.|[Error](#error)|
|**500**|Internal server error.|[Error](#error)|


#### Example HTTP response

##### Response 200
```json
{
  "id" : "291ae0e5956c69c2267489213df4459d19ed48a806603def19d417d004a4b67e",
  "attributes" : [ {
    "name" : "ip_addr",
    "value" : "1.2.3.4",
    "description" : "IP address"
  }, {
    "name" : "mac_addr",
    "value" : "00.01:02:03:04:05",
    "description" : "MAC address"
  }, {
    "name" : "ports",
    "value" : [ "8080", "8081" ],
    "description" : "Open ports"
  } ],
  "updated_ts" : "2016-10-03T16:58:51.639Z"
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

<a name="devices-id-delete"></a>
### Remove selected device
```
DELETE /devices/{id}
```


#### Description
Deletes all information concerning the device, including its attributes.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**id**  <br>*required*|Device identifier.|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**204**|Device removed|No Content|
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

<a name="devices-id-group-get"></a>
### Get a selected device's group
```
GET /devices/{id}/group
```


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**id**  <br>*required*|Device identifier.|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Successful response.<br><br>If the device is not assigned to any group, the 'group' field will be set to 'null'.|[Group](#group)|
|**400**|Missing or malformed request params or body. See the error message for details.|No Content|
|**404**|The device was not found.|[Error](#error)|
|**500**|Internal server error.|[Error](#error)|


#### Example HTTP response

##### Response 200
```json
{
  "group" : "testing"
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

<a name="devices-id-group-put"></a>
### Add a device to a group
```
PUT /devices/{id}/group
```


#### Description
Adds a device to a group.

Note that a given device can belong to at most one group.
If a device already belongs to some group, it will be moved
to the selected one.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**id**  <br>*required*|Device identifier.|string|
|**Body**|**group**  <br>*required*|Group descriptor.|[Group](#group)|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**204**|Success - the device was added to the group.|No Content|
|**400**|Missing or malformed request params or body. See the error message for details.|No Content|
|**404**|The device was not found.|[Error](#error)|
|**500**|Internal server error.|[Error](#error)|


#### Example HTTP request

##### Request body
```json
{
  "group" : "staging"
}
```


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

<a name="devices-id-group-name-delete"></a>
### Remove a device from a group
```
DELETE /devices/{id}/group/{name}
```


#### Description
Removes the device with identifier 'id' from the group 'group'.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**id**  <br>*required*|Device identifier.|string|
|**Path**|**name**  <br>*required*|Group name.|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**204**|The device was successfully removed from the group.|No Content|
|**404**|The device was not found or doesn't belong to the group.|[Error](#error)|
|**500**|Internal error.|[Error](#error)|


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

<a name="groups-get"></a>
### List groups
```
GET /groups
```


#### Description
Returns a collection of all defined device groups.


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Successful response.|< string > array|
|**500**|Internal server error.|[Error](#error)|


#### Example HTTP response

##### Response 200
```json
[ "staging", "testing", "production" ]
```


##### Response 500
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```
___

<a name="groups-name-devices-get"></a>
### List the devices belonging to a given group
```
GET /groups/{name}/devices
```


#### Description
Returns a paged collection of device IDs.


#### Parameters

|Type|Name|Description|Schema|Default|
|---|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])| |
|**Path**|**name**  <br>*required*|Group name.|string| |
|**Query**|**page**  <br>*optional*|Starting page.|number (integer)|`1`|
|**Query**|**per_page**  <br>*optional*|Number of results per page.|number (integer)|`10`|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Successful response  <br>**Headers** :   <br>`Link` (string) : Standard header, we support 'first', 'next', and 'prev'.|< string > array|
|**400**|Invalid request parameters.|[Error](#error)|
|**404**|The group was not found.|[Error](#error)|
|**500**|Internal server error.|[Error](#error)|


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

<a name="attribute"></a>
### Attribute
Attribute descriptor.


|Name|Description|Schema|
|---|---|---|
|**description**  <br>*optional*|Attribute description.|string|
|**name**  <br>*required*|A human readable, unique attribute ID, e.g. 'device_type', 'ip_addr', 'cpu_load', etc.|string|
|**value**  <br>*required*|The current value of the attribute.<br><br>Attribute type is implicit, inferred from the JSON type.<br><br>Supported types: number, string, array of numbers, array of strings. Mixed arrays are not allowed.|string|


<a name="device"></a>
### Device

|Name|Description|Schema|
|---|---|---|
|**attributes**  <br>*optional*|A list of attribute descriptors.|< [Attribute](#attribute) > array|
|**id**  <br>*optional*|Mender-assigned unique ID.|string|
|**updated_ts**  <br>*optional*|Timestamp of the most recent attribute update.|string|


<a name="devicenew"></a>
### DeviceNew

|Name|Description|Schema|
|---|---|---|
|**attributes**  <br>*optional*|A list of attribute descriptors.|< [Attribute](#attribute) > array|
|**id**  <br>*required*|Mender-assigned unique ID.|string|
|**updated_ts**  <br>*optional*|Timestamp of the most recent attribute update.|string|


<a name="error"></a>
### Error
Error descriptor.


|Name|Description|Schema|
|---|---|---|
|**error**  <br>*optional*|Description of the error.|string|
|**request_id**  <br>*optional*|Request ID (same as in X-MEN-RequestID header).|string|


<a name="group"></a>
### Group
Device group.


|Name|Schema|
|---|---|
|**group**  <br>*required*|string|





