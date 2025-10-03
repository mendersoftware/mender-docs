---
title: Using the APIs
taxonomy:
    category: docs
    label: tutorial
---

The Mender Server microservices are all accessible using an HTTPS API. These APIs can be used to configure the server (for example, preauthorizing devices) or implementing custom workflows (for example, integrating the Mender Server into an existing device management system.) The APIs are documented in [API chapter](../../200.Server-side-API).

There are many ways to interact with Mender's REST APIs and the most common ones are shown below.

## Install cURL and jq and set up the shell variables

There are many ways to call HTTP-based REST APIs, but the command line utility `curl` is the most generally available method.

The `jq` utility is commonly used to decode JSON messages and display them in a human-readable format. REST API responses contain raw JSON data and must run through a JSON parser (`jq`).

On a Debian-derived system, you can easily install both running:

```bash
sudo apt-get install curl jq
```

Open a terminal, which we will use in the following to call the Mender Server's REST APIs. First set a shell variable with the URI of your server:
```bash
MENDER_SERVER_URI='https://hosted.mender.io'
```

!!! Hosted Mender is available in multiple [regions](/13.General/00.Hosted-Mender-regions/docs.md) to connect to. Make sure you select your desired one before proceeding.

!!! Adjust the variable value to the Mender Server you are using.

Next, set a variable with your user email on the Mender Server (replace its content with your user email):

```bash
MENDER_SERVER_USER='myusername@example.com'
```

