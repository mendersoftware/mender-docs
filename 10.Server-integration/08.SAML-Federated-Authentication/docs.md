---
title: SAML Federated Authentication
taxonomy:
    category: docs
---

!!!!! SAML Federated Authentication is only available in the Mender Enterprise plan.
!!!!! See [the Mender plans page](https://mender.io/pricing/plans?target=_blank)
!!!!! for an overview of all Mender plans and features.

It is possible to configure a Mender tenant to leverage a SAML-compatible Identity Provider (IdP) to identify and authenticate users. Using SAML, users can log in to Mender using existing single sign-on credentials from services compatible with SAML 2.0, like Microsoft Entra ID, AWS IAM Identity Center, Okta and Google.

Mender supports both SAML 2.0 and OpenID Connect for Single Sign-On, and you can configure one of them per tenant. This page describes the SAML setup; for OpenID Connect, see [OpenID Connect Federated Authentication](../09.OIDC-Federated-Authentication/docs.md).

The steps to register an application differ between Identity Providers. Please refer to the documentation of your IdP for details on how to add a custom SAML 2.0 application.

## Obtain the Service Provider details from Mender

Go to the "Organization" settings view, click "Set up SSO" in the "Single Sign-On" section and select SAML as the type (the other option, OpenID Connect, is described in [OpenID Connect Federated Authentication](../09.OIDC-Federated-Authentication/docs.md)).
Mender displays the following details of your tenant as a SAML 2.0 Service Provider (SP):

* Entity ID, a globally unique name for a SAML Service Provider (Mender, in our case);
* ACS URL, the Assertion Consumer Service URL your IdP will send its SAML Response to after authenticating a user;
* Start URL (or Login URL), which will initiate the SAML authentication for your user.

The values have the following format, where `<sso-id>` is an identifier unique to your tenant and `hosted.mender.io` is replaced by the address of your Mender server if you don't use hosted Mender:

| Field     | Value                                                                           |
|-----------|---------------------------------------------------------------------------------|
| Entity ID | `https://hosted.mender.io/api/management/v1/useradm/sso/sp/metadata/<sso-id>`   |
| ACS URL   | `https://hosted.mender.io/api/management/v1/useradm/auth/sso/<sso-id>/acs`      |
| Start URL | `https://hosted.mender.io/api/management/v1/useradm/auth/sso/<sso-id>/login`    |

Always copy the values from the UI rather than composing them yourself.
These values are specific to your tenant and don't change when you upload or replace the IdP metadata.
You can also retrieve them using the [Management API](https://docs.mender.io/api/#management-api-user-administration-and-authentication-lists-all-sso-connection-endpoints).

## Add Mender to the Identity Provider

Create a new custom SAML 2.0 application in your Identity Provider and configure it with the details obtained from Mender:

* ACS URL (often called "Single sign-on URL", "Reply URL" or "Application ACS URL");
* Entity ID (often called "Audience URI", "Identifier" or "Application SAML audience");
* Start URL (optional, often called "Sign on URL" or "Application start URL").

As Mender uses the user's email address as a username, please make sure your IdP uses the email address as NameID format and that the Name ID value is the user's primary email address.

Once you have created the application, download its SAML metadata XML from your IdP.
You can verify the NameID format by checking that the metadata contains the following line:

```xml
<md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</md:NameIDFormat>
```

Finally, enable the application for the users who should have access to Mender.

## Upload the Identity Provider metadata to Mender

Back in the "Organization" settings view, click "Upload or edit metadata", upload the metadata XML file from your IdP or paste its content into the editor, and save.

Once you save the metadata, the "Single Sign-On" section is marked as "Enabled" and shows the SSO type, the Service Provider details and the metadata status. The SAML Federation is now complete, and you can start using it to authenticate your users to Mender.
If your IdP metadata changes, for example after rotating the signing certificate, upload the new metadata the same way.

## Authorizing users and federated log in

Only authorized users from your IdP can log in to Mender. 
For SAML integration you must authorize users by creating them in the "User management" settings view, leaving the password field blank and assigning the Role-Based Access Control roles as required.
The email address of the user in Mender must match the email address of the user in your IdP.

At this point, users can log in to Mender by opening the Start URL in their browsers and logging in using their credentials from the organization's Identity Provider. The user will be automatically linked to the SAML IdP on the first login.


## Limitations

Please note that IdP initiated SSO isn't supported.

JWT tokens issued to SSO users authenticating to Mender through the SAML 2.0 federated login are valid for 24 hours only. The reason for this limitation is that Mender cannot check whether the user is still active and authorized when verifying the token on subsequent API calls. Therefore, after 24 hours, the user will have to authenticate again to renew the JWT token. However, if the session in the Identity Provider is still valid, this won't trigger a new password or token request, and the IdP will seamlessly redirect the user back to the Mender UI.
