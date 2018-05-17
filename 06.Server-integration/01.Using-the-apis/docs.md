---
title: Using the APIs
taxonomy:
    category: docs
---

The Mender server microservices are all accessible using an HTTPS API.  These APIs can be used to configure the server (for example, pre-authorizing devices) or implementing custom workflows (for example, integrating the Mender server into an existing device management system.)


## Set up shell variables for cURL

There are many ways to call http-based REST APIs, but the most generally available method is most likely the command line utility `curl`.

Open a terminal, which we will use in the following to call the Mender server's REST APIs. First set a shell variable with the URI of your server:
```bash
MENDER_SERVER_URI='https://hosted.mender.io'
```

!!! Adjust the variable value to the Mender server you are using.

Next, set a variable with your user email on the Mender server (replace its content with your user email):

```bash
MENDER_SERVER_USER='myusername@example.com'
```

Now obtain a management API JSON Web Token by using the [login API](../../apis/management-apis/user-administration-and-authentication#log-in-to-mender):

```bash
JWT=$(curl -X POST -u $MENDER_SERVER_USER $MENDER_SERVER_URI/api/management/v1/useradm/auth/login)
```

!!! If you are using self-signed certificates in a demo setup you may want to skip validation with the `-k` option of `curl` (this is insecure).

You should now have an API token you can use to call any of the [Mender server management APIs](../../apis/management-apis) in the `JWT` shell variable.

!!! The `MENDER_SERVER_URI` and `JWT` shell variables will only exist in the current shell invocation by default, so make sure you use this same shell environment for any interactions with the API.


### Verify you can call the APIs

To verify you can call the server APIs, list the users of your Mender server instance:

```bash
curl -H "Authorization: Bearer $JWT" $MENDER_SERVER_URI/api/management/v1/useradm/users
```

If it succeeds it will return something like the following:

```bash
[
    {
        "created_ts": "2018-05-17T18:34:03.164Z",
        "email": "myusername@example.com",
        "id": "316517b2-fa41-4dd5-91e9-3ee7668ed230",
        "updated_ts": "2018-05-17T18:34:03.164Z"
    }
]
```

If this fails, e.g. returns `401 Authorization Required`, make sure that the contents of your `JWT` and `MENDER_SERVER_URI` shell variables is correct and re-run the steps above if necessary.
