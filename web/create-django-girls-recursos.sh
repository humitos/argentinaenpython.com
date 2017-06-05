#!/bin/bash

set -e

# create the compressed file
zip -r django-girls-recursos.zip @djangogirls

# create symlink pointing to the new file
cd output/django-girls
ln -fs ../../django-girls-recursos.zip .
cd -
