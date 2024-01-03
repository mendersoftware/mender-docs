# Contribute to the Mender documentation

Thank you for showing interest in contributing to the Mender project. Connecting
with contributors and growing a community is very important to us. We hope you
will find what you need to get started writing documentation on this page.

## Provide a pull request

Pull requests are very welcome, and the maintainers of Mender work hard to stay
on top to review and hopefully merge your work.

If your work is significant, it can make sense to discuss the idea with the
maintainers and relevant project members upfront. Start a discussion on our
[Mender Hub forum](https://hub.mender.io/c/general-discussions).

### Sign your work

Mender is licensed under the Apache License, Version 2.0. To ensure open source
license compatibility, we need to keep track of the origin of all commits and
make sure they comply with this license. To do this, we follow the same
procedure as used by the Linux kernel, and ask every commit to be signed off.

The sign-off is a simple line at the end of the explanation for the patch, which
certifies that you wrote it or otherwise have the right to pass it on as an
open-source commit.  The rules are pretty simple: if you can certify the below
(from [developercertificate.org](http://developercertificate.org/)):


```
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.
660 York Street, Suite 102,
San Francisco, CA 94110 USA

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.

Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
```

Then you just add a line to every git commit message:

    Signed-off-by: Random J Developer <random@developer.example.org>

Use your real name (sorry, no pseudonyms or anonymous contributions).

If you set your `user.name` and `user.email` git configs, you can sign your
commit automatically with `git commit -s`.

## Write documentation

### Documentation style guide

Writing documentation for the Mender project requires that you follow the style
guide as outlined in the [style guide document](./README-styleguide.markdown).

The project also has a dedicated guide to the CLI and Bash script examples
[here](./README-bash-styleguide.markdown).

### Tools for documentation writers

The project has a few tools to help with developing documentation:

* [checklinks](README-checklinks.markdown) - Which automatically checks all internal links for duds.
* [./scripts/weasel.sh](./scripts/README-weasel.markdown) - Checks a document for weasel words.
* [autoversion.py](README-autoversion.markdown) - Checks the version of a linked external tool.


## Let us work together with you

In an ever more digitized world, securing the world's connected devices is a
very important and meaningful task. To succeed, we will need to row in the same
direction and work to the best interest of the project.

This project appreciates your friendliness, transparency and a collaborative
spirit.
