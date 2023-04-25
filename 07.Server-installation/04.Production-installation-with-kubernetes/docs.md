---
title: Production installation with Kubernetes
taxonomy:
    category: docs
    label: tutorial
---

!!! You can save time by using [hosted Mender](https://hosted.mender.io?target=_blank), a secure Mender Server ready to use, maintained by the Mender developers.

This is a step by step tutorial for deploying the Mender Server for production
environments, and will cover relevant security and reliability aspects of Mender
production installations.  Most of the steps are the same whether you are installing
the Open Source or Enterprise edition of the Mender Server, but some extra are
are highlighted for the latter.


For a production installation the components are:
* Mender Server distributed via a [Helm chart](https://github.com/mendersoftware/mender-helm) to
* independently deployed dependencies of Mender Server
   * these are external services like the database, message broker and similar
   * the exact dependencies with the versions are mentioned in the subchapters

When installing the production server, please follow the order of subchapters.
This will ensure you have all the dependencies correctly met.

