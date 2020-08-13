---
title: Device admission
taxonomy:
    category: docs
api: true
template: docs
---

<a name="overview"></a>
## Overview
An API for device admission handling. Intended for use by the web GUI.


### Version information
*Version* : 1


### URI scheme
*Host* : docker.mender.io  
*BasePath* : /api/management/v1/admission  
*Schemes* : HTTPS




<a name="paths"></a>
## Paths
- [GET/devices](#devices-get)
- [GET/devices/{id}](#devices-id-get)
- [PUT/devices/{id}](#devices-id-put)
- [GET/devices/{id}/status](#devices-id-status-get)
- [PUT/devices/{id}/status](#devices-id-status-put)


___
<a name="devices-get"></a>
### List known device  data sets
```
GET /devices
```


#### Description
Returns a paged collection of device authentication data sets registered
for admission, and optionally filters by device admission status.


#### Parameters

|Type|Name|Description|Schema|Default|
|---|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])| |
|**Query**|**device_id**  <br>*optional*|List auth sets owned by given device|string| |
|**Query**|**page**  <br>*optional*|Starting page.|number (integer)|`1`|
|**Query**|**per_page**  <br>*optional*|Number of results per page.|number (integer)|`10`|
|**Query**|**status**  <br>*optional*|Admission status filter. If not specified, all device data sets are listed.|enum (pending, accepted, rejected)| |


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Successful response.  <br>**Headers** :   <br>`Link` (string) : Standard header, used for page navigation.<br><br>Supported relation types are 'first', 'next' and 'prev'.|< [Device](#device) > array|
|**400**|Invalid parameters. See error message for details.|[Error](#error)|
|**500**|Internal server error.|[Error](#error)|


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : "291ae0e5956c69c2267489213df4459d19ed48a806603def19d417d004a4b67e",
  "device_id" : "58be8208dd77460001fe0d78",
  "device_identity" : "{"mac":"00:01:02:03:04:05", "sku":"My Device 1", "sn":"SN1234567890"}",
  "key" : "-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzogVU7RGDilbsoUt/DdH
VJvcepl0A5+xzGQ50cq1VE/Dyyy8Zp0jzRXCnnu9nu395mAFSZGotZVr+sWEpO3c
yC3VmXdBZmXmQdZqbdD/GuixJOYfqta2ytbIUPRXFN7/I7sgzxnXWBYXYmObYvdP
okP0mQanY+WKxp7Q16pt1RoqoAd0kmV39g13rFl35muSHbSBoAW3GBF3gO+mF5Ty
1ddp/XcgLOsmvNNjY+2HOD5F/RX0fs07mWnbD7x+xz7KEKjF+H7ZpkqCwmwCXaf0
iyYyh1852rti3Afw4mDxuVSD7sd9ggvYMc0QHIpQNkD4YWOhNiE1AB0zH57VbUYG
UwIDAQAB
-----END PUBLIC KEY-----
",
  "status" : "pending",
  "attributes" : {
    "mac" : "00:01:02:03:04:05",
    "sku" : "My Device 1",
    "sn" : "SN1234567890"
  },
  "request_time" : "2016-10-03T16:58:51.639Z"
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
### Get the details of a selected device authentication data set
```
GET /devices/{id}
```


#### Description
Returns the details of a particular device authentication data set.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**id**  <br>*required*|Device authentication data set identifier.|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Successful response - a device authentication data set is returned.|[Device](#device)|
|**404**|The device authentication data set was not found.|[Error](#error)|
|**500**|Internal server error.|[Error](#error)|


#### Example HTTP response

##### Response 200
```json
{
  "id" : "291ae0e5956c69c2267489213df4459d19ed48a806603def19d417d004a4b67e",
  "device_id" : "58be8208dd77460001fe0d78",
  "device_identity" : "{"mac":"00:01:02:03:04:05", "sku":"My Device 1", "sn":"SN1234567890"}",
  "key" : "-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzogVU7RGDilbsoUt/DdH
VJvcepl0A5+xzGQ50cq1VE/Dyyy8Zp0jzRXCnnu9nu395mAFSZGotZVr+sWEpO3c
yC3VmXdBZmXmQdZqbdD/GuixJOYfqta2ytbIUPRXFN7/I7sgzxnXWBYXYmObYvdP
okP0mQanY+WKxp7Q16pt1RoqoAd0kmV39g13rFl35muSHbSBoAW3GBF3gO+mF5Ty
1ddp/XcgLOsmvNNjY+2HOD5F/RX0fs07mWnbD7x+xz7KEKjF+H7ZpkqCwmwCXaf0
iyYyh1852rti3Afw4mDxuVSD7sd9ggvYMc0QHIpQNkD4YWOhNiE1AB0zH57VbUYG
UwIDAQAB
-----END PUBLIC KEY-----
",
  "status" : "pending",
  "attributes" : {
    "mac" : "00:01:02:03:04:05",
    "sku" : "My Device 1",
    "sn" : "SN1234567890"
  },
  "request_time" : "2016-10-03T16:58:51.639Z"
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

<a name="devices-id-put"></a>
### Submit a device authentication data set for admission
```
PUT /devices/{id}
```


#### Description
Adds the device authentication data set to the database with a 'pending'
admission status. If the device already exists, it changes the device's
status to 'pending' and updates identity data. The user will be able to
inspect the device, and either accept, or reject it.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**id**  <br>*required*|Device authentication data set identifier.|string|
|**Body**|**device**  <br>*required*|A device for admission.|[NewDevice](#newdevice)|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**204**|Device authentication data set submitted successfully.|No Content|
|**400**|The request body is malformed. See error for details.|[Error](#error)|
|**500**|Internal server error.|[Error](#error)|


#### Example HTTP request

##### Request body
```json
{
  "id" : "291ae0e5956c69c2267489213df4459d19ed48a806603def19d417d004a4b67e",
  "device_id" : "58be8208dd77460001fe0d78",
  "device_identity" : "{"mac":"00:01:02:03:04:05", "sku":"My Device 1", "sn":"SN1234567890"}",
  "key" : "-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzogVU7RGDilbsoUt/DdH
VJvcepl0A5+xzGQ50cq1VE/Dyyy8Zp0jzRXCnnu9nu395mAFSZGotZVr+sWEpO3c
yC3VmXdBZmXmQdZqbdD/GuixJOYfqta2ytbIUPRXFN7/I7sgzxnXWBYXYmObYvdP
okP0mQanY+WKxp7Q16pt1RoqoAd0kmV39g13rFl35muSHbSBoAW3GBF3gO+mF5Ty
1ddp/XcgLOsmvNNjY+2HOD5F/RX0fs07mWnbD7x+xz7KEKjF+H7ZpkqCwmwCXaf0
iyYyh1852rti3Afw4mDxuVSD7sd9ggvYMc0QHIpQNkD4YWOhNiE1AB0zH57VbUYG
UwIDAQAB
-----END PUBLIC KEY-----
"
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


##### Response 500
```json
{
  "error" : "failed to decode device group data: JSON payload is empty",
  "request_id" : "f7881e82-0492-49fb-b459-795654e7188a"
}
```
___

<a name="devices-id-status-get"></a>
### Check the admission status of a selected device authentication data set
```
GET /devices/{id}/status
```


#### Description
Returns the admission status of a particular device authentication data set.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**id**  <br>*required*|Device authentication data set identifier.|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Successful response - the device's admission status is returned.|[Status](#status)|
|**404**|The device authentication data set was not found.|[Error](#error)|
|**500**|Internal server error.|[Error](#error)|


#### Example HTTP response

##### Response 200
```json
{
  "status" : "accepted"
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

<a name="devices-id-status-put"></a>
### Update the admission status of a selected device
```
PUT /devices/{id}/status
```


#### Description
Changes the given device's admission status.
Valid state transitions:
- 'pending' -> 'accepted'
- 'pending' -> 'rejected'
- 'rejected' -> 'accepted'
- 'accepted' -> 'rejected'


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**id**  <br>*required*|Device authentication data set identifier.|string|
|**Body**|**status**  <br>*required*|New status|[Status](#status)|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|The status of the device authentication data set was successfully updated.|[Status](#status)|
|**400**|The request body is malformed or the state transition is invalid. See error for details.|[Error](#error)|
|**404**|The device authentication data set was not found.|[Error](#error)|
|**500**|Internal server error.|[Error](#error)|


#### Example HTTP request

##### Request body
```json
{
  "status" : "accepted"
}
```


#### Example HTTP response

##### Response 200
```json
{
  "status" : "accepted"
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




<a name="definitions"></a>
## Definitions

<a name="attributes"></a>
### Attributes
Human readable attributes of the device, in the form of a JSON structure.
The attributes are completely vendor-specific, the provided ones are just an example.


|Name|Description|Schema|
|---|---|---|
|**mac**  <br>*optional*|MAC address.|string|
|**sku**  <br>*optional*|Stock keeping unit.|string|
|**sn**  <br>*optional*|Serial number.|string|


<a name="device"></a>
### Device
Device authentication data set descriptor.


|Name|Description|Schema|
|---|---|---|
|**attributes**  <br>*required*| |[Attributes](#attributes)|
|**device_id**  <br>*required*|System assigned device identifier.|string|
|**device_identity**  <br>*required*|Identity data|string|
|**id**  <br>*required*|Authentication data set identifier.|string|
|**key**  <br>*required*|Device public key|string|
|**request_time**  <br>*required*|Server-side timestamp of the request reception.|string (datetime)|
|**status**  <br>*required*|Status of the admission process for device authentication data set|enum (pending, accepted, rejected)|


<a name="error"></a>
### Error
Error descriptor.


|Name|Description|Schema|
|---|---|---|
|**error**  <br>*optional*|Description of the error.|string|
|**request_id**  <br>*optional*|Request ID (same as in X-MEN-RequestID header).|string|


<a name="newdevice"></a>
### NewDevice
New device authentication data set for admission process.


|Name|Description|Schema|
|---|---|---|
|**device_id**  <br>*required*|System-assigned device ID.|string|
|**device_identity**  <br>*required*|The identity data of the device.|string|
|**key**  <br>*required*|Device public key|string|


<a name="status"></a>
### Status
Admission status of device authentication data set.


|Name|Schema|
|---|---|
|**status**  <br>*required*|enum (pending, accepted, rejected)|





