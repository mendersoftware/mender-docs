#!/bin/sh
#
# Run the command line ispell utility on all markdown files.
# Note this uses a custom dictionary located in .ispell_english.
# File checksum, crypto hases and Bitbake variables are difficult to account
# for so this dictionary is rather large and will need to be added to over time.

ispell -p ./.ispell_english $(find . -name '*.md' | \
                                  grep -v '202.Release-information/02.Open-source-licenses/docs.md' | \
                                  grep -v '202.Release-information/01.Release-notes-changelog/docs.md')
