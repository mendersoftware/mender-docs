---
title: Device tiers
taxonomy:
  category: docs
  label: reference
---

Device tiers are a classification system that describes the class of an authenticated device in Mender.
The tier determines how the Mender Server handles the device, including artifact size limits, polling intervals, deployment restrictions, and device count limits within your plan.

## Overview

Mender supports three device tiers:

- **Micro** - Microcontroller units (MCUs) running `mender-mcu`, typically with constrained resources
- **Standard** - Embedded Linux devices running the Mender Client (mender-auth and mender-update)
- **System** - Devices running Mender Orchestrator for coordinated multi-component updates

Each tier is designed to accommodate different device capabilities and use cases.

## Device tier characteristics

### Micro tier

The micro tier is designed for resource-constrained microcontroller units (MCUs).

**Characteristics:**

- Runs `mender-mcu` (typically on Zephyr RTOS)
- Supports firmware updates
- Default update check interval: 604800 seconds (7 days)
- Default inventory update interval: 1209600 seconds (14 days)
- Reduced artifact size limits (10 MiB) due to constrained storage
- Limited feature set compared to standard tier (no delta updates, no state scripts)

**Typical devices:**

- ESP32 microcontrollers
- ARM Cortex-M based MCUs
- Zephyr RTOS devices
- Battery-powered sensors

**Limitations:**

- No delta update support
- No compressed artifacts support
- No signed artifacts support (in preview)
- No advanced update controls using state scripts

### Standard tier

The standard tier is designed for embedded Linux devices with sufficient resources to run a full operating system.

**Characteristics:**

- Runs the Mender Client
- Supports full Operating System updates with A/B partitioning
- Supports Application updates
- Default update check interval: 1800 seconds (30 minutes)
- Default inventory update interval: 28800 seconds (8 hours)
- Maximum artifact size: 10 GiB (default)

**Typical devices:**

- Raspberry Pi
- Industrial gateways
- Smart appliances
- Edge computing devices

### System tier

The system tier is designed for complex devices that need to orchestrate updates across multiple components.

**Characteristics:**

- Runs Mender Orchestrator alongside Mender Client
- Coordinates updates across multiple interdependent components
- Uses Manifest-based deployments with Topology definitions
- Supports both full system updates and partial component updates
- Can manage components over various protocols (CAN bus, I2C, etc.)

**Typical devices:**

- Automotive ECUs with multiple sub-components
- Drones with multiple interconnected modules
- Industrial equipment with distributed control systems
- Complex edge devices with independently versioned software components

**System type vs Device type:**
When a device is configured with the system tier, the Mender Client uses the System type (defined in Mender Orchestrator's Topology) when:

- Polling for deployments
- Installing Manifest Artifacts (payload type `mender-orchestrator-manifest`)

The regular Device type is used in all other cases, allowing a System device to receive both Manifests and regular rootfs updates.

## Device tier limits and restrictions

Tiers have different limits on Artifact sizes and polling intervals.
See [Limits](../18.Limits/docs.md) for the exact limitations.

### Deployment restrictions

Deployments to devices of different tiers may have restrictions:

- **Cross-tier deployments**: You cannot create a deployment that targets devices of different tiers in the same deployment group. Devices must be grouped by tier for deployments.
- **Manifest deployments**: Manifest Artifacts (payload type `mender-orchestrator-manifest`) can only be deployed to devices with the system tier.
- **MCU-specific artifacts**: Firmware artifacts for MCUs should only be deployed to devices with the micro tier.

### Device limits

Your Mender plan has a separate device limit for each tier.
You can purchase more devices for a given tiers at the upgrade page for your account.

The free trial evaluation period includes up to 5 devices of all device tiers.

## Backward compatibility

For backward compatibility, devices that do not specify a tier are automatically assigned the **standard** tier. This ensures that existing deployments continue to work without modification.

If you have devices already connected to Mender before device tiers were introduced:

- They will be treated as standard tier devices
- No action is required unless you want to explicitly set a different tier
- You can change the tier at any time through device configuration

## Setting the device tier

The device tier is set during device authentication and is included in the authentication request sent to the Mender Server.

### Configuration

Configuring the device tier depends on the integration method.
Please consult with the documentation for your integration method for setting the device tier.

- [Yocto Project](../../05.Operating-System-updates-Yocto-Project/05.Customize-Mender/docs.md#configuring-device-tier)
- [Debian](/04.Operating-System-updates-Debian-family/03.Customize-Mender/docs.md#device-tier)
- [Zephyr (MCU)](/06.Operating-System-updates-Zephyr/04.Customize-Mender-mcu/docs.md#device-tier)

### Changing the device tier

When a device changes tier:

1. **New authentication set**: The device creates a new authentication request with the new tier value
2. **Pending state**: The new authentication set enters the "pending" state, awaiting authorization
3. **User approval**: An administrator must authorize the new authentication set through the UI or API,
   or automatically using [mTLS authentication](/10.Server-integration/04.Mender-Gateway/10.Mutual-TLS-authentication/01.Keys-and-certificates/docs.md).
4. **Transition**: Once accepted, the old authentication set is rejected and the device operates with the new tier
5. **Configuration update**: The device configuration (on the device itself) must be updated to send the correct tier in future authentication requests

**Important considerations:**

- Changing tiers requires creating a new authentication set and getting it authorized
- Only one authentication set per device can be in the "accepted" state at a time
- The device must be reconfigured to send the correct tier value
- Deployments should be adjusted to account for the new tier's capabilities and restrictions

!!!! If device tier is not specified, the authentication set is treated as **Standard** device tier.

## Free trial and device tiers

The Mender free trial evaluation period includes:

- 12 months of Mender Enterprise plan access
- Up to 5 devices for each device tier
- No credit card required
- Full access to all features including device tiers

## Moving from free trial to production

When transitioning from the free trial evaluation to production:

1. **Evaluate your device fleet**: Determine how many devices of each tier you need
2. **Choose a plan**: Select a Mender plan that supports your device count, tiers and feature requirements
3. **Upgrade account**: Follow the account upgrade process in the settings of your account or [contact us](mailto:contact@mender.io) for a quote if you need an Enterprise plan.
4. **Scale deployment**: Your existing device configurations and tiers remain unchanged
5. **Monitor limits**: Ensure polling intervals and artifact sizes stay within plan limits

**Key points:**

- Device tier configurations do not need to change during the transition
- All devices (regardless of tier) continue to count toward your plan's device limit
- Production plans may have different limits for artifact sizes, active deployments, and polling intervals
- Consult with Mender for custom plans if you have specific tier or scaling requirements

## Best practices

1. **Choose the right tier**: Match the device tier to the actual device capabilities and use case
2. **Respect polling intervals**: Use the default polling intervals for each tier to avoid rate limiting
3. **Group by tier**: Create deployment groups that align with device tiers for easier management
4. **Test tier transitions**: If changing a device's tier, test the process in a development environment first
5. **Monitor artifact sizes**: Ensure artifacts fit within tier-specific size limits before creating deployments
6. **Document tier decisions**: Keep track of why specific devices are assigned to specific tiers for future reference
