---
title: Production installation
taxonomy:
    category: docs
---

This is a step by step guide for deploying the Mender Server for production environments,
and will cover relevant security and reliability aspects of Mender production installations.
The Mender backend services can be deployed to production using a skeleton provided
in the `template` directory
of the [integration](https://github.com/mendersoftware/integration?target=_blank)
repository.


## Prerequisites

- A machine with Ubuntu 16.04 (e.g. an instance from AWS EC2 or DigitalOcean) with
  the following tools installed:
  - git
  - [Docker Engine](https://docs.docker.com/engine/installation/linux/ubuntulinux/?target=_blank), version **1.11 or later**.
  - [Docker Compose](https://docs.docker.com/compose/install/?target=_blank), version **1.6 or later**.
- A public IP address assigned and ports 443 and 9000 publicly accessible.
- Allocated DNS names for the Mender API Gateway and the Mender Storage Proxy
  (for purpose of the guide, it is assumed that you
  own the domains `mender.acme.org` and `s3.acme.org`) that resolve to the public
  IP of current host on the devices.


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
- persistent service data in stored in Docker volumes:
  - artifact storage
  - MongoDB data
- SSL certificate for the API Gateway
- SSL certificate for the Storage Proxy
- a set of keys for generating and validating access tokens

Consult the section on [certificates and keys](../Certificates-and-keys) for details on
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

```bash
git clone https://github.com/mendersoftware/integration mender-server
```
> Cloning into 'deployment'...  
> remote: Counting objects: 1117, done.  
> remote: Compressing objects: 100% (11/11), done.  
> remote: Total 1117 (delta 1), reused 0 (delta 0), pack-reused 1106  
> Receiving objects: 100% (1117/1117), 233.85 KiB | 411.00 KiB/s, done.  
> Resolving deltas: 100% (678/678), done.  
> Checking connectivity... done.  

Enter the directory:

```bash
cd mender-server
```

Prepare a branch where all deployment related changes will be kept:

```bash
git checkout -b my-production-setup
```

Copy deployment configuration template to a new directory named `production`:

```bash
cp -a template production
```

Enter the directory:

```bash
cd production
```

```
ls -l
```
> total 12  
> -rw-rw-r--. 1 user user 4101 01-26 14:06 prod.yml  
> -rwxrwxr-x. 1 user user  161 01-26 14:06 run  

The template includes 2 files:

- `prod.yml` - contains deployment-specific configuration, builds on top of
  `docker-compose.yml` (located at the root of integration repository)

- `run` - a convenience helper that invokes `docker-compose` by passing the required
  compose files; arguments passed to `run` in command line are forwarded
  directly to `docker-compose`

First we need to update paths that are mounted from the root of integration repository:

```bash
sed -i -e 's#/template/#/production/#g' prod.yml
```

At this point all changes should be committed to the repository:

```bash
git add .
```

```bash
git commit -m 'production: initial template'
```
> [my-production-setup 556cc2e] production: initial template  
>  2 files changed, 110 insertions(+)  
>  create mode 100644 production/prod.yml  
>  create mode 100755 production/run  

Assuming that current working directory is still `production`, download
necessary Docker images:

```bash
./run pull
```

> Pulling mender-mongo-device-adm (mongo:3.4)...  
> 3.4: Pulling from library/mongo  
> Digest: sha256:aff0c497cff4f116583b99b21775a8844a17bcf5c69f7f3f6028013bf0d6c00c  
> Status: Image is up to date for mongo:3.4  
> Pulling mender-mongo-device-auth (mongo:3.4)...  
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

! Using the `run` helper script may fail when local user has insufficient permissions to reach a local docker daemon. Make sure that the Docker installation was completed successfully and the user has sufficient permissions (typically the user must be a member of the `docker` group).

### Certificates and keys

Prepare certificates using the helper script `keygen` (replacing `mender.acme.org`
and `s3.acme.org` with your DNS names):

```bash
CERT_API_CN=mender.acme.org CERT_STORAGE_CN=s3.acme.org ../keygen
```

> Generating a 256 bit EC private key  
> writing new private key to 'private.key'  
> ...  
> All keys and certificates have been generated in directory keys-generated.  
> Please include them in your docker compose and device builds.  
> For more information please see https://docs.mender.io/Administration/Certificates-and-keys.  

Your local directory tree should now look like this:

```bash
├── keys-generated
│   ├── certs
│   │   ├── api-gateway
│   │   │   ├── cert.crt
│   │   │   └── private.key
│   │   └── storage-proxy
│   │       ├── cert.crt
│   │       └── private.key
│   └── keys
│       ├── deviceauth
│       │   └── private.key
│       └── useradm
│           └── private.key
├── prod.yml
└── run
```

The production template file `prod.yml` is already configured to load keys and
certificates from locations created by the `keygen` script. If you wish to use a
different set of certificates or keys, please consult the
[relevant documentation](../Certificates-and-keys).

Next, we can add and commit generated keys and certificates:

! Note that the following steps will commit your keys in plaintext to the git history. Make sure to keep all keys secure. Use encryption if needed and decrypt the keys before using them in containers; see the section below on [encrypting keys](#encrypting-keys-optional) for some examples.

```bash
git add keys-generated
```

```bash
git commit -m 'production: adding generated keys and certificates'
```

> [my-production-setup fd8a397] production: adding generated keys and certificates  
>  6 files changed, 108 insertions(+)  
>  create mode 100644 production/keys-generated/certs/api-gateway/cert.crt  
>  create mode 100644 production/keys-generated/certs/api-gateway/private.key  
>  create mode 100644 production/keys-generated/certs/storage-proxy/cert.crt  
>  create mode 100644 production/keys-generated/certs/storage-proxy/private.key  
>  create mode 100644 production/keys-generated/keys/deviceauth/private.key  
>  create mode 100644 production/keys-generated/keys/useradm/private.key  

The API Gateway and Storage Proxy certificates generated here need to be made
available to the Mender client.
Consult the section on [building for production](../../Artifacts/Building-for-production)
for a description on how to include the certificates in the client builds.

!! Only certificates need to be made available to devices or end users. Private keys should never be shared.


#### Encrypting keys (optional)

A simple method for encrypting keys is to
use the [GNU Privacy Guard](https://www.gnupg.org/?target=_blank) tool. Instead of committing
plaintext keys to the repository, we will `tar` and encrypt the entire
`keys-generated` directory structure, then commit it to the repository as a
single binary blob.

The entire directory structure can be encrypted with the following command:

```bash
tar c keys-generated |  gpg --output keys-generated.tar.gpg --symmetric
Enter passphrase:
```

```
rm -rf keys-generated
```

```
ls -l
```
> total 20  
> -rw-rw-r--. 1 user group 5094 01-30 11:24 keys-generated.tar.gpg  
> -rw-rw-r--. 1 user group 5519 01-30 11:08 prod.yml  
> -rwxrwxr-x. 1 user group  173 01-27 14:16 run  

Keys need to be decrypted before bringing the whole environment up:

```bash
gpg --decrypt keys-generated.tar.gpg | tar xvf -
gpg: AES encrypted data
Enter passphrase:
```

When using encryption, commit `keys-generated.tar.gpg` instead of the
`keys-generated` directory structure to the repository, like this:

```bash
git add keys-generated.tar.gpg
```

```bash
git commit -m 'production: adding generated keys and certificates'
```

> [my-production-setup 237af44] production: adding generated keys and certificates  
>  1 file changed, 111 insertions(+)  
>  create mode 100644 production/keys-generated.tar.gpg  


### Persistent storage

Persistent storage of backend services' data is implemented using
named [Docker volumes](https://docs.docker.com/engine/tutorials/dockervolumes/?target=_blank).
The template is configured to mount the following volumes:

- `mender-artifacts` - artifact objects storage
- `mender-deployments-db` - deployments service database data
- `mender-useradm-db` - user administration service database data
- `mender-deviceauth-db` - device authentication service database data
- `mender-deviceadm-db` - device admission service database data
- `mender-inventory-db` - inventory service database data

Each of these volumes need to be created manually with the following commands:

```bash
docker volume create --name=mender-artifacts
```

```bash
docker volume create --name=mender-deployments-db
```

```bash
docker volume create --name=mender-useradm-db
```

```bash
docker volume create --name=mender-inventory-db
```

```bash
docker volume create --name=mender-deviceadm-db
```

```bash
docker volume create --name=mender-deviceauth-db
```

Since we are using local driver for volumes, each volume is based on a host
local directory. It is possible to access files in this directory once a local path
is known. To find the local path for a specific volume run the following
command:

```bash
docker volume inspect --format '{{.Mountpoint}}' mender-artifacts
```
> /var/lib/docker/volumes/mender-artifacts/_data  

The path depends on local docker configuration and may vary between installations.


### Final configuration

The deployment configuration still needs some final touches. Open `prod.yml` in
your favorite editor.


#### Storage proxy

Locate the `storage-proxy` service and add `s3.acme.org` (or your DNS name)
under `networks.mender.aliases` key. The entry should look like this:

```yaml
    ...
    storage-proxy:
        networks:
            mender:
                aliases:
                    - s3.acme.org
    ...

```

You can also change the values for `DOWNLOAD_SPEED` and `MAX_CONNECTIONS`.
See the [section on bandwidth](../Bandwidth) for more details on these
settings.


#### Minio

Locate the `minio` service. The keys `MINIO_ACCESS_KEY` and `MINIO_SECRET_KEY` control
credentials for uploading artifacts into the object store. Since Minio is a S3 API
compatible service, these settings correspond to Amazon's AWS Access Key ID and
Secret Access Key respectively.

Set `MINIO_ACCESS_KEY` to `mender-deployments`. `MINIO_SECRET_KEY` should be set
to a value that can not easily be guessed. We recommend using the `pwgen` utility
for generating the secret. Run the following command to generate a 32-character long secret:

```bash
pwgen 32 1
```
> ahshagheeD1ooPaeT8lut0Shaezeipoo  

The updated entry should look similar to this:

```yaml
    ...
    minio:
        environment:
            # access key
            MINIO_ACCESS_KEY: mender-deployments
            # secret
            MINIO_SECRET_KEY: ahshagheeD1ooPaeT8lut0Shaezeipoo
    ...

```


#### Deployments service

Locate the `mender-deployments` service. The deployments service will upload
artifact objects to `minio` storage via `storage-proxy`,
see the [administration overview](../Overview) for more details. For this reason,
access credentials `DEPLOYMENTS_AWS_AUTH_KEY` and `DEPLOYMENTS_AWS_AUTH_SECRET`
need to be updated and `DEPLOYMENTS_AWS_URI` must point to `s3.acme.org` (or
your DNS name).

!! The address used in `DEPLOYMENTS_AWS_URI` must be exactly the same as the one that will be used by devices. The deployments service generats signed URLs for accessing artifact storage. A different host name or port will result in signature verification failure and download attempts will be rejected.

Set `DEPLOYMENTS_AWS_AUTH_KEY` and `DEPLOYMENTS_AWS_AUTH_SECRET` to the values
of `MINIO_ACCESS_KEY` and `MINIO_SECRET_KEY` respectively. Set
`DEPLOYMENTS_AWS_URI` to point to `https://s3.acme.org:9000`.

The updated entry should look like this:

```yaml
    ...
    mender-deployments:
        ...
        environment:
            DEPLOYMENTS_AWS_AUTH_KEY: mender-deployments
            DEPLOYMENTS_AWS_AUTH_SECRET: ahshagheeD1ooPaeT8lut0Shaezeipoo
            DEPLOYMENTS_AWS_URI: https://s3.acme.org:9000
    ...
```

#### Saving the final configuration

Once all the configuration is complete, commit all changes to the repository:

```bash
git add prod.yml
```

```bash
git commit -m 'production: final configuration'
```

At this point your commit history should look as follows:

```bash
git log --oneline master..HEAD
```
> 7a4de3c production: final configuration  
> 41273f7 production: adding generated keys and certificates  
> 5ad6528 production: initial template  


### Bring it all up

Bring up all services up in detached mode with the following command:

```bash
./run up -d
```
> Creating network "menderproduction_mender" with the default driver  
> Creating menderproduction_mender-mongo-device-auth_1  
> Creating menderproduction_mender-mongo-inventory_1  
> Creating menderproduction_mender-gui_1  
> Creating menderproduction_minio_1  
> Creating menderproduction_mender-mongo-deployments_1  
> Creating menderproduction_mender-mongo-useradm_1  
> Creating menderproduction_mender-mongo-device-adm_1  
> Creating menderproduction_mender-device-auth_1  
> Creating menderproduction_mender-inventory_1  
> Creating menderproduction_storage-proxy_1  
> Creating menderproduction_mender-useradm_1  
> Creating menderproduction_mender-deployments_1  
> Creating menderproduction_mender-device-adm_1  
> Creating menderproduction_mender-api-gateway_1  

!!! Services, networks and volumes have a `menderproduction` prefix, see the note about [docker-compose naming scheme](#docker-compose-naming-scheme) for more details. When using `docker ..` commands, a complete container name must be provided (ex. `menderproduction_mender-deployments_1`).


#### Verification

To verify that the services are running, you can issue the following command:

```bash
./run ps
```

```bash
                   Name                                  Command               State           Ports
-------------------------------------------------------------------------------------------------------------
menderproduction_mender-api-gateway_1         /entrypoint.sh                   Up      0.0.0.0:443->443/tcp
menderproduction_mender-deployments_1         /entrypoint.sh                   Up      8080/tcp
menderproduction_mender-device-adm_1          /usr/bin/deviceadm -config ...   Up      8080/tcp
menderproduction_mender-device-auth_1         /usr/bin/deviceauth -confi ...   Up      8080/tcp
menderproduction_mender-gui_1                 /entrypoint.sh                   Up
menderproduction_mender-inventory_1           /usr/bin/inventory -config ...   Up      8080/tcp
menderproduction_mender-mongo-deployments_1   /entrypoint.sh mongod            Up      27017/tcp
menderproduction_mender-mongo-device-adm_1    /entrypoint.sh mongod            Up      27017/tcp
menderproduction_mender-mongo-device-auth_1   /entrypoint.sh mongod            Up      27017/tcp
menderproduction_mender-mongo-inventory_1     /entrypoint.sh mongod            Up      27017/tcp
menderproduction_mender-mongo-useradm_1       /entrypoint.sh mongod            Up      27017/tcp
menderproduction_mender-useradm_1             /usr/bin/useradm -config / ...   Up      8080/tcp
menderproduction_minio_1                      minio server /export             Up      9000/tcp
menderproduction_storage-proxy_1              /usr/local/openresty/bin/o ...   Up      0.0.0.0:9000->9000/tcp
```


Furthermore, since this is a brand new installation it should be possible to request initial
user login token through the API:

```bash
curl -X POST  -D - --cacert keys-generated/certs/api-gateway/cert.crt https://mender.acme.org:443/api/management/0.1/useradm/auth/login
```

> HTTP/2.0 200  
> server:openresty/1.11.2.2  
> date:Fri, 27 Jan 2017 15:44:53 GMT  
> content-type:application/json; charset=utf-8  
> content-length:734  
> vary:Accept-Encoding  
> x-men-requestid:9a50755b-a246-4128-bfac-e8d20c81a7dc  
> strict-transport-security:max-age=63072000; includeSubdomains; preload  
> x-frame-options:DENY  
> x-content-type-options:nosniff  
>  
> eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJle....  

!!! Note: if your DNS name does not resolve the public IP address of current host, you may need to add appropriate entries to `/etc/hosts`.

At this point you should be able to access [https://mender.acme.org](https://mender.acme.org) with your
web browser.

!!! If you encounter any issues while starting or running your Mender Server, you can take a look at the section for [troubleshooting Mender Server](../../Troubleshooting/Mender-Server).
