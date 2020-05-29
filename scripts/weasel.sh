#!/bin/bash
#
# Simple weasel words checker from "My Ph.D advisor rewrote himself in Bash"
#
# http://matt.might.net/articles/shell-scripts-for-passive-voice-weasel-words-duplicates/
#
# Usage:
#   weasel.sh <file> ...
#

GREEN='\033[0;32m'   # Error
YELLOW='\033[1;33m' # Warning
RED='\033[0;31m'    # Error
IRED='\033[0;91m'   # Fatal Error
NC='\033[0m'        # No Color


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

    N_LINES=$(wc --lines $file | cut -f1 -d ' ')

    N_WEASEL=$(egrep --ignore-case --only-matching --count "\\b($weasels)\\b" $file)

    PERCENTAGE=$(( 100 * ${N_WEASEL}/${N_LINES}))

    filename=${file#*mender-docs}
    if (( ${PERCENTAGE} > ${RATE_CUTOFF} )); then
      echo -e "${RED}[FAIL] The weasel-word rate for ${filename}:\n\tweasel-words/total-lines = ${N_WEASEL}/${N_LINES} ~= ${PERCENTAGE}% - and thus above the cut-off rate: ${RATE_CUTOFF}%${NC}"
      exit 1
    else
      echo -e "${GREEN}[OK] The weasel rate for ${filename}:\n\tweasel-words/total-lines = ${N_WEASEL}/${N_LINES} ~= ${PERCENTAGE} - and thus below the cut-off rate: ${RATE_CUTOFF}${NC}"
    fi

  fi
done

exit 0
