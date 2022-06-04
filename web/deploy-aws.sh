#!/bin/bash

set -e

export BW_SESSION=`bw unlock --raw`
export AWS_ACCESS_KEY_ID=`bw get item 2de9857c-c7d7-45d3-b7f4-ae5500daf50c | jq --raw-output ".fields[0].value"`
export AWS_SECRET_ACCESS_KEY=`bw get item 2de9857c-c7d7-45d3-b7f4-ae5500daf50c | jq --raw-output ".fields[1].value"`

aws s3 sync --follow-symlinks --acl public-read output/ s3://humitos-sites/apps/argentinaenpython/
aws cloudfront create-invalidation --distribution-id EKTBPXJN42478 --paths "/*"

unset BW_SESSION
unset AWS_ACCESS_KEY_ID
unset AWS_SECRET_ACCESS_KEY
