#!/bin/bash

set -e

rsync --progress --human-readable --recursive --links --verbose --update --compress --delete-after --exclude-from=rsync.exclude --copy-links --bwlimit=250 --stats --partial --partial-dir=/tmp output/* humitos@elblogdehumitos.com:apps/argentinaenpython.com.ar/

# rsync --progress --human-readable --recursive --links --verbose --update --compress --delete-after --exclude-from=rsync.exclude --copy-links --bwlimit=50 --stats --partial --partial-dir=/tmp output/* alarm@raspberrypi.redlibre:~/apps/argentinaenpython.com.ar/
