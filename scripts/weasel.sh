#!/bin/bash
#
# Simple weasel words checker from "My Ph.D advisor rewrote himself in Bash"
#

PATH="/bin/:/usr/bin:/sbin"

if [[ "$1" == "" ]]; then
  echo "usage: `basename $0` <file> ..."
  exit
fi

weasels="many|various|very|fairly|several|extremely\
|exceedingly|quite|remarkably|few|surprisingly\
|mostly|largely|huge|tiny|((are|is) a number)\
|excellent|interestingly|significantly\
|substantially|clearly|vast|relatively|completely"

! egrep --ignore-case --line-number --colour=always "\\b($weasels)\\b" $*

exit $?
