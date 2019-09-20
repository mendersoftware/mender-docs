---
title: Enterprise
taxonomy:
    category: docs
---

This is a step by step guide for deploying the Mender Enterprise Server for
production environments, and will focus on the Enterprise specific parts of the
installation.

## Prerequisites

- All [prerequisites for the Open Source edition](..#prerequisites) apply to the
  Enterprise edition as well
- Docker configuration logged into the Mender Enterprise Docker registry:
  ```bash
  docker login -u=<USERNAME> docker.download.mender.io
  ```
  Replace `<USERNAME>` with the username from your Mender Enterprise
  account. This gives a prompt:
  > ```
  > Password: <TYPE PASSWORD HERE>
  > ```

## Deployment steps

The Enterprise Mender server builds upon the Open Source server, and therefore a
large part of the configuration is the same. Just like the Open Source guide,
this guide will use a publicly available Mender integration repository. Then
proceed with setting up a local branch, preparing deployment configuration from
a template, committing the changes locally. Keeping deployment configuration in
a git repository ensures that the history of changes is tracked and subsequent
updates can be easily applied.

At the end of this guide you will have:

- production configuration in a single `docker-compose` file
- a running Mender backend cluster
- persistent service data is stored in Docker volumes:
  - artifact storage
  - MongoDB data
- SSL certificate for the API Gateway
- SSL certificate for the Storage Proxy
- a set of keys for generating and validating access tokens

Consult the section on [certificates and keys](../certificates-and-keys) for details on
how the certificates and keys are used in the system.

#### Docker compose naming scheme

`docker-compose` implements a particular naming scheme for containers, volumes
and networks that prefixes each object it creates with project name. By default,
the project is named after the directory the main compose file is located in.
The production configuration template provided in the repository explicitly sets
project name to `menderproduction`.

`docker-compose` automatically assigns a
`com.docker.compose.project=menderproduction` label to the created containers. The
label can be used when filtering output of commands such as `docker ps`.

### Basic configuration

In this initial step we will use the Open Source guide to set up the main
configuration. Once the Open Source parts of the server are set up, we will
return to the Enterprise guide to enable and set up the Enterprise features of
the server.

Please proceed to [the Basic Preparation Setup of the Open Source
guide](..#basic-preparation-setup) to start the setup. There will be a
notification when it is time to go back to the Enterprise guide.

### Configuring Enterprise

Once the Open Source parts of the configuration have been completed, you should
have a fully functional server setup, except that it has not been launched
yet. It is now time to configure the Enterprise specific features before
bringing the server up.

1. Make sure you are in the production folder:
   ```
   cd production
   ```

2. Copy the `enterprise.yml.template` file to its production location,
   `enterprise.yml`:
   ```
   cp config/enterprise.yml.template config/enterprise.yml
   ```

Creating the `enterprise.yml` file enables the Enterprise Mender server.

### First launch of the server

Bring up the server in detached mode using the following command inside the
`production` folder:

```bash
./run up -d
```

> ```
> Creating network "menderproduction_mender" with the default driver
> Creating menderproduction_mender-api-gateway_1 ... done
> Creating menderproduction_mender-conductor_1 ... done
> Creating menderproduction_mender-deployments_1 ... done
> Creating menderproduction_mender-device-auth_1 ... done
> Creating menderproduction_mender-elasticsearch_1 ... done
> Creating menderproduction_mender-email-sender_1 ... done
> Creating menderproduction_mender-gui_1 ... done
> Creating menderproduction_mender-inventory_1 ... done
> Creating menderproduction_mender-mongo_1 ... done
> Creating menderproduction_mender-org-welcome-email-preparer_1 ... done
> Creating menderproduction_mender-redis_1 ... done
> Creating menderproduction_mender-tenantadm_1 ... done
> Creating menderproduction_mender-useradm_1 ... done
> Creating menderproduction_minio_1 ... done
> Creating menderproduction_storage-proxy_1 ... done
> ```

Note that even though this launches the backend services, the Mender Enterprise
server is not fully functional yet. Running the server is necessary for some of
the upcoming steps.


### Multi tenancy

Multi tenancy is a feature of Mender where users can be divided into groups
called "organizations" (also sometimes called "tenants"). Each organization is
confined and can not see or influence the data of other organizations. This can
be used for example to give two different product teams access to the Mender
service, without them seeing each others data.

When using Mender Enterprise, multi tenancy is automatically enabled, and it
cannot be turned off. However, since multi tenancy is not desirable in all
situations, a default organization can be specified, which makes using this one
organization transparent. See the section on [using a default
organization](#option-1-using-a-default-organization) for more information.

Below follows a guide for setting up a basic, working multi tenancy
configuration. For additional information on administering organizations, see
the [API for the tenantadm service (TODO!)](TODO), as well as the help screen
from:

```bash
./run exec mender-tenantadm /usr/bin/tenantadm --help`
```

#### Creating the first organization and user

In either case, at least one organization must be created when first installing
the service. Execute this command in the `integration/production` directory:

```bash
./run exec mender-tenantadm /usr/bin/tenantadm create-org --name=MyOrganization --username=myusername@host.com --password=mysecretpassword
```

Replace the organization name, username and password with desired values. Make
sure to save the **tenant ID** that appears after calling the command; this will
be the identifier for the first organization. Creating additional organizations
works exactly the same way, so the above step may be repeated multiple times.

Now fetch the **tenant token** for the new organization by calling:

```
./run exec mender-tenantadm /usr/bin/tenantadm get-tenant --id TENANT_ID
```

where `TENANT_ID` is the ID that was printed by the previous command. This will
produce JSON output, and the **tenant token** is in the `tenant_token`
field. See the example in bold:

> {"id":"5d833532d13058002848ffdf","name":"MyTenant","tenant_token":"**eyJhbGciOiJSUzI1NiIsInR5cCI6I<br>
kpXVCJ9.eyJtZW5kZXIudGVuYW50IjoiNWQ4MzM1MzJkMTMwNTgwMDI4NDhmZmRmIiwiaXNzIjoiTWVuZGVyIiwic3ViIjoiNWQ4<br>
MzM1MzJkMTMwNTgwMDI4NDhmZmRmIn0.HJDGHzqZqbosAYyJpSIEeL0W4HMiOmb15ETnuChxE0i7ahW49dZZlQNJBKLkLzuESDxX<br>
nmQbQwsSGP6t32pGkeHVXTPjrSjhtMPC80NiibNG3f-QATw9I8YgG2SBd5xaKl17qdta1nGi80T2UKrwlzqLHR7wNed10ss3NgJD<br>
IDvrm89XO0Rg6jpFZsHCPyyK1c8-Vn8zZjW5azZLNSgtgSLSmFQguQLRRXL2x12VEcmeztFY0kJnhGtN07CD3XXxcz0BpWbevDYO<br>
POEUusGd2KpLK2Y4QU8RdngqNtRe7SppG0fn6m6tKiifrPDAv_THCEG6dvpMHyIM77vGIPwvV4ABGhZKRAlDe1R4csJQIbhVcTWM<br>
GcoZ4bKH-zDK0900_wWM53i9rkgNFDM470i6-d1oqfaCPcbiniKsq1HcJRZsIVNJ1edDovhQ6IbffPRCw-Au_GlnPTn_czovJqSa<br>
3bgwrJguYRIKJGWhHgx0e3j795oJ08ks2Mp3Rshbv4da**","status":"active"}

Make sure the qoutes are not included! If you have the `jq` tool installed, you
can get the token directly by calling:

```
./run exec mender-tenantadm /usr/bin/tenantadm get-tenant --id TENANT_ID | jq -r .tenant_token
```

> eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW5kZXIudGVuYW50IjoiNWQ4MzM1MzJkMTMwNTgwMDI4NDhmZmRmIiwia<br>
XNzIjoiTWVuZGVyIiwic3ViIjoiNWQ4MzM1MzJkMTMwNTgwMDI4NDhmZmRmIn0.HJDGHzqZqbosAYyJpSIEeL0W4HMiOmb15ETnu<br>
ChxE0i7ahW49dZZlQNJBKLkLzuESDxXnmQbQwsSGP6t32pGkeHVXTPjrSjhtMPC80NiibNG3f-QATw9I8YgG2SBd5xaKl17qdta1<br>
nGi80T2UKrwlzqLHR7wNed10ss3NgJDIDvrm89XO0Rg6jpFZsHCPyyK1c8-Vn8zZjW5azZLNSgtgSLSmFQguQLRRXL2x12VEcmez<br>
tFY0kJnhGtN07CD3XXxcz0BpWbevDYOPOEUusGd2KpLK2Y4QU8RdngqNtRe7SppG0fn6m6tKiifrPDAv_THCEG6dvpMHyIM77vGI<br>
PwvV4ABGhZKRAlDe1R4csJQIbhVcTWMGcoZ4bKH-zDK0900_wWM53i9rkgNFDM470i6-d1oqfaCPcbiniKsq1HcJRZsIVNJ1edDo<br>
vhQ6IbffPRCw-Au_GlnPTn_czovJqSa3bgwrJguYRIKJGWhHgx0e3j795oJ08ks2Mp3Rshbv4da

!!! On Debian based distributions you can install `jq` with the command `apt-get
!!! install jq`.

The tenant token will be used the following sections.

#### Choosing organization configuration

An organization configuration must be chosen before the server is fully
functional, and there are two configurations to choose from:

1. Default organization configuration
2. Tenant token configuration

By specifying a default organization, devices will be able to register with the
specified default organization, without a tenant token. With a tenant token
configuration, each device needs a **tenant token** which enables it to register
in that organization's account.

The general recommendation is to use option number 2, tenant token
configuration. However, option 1, default organization configuration, is
sometimes more appropriate, and there are usually two reasons to use this:

* You are upgrading from the Open Source version of Mender
* You don't need multiple organizations and wish to use only one, and you don't
  wish to provide a tenant token in the device configuration.

**Note:** Even when only one organization is going to be used, the
recommendation is to use the tenant token configuration. This ensures a smooth
upgrade path if you later decide to use multiple organizations. It also gives a
small security benefit, by completely blocking devices that don't have a tenant
token.

#### Option 1: Using a default organization

If you are not going to use a default organization, you can skip this section
and proceed to the section on [using a tenant
token](#option-2-using-a-tenant-token).

To specify a default organization:

1. Stop the services by calling `./run down`

2. In `config/enterprise.yml`, locate the `DEVICEAUTH_DEFAULT_TENANT_TOKEN`
   variable, and make sure its value is set to the **tenant token** that was
   fetched in the previous section

3. Start the services again with `./run up -d`

#### Option 2: Using a tenant token

If you configured a default organization above, then this section can be skipped
unless you want more organizations in addition to the default one.

First, make sure you have fetched the tenant token as described
[earlier](#creating-the-first-organization-and-user). You can repeat the steps
for multiple organizations if you need to. The **tenant token** needs to be
included in the client configuration of each device that is going to be managed
by Mender. Exactly how to include the token depends on which integration method
is used with the client. Please refer to one of these sections:

* [Mender installed on device using a deb
  package](../../../client-configuration/installing#configuration-for-hosted-mender-server)
* [Device integration using Yocto
  Project](../../../artifacts/yocto-project/variables#mender_tenant_token)
* [Device integration with Debian
  Family](../../../artifacts/debian-family#convert-a-raw-disk-image)
* [Modifying an existing prebuilt
  image](../../../artifacts/modifying-a-mender-artifact#changing-the-mender-server)

No further configuration is needed on the server to use a tenant token on the
clients.


## Verification

To verify that the services are running, execute the following command and
verify that the state of all services is "Up":

```bash
./run ps
```

> ```
>                         Name                                      Command               State           Ports          
> ----------------------------------------------------------------------------------------------------------------------
> menderproduction_mender-api-gateway_1                  /entrypoint.sh                   Up      0.0.0.0:443->443/tcp
> menderproduction_mender-conductor_1                    /srv/start_conductor.sh          Up      8080/tcp, 8090/tcp
> menderproduction_mender-deployments_1                  /entrypoint.sh --config /e ...   Up      8080/tcp
> menderproduction_mender-device-auth_1                  /usr/bin/deviceauth --conf ...   Up      8080/tcp
> menderproduction_mender-elasticsearch_1                /docker-entrypoint.sh elas ...   Up      9200/tcp, 9300/tcp
> menderproduction_mender-email-sender_1                 /usr/bin/entrypoint.sh           Up
> menderproduction_mender-gui_1                          /entrypoint.sh nginx             Up      80/tcp
> menderproduction_mender-inventory_1                    /usr/bin/inventory --confi ...   Up      8080/tcp
> menderproduction_mender-mongo_1                        docker-entrypoint.sh mongod      Up      27017/tcp
> menderproduction_mender-org-welcome-email-preparer_1   /usr/bin/entrypoint.sh           Up
> menderproduction_mender-redis_1                        /redis/entrypoint.sh             Up      6379/tcp
> menderproduction_mender-tenantadm_1                    /usr/bin/tenantadm --confi ...   Up      8080/tcp
> menderproduction_mender-useradm_1                      /usr/bin/useradm-enterpris ...   Up      8080/tcp
> menderproduction_minio_1                               /usr/bin/docker-entrypoint ...   Up      9000/tcp
> menderproduction_storage-proxy_1                       /usr/local/openresty/bin/o ...   Up      0.0.0.0:9000->9000/tcp
> ```

At this point you can try to log into the Web UI using the URL of your server,
and the username and password that was [created
earlier](#creating-the-first-organization-and-user).

!! It is advised to use the UI to change the password of all users that were
!! added in this guide, since the shell may keep a record of the password in
!! plaintext.

If you encounter any issues while starting or running your Mender Server, you
can take a look at the section for [troubleshooting Mender
Server](../../../troubleshooting/mender-server).
