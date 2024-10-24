---
title: Multi Tenancy
taxonomy:
category: docs
---

!!!!! Multi Tenancy is only available in the Mender Enterprise plan.
!!!!! See [the Mender plans page](https://mender.io/pricing/plans?target=_blank)
!!!!! for an overview of all Mender plans and features.

## Introduction

Multi Tenancy is a feature that allows multiple tenants (organizations or teams)
to share a single Mender server infrastructure while keeping their data, users, and
devices isolated from each other. This is especially useful in enterprise environments
where different departments or clients need separate management but can benefit from a
centralized deployment and update management system.


## High-Level Overview

Mender's multitenancy feature ensures that different tenants have completely separate
environments, meaning that each tenant has their own set of users, devices, and device
groups, and only the users associated with a tenant can access its data. This enables
centralized device management at scale across multiple teams or organizations without
compromising on security or data privacy.

Mender achieves multitenancy by logically partitioning the platform's resources so
that multiple tenants can use the same underlying infrastructure without interfering
with one another. This setup helps organizations reduce overhead and operational costs,
as they don't need to set up and maintain separate servers for each department or
customer.


## Typical Use Cases for Multitenancy in Mender

The typical use cases for this feature are:

1. *Managed Service Providers (MSPs)*: A managed service provider can use Mender
Server's multitenancy feature to offer device management services to multiple clients.
Each client would have a separate tenant environment where they can manage their own
fleet of devices, but they all share the same server infrastructure managed by the MSP.

2. *Large Enterprises with Multiple Divisions*: Organizations that have several
departments, subsidiaries, or teams working on different projects can use Mender
Server to isolate device management for each division. For example, an organization
with multiple product lines can keep devices for each product isolated while still
using a central Mender Server instance.

3. *OEMs (Original Equipment Manufacturers)*: OEMs can manage device deployments
for different customers, ensuring each customer has access to their own devices
and updates. Each customer would be a separate tenant, making it easy to handle
updates, deployments, and monitoring while maintaining strict separation of data.

4. *Test and Production Environments*: Multitenancy can also be used internally
to separate different environments, such as test, staging, and production
environments. Each environment can have its own set of devices and updates to
ensure that no test data interferes with production systems.

Mender Server's multitenancy feature is essential for organizations that need to
manage devices across different teams, clients, or environments while sharing the
same infrastructure. It supports scalability, data isolation, and efficient resource
management, making it a key feature for enterprises and managed service providers.


## Service Provider Tenants

In Mender Server Enterprise, Multi Tenancy is available to special Tenants called
Service Provider Tenants (or SP Tenants). These organizations can:

- Create a child Tenant: Admin users can create multiple tenants through the
  Mender Enterprise UI or the Management APIs. Each tenant is assigned a unique
  Tenant ID and Token and set of users, which can be managed independently from
  other tenants.

- User Management: Admins can assign different roles and permissions within
  each children tenant, ensuring proper access control. Each children tenant's
  users only have access to devices and groups within their own tenant.

- Device Assignment: Devices are registered to a specific tenant during the
  provisioning process based on the Tenant Token. Once assigned to a tenant,
  devices cannot be accessed or managed by users in another tenant, ensuring
  data isolation.

- Billing and Resource Usage: In some enterprise setups, billing may be
  associated with tenants. Mender Server can track resource usage (such as device
  limits and consumption) per tenant, enabling cost management across different
  clients or teams.

- Monitoring and Audit Logs: Mender Server provides monitoring and audit logs
  capabilities at the tenant level, allowing each tenant to monitor its own devices
  and audit logs without visibility into other tenants' environments.


## How to enable Multi Tenancy

This feature is currently under development. If you want to know more,
please [contact us](https://mender.io/contact-us).
