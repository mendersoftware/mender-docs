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
! To overcome this, you can perform regular rootfs update after the initial flashing before proceeding with the verification or flash the second partition of storage with the same rootfs the verification.


## The Mender service launches properly

!!! If full rootfs updates are not required, this is the only validation needed.

The Mender Client consists of a number of components and configuration files, with the `mender-auth` userspace application being the responsible for authentication against the Mender Server, and `mender-update` responsible for executing the updates.
By default, both run as systemd services.
To verify the correct installation of the service, run the following commands and confirm the output:

```
systemctl is-active mender-authd
# Output:
# active

systemctl is-enabled mender-authd
# Output:
# enabled

systemctl is-active mender-updated
# Output:
# active

systemctl is-enabled mender-updated
# Output:
# enabled
```

<!--AUTOVERSION: "mendersoftware/mender/blob/%/"/mender-->
In the remaining verification, we will manually be executing similar steps to what the [rootfs-image update module](https://github.com/mendersoftware/mender/blob/5.0.3/support/modules/rootfs-image) usually does in regular operations to communicate with the bootloader.

To avoid the Mender Client interfering with the manual verification it is recommended to disconnect the device from the internet.


## Bootloader environment tools are present on the device

Verify which of the two commands to manipulate the bootloader environment are executable and available in the path. 
These are used by the `rootfs-image` update module to set the bootloader environment.

The executables which the rootfs-image update module expects are bootloader specific. By default, `GRUB` and `uboot` implementations are supported.
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
These steps will identify the partitions and check if they align with what is in the Mender Client configuration (`/var/lib/mender/mender.conf`).

! By default the Mender Client looks for [configuration in two locations](../07.Configuration/docs.md). One of those is `/var/lib/mender/mender.conf` which is - in the default case - a link to the persistent partition `/data/mender/mender.conf` and doesn't get overwritten during the rootfs update. We recommend keeping the backup of the `RootfsPartA/B` settings in `/var/lib/mender/mender.conf` as it is very rare that you need to change partition names as a result of an update.

Please note that the output can vary depending on the actual device names or if you're using PARTUUIDs.

**Partitions as device files**

The device name can vary according to the storage type and kernel naming convention.

``` bash
cat /var/lib/mender/mender.conf | grep RootfsPart
# Output:
# "RootfsPartA": "/dev/nvme0n1p2"
# "RootfsPartB": "/dev/nvme0n1p3"
```


**Partitions as PARTUUIDs**

!! The PARTUUID feature hasn't been tested for u-boot

``` bash
cat /var/lib/mender/mender.conf | grep RootfsPart
# Output:
#   "RootfsPartA": "/dev/disk/by-partuuid/bdcae16f-400a-45e3-b5bb-c9512d3f56c1",
#   "RootfsPartB": "/dev/disk/by-partuuid/bdcae16f-400a-45e3-b5bb-c9512d3f56c2"
```


Identify the currently active partition with the following command:

**Partitions as device files**

``` bash
mount | grep 'on / '
# Output:
#/dev/nvme0n1p2 on / type ext4 ... ...
```

On some devices the rootfs is not listed as a block device but as `/dev/root` or similar. You can use an alternative method for verifying it, by calling the following series of commands:

```bash
stat -c %D /
# Output:
# 10303
stat -c %t%02T /dev/nvme0n1p2
# Output:
# 10303
```

The output of the two commands should be identical. This verifies that the correct partition is mounted as the root device when partition A is active.


**Partitions as PARTUUIDs**

``` bash
dev=$(mount | grep 'on / ' | awk '{print $1}') && echo "$dev $(blkid -s PARTUUID -o value $dev)"
# Output:
# /dev/sda3 bdcae16f-400a-45e3-b5bb-c9512d3f56c2
```


At the end of this step, we need to identify the partition numbering.
This is because the rootfs-image update module passes only partition numbers to the bootloader and not the whole path as seen from `mender.conf`.


**Partitions as device files**

For device files, the partition numbers are whatever is the last number in the device name.

``` bash
cat /var/lib/mender/mender.conf | grep RootfsPart
# Output:                             # Comment for clarification
# "RootfsPartA": "/dev/nvme0n1p2"     ->    Partition A number: 2
# "RootfsPartB": "/dev/nvme0n1p3"     ->    Partition B number: 3
```


**Partitions as PARTUUIDs**

For PARTUUID we need to get that mapping from the grub.cfg: 

``` bash
grep 'mender_rootfsa_part=\|mender_rootfsa_uuid=\|mender_rootfsb_part=\|mender_rootfsb_uuid='    /boot/efi/grub-mender-grubenv/grub.cfg
# Output:                                                       # Comment for clarification
# mender_rootfsa_part=2
# mender_rootfsb_part=3
# mender_rootfsa_uuid=bdcae16f-400a-45e3-b5bb-c9512d3f56c1      ->  Partition A number: 2 (because rootfsa is 2)
# mender_rootfsb_uuid=bdcae16f-400a-45e3-b5bb-c9512d3f56c2      ->  Partition B number: 3 (because rootfsb is 3)
```


!! It doesn't matter which partition happens to be active in your example, if it's reversed from the example just adjust the numbers.


##  Confirm OS switch using bootloader variables

!!! We identified edge cases in certain u-boot board integrations which lead to the introduction of the `mender_boot_part_hex` variable.
!!! To make the verification steps generally applicable, we change both variables in the steps even though they aren't both used in all cases.

We will confirm the bootloader can read the environment and is behaving correctly by manually switching to the inactive partition.

In the previous step, we identified the currently running partition to be `nvme0n1p2` and the inactive one `nvme0n1p3`.
Set the bootloader variables manually so it boots from the currently inactive partition on the next reboot.

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="GRUB"]
``` bash
grub-mender-grubenv-set mender_boot_part 3
grub-mender-grubenv-set mender_boot_part_hex 3
reboot
```
[/ui-tab]
[ui-tab title="UBoot"]
``` bash
fw_setenv mender_boot_part 3
fw_setenv mender_boot_part_hex 3
reboot
```
[/ui-tab]
[/ui-tabs]

