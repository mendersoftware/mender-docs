---
title: Integration checklist
taxonomy:
    category: docs
---


To ensure that the necessary components for Mender are properly integrated, you should use this checklist to verify each of them in turn. You can run this checklist after you have successfully built all components and correctly booted the device.

Please note that the full checklist is required only for doing full rootfs updates.

## Introduction

This checklist will verify some key functionality aspects of the Mender integration. It will verify that:

* The Mender service launches properly
* Bootloader environment tools are present on the device
* Identify A/B partitions
* Confirm OS switch using bootloader variables
* Identify the transitions state 
  * a) Confirm behavior for the 'successful update' case
  * b) Confirm behavior for the 'failed update and rollback' case


! **Please note** During these steps we will be switching between the two partitions without downloading new content to them. 
! If you don't have a bootable OS on the second partition, nothing will boot once we do the switch.
! One way to overcome this is to do one regular rootfs update after the initial flashing before proceeding with the verification.


## The Mender service launches properly

!!! If you don't need full rootfs updates you only need to verify this step

mender-client is the userspace application responsible for executing the updates.
It runs as a systemd service.
To verify it's successfully running run the following commands and confirm the output:

```
systemctl is-active mender-client
# active

systemctl is-enabled mender-client
# enabled
```

In the remaining verification, we'll manually be executing similar steps to what the mender-client usually does in regular operations to communicate with the bootloader.

To not have the mender-client interfere with the manual verification it's best to disconnect the device from the internet to prevent an update happening during verification time.


## Bootloader environment tools are present on the device

Verify that the two commands to manipulate the bootloader environment are in the path and are executable. These are used by the mender-client to communicate with the bootloader. 

Depending on the bootloader you're using these might be GRUB or uboot specific.
Please run the commands below:

* For GRUB:
    * `grub-mender-grubenv-print`
    * `grub-mender-grubenv-set`
* For U-Boot:
    * `fw_printenv`
    * `fw_setenv`


If you get errors when calling the `set` command without arguments, that's ok.
We will test the setting of variables in the upcoming steps.

For the remaining steps, the GRUB CLI tools will be used, but the verification steps are equivalent when using the uboot tools.

<!--AUTOVERSION: "prior to 4.0 %"/ignore-->
! In Yocto releases prior to 4.0 kirkstone, the names of the GRUB tools were the same as the U-Boot tools. Make sure to take this into account in the remaining examples on this page.



## Identify A/B partitions

Redundant (A/B) partitioning is a requirement for full rootfs updates.
These steps will identify the partitions and check if they align with what is in mender-client configuration.

Please note that depending on the types of disks you're using the actual device names can vary.

Check the partitions set in mender.conf to identify rootfs partitions:

``` bash
cat /var/lib/mender/mender.conf | grep RootfsPart
# "RootfsPartA": "/dev/nvme0n1p2"
# "RootfsPartB": "/dev/nvme0n1p3"
```

! By default mender-client look for [configuration at two locations](../07.Configuration-file/docs.md). One of those is `/var/lib/mender/mender.conf` which is - in the default case - a link to `/data/mender/mender.conf` and doesn't get overwritten during the rootfs update. We recommend keeping the backup of the `RootfsPartA/B` settings in `/var/lib/mender/mender.conf` as it's very rare that you need to change partition names as a result of an update.

Identify the currently active partition with the following command:

``` bash
mount | grep 'on /'
#/dev/nvme0n1p3 on / type ext4 ... ...
```


If the device listed is an ambiguous device, such as `/dev/root`, you can use an alternative method for verifying it. If you call the following series of commands:

```bash
stat -c %D /
# 10303
stat -c %t%02T /dev/nvme0n1p3
# 10303
```

The output of the two commands should be identical. This verifies that the correct partition is mounted as the root device when partition A is active.

At the end of this step, we should have successfully identified the active partition (`nvme0n1p3` in the example) and the inactive partition (`nvme0n1p2`). We will use this info when proceeding with the test.


##  Confirm OS switch using bootloader variables

We will confirm the bootloader can read the environment and is behaving correctly by manually switching to the inactive partition.

In the previous step, we identified the currently running partition to be `nvme0n1p3` and the inactive one `nvme0n1p2`.
Let's manually set the bootloader variable so it boots from the inactive partition on the next reboot.

