---
title: Production installation with Kubernetes
taxonomy:
    category: docs
    label: tutorial
---

!!! You can save time by using [hosted Mender](https://hosted.mender.io?target=_blank), a secure Mender Server ready to use, maintained by the Mender developers.


This section is a step by step tutorial for deploying the Mender Server for production environments, and will cover relevant security and reliability aspects of Mender production installations. Most of the steps are the same whether you are installing the Open Source or Enterprise edition of the Mender Server, but some extra are are highlighted for the latter.

You will use the [Helm chart](https://github.com/mendersoftware/mender-helm) to
deploy to production the Mender backend services on a Kubernetes cluster.

Please read the [Requirements and support](01.Requirements-and-support/docs.md) page to understand what software versions and cloud architectures are validated by Northern.tech.
Once that is clear please move on the first paragraph [Kubernetes](./01.Kubernetes).


