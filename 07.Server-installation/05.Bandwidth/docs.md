---
title: Bandwidth
taxonomy:
    category: docs
---

## Artifact download and connection limiting

!!! This section applies only to Mender with Minio storage backend.

When a large number of devices is being updated, the uplink connection of the
backend can easily get saturated. For this reason `storage-proxy` container is
aware of 2 environment variables:

* `MAX_CONNECTIONS` - limits the number of concurrent GET requests. Integer,
  defaults to 100.

* `DOWNLOAD_SPEED` - limits the download speed of proxy response. String,
  defaults to `1m` (1MByte/s). Detailed format description is provided in nginx
  documentation
  of
  [limit_rate](https://nginx.org/en/docs/http/ngx_http_core_module.html#limit_rate?target=_blank) variable

These options can be adjusted using a separate compose file with the following
entry (example limiting download speed to 512kB/s, max 5 concurrent transfers):

```yaml
    storage-proxy:
        environment:
            MAX_CONNECTIONS: 5
            DOWNLOAD_SPEED: 512k
```

