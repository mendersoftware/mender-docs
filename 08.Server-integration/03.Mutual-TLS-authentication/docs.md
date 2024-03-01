---
title: Mutual TLS authentication
taxonomy:
    category: docs
---

!!!!! Mutual TLS authentication, or mTLS, is only available in the Mender Enterprise plan.
!!!!! To access the mTLS proxy container, please [contact support](https://support.northern.tech/hc/en-us).
!!!!! In the message, please mention that you are requesting *"Access to the mTLS proxy"*.

Mender supports setting up a reverse proxy at the edge of the network, which can authenticate devices using TLS client certificates. 
Each client presents a certificate signed by a CA certificate and the edge proxy authenticates devices by verifying this signature. 
Authenticated devices are automatically authorized in the Mender backend and do not need manual approval or preauthorization.

This is particularly useful in a mass production setting because you can sign client certificates during the manufacturing process, so they automatically get accepted into the Mender Server when your customer turns them on (which might happen several months after manufacturing).

See [Device Authentication](../../02.Overview/13.Device-authentication/docs.md) for a general overview of how device authentication works in Mender.


If you are unfamiliar with the mTLS flow, please take a look at the [flow diagram](../../02.Overview/13.Device-authentication/docs.md#client-certificates-and-mutual-tls) and also read about the [keys involved](../03.Mutual-TLS-authentication/01.Keys-and-certificates/docs.md).

After it is suggested that you complete the [evaluation with docker-compose](../03.Mutual-TLS-authentication/02.Evaluation-with-docker-compose/docs.md). It will lead you to a working example with a simple server setup and a client.

Once you have made the choices regarding [Public Key Infrastructure](https://en.wikipedia.org/wiki/Public_key_infrastructure) (PKI) and have the client ready, check the [production installation with Kubernetes](../03.Mutual-TLS-authentication/03.Production-installation-with-kubernetes/docs.md) which focuses only on how to set up the mTLS proxy server for production. 
