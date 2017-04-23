#!/bin/bash

set -e

# HTML

# create the GitBook Django Girls Tutorial Translation
cd ../djangogirls/tutorial-extensions/traducidos/
# npm install gitbook-cli
# ./node_modules/.bin/gitbook install
./node_modules/.bin/gitbook build


# PDF
# this needs calibre since it uses `ebook-convert`
# https://trello.com/c/JWgZfauR/24-create-pdf-con-gitbook
./node_modules/.bin/gitbook pdf
mkdir -p /home/humitos/Source/argentinaenpython.com.ar/web/@djangogirls/pdf
mv book.pdf _book/django-girls-extensiones-tutorial.es.pdf
cp _book/django-girls-extensiones-tutorial.es.pdf /home/humitos/Source/argentinaenpython.com.ar/web/@djangogirls/pdf/
# go back to original directory
cd -

# create symbolic link to the GitBook Django Girls Tutorial Translation
rm -f output/django-girls/extensiones-tutorial
ln -sf ../../../djangogirls/tutorial-extensions/traducidos/_book output/django-girls/extensiones-tutorial
