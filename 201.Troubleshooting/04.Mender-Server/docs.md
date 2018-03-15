---
title: Mender Server
taxonomy:
    category: docs
---

This document details troubleshooting steps for the most common problems with the Mender server.
The first part applies to all installations, while the section below on Production installations
only applies when the Mender server is [installed for production](../../administration/production-installation).

## Cleaning up the deviceauth database after device decommissioning.
It is possible that after the device decommissioning operation there will be some unaccessible and unnecessary data in the deviceauth database.
In this case, you should clean your deviceauth database.

Is is recommended to backup your data before performing the clean up operation.
The [Backup and restore](../../administration/backup-and-restore) chapter provides examples and
introduces example tools provided in Mender integration repository.

To clean up the deviceauth database, run the following from within the integration repository:
```
docker-compose exec mender-device-auth /usr/bin/deviceauth maintenance --decommissioning-cleanup
```

##The virtual QEMU device is not showing up in test mode

When running the Mender server in test mode, as described in the [getting started tutorial](../../getting-started/deploy-to-virtual-devices),
a virtual `vexpress-qemu` device should connect to and ask to join the server.

If this does not happen, please make sure your environment meet the resource requirements
to run the Mender Server. In particular, it is known that the virtual device will not
start if you do not have enough memory.


# Production installations

For the rest of this document, it is assumed that commands are run through production
helper script `run` as detailed in the [production installation documentation](../../administration/production-installation).

## Listing active containers

Listing containers and their statuses is a first step in any troubleshooting
scenario. Assuming current working directory is `production` we can call
production helper script like this:


```
user@local$ ./run ps
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

Alternatively, the same information can be obtained by running `docker ps`
directly with a label filter, like this:

```
user@local$ docker ps --filter label=com.docker.compose.project=menderproduction
CONTAINER ID        IMAGE                                               COMMAND                  CREATED             STATUS              PORTS                    NAMES
c668a91617ea        mendersoftware/api-gateway:latest                   "/entrypoint.sh"         39 minutes ago      Up 39 minutes       0.0.0.0:443->443/tcp     menderproduction_mender-api-gateway_1
9ebb2fc86d0c        mendersoftware/useradm:latest                       "/usr/bin/useradm ..."   40 minutes ago      Up 39 minutes       8080/tcp                 menderproduction_mender-useradm_1
566a2a3c3773        mendersoftware/inventory:latest                     "/usr/bin/inventor..."   40 minutes ago      Up 39 minutes       8080/tcp                 menderproduction_mender-inventory_1
d33f8b4af1bd        mendersoftware/deployments:latest                   "/entrypoint.sh"         40 minutes ago      Up 39 minutes       8080/tcp                 menderproduction_mender-deployments_1
0bb97d64ee4f        mendersoftware/deviceadm:latest                     "/usr/bin/devicead..."   40 minutes ago      Up 39 minutes       8080/tcp                 menderproduction_mender-device-adm_1
1ddbad5520e9        mendersoftware/deviceauth:latest                    "/usr/bin/deviceau..."   40 minutes ago      Up 39 minutes       8080/tcp                 menderproduction_mender-device-auth_1
e7ad33929628        mendersoftware/openresty:1.11.2.2-alpine            "/usr/local/openre..."   40 minutes ago      Up 39 minutes       0.0.0.0:9000->9000/tcp   menderproduction_storage-proxy_1
cdaab7768ec7        mongo:3.4                                           "/entrypoint.sh mo..."   40 minutes ago      Up 40 minutes       27017/tcp                menderproduction_mender-mongo-useradm_1
6502c3c2ae48        mongo:3.4                                           "/entrypoint.sh mo..."   40 minutes ago      Up 40 minutes       27017/tcp                menderproduction_mender-mongo-inventory_1
221778cc0c2b        mongo:3.4                                           "/entrypoint.sh mo..."   40 minutes ago      Up 40 minutes       27017/tcp                menderproduction_mender-mongo-deployments_1
867e76066fad        mendersoftware/gui:latest                           "/entrypoint.sh"         40 minutes ago      Up 40 minutes                                menderproduction_mender-gui_1
00b85b65c157        mongo:3.4                                           "/entrypoint.sh mo..."   40 minutes ago      Up 40 minutes       27017/tcp                menderproduction_mender-mongo-device-adm_1
392362ecb035        mongo:3.4                                           "/entrypoint.sh mo..."   40 minutes ago      Up 40 minutes       27017/tcp                menderproduction_mender-mongo-device-auth_1
54ae287d24ac        mendersoftware/minio:RELEASE.2016-12-13T17-19-42Z   "minio server /export"   40 minutes ago      Up 40 minutes       9000/tcp                 menderproduction_minio_1
```
## Service keeps restarting

!!! Mender service containers are configured with restart policy `on-failure`.

`docker-compose ps` may be helpful with identification of containers that are
restarting:

```
user@local$ ./run ps
                   Name                                  Command                 State              Ports