Now obtain a management API JSON Web Token by using the [login API](../../200.Server-side-API/?target=_blank#management-api-user-administration-and-authentication-login):

```bash
JWT=$(curl -X POST -u $MENDER_SERVER_USER $MENDER_SERVER_URI/api/management/v1/useradm/auth/login)
```

!!! If you are using self-signed certificates in a demo setup you may want to skip validation with the `-k` option of `curl` (this is insecure).

You should now have an API token you can use to call any of the [Mender Server management APIs](../../200.Server-side-API/?target=_blank#management-apis) in the `JWT` shell variable.

!!! The `MENDER_SERVER_URI` and `JWT` shell variables will only exist in the current shell invocation by default, so make sure you use this same shell environment for any interactions with the API.


### Verify you can call the APIs

To verify you can call the server APIs, you can get your user's details:

```bash
curl -H "Authorization: Bearer $JWT" $MENDER_SERVER_URI/api/management/v1/useradm/users/me | jq '.'
```

If it succeeds, it will return:

> ```
> {
>   "id": "0a6c526c-4637-4a62-bf38-81aa70c4aa59",
>   "email": "mender-demo@example.com",
>   "created_ts": "2022-06-08T03:58:28.582Z",
>   "updated_ts": "2022-06-08T03:58:28.582Z",
>   "login_ts": "2022-06-08T04:02:06.855Z"
> }
> ```

If this fails, e.g. returns `401 Authorization Required`, make sure that the contents of your `JWT` and `MENDER_SERVER_URI` shell variables are correct and re-run the steps above if necessary.


### Personal Access Tokens

Personal Access Tokens are **long-lived** JWT tokens that you can use to programmatically access the Mender management APIs without logging in each time you need to perform API calls nor handle the JWT token expiration every week. Personal Access Tokens act as API keys you can use from your *CI/CD pipelines* or scheduled jobs to access the Mender management APIs.

You can generate a Personal Access Token using the web-based UI from the "My profile" page or the following API call:

```bash
PERSONAL_ACCESS_TOKEN=$(curl -H "Authorization: Bearer $JWT" -H "Content-Type: application/json" -X POST $MENDER_SERVER_URI/api/management/v1/useradm/settings/tokens -d '{"name": "my_token", "expires_in": 31536000}')
```

Personal Access Tokens have a unique name and an expiration time in seconds, up to one year (31536000 seconds). Once generated, the server won't return the content of the access token anymore. Therefore, it is your responsibility to store its value securely.

You can list your Personal Access Tokens as follows:

```bash
curl -H "Authorization: Bearer $JWT" -k $MENDER_SERVER_URI/api/management/v1/useradm/settings/tokens | jq '.'
```
> ```
> [
>   {
>     "id": "767c2a29-a983-45ce-b58f-c4379d1b8ee8",
>     "name": "my_token",
>     "expiration_date": "2023-06-08T04:02:36.298Z",
>     "created_ts": "2022-06-08T04:02:36.298Z"
>   }
> ]
> ```

You can now use your Personal Access Token to perform API calls:

```bash
curl -H "Authorization: Bearer $PERSONAL_ACCESS_TOKEN" $MENDER_SERVER_URI/api/management/v1/useradm/users/me | jq '.'
```

If it succeeds, it will return:

> ```
> {
>   "id": "0a6c526c-4637-4a62-bf38-81aa70c4aa59",
>   "email": "mender-demo@example.com",
>   "created_ts": "2022-06-08T03:58:28.582Z",
>   "updated_ts": "2022-06-08T03:58:28.582Z",
>   "login_ts": "2022-06-08T04:02:06.855Z"
> }
> ```

You can revoke a Personal Access Token by calling the following API end-point using the token ID:

```bash
curl -H "Authorization: Bearer $JWT" -X DELETE -k $MENDER_SERVER_URI/api/management/v1/useradm/settings/tokens/0a6c526c-4637-4a62-bf38-81aa70c4aa59
```

!!! Personal Access Tokens inherit all the permissions and roles of the user who generated them.

!! WARNING: Your personal access token (PAT) will be revoked if your
!! [Mender plan](https://mender.io/product/pricing) or enabled add-ons
!! change. This is because the token contains information about your current plan,
!! and it will become invalid upon upgrade.

### Session Token

If you are using SSO then Personal Access Tokens are not an option to you.
As such, you can still access the APIs and use mender-cli using a Session Token.
To get the session token navigate to [your profile](https://hosted.mender.io/ui/settings/my-profile) and under "Session token" click "COPY TO CLIPBOARD".
Then use this token anywhere that the Personal Access Token should be used.

Session Tokens have the same validity span as a JWT generated using the login endpoint:
* With "Keep me signed in" they are valid for 24 hours
* Without it, the are invalidated after 15 minutes of inactivity.

!!! Session Tokens have similar security implications as Personal Access Tokens do.

## Set up mender-cli

`mender-cli` is a standalone CLI tool that works as a client against the Mender Server management APIs in order to make it much easier to interact with the APIs.

It supports use cases for cloud systems, like uploading an Artifact to the Mender Server, as well as end user workstation use cases like Remote terminal and Port forward (Troubleshoot add-on required).

Over time the functionality of `mender-cli` will be extended to simplify the most common use cases for integrating the Mender Server into other backend and cloud systems. If you need to cover other use cases today, follow the [tutorial for cURL instead](#install-curl-and-jq-and-set-up-the-shell-variables).

First install the `mender-cli` tool as described in the [Downloads page](../../12.Downloads/01.Workstation-tools/docs.md#mender-cli).

Then open a terminal and run the following command to log in to your Mender Server.

```bash
mender-cli login --server https://hosted.mender.io --username myusername@example.com
```

!!! Adjust the server URI and email to the correct values for the server you are using.

If the log in succeeds, you should see a message similar to the following:

> login successful


You can now use the other options of mender-cli to interact with the APIs.
For example, to upload an Artifact you can run the following command:

```bash
./mender-cli artifacts --server https://hosted.mender.io upload release_1.mender
```

Instead of logging in using your credentials, you can specify a Personal Access Token:

```bash
./mender-cli artifacts --server https://hosted.mender.io --token-value $PERSONAL_ACCESS_TOKEN upload release_1.mender
```

<!--AUTOVERSION: "mender-cli/%/"/mender-cli -->
[x.x.x_mender-cli]: https://downloads.mender.io/mender-cli/1.12.0/linux/mender-cli