After the device boots up verify that you are indeed running on the expected partition:

``` bash
mount | grep 'on / '
# Output:
#/dev/nvme0n1p3 on / type ext4 ... ...
```

After completion, return to the previously active partition by adapting the previous steps:

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="GRUB"]
``` bash
grub-mender-grubenv-set mender_boot_part 2
grub-mender-grubenv-set mender_boot_part_hex 2
reboot
```
[/ui-tab]
[ui-tab title="UBoot"]
``` bash
fw_setenv mender_boot_part 2
fw_setenv mender_boot_part_hex 2
reboot
```
[/ui-tab]
[/ui-tabs]

## Transition state

In the [Mender state machine workflow](../../08.Artifact-creation/08.Create-a-custom-Update-Module/docs.md#the-state-machine-workflow) the transitional state for the bootloader starts with `ArtifactReboot` and ends with either `ArtifactCommit` or `ArtifactFailure`.

During this verification process, it is expected that the bootloader's environment variables will experience changes - either by the rootfs-image update module or the bootloader itself - and the bootloader is expected to enact conditional logic. For comparison, in the non-transition state, the bootloader's variables remain unchanged. 

To notify the bootloader about the switch to the transitional state, we will set the following variables:

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="GRUB"]
``` bash
grub-mender-grubenv-set upgrade_available 1
grub-mender-grubenv-set bootcount 0
```
[/ui-tab]
[ui-tab title="UBoot"]
``` bash
fw_setenv upgrade_available 1
fw_setenv bootcount 0
```
[/ui-tab]
[/ui-tabs]

Setting `upgrade_available` to `1` has multiple side effects:

* The bootloader will increase the `bootcount` by 1 for every new boot attempt
* The rootfs-image update module and the bootloader know there is a partitioning switch taking place
    * They can make decisions on when to rollback or commit
* Returning the `upgrade_available` to `0` marks the end of transition state


### Confirm behavior for the successful update case


As explained on the variables in the previous paragraph, test a full active partition switch including reboot:

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="GRUB"]
``` bash
# In the normal update process, at this point the Mender Client just
# concluded streaming the new version to the inactive partition

# We are currently running the active partition
# Identify active partition
mount | grep 'on / '
# Output:
#/dev/nvme0n1p2 on / type ext4 ... ...


# Start the transition state
grub-mender-grubenv-set upgrade_available 1
grub-mender-grubenv-set bootcount 0


# Switch to the inactive partition
grub-mender-grubenv-set mender_boot_part 3
grub-mender-grubenv-set mender_boot_part_hex 3

reboot
```
[/ui-tab]
[ui-tab title="UBoot"]
``` bash
# In the normal update process, at this point the Mender Client just
# concluded streaming the new version to the inactive partition

# We are currently running the active partition
# Identify active partition
mount | grep 'on / '
# Output:
#/dev/nvme0n1p2 on / type ext4 ... ...


# Start the transition state
fw_setenv upgrade_available 1
fw_setenv bootcount 0


# Switch to the inactive partition
fw_setenv mender_boot_part 3
fw_setenv mender_boot_part_hex 3

reboot
```
[/ui-tab]
[/ui-tabs]

After the reboot the partition changed and the bootcount increased:

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="GRUB"]
``` bash
# Identify the active partition
mount | grep 'on / '
# Output:
#/dev/nvme0n1p3 on / type ext4 ... ...

grub-mender-grubenv-print bootcount upgrade_available
# Output:
# bootcount=1
# upgrade_available=1
```
[/ui-tab]
[ui-tab title="UBoot"]
``` bash
# Identify the active partition
mount | grep 'on / '
# Output:
#/dev/nvme0n1p3 on / type ext4 ... ...

fw_printenv bootcount upgrade_available
# Output:
# bootcount=1
# upgrade_available=1
```
[/ui-tab]
[/ui-tabs]

