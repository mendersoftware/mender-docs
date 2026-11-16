---
title: Inventory
taxonomy:
    category: docs
---


### Using System and Component attributes in filters

Inventory attributes reported by Systems and their Components are displayed under the `System` section of the device filter attribute selector in the Mender UI. Use these attributes to create filters that evaluate the attributes of Systems and their Components, rather than those of devices, against the filter criteria.

**Some examples of useful attributes filters**

* `manifest_name` - find System devices with a specific Manifest version installed. Useful for monitoring installation rates or for other reasons get an oversight of your fleet of System devices.

* `version` - find System devices where a component is running a certain version. Useful if you, for example, know that a firmware version is vulnerable and you need to check which Systems include is so you can deploy the necessary updates.

* `component_type` - find System devices with a component type as part of their topology. Some Systems are more “advanced” than others and have extra/optional components, a LIDAR (in a vehicle) for example, and this attribute can be be useful in locating them.

* `component_id` - find System devices that include a component id their topology. Similarly to the `component_type` example, some Systems include multiple instances of the same component type. The heating system of a building for example, could be configured with 1 or 2 heating pumps and you can use this attribute to target them (`component_id = "heat_pump_2"`).

* `component_type` and `version` - find System devices with a combination of component type and version. If you, for example, know that only one component types is affected by a vulnerability in a version this combination  can help you narrow down your search.
