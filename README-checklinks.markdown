# checklinks

`checklinks` is a `node.js` script based upon the
[`remark-validate-links`](https://github.com/remarkjs/remark-validate-links)
tool. It validates all internal links (i.e., [foobar](#install)).

## Install

The tool has a few `node.js` requirements. If you already have `node` installed on your system, run:

```console
npm install
```

in the documentation directory.

## Usage

```console
./checklinks [directory]
```

This will validate internal link references on all files ending with `.md` in
the repository. If invalid links are found, an error message is shown with
details about the invalid link, and an error code is returned.

## Output

> ```console
> mender-docs: ./checklink 
> Do not fail on missing sections in API links
> Do not fail on missing sections in API links
> Do not fail on missing sections in API links
> 01.Getting-started/02.On-premise-installation/docs.md
>   13:146-13:224  warning  Link to unknown file: `../01.uickstart-with-raspberry-pi/docs.md`. Did you mean `../01.Quickstart-with-raspberry-pi/docs.md`  missing-file  remark-validate-links
> 
> ⚠ 1 warning
> ```

## Ignoring paths

The link-checker has the ability to ignore failing links to certain files, by
adding the absolute path to the file `.checklinks-whitelist`. The `paths` field
list is then matched as a substring search to every link in the documentation.
As such, all links pointing to the `200.API` section is ignored by default, as
this section is generated independently from `mender-api-docs` repo.

## Note

A few things to keep in mind:

* The checker does not verify sections in the `200.API` folder, as this
  section is generated independently from `mender-api-docs` repo, and
  not present when the tool is run.
* The header slug is a modified Github header slugger, which collapses multiple dashes into one. That is slug(---) -> slug(-). This is because Grav, which our documentation uses does not fully support the Github slug format.


# didyoumean -- Automatic broken link fixing

`didyoumean` is a simple script which helps migrating sections in the
documentation with the help of the `checklinks` script.

The script takes the output from `checklinks`, which can be on the form:

> ```console
> 02.Overview/01.Introduction/docs.md
>   30:433-30:573  warning  Link to unknown heading in `../../04.Artifacts/10.Yocto-project/02.Image-configuration/docs.md`: `disabling-mender-s-a-system-service`. Did you mean `disabling-mender-as-a-system-service`  missing-heading-in-file  remark-validate-links
> 
> 1 warning
> ```

Notice the `Did you mean` part. This is output from the checklinks script if the
string distance between the erronous link, and a valid link is close enough.

Thus, this can be taken advantage of by the `didyoumean` script. The script will
automatically rewrite all the suggested links:

```console
checklinks |& bash ./scripts/didyoumean
```
Resulting in a successfully migrated section.

## If unsuccesful

If the string distance is too big, the `checklinks` is unable to guess the
replacement candidate, and obviously, the `didyoumean` script is unable to fill
in the replacement. In this instance, the replacement must be done by hand. A
recommendation is to script this also. Most modern editors have some sort of
server support, which means it enables you to open a buffer of a given file,
with the cursor at a given line and column.

For `Emacs` this would be something like:

```console
emacsclient +<line>:<column> <filepath>
```
