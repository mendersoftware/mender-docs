---
title: Upgrading from previous versions
taxonomy:
    category: docs
    label: tutorial
---

Upgrading the production Mender Server installations can be a complex task.
It is supported, and encouraged, but there is a number of 

* upgrade between the adjacent versions, i.e.: if you want to upgrade to 3.5,
 you should first bring your server to version 3.4.
* always have a full backup
* read this document
* perform a test upgrade using a copy of your production database
* prepare for maintenance window
* be prepared for the necessity to run some commands by hand
* verify that the current installation works,
* in particular that it starts up correctly

## Prerequisites

### Taking a full backup

In the following chapters the backup will be always the first item on the agenda.
It is the first step in the upgrade preparation. Ideally, you should have a backup
that you are sure is valid, that is: you have means to restore it to some environment
and verify your setup works.

### Maintenance window

Be prepared that in some complicated upgrades there may be a period when the Mender Server
is not available, or otherwise presents lack of proper service, or incomplete data to the clients.
Exercising our imagination we can come up with a scenario when during a certain upgrade a flood
of request will lead to data inconsistencies. To mitigate that risk it is better to prepare
a maintenance window to complete the upgrade in its due time and place.