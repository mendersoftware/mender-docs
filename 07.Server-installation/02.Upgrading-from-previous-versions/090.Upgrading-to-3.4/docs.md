---
title: Upgrading to 3.4
taxonomy:
category: docs
label: tutorial
---

This is a tutorial for upgrading the Mender Server from version 3.3 o 3.4 in production environments.
There are no particular steps you should take, other than take a backup and run the new
version, however there are things to look out for.

## Before you start

### Current version

Be sure that your current version is 3.3 and that it works, and Mender Server starts properly.

### useradm database

Be sure that `useradm` database is clean. Especially look out for leftovers from previous
(possible single tenant installations). They can make database migrations to fail.

### Maintenance window

Be prepared for the maintenance window of approximately 15 minutes. This is the maximal
estimated migration time, as seen in the biggest databases we are dealing with.

## Running the new version

Once the new version is up and running give a UI a full refresh without cache, and enjoy your
new Mender version. You are now ready to upgrade to 3.5.