------------------------------------------------------------------------------------------------------------------
menderproduction_mender-api-gateway_1         /entrypoint.sh                   Up           0.0.0.0:443->443/tcp
menderproduction_mender-deployments_1         /entrypoint.sh                   Restarting
menderproduction_mender-device-adm_1          /usr/bin/deviceadm -config ...   Up           8080/tcp
menderproduction_mender-device-auth_1         /usr/bin/deviceauth -confi ...   Up           8080/tcp
menderproduction_mender-gui_1                 /entrypoint.sh                   Up
menderproduction_mender-inventory_1           /usr/bin/inventory -config ...   Up           8080/tcp
menderproduction_mender-mongo-deployments_1   /entrypoint.sh mongod            Up           27017/tcp
menderproduction_mender-mongo-device-adm_1    /entrypoint.sh mongod            Up           27017/tcp
menderproduction_mender-mongo-device-auth_1   /entrypoint.sh mongod            Up           27017/tcp
menderproduction_mender-mongo-inventory_1     /entrypoint.sh mongod            Up           27017/tcp
menderproduction_mender-mongo-useradm_1       /entrypoint.sh mongod            Up           27017/tcp
menderproduction_mender-useradm_1             /usr/bin/useradm -config / ...   Up           8080/tcp
menderproduction_minio_1                      minio server /export             Up           9000/tcp
menderproduction_storage-proxy_1              /usr/local/openresty/bin/o ...   Up           0.0.0.0:9000->9000/tcp
```
In the case presented above, `mender-deployments` is restarting.

!! `docker-compose` may show `Restating` status for containers that are restarting in a quick succession, if containers restart after a longer while, they may appear as `Up`

In situations where some containers are restarting after running for a longer
while, `docker ps` will show the containers having a shorter lifetime than
others. In the listing show below, `mender-deployments` service uptime is
shorter than that of the other containers:

```
user@local$ docker ps --filter label=com.docker.compose.project=menderproduction
CONTAINER ID        IMAGE                                               COMMAND                  CREATED             STATUS              PORTS                    NAMES
2f4c700923f9        mendersoftware/api-gateway:latest                   "/entrypoint.sh"         4 minutes ago       Up 4 minutes        0.0.0.0:443->443/tcp     menderproduction_mender-api-gateway_1
8f46579aefa4        mendersoftware/deployments:latest                   "/entrypoint.sh"         5 minutes ago       Up 54 seconds       8080/tcp                 menderproduction_mender-deployments_1
7236def09c97        mendersoftware/useradm:latest                       "/usr/bin/useradm ..."   5 minutes ago       Up 5 minutes        8080/tcp                 menderproduction_mender-useradm_1
be9cc9ee74b2        mendersoftware/deviceauth:latest                    "/usr/bin/deviceau..."   5 minutes ago       Up 5 minutes        8080/tcp                 menderproduction_mender-device-auth_1
aa70b181d490        mendersoftware/deviceadm:latest                     "/usr/bin/devicead..."   5 minutes ago       Up 5 minutes        8080/tcp                 menderproduction_mender-device-adm_1
5d84b70d1187        mendersoftware/inventory:latest                     "/usr/bin/inventor..."   5 minutes ago       Up 5 minutes        8080/tcp                 menderproduction_mender-inventory_1
1dc4843ec4db        mendersoftware/openresty:1.11.2.2-alpine            "/usr/local/openre..."   5 minutes ago       Up 5 minutes        0.0.0.0:9000->9000/tcp   menderproduction_storage-proxy_1
fb216139bc60        mongo:3.4                                           "/entrypoint.sh mo..."   5 minutes ago       Up 5 minutes        27017/tcp                menderproduction_mender-mongo-deployments_1
9d6eacd2ae83        mendersoftware/gui:latest                           "/entrypoint.sh"         5 minutes ago       Up 5 minutes                                 menderproduction_mender-gui_1
c318c024bf85        mongo:3.4                                           "/entrypoint.sh mo..."   5 minutes ago       Up 5 minutes        27017/tcp                menderproduction_mender-mongo-useradm_1
c41c857663a7        mongo:3.4                                           "/entrypoint.sh mo..."   5 minutes ago       Up 5 minutes        27017/tcp                menderproduction_mender-mongo-device-auth_1
6a9ae9835e40        mongo:3.4                                           "/entrypoint.sh mo..."   5 minutes ago       Up 5 minutes        27017/tcp                menderproduction_mender-mongo-device-adm_1
2af6f3e56080        mongo:3.4                                           "/entrypoint.sh mo..."   5 minutes ago       Up 5 minutes        27017/tcp                menderproduction_mender-mongo-inventory_1
cc0b330a3cd5        mendersoftware/minio:RELEASE.2016-12-13T17-19-42Z   "minio server /export"   5 minutes ago       Up 5 minutes        9000/tcp                 menderproduction_minio_1
```

### Docker event log

Docker event monitor provides a dynamic view of events. This feature can be
helpful, especially with filters applied. Example view of events registered when
a `mender-deployments` container was restarting (output edited for clarity):

```
user@local$ docker events --filter label=com.docker.compose.project=menderproduction
2017-01-31T09:14:13.291589609+01:00 container die 8f46579aefa47b717c79c4216131391fba7fc938b276d1469d0944691a740d37
   (com.docker.compose.config-hash=80ec90a07e4567c923a6f54126052f4e73a68373113b0dc460d7488b8be9761b,
    com.docker.compose.container-number=1, com.docker.compose.oneoff=False,
    com.docker.compose.project=menderproduction, com.docker.compose.service=mender-deployments,
    com.docker.compose.version=1.10.0, exitCode=1,
    image=mendersoftware/deployments:latest, name=menderproduction_mender-deployments_1)
