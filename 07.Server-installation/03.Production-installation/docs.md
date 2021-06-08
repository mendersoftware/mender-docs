---
title: Production installation
taxonomy:
    category: docs
    label: tutorial
---

<!-- The variables used in the testing of production installation instructions -->
<!--AUTOMATION: execute=export EXPECTED_COUNT_OPENSOURCE=14 -->
<!--AUTOMATION: execute=export EXPECTED_COUNT_ENTERPRISE=16 -->
<!--AUTOMATION: execute=export SLEEP_INTERVAL=4 -->
<!--AUTOMATION: execute=export MAX_INTERATIONS=11 -->

<!-- AUTOMATION: execute=if [ "$TEST_OPEN_SOURCE" != 1 ] && [ "$TEST_ENTERPRISE" != 1 ]; then echo "Either TEST_OPEN_SOURCE xor TEST_ENTERPRISE must be set to 1!"; exit 1; fi -->
<!-- AUTOMATION: execute=if [ "$TEST_OPEN_SOURCE" = 1 ] && [ "$TEST_ENTERPRISE" = 1 ]; then echo "TEST_OPEN_SOURCE and TEST_ENTERPRISE cannot both be 1!"; exit 1; fi -->

<!-- Cleanup code -->
<!-- AUTOMATION: execute=ORIG_DIR=$PWD; function cleanup() { set +e; cd $ORIG_DIR/mender-server/production; ./run down -v; docker volume rm mender-artifacts mender-db; cd $ORIG_DIR; rm -rf mender-server; } -->
<!-- AUTOMATION: execute=trap cleanup EXIT -->

