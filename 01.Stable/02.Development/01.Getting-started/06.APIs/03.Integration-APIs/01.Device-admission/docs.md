---
title: Device admission
taxonomy:
    category: docs
api: true
---

<a name="overview"></a>
## Overview
An API for managing device admissions. Using this API, devices can be 
'admitted' for use by Mender, or blocked from connecting to Mender.

Devices can have one of three status: 'pending', 'accepted' or 'rejected'.
Once a device is 'accepted', it can connect to Mender and have updates
deployed to it.


### Version information
*Version* : 0.1.0


### URI scheme
*BasePath* : /api/0.1.0



<a name="paths"></a>
## Paths

<a name="devices-post"></a>
### Add a new device for admission
```
POST /devices
```


#### Description
Add a new device to be considered for admission. A new device will be created with status "pending".


#### Parameters

|Type|Name|Description|Schema|Default|
|---|---|---|---|---|
|**Body**|**Device**  <br>*required*|New device for admission|[NewDevice](#newdevice)||


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**201**|New device for admission created  <br>**Headers** :   <br>`Location` (string) : URI for the new created resource.|No Content|
|**400**|Invalid request|[SimpleError](#simpleerror)|
|**500**|Internal Server Error|[SimpleError](#simpleerror)|


#### Example HTTP request

##### Request body
```
json :
{
  "id" : "00a0c91e6-7dec-11d0-a765-f81d4faebf1",
  "device_identity" : "{\"cpuid\":\"12331-ABC\", \"mac\":\"00:11:22:33:44:55\"}",
  "key" : "5f36d271484c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a21"
}
```


#### Example HTTP response

##### Response 500
```
json :
{
  "application/json" : {
    "error" : "Detailed error message"
  }
}
```


<a name="devices-get"></a>
### List devices
```
GET /devices
```


#### Description
Returns a list of all devices for admission. Devices can be filtered by admission status.


#### Parameters

|Type|Name|Description|Schema|Default|
|---|---|---|---|---|
|**Query**|**page**  <br>*optional*|Starting page|number(integer)|`"1"`|
|**Query**|**per_page**  <br>*optional*|Number of results per page|number(integer)|`"10"`|
|**Query**|**status**  <br>*optional*|Filter devices by admission status (pending, accepted, rejected).|enum (pending, accepted, rejected)||


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Successful response  <br>**Headers** :   <br>`Link` (string) : Standard header, we support "first", "next", and "prev".|< [Device](#device) > array|
|**202**|No Content|No Content|
|**400**|Invalid parameters|[SimpleError](#simpleerror)|
|**500**|Internal Server Error|[SimpleError](#simpleerror)|


#### Example HTTP response

##### Response 200
```
json :
{
  "application/json" : [ {
    "id" : "aac4b9924873905243fefbdfa8dee88ae1da57c80579f0d383e53e5f3676e38b",
    "device_identity" : "{\"mac\":\"52:54:00:9f:5f:19\"}",
    "key" : "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA8ykrU+F1T/KIt5LS4S9J\nvyHvl2J8o9TVuKgqy8LfKga0P0rznNY6cvKEqYtuXIfBBWp7Dz+fMANM8GZZGqiq\nZNR5Ke+J4CPrKTEnfBUts/kaFd3NgYyaV8yBLyYbNhxvBFiIJAXOI4XG10CktbCb\n+BUVBpCcRf++a4KCIutp46n6LgsyzPWvLAGIsXYnR8OX0Vy3S56jBXikb/fD/Xqe\nq4N8og6vTQsTk4ZkbqQXK3acGHAg08HWzTPV4vphEzN9u9Mg11UQLbnOUCKYw65l\nnHICIsD+d5aUS09ET6Y78rjvwiH3/abB1MK7g6oSiyqW115lu6lcTO+BumtJEOkD\nHwIDAQAB\n-----END PUBLIC KEY-----\n",
    "status" : "accepted",
    "attributes" : {
      "mac" : "52:54:00:9f:5f:19"
    },
    "request_time\"" : "2016-09-21T07:56:33.474Z"
  }, {
    "id" : "9c25aca9b686e7e9834e72ad9150eeb952264de15acc8445bc54124afbcd70a2",
    "device_identity" : "{\"mac\":\"52:54:00:5b:b1:2b\"}",
    "key" : "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3+as7AjG9gmO7NiVYf5X\nlJKsg2Cr0HzN7vg2Pfh7NqdBmPjKb0mf/UxFqosFfLkS+FMuEfZqojEDodhnNvvG\nsIB7q0aBMwK8JVgtNkrzxMWp0qXMqps9coXMuL9B+onSsnFXHXZUjbNZukNK+ILg\nC9uCIRqL1YXE9XX61cJfQJ3EXXOIENNCjucitVs4+3xyu7+LLjYYXAqK66CCmYA/\nbReOXjbV9o1hPCxvwVBO9+tLOdXZ1oBaB+WQJyeqWPdQ2Y3Sd1eC11EYv4afZUtD\nRSpSW4283q3wJ5mJ+Flqh3rbVA959tUp9dm8S9Uh7I7W6586Zt3SCD5rX/39Ha+P\n9QIDAQAB\n-----END PUBLIC KEY-----\n",
    "status" : "pending",
    "attributes" : {
      "mac" : "52:54:00:5b:b1:2b"
    },
    "request_time\"" : "2016-09-21T07:56:33.474Z"
  } ]
}
```

##### Response 500
```
json :
{
  "application/json" : {
    "error" : "Detailed error message"
  }
}
```


<a name="devices-id-get"></a>
### Get a single device
```
GET /devices/{id}
```


#### Description
Get a single device by its ID.


#### Parameters

|Type|Name|Description|Schema|Default|
|---|---|---|---|---|
|**Path**|**id**  <br>*required*|Device identifier|string||


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Device|[Device](#device)|
|**404**|Not Found|[SimpleError](#simpleerror)|
|**500**|Internal Server Error|[SimpleError](#simpleerror)|


#### Example HTTP response

##### Response 200
```
json :
{
  "application/json" : [ {
    "id" : "9c25aca9b686e7e9834e72ad9150eeb952264de15acc8445bc54124afbcd70a2",
    "device_identity" : "{\"mac\":\"52:54:00:5b:b1:2b\"}",
    "key" : "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3+as7AjG9gmO7NiVYf5X\nlJKsg2Cr0HzN7vg2Pfh7NqdBmPjKb0mf/UxFqosFfLkS+FMuEfZqojEDodhnNvvG\nsIB7q0aBMwK8JVgtNkrzxMWp0qXMqps9coXMuL9B+onSsnFXHXZUjbNZukNK+ILg\nC9uCIRqL1YXE9XX61cJfQJ3EXXOIENNCjucitVs4+3xyu7+LLjYYXAqK66CCmYA/\nbReOXjbV9o1hPCxvwVBO9+tLOdXZ1oBaB+WQJyeqWPdQ2Y3Sd1eC11EYv4afZUtD\nRSpSW4283q3wJ5mJ+Flqh3rbVA959tUp9dm8S9Uh7I7W6586Zt3SCD5rX/39Ha+P\n9QIDAQAB\n-----END PUBLIC KEY-----\n",
    "status" : "pending",
    "attributes" : {
      "mac" : "52:54:00:5b:b1:2b"
    },
    "request_time\"" : "2016-09-21T07:56:33.474Z"
  } ]
}
```


##### Response 404
```
json :
{
  "application/json" : {
    "error" : "Detailed error message"
  }
}
```


##### Response 500
```
json :
{
  "application/json" : {
    "error" : "Detailed error message"
  }
}
```


<a name="devices-id-status-get"></a>
### Checks admission status for the device
```
GET /devices/{id}/status
```


#### Parameters

|Type|Name|Description|Schema|Default|
|---|---|---|---|---|
|**Path**|**id**  <br>*required*|Device identifier|string||


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Admission status of the device|[Status](#status)|
|**404**|Not Found|[SimpleError](#simpleerror)|
|**500**|Internal Server Error|[SimpleError](#simpleerror)|


#### Example HTTP response

##### Response 200
```
json :
{
  "application/json" : {
    "status" : "accepted"
  }
}
```


##### Response 404
```
json :
{
  "application/json" : {
    "error" : "Detailed error message"
  }
}
```


##### Response 500
```
json :
{
  "application/json" : {
    "error" : "Detailed error message"
  }
}
```


<a name="devices-id-status-put"></a>
### Update device admission state
```
PUT /devices/{id}/status
```


#### Description
Allows changing the device's admission status. Valid state transitions
- pending -> accepted
- pending -> rejected
- rejected -> accepted
- accepted -> rejected


#### Parameters

|Type|Name|Description|Schema|Default|
|---|---|---|---|---|
|**Path**|**id**  <br>*required*|Device identifier|string||
|**Body**|**status**  <br>*required*|New status|[Status](#status)||


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Device status updated|[Status](#status)|
|**303**|Device updated  <br>**Headers** :   <br>`Location` (string) : URI of updated device.|No Content|
|**400**|Bad request (including invalid state and/or state transition)|[SimpleError](#simpleerror)|
|**404**|Not Found|[SimpleError](#simpleerror)|
|**500**|Internal Server Error|[SimpleError](#simpleerror)|


#### Example HTTP response

##### Response 400
```
json :
{
  "application/json" : {
    "error" : "Detailed error message"
  }
}
```


##### Response 404
```
json :
{
  "application/json" : {
    "error" : "Detailed error message"
  }
}
```


##### Response 500
```
json :
{
  "application/json" : {
    "error" : "Detailed error message"
  }
}
```





---


<a name="definitions"></a>
## Definitions

<a name="attributes"></a>
### Attributes
Human readable attributes of the device.
Attributes can have more or different properties then defined here.


|Name|Description|Schema|
|---|---|---|
|**SKU**  <br>*optional*|Stock keeping unit  <br>**Example** : `"My Device 1"`|string|
|**SN**  <br>*optional*|Serial Number  <br>**Example** : `"13132313"`|string|
|**mac_address**  <br>*optional*|Device MAC address  <br>**Example** : `"aa:bb:cc:dd:00:11"`|string|


<a name="device"></a>
### Device
Device


|Name|Description|Schema|
|---|---|---|
|**attributes**  <br>*required*||[Attributes](#attributes)|
|**device_identity**  <br>*optional*|Identity data|string|
|**id**  <br>*required*|Hash created based on the device identity data|string|
|**key**  <br>*optional*|Device public key|string|
|**request_time**  <br>*required*|Server-side timestamp of the request reception.|string|
|**status**  <br>*required*|Status of the admission process for the device|enum (pending, accepted, rejected)|


<a name="newdevice"></a>
### NewDevice
New device for admission process


|Name|Description|Schema|
|---|---|---|
|**device_identity**  <br>*required*|Device identity data|string|
|**id**  <br>*required*|Hash created based on the device identity data|string|
|**key**  <br>*required*|Device public key|string|


<a name="simpleerror"></a>
### SimpleError
Simple error descriptor


|Name|Description|Schema|
|---|---|---|
|**error**  <br>*optional*|Description of error|string|


<a name="status"></a>
### Status
Admission status of the device


|Name|Description|Schema|
|---|---|---|
|**status**  <br>*required*||enum (pending, accepted, rejected)|






