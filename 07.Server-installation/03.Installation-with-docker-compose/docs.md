---
title: Installation with Docker Compose
taxonomy:
    category: docs
    label: tutorial
routes:
    canonical: /3.3/server-installation/installation-with-docker-compose
---

<!-- The variables used in the testing of production installation instructions -->
<!--AUTOMATION: execute=export EXPECTED_COUNT_OPENSOURCE=14 -->
<!--AUTOMATION: execute=export EXPECTED_COUNT_ENTERPRISE=19 -->
<!--AUTOMATION: execute=export SLEEP_INTERVAL=4 -->
<!--AUTOMATION: execute=export MAX_INTERATIONS=11 -->

<!-- AUTOMATION: execute=if [ "$TEST_OPEN_SOURCE" -ne 1 ] && [ "$TEST_ENTERPRISE" -ne 1 ]; then echo "Either TEST_OPEN_SOURCE xor TEST_ENTERPRISE must be set to 1!"; exit 1; fi -->
<!-- AUTOMATION: execute=if [ "$TEST_OPEN_SOURCE" -eq 1 ] && [ "$TEST_ENTERPRISE" -eq 1 ]; then echo "TEST_OPEN_SOURCE and TEST_ENTERPRISE cannot both be 1!"; exit 1; fi -->

<!-- Cleanup code -->
<!-- AUTOMATION: execute=ORIG_DIR=$PWD; function cleanup() { set +e; cd $ORIG_DIR/mender-server/production; ./run down -v; docker volume rm mender-artifacts mender-db; cd $ORIG_DIR; rm -rf mender-server; } -->
<!-- AUTOMATION: execute=trap cleanup EXIT -->

