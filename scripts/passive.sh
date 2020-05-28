#!/bin/bash
#
# Simple passive voice checker from "My Ph.D advisor rewrote himself in Bash"
#
# http://matt.might.net/articles/shell-scripts-for-passive-voice-weasel-words-duplicates/
#
# Usage:
#
# passive.sh <file> ...
#

irregulars="awoken|\
been|born|beat|\
become|begun|bent|\
beset|bet|bid|\
bidden|bound|bitten|\
bled|blown|broken|\
bred|brought|broadcast|\
built|burnt|burst|\
bought|cast|caught|\
chosen|clung|come|\
cost|crept|cut|\
dealt|dug|dived|\
done|drawn|dreamt|\
driven|drunk|eaten|fallen|\
fed|felt|fought|found|\
fit|fled|flung|flown|\
forbidden|forgotten|\
foregone|forgiven|\
forsaken|frozen|\
gotten|given|gone|\
ground|grown|hung|\
heard|hidden|hit|\
held|hurt|kept|knelt|\
knit|known|laid|led|\
leapt|learnt|left|\
lent|let|lain|lighted|\
lost|made|meant|met|\
misspelt|mistaken|mown|\
overcome|overdone|overtaken|\
overthrown|paid|pled|proven|\
put|quit|read|rid|ridden|\
rung|risen|run|sawn|said|\
seen|sought|sold|sent|\
set|sewn|shaken|shaven|\
shorn|shed|shone|shod|\
shot|shown|shrunk|shut|\
sung|sunk|sat|slept|\
slain|slid|slung|slit|\
smitten|sown|spoken|sped|\
spent|spilt|spun|spit|\
split|spread|sprung|stood|\
stolen|stuck|stung|stunk|\
stridden|struck|strung|\
striven|sworn|swept|\
swollen|swum|swung|taken|\
taught|torn|told|thought|\
thrived|thrown|thrust|\
trodden|understood|upheld|\
upset|woken|worn|woven|\
wed|wept|wound|won|\
withheld|withstood|wrung|\
written"

if [ "$1" = "" ]; then
 echo "usage: `basename $0` <file> ..."
 exit
fi

RATE_CUTOFF=${RATE_CUTOFF:-3}

for file in $*; do

  if egrep --ignore-case --with-filename  --line-number --only-matching --color=always \
       "\\b(am|are|were|being|is|been|was|be)\
\\b[ ]*(\w+ed|($irregulars))\\b" $*; then

    N_WORDS=$(wc --words $file | cut -f1 -d ' ')

    N_PASSIVE=$(egrep --ignore-case --only-matching --count  \
                      "\\b(am|are|were|being|is|been|was|be)\
\\b[ ]*(\w+ed|($irregulars))\\b" $file)

    PERCENTAGE=$(( 100 * ${N_PASSIVE}/${N_WORDS}))

    if (( ${PERCENTAGE} > ${RATE_CUTOFF} )); then
      echo "The passive rate for ${file} is ${PERCENTAGE} and thus above the cut-off rate: ${RATE_CUTOFF}"
      exit 1
    fi

  fi

done

exit 0
