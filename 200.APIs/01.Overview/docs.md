---
title: API overview
taxonomy:
    category: docs
---

## Mender APIs


### REST

The Mender API is a RESTful API. This means that the API is designed to allow 
you to get, create, update, & delete objects with the HTTP verbs GET, POST, 
PUT, PATCH, & DELETE. The APIs make use of CORS (cross-origin-request) which 
also uses the OPTIONS request method.

### Device and Management APIs

The APIs are split into two types - *Device* and *Management*. Device APIs are for
device-originating requests, the Management APIs are intended
for use by the UI and other tools that manage devices, Artifacts or deployments
across devices.

### API Versioning

We are constantly working on improving our APIs. In case breaking backwards 
compatibility of the APIs, version number in the URI will be increased.

Following changes are considered backwards-compatible and the API consumers 
should be flexible enough to handle them:
* Adding new endpoints
* Extending existing endpoints with additional attributes.
* Support additional query parameters for existing endpoints.
