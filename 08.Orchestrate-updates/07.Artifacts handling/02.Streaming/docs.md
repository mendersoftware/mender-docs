---
title: Streaming
taxonomy:
    category: docs
---
Artifact streaming allows Mender Orchestrator to pass data directly to a Component's Interface as it is being downloaded from the Mender Server. Instead of downloading and storing the entire Artifact before beginning the installation, the Orchestrator opens a "streams tree" of named pipes that the Interface can read in real-time.

Streaming is particularly valuable for Mender Orchestrator because orchestrated updates often involve multiple Components, each requiring its own Artifact. In a complex system with many components, downloading and storing every Artifact in full before installation significantly increases the risk of running out of local disk space.

By using the streaming interface, you can install large updates even on systems with limited storage, as the data is passed through the Orchestrator without being written to a temporary directory first.

### Usage

For documentation on how to use this feature, see [Streams tree](../../04.Interface-protocol/docs.md#streams-tree).

### Interaction with Artifact caching

If [Artifact Caching](../01.Caching/docs.md) is enabled, the Orchestrator manages both processes simultaneously. Even when an Interface is streaming the data from the pipes in the streams directory, the Orchestrator will still save the Artifact to the local cache. 

Because caching requires dedicated disk space, enabling it will partially negate the storage-saving benefits of streaming: one copy of the Artifact will be cached, in contrast to multiple copies (one per Component) when streaming is not used.

However, if there is not enough free disk space to accommodate the cache, the caching step is automatically omitted and the deployment continues to stream normally. See [Storage and Fallback](../01.Caching/docs.md#storage-and-fallback) for more information.