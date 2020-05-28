#!/bin/bash
#
# Simple weasel words checker from "My Ph.D advisor rewrote himself in Bash"
#
# http://matt.might.net/articles/shell-scripts-for-passive-voice-weasel-words-duplicates/
#
# Usage:
#   weasel.sh <file> ...
#

if [[ "$1" == "" ]]; then
  echo "usage: `basename $0` <file> ..."
  exit
fi

weasels="many|various|very|fairly|several|extremely\
|exceedingly|quite|remarkably|few|surprisingly\
|mostly|largely|huge|tiny|((are|is) a number)\
|excellent|interestingly|significantly\
|substantially|clearly|vast|relatively|completely"

RATE_CUTOFF=${RATE_CUTOFF:-3}

for file in $*; do

  if egrep --ignore-case --with-filename --line-number --only-matching --colour=always "\\b($weasels)\\b" $file; then

    N_WORDS=$(wc --words $file | cut -f1 -d ' ')

    N_PASSIVE=$(egrep --ignore-case --only-matching --count "\\b($weasels)\\b" $file)

    PERCENTAGE=$(( 100 * ${N_PASSIVE}/${N_WORDS}))

    if (( ${PERCENTAGE} > ${RATE_CUTOFF} )); then
      echo "The weasel-word rate for $file is ${PERCENTAGE} and thus above the cut-off rate: ${RATE_CUTOFF}"
      exit 1
    fi

  fi
done

exit 0
