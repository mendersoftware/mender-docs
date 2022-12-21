Mender Docs `hosted` branch maintenance
=======================================

<!--AUTOVERSION: "%. Whereas the rest"/ignore "point in time from %"/ignore "frequent merges from %"/ignore-->
`hosted` is the only branch in `mender-docs` repository that we update from
master. Whereas the rest of the release branches are branched out at some
point in time from master, and not updated again (except for bugfix releases
or minor text fixes), the `hosted` branch is a "live" branch that gets
frequent merges from master.

## Procedure

To update `hosted` branch:

### 1. Create a new branch from `hosted`

For example:

```
git fetch origin hosted:hosted-update-$(date --iso-8601)
git checkout hosted-update-$(date --iso-8601)
```

<!--AUTOVERSION: "Merge in `%` and"/ignore-->
### 2. Merge in `master` and resolve conflicts

<!--AUTOVERSION: "git merge origin/%"/ignore-->
```
git merge origin/master
<fix conflicts>
git add <files>
git commit -s
```

There are two main cases where conflicts are expected in `hosted`
branch:

#### Latest versions of the Mender components

<!--AUTOVERSION: "while for `%` are %"/ignore "taking % \"text\""/ignore-->
In `hosted` the versions for all Mender components are set to
latest stable release, while for `master` are master. Therefore
these conflicts are resolved by taking master "text" with hosted
"versions".

#### 08.Server-installation and 301.Troubleshoot/Mender-Server

These sections are completely overridden in `hosted` branch, so
conflicts are resolved here by choosing "our" version.

### 3. Run `./autoversion.py --update` and commit the changes

<!--AUTOVERSION: "incoming text from `%`,"/ignore-->
To update version references of any incoming text from `master`,
run `autoversion.py` tool using latest versions. For example:

<!--AUTOVERSION: "--mender-convert-version %"/ignore "--meta-mender-version %"/ignore "--poky-version %"/ignore "--mender-binary-delta-version %"/ignore-->
```
./autoversion.py --update --integration-dir <local-dir> \
      --integration-version staging \
      --meta-mender-version kirkstone \
      --poky-version kirkstone \
```

### 4. Launch a PR and ask for review

The pull request shall target `hosted` branch. The main things
to look for in the review are:

* References to Mender components' versions are correct.
* 08.Server-installation and 301.Troubleshoot/Mender-Server sections
  have the overridden content.
