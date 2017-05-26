---
title: Upgrading
taxonomy:
    category: docs
---

This is a guide for upgrading the Mender Server in production environments.

! The upgrade procedure involves some downtime.

## Prerequisites

It is assumed that the installation was performed following the steps
in the [Production installation](../production-installation) guide. That means that
you currently have:

* a local git repository based
  on [mender-integration](https://github.com/mendersoftware/integration?target=_blank)
* a branch with your production overrides
* all configuration overrides committed to your production branch

As a good engineering practice, it is advisable to perform the upgrade on a
staging environment first. This will allow you to discover potential problems
and allow to exercise the procedure in a safe manner. 

[Production installation](../production-installation) is largely based on using git and Mender integration
repository. This is the reason why the upgrade procedure follows a regular git
workflow with branching, pulling remote changes and merging locally.

## Backing up existing data

Before upgrading it is advisable to backup existing data and volumes.
Consult the MongoDB and Docker manuals for the necessary steps.

## Updating your local repository

The first step is to upgrade your local repository by pulling changes from the
Mender integration repository. This can be achieved by running `git remote
update origin`.

```bash
git fetch origin --tags
```
> Fetching origin  
> remote: Counting objects: 367, done.  
> remote: Compressing objects: 100% (31/31), done.  
> remote: Total 367 (delta 134), reused 122 (delta 122), pack-reused 214  
> Receiving objects: 100% (367/367), 83.55 KiB | 0 bytes/s, done.  
> Resolving deltas: 100% (214/214), completed with 42 local objects.  
> From https://github.com/mendersoftware/integration  
>    02cd118..75b7831  1.0.x      -> origin/1.0.x  
>    06f3212..e9e5df4  master     -> origin/master  

For each release there will be a corresponding release branch. For example, the
branch named `1.0.x` provides the 1.0 release setup. Stable releases are tagged,
e.g. `1.0.1`.

Recall from the [production installation](../production-installation) guide that our
local setup was introduced in a branch that was created from given release
version. You can use git commands such as `git log` and `git diff` to review the changes
introduced in upstream branch. For example:

```bash
# to list differences between current HEAD and remote branch
git log HEAD..origin/1.0.x
# to list differences between current HEAD and stable tag
git log HEAD..1.0.1
```

The most important thing to review is the diff between our production template
version and the version present in the repository. For a patch release
there should be none, or just some minor changes. However, when there is a
minor/major release, one can expect the diff to be larger. Example:

```bash
# while at the root of repository
user@local$ git diff HEAD..1.0.1 -- template
```

Upgrading our local production branch is performed by issuing a `git merge` command, like this:

```bash
git merge 1.0.1
```
> Merge made by the 'recursive' strategy.  
>  .travis.yml            | 16 ++++++++++++++++  
>  tests/run.sh           |  4 ++--  
>  update                 |  1 -  
>  verify-docker-versions | 29 ++++++++++++++++++++---------  
>  4 files changed, 38 insertions(+), 12 deletions(-)  

!!! Since your local changes are kept in git, it is possible to tag your production version or branch to create pre-merge branches that can be tested in a staging environment.

## Starting upgraded environment

Once the changes are merged, you can recreate the containers. 

First, pull in new container images:

```bash
./run pull
```
> Pulling mender-mongo-device-adm (mongo:3.4)...  
> 3.4: Pulling from library/mongo  
> Digest: sha256:e5a4f6caf4fb6773e41292b56308ed427692add67ffd7c655fdf11a78a72df4e  
> Status: Image is up to date for mongo:3.4  
> Pulling mender-mongo-device-auth (mongo:3.4)...  
> 3.4: Pulling from library/mongo  
> Digest: sha256:e5a4f6caf4fb6773e41292b56308ed427692add67ffd7c655fdf11a78a72df4e  
> Status: Image is up to date for mongo:3.4  
> Pulling minio (mendersoftware/minio:RELEASE.2016-12-13T17-19-42Z)...  
> RELEASE.2016-12-13T17-19-42Z: Pulling from mendersoftware/minio  
> Digest: sha256:0ded6733900e6e09760cd9a7c79ba4981dea6f6b142352719f7a4157b4a3352d  
> Status: Image is up to date for mendersoftware/minio:RELEASE.2016-12-13T17-19-42Z  
> ...  
> Pulling mender-device-auth (mendersoftware/deviceauth:1.0.1)...  
> 1.0.x: Pulling from mendersoftware/deviceauth  
> Digest: sha256:07ed10f6fdee40df1de8e10efc3115cb64b0c190bcf5bcd194b9f34086396058  
> Status: Image is up to date for mendersoftware/deviceauth:1.0.1  
> Pulling mender-gui (mendersoftware/gui:1.0.1)...  
> 1.0.x: Pulling from mendersoftware/gui  
> Digest: sha256:af2d2349f27dd96ca21940672aa3a91335b17153f8c7ef2ca865a9a7fdf2fd22  
> Status: Image is up to date for mendersoftware/gui:1.0.1  
> Pulling mender-api-gateway (mendersoftware/api-gateway:1.0.1)...  
> 1.0.x: Pulling from mendersoftware/api-gateway  
> Digest: sha256:0a2033a57f88afc38253a45301c83484e532047d75858df95d46c12b48f1f2f8  
> Status: Image is up to date for mendersoftware/api-gateway:1.0.1````  

Then stop and remove existing containers:

! Stopping the containers will make the Mender Server temporarily unavailable to devices and users.

```bash
./run stop
```
> Stopping menderproduction_mender-api-gateway_1 ... done  
> Stopping menderproduction_mender-inventory_1 ... done  
> Stopping menderproduction_mender-deployments_1 ... done  
> Stopping menderproduction_mender-device-auth_1 ... done  
> Stopping menderproduction_mender-device-adm_1 ... done  
> Stopping menderproduction_mender-useradm_1 ... done  
> Stopping menderproduction_storage-proxy_1 ... done  
> Stopping menderproduction_mender-mongo-inventory_1 ... done  
> Stopping menderproduction_mender-mongo-deployments_1 ... done  
> Stopping menderproduction_mender-mongo-device-auth_1 ... done  
> Stopping menderproduction_mender-mongo-device-adm_1 ... done  
> Stopping menderproduction_mender-mongo-useradm_1 ... done  
> Stopping menderproduction_mender-gui_1 ... done  
> Stopping menderproduction_minio_1 ... done  

!!! All system data is kept in named Docker volumes. Removing containers does not affect volumes.

```bash
./run rm
```
> Going to remove menderproduction_mender-api-gateway_1, ...  
> Are you sure? [yN] y  
> Removing menderproduction_mender-api-gateway_1 ... done  
> Removing menderproduction_mender-inventory_1 ... done  
> Removing menderproduction_mender-deployments_1 ... done  
> Removing menderproduction_mender-device-auth_1 ... done  
> Removing menderproduction_mender-device-adm_1 ... done  
> Removing menderproduction_mender-useradm_1 ... done  
> Removing menderproduction_storage-proxy_1 ... done  
> Removing menderproduction_mender-mongo-inventory_1 ... done  
> Removing menderproduction_mender-mongo-deployments_1 ... done  
> Removing menderproduction_mender-mongo-device-auth_1 ... done  
> Removing menderproduction_mender-mongo-device-adm_1 ... done  
> Removing menderproduction_mender-mongo-useradm_1 ... done  
> Removing menderproduction_mender-gui_1 ... done  
> Removing menderproduction_minio_1 ... done  

Start the new environment:

```bash
./run up -d
```
> Creating menderproduction_mender-mongo-useradm_1  
> Creating menderproduction_mender-mongo-device-adm_1  
> Creating menderproduction_mender-mongo-deployments_1  
> Creating menderproduction_minio_1  
> Creating menderproduction_mender-gui_1  
> Creating menderproduction_mender-mongo-device-auth_1  
> Creating menderproduction_mender-mongo-inventory_1  
> Creating menderproduction_mender-useradm_1  
> Creating menderproduction_mender-device-adm_1  
> Creating menderproduction_mender-deployments_1  
> Creating menderproduction_storage-proxy_1  
> Creating menderproduction_mender-device-auth_1  
> Creating menderproduction_mender-inventory_1  
> Creating menderproduction_mender-api-gateway_1  


## Upgrading Mender Clients

The Mender Client binary is built into the root file system, so it can be upgraded by
fetching the sources when [building a Yocto Project image](../../artifacts/building-mender-yocto-image).

!! Older Mender clients do not support newer [versions of the Mender Artifact format](../../architecture/mender-artifacts#versions); they will abort the deployment. You can build older versions of the Mender Artifact format to upgrade older Mender clients. See [Write a new Artifact](../../artifacts/modifying-a-mender-artifact#write-a-new-artifact) for an introduction how to do this.



## Closing notes

Since the production repository is versioned in git, it is possible to use git
tools and apply typical git workflows, such as pushing, pulling, branching, etc.

Pushing and pulling to/from a company hosted git repository is a great way
to share configuration between staging and production environments. A
configuration can be validated in a staging environment as
relevant changes are committed and pushed to the repository. Once they are validated, a
production environment can pull the changes and apply them locally.
