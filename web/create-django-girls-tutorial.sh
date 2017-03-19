#!/bin/bash

set -e

# HTML

# create the GitBook Django Girls Tutorial Translation
cd ../djangogirls/tutorial/our/es/
# npm install gibook-cli
# ./node_modules/.bin/gitbook install
./node_modules/.bin/gitbook build


# PDF
# this needs calibre since it uses `ebook-convert`
# https://trello.com/c/JWgZfauR/24-create-pdf-con-gitbook
./node_modules/.bin/gitbook pdf
mv book.pdf _book/django-girls-tutorial.es.pdf

# go back to original directory
cd -

# create symbolic link to the GitBook Django Girls Tutorial Translation
rm -f output/django-girls/tutorial
ln -sf ../../../djangogirls/tutorial/our/es/_book output/django-girls/tutorial

