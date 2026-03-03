---
title: Caching
taxonomy:
    category: docs
---

Artifact Caching feature optimizes deployments that involve multiple Components sharing the same Artifact. By enabling the cache, Mender Orchestrator avoids redundant network downloads, significantly reducing bandwidth usage and deployment time for complex multi-component updates.

### Overview

When Mender Orchestrator initiates a Component update with caching enabled, it first checks the local cache for the required Artifact. If the Artifact is missing, the Orchestrator begins downloading it from the Mender Server.

To ensure maximum efficiency, the Orchestrator saves the Artifact to the local cache simultaneously while the Artifact is being downloaded by the Component's Interface. This means the cache is populated in real-time as the first Component receives its data.

If any subsequent Components in the same or concurrent deployments require that same Artifact, the Orchestrator serves it directly from the local cache.

When multiple components using the same Artifact are updated simultaneously, they wait until the caching of the required Artifact is finished and use the cached version subsequently.

### Cache persistence and Cleanup

Cached Artifacts stay on the filesystem for the duration of the deployment. To prevent the cache from growing indefinitely, the Orchestrator performs a cleanup at the end of every deployment. An Artifact is removed only after a deployment finishes successfully and the Orchestrator determines that the Artifact was not used by that specific deployment.

### Storage and Fallback

The filesystem hosting the cache must have sufficient free space to store the full Artifact. However, the caching mechanism is designed to be non-blocking. If the Orchestrator cannot cache an Artifact - for example, if the destination filesystem has reached its capacity - it will skip the caching process. The deployment will continue to function normally, ensuring that storage issues do not cause update failures.

### Configuration

Artifact caching is configured in the Mender Orchestrator configuration file, located at `/etc/mender-orchestrator/mender-orchestrator.conf`.

```json
{
  "ArtifactsCache": {
    "Enabled": true,
    "Path": "/var/cache/mender-orchestrator"
  }
}
```

* `Enabled`: Set to true to activate caching. Defaults to false.
* `Path`: The directory where the cached Artifacts are stored.

!!! Note: The path configured for the cache must exist on the filesystem before the Orchestrator starts. The service will not attempt to create the directory structure if it is missing. In this case the deployments will work normally but without the cache.