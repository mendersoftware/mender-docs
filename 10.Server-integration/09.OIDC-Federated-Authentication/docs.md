---
title: OpenID Connect Federated Authentication
taxonomy:
    category: docs
---

!!!!! OpenID Connect Federated Authentication is only available in the Mender Enterprise plan.
!!!!! See [the Mender plans page](https://mender.io/pricing/plans?target=_blank)
!!!!! for an overview of all Mender plans and features.

OpenID Connect (OIDC) uses a very similar flow to [SAML](../08.SAML-Federated-Authentication). As with SAML, you can configure Mender to initiate the authorization process with the OpenID Connect provider by exposing a login endpoint that redirects users to the authorization server, which in turn calls an authentication callback.

! Please note that as of today, Mender only supports the [Implicit Flow](https://openid.net/specs/openid-connect-implicit-1_0.html).

## Configure OpenID Connect:

Please note that there are many names for actors in all the federated authentication mechanisms. Mender mostly follows SAML nomenclature.

### Pre-requisites

Before you're ready to configure OpenID Connect (OIDC) in Mender you first need to register Mender as an application in your Identity Provider (IdP). The steps to achieve this depends on your IdP and we encourage you to refer to the documentation of your specific IdP for details on this process.

__A working OIDC flow with Mender requires the following__:
* The `Client ID` and `Client Secret` of your OIDC Application if your IdP requires it (this is typically the case).
* The OIDC Application must be allowed to issue `ID Tokens`. This is sometimes disabled by default, but is required by the Mender OIDC implementation.
* `ID Tokens` issued by the Application must include the optional claim `email`. Mender uses this claim to lookup users by their email and any tokens that do not include the `email` claim will be rejected.
* Redirect URI(s) configured in the OIDC Application to allow redirects back to Mender after a successful login. The URIs that must be configured are made available [after Mender provider creation](#redirect-uris) below.


### Create a provider

The first step is to create a Mender _provider_ that stores all the settings needed to initiate and complete the OIDC flow. You can create an OIDC provider in Mender through the UI by accessing the [Organization and billing](https://hosted.mender.io/ui/settings/organization-and-billing) view, enabling Single Sign-On, choosing OpenID Connect and provide the necessary settings as described below. Alternatively you can create an OIDC provider in Mender via API call to the [/sso/idp/metadata](https://docs.mender.io/api/#management-api-user-administration-and-authentication-post-saml--openid-connect-metadata--or-url-point-to-them)
endpoint.

__The well-known endpoint__  
There are several parameters needed for OIDC to work which are made available by your IdP at the so-called `well-known` endpoint. You can have Mender fetch them for you or you can enter them manually. The `well-known` endpoint is IdP dependant, but it often comes in the form `https:///your.openidconnect.provider.com/<your.idp.tenant.id>/.well-known/openid-configuration` ("your.openidconnect.provider.com" is the hostname of your IdP). Please refer to the documentation provided by your IdP for further details.

If you prefer that Mender fetches the required information from the `well-known` endpoint you can simply specify the `well_known_url` property when creating the Mender provider:

```json
{
  "name":"identity-provider-name",
  "client_id":"Ylb6gfnmXckxHFoXH1aKLX2poDCvS9MV",
  "client_secret":"zygGHMTL9VlCQpOIHNbXpTZqd77LqqIP",
  "well_known_url":"https:///your.openidconnect.provider.com/<your.tenant.id>/.well-known/openid-configuration"
}
```

In the above, the name is mandatory, while both `client_id` and `client_secret` are optional. Be advised though that most OpenID Connect providers require the `client_id` and `client_secret` for login work as expected.

! Mender fetches the information it needs from the `well-known` endpoint upon provider creation only. Any changes to the `well-known` endpoint after the provider has been created will not be reflected in Mender.

If you prefer to provider the information Mender requires manually you can leave out the `well_known_url` property and provide the full set of information in the `settings` property instead:

```json
{
  "name": "your-provider-name",
  "client_id":"Ylb6gfnmXckxHFoXH1aKLX2poDCvS9MV",
  "client_secret":"zygGHMTL9VlCQpOIHNbXpTZqd77LqqIP",
  "settings": {
    "issuer": "https://your.openidconnect.provider.com/",
    "authorization_endpoint": "https://your.openidconnect.provider.com/authorize",
    "token_endpoint": "https://your.openidconnect.provider.com/oauth/token2",
    "device_authorization_endpoint": "https://your.openidconnect.provider.com/oauth/device/code",
    "userinfo_endpoint": "https://your.openidconnect.provider.com/userinfo",
    "mfa_challenge_endpoint": "https://your.openidconnect.provider.com/mfa/challenge",
    "jwks_uri": "https://your.openidconnect.provider.com/.well-known/jwks.json",
    "registration_endpoint": "https://your.openidconnect.provider.com/oidc/register",
    "revocation_endpoint": "https://your.openidconnect.provider.com/oauth/revoke",
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
    "end_session_endpoint": "https://your.openidconnect.provider.com/oidc/logout"
  }
}
```

! The `id_token_signing_alg_values_supported` and `token_endpoint_auth_signing_alg_values_supported` fields both specify allowed algorithms for signing tokens. Mender only supports the algorithms below, so make sure your IdP supports at least one of them.
! ```json
! "ES256", "ES256K", "ES384", "ES512", "PS256", "PS384", "PS512", "RS384", "RS512"
! ```


After successfully creating the Mender OIDC provider, the UI will present you with a start URL that looks like this: `https://hosted.mender.io/api/management/v1/useradm/oidc/<your provider id>/start`. This is the URL your users must use to initiate the OpenID Connect login process.

### Redirect URIs

Once you have the Mender OpenID Connect provider created you need to do the final step of the configuration. The Application you created in the [pre-requisites section](#pre-requisites) needs to be configured to allow redirects back to Mender.

The Redirect URI you need to configure in your IdP Application is identical to the start URL above, except that it ends with `/login` instead of `/start`:
```bash
# If your login URL is
https://hosted.mender.io/api/management/v1/useradm/oidc/a82a2e98-833e-4a5a-9856-1e838702a35d/start
# you need to add
https://hosted.mender.io/api/management/v1/useradm/oidc/a82a2e98-833e-4a5a-9856-1e838702a35d/login
# to the Redirect URIs of your IdPs OpenID Connect Application
```

This is the URL your IdP will redirect users back to after successful authentication and unless you allow this explicitly, the login will be denied by your IdP.

! The `/login` URL above is Mender Tenant specific and must therefore be configured on a per Tenant basis in your OIDC Application. Most IdPs supports multiple Redirect URIs for one OIDC Application and Application re-use for multiple tenants should be possible in most cases if desired.

### User creation

Before users can use OpenID Connect to login to Mender, you must first create the users and assign appropriate roles. You can do this [through the UI](../../02.Overview/12.Role-based-access-control/docs.md) or via API request to the [/v1/useradm/users](https://docs.mender.io/api/#management-api-user-administration-and-authentication-create-user) endpoint.

It's important that you ensure that the `email` of the users are the same as their `email` in your IdP and that the user has **no password configured** in Mender. This is because Mender matches the `email` from the id_token issued by your IdP with the `email` of Mender users in the Tenant to determine which user to authenticate.