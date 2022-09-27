---
title: Backup and restore
taxonomy:
    category: docs
    label: tutorial
---

## Docker volumes

As described in the [installation](../docs.md) chapter, the Mender stack requires
a number of Docker volumes to be created. These volumes can be backed up using
regular docker commands, such as `docker run` or `docker cp`.

A simple example displaying a method of backing up the contents of the
`mender-artifacts` volume is provided below. The command will start a temporary
container using the `alpine:latest` image, mount the `mender-artifacts` volume under
the `/from` path and `$PWD` under `/to`. Then all files and directories under
`/from` are passed through the `tar | gzip` pipeline and saved to
`/to/artifacts-backup.tar.gz`. Once the container exits, the file
`$PWD/artifacts-backup.tar.gz` can be verified to have correct contents.


```bash
docker run -it --rm -v mender-artifacts:/from -v $PWD:/to -w /from \
    alpine \
    ash -c 'tar c * | gzip -9 > /to/artifacts-backup.tar.gz'
```
This method can be applied to all volumes used by the Mender stack.

! Make sure that the relevant services are stopped before backing up respective volumes.

## Database

While it is possible to perform a backup of the databases used by Mender services
with the volume based method outlined in [volumes](#docker-volumes) section, one can also
use DB specific tools to dump and restore database contents.

The Mender integration repository provides tools for dumping and restoring all
databases.

The tool `dump-db` will run a mongo container inside the mender network and dump
the contents of each DB into `$PWD/db-dump/<service-name>` directory.

```bash
../migration/dump-db
```
> ```
> Stopping menderproduction_mender-deployments_1            ... done
> Stopping menderproduction_mender-device-auth_1            ... done
> Stopping menderproduction_mender-workflows-worker_1       ... done
> Stopping menderproduction_mender-deviceconnect_1          ... done
> Stopping menderproduction_mender-useradm_1                ... done
> Stopping menderproduction_mender-inventory_1              ... done
> Stopping menderproduction_mender-create-artifact-worker_1 ... done
> Stopping menderproduction_mender-deviceconfig_1           ... done
> Stopping menderproduction_mender-workflows-server_1       ... done
> Starting mender-mongo ... done
> 2017-06-06T11:20:05.004+0000    writing admin.system.version to
> 2017-06-06T11:20:05.024+0000    done dumping admin.system.version (1 document)
> 2017-06-06T11:20:05.024+0000    writing useradm.migration_info to
> 2017-06-06T11:20:05.024+0000    writing useradm.users to
> 2017-06-06T11:20:05.025+0000    done dumping useradm.migration_info (1 document)
> (output continues...)
> 2017-06-06T11:20:05.315+0000    done dumping deployment_service.migration_info (1 document)
> ```

The tool `restore-db` will run a mongo container inside the mender network to restore
DB dumps previously created with `dump-db`.

```bash
../migration/restore-db
```
> ```
> Stopping menderproduction_mender-deployments_1            ... done
> Stopping menderproduction_mender-device-auth_1            ... done
> Stopping menderproduction_mender-workflows-worker_1       ... done
> Stopping menderproduction_mender-deviceconnect_1          ... done
> Stopping menderproduction_mender-useradm_1                ... done
> Stopping menderproduction_mender-inventory_1              ... done
> Stopping menderproduction_mender-create-artifact-worker_1 ... done
> Stopping menderproduction_mender-deviceconfig_1           ... done
> Stopping menderproduction_mender-workflows-server_1       ... done
> Starting mender-mongo ... done
> 2017-06-06T11:35:09.988+0000    preparing collections to restore from
> 2017-06-06T11:35:10.088+0000    reading metadata for useradm.migration_info from /srv/db-dump/mender-mongo/useradm/migration_info.metadata.json
> (output continues...)
> 2017-06-06T11:35:14.563+0000    no indexes to restore
> 2017-06-06T11:35:14.563+0000    finished restoring deployment_service.migration_info (1 document)
> 2017-06-06T11:35:14.563+0000    done
> ```

! Note `restore-db` and `dump-db` will automatically stop all Mender services that may access respective DBs.

Once the data has been dumped or restored, the services can be started using

```bash
./run up -d
```
> ```
> menderproduction_mender-mongo_1 is up-to-date
> menderproduction_mender-gui_1 is up-to-date
> menderproduction_mender-nats_1 is up-to-date
> menderproduction_minio_1 is up-to-date
> Starting menderproduction_mender-inventory_1 ... 
> Starting menderproduction_mender-workflows-server_1 ... 
> Starting menderproduction_mender-inventory_1              ... done
> Starting menderproduction_mender-workflows-server_1       ... done
> Starting menderproduction_mender-deviceconfig_1           ... done
> Starting menderproduction_mender-workflows-worker_1       ... done
> Starting menderproduction_mender-useradm_1                ... done
> Starting menderproduction_mender-create-artifact-worker_1 ... done
> Starting menderproduction_mender-deviceconnect_1          ... done
> Starting menderproduction_mender-deployments_1            ... done
> Starting menderproduction_mender-device-auth_1            ... done
> menderproduction_mender-api-gateway_1 is up-to-date
> ```

