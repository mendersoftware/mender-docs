---
title: Build from source code
taxonomy:
    category: docs
---

Mender project consist of multiple repositiories with various types of the source code.
Most of the repositories support `make` and `Makefile` based building / testing /deploying.
The 2nd most popular build chain used in the project is `CMake`.

Every repository contains a README page with how to run and build instructions.
It is strongly advised to follow build instructions which can be found
in the project repositories as they may vary from the general building instructions
and can contain project specific settings.

## Project repositiories list

| Name                    | Type     | Link                                                      |
|-------------------------|----------|-----------------------------------------------------------|
| mender                  | CMake    | https://github.com/mendersoftware/mender                  |
| mender-artifact         | make     | https://github.com/mendersoftware/mender-artifact         |
| mender-cli              | make     | https://github.com/mendersoftware/mender-cli              |
| mender-configure-module | make     | https://github.com/mendersoftware/mender-configure-module |
| mender-connect          | make     | https://github.com/mendersoftware/mender-connect          |
| mender-convert          | scripts  | https://github.com/mendersoftware/mender-convert          |
| mender-dist-packages    | scripts  | https://github.com/mendersoftware/mender-dist-packages    |
| mender-docs             | scripts  | https://github.com/mendersoftware/mender-docs             |
| mender-flash            | CMake    | https://github.com/mendersoftware/mender-flash            |
| mender-mcu              | custom   | https://github.com/mendersoftware/mender-mcu              |
| mender-mcu-integration  | custom   | https://github.com/mendersoftware/mender-mcu-integration  |
| mender-qa               | scripts  | https://github.com/mendersoftware/mender-qa               |
| mender-setup            | make     | https://github.com/mendersoftware/mender-setup            |
| mender-snapshot         | make     | https://github.com/mendersoftware/mender-snapshot         |
| mender-test-containers  | scripts  | https://github.com/mendersoftware/mender-test-containers  |
| mendertesting           | scripts  | https://github.com/mendersoftware/mendertesting           |
| meta-mender             | scripts  | https://github.com/mendersoftware/meta-mender             |

## make based project general rules

**Warning: Always follow repository README instructions first**

For the `make` based project build and deploiment uses some common target:
* `make` / `make build` - build the project
* `make test` - run tests (may contain both: unit tests and integration tests)
* `make install` - deploy the software on the host machine
* `make uninstall` - remove the software from the host machine

The easiest way to understand supported targets better is to check
`Makefile` located in the project directory.

## CMake based projects general rules

**Warning: Always follow repository README instructions first**

For building `CMake` based project:
* `cmake -D CMAKE_INSTALL_PREFIX:PATH=/usr -B build .` - prepare build directory
* `cmake --build build` - perform a build

In the case of a `CMake` build some project specific flags may be used (like the one above)
to change the resulting makefile behavior (eg. force specific install directory).


