# Passive.sh - A simple passive voice checker

`passive.sh` is a simple script which does a simple regex search for passive
voice using a regex search on the documentation text.

The script always outputs any passive voice it finds, but only fails on default
if there are more than 3% in the file total. This cutoff can be modified through
the environment variable: `RATE_CUTOFF`.

## Usage

```bash
bash passive.sh <file>
```

## Example

```bash
$ mender-docs: bash ./scripts/passive.sh 01.Getting-started/01.Quickstart-with-raspberry-pi/docs.md
01.Getting-started/01.Quickstart-with-raspberry-pi/docs.md:37:been converted
01.Getting-started/01.Quickstart-with-raspberry-pi/docs.md:37:been installed
01.Getting-started/01.Quickstart-with-raspberry-pi/docs.md:123:be asked
01.Getting-started/01.Quickstart-with-raspberry-pi/docs.md:183:be found
[OK] The passive rate for 01.Getting-started/01.Quickstart-with-raspberry-pi/docs.md:
	passive-words/total-lines = 3/195 ~= 1 - and thus below the cut-off rate: 3

```
