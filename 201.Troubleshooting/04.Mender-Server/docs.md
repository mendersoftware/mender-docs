---
title: Mender Server
taxonomy:
    category: docs
---

##The virtual QEMU device is not showing up in test mode

When running the Mender server in test mode, as described in the Getting started
guide, a virtual `vexpress-qemu` device should connect to and ask to join the server.

If this does not happen, please make sure your environment meet the resource requirements
to run the Mender Server. In particular, it is known that the virtual device will not
start if you do not have enough memory.
