# didyoumean - A simple passive voice checker

`didyoumean` is a simple script helps migrating sections in the documentation
with the help of the `checklinks` script.

The script takes the output from `checklinks`, which can be on the form:

```bash
02.Overview/01.Introduction/docs.md
  30:433-30:573  warning  Link to unknown heading in `../../04.Artifacts/10.Yocto-project/02.Image-configuration/docs.md`: `disabling-mender-s-a-system-service`. Did you mean `disabling-mender-as-a-system-service`  missing-heading-in-file  remark-validate-links

1 warning
```

Notice the `Did you mean` part. This is output from the checklinks script if the
string distance between the erronous link, and a valid link is close enough.

Thus, this can be taken advantage of by the `didyoumean` script.
The script will automatically rewrite all the suggested links:

```bash
checklinks |& bash ./scripts/didyoumean
```
Resulting in a successfully migrated section.

# If unsuccesful

If the string distance is too big, the `checklinks` is unable to guess the
replacement candidate, and obviously, the `didyoumean` script is unable to fill
in the replacement. In this instance, the replacement must be done by hand. A
recommendation is to script this also. Most modern editors have some sort of
server support, which means it enables you to open a buffer of a given file,
with the cursor at a given line and column.

For `Emacs` this would be something like:

```bash
emacsclient +<line>:<column> <filepath>
```
