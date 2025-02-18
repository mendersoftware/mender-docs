---
title: Backup and Restore
taxonomy:
    category: docs
    label: tutorial
---

## Overview

Mender Server stores all data in a MongoDB database. This includes device authentication data, inventory data, users and organization settings. It is important to back up this data regularly to prevent data loss.
Artifacts data are stored in an external storage, such as AWS S3 or Minio, and are not part of the Mender Server database. You should also back up this data separately.

## Backup

!!!!! Always verify the right backup procedure from your database vendor documentation. The following is a general guideline.

The backup procedure for MongoDB is straightforward. You can use the `mongodump` tool to create a backup of the database. The following command creates a backup of the database to the `backup` directory:

```bash
mongodump --host <MONGODB_HOST> --port <MONGODB_PORT> --out /backup/directory
```

You can also backup artifacts data stored in an external storage, such as AWS S3 or Minio, by copying the data to a backup location. For example:

```bash
aws s3 cp s3://<BUCKET_NAME> /backup/directory --recursive
```

## Restore

!!!!! Always verify the right restore procedure from your database vendor documentation. The following is a general guideline.

To restore the MongoDB database from a backup, you can use the `mongorestore` tool. The following command restores the database from the `backup` directory:

```bash
mongorestore --host <MONGODB_HOST> --port <MONGODB_PORT> /backup/directory
```

You can also restore artifacts data stored in an external storage, such as AWS S3 or Minio, by copying the data from the backup location to the original storage location. For example:

```bash
aws s3 cp /backup/directory s3://<BUCKET_NAME> --recursive
```

## Mender Server

At this point you can start the Mender Server services. If you have restored the database to a different server, you may need to update the `global.mongodb.URL` setting in the `mender-server` helm configuration to point to the new MongoDB server.
The same applies for your external storage, if you have restored the artifacts data to a different location, by updating the `global.s3.AWS_BUCKET` setting in the `mender-server` helm configuration.
