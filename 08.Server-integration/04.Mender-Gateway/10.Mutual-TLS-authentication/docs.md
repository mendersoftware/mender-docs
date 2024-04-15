---
title: Mutual TLS authentication
taxonomy:
    category: docs
---

!!!!! The Mender Gateway and Mutual TLS (mTLS) authentication, is only available in the Mender Enterprise plan.
!!!!! To access the *Mender Gateway* container, please [contact support](https://support.northern.tech/hc/en-us).
!!!!! In the message, please mention that you are requesting *"Access to the Mender Gateway"*.

! Mutual TLS was previously supported by the `mtls-ambassador` server component - which has been replaced by `mender-gateway`.
! Please see the [migration guide](99.MTLS-ambassador-migration/docs.md) for steps on how to migrate from `mtls-ambassador` to `mender-gateway`.

Mender supports setting up a reverse proxy at the edge of the network, which can authenticate devices using TLS client certificates.
Each client presents a certificate signed by a Certificate Auhtority (CA) and the edge proxy authenticates devices by verifying this signature.
Authenticated devices are automatically authorized in the Mender backend and do not need manual approval or preauthorization.

This is particularly useful in a mass production setting because you can sign client certificates during the manufacturing process, so they automatically get accepted into the Mender Server when your customer turns them on (which might happen several months after manufacturing).

See [Device Authentication](../../../02.Overview/13.Device-authentication/docs.md) for a general overview of how device authentication works in Mender.


If you are unfamiliar with the mTLS flow, please take a look at the [flow diagram](../../../02.Overview/13.Device-authentication/docs.md#client-certificate-authentication-and-mutual-tls) and also read about the [keys involved](01.Keys-and-certificates/docs.md).

After it is suggested that you complete the [evaluation with docker-compose](02.Evaluation-with-docker-compose/docs.md). It will lead you to a working example with a simple server setup and a client.

Once you have made the choices regarding [Public Key Infrastructure](https://en.wikipedia.org/wiki/Public_key_infrastructure) (PKI) and have the client ready, check the [production installation with Kubernetes](03.Production-installation-with-kubernetes/docs.md) which focuses only on how to set up the mTLS proxy server for production.
