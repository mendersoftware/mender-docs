---
title: Open Source API overview
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

### API Versioning and compatibility

The APIs are being continuously reviewed and improved.

The following changes are considered backwards-compatible and users of the APIs
should be flexible enough to handle them:

* Adding new endpoints
* Extending existing endpoints with additional attributes.
* Support additional query parameters for existing endpoints.

If API compatibility needs to be broken at some point, the version number in the URI
will be increased, e.g. from `/api/management/v1/deployments` to 
`/api/management/v2/deployments`. In such cases, both versions will
be supported by the server for some period to allow for graceful transition.
