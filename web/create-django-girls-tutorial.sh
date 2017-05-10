#!/bin/bash

set -e

PATH=./node_modules/.bin:$PATH

# HTML

# create the GitBook Django Girls Tutorial Translation
cd ../djangogirls/tutorial/our/es/
# npm install gitbook-cli
# npm install svgexport
# gitbook install
gitbook build


# PDF
# this needs calibre since it uses `ebook-convert`
# sudo apt install calibre
# https://trello.com/c/JWgZfauR/24-create-pdf-con-gitbook
gitbook pdf
mkdir -p /home/humitos/Source/argentinaenpython.com.ar/web/@djangogirls/pdf
mv book.pdf _book/django-girls-tutorial.es.pdf
cp _book/django-girls-tutorial.es.pdf /home/humitos/Source/argentinaenpython.com.ar/web/@djangogirls/pdf/
# go back to original directory
cd -

# create symbolic link to the GitBook Django Girls Tutorial Translation
rm -f output/django-girls/tutorial
ln -sf ../../../djangogirls/tutorial/our/es/_book output/django-girls/tutorial

