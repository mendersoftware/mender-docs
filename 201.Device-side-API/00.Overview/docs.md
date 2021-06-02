---
title: Overview
taxonomy:
    category: docs
github:
    enabled: false
---

This section describes the Device-side API for the Mender clients. The Device-side API constitutes
the only public API of the Mender client. The Device-side API is a thin layer which receives messages
on the D-Bus, processes them, transmits them to the Mender client, receives the results from
the client, and transmits a response on the D-Bus.
