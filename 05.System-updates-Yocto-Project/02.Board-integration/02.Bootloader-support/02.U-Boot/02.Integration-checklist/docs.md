---
title: Integration checklist
taxonomy:
    category: docs
---

In order to ensure that the necessary components for Mender have been integrated correctly, use this checklist to verify each of them in turn. Use this when all components have been built successfully, and the device has booted correctly.

!!! This checklist applies only if you are using U-Boot. If you are using another bootloader, such as GRUB, this section can be skipped.

## What is verified

This checklist will verify some key functionality aspects of the Mender integration. It will verify that:

1. libubootenv tools are present on the device
2. the U-Boot bootloader and libubootenv agree on the format for the U-Boot environment. The format of the U-Boot environment is checksummed and highly device dependent, which is why this check is necessary
3. the correct kernel is loaded from partition A
4. the correct kernel is loaded from partition B
5. the correct rootfs is mounted when partition A is active
6. the correct rootfs is mounted when partition B is active
7. rollback works
8. the Mender daemon is started as a service

## The steps

!!! Steps 1-4 can be skipped when verifying [raw flash](../../../03.Raw-flash/docs.md) integration.

1. As part of the test, we will need two different Linux kernels, in order to verify that both are booted correctly when they should. Therefore, before building the images you will test with, run the commands:

   ```bash
   bitbake -c cleansstate linux-yocto core-image-full-cmdline
   ```

   ! Note that `core-image-full-cmdline` should be switched to whatever image recipe you are testing with.

   ! Note that `linux-yocto` may need to be switched with the particular kernel being used with your device.

   Then build the image normally.

2. Copy the resulting `.sdimg` file to a safe location, for example `base-image.sdimg` and then repeat step 1.

3. Run the following commands:

   ```bash
   sudo kpartx -av base-image.sdimg
   sudo dd if=tmp/deploy/images/<machine>/<image>.ext4 of=/dev/mapper/loop0p3
   sync
   sudo kpartx -d base-image.sdimg
   ```

   ! The first number in `loop0p3` may change depending on devices in your system. Please adjust based on the output of the `kpartx` command.
   
   ! The last number in `loop0p3` should correspond to the partition number of the second rootfs partition, and may need to be adjusted if `MENDER_ROOTFS_PART_B` has been changed.

   ! The `kpartx` tool may require installation before it can be used.

   ! Some Linux distributions may try to auto-mount the devices that `kpartx` maps. If so you need to unmount them again manually before calling `kpartx -d`.

   The reason for doing this manual image patching is to have two kernels in the image with differing build dates, which will be useful for verification later.

4. Flash the `base-image.sdimg` image to the device and boot it.

5. Verify that the two commands `fw_printenv` and `fw_setenv` are in the path and are executable. Calling them with no arguments will should give a variable listing and an error about missing variable name, respectively. This verifies that libubootenv tools are present on the device.

6. Now we will test that storing and reading values in the U-Boot environment works. Run:

   ```bash
   fw_setenv mender_linux_test 1
   ```

7. Reboot, and interrupt U-Boot so you get the U-Boot prompt.

8. Run:

   ```bash
   printenv mender_linux_test
   ```

   The output should be:

   ```bash
   mender_linux_test=1
   ```

   in other words the same value that was set earlier.

9. While still at the U-Boot prompt, run:

   ```bash
   setenv mender_uboot_test 1
   saveenv
   run bootcmd
   ```

10. You should be back inside Linux now, so run:

    ```bash
    fw_printenv mender_uboot_test
    ```

    The output should be:

    ```bash
    mender_uboot_test=1
    ```

    in other words the same value that was set earlier. This verifies that U-Boot the bootloader, and libubootenv agree on format for the U-Boot environment.

11. Now we will verify that Mender is running. Run the following:

    ```bash
    pidof mender
    ```

    If Mender has been enabled as a daemon, either through inheriting `mender-full` or enabling the `mender-systemd` feature in `MENDER_FEATURES_ENABLE`, it should return a PID. If not, it should return nothing. This verifies that Mender is started as a service if applicable.

