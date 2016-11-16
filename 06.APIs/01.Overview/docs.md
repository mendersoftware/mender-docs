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

### Device and Integration APIs

The APIs are split into two types - device and integration. Device APIs are for
device-originating requests, the Integration APIs are management APIs intended
for use by the web UI. 
