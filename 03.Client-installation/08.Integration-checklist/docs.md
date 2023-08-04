---
title: Integration checklist
taxonomy:
    category: docs
---


To ensure that the necessary components for Mender are properly integrated, you should use this checklist to verify each of them in turn. You can run this checklist after you have successfully built all components and correctly booted the device.


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

The Mender Client consists of a number of components and configuration files, with the `mender-client` userspace application being the core responsible for executing the updates.
By default, it runs as a systemd service.
To verify the correct installation of the service, run the following commands and confirm the output:

```
systemctl is-active mender-client
# Output:
# active

systemctl is-enabled mender-client
# Output:
# enabled
```

In the remaining verification, we will manually be executing similar steps to what the Mender Client usually does in regular operations to communicate with the bootloader.

To avoid the Mender Client interfering with the manual verification it is recommended disconnect the device from the internet.


## Bootloader environment tools are present on the device

Verify that the two commands to manipulate the bootloader environment are in the path and are executable. These are used by the Mender Client to communicate with the bootloader. 

The executables which the Mender Client expects are bootloader specific. By default, `GRUB` and `uboot` implementations are supported.
Please run the commands below:

* For GRUB:
    * `grub-mender-grubenv-print`
    * `grub-mender-grubenv-set`
* For U-Boot:
    * `fw_printenv`
    * `fw_setenv`


Errors upon calling the `set` command without arguments are expected and can be ignored, this step only checks the executable form.
We will test the setting of variables in the upcoming steps.

For the remaining steps, the GRUB CLI tools will be used, but the verification steps are equivalent when using the uboot tools.

<!--AUTOVERSION: "prior to 4.0 %"/ignore-->
! In Yocto releases prior to 4.0 kirkstone, the names of the GRUB tools were the same as the U-Boot tools. Make sure to take this into account in the remaining examples on this page.



## Identify A/B partitions

Redundant (A/B) partitioning is a requirement for full rootfs updates.
These steps will identify the partitions and check if they align with what is in the Mender Client configuration.

Please note that depending on the types of storage the actual device names can vary.

Check the partitions set in `mender.conf` to identify rootfs partitions:

``` bash
cat /var/lib/mender/mender.conf | grep RootfsPart
# Output:
# "RootfsPartA": "/dev/nvme0n1p2"
# "RootfsPartB": "/dev/nvme0n1p3"
```

! By default the Mender Client looks for [configuration in two locations](../07.Configuration-file/docs.md). One of those is `/var/lib/mender/mender.conf` which is - in the default case - a link to the persistent partition `/data/mender/mender.conf` and doesn't get overwritten during the rootfs update. We recommend keeping the backup of the `RootfsPartA/B` settings in `/var/lib/mender/mender.conf` as it is very rare that you need to change partition names as a result of an update.

Identify the currently active partition with the following command:

``` bash
mount | grep 'on /'
# Output:
#/dev/nvme0n1p3 on / type ext4 ... ...
```


On some devices the rootfs is not listed as a block device but as `/dev/root` or similar. You can use an alternative method for verifying it, by calling the following series of commands:

```bash
stat -c %D /
# Output:
# 10303
stat -c %t%02T /dev/nvme0n1p3
# Output:
# 10303
```

The output of the two commands should be identical. This verifies that the correct partition is mounted as the root device when partition A is active.

At the end of this step, we should have successfully identified the active partition (`nvme0n1p3` in the example) and the inactive partition (`nvme0n1p2`). We will use this info when proceeding with the test.


##  Confirm OS switch using bootloader variables

!!! We identified edge cases in certain u-boot board integrations which lead to the introduction of the `mender_boot_part_hex` variable.
!!! To make the verification steps generally applicable, we change both variables in the steps event though they aren't both used in all cases.

We will confirm the bootloader can read the environment and is behaving correctly by manually switching to the inactive partition.

In the previous step, we identified the currently running partition to be `nvme0n1p3` and the inactive one `nvme0n1p2`.
Set the bootloader variables manually so it boots from the currently inactive partition on the next reboot.

``` bash
grub-mender-grubenv-set mender_boot_part 2
grub-mender-grubenv-set mender_boot_part_hex 2
reboot
```


After the device boots up verify that you are indeed running on the expected partition:

``` bash
mount | grep 'on /'
# Output:
#/dev/nvme0n1p2 on / type ext4 ... ...
```

After completion, return to the previously active partition by adapting the previous steps:


``` bash
grub-mender-grubenv-set mender_boot_part 3
grub-mender-grubenv-set mender_boot_part_hex 3
reboot
```


## Transition state

In the [Mender state machine workflow](../../06.Artifact-creation/08.Create-a-custom-Update-Module/docs.md#the-state-machine-workflow) the transitional state for the bootloader starts with `ArtifactReboot` and ends with either `ArtifactCommit` or `ArtifactFailure`.

For this verification, this is a period during which the bootloader environmental variables are expected to change - either by the Mender Client or the bootloader itself - and the bootloader is expected to enact conditional logic. For comparison, in the non-transition state, the bootloader variables are stable. 

To notify the bootloader about the switch to the transitional state we will set the following variables:

``` bash
grub-mender-grubenv-set upgrade_available 1
grub-mender-grubenv-set bootcount 0
```

Setting `upgrade_available` to `1` has multiple side effects:

* the bootloader will start incrementing `bootcount` for every new boot attempt
* the Mender Client and the bootloader know there is a partitioning switch taking place
    * they can make decisions on when to rollback or commit
* returning the `upgrade_available` to `0` represents the conclusion of the transition state


### Confirm behavior for the successful update case


As explained on the variables in the previous paragraph, test a full active partition switch including reboot:

``` bash
# In the normal update process, at this point the Mender Client just
# concluded streaming the new version to the inactive partition

# We are currently running the active partition
# Identify active partition
mount | grep 'on /'
# Output:
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
# Output:
#/dev/nvme0n1p2 on / type ext4 ... ...

grub-mender-grubenv-print bootcount upgrade_available
# Output:
# bootcount=1
# upgrade_available=1

# All good, concluding the transition state
grub-mender-grubenv-set upgrade_available 0
```


### Confirm behavior for the 'failed update and rollback' case


The process initiation is identical to the "success" form.


``` bash
# In the normal update process, at this point the Mender Client just
# concluded streaming the new version to the inactive partition

# We are currently running the active partition
# Identify the active partition
mount | grep 'on /'
# Output:
#/dev/nvme0n1p2 on / type ext4 ... ...


# Start the transition state
grub-mender-grubenv-set upgrade_available 1
grub-mender-grubenv-set bootcount 0


# Switch to the inactive partition
grub-mender-grubenv-set mender_boot_part 3
grub-mender-grubenv-set mender_boot_part_hex 3
```


To trigger the rollback mechanism, rename the kernel on the inactive partition to break the boot process.
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
# Output:
# upgrade_available=0
```



! **Please note** - the rollback is triggered by an unplanned second reboot that takes place during the transition period, and it is not a result of the bootloader detecting a faulty kernel in any way.

##  Conclusion

If you have verified all the steps you have confirmed your device has the correct partitioning and bootloader integration to do full rootfs updates.
