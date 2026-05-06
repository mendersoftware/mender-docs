---
title: Operating mTLS securely
taxonomy:
    category: docs
---

This chapter covers a hardening pattern that shortens recovery from a Root CA compromise, and the incident-response procedure for when a private key in the PKI has actually been compromised. For scheduled, zero-downtime turnover see [Certificate rotation](../04.Certificate-rotation/docs.md). That procedure does not solve a compromise.

## Pre-staging a backup mTLS PKI

Recovery from a compromised Root CA is operationally expensive: every device in the field needs new crypto material, generated and delivered after the incident. You can shorten that recovery dramatically by pre-staging a backup PKI at manufacturing time and keeping its Root CA private key offline.

The pattern:

1. Generate two independent Root CAs at provisioning time, a *primary* and a *backup*. Each has its own intermediate.
2. Provision both chains and both private keys on every device: `device-chain-primary.pem` and `device-primary.key` are the active pair, `device-chain-backup.pem` and `device-backup.key` sit on the data partition unused.
3. Keep the backup Root CA's private key offline and isolated from the primary, in stronger storage and under separate access controls. Treat it as break-glass material.
4. Configure the gateway to trust only the primary Root CA via `MTLS_CA_CERTIFICATE`.

In the event of a primary Root CA compromise, recovery becomes a configuration switch instead of a re-provisioning project: see [If you pre-staged a backup PKI](#if-you-pre-staged-a-backup-pki) below.

Operational notes:

- The two Root CAs must come from genuinely independent ceremonies. If both are generated on the same host, a host compromise takes both.
- After switching from primary to backup, you have used your second life. Generate and roll out a new backup chain so the fleet is two-deep again.

## Compromised intermediate CA

The first question to answer is: does the attacker have the intermediate's private key, or only specific issued device certificates?

If the attacker holds the private key, blacklisting does not contain the threat. They can issue new device certs with serial numbers you have never seen, which will never be in your blacklist. Treat this as a compromised Root CA; see below.

If only specific device certs are compromised, blacklist those serials with `MTLS_BLACKLIST_PATH` (see [Configuration file](../../99.Configuration-file/docs.md)). The file is a newline-separated list of hex serial numbers. This works only if you have kept a record of issued serials so you know which to add.

## Compromised Root CA

The Root CA is the trust anchor, so once it is suspect the only remedy is to switch the fleet to a new Root CA. There is no zero-downtime path.

Decide first: is the attacker holding the Root CA's private key, or do you suspect compromise of trust on other grounds (mis-issuance you cannot reproduce, suspicious activity in the signing infrastructure, lost confidence in the offline storage)? The two cases want different trade-offs.

### Attacker holds the private key

Take the old gateway offline as soon as you detect the compromise. While it is up, anything signed by the old root is trusted, including a server certificate the attacker can issue for the gateway's own hostname; a device that still trusts the old root will accept the impersonation without warning. Devices in the field cannot connect until they receive the new crypto material. That is the cost of containment, and it is the correct trade-off in a real compromise.

The [migration via parallel gateway](#migration-via-parallel-gateway) below is not directly applicable in this scenario: it assumes the rollout flows through a still-running gateway, which contradicts containment. Use the [pre-staged backup PKI](#if-you-pre-staged-a-backup-pki) recovery if you have one; otherwise use the [bypass strategy](#bypass-via-direct-mender-server-connection).

### Pre-emptive rotation without key exposure

If you do not believe the private key has been exfiltrated (for example, you are rotating because of unrelated suspicious activity), you can run two gateways side by side and stage the cutover. Devices keep authenticating against the old gateway until they receive the new crypto material.

### If you pre-staged a backup PKI

If you followed the [pre-staging hardening pattern](#pre-staging-a-backup-mtls-pki), recovery is mostly a configuration switch. Devices already have the backup chain on disk, so the deployment only needs to tell them which file to use.

1. **Update `MTLS_CA_CERTIFICATE` on the gateway** to trust both the primary and the backup Root CA (concatenate the two root certificates in the file). For pre-emptive rotation this is fine; for a real compromise the operator must accept a window where the gateway still trusts the compromised root. If that window is unacceptable, see the hard-cutover note below.
2. **Push a Mender Deployment** (typically an [`apply-device-config`](../../../../11.Add-ons/10.Configure/01.Device-integration/docs.md) script) that updates `mender.conf` on each device to use `device-chain-backup.pem` and `device-backup.key` for the active client chain.
3. **Remove the primary Root CA** from `MTLS_CA_CERTIFICATE` on the gateway, once all devices have switched.
4. **Generate a new backup PKI** (Root CA + intermediate + per-device chains) and roll it out via a normal Mender Deployment so the fleet is two-deep again.

The per-device generation of new client material is skipped: the bottleneck is the deployment rollout itself.

For a hard cutover, take the gateway offline immediately and deliver step 2 via the [bypass strategy](#bypass-via-direct-mender-server-connection). The pre-staged backup still saves the per-device generation step.

### Migration via parallel gateway

This procedure assumes the old gateway stays reachable while the rollout proceeds, so it fits pre-emptive rotation. For a real key-exposure compromise, use the [pre-staged backup](#if-you-pre-staged-a-backup-pki) or [bypass](#bypass-via-direct-mender-server-connection) recovery paths instead.

1. **Stand up the new gateway** on a separate hostname or IP, with `MTLS_CA_CERTIFICATE` pointing at the new Root CA and a fresh `HTTPS_SERVER_CERTIFICATE` chain. Verify the listener with the procedure in [Verifying the chains](../04.Certificate-rotation/docs.md#verifying-the-chains).

2. **Generate new client crypto material** for each device, signed by the new Root CA: device cert, intermediate cert, device key. Bundle the chain as `device-chain.pem`.

3. **Build a Mender Artifact** (or an `apply-device-config` script using the [Configure add-on](../../../../11.Add-ons/10.Configure/01.Device-integration/docs.md)) that on each device:
   - installs the new `device-chain.pem` and `device.key`,
   - updates `mender.conf` to set `Servers` to the new gateway URL,
   - sets `ServerCertificate` to the new gateway's CA chain. Do **not** include the old root in this file if the private key is suspected exfiltrated; keeping it would let the attacker impersonate the gateway. If the rotation is pre-emptive and the old key is not exposed, you can concatenate old + new so devices verify both gateways during the rollout.

   See [client configuration options](../../../../03.Client-installation/07.Configuration/50.Configuration-options/docs.md#servers) for the relevant fields.

4. **Test on a canary device first.** Confirm the canary appears on the new gateway and that the deployment reports success before rolling out further. A bad `mender.conf` (invalid JSON) stops `mender-updated` from starting and the device only rolls back on the next reboot.

5. **Roll out to the fleet in waves.** Watch the new gateway logs and authentication counts as devices switch over.

6. **Decommission the old gateway** once the new gateway shows all expected devices and the old one is idle.

### Bypass via direct Mender Server connection

Where the Mender Server is reachable from the devices' network, you can avoid the parallel-gateway approach entirely:

1. Push a Mender Artifact that updates `mender.conf` to set `ServerURL` to the Mender Server directly and removes the mTLS settings. The device falls back to the standard Mender authentication flow, using its auto-generated `mender-agent.pem` keypair, which is independent of the gateway PKI.
2. Take the compromised gateway offline.
3. Stand up a new Mender Gateway with a new Root CA at your own pace.
4. Push a second deployment to re-introduce the new gateway URL and new client crypto material. That step is now a normal scheduled rotation, not incident response.

The deployment in step 1 still passes through the compromised gateway, so the attacker can read its contents (TLS confidentiality is lost) and can block it from reaching devices (denial of service). They cannot tamper with the payload: Mender Artifacts are signed with a key separate from the gateway PKI (see `ArtifactVerifyKeys` in the [client configuration options](../../../../03.Client-installation/07.Configuration/50.Configuration-options/docs.md)). Watch deployment success rates closely.

For a real key-exposure compromise where containment is the priority, the operator can swap steps 1 and 2: take the gateway offline first to stop the exposure, then deliver step 1 to whatever devices are still online. Devices that were offline at that moment will need manual re-provisioning when they reappear.

This strategy is not available if the Mender Server is behind the gateway on a private network and the devices cannot reach it directly. It also requires that you can approve devices on the Mender Server when they appear there for the first time without gateway pre-auth: set auto-accept policies first if your fleet is large.

### Cleaning up the compromised key

The compromised material is the CA private key, not the per-device keys. Identify and destroy every copy.

### Things that go wrong

Devices that are offline during the rollout stay on the old gateway until they come back. If the rotation is pre-emptive you can wait for them. For a real compromise where the old gateway must come down immediately, offline devices will require manual re-provisioning when they reappear.
