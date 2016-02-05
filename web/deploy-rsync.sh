#!/bin/bash

rsync --progress --human-readable --recursive --links --verbose --checksum --update --compress --delete-after --exclude-from=rsync.exclude --copy-links --bwlimit=50 --stats output/* humitos@mkaufmann.com.ar:apps/argentinaenpython.com.ar/

rsync --progress --human-readable --recursive --links --verbose --checksum --update --compress --delete-after --exclude-from=rsync.exclude --copy-links --bwlimit=50 --stats output/* alarm@raspberrypi.redlibre:~/apps/argentinaenpython.com.ar/
