#!/bin/bash

set -ex

./test_autoversion.py
./autoversion.py --check
./test_docs.py 03.Client-installation/02.Install-with-Debian-package/docs.md
env TEST_OPEN_SOURCE=1 ./test_docs.py 07.Server-installation/03.Installation-with-docker-compose/docs.md
if [ -n "$REGISTRY_MENDER_IO_PASSWORD" ]; then
    docker login -u ntadm_menderci -p "$REGISTRY_MENDER_IO_PASSWORD" registry.mender.io
    env TEST_ENTERPRISE=1 ./test_docs.py 07.Server-installation/03.Installation-with-docker-compose/docs.md
    env TEST_ENTERPRISE=1 ./test_docs.py 07.Server-installation/03.Installation-with-docker-compose/02.Upgrading-from-OS-to-Enterprise/docs.md
    env TEST_ENTERPRISE=1 ./test_docs.py 08.Server-integration/03.Mutual-TLS-authentication/docs.md
    env TEST_ENTERPRISE=1 ./test_docs.py 09.Downloads/docs.md
fi