!!! You can save time by using [hosted Mender](https://hosted.mender.io?target=_blank), a secure Mender server ready to use, maintained by the Mender developers.

! This chapter contains the legacy documentation for the production installation using Docker Compose. If you are interested in setting up a Mender server for production, we highly suggest reading the [Production installation with Kubernetes](../04.Production-installation-with-kubernetes/docs.md), which is is the only supported platform for the installation of a production-grade Mender Server.

This is a step by step tutorial for deploying the Mender Server for production
environments using Docker compose, and will cover relevant security and reliability
aspects of Mender production installations.  The Mender backend services can be
deployed to production using a skeleton provided in the `production` directory of the
[integration](https://github.com/mendersoftware/integration?target=_blank)
repository. Most of the steps are the same whether you are installing the Open
Source or Enterprise edition of the Mender Server, but there are some extra
steps that are covered in the [Enterprise subsection](#enterprise).

For details and best practices of using `docker-compose` in production consult
the official
documentation:
[Using Compose in production](https://docs.docker.com/compose/production/?target=_blank)

! If you have already installed an Open Source server and wish to upgrade to
! Enterprise, you should follow [the Enterprise upgrade
! tutorial](02.Upgrading-from-OS-to-Enterprise/docs.md) instead of this tutorial.


## Prerequisites

- A machine with Ubuntu 18.04 (e.g. an instance from AWS EC2 or DigitalOcean) with the following tools installed:
  - git
  - [Docker Engine](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/?target=_blank), version **17.03 or later**.
  - [Docker Compose](https://docs.docker.com/compose/install/?target=_blank), version **1.9 or later**.
- Minimum of 10 GB free disk space and 4 GB RAM available for Mender and its services.
    - This heavily depends on your scale and environment, the supported [Mender Enterprise](https://mender.io/product/mender-enterprise?target=_blank) edition is recommended for larger-scale environments.
- A public IP address assigned and port 443 publicly accessible.
- Allocated DNS names for the Mender API Gateway and the Mender Storage Proxy
  that resolve to the public IP of the Mender server by the devices. By following this tutorial
  all services will be hosted on the same server, so you can use just one domain name for both.
  If you are just testing you can use a temporary domain name obtained from services like
  [https://ipq.co](https://ipq.co?target=_blank).

If you are setting up a Mender Enterprise server, you will also need:

- An account with Mender in order to evaluate and use the commercial features in
  Mender Enterprise. Please email [contact@mender.io](mailto:contact@mender.io)
  to receive an evaluation account.

!!! It is very likely possible to use other Linux distributions and versions. However, we recommend using this exact environment for running Mender because it is known to work and you will thus avoid any issues specific to your environment if you use this reference.


## Deployment steps

The tutorial will use a publicly available Mender integration repository. Then
proceed with setting up a local branch, preparing deployment configuration from
a template, committing the changes locally. Keeping deployment configuration in
a git repository ensures that the history of changes is tracked and subsequent
updates can be easily applied.

At the end of this tutorial you will have:

- production configuration in a single `docker-compose` file
- a running Mender backend cluster
- persistent service data is stored in Docker volumes:
  - artifact storage
  - MongoDB data
- SSL certificate for the API Gateway
- SSL certificate for the storage domain
- a set of keys for generating and validating access tokens

Consult the section on [certificates and keys](../05.Certificates-and-keys/docs.md) for details on
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


### Basic preparation setup

Start off by cloning the Mender integration repository into a local directory
named `mender-server`:

<!--AUTOVERSION: "-b %"/integration -->
```bash
git clone -b 3.3.0 https://github.com/mendersoftware/integration mender-server
```

> ```
> Cloning into 'deployment'...
> remote: Counting objects: 1117, done.
> remote: Compressing objects: 100% (11/11), done.
> remote: Total 1117 (delta 1), reused 0 (delta 0), pack-reused 1106
> Receiving objects: 100% (1117/1117), 233.85 KiB | 411.00 KiB/s, done.
> Resolving deltas: 100% (678/678), done.
> Checking connectivity... done.
> ```

Enter the directory:

```bash
cd mender-server
```

Prepare a branch where all deployment related changes will be kept:

```bash
git checkout -b my-production-setup
```

Enter the `production` directory:

```bash
cd production
```

Copy the production template to its own file:

```bash
cp config/prod.yml.template config/prod.yml
```

```bash
ls -l *
```

> ```
> -rwxr-xr-x 1 user user  725 Sep 17 14:14 run
>
> config:
> total 24
> -rw-r--r-- 1 user user  566 Sep 17 14:14 enterprise.yml.template
> -rw-r--r-- 1 user user 5814 Sep 10 15:44 prod.yml
> -rw-r--r-- 1 user user 5752 Sep 17 14:14 prod.yml.template
> ```

The template includes a few files:

- `run` - a convenience helper that invokes `docker-compose` by passing the required
  compose files; arguments passed to `run` in command line are forwarded
  directly to `docker-compose`

- `prod.yml` and `prod.yml.template` - contains deployment-specific
  configuration, builds on top of `docker-compose.yml` (located at the root of
  integration repository)

- `enterprise.yml.template` - configuration for running an Enterprise instance
  of the Mender server. This topic is covered separately in [the Enterprise
  part](#enterprise) of the installation tutorial

!!! If an `enterprise.yml` file exists in the `config` directory, this will
!!! automatically turn on Enterprise features in the backend service. If you
!!! want to use the Open Source edition (not Enterprise), please remove
!!! `enterprise.yml` from the `config` directory.

At this point all changes should be committed to the repository:

<!--AUTOMATION: ignore -->
```bash
git add .
```

<!--AUTOMATION: ignore -->
```bash
git commit -m 'production: initial template'
```
> ```
> [my-production-setup 556cc2e] production: initial template
>  1 file changed, 54 insertions(+)
>  create mode 100644 production/config/prod.yml
> ```

Assuming that current working directory is still `production`, download
necessary Docker images:

```bash
./run pull
```

> ```
> Pulling mender-mongo                  ... done
> Pulling mender-deviceconfig           ... done
> Pulling mender-useradm                ... done
> Pulling mender-workflows-worker       ... done
> Pulling mender-create-artifact-worker ... done
> Pulling mender-workflows-server       ... done
> Pulling mender-device-auth            ... done
> Pulling mender-gui                    ... done
> Pulling mender-inventory              ... done
> Pulling mender-api-gateway            ... done
> Pulling minio                         ... done
> Pulling mender-deployments            ... done
> Pulling mender-nats                   ... done
> Pulling mender-deviceconnect          ... done
> Pulling mender-mongo (mongo:4.4)...
> ```

! Using the `run` helper script may fail when local user has insufficient permissions to reach a local docker daemon. Make sure that the Docker installation was completed successfully and the user has sufficient permissions (typically the user must be a member of the `docker` group).

!! Please note that Docker Hub enforced limits on pulls originating
!! from anonymous users to 100 per 6 hours (see: [Docker pricing](https://www.docker.com/pricing)).
!! This means that, for reasons completely independent from Mender,
!! the above step may fail and you may have to retry after some time.


### Certificates and keys

First, set the public domain name of your server (the URL your devices will reach your Mender server on):

```bash
API_GATEWAY_DOMAIN_NAME="mender.example.com"  # NB! replace with your server's public domain name
STORAGE_PROXY_DOMAIN_NAME="${API_GATEWAY_DOMAIN_NAME}"  # change if you are using a different domain name than the the default one
```

Prepare certificates using the helper script `keygen`:

```bash
CERT_CN=$API_GATEWAY_DOMAIN_NAME \
CERT_SAN="DNS:${API_GATEWAY_DOMAIN_NAME},DNS:*.${STORAGE_PROXY_DOMAIN_NAME}" \
../keygen
```

> ```
> Generating a 256 bit EC private key
> writing new private key to 'private.key'
> ...
> All Mender Server keys and certificates have been generated in directory keys-generated.
> Please include them in your docker compose and device builds.
> For more information, please refer to https://docs.mender.io/
> ```

Your local directory tree should now look like this:

> ```
> ├── keys-generated
> │   ├── cert
> │   │   ├── cert.crt
> │   │   └── private.key
> │   └── keys
> │       ├── deviceauth
> │       │   └── private.key
> │       └── useradm
> │           └── private.key
> ├── config/enterprise.yml.template
> ├── config/prod.yml
> ├── config/prod.yml.template
> └── run
> ```

The production template file `prod.yml` is already configured to load keys and
certificates from locations created by the `keygen` script. If you wish to use a
different set of certificates or keys, please consult the
[relevant documentation](../05.Certificates-and-keys/docs.md).

Next, we can add and commit generated keys and certificates:

! Note that the following steps will commit your keys in plaintext to the git history. Make sure to keep all keys secure. Use encryption if needed and decrypt the keys before using them in containers; see the section below on [encrypting keys](#encrypting-keys-optional) for some examples.

```bash
git add keys-generated
```

```bash
git commit -m 'production: adding generated keys and certificates'
```

> ```
> [my-production-setup fd8a397] production: adding generated keys and certificates
>  6 files changed, 108 insertions(+)
>  create mode 100644 production/keys-generated/cert/cert.crt
>  create mode 100644 production/keys-generated/cert/private.key
>  create mode 100644 production/keys-generated/keys/deviceauth/private.key
>  create mode 100644 production/keys-generated/keys/useradm/private.key
> ```

The API Gateway and Storage Proxy certificates generated here need to be made
available to the Mender client.
Consult the section on [building for production](../../05.System-updates-Yocto-Project/06.Build-for-production/docs.md)
for a description on how to include the certificates in the client builds.

!! Only certificates need to be made available to devices or end users. Private keys should never be shared.


#### Encrypting keys (optional)

A simple method for encrypting keys is to
use the [GNU Privacy Guard](https://www.gnupg.org/?target=_blank) tool. Instead of committing
plaintext keys to the repository, we will `tar` and encrypt the entire
`keys-generated` directory structure, then commit it to the repository as a
single binary blob.

The entire directory structure can be encrypted with the following command:

<!--AUTOMATION: ignore=optional step -->
```bash
tar c keys-generated |  gpg --output keys-generated.tar.gpg --symmetric
Enter passphrase:
```

<!--AUTOMATION: ignore=optional step -->
```bash
rm -rf keys-generated
```

<!--AUTOMATION: ignore=optional step -->
```bash
ls -l
```
> ```
> total 20
> drwxrwxr-x. 1 user group 4096 01-30 11:08 config
> -rw-rw-r--. 1 user group 5094 01-30 11:24 keys-generated.tar.gpg
> -rwxrwxr-x. 1 user group  173 01-27 14:16 run
> ```

Keys need to be decrypted before bringing the whole environment up:

<!--AUTOMATION: ignore=optional step -->
```bash
gpg --decrypt keys-generated.tar.gpg | tar xvf -
gpg: AES encrypted data
Enter passphrase:
```

When using encryption, commit `keys-generated.tar.gpg` instead of the
`keys-generated` directory structure to the repository, like this:

<!--AUTOMATION: ignore=optional step -->
```bash
git add keys-generated.tar.gpg
```

<!--AUTOMATION: ignore=optional step -->
```bash
git commit -m 'production: adding generated keys and certificates'
```

> ```
> [my-production-setup 237af44] production: adding generated keys and certificates
>  1 file changed, 111 insertions(+)
>  create mode 100644 production/keys-generated.tar.gpg
> ```


### Persistent storage

Persistent storage of backend services' data is implemented using
named [Docker volumes](https://docs.docker.com/engine/admin/volumes/volumes/?target=_blank).
The template is configured to mount the following volumes:

- `mender-artifacts` - artifact objects storage
- `mender-db` - mender services databases data

Create these volumes with the following commands:

```bash
docker volume create --name=mender-artifacts
docker volume create --name=mender-db
```

!!! The storage location of these volumes depends on your docker configuration. You can check the path for a specific volume by running
!!! ```bash
!!! docker volume inspect --format '{{.Mountpoint}}' mender-artifacts
!!! ```


### Configuration

The deployment configuration in `config/prod.yml` now needs to be updated.


#### Minio

The keys `MINIO_ACCESS_KEY` and `MINIO_SECRET_KEY` control
credentials for uploading artifacts into the object store. Since Minio is a S3 API
compatible service, these settings correspond to Amazon's AWS Access Key ID and
Secret Access Key respectively.

First, generate a secret key for Minio with the `pwgen` utility:

!!! On the Debian family of distributions you can install `pwgen` with `apt-get install pwgen`.
!!! On the RPM family of distributions, you can install it with `yum install pwgen`.

```bash
MINIO_SECRET_KEY_GENERATED=$(pwgen 16 1) && echo $MINIO_SECRET_KEY_GENERATED
```
> ```
> ahshagheeD1ooPae
> ```

Insert the access and secret keys into `config/prod.yml` with the following commands:

```bash
sed -i.bak "s/MINIO_ACCESS_KEY:.*/MINIO_ACCESS_KEY: mender-deployments/g" config/prod.yml
sed -i.bak "s/MINIO_SECRET_KEY:.*/MINIO_SECRET_KEY: $MINIO_SECRET_KEY_GENERATED/g" config/prod.yml
```

The updated entry should look similar to this, you can verify with `git diff`:

```yaml
    ...
    minio:
        environment:
            # access key
            MINIO_ACCESS_KEY: mender-deployments
            # secret
            MINIO_SECRET_KEY: ahshagheeD1ooPae
    ...

```


#### Deployments service

The deployments service will upload artifact objects to `minio` storage via `storage-proxy`,
see the [administration overview](../01.Overview/docs.md) for more details. For this reason,
access credentials `DEPLOYMENTS_AWS_AUTH_KEY` and `DEPLOYMENTS_AWS_AUTH_SECRET`
need to be updated and `DEPLOYMENTS_AWS_URI` must point to the domain name of your Storage proxy.

Run the following commands to set `DEPLOYMENTS_AWS_AUTH_KEY` and
`DEPLOYMENTS_AWS_AUTH_SECRET` to the values of `MINIO_ACCESS_KEY`
and `MINIO_SECRET_KEY`, respectively.

```bash
sed -i.bak "s/DEPLOYMENTS_AWS_AUTH_KEY:.*/DEPLOYMENTS_AWS_AUTH_KEY: mender-deployments/g" config/prod.yml
sed -i.bak "s/DEPLOYMENTS_AWS_AUTH_SECRET:.*/DEPLOYMENTS_AWS_AUTH_SECRET: $MINIO_SECRET_KEY_GENERATED/g" config/prod.yml
```
Also, run the following command so `DEPLOYMENTS_AWS_URI` points to your Storage proxy:

```bash
sed -i.bak "s/https:\/\/set-my-alias-here.com/https:\/\/$STORAGE_PROXY_DOMAIN_NAME/g" config/prod.yml
```

After these three commands, the updated entry should look like this (you can again verify with `git diff`):

```yaml
    ...
    mender-deployments:
        ...
        environment:
            DEPLOYMENTS_AWS_AUTH_KEY: mender-deployments
            DEPLOYMENTS_AWS_AUTH_SECRET: ahshagheeD1ooPae
            DEPLOYMENTS_AWS_URI: https://mender.example.com
    ...
```

!! The address used in `DEPLOYMENTS_AWS_URI` must be exactly the same as the one that will be used by devices. The deployments service generates signed URLs for accessing artifact storage. A different hostname or port will result in signature verification failure and download attempts will be rejected.


#### Storage proxy

In the default setup there is no separate process acting as a proxy to storage service.
For this purpose you can use Mender API Gateway, but with an additional domain name.
Change the placeholder value `set-my-alias-here` to a valid domain name to use
Mender API Gateway as a proxy to the storage service, by running the following command:
```bash
sed -i.bak "s/set-my-alias-here.com/$STORAGE_PROXY_DOMAIN_NAME/g" config/prod.yml
```


#### API gateway

For security purposes, the API Gateway must know precisely the DNS name allocated to it,
which you'll configure via the `ALLOWED_HOSTS` environment variable.

Change the placeholder value `my-gateway-dns-name` to a valid hostname, by running
the following command:

```bash
sed -i.bak "s/my-gateway-dns-name/$API_GATEWAY_DOMAIN_NAME/g" config/prod.yml
```

The updated entry should look like this:

```yaml
    ...
    mender-api-gateway:
        ...
        environment:
            ALLOWED_HOSTS: mender.example.com
    ...
```

Note that if for some reason you need more than 1 DNS name pointing to the gateway,
you can supply a whitespace-separated list of hostnames as follows:

```yaml
    ...
    mender-api-gateway:
        ...
        environment:
            ALLOWED_HOSTS: mender.example.com mender2.example.com
    ...
```


#### Logging

The setup uses Docker's default `json-file` logging driver, which exposes two important log
rotation parameters: `max-file` and `max-size`. For selected services - consistently producing
a large amount of logs - we override these settings to ensure that at any given time, logs capture
about 1 week of a running system's operation.

The reference setup used for determining these parameters (`max-file: 10`, `max-size: 50m`)
was 200 devices, polling the server every 30 minutes. The total log volume produced was 2.4GB,
and this is the recommended amount of disk space to reserve for logging purposes alone.

These parameters can however be adjusted accordingly to a particular deployment and workload. The
deciding factors determining the log volume are:
- the number of devices accessing the system.
- polling frequency

It is suggested to adjust log rotation parameters only after measuring the actual space usage for a given use case.

#### Saving the configuration

Once all the configuration is complete, commit all changes to the repository:

<!--AUTOMATION: ignore -->
```bash
git add config/prod.yml
```

<!--AUTOMATION: ignore -->
```bash
git commit -m 'production: configuration'
```

At this point your commit history should look as follows:

<!--AUTOVERSION: "git log --oneline %..HEAD"/integration -->
<!--AUTOMATION: ignore -->
```bash
git log --oneline 3.3.0..HEAD
```
> ```
> 7a4de3c production: configuration
> 41273f7 production: adding generated keys and certificates
> 5ad6528 production: initial template
> ```


## Open Source

<!-- Test block for TEST_OPEN_SOURCE=1 -->
<!-- AUTOMATION: execute=if [ "$TEST_OPEN_SOURCE" -eq 1 ]; then -->

This section deals specifically with setting up an Open Source server. If you
are setting up an Enterprise server, please proceed to the [Enterprise
section](#enterprise).

### Bring up the Open Source server

Bring up all services up in detached mode with the following command:

```bash
./run up -d
```
> ```
> Creating network "menderproduction_mender" with the default driver
> Creating menderproduction_mender-nats_1                   ... done
> Creating menderproduction_mender-mongo_1 ... done
> Creating menderproduction_minio_1        ... done
> Creating menderproduction_mender-gui_1   ... done
> Creating menderproduction_mender-workflows-worker_1       ... done
> Creating menderproduction_mender-create-artifact-worker_1 ... done
> Creating menderproduction_mender-useradm_1                ... done
> Creating menderproduction_mender-workflows-server_1       ... done
> Creating menderproduction_mender-deviceconfig_1           ... done
> Creating menderproduction_mender-inventory_1              ... done
> Creating menderproduction_mender-deviceconnect_1          ... done
> Creating menderproduction_mender-device-auth_1            ... done
> Creating menderproduction_mender-api-gateway_1            ... done
> Creating menderproduction_mender-deployments_1            ... done
> ```

!!! Services, networks and volumes have a `menderproduction` prefix, see the note about [docker-compose naming scheme](#docker-compose-naming-scheme) for more details. When using `docker ..` commands, a complete container name must be provided (ex. `menderproduction_mender-deployments_1`).


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

<!--AUTOMATION: execute=function CONTAINERS_COUNT_TEST() { EXPECTED="$(./run config --services | sort)"; ACTUAL="$(./run ps --services --filter 'status=running' | sort)"; if [ "$EXPECTED" != "$ACTUAL" ]; then echo "Not all expected services are running ($(echo "$ACTUAL" | wc -w)/$(echo "$EXPECTED" | wc -w))"; return 1; else return 0; fi } -->
<!--AUTOMATION: test=CONTAINERS_COUNT_TEST; -->
<!--AUTOMATION: test=./run stop -->
<!--AUTOMATION: test=./run up -d -->
<!--AUTOMATION: test=CONTAINERS_COUNT_TEST; -->
<!--AUTOMATION: test=docker ps | grep menderproduction | grep "0.0.0.0:443" -->

<!-- End of test block for TEST_OPEN_SOURCE=1 -->
<!-- AUTOMATION: execute=fi -->


## Enterprise

<!-- Test block for TEST_ENTERPRISE=1 -->
<!-- AUTOMATION: execute=if [ "$TEST_ENTERPRISE" -eq 1 ]; then -->

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

!!! If you have lost your credentials or need an evaluation account please email [contact@mender.io](mailto:contact@mender.io).

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
  server](02.Upgrading-from-OS-to-Enterprise/docs.md#migrating-clients)
* [Mender installed on device using a deb
  package](../../03.Client-installation/02.Install-with-Debian-package/docs.md)
* [Device integration using Yocto
  Project](../../05.System-updates-Yocto-Project/99.Variables/docs.md#mender_tenant_token)
* [Device integration with Debian
  Family](../../04.System-updates-Debian-family/03.Customize-Mender/docs.md)
* [Modifying an existing prebuilt
  image](../../06.Artifact-creation/03.Modify-an-Artifact/docs.md)


### Saving the Enterprise configuration

Once the Enterprise configuration is complete, commit all changes to the
repository:

<!--AUTOMATION: ignore -->
```bash
git add config/enterprise.yml
```

<!--AUTOMATION: ignore -->
```bash
git commit -m 'production: Enterprise configuration'
```

At this point your commit history should look as follows:

<!--AUTOVERSION: "git log --oneline %..HEAD"/integration -->
<!--AUTOMATION: ignore -->
```bash
git log --oneline 3.3.0..HEAD
```
> ```
> 76b3d00 production: Enterprise configuration
> 7a4de3c production: configuration
> 41273f7 production: adding generated keys and certificates
> 5ad6528 production: initial template
> ```

<!-- Verification of Enterprise instance -->

<!--AUTOMATION: execute=function CONTAINERS_COUNT_TEST() { EXPECTED="$(./run config --services | sort)"; ACTUAL="$(./run ps --services --filter 'status=running' | sort)"; if [ "$EXPECTED" != "$ACTUAL" ]; then echo "Not all expected services are running ($(echo "$ACTUAL" | wc -w)/$(echo "$EXPECTED" | wc -w))"; return 1; else return 0; fi } -->
<!--AUTOMATION: test=CONTAINERS_COUNT_TEST; -->
<!--AUTOMATION: test=./run stop -->
<!--AUTOMATION: test=./run up -d -->
<!--AUTOMATION: test=CONTAINERS_COUNT_TEST; -->
<!--AUTOMATION: test=docker ps | grep menderproduction | grep "0.0.0.0:443" -->

<!-- End of test block for TEST_ENTERPRISE=1 -->
<!-- AUTOMATION: execute=fi -->


## Verification

To verify that the services are running, execute the following command and
verify that the state of all services is "Up":

```bash
./run ps
```

Below you can see typical output for the Enterprise server. The Open Source
server will be similar, but will have fewer services running.

> ```
>                       Name                                    Command                  State                  Ports            
> -------------------------------------------------------------------------------------------------------------------------------
> menderproduction_mender-api-gateway_1              /entrypoint.sh --accesslog ...   Up             0.0.0.0:443->443/tcp, 80/tcp
> menderproduction_mender-auditlogs_1                /usr/bin/auditlogs --confi ...   Up             8080/tcp                    
> menderproduction_mender-create-artifact-worker_1   /usr/bin/workflows --confi ...   Up             8080/tcp                    
> menderproduction_mender-deployments_1              /entrypoint.sh --config /e ...   Up             8080/tcp                    
> menderproduction_mender-device-auth_1              /usr/bin/deviceauth --conf ...   Up             8080/tcp                    
> menderproduction_mender-deviceconfig_1             /usr/bin/deviceconfig --co ...   Up             8080/tcp                    
> menderproduction_mender-deviceconnect_1            /usr/bin/deviceconnect --c ...   Up             8080/tcp                    
> menderproduction_mender-gui_1                      /entrypoint.sh nginx             Up (healthy)   80/tcp, 8080/tcp            
> menderproduction_mender-inventory_1                /usr/bin/inventory-enterpr ...   Up             8080/tcp                    
> menderproduction_mender-mongo_1                    docker-entrypoint.sh mongod      Up             27017/tcp                   
> menderproduction_mender-nats_1                     docker-entrypoint.sh nats- ...   Up             4222/tcp, 6222/tcp, 8222/tcp
> menderproduction_mender-tenantadm_1                /usr/bin/tenantadm --confi ...   Up             8080/tcp                    
> menderproduction_mender-useradm_1                  /usr/bin/useradm-enterpris ...   Up             8080/tcp                    
> menderproduction_mender-workflows-server_1         /usr/bin/workflows-enterpr ...   Up             8080/tcp                    
> menderproduction_mender-workflows-worker_1         /entrypoint.sh worker --au ...   Up                                         
> menderproduction_minio_1                           /usr/bin/docker-entrypoint ...   Up (healthy)   9000/tcp
> ```

At this point you can try to log into the Web UI using the URL of your server,
and the username and password that was [created
earlier](#creating-the-first-organization-and-user).

!! It is advised to use the UI to change the password of all users that were
!! added in this tutorial, since the shell may keep a record of the password in
!! plaintext.

If you encounter any issues while starting or running your Mender Server, you
can take a look at the section for [troubleshooting Mender
Server]().
