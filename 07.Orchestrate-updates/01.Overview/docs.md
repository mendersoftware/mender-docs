---
title: Overview
taxonomy:
    category: docs
---

!! This section is a preview of Mender's support for Orchestrated updates using mender-orchestrator. It is not yet recommended for production use. Also, expect the APIs and configurations to evolve as the implementation matures.

Mender Orchestrator is the software responsible for updating the Components in a System.
It is responsible for inspecting the System's current state, such as the software versions running on the Components. The System's architecture is defined by the [Topology](../02.Topology/docs.md),
which specifies what Components are present and how they can be updated. The Orchestrator reads the System's desired state from a [Manifest](../03.Manifest/docs.md), which defines the exact combination
of Artifacts that should be deployed to each Component type and controls the update strategy. The Orchestrator then applies the changes to the different Components to reach the state described in the Manifest.
If this is not possible, the Orchestrator may roll back to the previously known working state, in other words, the previous version of the Manifest.
