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

Mender's Multi Tenancy feature ensures that different tenants have completely separate
environments, meaning that each tenant has their own set of users, devices, and device
groups, and only the users associated with a tenant can access its data. This enables
centralized device management at scale across multiple teams or organizations without
compromising on security or data privacy.

Additionally, thanks to the SSO support in Mender Enterprise, it is possible to
ensure that only users authenticated by the organization's Identity Provider can
access any Mender Tenant.


## Tenant isolation

Mender achieves multi tenancy by logically partitioning the platform's resources so
that multiple tenants can use the same underlying infrastructure without interfering
with one another. This setup helps organizations reduce overhead and operational costs,
as they don't need to set up and maintain separate servers for each department or
customer.

Every microservice stores the information about all the Tenants in a single database,
and every record includes the Tenant ID. When retrieving information from the database,
the server filters the records by Tenant ID and returns the data belonging to the
specific Tenant the user or the device belongs to. Similarly, the Mender artifacts
are stored in a common storage account (Azure Blob Storage or AWS S3 bucket) and
prefixed by the Tenant ID. It is also possible to configure a Tenant specific
object store for the artifacts if needed.

Individual billing may be addressed on the Tenant level: Mender Server tracks resource
usage (such as device limits and consumption) per Tenant, enabling cost management
across different clients or teams.

The Mender Server provides monitoring and audit logs capabilities at the Tenant level, 
allowing each Tenant to monitor its own devices and audit logs without visibility 
into other Tenants' environments.


## Typical Use Cases for Multi Tenancy in Mender

The typical use cases for this feature are:

1. *Large Enterprises with Multiple Divisions*: Organizations that have several
departments, subsidiaries, or teams working on different projects can use Mender
Server to isolate device management for each division. For example, an organization
with multiple Business Units focusing on different verticals can keep each Business
Unit and their product lines isolated.

3. *OEMs (Original Equipment Manufacturers)*: OEMs can manage a customer's
environment by adding a user into their Tenant, or they can let a customer
manage their devices and OTA fully themselves, completely isolated from the OEM.

4. *Test and Production Environments*: Multi Tenancy can also be used internally
to separate different environments, such as test, staging, and production
environments. Each environment can have its own set of devices and updates to
ensure that no test data interferes with production systems.


## Service Provider Tenants

![Service Provider](service-provider.png)

In Mender Server Enterprise, Multi Tenancy is managed by a special type of Tenant
called Service Provider Tenant (or SP Tenant). 

Service Provider Tenant acts as a central point of control for all the children
Tenants allowing for organisation wide definition of policies applicable to all
children Tenants (i.e. SSO and features available to child tenants). 

The SP Tenant can:

- Create a child Tenant: Admin users can create multiple Tenants through the
  Mender Enterprise UI or the Management APIs. Each Tenant is assigned a unique
  Tenant ID, Tenant Token and initial administrative account.

- User Management: SP Tenant administrators can create an initial admin for a child
  Tenant which will be responsible for assigning different roles and permissions
  within the child Tenant intself, ensuring proper access control. Each child
  Tenant's users only have access to devices and groups within their own Tenant.
  Optionally, SP Tenant Admins can enable SSO for the children Tenants inheriting
  the configuration from the Service Provider Tenant and map users to specific
  tenants; this way, only users from the organization's Identity Provider can log
  in to the Mender Server accessing the correct Tenant based on their needs.

- Device limit: Set and change device limit of all children Tenants. Allocates
  the overall Device limit of to children Tenants.


## How to enable Multi Tenancy

If you are using hosted Mender Enterprise please
[contact us](https://mender.io/contact-us) for help with migration to a multi
tenant setup using the Service Provider Tenant. For existing Tenants with a
more complex configuration it may be treated as a
[Consulting project](https://mender.io/pricing/mender-extras).

For on-premise installations, you can promote an existing Tenant to a Service Provider Tenant with the following command:

```bash
TENANTID=your-tenant-id-here
tenantadm update-tenant --id "${TENANTID}" --service-provider
```

where `TENANTID` variable holds the ID of the Tenant to promote.
Please note, you have to execute the above command from the inside of the `tenantadm`
container. For on-premise installations you can find the Tenant ID by listing the Tenants using the following command:

```bash
# tenantadm list-tenants  | grep -v loading | jq '.[] | { "tenant id": .id, "tenant name":.name}'
{
  "tenant id": "673a03e3c9eca7a440f2f444",
  "tenant name": "DemoOrganization"
}
{
  "tenant id": "673a0ebbe998e3d46fc010d3",
  "tenant name": "demo5"
}
```

## Service Provider Tenant in the Mender UI

### Managing Tenants

After you log in to the Tenant that is a Service Provider, you will see an empty tenants list: 

![Service provider main view empty](sp0.png)

Starting here you can add a new Tenant:

![Service provider add](sp0-add.png)

And it will appear in the list:

![Service provider add](sp1.png)

Now there are additional operations you can perform on it, by clicking the details link:

![Service provider add](sp1-edit.png)

As you can see, the Mender UI allows the Service Provider Tenant to manage the children Tenants.
Every operation is recorded in the audit logs:

![Service provider add](sp2.png)