2017-01-31T09:14:14.699717693+01:00 container start 8f46579aefa47b717c79c4216131391fba7fc938b276d1469d0944691a740d37
   (com.docker.compose.config-hash=80ec90a07e4567c923a6f54126052f4e73a68373113b0dc460d7488b8be9761b,
    com.docker.compose.container-number=1, com.docker.compose.oneoff=False,
    com.docker.compose.project=menderproduction, com.docker.compose.service=mender-deployments,
    com.docker.compose.version=1.10.0,
    image=mendersoftware/deployments:latest, name=menderproduction_mender-deployments_1)
```

## Container logs

Container logs provide access to logging output from the container. Example listing:

```
user@local$ ./run logs --tail 10 mender-deployments
Attaching to menderproduction_mender-deployments_1
mender-deployments_1        | WARNING: ca-certificates.crt does not contain exactly one certificate or CRL: skipping
mender-deployments_1        | time="2017-01-31T08:18:26Z" level=fatal msg="NoCredentialProviders: no valid providers in chain. Deprecated. \n\tFor verbose messaging see aws.Config.CredentialsChainVerboseErrors" file=proc.go func=runtime.main line=183
mender-deployments_1        | WARNING: ca-certificates.crt does not contain exactly one certificate or CRL: skipping
mender-deployments_1        | time="2017-01-31T08:18:57Z" level=fatal msg="NoCredentialProviders: no valid providers in chain. Deprecated. \n\tFor verbose messaging see aws.Config.CredentialsChainVerboseErrors" file=proc.go func=runtime.main line=183
mender-deployments_1        | WARNING: ca-certificates.crt does not contain exactly one certificate or CRL: skipping
mender-deployments_1        | time="2017-01-31T08:19:56Z" level=fatal msg="NoCredentialProviders: no valid providers in chain. Deprecated. \n\tFor verbose messaging see aws.Config.CredentialsChainVerboseErrors" file=proc.go func=runtime.main line=183
mender-deployments_1        | WARNING: ca-certificates.crt does not contain exactly one certificate or CRL: skipping
mender-deployments_1        | time="2017-01-31T08:21:44Z" level=fatal msg="NoCredentialProviders: no valid providers in chain. Deprecated. \n\tFor verbose messaging see aws.Config.CredentialsChainVerboseErrors" file=proc.go func=runtime.main line=183
mender-deployments_1        | WARNING: ca-certificates.crt does not contain exactly one certificate or CRL: skipping
mender-deployments_1        | time="2017-01-31T08:25:15Z" level=fatal msg="NoCredentialProviders: no valid providers in chain. Deprecated. \n\tFor verbose messaging see aws.Config.CredentialsChainVerboseErrors" file=proc.go func=runtime.main line=183
```

The same log can be obtained by running ``docker log`:

