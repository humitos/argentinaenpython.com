#!/bin/bash

set -e

# # create folder structure
mkdir -p @djangogirls
cd @djangogirls
mkdir -p django gedit/windows git/{mac,windows} notepad++/windows pdf python/{mac,windows} 'sublime text'/v3/{linux, mac, windows} website

# download all the needed data
# django
wget -c https://pypi.python.org/packages/82/33/f9d2871f3aed5062661711bf91b3ebb03daa52cc0e1c37925f3e0c4508c5/Django-1.11.6-py2.py3-none-any.whl#md5=89322a57ced871be6e794a9a63a897a2 \
     --directory-prefix @djangogirls/django

# gedit
wget -c http://ftp.gnome.org/pub/GNOME/binaries/win64/gedit/gedit-x86_64-3.20.1.msi \
     --directory-prefix @djangogirls/gedit/windows

# git
wget -c https://github.com/git-for-windows/git/releases/download/v2.14.2.windows.2/Git-2.14.2.2-32-bit.exe \
     --directory-prefix @djangogirls/git/windows

wget -c https://github.com/git-for-windows/git/releases/download/v2.14.2.windows.2/Git-2.14.2.2-64-bit.exe \
     --directory-prefix @djangogirls/git/windows

# notepad ++
wget -c https://notepad-plus-plus.org/repository/7.x/7.5.1/npp.7.5.1.Installer.exe
     --directory-prefix @djangogirls/notepad++/windows

# python
wget -c https://www.python.org/ftp/python/3.6.3/python-3.6.3.exe
     --directory-prefix @djangogirls/python/windows

wget -c https://www.python.org/ftp/python/3.6.3/python-3.6.3-amd64.exe
     --directory-prefix @djangogirls/python/windows

wget -c https://www.python.org/ftp/python/3.4.4/python-3.4.4.msi
     --directory-prefix @djangogirls/python/windows

wget -c https://www.python.org/ftp/python/3.4.4/python-3.4.4.amd64.msi
     --directory-prefix @djangogirls/python/windows

wget -c https://www.python.org/ftp/python/3.6.3/python-3.6.3-macosx10.6.pkg
     --directory-prefix @djangogirls/python/windows

# create the compressed file
zip -r django-girls-recursos.zip @djangogirls

# create symlink pointing to the new file
cd output/django-girls
ln -fs ../../django-girls-recursos.zip .
cd -
