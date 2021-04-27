---
title: Configure
taxonomy:
    category: docs
---

!!!!! The Mender Configure add-on package is required.
!!!!! See [the Mender features page](https://mender.io/plans/features?target=_blank)
!!!!! for an overview of all Mender plans and features.

## Overview

Configure is a Mender add-on package that allows the application of the configuration to the device using Mender.
It is possible to create and apply configuration for the device using Mender UI (see the pictures below).

![configuration-1](deviceconfig1.png)
![configuration-2](deviceconfig2.png)
![configuration-3](deviceconfig3.png)

## How it works

Mender applies configuration in a similar way as software updates.
`deviceconfig` is a microservice on the server responsible for "translating" a configuration change made in the UI into a deployment.
It then proceeds to trigger a deployment to the device using the same mechanism used in OTA, the `deployments` microservice. 

On the device side, a specialized update module is responsible for applying the configuration.
You can find more information about the configuration update module on [Mender Hub](https://hub.mender.io).
The picture below shows the configuration update flow.

![configuration-4](configure1.png)
