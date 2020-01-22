#!/bin/sh

mongo_url=mender-mongo:27017
export WORKFLOWS_MONGO_URL="mongodb://${mongo_url}"

if [ "${mongo_url}" != "" ]; then
 while ! nc -z -v "${mongo_url}"; do
  echo "`date` workflows: waiting for mongodb to be ready at $mongo_url";
  sleep 1;
 done;
fi;
/usr/bin/workflows --config /etc/workflows/config.yaml server --automigrate
