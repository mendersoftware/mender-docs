#!/bin/sh
set -e -x -u

# This script triggers a build of the mender-doc in travis, which redeploys the webite.
# The only argument you have to pass to this script is the branch of mender-docs you want to build.

body=$(cat <<EOF
    {
      "request": {
         "branch": "$1"
    }}
EOF
)

curl -s -X POST \
   -H "Content-Type: application/json" \
   -H "Accept: application/json" \
   -H "Travis-API-Version: 3" \
   -H "Authorization: token $TRAVIS_COM_TOKEN" \
   -d "$body" \
   https://api.travis-ci.com/repo/mendersoftware%2Fmender-docs-site/requests
