---
title: Upgrading
taxonomy:
    category: docs
---

This is a tutorial for upgrading the Mender Server in production environments. In
general updating is only supported between connected minor versions, and latest
minor to next major version, and this tutorial reflects this. Both the Open Source
and Enterprise editions can be upgraded using this tutorial, but both the old and
the new version must be the same type of server, either both Open Source, or
both Enterprise.

!!! If you are looking to upgrade from Open Source to Enterprise, please visit
!!! [the section on upgrading from Open Source to
!!! Enterprise](../03.Production-installation/01.Upgrading-from-OS-to-Enterprise/docs.md).

! The upgrade procedure involves some downtime.

## Prerequisites

It is assumed that the installation was performed following the steps
in the [Production installation](../03.Production-installation/docs.md) tutorial. That means that
you currently have:

* a local git repository based
  on [mender-integration](https://github.com/mendersoftware/integration?target=_blank)
* a branch with your production overrides
* all configuration overrides committed to your production branch

As a good engineering practice, it is advisable to perform the upgrade on a
staging environment first. This will allow you to discover potential problems
and allow to exercise the procedure in a safe manner.

[Production installation](../03.Production-installation/docs.md) is largely based on using git and Mender integration
repository. This is the reason why the upgrade procedure follows a regular git
workflow with branching, pulling remote changes and merging locally.

## Backing up existing data

Before upgrading it is advisable to backup existing data and volumes.
Consult the MongoDB and Docker manuals for the necessary steps.

The [Backup and restore](../08.Backup-and-restore/docs.md) chapter provides examples and
introduces example tools provided in Mender integration repository.

## Cleaning up the deviceauth database after device decommissioning.

Before upgrading it is advisable to clean up any leftover devices from the deviceauth database.
These can sometimes happen due to device decommissioning.
You can find instructions on how to clean up the deviceauth database
in the [Troubleshooting](../../201.Troubleshooting/04.Mender-Server/docs.md) chapter.

## Updating your local repository

The first step is to upgrade your local repository by pulling changes from the
Mender integration repository. This can be achieved by running `git remote
update origin`.

```bash
git fetch origin --tags
```
<!--AUTOVERSION: "%      -> origin/%"/integration "%     -> origin/%"/integration-->
> ```
> Fetching origin
> remote: Counting objects: 367, done.
> remote: Compressing objects: 100% (31/31), done.
> remote: Total 367 (delta 134), reused 122 (delta 122), pack-reused 214
> Receiving objects: 100% (367/367), 83.55 KiB | 0 bytes/s, done.
> Resolving deltas: 100% (214/214), completed with 42 local objects.
> From https://github.com/mendersoftware/integration
>    02cd118..75b7831  2.0.x      -> origin/2.0.x
>    06f3212..e9e5df4  master     -> origin/master
> ```

<!--AUTOVERSION: "branch named `%` provides"/ignore "e.g. `%`"/ignore-->
For each release there will be a corresponding release branch. For example, the
branch named `2.0.x` provides the 2.0 release setup. Stable releases are tagged,
e.g. `2.0.1`.

Recall from the [production installation](../03.Production-installation/docs.md) tutorial that our
local setup was introduced in a branch that was created from given release
version. You can use git commands such as `git log` and `git diff` to review the changes
introduced in upstream branch. For example:

<!--AUTOVERSION: "HEAD..origin/%"/ignore "HEAD..%"/integration-->
```bash
# to list differences between current HEAD and remote branch
git log HEAD..origin/2.0.x
# to list differences between current HEAD and stable tag
git log HEAD..master
```

The most important thing to review is the diff between our production template
version and the version present in the repository. For a patch release
there should be none, or just some minor changes. However, when there is a
minor/major release, one can expect the diff to be larger. Example:

<!--AUTOVERSION: "HEAD..%"/integration-->
```bash
# while at the root of repository
user@local$ git diff HEAD..master -- template
```

Upgrading our local production branch is performed by issuing a `git merge` command, like this:

<!--AUTOVERSION: "git merge %"/integration-->
```bash
git merge master
```
> ```
> Merge made by the 'recursive' strategy.
>  .travis.yml            | 16 ++++++++++++++++
>  tests/run.sh           |  4 ++--
>  update                 |  1 -
>  verify-docker-versions | 29 ++++++++++++++++++++---------
>  4 files changed, 38 insertions(+), 12 deletions(-)
> ```

!!! Since your local changes are kept in git, it is possible to tag your production version or branch to create pre-merge branches that can be tested in a staging environment.

## Starting upgraded environment

Once the changes are merged, you can recreate the containers.

First, pull in new container images:

```bash
./run pull
```
<!--AUTOVERSION: "mender-%: Pulling from mendersoftware/deviceauth"/integration "mender-%: Pulling from mendersoftware/gui"/integration "mender-%: Pulling from mendersoftware/api-gateway"/integration "mendersoftware/deviceauth:mender-%"/integration "mendersoftware/gui:mender-%"/integration "mendersoftware/api-gateway:mender-%"/integration-->
> ```
> Pulling mender-mongo (mongo:3.4)...
> 3.4: Pulling from library/mongo
> Digest: sha256:e5a4f6caf4fb6773e41292b56308ed427692add67ffd7c655fdf11a78a72df4e
> Status: Image is up to date for mongo:3.4
> Pulling minio (mendersoftware/minio:RELEASE.2016-12-13T17-19-42Z)...
> RELEASE.2016-12-13T17-19-42Z: Pulling from mendersoftware/minio
> Digest: sha256:0ded6733900e6e09760cd9a7c79ba4981dea6f6b142352719f7a4157b4a3352d
> Status: Image is up to date for mendersoftware/minio:RELEASE.2016-12-13T17-19-42Z
> ...
> Pulling mender-device-auth (mendersoftware/deviceauth:mender-master)...
> mender-master: Pulling from mendersoftware/deviceauth
> Digest: sha256:07ed10f6fdee40df1de8e10efc3115cb64b0c190bcf5bcd194b9f34086396058
> Status: Image is up to date for mendersoftware/deviceauth:mender-master
> Pulling mender-gui (mendersoftware/gui:mender-master)...
> mender-master: Pulling from mendersoftware/gui
> Digest: sha256:af2d2349f27dd96ca21940672aa3a91335b17153f8c7ef2ca865a9a7fdf2fd22
> Status: Image is up to date for mendersoftware/gui:mender-master
> Pulling mender-api-gateway (mendersoftware/api-gateway:mender-master)...
> mender-master: Pulling from mendersoftware/api-gateway
> Digest: sha256:0a2033a57f88afc38253a45301c83484e532047d75858df95d46c12b48f1f2f8
> Status: Image is up to date for mendersoftware/api-gateway:mender-master````
> ```

Then stop and remove existing containers:

! Stopping the containers will make the Mender Server temporarily unavailable to devices and users.

```bash
./run stop
```
> ```
> Stopping menderproduction_mender-api-gateway_1 ... done
> Stopping menderproduction_mender-inventory_1 ... done
> Stopping menderproduction_mender-deployments_1 ... done
> Stopping menderproduction_mender-device-auth_1 ... done
> Stopping menderproduction_mender-useradm_1 ... done
> Stopping menderproduction_storage-proxy_1 ... done
> Stopping menderproduction_mender-mongo_1 ... done
> Stopping menderproduction_mender-gui_1 ... done
> Stopping menderproduction_minio_1 ... done
> ```

!!! All system data is kept in named Docker volumes. Removing containers does not affect volumes.

```bash
./run rm
```
> ```
> Going to remove menderproduction_mender-api-gateway_1, ...
> Are you sure? [yN] y
> Removing menderproduction_mender-api-gateway_1 ... done
> Removing menderproduction_mender-inventory_1 ... done
> Removing menderproduction_mender-deployments_1 ... done
> Removing menderproduction_mender-device-auth_1 ... done
> Removing menderproduction_mender-useradm_1 ... done
> Removing menderproduction_storage-proxy_1 ... done
> Removing menderproduction_mender-mongo_1 ... done
> Removing menderproduction_mender-gui_1 ... done
> Removing menderproduction_minio_1 ... done
> ```

Start the new environment:

```bash
./run up -d
```
> ```
> Creating menderproduction_mender-mongo_1
> Creating menderproduction_minio_1
> Creating menderproduction_mender-gui_1
> Creating menderproduction_mender-useradm_1
> Creating menderproduction_mender-deployments_1
> Creating menderproduction_storage-proxy_1
> Creating menderproduction_mender-device-auth_1
> Creating menderproduction_mender-inventory_1
> Creating menderproduction_mender-api-gateway_1
> ```


## Closing notes

Since the production repository is versioned in git, it is possible to use git
tools and apply typical git workflows, such as pushing, pulling, branching, etc.

Pushing and pulling to/from a company hosted git repository is a great way
to share configuration between staging and production environments. A
configuration can be validated in a staging environment as
relevant changes are committed and pushed to the repository. Once they are validated, a
production environment can pull the changes and apply them locally.
