#!/bin/bash

set -e

PATH=./node_modules/.bin:$PATH

# HTML

# create the GitBook Django Girls Coach Manual
cd ../djangogirls/coach-manual/traducidos
# npm install gitbook-cli
# gitbook install
gitbook build


# PDF
# this needs calibre since it uses `ebook-convert`
# https://trello.com/c/JWgZfauR/24-create-pdf-con-gitbook
gitbook pdf
mkdir -p /home/humitos/Source/argentinaenpython.com.ar/web/@djangogirls/pdf
mv book.pdf _book/django-girls-coach.es.pdf
cp _book/django-girls-coach.es.pdf /home/humitos/Source/argentinaenpython.com.ar/web/@djangogirls/pdf/
# go back to original directory
cd -

# create symbolic link to the GitBook Django Girls Tutorial Translation
rm -rf output/django-girls/manual-de-guia
ln -sf ../../../djangogirls/coach-manual/traducidos/_book output/django-girls/manual-de-guia