12. Now we verify that the booted kernel is from the rootfs. The easiest way to check this is to check the build date, which can be seen by running:

    ```bash
    cat /proc/version
    ```

    Make sure it matches the build date and time of the first kernel you just built, and not an older one. Make a note of this time, as you will need it later. This verifies that the correct kernel is loaded from partition A.

13. Now we will look at which rootfs is mounted. Run `mount` with no arguments. The file system mounted as root (signified by the `<device> on /` entry) should be:

    - `/dev/mmcblk0p2` when using SD card or eMMC storage.
    - `ubi0_0` when using raw flash storage.

    If the device listed is an ambiguous device, such as `/dev/root`, you can use an alternative method for verifying it. If you call the following series of commands:

    ```bash
    stat -c %D /
    stat -c %t%02T /dev/mmcblk0p2
    ```

    The output of the two commands should be identical. This verifies that the correct rootfs is mounted when partition A is active.

    ! If you have selected a different device using either `MENDER_ROOTFS_PART_A` or `MENDER_STORAGE_DEVICE` in the Yocto configuration, the `/dev/mmcblk0p2` (or `ubi0_0`) entry may be different, but it should always correspond to the value in `MENDER_ROOTFS_PART_A`.

14. Everything we have tested so far has been for partition A; we will now verify both kernel and rootfs for partition B. Run the following:

    - When using SD card or eMMC storage:
    ```bash
    fw_setenv mender_boot_part 3
    fw_setenv mender_boot_part_hex 3
    ```

    - When using raw flash storage:
    ```bash
    fw_setenv mender_boot_part 1
    fw_setenv mender_boot_part_hex 1
    ```

    ! The number is the number of the second rootfs partition, and corresponds to the last component of the `MENDER_ROOTFS_PART_B` variable. If you've changed this variable in the Yocto configuration, you may need to use a different number.

15. Reboot.

16. Repeat step 12, but this time verify that the build date is later than the first time you did this step. This is because we replaced the kernel of the second rootfs partition with a newer one. This verifies that the correct kernel is loaded from partition B.

    !!! In the case of raw flash storage, the second rootfs was not updated, hence the build time listed in `/proc/version` will be the same as for the first partition.

17. Repeat step 13, but this time using `/dev/mmcblk0p3` (or `ubi0_1`). This verifies that the correct rootfs is mounted when partition B is active.

    ! As in the previous step, `/dev/mmcblk0p3` (or `ubi0_1`) may be different if `MENDER_ROOTFS_PART_B` or `MENDER_STORAGE_DEVICE` has been changed.

18. Run the following commands:

    - When using SD card or eMMC storage:
    ```bash
    fw_setenv mender_boot_part 2
    fw_setenv mender_boot_part_hex 2
    ```

    - When using raw flash storage:
    ```bash
    fw_setenv mender_boot_part 0
    fw_setenv mender_boot_part_hex 0
    ```

    Once the commands above have been run, we need to tell Mender that there is an upgrade available:

    ```bash
    fw_setenv upgrade_available 1
    fw_setenv bootcount 0
    ```


    ! The `mender_boot_part` number is the number of the first rootfs partition, and corresponds to the last component of the `MENDER_ROOTFS_PART_A` variable. If you've changed this variable in the Yocto configuration, you may need to use a different number.

19. Reboot, but pull the power plug before the system has had time to finish booting. Mender will auto-commit the update if it is enabled as a service, which will defeat the purpose of this test, so it's important that the power is cut after the kernel has started booting, but before Mender has started.

20. Restore power, boot, and repeat step 13, again with `/dev/mmcblk0p3` (or `ub0_1`). The detected device should **not** be `/dev/mmcblk0p2` (`ubi0_0`), this indicates that the rollback has not worked. Otherwise this verifies that rollback, indeed, has worked.

That's it! You have now verified compatibility with Mender!
