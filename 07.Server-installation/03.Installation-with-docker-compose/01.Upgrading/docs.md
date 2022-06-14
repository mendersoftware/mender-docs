---
title: Upgrading
taxonomy:
    category: docs
    label: tutorial
---

This is a tutorial for upgrading the Mender Server in production environments. In
general updating is only supported between connected minor versions, and latest
minor to next major version, and this tutorial reflects this. Both the Open Source
and Enterprise editions can be upgraded using this tutorial, but both the old and
the new version must be the same type of server, either both Open Source, or
both Enterprise.

!!! If you are looking to upgrade from Open Source to Enterprise, please visit
!!! [the section on upgrading from Open Source to
!!! Enterprise](../02.Upgrading-from-OS-to-Enterprise/docs.md).

! The upgrade procedure involves some downtime.

## Prerequisites

It is assumed that the installation was performed following the steps
in the [Installation](../docs.md) tutorial. That means that
you currently have:

* a local git repository based
  on [mender-integration](https://github.com/mendersoftware/integration?target=_blank)
* a branch with your production overrides
* all configuration overrides committed to your production branch

As a good engineering practice, it is advisable to perform the upgrade on a
staging environment first. This will allow you to discover potential problems
and allow to exercise the procedure in a safe manner.

The [installation](../docs.md) is largely based on using git and Mender integration
repository. This is the reason why the upgrade procedure follows a regular git
workflow with branching, pulling remote changes and merging locally.

## Backing up existing data

Before upgrading it is advisable to backup existing data and volumes.
Consult the MongoDB and Docker manuals for the necessary steps.

The [Backup and restore](../03.Backup-and-restore/docs.md) chapter provides examples and
introduces example tools provided in Mender integration repository.

## Cleaning up the deviceauth database after device decommissioning.

Before upgrading it is advisable to clean up any leftover devices from the deviceauth database.
These can sometimes happen due to device decommissioning.
You can find instructions on how to clean up the deviceauth database
in the [Troubleshoot](../../../301.Troubleshoot/04.Mender-Server/docs.md) chapter.

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
>    02cd118..75b7831  3.3.0      -> origin/3.3.0
>    06f3212..e9e5df4  3.3.0     -> origin/3.3.0
> ```

<!--AUTOVERSION: "branch named `%` provides"/ignore "e.g. `%`"/ignore-->
For each release there will be a corresponding release branch. For example, the
branch named `2.0.x` provides the 2.0 release setup. Stable releases are tagged,
e.g. `2.0.1`.

Recall from the [installation](../docs.md) tutorial that our local setup was introduced
in a branch that was created from given release version. You can use git commands such
as `git log` and `git diff` to review the changes introduced in upstream branch.
For example:

<!--AUTOVERSION: "HEAD..origin/%"/ignore "HEAD..%"/integration-->
```bash
# to list differences between current HEAD and remote branch
git log HEAD..origin/2.0.x
# to list differences between current HEAD and stable tag
git log HEAD..3.3.0
```

The most important thing to review is the diff between our production template
version and the version present in the repository. For a patch release
there should be none, or just some minor changes. However, when there is a
minor/major release, one can expect the diff to be larger. Example:

<!--AUTOVERSION: "HEAD..%"/integration-->
```bash
# while at the root of repository
user@local$ git diff HEAD..3.3.0 -- template
```

Upgrading our local production branch is performed by issuing a `git merge` command, like this:

<!--AUTOVERSION: "git merge %"/integration-->
```bash
git merge 3.3.0
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

# Upgrading from Mender 2.6 or older

If you are upgrading from Mender 2.6 or older to Mender 2.7 or newer please follow this section.
If you are already running Mender 2.7 or newer you can skip this.

Starting from version 2.7, Mender backend is not using separate service as a Storage Proxy.
Instead, Mender backend uses an API Gateway based on traefik to serve both backend endpoints and artifacts downloads.
Because of this you should update the gateway definition in your production yaml file to include
the domain name of your old Storage Proxy.
The updated entry should look like that:
```yaml
    ...
    mender-api-gateway:
        ...
        networks:
            mender:
                aliases:
                    # mender-api-gateway is a proxy to storage
                    # and has to use exactly the same name as devices
                    # and the deployments service will;
                    #
                    # if devices and deployments will access storage
                    # using https://s3.acme.org:9000, then
                    # set this to https://s3.acme.org:9000
                    - set-my-alias-here.com
    ...
```

<!--AUTOVERSION: "older than %"/ignore "tree/%/storage"/ignore -->
! If you are using mender-client older than 1.7.1 you can face some issues.
! You can find details [here](https://mender.io/blog/deprecating-mender-1-7-0-and-older-on-premise).
! If you still want to use Mender 2.7 or newer with clients older than 1.7.1 you have to set up an additional proxy
! in front of storage service. For that purpose you can include the one provided [here](https://github.com/mendersoftware/integration/tree/master/storage-proxy)
! into your setup (with updated domain name).

## Starting upgraded environment

Once the changes are merged, you can recreate the containers.

First, pull in new container images:

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
> Creating menderproduction_mender-nats_1  ... done
> Creating menderproduction_mender-gui_1   ... done
> Creating menderproduction_minio_1        ... done
> Creating menderproduction_mender-mongo_1 ... done
> Creating menderproduction_mender-deviceconfig_1           ... done
> Creating menderproduction_mender-workflows-worker_1       ... done
> Creating menderproduction_mender-create-artifact-worker_1 ... done
> Creating menderproduction_mender-deviceconnect_1          ... done
> Creating menderproduction_mender-useradm_1                ... done
> Creating menderproduction_mender-inventory_1              ... done
> Creating menderproduction_mender-workflows-server_1       ... done
> Creating menderproduction_mender-device-auth_1            ... done
> Creating menderproduction_mender-api-gateway_1            ... done
> Creating menderproduction_mender-deployments_1            ... done
> ```


## Closing notes

Since the production repository is versioned in git, it is possible to use git
tools and apply typical git workflows, such as pushing, pulling, branching, etc.

Pushing and pulling to/from a company hosted git repository is a great way
to share configuration between staging and production environments. A
configuration can be validated in a staging environment as
relevant changes are committed and pushed to the repository. Once they are validated, a
production environment can pull the changes and apply them locally.
