#!/bin/bash

set -ex

./test_autoversion.py
./autoversion.py --check
./test_docs.py 03.Client-installation/02.Install-with-Debian-package/docs.md
if [ -n "$REGISTRY_MENDER_IO_PASSWORD" ]; then
    docker login -u ntadm_menderci -p "$REGISTRY_MENDER_IO_PASSWORD" registry.mender.io
    env TEST_ENTERPRISE=1 ./test_docs.py 10.Server-integration/04.Mender-Gateway/10.Mutual-TLS-authentication/docs.md
    env TEST_ENTERPRISE=1 ./test_docs.py 12.Downloads/00.Disk-images/docs.md
    env TEST_ENTERPRISE=1 ./test_docs.py 12.Downloads/01.Workstation-tools/docs.md
    env TEST_ENTERPRISE=1 ./test_docs.py 12.Downloads/02.Device-components/docs.md
fi
