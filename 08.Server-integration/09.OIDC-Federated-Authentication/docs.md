---
title: OpenID Connect Federated Authentication
taxonomy:
    category: docs
---

!!!!! OpenID Connect Federated Authentication is only available in the Mender Enterprise plan.
!!!!! See [the Mender plans page](https://mender.io/pricing/plans?target=_blank)
!!!!! for an overview of all Mender plans and features.

OpenID Connect (OIDC) uses a very similar flow to [SAML](../08.SAML-Federated-Authentication).
And as with SAML, you can configure Mender to initiate the authorization process
with the OpenID Connect provider by exposing a login endpoint that redirects
user to the authorization server, which in turn calls an authentication callback.

Please note that as of today, Mender only implements
the [Implicit Flow](https://openid.net/specs/openid-connect-implicit-1_0.html).

## Configure OpenID Connect: create a provider

The first step is to create a _provider_. Please note that there are many names for actors
in all the federated authentication mechanisms. Mender mostly follows SAML nomenclature.
The provider we are going to create is an entity that stores all the settings needed
to initiate and complete the OIDC flow.

### The well-known endpoint

There are several parameters needed for OIDC to operate. You can get all of them from the so-called
_well-known_ endpoint, and use those to create a provider, or pass the well-known URL in the creation
process. In the latter case, you need to use the following document (either
in the [organization-and-billing](https://hosted.mender.io/ui/settings/organization-and-billing)
or in the POST API call to [https://hosted.mender.io/api/management/v1/useradm/sso/idp/metadata](https://docs.mender.io/api/#management-api-user-administration-and-authentication-post-saml--openid-connect-metadata--or-url-point-to-them)
endpoint)

### Upload the metadata and get the login URL

To create an OIDC provider in Mender, you can use the UI accessing
the [Organization and billing](https://hosted.mender.io/ui/settings/organization-and-billing) view.
Enabling the Single Sign-On and choosing the type will allow you to type or upload the metadata
you need to configure OpenID Connect to authenticate users.

Mender can use the well-known URL, and in that case, it is enough to provide the following
document:

```json
{
  "name":"identity-provider-name",
  "client_id":"Ylb6gfnmXckxHFoXH1aKLX2poDCvS9MV",
  "client_secret":"zygGHMTL9VlCQpOIHNbXpTZqd77LqqIP",
  "well_known_url":"https://your.openidconnect.provider.oidc/.well-known/openid-configuration"
}
```

In the above, the name is mandatory, while both `client_id` and `client_secret` are optional but may be required
by your OpenID Connect provider. The `well_known_url` denotes the URL for the well-known endpoint, which contains
the hostname of your OIDC provider (called "your.openidconnect.provider.oidc" throughout this section).

You can also leave out the `well_known_url` field and provide all the settings by yourself:

```json
{
  "name": "your-provider-name",
  "client_id":"Ylb6gfnmXckxHFoXH1aKLX2poDCvS9MV",
  "client_secret":"zygGHMTL9VlCQpOIHNbXpTZqd77LqqIP",
  "settings": {
    "issuer": "https://your.openidconnect.provider.oidc/",
    "authorization_endpoint": "https://your.openidconnect.provider.oidc/authorize",
    "token_endpoint": "https://your.openidconnect.provider.oidc/oauth/token2",
    "device_authorization_endpoint": "https://your.openidconnect.provider.oidc/oauth/device/code",
    "userinfo_endpoint": "https://your.openidconnect.provider.oidc/userinfo",
    "mfa_challenge_endpoint": "https://your.openidconnect.provider.oidc/mfa/challenge",
    "jwks_uri": "https://your.openidconnect.provider.oidc/.well-known/jwks.json",
    "registration_endpoint": "https://your.openidconnect.provider.oidc/oidc/register",
    "revocation_endpoint": "https://your.openidconnect.provider.oidc/oauth/revoke",
    "scopes_supported": [
      "openid",
      "profile",
      "offline_access",
      "name",
      "given_name",
      "family_name",
      "nickname",
      "email",
      "email_verified",
      "picture",
      "created_at",
      "identities",
      "phone",
      "address"
    ],
    "response_types_supported": [
      "code",
      "token",
      "id_token",
      "code token",
      "code id_token",
      "token id_token",
      "code token id_token"
    ],
    "code_challenge_methods_supported": [
      "S256",
      "plain"
    ],
    "response_modes_supported": [
      "query",
      "fragment",
      "form_post"
    ],
    "subject_types_supported": [
      "public"
    ],
    "id_token_signing_alg_values_supported": [
      "RS256"
    ],
    "token_endpoint_auth_methods_supported": [
      "client_secret_basic",
      "client_secret_post",
      "private_key_jwt"
    ],
    "claims_supported": [
      "aud",
      "auth_time",
      "created_at",
      "email",
      "email_verified",
      "exp",
      "family_name",
      "given_name",
      "iat",
      "identities",
      "iss",
      "name",
      "nickname",
      "phone_number",
      "picture",
      "sub"
    ],
    "request_uri_parameter_supported": false,
    "request_parameter_supported": false,
    "token_endpoint_auth_signing_alg_values_supported": [
      "RS256"
    ],
    "end_session_endpoint": "https://your.openidconnect.provider.oidc/oidc/logout"
  }
}
```

In the first case, Mender will query and validate the required settings.
Once you see the success of parsing and saving the metadata the UI will
present you with a start or login URL: this is the address you use
to initiate the login process, which completes the setup.

## Supported algorithms

For both `id_token_signing_alg_values_supported` and
`token_endpoint_auth_signing_alg_values_supported` fields denoting
the allowed algorithms for signing, we support the following values:

```json
"ES256",
"ES256K",
"ES384",
"ES512",
"PS256",
"PS384",
"PS512",
"RS384",
"RS512"
```
