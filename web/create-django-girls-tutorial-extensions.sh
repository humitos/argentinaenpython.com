#!/bin/bash

set -e

PATH=/usr/bin:./node_modules/.bin:$PATH

# HTML

# create the GitBook Django Girls Tutorial Translation
cd ../djangogirls/tutorial-extensions/traducidos/
# npm install gitbook-cli
# gitbook install
gitbook build


# PDF

# we need to run first aep python version (3.6.2) and then the system
# one (because calibre needs Python2 from the system
pyenv local argentinaenpython.com system

# this needs calibre since it uses `ebook-convert`
# https://trello.com/c/JWgZfauR/24-create-pdf-con-gitbook
gitbook pdf
mkdir -p /home/humitos/Source/argentinaenpython.com.ar/web/@djangogirls/pdf
mv book.pdf _book/django-girls-extensiones-tutorial.es.pdf
cp _book/django-girls-extensiones-tutorial.es.pdf /home/humitos/Source/argentinaenpython.com.ar/web/@djangogirls/pdf/
# go back to original directory
cd -

# create symbolic link to the GitBook Django Girls Tutorial Translation
rm -f output/django-girls/extensiones-tutorial
ln -sf ../../../djangogirls/tutorial-extensions/traducidos/_book output/django-girls/extensiones-tutorial
