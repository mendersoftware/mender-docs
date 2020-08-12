---
title: Device authentication
taxonomy:
    category: docs
api: true
template: docs
---

<a name="overview"></a>
## Overview
An API for device authentication handling.


### Version information
*Version* : 2


### URI scheme
*Host* : mender-device-auth:8080  
*BasePath* : /api/management/v2/devauth/  
*Schemes* : HTTP




<a name="paths"></a>
## Paths
- [POST/devices](#devices-post)
- [GET/devices](#devices-get)
- [GET/devices/count](#devices-count-get)
- [GET/devices/{id}](#devices-id-get)
- [DELETE/devices/{id}](#devices-id-delete)
- [DELETE/devices/{id}/auth/{aid}](#devices-id-auth-aid-delete)
- [GET/devices/{id}/auth/{aid}/status](#devices-id-auth-aid-status-get)
- [PUT/devices/{id}/auth/{aid}/status](#devices-id-auth-aid-status-put)
- [GET/limits/max_devices](#limits-max_devices-get)
- [DELETE/tokens/{id}](#tokens-id-delete)


___
<a name="devices-post"></a>
### Submit a preauthorized device.
```
POST /devices
```


#### Description
Adds a given device/authentication data set in the 'preauthorized' state. The device identity data set must not yet exist in the DB (regardless of status).

When the device requests authentication from deviceauth the next time, it will be issued a token without further user intervention.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Body**|**pre_auth_request**  <br>*required*|Preauthentication request.|[PreAuthSet](#preauthset)|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**201**|Device submitted.|No Content|
|**400**|Missing/malformed request params.|[Error](#error)|
|**409**|Device already exists. Response contains conflicting device.|[Device](#device)|
|**500**|Unexpected error|[Error](#error)|


#### Example HTTP request

##### Request body
```json
{
  "identity_data" : {
    "application/json" : {
      "mac" : "00:01:02:03:04:05",
      "sku" : "My Device 1",
      "sn" : "SN1234567890"
    }
  },
  "pubkey" : "-----BEGIN PUBLIC KEY-----
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
___

<a name="devices-get"></a>
### Get a list of tenant's devices.
```
GET /devices
```


#### Description
Provides a list of tenant's devices, sorted by creation date, with optional device status filter.


#### Parameters

|Type|Name|Description|Schema|Default|
|---|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])| |
|**Query**|**page**  <br>*optional*|Results page number|number (integer)|`1`|
|**Query**|**per_page**  <br>*optional*|Number of results per page|number (integer)|`20`|
|**Query**|**status**  <br>*optional*|Device status filter. If not specified, all devices are listed.|enum (pending, accepted, rejected, preauthorized)| |


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|An array of devices.  <br>**Headers** :   <br>`Link` (string) : Standard header, we support 'first', 'next', and 'prev'.|< [Device](#device) > array|
|**400**|Missing/malformed request params.|[Error](#error)|
|**500**|Unexpected error|[Error](#error)|
___

<a name="devices-count-get"></a>
### Get a count of devices, optionally filtered by status.
```
GET /devices/count
```


#### Description
Provides a list of devices, optionally filtered by status.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Query**|**status**  <br>*optional*|Device status filter, one of 'pending', 'accepted', 'rejected'. Default is 'all devices'.|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Device count.|[Count](#count)|
|**400**|Missing/malformed request params.|[Error](#error)|
|**500**|Unexpected error|[Error](#error)|


#### Example HTTP response

##### Response 200
```json
{
  "count" : "42"
}
```
___

<a name="devices-id-get"></a>
### Get a particular device.
```
GET /devices/{id}
```


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**id**  <br>*required*|Device identifier|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Device found.|[Device](#device)|
|**404**|Device not found.|[Error](#error)|
|**500**|Unexpected error|[Error](#error)|
___

<a name="devices-id-delete"></a>
### Decommission device
```
DELETE /devices/{id}
```


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**id**  <br>*required*|Device identifier.|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**204**|Device decommissioned.|No Content|
|**404**|Device not found|[Error](#error)|
|**500**|Internal server error.|[Error](#error)|
___

<a name="devices-id-auth-aid-delete"></a>
### Remove the device authentication set
```
DELETE /devices/{id}/auth/{aid}
```


#### Description
Removes the device authentication set.
Removing 'accepted' authentication set is equivalent
to rejecting device and removing authentication set.
If there is only one authentication set for the device
and the device is 'preauthorized' then the device
will also be deleted.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**aid**  <br>*required*|Authentication data set identifier.|string|
|**Path**|**id**  <br>*required*|Device identifier.|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**204**|Device authentication set deleted.|No Content|
|**404**|Device authentication set not found|[Error](#error)|
|**500**|Internal server error.|[Error](#error)|
___

<a name="devices-id-auth-aid-status-get"></a>
### Get the device authentication set status
```
GET /devices/{id}/auth/{aid}/status
```


#### Description
Returns the status of a particular device authentication data set.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**aid**  <br>*required*|Authentication data set identifier.|string|
|**Path**|**id**  <br>*required*|Device identifier.|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|successful response - the device's authentication set status is returned.|[Status](#status)|
|**404**|The device was not found.|[Error](#error)|
|**500**|Internal server error.|[Error](#error)|


#### Example HTTP response

##### Response 200
```json
{
  "status" : "accepted"
}
```
___

<a name="devices-id-auth-aid-status-put"></a>
### Update the device authentication set status
```
PUT /devices/{id}/auth/{aid}/status
```


#### Description
Sets the status of a authentication data set of selected value.
Valid state transitions:
- 'pending' -> 'accepted'
- 'pending' -> 'rejected'
- 'rejected' -> 'accepted'
- 'accepted' -> 'rejected'


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Path**|**aid**  <br>*required*|Authentication data set identifier.|string|
|**Path**|**id**  <br>*required*|Device identifier.|string|
|**Body**|**status**  <br>*required*|New status.|[Status](#status)|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**204**|The device authentication data set status was successfully updated.|No Content|
|**400**|Bad request.|[Error](#error)|
|**404**|The device was not found.|[Error](#error)|
|**422**|Request cannot be fulfilled e.g. due to exceeded limit on maximum accepted devices (see error message).|[Error](#error)|
|**500**|Internal server error.|[Error](#error)|


#### Example HTTP request

##### Request body
```json
{
  "status" : "accepted"
}
```
___

<a name="limits-max_devices-get"></a>
### Obtain limit of accepted devices.
```
GET /limits/max_devices
```


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and<br>Authentication Service.|string (Bearer [token])|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Usage statistics and limits.|[Limit](#limit)|
|**500**|Internal server error.|[Error](#error)|


#### Example HTTP response

##### Response 200
```json
{
  "limit" : 123
}
```
___

<a name="tokens-id-delete"></a>
### Delete device token
```
DELETE /tokens/{id}
```


#### Description
Deletes the token, effectively revoking it. The device must
apply for a new one with a new authentication request.
The token 'id' corresponds to the standard 'jti' claim.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Path**|**id**  <br>*required*|Unique token identifier('jti').|string|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**204**|The token was successfully deleted.|No Content|
|**404**|The token was not found.|[Error](#error)|
|**500**|Internal server error.|[Error](#error)|




<a name="definitions"></a>
## Definitions

<a name="authset"></a>
### AuthSet
Authentication data set


|Name|Description|Schema|
|---|---|---|
|**id**  <br>*optional*|Authentication data set ID.|string|
|**identity_data**  <br>*optional*| |[IdentityData](#identitydata)|
|**pubkey**  <br>*optional*|The device's public key, generated by the device or pre-provisioned by the vendor.|string|
|**status**  <br>*optional*| |enum (pending, accepted, rejected, preauthorized)|
|**ts**  <br>*optional*|Created timestamp|string (datetime)|


<a name="count"></a>
### Count
Counter type


|Name|Description|Schema|
|---|---|---|
|**count**  <br>*optional*|The count of requested items.|integer|


<a name="device"></a>
### Device

|Name|Description|Schema|
|---|---|---|
|**auth_sets**  <br>*optional*| |< [AuthSet](#authset) > array|
|**created_ts**  <br>*optional*|Created timestamp|string (datetime)|
|**decommissioning**  <br>*optional*|Devices that are part of ongoing decomissioning process will return True|boolean|
|**id**  <br>*optional*|Mender assigned Device ID.|string|
|**identity_data**  <br>*optional*| |[IdentityData](#identitydata)|
|**status**  <br>*optional*| |enum (pending, accepted, rejected, preauthorized)|
|**updated_ts**  <br>*optional*|Updated timestamp|string (datetime)|


<a name="error"></a>
### Error
Error descriptor


|Name|Description|Schema|
|---|---|---|
|**error**  <br>*optional*|Description of the error|string|


<a name="identitydata"></a>
### IdentityData
Device identity attributes, in the form of a JSON structure.

The attributes are completely vendor-specific, the provided ones are just an example.
In reference implementation structure contains vendor-selected fields,
such as MACs, serial numbers, etc.


|Name|Description|Schema|
|---|---|---|
|**mac**  <br>*optional*|MAC address.|string|
|**sku**  <br>*optional*|Stock keeping unit.|string|
|**sn**  <br>*optional*|Serial number.|string|


<a name="limit"></a>
### Limit
Limit definition


|Name|Schema|
|---|---|
|**limit**  <br>*required*|integer|


<a name="preauthset"></a>
### PreAuthSet

|Name|Description|Schema|
|---|---|---|
|**identity_data**  <br>*required*| |[IdentityData](#identitydata)|
|**pubkey**  <br>*required*|The device's public key, generated by the device or pre-provisioned by the vendor.|string|


<a name="status"></a>
### Status
Admission status of the device.


|Name|Schema|
|---|---|
|**status**  <br>*required*|enum (pending, accepted, rejected)|





