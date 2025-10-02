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

| Name                                                                                 | Type    |
|--------------------------------------------------------------------------------------|---------|
| [mender](https://github.com/mendersoftware/mender)                                   | CMake   |
| [mender-artifact](https://github.com/mendersoftware/mender-artifact)                 | make    |
| [mender-cli](https://github.com/mendersoftware/mender-cli)                           | make    |
| [mender-configure-module](https://github.com/mendersoftware/mender-configure-module) | make    |
| [mender-connect](https://github.com/mendersoftware/mender-connect)                   | make    |
| [mender-convert](https://github.com/mendersoftware/mender-convert)                   | scripts |
| [mender-dist-packages](https://github.com/mendersoftware/mender-dist-packages)       | scripts |
| [mender-docs](https://github.com/mendersoftware/mender-docs)                         | scripts |
| [mender-flash](https://github.com/mendersoftware/mender-flash)                       | CMake   |
| [mender-mcu](https://github.com/mendersoftware/mender-mcu)                           | custom  |
| [mender-mcu-integration](https://github.com/mendersoftware/mender-mcu-integration)   | custom  |
| [mender-qa](https://github.com/mendersoftware/mender-qa)                             | scripts |
| [mender-setup](https://github.com/mendersoftware/mender-setup)                       | make    |
| [mender-snapshot](https://github.com/mendersoftware/mender-snapshot)                 | make    |
| [mender-test-containers](https://github.com/mendersoftware/mender-test-containers)   | scripts |
| [mendertesting](https://github.com/mendersoftware/mendertesting)                     | scripts |
| [meta-mender](https://github.com/mendersoftware/meta-mender)                         | scripts |

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


