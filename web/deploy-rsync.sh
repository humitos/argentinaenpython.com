#!/bin/bash

set -e

# create the GitBook Django Girls Tutorial Translation
cd ../djangogirls/tutorial/our/es/
# npm install gibook-cli
# ./node_modules/.bin/gitbook install
./node_modules/.bin/gitbook build
cd -

# create symbolic link to the GitBook Django Girls Tutorial Translation
rm output/django-girls/gitbook
ln -sf ../../../djangogirls/tutorial/our/es/_book output/django-girls/gitbook

rsync --progress --human-readable --recursive --links --verbose --update --compress --delete-after --exclude-from=rsync.exclude --copy-links --bwlimit=250 --stats --partial --partial-dir=/tmp output/* humitos@elblogdehumitos.com:apps/argentinaenpython.com.ar/

rsync --progress --human-readable --recursive --links --verbose --update --compress --delete-after --exclude-from=rsync.exclude --copy-links --bwlimit=50 --stats --partial --partial-dir=/tmp output/* alarm@raspberrypi.redlibre:~/apps/argentinaenpython.com.ar/
