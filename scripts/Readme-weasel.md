# weasel.sh - A simple weasel-word checker

`weasel.sh` is a simple script which does a simple regex search for [weasel
words](https://en.wikipedia.org/wiki/Weasel_word) using a regex search on the
documentation text.

The script always outputs any weasel words it finds, but only fails on default
if there are more than 3% in the file total. This cutoff can be modified through
the environment variable: `RATE_CUTOFF`.

## Usage

```bash
bash weasel.sh <file>
```

## Example

```bash
$ mender-docs: bash ./scripts/weasel.sh 05.Client-configuration/03.Identity/docs.md 
05.Client-configuration/03.Identity/docs.md:30:very
05.Client-configuration/03.Identity/docs.md:37:several
05.Client-configuration/03.Identity/docs.md:57:several
05.Client-configuration/03.Identity/docs.md:74:very
05.Client-configuration/03.Identity/docs.md:80:Clearly
[OK] The weasel rate for 05.Client-configuration/03.Identity/docs.md:
	weasel-words/total-lines = 5/131 ~= 3 - and thus below the cut-off rate: 3
```
