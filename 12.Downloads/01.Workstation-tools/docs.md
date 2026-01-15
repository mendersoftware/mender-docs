---
title: Workstation tools
taxonomy:
    category: docs
markdown:
    extra: true
process:
    twig: true
---

# Workstation tools

## Set up the APT repository

Right now we support two package repositories: `workstation-tools` and `device-components`.

Workstation tools repo contains:
* mender-artifact
* mender-cli

!!! If you want the bleeding edge version of software, you can use our
!!! `experimental` repository by replacing `stable` with `experimental` in
!!! the above command. Do not use the `experimental` repository in production
!!! as these releases are not fully tested.

<!--AUTOVERSION: "Mender %"/ignore -->
!!! As of Mender 3.2.1 we deprecated the previous stable repository and stopped updating it. As of Mender 3.3 we removed it.

!!! With APT repo method, you will always install the latest released Mender components. If you need to install a specific version,
!!! or you want to stick to a specific minor release (e.g., to the latest LTS version), you can manually download the
!!! Debian packages from the [workstation tools repository](https://downloads.mender.io/repos/workstation-tools/pool/main).

<!-- AUTOMATION: execute=DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata -->

1. Update the `apt` package index and install required dependencies.

    ```bash
    sudo apt-get update
    sudo apt-get install --assume-yes \
    		apt-transport-https \
    		ca-certificates \
    		curl \
    		gnupg \
            jq
    ```

2. Add the official Mender GPG key to your trusted `apt` keychain:

    ```bash
    curl -fsSL https://downloads.mender.io/repos/debian/gpg | sudo tee /etc/apt/trusted.gpg.d/mender.asc
    ```

    Inspect the GPG key fingerprint and verify that it matches
    `E6C8 5734 5575 F921 8396  5662 2407 2B80 A1B2 9B00`.

    <!--AUTOMATION: ignore -->
    ```bash
    gpg --show-keys --with-fingerprint /etc/apt/trusted.gpg.d/mender.asc
    ```
    ```
    pub   rsa3072 2020-11-13 [SC] [expires: 2026-10-01]
          E6C8 5734 5575 F921 8396  5662 2407 2B80 A1B2 9B00
    uid                      Mender Team <mender@northern.tech>
    sub   rsa3072 2020-11-13 [E] [expires: 2026-10-01]
    ```

3. Add the Mender repository to your sources list by selecting the architecture
matching your device.

    First, in order to make sure that there are no mender sources in
    '/etc/apt/sources.list' lingering from a previous install, run

    <!--AUTOMATION: ignore -->
    ```bash
    sudo sed -i.bak -e "\,https://downloads.mender.io/repos/workstation-tools,d" /etc/apt/sources.list
    ```

    Then add the sources according to your Linux distribution

    !!! For Raspberry OS, use Debian distributions. To know which version is your device running,
    !!! do `(. /etc/os-release && echo $VERSION_CODENAME)`

    [ui-tabs position="top-left" active="0" theme="lite" ]
    [ui-tab title="Debian 13"]
    <!--AUTOMATION: ignore -->
    ```bash
    echo "deb [arch=$(dpkg --print-architecture)] https://downloads.mender.io/repos/workstation-tools debian/trixie/stable main" \
     | sudo tee /etc/apt/sources.list.d/mender.list
    ```
    [/ui-tab]
    [ui-tab title="Debian 12"]
    <!--AUTOMATION: ignore -->
    ```bash
    echo "deb [arch=$(dpkg --print-architecture)] https://downloads.mender.io/repos/workstation-tools debian/bookworm/stable main" \
     | sudo tee /etc/apt/sources.list.d/mender.list
    ```
    [/ui-tab]
    [ui-tab title="Ubuntu 24.04"]
    <!--AUTOMATION: ignore -->
    ```bash
    echo "deb [arch=$(dpkg --print-architecture)] https://downloads.mender.io/repos/workstation-tools ubuntu/noble/stable main" \
     | sudo tee /etc/apt/sources.list.d/mender.list
    ```
    [/ui-tab]
    [ui-tab title="Ubuntu 22.04"]
    <!--AUTOMATION: ignore -->
    ```bash
    echo "deb [arch=$(dpkg --print-architecture)] https://downloads.mender.io/repos/workstation-tools ubuntu/jammy/stable main" \
     | sudo tee /etc/apt/sources.list.d/mender.list
    ```
    [/ui-tab]
    [/ui-tabs]


## mender-artifact

The `mender-artifact` utility is used to work with Mender Artifacts,
which are files with the `.mender` suffix and contain software to be deployed.
See [Artifact creation](../../08.Artifact-creation/chapter.md) for more information on how to
use this utility.

### Install using the APT repository

`mender-artifact` is available in the APT repository.
Follow the steps in [Set up the APT repository](#set-up-the-apt-repository) chapter to enable the repository and install `mender-artifact`.

Update the package index and install the Mender Artifact:

<!--AUTOMATION: ignore -->
```bash
sudo apt-get update
sudo apt-get install mender-artifact
```
<!-- AUTOMATION: execute=apt-get update -->
<!-- AUTOMATION: execute=DEBIAN_FRONTEND=noninteractive apt-get install -y mender-client4 -->

### Mac OS X

Use `brew` to install `mender-artifact` from [the Homebrew repository](https://brew.sh/):

<!--AUTOMATION: ignore -->
```bash
brew install mender-artifact
```

! Note that using `mender-artifact` on MacOS with disk image files (e.g.: `*.sdimg`,
! `*.img`, or others holding the storage partitions) has limited functionality. Commands
! like `mender-artifact cat` or `mender-artifact cp` will not work due to lack of support
! for certain utilities on the Mac platform.


!!! `mender-artifact` binary is shipped also in [mender-ci-tools Docker image](https://hub.docker.com/r/mendersoftware/mender-ci-tools). More information [here](../../08.Artifact-creation/12.CI-CD/docs.md#mender-ci-workflows-docker-image).


## mender-cli

The `mender-cli` utility enables an easy interface to key use cases
of the Mender Server API, such as uploading a Mender Artifact, from
the command line. See [Server integration](../../10.Server-integration/chapter.md) for
more information.

### Install using the APT repository

`mender-cli` is available in the APT repository.
Follow the steps in [Set up the APT repository](#set-up-the-apt-repository) chapter to enable the repository and install `mender-cli`.

Update the package index and install the Mender CLI:

<!--AUTOMATION: ignore -->
```bash
sudo apt-get update
sudo apt-get install mender-cli
```
<!-- AUTOMATION: execute=apt-get update -->
<!-- AUTOMATION: execute=DEBIAN_FRONTEND=noninteractive apt-get install -y mender-client4 -->

### Mac OS X

Use `brew` to install `mender-cli` from [the Homebrew repository](https://brew.sh/):

<!--AUTOMATION: ignore -->
```bash
brew install mender-cli
```

!!! `mender-cli` binary is shipped also in [Docker image](https://hub.docker.com/r/mendersoftware/mender-ci-tools). More information [here](../../08.Artifact-creation/12.CI-CD/docs.md#mender-ci-workflows-docker-image).