```
user@local$ docker logs --tail 10  menderproduction_mender-deployments_1
WARNING: ca-certificates.crt does not contain exactly one certificate or CRL: skipping
time="2017-01-31T08:18:26Z" level=fatal msg="NoCredentialProviders: no valid providers in chain. Deprecated. \n\tFor verbose messaging see aws.Config.CredentialsChainVerboseErrors" file=proc.go func=runtime.main line=183
WARNING: ca-certificates.crt does not contain exactly one certificate or CRL: skipping
time="2017-01-31T08:18:57Z" level=fatal msg="NoCredentialProviders: no valid providers in chain. Deprecated. \n\tFor verbose messaging see aws.Config.CredentialsChainVerboseErrors" file=proc.go func=runtime.main line=183
WARNING: ca-certificates.crt does not contain exactly one certificate or CRL: skipping
time="2017-01-31T08:19:56Z" level=fatal msg="NoCredentialProviders: no valid providers in chain. Deprecated. \n\tFor verbose messaging see aws.Config.CredentialsChainVerboseErrors" file=proc.go func=runtime.main line=183
WARNING: ca-certificates.crt does not contain exactly one certificate or CRL: skipping
time="2017-01-31T08:21:44Z" level=fatal msg="NoCredentialProviders: no valid providers in chain. Deprecated. \n\tFor verbose messaging see aws.Config.CredentialsChainVerboseErrors" file=proc.go func=runtime.main line=183
WARNING: ca-certificates.crt does not contain exactly one certificate or CRL: skipping
time="2017-01-31T08:25:15Z" level=fatal msg="NoCredentialProviders: no valid providers in chain. Deprecated. \n\tFor verbose messaging see aws.Config.CredentialsChainVerboseErrors" file=proc.go func=runtime.main line=183
```

## Inspecting containers

As seen in [container logs](#container-logs) section, `mender-deployments`
service is restarting. The logs suggest there might be missing credentials for
an AWS related service.
From the [production installation](../../administration/production-installation) guide, we can recall
that
`mender-deployments`
[service configuration](../../administration/production-installation#deployments-service) contains
credentials for artifact storage service.

Configuration of current instance of `mender-deployments` can be viewed using
`docker inspect` command. Looking for `Env` (container environment
configuration) in inspect output reveals that `DEPLOYMENTS_AWS_AUTH_KEY` and
`DEPLOYMENTS_AWS_AUTH_SECRET` are unset:

```
user@local$ docker inspect menderproduction_mender-deployments_1 |& less
...
            "StdinOnce": false,
            "Env": [
                "DEPLOYMENTS_AWS_AUTH_KEY",
                "DEPLOYMENTS_AWS_AUTH_SECRET",
                "DEPLOYMENTS_AWS_URI=https://s3.example.com:9000",
                "STORAGE_BACKEND_CERT=/etc/ssl/certs/storage-proxy.crt",
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
...
```

`docker inspect` output contains all information about container instance,
volumes, network, aliases etc.