!!! You can save time by using [hosted Mender](https://hosted.mender.io?target=_blank), a secure Mender server ready to use, maintained by the Mender developers.

FIXME
- careful with the 'step by step' wording, k8s/helm charts put much more responsibility on the user, e.g. cluster setup, 3rd party deps setup (separate helm charts for mongo and minio), helm param customizations for cloud provider (e.g. service load balancers), same for dns (external-dns sidecar, etc)
- 'production' directory in integration is irrelevant ATM; all that's needed for install is at https://github.com/mendersoftware/mender-helm

! If you have already installed an Open Source server and wish to upgrade to
! Enterprise, you should follow [the Enterprise upgrade
! tutorial](01.Upgrading-from-OS-to-Enterprise/docs.md) instead of this tutorial.


## Prerequisites

FIXME
- user needs a k8s cluster, on whichever selected provider - far out of scope for this doc; no git, docker, compose
- listed limits are not that relevant anymore - omit or advise to consult helm chart defaults
- in the simplest case, just one DNS is needed; traefik took over the 'storage-proxy' responsibilities
we do have a new *new storage proxy* as a workaround for old client incompatible with traefik, but new users
won't be interested

If you are setting up a Mender Enterprise server, you will also need:

- An account with Mender in order to evaluate and use the commercial features in
  Mender Enterprise. Please email [contact@mender.io]()
  to receive an evaluation account.

FIXME
not relevant anymore, environment is now a k8s cluster


## Deployment steps

FIXME
- we'll use only https://github.com/mendersoftware/mender-helm
- no more git magic - user can maintain their helm values however they want, out of scope

FIXME
- at the end of this tutorial the user will have a versioned mender release installed onto
their cluster
- we'll provide some minimal helm value override layers that will aid in setting up os vs enterprise, 
aws vs minio; user must fill them in
- further customizations are possible, helm chart exposes a large number of attributes - consult the
chart's readme

Consult the section on [certificates and keys](../04.Certificates-and-keys/docs.md) for details on
how the certificates and keys are used in the system.

FIXME
irrelevant

### Basic preparation setup

FIXME:
- tell the user to prep the cluster and kubectl context
- clone mender-helm, checkout tag
- make package
- there is no 'prod' template anymore, but the interesting files are in mender-helm/install; they are the scaffolding now
- user must generate/obtain and paste certs and some environment into these 

!! Please note that Docker Hub enforced limits on pulls originating
!! from anonymous users to 100 per 6 hours (see: [Docker pricing](https://www.docker.com/pricing)).
!! This means that, for reasons completely independent from Mender,
!! the above step may fail and you may have to retry after some time.


### Certificates and keys

FIXME
- just 1 domain, mender.example.com
- (second only if using old clients and need storage proxy)
- suggestion: get rid of keygen; the structure will not be used anymore,
also it's incorrect (generates 0-depth certs, generates for storage proxy by default)
- maybe instead just advise the user to prep keys and certs using 'known methods' (openssl, etc)
- important:
   - if self signed: must not be 0 depth; user must have their own root CA cert
   - cert must respect SAN (domain in subjectAltNames, not CN)


FIXME
- no more git magic

The API Gateway and Storage Proxy certificates generated here need to be made
available to the Mender client.
Consult the section on [building for production](../../05.System-updates-Yocto-Project/06.Build-for-production/docs.md)
for a description on how to include the certificates in the client builds.
GOTCHA: SkipVerify for client seems to have no effect, if self signed, root CA cert must be added to trusted certs;
ServerCertificate has no effect either


!! Only certificates need to be made available to devices or end users. Private keys should never be shared.


FIXME
not relevant anymore?

FIXME
- the following sections could be streamlined, no need to go through each component one by one
- the idea is: user picks installation type (os, enterprise, minio/aws), picks up templates from /mender-helm/install, 
and simply fills the fields we suggest

### Persistent storage

FIXME
- it's now up to the user to set up persistent volumes ('persistent volume claims') for mongo and minio
- (this is done via the cloud provider-specific addons/annotations in user's custom helm values files - out of scope)
- both minio and mongo are installed from their own helm charts now (see helm readme) - refer user to that

FIXME
irrelevant

#### Minio

FIXME:
- see above, most of it is irrelevant
- user will a) setup minio on their own b) transfer the settings to mender-helm/install/ storage value file

#### Deployments service

FIXME
- by default - no storage proxy

FIXME 
- irrelevant

```

!! The address used in `DEPLOYMENTS_AWS_URI` must be exactly the same as the one that will be used by devices. The deployments service generates signed URLs for accessing artifact storage. A different hostname or port will result in signature verification failure and download attempts will be rejected.


#### Storage proxy

FIXME
- needs restructuring into another section for 'old clients'


#### API gateway

FIXME:
- done via helm chart


#### Logging

FIXME
- I believe this was pre-traefik access logs example volumes
- anyway, info about docker driver is obsolete

FIXME
no more git magic

## Open Source

<!-- Test block for TEST_OPEN_SOURCE=1 -->
<!-- AUTOMATION: execute=if [ "$TEST_OPEN_SOURCE" = 1 ]; then -->

This section deals specifically with setting up an Open Source server. If you
are setting up an Enterprise server, please proceed to the [Enterprise
section](#enterprise).

### Bring up the Open Source server

FIXME
Installing and running are pretty much the same here
TODO: helm cmd


### Creating the first user

Since this is a brand new installation we need to create the initial user via
the CLI provided by the User Administration Service. The service's binary is
embedded in a Docker container, so to execute it you will issue the **exec**
subcommand of docker-compose, e.g.:

<!--AUTOMATION: ignore -->
```bash
./run exec mender-useradm /usr/bin/useradm create-user --username=myusername@host.com --password=mysecretpassword
```

! Keep in mind that above is executed in a command-line interpreter meaning that certain characters might need to be escaped, e.g if you are using the `$` character in your password, this could interpret as a variable name unless it is escaped.

The next sections deal with installation of an Enterprise server. If you are
installing an Open Source server, please proceed to
[verification](#verification) now.

<!-- Verification of Open Source instance -->

<!--AUTOMATION: execute=function CONTAINERS_COUNT_TEST_OPENSOURCE() { local n; [ "${EXPECTED_COUNT_OPENSOURCE}" == "" ] && return 1; for ((n=0;n<${MAX_INTERATIONS};n++)); do count=$(docker container ls -f "status=running" --format 'table {{.Status}}\t{{.Names}}' | grep ^Up | grep -c menderproduction); [ ${count} -eq ${EXPECTED_COUNT_OPENSOURCE} ] && break; sleep ${SLEEP_INTERVAL}; done; [ ${count} -eq ${EXPECTED_COUNT_OPENSOURCE} ] || { echo "some containers are not 'Up'; ${count}/${EXPECTED_COUNT_OPENSOURCE} running." && docker ps && ./run images && ./run logs && exit 1; }; } -->
<!--AUTOMATION: test=CONTAINERS_COUNT_TEST_OPENSOURCE; -->
<!--AUTOMATION: test=./run stop -->
<!--AUTOMATION: test=./run up -d -->
<!--AUTOMATION: test=CONTAINERS_COUNT_TEST_OPENSOURCE; -->
<!--AUTOMATION: test=docker ps | grep menderproduction | grep "0.0.0.0:443" -->

<!-- End of test block for TEST_OPEN_SOURCE=1 -->
<!-- AUTOMATION: execute=fi -->


## Enterprise

<!-- Test block for TEST_ENTERPRISE=1 -->
<!-- AUTOMATION: execute=if [ "$TEST_ENTERPRISE" = 1 ]; then -->

This section will go through setting up the Enterprise features of the Mender
server. If you are using the Open Source edition of the Mender server, you can
skip ahead to [the verification](#verification).

### Configuring Enterprise

Once the Open Source parts of the configuration have been completed, you should
have a fully functional server setup, except that it has not been launched
yet. It is now time to configure the Enterprise specific features before
bringing the server up.

Copy the `enterprise.yml.template` file to its production location,
`enterprise.yml`:

```bash
cp config/enterprise.yml.template config/enterprise.yml
```

Creating the `enterprise.yml` file enables the Enterprise Mender server.

### Bring up the Enterprise server

First log in to the Mender docker registry with your Mender Enterprise credentials:

<!--AUTOMATION: ignore -->
```bash
docker login registry.mender.io
```

!!! If you have lost your credentials or need an evaluation account please email [contact@mender.io]().

Bring up all services up in detached mode with the following command:

```bash
./run up -d
```
> ```
> Creating menderproduction_mender-api-gateway_1 ... done
> Creating menderproduction_mender-create-artifact-worker_1 ... done
> Creating menderproduction_mender-deployments_1 ... done
> Creating menderproduction_mender-device-auth_1 ... done
> Creating menderproduction_mender-gui_1 ... done
> Creating menderproduction_mender-inventory_1 ... done
> Creating menderproduction_mender-mongo_1 ... done
> Creating menderproduction_mender-tenantadm_1 ... done
> Creating menderproduction_mender-useradm_1 ... done
> Creating menderproduction_mender-workflows-server_1 ... done
> Creating menderproduction_mender-workflows-worker_1 ... done
> Creating menderproduction_minio_1 ... done
> ```

!!! Services, networks and volumes have a `menderproduction` prefix, see the note about [docker-compose naming scheme](#docker-compose-naming-scheme) for more details. When using `docker ..` commands, a complete container name must be provided (ex. `menderproduction_mender-deployments_1`).

Note that even though this launches the Enterprise backend services, the Mender
Enterprise server is not fully functional yet.

### Multi tenancy

Multi tenancy is a feature of Mender where users can be divided into
"organizations" (also sometimes called "tenants"). Each organization is confined
and can not see or influence the data of other organizations. This can be used
for example to give two different product teams access to the Mender service,
without them seeing each others data, as well as isolating devices and users in
test and production environments.

When using Mender Enterprise, multi tenancy is automatically enabled, and it
cannot be turned off. Below follows a tutorial for setting up a single
organization. For additional information on administering organizations, see the
help screen from:

<!--AUTOMATION: ignore -->
```bash
./run exec mender-tenantadm /usr/bin/tenantadm --help
```

#### Creating the first organization and user

In either case, at least one organization must be created when first installing
the service. Execute this command in the `production` directory.

Replace the organization name, username and password with desired values and run this command:

<!-- Wait for service to start -->
<!--AUTOMATION: execute=sleep 30 -->

<!-- Trick to capture the output. The `tr` is because Go prints with Windows
line endings for whatever reason. -->
```bash
TENANT_ID=$(./run exec -T mender-tenantadm /usr/bin/tenantadm create-org --name=MyOrganization --username=myusername@host.com --password=mysecretpassword | tr -d '\r') && (echo $TENANT_ID)
```
<!--AUTOMATION: test=test -n "$TENANT_ID" -->

<!-- create-org is an async workflow, give it some time -->
<!--AUTOMATION: execute=sleep 10 -->

**Make sure to save the tenant ID** that appears after calling the command (which will also be in the `TENANT_ID` shell variable).
This will be the identifier for the first organization. Creating additional organizations
works exactly the same way, so the above step may be repeated multiple times.


#### Fetching the tenant token

Now we need to fetch the **tenant token** for the new organization. This is
available in the JSON output from the `get-tenant` command, in the
`tenant_token` field. To avoid manually parsing raw JSON, we can use the `jq`
tool:

!!! On the Debian family of distributions you can install `jq` with `apt-get install jq`.

```bash
TENANT_TOKEN=$(./run exec -T mender-tenantadm /usr/bin/tenantadm get-tenant --id $TENANT_ID | jq -r .tenant_token) && (echo $TENANT_TOKEN)
```
<!--AUTOMATION: test=test -n "$TENANT_TOKEN" -->

where `$TENANT_ID` is the ID that was printed by the previous command.
The output tenant token should be a long string like this:

> eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW5kZXIudGVuYW50IjoiNWQ4MzM1MzJkMTMwNTgwMDI4NDhmZmRmIiwia<br>
XNzIjoiTWVuZGVyIiwic3ViIjoiNWQ4MzM1MzJkMTMwNTgwMDI4NDhmZmRmIn0.HJDGHzqZqbosAYyJpSIEeL0W4HMiOmb15ETnu<br>
ChxE0i7ahW49dZZlQNJBKLkLzuESDxXnmQbQwsSGP6t32pGkeHVXTPjrSjhtMPC80NiibNG3f-QATw9I8YgG2SBd5xaKl17qdta1<br>
nGi80T2UKrwlzqLHR7wNed10ss3NgJDIDvrm89XO0Rg6jpFZsHCPyyK1c8-Vn8zZjW5azZLNSgtgSLSmFQguQLRRXL2x12VEcmez<br>
tFY0kJnhGtN07CD3XXxcz0BpWbevDYOPOEUusGd2KpLK2Y4QU8RdngqNtRe7SppG0fn6m6tKiifrPDAv_THCEG6dvpMHyIM77vGI<br>
PwvV4ABGhZKRAlDe1R4csJQIbhVcTWMGcoZ4bKH-zDK0900_wWM53i9rkgNFDM470i6-d1oqfaCPcbiniKsq1HcJRZsIVNJ1edDo<br>
vhQ6IbffPRCw-Au_GlnPTn_czovJqSa3bgwrJguYRIKJGWhHgx0e3j795oJ08ks2Mp3Rshbv4da

Make sure that the string does not include any spaces or newlines when you copy
it from the terminal. The tenant token will be used in the following sections.

You can repeat the steps if you would like to isolate devices into multiple organizations.


#### Installing the tenant token

The **tenant token** needs to be included in the client configuration of each device that
is going to be managed by Mender. Exactly how to include the token depends on
which integration method is used with the client. Please refer to one of these sections:

* [Migrating existing clients from an Open Source to an Enterprise
  server](01.Upgrading-from-OS-to-Enterprise/docs.md#migrating-clients)
* [Mender installed on device using a deb
  package](../../03.Client-installation/02.Install-with-Debian-package/docs.md)
* [Device integration using Yocto
  Project](../../05.System-updates-Yocto-Project/99.Variables/docs.md#mender_tenant_token)
* [Device integration with Debian
  Family](../../04.System-updates-Debian-family/03.Customize-Mender/docs.md)
* [Modifying an existing prebuilt
  image](../../06.Artifact-creation/03.Modify-an-Artifact/docs.md)


FIXME
irrelevant

<!-- Verification of Enterprise instance -->

<!--AUTOMATION: execute=function CONTAINERS_COUNT_TEST_ENTERPRISE() { local n; [ "${EXPECTED_COUNT_ENTERPRISE}" == "" ] && return 1; for ((n=0;n<${MAX_INTERATIONS};n++)); do count=$(docker container ls -f "status=running" --format 'table {{.Status}}\t{{.Names}}' | grep ^Up | grep -c menderproduction); [ ${count} -eq ${EXPECTED_COUNT_ENTERPRISE} ] && break; sleep ${SLEEP_INTERVAL}; done; [ ${count} -eq ${EXPECTED_COUNT_ENTERPRISE} ] || { echo "some containers are not 'Up'; ${count}/${EXPECTED_COUNT_ENTERPRISE} running." && docker ps && ./run images && ./run logs && exit 1; }; } -->
<!--AUTOMATION: test=CONTAINERS_COUNT_TEST_ENTERPRISE; -->
<!--AUTOMATION: test=./run stop -->
<!--AUTOMATION: test=./run up -d -->
<!--AUTOMATION: test=CONTAINERS_COUNT_TEST_ENTERPRISE; -->
<!--AUTOMATION: test=docker ps | grep menderproduction | grep "0.0.0.0:443" -->

<!-- End of test block for TEST_ENTERPRISE=1 -->
<!-- AUTOMATION: execute=fi -->


## Verification

FIXME
- use kubectl get services/pods/deployments, helm mainfest, etc. to inspect the installed release


FIXME: this section will need a review as well
If you encounter any issues while starting or running your Mender Server, you
can take a look at the section for [troubleshooting Mender
Server]().


## Mutual TLS

Mender Enterprise supports setting up a reverse proxy at the edge of the network, which can authenticate devices using TLS client certificates. Each client is equipped with a certificate signed by a CA certificate (Certificate Authority), and the edge proxy authenticates devices by verifying this signature. Authenticated devices are automatically authorized in the Mender backend, and do not need manual approval.

Please refer to the [Mutual TLS section](../../08.Server-integration/03.Mutual-TLS-authentication/docs.md)
to find further details on the configuration of this feature.
