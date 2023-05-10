---
menu: Upgrading from OS to Enterprise
title: Upgrading from Open Source to Enterprise
taxonomy:
    category: docs
    label: tutorial
---
<!-- "Upgrading from Open Source to Enterprise" is slightly too big to fit in
    the navigation menu, hence the two titles above. -->

<!-- The variables used in the testing of production installation instructions -->
<!--AUTOMATION: execute=export EXPECTED_COUNT_ENTERPRISE=19 -->
<!--AUTOMATION: execute=export SLEEP_INTERVAL=4 -->
<!--AUTOMATION: execute=export MAX_INTERATIONS=11 -->

<!-- AUTOMATION: execute=if [ "$TEST_ENTERPRISE" -ne 1 ]; then echo "TEST_ENTERPRISE must be set to 1!"; exit 1; fi -->

<!-- Cleanup code -->
<!-- AUTOMATION: execute=ORIG_DIR=$PWD; function cleanup() { set +e; cd $ORIG_DIR/mender-server/production; ./run down -v; docker volume rm mender-artifacts mender-db mender-artifacts-backup mender-db-backup; cd $ORIG_DIR; rm -rf mender-server; } -->
<!-- AUTOMATION: execute=trap cleanup EXIT -->

<!-- Basically a repeat of Open Source setup from the Installation tutorial -->
<!-- AUTOVERSION: "git clone -b %"/integration -->
<!-- AUTOMATION: execute=git clone -b master https://github.com/mendersoftware/integration mender-server -->
<!-- AUTOMATION: execute=cd mender-server -->
<!-- AUTOMATION: execute=git checkout -b my-production-setup -->
<!-- AUTOMATION: execute=cd production -->
<!-- AUTOMATION: execute=cp config/prod.yml.template config/prod.yml -->
<!-- AUTOMATION: execute=sed -i.bak "s/set-my-alias-here.com/s3.docker.mender.io/g" config/prod.yml -->
<!-- AUTOMATION: execute=sed -i.bak 's|DEPLOYMENTS_AWS_URI:.*|DEPLOYMENTS_AWS_URI: https://s3.docker.mender.io|' config/prod.yml -->
<!-- AUTOMATION: execute=CERT_CN=docker.mender.io CERT_SAN=DNS:docker.mender.io,DNS:*.docker.mender.io ../keygen -->
<!-- AUTOMATION: execute=docker volume create --name=mender-artifacts -->
<!-- AUTOMATION: execute=docker volume create --name=mender-db -->
<!-- AUTOMATION: execute=docker volume inspect --format '{{.Mountpoint}}' mender-artifacts -->
<!-- AUTOMATION: execute=sed -i.bak 's/MINIO_ACCESS_KEY:.*/MINIO_ACCESS_KEY: Q3AM3UQ867SPQQA43P2F/' config/prod.yml -->
<!-- AUTOMATION: execute=sed -i.bak 's/MINIO_SECRET_KEY:.*/MINIO_SECRET_KEY: abcssadasdssado798dsfjhkksd/' config/prod.yml -->
<!-- AUTOMATION: execute=sed -i.bak 's/DEPLOYMENTS_AWS_AUTH_KEY:.*/DEPLOYMENTS_AWS_AUTH_KEY: Q3AM3UQ867SPQQA43P2F/' config/prod.yml -->
<!-- AUTOMATION: execute=sed -i.bak 's/DEPLOYMENTS_AWS_AUTH_SECRET:.*/DEPLOYMENTS_AWS_AUTH_SECRET: abcssadasdssado798dsfjhkksd/' config/prod.yml -->
<!-- AUTOMATION: execute=./run up -d -->

This section describes how to upgrade from the Mender Open Source server, to the
Mender Enterprise server. If you have any questions or would like assistance
with upgrading to Mender Enterprise, please email
[contact@mender.io](mailto:contact@mender.io).

!! In this version of Mender, there is no support for migrating data between the
!! Open Source and Enterprise servers. Hence you will **lose all data** on the
!! server by following this tutorial, and all users must be recreated, artifacts
!! must be re-uploaded, and devices re-accepted. The focus in this tutorial will be
!! on how to migrate the device fleet. Support for migrating server data will be
!! added to a later Mender release.

