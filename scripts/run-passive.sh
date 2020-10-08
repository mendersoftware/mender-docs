#!/bin/bash
#
# This script collects all markdown files in the documentation repositories, and
# filters them through the blacklist, and then runs the `passive.sh` script on
# them.
#
# Usage:
#
# ./scripts/run-passive.sh [--verbose]
#
# Note:
#
# The script automatically reads in the .passive-blacklist from the root
# directory, and applies the entries as a filter to a grep expression. Have a
# look at the `.passive-blacklist` file in the root directory for an example of
# how it works.
#


# List all files not in caught by the blacklist
files=$(find . -type f -regex './[0-9]+.*\.md' | grep -vFf .passive-blacklist | sort)

EXIT_CODE=0

for file in $files; do
  if ! ./scripts/passive.sh $* $file; then
    EXIT_CODE=1
  fi
done

exit $EXIT_CODE

