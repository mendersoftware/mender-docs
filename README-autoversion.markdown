`autoversion.py` and `AUTOVERSION` tags
=======================================

`AUTOVERSION` tags are used to mark sections of the documentation that have
version numbers in them. This is used to automatically update version numbers
when we release a new version, as well as to catch version numbers that are
added without an appropriate `AUTOVERSION` tag.

## Basic usage

The basic syntax of the `AUTOVERSION` tag is:

```
<!--AUTOVERSION: "{search_string}"/{action} ...-->
```

where `{search_string}` is a string that should be matched against the text. It
must contain at least one `%`, which is the location in the string where the
version is. Note that it should also include some surrounding text to avoid
false matches.

`{action}` is the action to take for this particular version string. The actions
come in three flavors, described in the next sections.

Each `AUTOVERSION` tag is only active for the code block or paragraph
immediately following it (*).

(*) There is one exception: The tag may come after a page header, and affect
that header. The reason this exception was made is because the page doesn't
render correctly if the tag is above the page header. This only works if the tag
comes *immediately* after the header.


### Version numbers for Mender components

In this case, `{action}` is the name of the repository whose version you would
like to insert in the given location. For example:

<!-- CONGRATULATIONS! If you found this comment, you are one of those that get
to see `AUTOVERSION` in practice. This is an `.md` file just like the others, so
it needs to be covered by `AUTOVERSION` just like every other file. So the
*real* tag is the next one here, the demonstration tag is inside the code
block. Same for the rest of the code blocks. -->

<!--AUTOVERSION: "mender-artifact version %"/ignore-->
```
<!--AUTOVERSION: "mender-artifact version %"/mender-artifact-->
Joe User uses mender-artifact version 2.2.0, and likes it!
```

Note the `%`, which is where the version should go. If mender-artifact is later
updated, `autoversion.py --update` will turn it into this:

<!--AUTOVERSION: "mender-artifact version %"/ignore-->
```
<!--AUTOVERSION: "mender-artifact version %"/mender-artifact-->
Joe User uses mender-artifact version 2.3.0, and likes it!
```


### Version numbers of other software

Version numbers of other software should generally be ignored, and for this
you can use the `ignore` action:

<!--AUTOVERSION: "Docker version %"/ignore-->
```
<!--AUTOVERSION: "Docker version %"/ignore-->
Please use Docker version 1.12.0.
```

This will make the version completely ignored by both the `--check` and
`--update` flags. Without an ignore section though, `--check` would complain
that you might have entered a version number that should have a tag.

Note that the `%` is mandatory even for ignore tags.


### Version numbers that need manual treatment

Although rare, in some corner cases the versions can not be updated manually. In
this case a tag must be inserted to warn about this when the documentation is
being updated. This uses the repository name action, together with the special
`complain` tag and looks like this:

<!--AUTOVERSION: "bleeding-edge % branch"/ignore-->
```
<!--AUTOVERSION: "bleeding-edge % branch"/integration/complain-->
This is documentation for Mender's bleeding-edge master branch
```

In order to turn this into a valid documentation string, the entire sentence
must be restructured to avoid the use of "bleeding-edge" and "branch", so for
this we use the `complain` action. It will not complain in `--check` mode, only
in `--update` mode, when the component is selected for update. The search string
is expected to match the doc text prior to being modified into the correct
sentence, and it must no longer match after being corrected.

This is the only mode where it is permitted not to use a `%` in the search
string.


## Multiple versions in one paragraph

If you have a long paragraph or code block with multiple version numbers, you
can include several search and action pairs in one tag by separating them with
spaces, like this:

<!--AUTOVERSION: "Docker % and integration %"/ignore-->
```
<!--AUTOVERSION: "Docker %"/ignore "integration %"/integration-->
Please use Docker 1.12.0 and integration 1.6.0.
```


## Using `autoversion.py`

The `autoversion.py` supports two modes, `--check` and `--update`. `--check`
checks that there are no versions numbers in the documentation that are not
covered by an `AUTOVERSION` tag, and is part of our tests.

`--update` updates references of all given components, which can be:

* `--mender-version` - Updates all components for a Mender release, including
  micro services. This one requires `--integration-dir` to be given as well

* `--mender-convert-version` - Updates all mender-convert references

* `--meta-mender-version` - Updates all meta-mender references. This requires
  `--poky-version` to be specified as well

See the command line help for more information.
