---
title: Integration checklist
taxonomy:
    category: docs
---

In order to ensure that the necessary components for Mender are properly integrated, you should use this checklist to verify each of them in turn. You can run this checklist after you have successfully built all components, and correctly booted the device.

!!! This checklist applies if you are using U-Boot or GRUB.

## Introduction

This checklist will verify some key functionality aspects of the Mender integration. It will verify that:

1. Bootloader environment tools are present on the device
2. the bootloader and the environment tools agree on the format for the environment.
3. the bootloader loads the correct kernel from partition A
4. the bootloader loads the correct kernel from partition B
5. the system mounts the correct rootfs when partition A is active
6. the system mounts the correct rootfs when partition B is active
7. rollback works
8. the Mender service launches properly

## The steps

1. As part of the test, we will rename the Linux kernel in one of the partitions to ensure that the correct kernel image is loaded. In your initially booted system, do the following to hide the Linux kernel from the bootloader

   ```bash
   mv /boot/uImage /boot/uImage.testing-backup
   ```

   ! Note that you should update `uImage` to match the kernel image type for your platform.

2. Verify that the two commands to manipulate the environment are in the path and are executable. Calling them with no arguments should give a variable listing and an error about missing variable name, respectively. This verifies that the bootloader environment tools are present on the device.

    * For GRUB:
        * `grub-mender-grubenv-print`
        * `grub-mender-grubenv-set`
    * For U-Boot:
        * `fw_printenv`
        * `fw_setenv`

<!--AUTOVERSION: "prior to 4.0 %"/ignore-->
    ! In Yocto releases prior to 4.0 kirkstone, the names of the GRUB tools were the same as the U-Boot tools. Make sure to take this into account in the remaining examples on this page.

3. Now we will verify that Mender is running. Run the following:

   ```bash
   pidof mender
   ```

   If the Mender daemon has been enabled, it should return a PID. If not, it should return nothing. This verifies that the Mender service is started, if applicable.

4. Now we will look at which filesystem is mounted as the rootfs device. Run `mount` with no arguments. The file system mounted as root (signified by the `<device> on /` entry) should be:

   - `/dev/mmcblk0p2` when using SD card or eMMC storage.
   - `ubi0_0` when using raw flash storage.

   If the device listed is an ambiguous device, such as `/dev/root`, you can use an alternative method for verifying it. If you call the following series of commands:

   ```bash
   stat -c %D /
   stat -c %t%02T /dev/mmcblk0p2
   ```

   The output of the two commands should be identical. This verifies that the correct partition is mounted as the root device when partition A is active.

   ! If you have selected a different device using either `MENDER_ROOTFS_PART_A` or `MENDER_STORAGE_DEVICE` in the Yocto configuration, the `/dev/mmcblk0p2` (or `ubi0_0`) entry may be different, but it should always correspond to the value in `MENDER_ROOTFS_PART_A`.

5. Everything we have tested so far has been for partition A; we will now verify both kernel and rootfs for partition B. Run the following:

   - When using GRUB:
   ```bash
   grub-mender-grubenv-set mender_boot_part 3
   grub-mender-grubenv-set mender_boot_part_hex 3
   ```

   - When using U-Boot and SD card or eMMC storage:
   ```bash
   fw_setenv mender_boot_part 3
   fw_setenv mender_boot_part_hex 3
   ```

   - When using U-Boot and raw flash storage:
   ```bash
   fw_setenv mender_boot_part 1
   fw_setenv mender_boot_part_hex 1
   ```

   ! The number is the number of the second rootfs partition, and corresponds to the last component of the `MENDER_ROOTFS_PART_B` variable. If you've changed this variable in the Yocto configuration, you may need to use a different number.

6. Reboot.

7. Repeat step 4, but this time verify that the root filesystem partition is different than the previous check. This verifies that both the root filesystem partition and kernel image are properly loaded from partition B.

8. Now, restore the kernel image on partition A:

    - When using SD card or eMMC storage:
    ```bash
    mount /dev/mmcblk0p2 /mnt
    mv /mnt/boot/uImage.testing-backup /mnt/boot/uImage
    umount /mnt
    ```

    - When using raw flash storage:
    ```bash
    mount /dev/ubi0_0 /mnt
    mv /mnt/boot/uImage.testing-backup /mnt/boot/uImage
    umount /mnt
    ```

9. Run the following commands:

    - When using GRUB:
    ```bash
    grub-mender-grubenv-set mender_boot_part 2
    grub-mender-grubenv-set mender_boot_part_hex 2
    ```

    - When using U-Boot and SD card or eMMC storage:
    ```bash
    fw_setenv mender_boot_part 2
    fw_setenv mender_boot_part_hex 2
    ```

    - When using raw flash storage:
    ```bash
    fw_setenv mender_boot_part 0
    fw_setenv mender_boot_part_hex 0
    ```

    Once you have run the above commands, we need to tell Mender that there is an upgrade available:

    - When using GRUB:
    ```bash
    grub-mender-grubenv-set upgrade_available 1
    grub-mender-grubenv-set bootcount 0
    ```

    - When using U-Boot:
    ```bash
    fw_setenv upgrade_available 1
    fw_setenv bootcount 0
    ```


    ! The `mender_boot_part` number is the number of the first rootfs partition, and corresponds to the last component of the `MENDER_ROOTFS_PART_A` variable. If you've changed this variable in the Yocto configuration, you may need to use a different number.

10. Reboot.  Now verify that the bootloader has updated the bootcount variable.

    - When using GRUB:
    ```bash
    grub-mender-grubenv-print bootcount
    ```

    - When using U-Boot:
    ```bash
    fw_printenv bootcount
    ```

    This should return the value 1. This step verifies that the bootloader and the bootloader environment tools can properly communicate and agree on the format of the bootloader environment.

11. Repeat step 9.

12. Reboot, but pull the power plug before the system has had time to finish booting. The Mender will service will auto-commit the update, which will defeat the purpose of this test. It is important to reboot the system after the kernel has started booting, but before Mender has started.

13. Restore power, boot, and repeat step 4, again with `/dev/mmcblk0p3` (or `ub0_1`). The detected device should **not** be `/dev/mmcblk0p2` (`ubi0_0`), this indicates that the rollback has not worked. Otherwise this verifies that rollback, indeed, has worked.

That's it! You have now verified compatibility with Mender!
