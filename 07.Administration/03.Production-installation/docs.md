---
title: Production installation
taxonomy:
    category: docs
---

<!-- AUTOMATION: execute=if [ "$TEST_OPEN_SOURCE" != 1 ] && [ "$TEST_ENTERPRISE" != 1 ]; then echo "Either TEST_OPEN_SOURCE xor TEST_ENTERPRISE must be set to 1!"; exit 1; fi -->
<!-- AUTOMATION: execute=if [ "$TEST_OPEN_SOURCE" = 1 ] && [ "$TEST_ENTERPRISE" = 1 ]; then echo "TEST_OPEN_SOURCE and TEST_ENTERPRISE cannot both be 1!"; exit 1; fi -->

<!-- Cleanup code -->
<!-- AUTOMATION: execute=ORIG_DIR=$PWD; function cleanup() { set +e; cd $ORIG_DIR/mender-server/production; ./run down -v; docker volume rm mender-artifacts mender-db; cd $ORIG_DIR; rm -rf mender-server; } -->
<!-- AUTOMATION: execute=trap cleanup EXIT -->

!!! You can save time by using [hosted Mender](https://hosted.mender.io?target=_blank), a secure Mender server ready to use, maintained by the Mender developers.

This is a step by step guide for deploying the Mender Server for production
environments, and will cover relevant security and reliability aspects of Mender
production installations.  The Mender backend services can be deployed to
production using a skeleton provided in the `production` directory of the
[integration](https://github.com/mendersoftware/integration?target=_blank)
repository. Most of the steps are the same whether you are installing the Open
Source or Enterprise edition of the Mender Server, but there are some extra
steps that are covered in the [Enterprise subsection](#enterprise).

! If you have already installed an Open Source server and wish to upgrade to
! Enterprise, you should follow [the Enterprise upgrade
! guide](upgrading-from-os-to-enterprise) instead of this guide.


## Prerequisites

- A machine with Ubuntu 18.04 (e.g. an instance from AWS EC2 or DigitalOcean) with the following tools installed:
  - git
  - [Docker Engine](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/?target=_blank), version **17.03 or later**.
  - [Docker Compose](https://docs.docker.com/compose/install/?target=_blank), version **1.6 or later**.
- Minimum of 10 GB free disk space and 4 GB RAM available for Mender and its services.
    - This heavily depends on your scale and environment, the supported [Mender Enterprise](https://mender.io/product/mender-enterprise) edition is recommended for larger-scale environments.
- A public IP address assigned and ports 443 and 9000 publicly accessible.
- Allocated DNS names for the Mender API Gateway and the Mender Storage Proxy
  that resolve to the public IP of the Mender server by the devices. By following this guide
  all services will be hosted on the same server, so you can use just one domain name for both.
  If you are just testing you can use a temporary domain name obtained from services like
  [https://ipq.co](https://ipq.co?target=_blank).

If you are setting up a Mender Enterprise server, you will also need:

- An account with Mender in order to evaluate and use the commercial features in
  Mender Enterprise. Please email [contact@mender.io](mailto:contact@mender.io)
  to receive an evaluation account.

!!! It is very likely possible to use other Linux distributions and versions. However, we recommend using this exact environment for running Mender because it is known to work and you will thus avoid any issues specific to your environment if you use this reference.


## Deployment steps

The guide will use a publicly available Mender integration repository. Then
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


### Basic preparation setup

Start off by cloning the Mender integration repository into a local directory
named `mender-server`:

<!--AUTOVERSION: "-b %"/integration -->
```bash
git clone -b master https://github.com/mendersoftware/integration mender-server
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
  part](#enterprise) of the Production installation guide

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
> Pulling mender-mongo (mongo:3.4)...
> 3.4: Pulling from library/mongo
> Digest: sha256:aff0c497cff4f116583b99b21775a8844a17bcf5c69f7f3f6028013bf0d6c00c
> Status: Image is up to date for mongo:3.4
> ...
> Pulling mender-gui (mendersoftware/gui:latest)...
> latest: Pulling from mendersoftware/gui
> b7f33cc0b48e: Already exists
> 31e101b48355: Pull complete
> 307a023cd01f: Pull complete
> 2edcf3035646: Pull complete
> aeb59eb28f90: Pull complete
> ...
> Pulling mender-useradm (mendersoftware/useradm:latest)...
> latest: Pulling from mendersoftware/useradm
> Digest: sha256:3346985a2679b7edd9243363c4b1c291871481f8c6f557ccdc51af58dc6d3a1a
> Status: Image is up to date for mendersoftware/useradm:latest
> Pulling mender-device-auth (mendersoftware/deviceauth:latest)...
> latest: Pulling from mendersoftware/deviceauth
> Digest: sha256:ed47310dc9a86cca70d52c520d565ef9814f39421f2faa02d60bbe8a1dbd63c5
> Status: Image is up to date for mendersoftware/deviceauth:latest
> Pulling mender-api-gateway (mendersoftware/api-gateway:latest)...
> latest: Pulling from mendersoftware/api-gateway
> Digest: sha256:97243de3da950e754ada73abf8c123001c0a0c8b20344256dc7db4c89c0ecd82
> Status: Image is up to date for mendersoftware/api-gateway:latest
> ```

! Using the `run` helper script may fail when local user has insufficient permissions to reach a local docker daemon. Make sure that the Docker installation was completed successfully and the user has sufficient permissions (typically the user must be a member of the `docker` group).

### Certificates and keys

First, set the public domain name of your server (the URL your devices will reach your Mender server on):

<!--AUTOMATION: ignore=use s3.docker.mender.io (localhost) instead-->
```bash
API_GATEWAY_DOMAIN_NAME="mender.example.com"  # NB! replace with your server's public domain name
STORAGE_PROXY_DOMAIN_NAME="$API_GATEWAY_DOMAIN_NAME"  # change if you are hosting the Storage Proxy on a different domain name (not the default)
```
<!--AUTOMATION: execute=API_GATEWAY_DOMAIN_NAME="s3.docker.mender.io" -->
<!--AUTOMATION: execute=STORAGE_PROXY_DOMAIN_NAME="$API_GATEWAY_DOMAIN_NAME" -->

Prepare certificates using the helper script `keygen`:

```bash
CERT_API_CN=$API_GATEWAY_DOMAIN_NAME CERT_STORAGE_CN=$STORAGE_PROXY_DOMAIN_NAME ../keygen
```

> ```
> Generating a 256 bit EC private key
> writing new private key to 'private.key'
> ...
> All keys and certificates have been generated in directory keys-generated.
> Please include them in your docker compose and device builds.
> For more information please see https://docs.mender.io/Administration/Certificates-and-keys.
> ```

Your local directory tree should now look like this:
<!--AUTOMATION: ignore -->
```bash
├── keys-generated
│   ├── certs
│   │   ├── api-gateway
│   │   │   ├── cert.crt
│   │   │   └── private.key
│   │   └── server.crt
│   │   └── storage-proxy
│   │       ├── cert.crt
│   │       └── private.key
│   └── keys
│       ├── deviceauth
│       │   └── private.key
│       └── useradm
│           └── private.key
├── config/enterprise.yml.template
├── config/prod.yml
├── config/prod.yml.template
└── run
```

The production template file `prod.yml` is already configured to load keys and
certificates from locations created by the `keygen` script. If you wish to use a
different set of certificates or keys, please consult the
[relevant documentation](../certificates-and-keys).

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
>  create mode 100644 production/keys-generated/certs/api-gateway/cert.crt
>  create mode 100644 production/keys-generated/certs/api-gateway/private.key
>  create mode 100644 production/keys-generated/certs/server.crt
>  create mode 100644 production/keys-generated/certs/storage-proxy/cert.crt
>  create mode 100644 production/keys-generated/certs/storage-proxy/private.key
>  create mode 100644 production/keys-generated/keys/deviceauth/private.key
>  create mode 100644 production/keys-generated/keys/useradm/private.key
> ```

The API Gateway and Storage Proxy certificates generated here need to be made
available to the Mender client.
Consult the section on [building for production](../../artifacts/yocto-project/building-for-production)
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

!!! The storage location of these volumes depends on your docker configuration. You can check the path for a specific volume by running `docker volume inspect --format '{{.Mountpoint}}' mender-artifacts`.


### Configuration

The deployment configuration in `config/prod.yml` now needs to be updated.


#### Minio

The keys `MINIO_ACCESS_KEY` and `MINIO_SECRET_KEY` control
credentials for uploading artifacts into the object store. Since Minio is a S3 API
compatible service, these settings correspond to Amazon's AWS Access Key ID and
Secret Access Key respectively.

First, generate a secret key for Minio with the `pwgen` utility:

!!! On the Debian family of distributions you can install `pwgen` with `apt-get install pwgen`.

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
see the [administration overview](../overview) for more details. For this reason,
access credentials `DEPLOYMENTS_AWS_AUTH_KEY` and `DEPLOYMENTS_AWS_AUTH_SECRET`
need to be updated and `DEPLOYMENTS_AWS_URI` must point to the domain name of your Storage proxy.

Run the following commands to set `DEPLOYMENTS_AWS_AUTH_KEY` and
`DEPLOYMENTS_AWS_AUTH_SECRET` to the values of `MINIO_ACCESS_KEY`
and `MINIO_SECRET_KEY`, respectively.

```bash
sed -i.bak "s/DEPLOYMENTS_AWS_AUTH_KEY:.*/DEPLOYMENTS_AWS_AUTH_KEY: mender-deployments/g" config/prod.yml
sed -i.bak "s/DEPLOYMENTS_AWS_AUTH_SECRET:.*/DEPLOYMENTS_AWS_AUTH_SECRET: $MINIO_SECRET_KEY_GENERATED/g" config/prod.yml
```
Also, run the following command so `DEPLOYMENTS_AWS_URI` points to your Storage proxy (including the right port, 9000 by default):

```bash
sed -i.bak "s/https:\/\/set-my-alias-here.com/https:\/\/$STORAGE_PROXY_DOMAIN_NAME:9000/g" config/prod.yml
```

After these three commands, the updated entry should look like this (you can again verify with `git diff`):

```yaml
    ...
    mender-deployments:
        ...
        environment:
            DEPLOYMENTS_AWS_AUTH_KEY: mender-deployments
            DEPLOYMENTS_AWS_AUTH_SECRET: ahshagheeD1ooPae
            DEPLOYMENTS_AWS_URI: https://mender.example.com:9000
    ...
```

!! The address used in `DEPLOYMENTS_AWS_URI` must be exactly the same as the one that will be used by devices. The deployments service generates signed URLs for accessing artifact storage. A different hostname or port will result in signature verification failure and download attempts will be rejected.


#### Storage proxy

Add your storage server's DNS name under the key `networks.mender.aliases` key
by running the following command:

```bash
sed -i.bak "s/set-my-alias-here.com/$STORAGE_PROXY_DOMAIN_NAME/g" config/prod.yml
```

The entry should now look like this:

```yaml
    ...
    storage-proxy:
        networks:
            mender:
                aliases:
                    - mender.example.com
    ...

```

You can also change the values for `DOWNLOAD_SPEED` and `MAX_CONNECTIONS`.
See the [section on bandwidth](../bandwidth) for more details on these
settings.



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
git log --oneline master..HEAD
```
> ```
> 7a4de3c production: configuration
> 41273f7 production: adding generated keys and certificates
> 5ad6528 production: initial template
> ```


## Open Source

<!-- Test block for TEST_OPEN_SOURCE=1 -->
<!-- AUTOMATION: execute=if [ "$TEST_OPEN_SOURCE" = 1 ]; then -->

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
> Creating menderproduction_mender-mongo_1
> Creating menderproduction_mender-gui_1
> Creating menderproduction_minio_1
> Creating menderproduction_mender-device-auth_1
> Creating menderproduction_mender-inventory_1
> Creating menderproduction_storage-proxy_1
> Creating menderproduction_mender-useradm_1
> Creating menderproduction_mender-deployments_1
> Creating menderproduction_mender-api-gateway_1
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

<!--AUTOMATION: test=for ((n=0;n<5;n++)); do sleep 3 && test "$(docker ps | grep menderproduction | grep -c -i 'up')" = 12  || ( echo "some containers are not 'Up'" && docker ps && ./run images && ./run logs && exit 1 ); done -->
<!--AUTOMATION: test=./run restart -->
<!--AUTOMATION: test=for ((n=0;n<5;n++)); do sleep 3 && test "$(docker ps | grep menderproduction | grep -c -i 'up')" = 12  || ( echo "some containers are not 'Up'" && docker ps && ./run images && ./run logs && exit 1 ); done -->
<!--AUTOMATION: test=docker ps | grep menderproduction | grep "0.0.0.0:443" -->
<!--AUTOMATION: test=docker ps | grep menderproduction | grep "0.0.0.0:9000" -->

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
> Creating menderproduction_storage-proxy_1 ... done
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
cannot be turned off. Below follows a guide for setting up a single
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
TENANT_ID=$(./run exec mender-tenantadm /usr/bin/tenantadm create-org --name=MyOrganization --username=myusername@host.com --password=mysecretpassword | tr -d '\r') && (echo $TENANT_ID)
```

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
TENANT_TOKEN=$(./run exec mender-tenantadm /usr/bin/tenantadm get-tenant --id $TENANT_ID | jq -r .tenant_token) && (echo $TENANT_TOKEN)
```

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
  server](upgrading-from-os-to-enterprise#migrating-clients)
* [Mender installed on device using a deb
  package](../../client-configuration/installing#configuration-for-hosted-mender-server)
* [Device integration using Yocto
  Project](../../artifacts/yocto-project/variables#mender_tenant_token)
* [Device integration with Debian
  Family](../../artifacts/debian-family#convert-a-raw-disk-image)
* [Modifying an existing prebuilt
  image](../../artifacts/modifying-a-mender-artifact#changing-the-mender-server)


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
git log --oneline master..HEAD
```
> ```
> 76b3d00 production: Enterprise configuration
> 7a4de3c production: configuration
> 41273f7 production: adding generated keys and certificates
> 5ad6528 production: initial template
> ```

<!-- Verification of Enterprise instance -->

<!--AUTOMATION: test=for ((n=0;n<5;n++)); do sleep 3 && test "$(docker ps | grep menderproduction | grep -c -i 'up')" = 13 || ( echo "some containers are not 'Up'" && docker ps && ./run images && ./run logs && exit 1 ); done -->
<!--AUTOMATION: test=./run restart -->
<!--AUTOMATION: test=for ((n=0;n<5;n++)); do sleep 3 && test "$(docker ps | grep menderproduction | grep -c -i 'up')" = 13 || ( echo "some containers are not 'Up'" && docker ps && ./run images && ./run logs && exit 1 ); done -->
<!--AUTOMATION: test=docker ps | grep menderproduction | grep "0.0.0.0:443" -->
<!--AUTOMATION: test=docker ps | grep menderproduction | grep "0.0.0.0:9000" -->

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
> menderproduction_mender-api-gateway_1              /entrypoint.sh                   Up             0.0.0.0:443->443/tcp, 80/tcp
> menderproduction_mender-create-artifact-worker_1   /usr/bin/workflows --confi ...   Up             8080/tcp
> menderproduction_mender-deployments_1              /entrypoint.sh --config /e ...   Up             8080/tcp
> menderproduction_mender-device-auth_1              /usr/bin/deviceauth --conf ...   Up             8080/tcp
> menderproduction_mender-gui_1                      /entrypoint.sh nginx             Up (healthy)   80/tcp
> menderproduction_mender-inventory_1                /usr/bin/inventory --confi ...   Up             8080/tcp
> menderproduction_mender-mongo_1                    docker-entrypoint.sh mongod      Up             27017/tcp
> menderproduction_mender-useradm_1                  /usr/bin/useradm --config  ...   Up             8080/tcp
> menderproduction_mender-workflows-server_1         /usr/bin/workflows --confi ...   Up             8080/tcp
> menderproduction_mender-workflows-worker_1         /usr/bin/workflows --confi ...   Up
> menderproduction_minio_1                           /usr/bin/docker-entrypoint ...   Up (healthy)   9000/tcp
> menderproduction_storage-proxy_1                   /usr/local/openresty/bin/o ...   Up             0.0.0.0:9000->9000/tcp
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
