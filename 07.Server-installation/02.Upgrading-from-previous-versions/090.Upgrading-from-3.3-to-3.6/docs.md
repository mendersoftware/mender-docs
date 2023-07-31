---
title: Upgrading to Mender 3.6
taxonomy:
category: docs
label: tutorial
---

This is a tutorial for upgrading the Mender Server from version 3.3 and 3.4 to
3.6 in production environments. There are no particular steps you should take,
other than take a backup and run the new version, however there are things to
look out for.

Besides the version specific guidelines below, please make sure you're following
the [suggested upgrade best practices](../docs.md) to reduce the risk of
unpredictable downtime and data loss.

## Before you start

### Current version

Be sure that your current version is either 3.3 or 3.4 and that it works, and Mender Server starts properly.

### Upgrade MongoDB to 5.0 (optional)

We recommend upgrading your MongoDB deployment from 4.4 to 5.0. Please refer to
the [official
documentation](https://www.mongodb.com/docs/manual/release-notes/5.0-upgrade-replica-set/)
for conducting the upgrade. Mender 3.3, 3.4 and 3.6 are all compatible with both
MongoDB 4.4 and 5.0.

## Migrating from 3.3

### useradm database

Be sure that `useradm` database is clean. Especially look out for leftovers from previous
(possible single tenant installations). They can make database migrations to fail.

## Maintenance window

Be prepared for the maintenance window of approximately 15 minutes. This is the maximal
estimated migration time, as seen in the biggest databases we are dealing with.