This is as expected, we can conclude the transition state and confirm the variables remain unchanged:

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="GRUB"]
``` bash
grub-mender-grubenv-set upgrade_available 0
grub-mender-grubenv-set bootcount 0

# This is now the stable state which must remain the same after reboots
grub-mender-grubenv-print
# Output:
# bootcount=0
# mender_boot_part=3
# upgrade_available=0
# mender_boot_part_hex=3

reboot

grub-mender-grubenv-print
# Output:
# bootcount=0
# mender_boot_part=3
# upgrade_available=0
# mender_boot_part_hex=3
```
[/ui-tab]
[ui-tab title="UBoot"]
``` bash
fw_setenv upgrade_available 0
fw_setenv bootcount 0

# This is now the stable state which must remain the same after reboots
fw_printenv bootcount mender_boot_part upgrade_available mender_boot_part_hex
# Output:
# bootcount=0
# mender_boot_part=3
# upgrade_available=0
# mender_boot_part_hex=3

reboot

fw_printenv bootcount mender_boot_part upgrade_available mender_boot_part_hex
# Output:
# bootcount=0
# mender_boot_part=3
# upgrade_available=0
# mender_boot_part_hex=3
```
[/ui-tab]
[/ui-tabs]

### Confirm behavior for the 'failed update and rollback' case


The process initiation is identical to the "success" form.

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="GRUB"]
``` bash
# In the normal update process, at this point the Mender Client just
# concluded streaming the new version to the inactive partition

# We are currently running the active partition
# Identify the active partition
mount | grep 'on / '
# Output:
#/dev/nvme0n1p3 on / type ext4 ... ...


# Start the transition state
grub-mender-grubenv-set upgrade_available 1
grub-mender-grubenv-set bootcount 0


# Switch to the inactive partition
grub-mender-grubenv-set mender_boot_part 2
grub-mender-grubenv-set mender_boot_part_hex 2
```
[/ui-tab]
[ui-tab title="UBoot"]
``` bash
# In the normal update process, at this point the Mender Client just
# concluded streaming the new version to the inactive partition

# We are currently running the active partition
# Identify the active partition
mount | grep 'on / '
# Output:
#/dev/nvme0n1p3 on / type ext4 ... ...


# Start the transition state
fw_setenv upgrade_available 1
fw_setenv bootcount 0


# Switch to the inactive partition
fw_setenv mender_boot_part 2
fw_setenv mender_boot_part_hex 2
```
[/ui-tab]
[/ui-tabs]

To trigger the rollback mechanism, rename the kernel on the inactive partition to break the boot process.
This is equivalent to a use case where the new update contains a faulty kernel.


<!--AUTOVERSION: "vmlinuz-%"/ignore-->
``` bash
mkdir /mnt/inactive-partition
mount /dev/nvme0n1p2 /mnt/inactive-partition
mv /mnt/inactive-partition/boot/vmlinuz-5.13.0-35-generic /mnt/inactive-partition/boot/vmlinuz-5.13.0-35-generic.backup
umount /mnt/inactive-partition

reboot
```


The device will attempt to boot; however, it will fail and trigger a rollback to booting from the previously working partition.
The bootloader will automatically conclude the transition state in that case:

[ui-tabs position="top-left" active="0" theme="lite" ]
[ui-tab title="GRUB"]
``` bash
grub-mender-grubenv-print upgrade_available
# Output:
# upgrade_available=0
```
[/ui-tab]
[ui-tab title="UBoot"]
``` bash
fw_printenv upgrade_available
# Output:
# upgrade_available=0
```
[/ui-tab]
[/ui-tabs]

And the active partition is still the one we started with.

``` bash
# Identify the active partition
mount | grep 'on / '
# Output:
#/dev/nvme0n1p3 on / type ext4 ... ...
```

You can return your kernel back to normal again:

<!--AUTOVERSION: "vmlinuz-%"/ignore-->
``` bash
mkdir /mnt/inactive-partition
mount /dev/nvme0n1p2 /mnt/inactive-partition
mv /mnt/inactive-partition/boot/vmlinuz-5.13.0-35-generic /mnt/inactive-partition/boot/vmlinuz-5.13.0-35-generic.backup
umount /mnt/inactive-partition
```

! **Please note** - the rollback is triggered by an unplanned second reboot that takes place during the transition period, and it is not a result of the bootloader detecting a faulty kernel in any way.

##  Conclusion

If you have successfully followed and verified all the steps, you can confirm that your device has the appropriate partitioning and bootloader integration for complete rootfs updates using Mender.
