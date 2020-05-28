---
title: Bandwidth
taxonomy:
    category: docs
    label: guide
---

## Artifact download and connection limiting

!!! This section applies only to Mender with Minio as an S3 storage backend.

When you update many devices, the up-link connection of the
backend can easily get saturated. In order to control the number
of connections and download speed, the `storage-proxy` container uses 2 environment
variables:

* `MAX_CONNECTIONS` - limits the number of concurrent GET requests. Integer,
  defaults to 100.

* `DOWNLOAD_SPEED` - limits the download speed of proxy response. String,
  defaults to `1m` (1MByte/s). You can find a detailed format description
  in nginx documentation of [limit_rate](https://nginx.org/en/docs/http/ngx_http_core_module.html#limit_rate) variable

You can adjust these options using a separate compose file with the following
entry (example limiting download speed to 512kB/s, max 5 concurrent transfers):

```yaml
    storage-proxy:
        environment:
            MAX_CONNECTIONS: 5
            DOWNLOAD_SPEED: 512k
```

