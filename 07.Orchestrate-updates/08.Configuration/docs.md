---
title: Configuration
taxonomy:
    category: docs
---

Mender Orchestrator's configuration resides in
`/etc/mender-orchestrator/mender-orchestrator.conf` on the root filesystem. This
file is JSON structured and defines various parameters for the Orchestrator's
operation.

On systems where one or more of the configuration options must survive future
updates, there is an optional "fallback" configuration file in
`/var/lib/mender-orchestrator/mender-orchestrator.conf`. Because the directory
`/var/lib/mender-orchestrator` is on persistent storage, the fallback configuration
file is not overwritten by system updates.

The fallback configuration file has the same JSON structure as the main
configuration file. Any value set in the main configuration file
`/etc/mender-orchestrator/mender-orchestrator.conf` takes precedence, whether or
not the setting appears in the fallback file
`/var/lib/mender-orchestrator/mender-orchestrator.conf`. The Orchestrator only uses
a setting from the fallback file if it does not appear in the main file.

## Example mender-orchestrator.conf file

Here is an example of a `mender-orchestrator.conf` file:

```json
{
  "LogLevel": "info",
  "ArtifactsCache": {
    "Enabled": true,
    "Path": "/var/cache/mender-orchestrator",
    "MaxSizeBytes": 2147483648
  }
}
```

For a full list of available options, see
[Configuration options](50.Configuration-options/docs.md).

## Environment variables

The following table describes the environment variables Mender Orchestrator
respects:

| Environment variable                          | Description                                        | Default value                    |
| --------------------------------------------- | -------------------------------------------------- | -------------------------------- |
| `MENDER_ORCHESTRATOR_CONF_DIR`                | Configuration directory                            | `/etc/mender-orchestrator`       |
| `MENDER_ORCHESTRATOR_DATA_DIR`                | Data directory (interfaces, static files)          | `/usr/share/mender-orchestrator` |
| `MENDER_ORCHESTRATOR_DATASTORE_DIR`           | Persistent datastore directory                     | `/var/lib/mender-orchestrator`   |
| `MENDER_ORCHESTRATOR_TOPOLOGY_DIR`            | Directory where the Topology is stored             | Value of datastore directory     |
| `MENDER_ORCHESTRATOR_TOPOLOGY_COMPONENTS_FILE`| Path to the user-provided Topology components YAML | empty                            |
| `MENDER_ORCHESTRATOR_MANIFEST_STORE_DIR`      | Manifest storage directory                         | `{datastore}/manifests`          |
| `MENDER_ORCHESTRATOR_ARTIFACTS_CACHE_DIR`     | Artifacts cache directory                          | `{datastore}/artifacts`          |
| `HTTP_PROXY`                                  | Proxy server to use for HTTP                       | empty                            |
| `HTTPS_PROXY`                                 | Proxy server to use for HTTPS                      | empty                            |
| `NO_PROXY`                                    | Hosts that should not go through proxy             | empty                            |
