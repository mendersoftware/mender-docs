---
title: Using the APIs
taxonomy:
    category: docs
---

The Mender server microservices are all accessible using an HTTPS API. These APIs can be used to configure the server (for example, preauthorizing devices) or implementing custom workflows (for example, integrating the Mender server into an existing device management system.) There are separate APIs for [Open Source](../../200.APIs/01.Open-source/docs.md) and [Enterprise](../../200.APIs/02.Enterprise/docs.md).

There are many ways to interact with Mender's REST APIs and the most common ones are shown below.

## Set up mender-cli

`mender-cli` is a standalone CLI tool that works as a client against the Mender server management APIs in order to make it much easier to interact with the APIs.

Currently two use cases are supported:

* Log in
* Upload Artifact

Over time the functionality of `mender-cli` will be extended to simplify the most common use cases for integrating the Mender server into other backend and cloud systems. If you need to cover other use cases today, follow the [tutorial for cURL instead](#set-up-shell-variables-for-curl).

First download the [prebuilt mender-cli Linux binary here][x.x.x_mender-cli].

!!! If you need to build `mender-cli` from source, the general steps are the same as for [compiling mender-artifact from source](../../04.Artifacts/25.Modifying-a-Mender-Artifact/docs.md#compiling-mender-artifact). Just use the [mender-cli repository](https://github.com/mendersoftware/mender-cli?target=_blank) instead of the mender-artifact repository.

Then open a terminal in the directory you downloaded `mender-cli` and run the following commands to log in to your Mender server.

```bash
chmod +x mender-cli
./mender-cli login --server https://hosted.mender.io --username myusername@example.com
```

!!! Adjust the server URI and email to the correct values for the server you are using.

If the log in succeeds, you should see a message similar to the following:

> login successful


You can now use the other options of mender-cli to interact with the APIs.
For example, to upload an Artifact you can run the following command:

```bash
./mender-cli artifacts --server https://hosted.mender.io upload release_1.mender
```


## Set up shell variables for cURL

There are many ways to call http-based REST APIs, but the most generally available method is the command line utility `curl`. The `jq` utility is commonly used to decode JSON messages and display them in human-readable format. REST API responses can contain raw data and must run through a JSON parser (`jq`).

You can easily get both using:

```bash
sudo apt-get install curl jq
```

Open a terminal, which we will use in the following to call the Mender server's REST APIs. First set a shell variable with the URI of your server:
```bash
MENDER_SERVER_URI='https://hosted.mender.io'
```

!!! Adjust the variable value to the Mender server you are using.

Next, set a variable with your user email on the Mender server (replace its content with your user email):

```bash
MENDER_SERVER_USER='myusername@example.com'
```

Now obtain a management API JSON Web Token by using the [Open Source](../../200.APIs/01.Open-source/02.Management-APIs/06.User-administration-and-authentication/docs.md#log-in-to-mender) or [Enterprise](../../200.APIs/02.Enterprise/02.Management-APIs/06.User-administration-and-authentication/docs.md#log-in-to-mender) login API:

```bash
JWT=$(curl -X POST -u $MENDER_SERVER_USER $MENDER_SERVER_URI/api/management/v1/useradm/auth/login)
```

!!! If you are using self-signed certificates in a demo setup you may want to skip validation with the `-k` option of `curl` (this is insecure).

You should now have an API token you can use to call any of the [Mender server management APIs](../../200.APIs/01.Open-source/02.Management-APIs/docs.md) in the `JWT` shell variable.

!!! The `MENDER_SERVER_URI` and `JWT` shell variables will only exist in the current shell invocation by default, so make sure you use this same shell environment for any interactions with the API.


### Verify you can call the APIs

To verify you can call the server APIs, list the users of your Mender server instance:

```bash
curl -H "Authorization: Bearer $JWT" $MENDER_SERVER_URI/api/management/v1/useradm/users | jq '.'
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

<!--AUTOVERSION: "mender-cli/%/"/mender-cli -->
[x.x.x_mender-cli]: https://d1b0l86ne08fsf.cloudfront.net/mender-cli/master/linux/mender-cli