## Creating a backup

The first thing we will do is to create a backup of the Open Source server so
that it can be restored if needed.

Start by shutting down the Mender Server:

<!-- AUTOMATION: execute=cd $ORIG_DIR -->

```bash
cd mender-server/production
./run down -v
```

Create new backup volumes:

```bash
docker volume create --name=mender-artifacts-backup
docker volume create --name=mender-db-backup
```

Clone the contents of the original volumes to the backup volumes:

```bash
docker run --rm -v mender-artifacts:/from        -v mender-artifacts-backup:/to        alpine cp -a /from /to
docker run --rm -v mender-db:/from               -v mender-db-backup:/to               alpine cp -a /from /to
```

This backup can later be restored with this command:

```bash
docker run --rm -v mender-artifacts:/to        -v mender-artifacts-backup:/from        alpine cp -a /from /to
docker run --rm -v mender-db:/to               -v mender-db-backup:/from               alpine cp -a /from /to
```

You can try the above command immediately, it will just restore the already
existing volumes.

## Setting up the Enterprise server

Delete the original volumes:

```bash
docker volume create --name=mender-artifacts
docker volume create --name=mender-db
```

After deleting the volumes, you need to follow [the main tutorial for installing
the Enterprise server](../docs.md#enterprise). You will be directed back to this tutorial
when it is time to migrate the clients.

<!-- AUTOMATION: execute=cp config/enterprise.yml.template config/enterprise.yml -->
<!-- AUTOMATION: execute=./run up -d -->
<!-- AUTOMATION: execute=sleep 30 -->


## Migrating clients

With Mender Enterprise, each device needs to have a tenant token associated with
it. When upgrading from Open Source however, the devices that are already
deployed will be lacking this token. Therefore we need to use a special default
tenant token which will automatically be assigned to all clients that try to
connect without a tenant token.

1. Fetch the tenant token using the **tenant ID** that you obtained while
   [creating the first organization and
   user](../docs.md#creating-the-first-organization-and-user) (replace `$TENANT_ID`
   accordingly):

   <!-- AUTOMATION: execute=TENANT_ID=$( ( ./run exec -T mender-tenantadm /usr/bin/tenantadm create-org --name=MyOrganization --username=myusername@host.com --password=mysecretpassword ) | tr -d '\r' ) -->
   <!--AUTOMATION: test=test -n "$TENANT_ID" -->
   <!-- AUTOMATION: execute=sleep 10 -->

   <!-- Trick to capture the output. The `tr` is because Go prints with Windows
   line endings for whatever reason. -->
   <!-- AUTOMATION: execute=TENANT_TOKEN=$( ( -->
   ```bash
   ./run exec -T mender-tenantadm /usr/bin/tenantadm get-tenant --id $TENANT_ID | jq -r .tenant_token
   ```
   <!-- AUTOMATION: execute=) | tr -d '\r' ) -->
   <!--AUTOMATION: test=test -n "$TENANT_TOKEN" -->

   > eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW5kZXIudGVuYW50IjoiNWQ4MzM1MzJkMTMwNTgwMDI4NDhmZmRmIiwia<br>
   XNzIjoiTWVuZGVyIiwic3ViIjoiNWQ4MzM1MzJkMTMwNTgwMDI4NDhmZmRmIn0.HJDGHzqZqbosAYyJpSIEeL0W4HMiOmb15ETnu<br>
   ChxE0i7ahW49dZZlQNJBKLkLzuESDxXnmQbQwsSGP6t32pGkeHVXTPjrSjhtMPC80NiibNG3f-QATw9I8YgG2SBd5xaKl17qdta1<br>
   nGi80T2UKrwlzqLHR7wNed10ss3NgJDIDvrm89XO0Rg6jpFZsHCPyyK1c8-Vn8zZjW5azZLNSgtgSLSmFQguQLRRXL2x12VEcmez<br>
   tFY0kJnhGtN07CD3XXxcz0BpWbevDYOPOEUusGd2KpLK2Y4QU8RdngqNtRe7SppG0fn6m6tKiifrPDAv_THCEG6dvpMHyIM77vGI<br>
   PwvV4ABGhZKRAlDe1R4csJQIbhVcTWMGcoZ4bKH-zDK0900_wWM53i9rkgNFDM470i6-d1oqfaCPcbiniKsq1HcJRZsIVNJ1edDo<br>
   vhQ6IbffPRCw-Au_GlnPTn_czovJqSa3bgwrJguYRIKJGWhHgx0e3j795oJ08ks2Mp3Rshbv4da

2. Shut down the server:
   ```bash
   ./run down
   ```

3. In `config/enterprise.yml`, locate the `DEVICEAUTH_DEFAULT_TENANT_TOKEN`
   variable, and make sure its value is set to the **tenant token** that was
   fetched in the previous step

   <!-- AUTOMATION: execute=sed -i.bak -e "s;DEVICEAUTH_DEFAULT_TENANT_TOKEN:;DEVICEAUTH_DEFAULT_TENANT_TOKEN: $TENANT_TOKEN;" config/enterprise.yml -->

4. Start the server again:
   ```bash
   ./run up -d
   ```

5. To finalize the upgrade follow the steps in [the Enterprise installation
   tutorial from saving the enterprise
   configuration](../docs.md#saving-the-enterprise-configuration).

<!-- Verification -->

<!--AUTOMATION: execute=function CONTAINERS_COUNT_TEST() { EXPECTED="$(./run config --services | sort)"; ACTUAL="$(./run ps --services --filter 'status=running' | sort)"; if [ "$EXPECTED" != "$ACTUAL" ]; then echo "Not all expected services are running ($(echo "$ACTUAL" | wc -w)/$(echo "$EXPECTED" | wc -w))"; return 1; else return 0; fi } -->
<!--AUTOMATION: test=CONTAINERS_COUNT_TEST; -->
<!--AUTOMATION: test=./run stop -->
<!--AUTOMATION: test=./run up -d -->
<!--AUTOMATION: test=CONTAINERS_COUNT_TEST; -->
<!--AUTOMATION: test=docker ps | grep menderproduction | grep "0.0.0.0:443" -->


## Optional: Migrating away from default tenant token

After the Enterprise server has been set up and verified to work correctly, it
is recommended to switch to tenant tokens on each device, as opposed to the
default tenant token that was configured earlier in this tutorial. This gives a
small security benefit, by completely blocking devices that don't have a tenant
token, and prevents devices showing up in the default organization by mistake,
for example if the tenant token has been misspelled.

In order to migrate to tenant tokens on the device, an update must be made to
**all** devices. The update must contain the the tenant token of the default
organization. See one of these sections for details on how to include tenant
tokens using various client integration methods:

* [Mender installed on device using a deb
  package](../../../03.Client-installation/02.Install-with-Debian-package/docs.md)
* [Device integration using Yocto
  Project](../../../05.Operating-System-updates-Yocto-Project/99.Variables/docs.md#mender_tenant_token)
* [Device integration with Debian
  Family](../../../04.Operating-System-updates-Debian-family/03.Customize-Mender/docs.md)
* [Modifying an existing prebuilt
  image](../../../06.Artifact-creation/03.Modify-an-Artifact/docs.md)

Once all devices have been migrated, the `DEVICEAUTH_DEFAULT_TENANT_TOKEN`
should be configured empty.

<!-- AUTOMATION: ignore="We're not testing this part currently" -->
1. Shut down the server:
   ```bash
   ./run down
   ```

2. In `config/enterprise.yml`, locate the `DEVICEAUTH_DEFAULT_TENANT_TOKEN`
   variable, and make sure it is empty

<!-- AUTOMATION: ignore="We're not testing this part currently" -->
3. Bring up the server again:
   ```bash
   ./run up -d
   ```

! It's important that **all** devices are migrated before removing the default
! tenant token, or you will lose access to these devices unless it is
! reinstated.
