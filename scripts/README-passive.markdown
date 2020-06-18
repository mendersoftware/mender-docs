# Passive.sh - A simple passive voice checker

`passive.sh` is a simple script which does a simple regex search for passive
voice using a regex search on the documentation text.

The script always outputs any passive voice it finds, but only fails on default
if there are more than 3% in the file total. This cutoff can be modified through
the environment variable: `RATE_CUTOFF`.

## Usage

```console
bash ./scripts/passive.sh <file>
```

## Example

> ```console
> mender-docs: bash ./scripts/passive.sh 04.Artifacts/*/*.md 
> 04.Artifacts/20.Provisioning-a-new-device/docs.md:12:is intended
> 04.Artifacts/20.Provisioning-a-new-device/docs.md:32:be used
> 04.Artifacts/20.Provisioning-a-new-device/docs.md:35:is meant
> 04.Artifacts/20.Provisioning-a-new-device/docs.md:50:is placed
> [OK] The passive rate for 04.Artifacts/10.Yocto-project/docs.md:
> 	passive-words/total-lines = 4/60 ~= 1 - and thus below the cut-off rate: 3
> ```
