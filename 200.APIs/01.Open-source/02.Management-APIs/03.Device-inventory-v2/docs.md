---
title: Device inventory filters and search
taxonomy:
    category: docs
api: true
template: docs
---

<a name="overview"></a>
## Overview
An API for inventory-based filters management and device search.
It is intended for use by the web GUI.

Devices can upload vendor-specific attributes (software/hardware info, health checks, metrics, etc.) of various data types to the backend as scoped attributes.

This API enables the user to:
* search devices by inventory scoped attribute value
* use the results to create and manage device groups for deployment scheduling


### Version information
*Version* : 1


### URI scheme
*Host* : hosted.mender.io  
*BasePath* : /api/management/v2/inventory  
*Schemes* : HTTPS




<a name="paths"></a>
## Paths
- [POST/filters/search](#filters-search-post)


___
<a name="filters-search-post"></a>
### Search devices based on inventory attributes
```
POST /filters/search
```


#### Description
Returns a paged collection of devices and their attributes.

It accepts optional filters and sort parameters as body parameters.


#### Parameters

|Type|Name|Description|Schema|
|---|---|---|---|
|**Header**|**Authorization**  <br>*required*|Contains the JWT token issued by the User Administration and Authentication Service.|string (Bearer [token])|
|**Body**|**body**  <br>*optional*|The search and sort parameters of the filter|[body](#filters-search-post-body)|

<a name="filters-search-post-body"></a>
**body**

|Name|Description|Schema|
|---|---|---|
|**filters**  <br>*optional*|List of filter predicates, chained with boolean AND operators to build the search condition definition.|< [FilterPredicate](#filterpredicate) > array|
|**page**  <br>*optional*|Starting page.|number (integer)|
|**per_page**  <br>*optional*|Maximum number of results per page.|number (integer)|
|**sort**  <br>*optional*|List of ordered sort criterias|< [SortCriteria](#sortcriteria) > array|


#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|Successful response.  <br>**Headers** :   <br>`Link` (string) : Standard header, used for page navigation.<br><br>Supported relation types are 'first', 'next' and 'prev'.  <br>`X-Total-Count` (string) : Custom header indicating the total number of devices for the given query parameters.|< [Device](#device) > array|
|**400**|Missing or malformed request parameters. See error for details.|[Error](#error)|
|**500**|Internal error.|[Error](#error)|


#### Consumes

* `application/json`


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




<a name="definitions"></a>
## Definitions

<a name="attribute"></a>
### Attribute
Attribute descriptor.


|Name|Description|Schema|
|---|---|---|
|**description**  <br>*optional*|Attribute description.|string|
|**name**  <br>*required*|A human readable, unique attribute ID, e.g. 'device_type', 'ip_addr', 'cpu_load', etc.|string|
|**scope**  <br>*required*|The scope of the attribute.<br><br>Scope is a string and acts as namespace for the attribute name.|string|
|**value**  <br>*required*|The current value of the attribute.<br><br>Attribute type is implicit, inferred from the JSON type.<br><br>Supported types: number, string, array of numbers, array of strings.<br>Mixed arrays are not allowed.|string|


<a name="device"></a>
### Device

|Name|Description|Schema|
|---|---|---|
|**attributes**  <br>*optional*|A list of attribute descriptors.|< [Attribute](#attribute) > array|
|**id**  <br>*optional*|Mender-assigned unique ID.|string|
|**updated_ts**  <br>*optional*|Timestamp of the most recent attribute update.|string|


<a name="error"></a>
### Error
Error descriptor.


|Name|Description|Schema|
|---|---|---|
|**error**  <br>*optional*|Description of the error.|string|
|**request_id**  <br>*optional*|Request ID (same as in X-MEN-RequestID header).|string|


<a name="filterpredicate"></a>
### FilterPredicate
Attribute filter predicate


|Name|Description|Schema|
|---|---|---|
|**attribute**  <br>*optional*|Name of the attribute to be queried for filtering.|string|
|**scope**  <br>*required*|The scope of the attribute.<br><br>Scope is a string and acts as namespace for the attribute name.|string|
|**type**  <br>*required*|Type or operator of the filter predicate.|enum ($eq)|
|**value**  <br>*optional*|The value of the attribute to be used in filtering.<br><br>Attribute type is implicit, inferred from the JSON type.<br><br>Supported types: number, string, array of numbers, array of strings.<br>Mixed arrays are not allowed.|string|


<a name="sortcriteria"></a>
### SortCriteria
Sort criteria definition


|Name|Description|Schema|
|---|---|---|
|**attribute**  <br>*required*|Name of the attribute to be queried for filtering.|string|
|**order**  <br>*required*|Order direction, ascending or descending.<br><br>Defaults to ascending.|enum (asc, desc)|
|**scope**  <br>*required*|The scope of the attribute.<br><br>Scope is a string and acts as namespace for the attribute name.|string|