``` bash
grub-mender-grubenv-set mender_boot_part 2
grub-mender-grubenv-set mender_boot_part_hex 2
reboot
```


After the device boots up verify that you are indeed running on the expected partition:

``` bash
mount | grep 'on /'
#/dev/nvme0n1p2 on / type ext4 ... ...
```

Once that is complete repeat the step to return to the previously active partition:


``` bash
grub-mender-grubenv-set mender_boot_part 3
grub-mender-grubenv-set mender_boot_part_hex 3
reboot
```


## Transition state

In the [Mender state machine workflow](../../06.Artifact-creation/08.Create-a-custom-Update-Module/docs.md#the-state-machine-workflow) the transitional state for the bootloader starts with `ArtifactReboot` and ends with either `ArtifactCommit` or `ArtifactFailure`.

For this verification, this is a period during which the bootloader environmental variables are expected to change - either by mender-client or the bootloader itself - and the bootloader is expected to enact conditional logic. For comparison, in the non-transition state, the bootloader variables are stable. 

To notify the bootloader about the switch to the transitional state we will set the following variables:

``` bash
grub-mender-grubenv-set upgrade_available 1
grub-mender-grubenv-set bootcount 0
```

Setting `upgrade_available` to `1` has multiple side effects:

* the bootloader will start incrementing `bootcount` for every new boot attempt
* mender-client and the bootloader know there is a partitioning switch taking place
    * they can make decisions on when to rollback or commit
* returning the `upgrade_available` to `0` represents the conclusion of the transition state


### Confirm behavior for the successful update case


Once you set the variables from above, confirm your current active partition and reboot:

``` bash
# In the normal update process, at this point mender-client just
# concluded streaming the new version to the inactive partition

# We are currently running the active partition
# Identify active partition
mount | grep 'on /'
#/dev/nvme0n1p3 on / type ext4 ... ...


# Start the transition state
grub-mender-grubenv-set upgrade_available 1
grub-mender-grubenv-set bootcount 0


# Switch to the inactive partition
grub-mender-grubenv-set mender_boot_part 2
grub-mender-grubenv-set mender_boot_part_hex 2

reboot
```


After the reboot the partition changed and the bootcount increased:

``` bash
# Identify the active partition
mount | grep 'on /'
#/dev/nvme0n1p2 on / type ext4 ... ...

grub-mender-grubenv-print bootcount upgrade_available
# bootcount=1
# upgrade_available=1

# All good, concluding the transition state
grub-mender-grubenv-set upgrade_available 0
```


### Confirm behavior for the 'failed update and rollback' case


The starting steps are similar to the successful case:


``` bash
# In the normal update process, at this point mender-client just
# concluded streaming the new version to the inactive partition

# We are currently running the active partition
# Identify the active partition
mount | grep 'on /'
#/dev/nvme0n1p2 on / type ext4 ... ...


# Start the transition state
grub-mender-grubenv-set upgrade_available 1
grub-mender-grubenv-set bootcount 0


# Switch to the inactive partition
grub-mender-grubenv-set mender_boot_part 3
grub-mender-grubenv-set mender_boot_part_hex 3
```


With the distinction where we're going to mess up the kernel on the inactive partition.
This is equivalent to a use case where the new update contains a faulty kernel.


<!--AUTOVERSION: "vmlinuz-%"/ignore-->
``` bash
mkdir /mnt/inactive-partition
mount /dev/nvme0n1p3 /mnt/inactive-partition
mv /mnt/inactive-partition/boot/vmlinuz-5.13.0-35-generic /mnt/inactive-partition/boot/vmlinuz-5.13.0-35-generic.backup

umount /mnt/inactive-partition

reboot
```


The device will attempt to boot, fail and then roll back to booting from the previously working partition.
The bootloader will automatically conclude the transition state in that case:

``` bash
grub-mender-grubenv-print upgrade_available
# upgrade_available=0
```



! **Please note** - the trigger for the rollback is the fact that an unplanned second reboot happened during the transition period, not the fact that the bootloader detected a faulty kernel.
! Any unexpected reboot in the transition period will result in a rollback.


##  Conclusion

If you have verified all the steps you have confirmed your device has the correct partitioning and bootloader integration to do full rootfs updates.
f you have verified all the steps you have confirmed your device has the correct partitioning and bootloader integration to do full rootfs updates.
