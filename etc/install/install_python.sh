#!/bin/bash

cd /home/vagrant

apt-get update -y
# Python dev packages
apt-get install -y build-essential checkinstall python3-dev python3-setuptools python3-pip curl
# python-setuptools being installed manually
wget -q https://bootstrap.pypa.io/ez_setup.py -O - | python3
# Dependencies for image processing with Pillow (drop-in replacement for PIL)
# supporting: jpeg, tiff, png, freetype, littlecms
# (pip install pillow to get pillow itself, it is not in requirements.txt)
apt-get install -y python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 shared-mime-info pango1.0-tests pandoc libcairo2-dev libjpeg-dev libfreetype6-dev liblcms2-dev libxml2-dev libxslt-dev python3-lxml libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev libncurses5-dev libreadline-dev libgdm-dev libdb4o-cil-dev libpcap-dev openssl gettext rsync

# python 3.11 install
cd /usr/src
wget -q https://www.python.org/ftp/python/3.11.3/Python-3.11.3.tgz
tar xzf Python-3.11.3.tgz
cd Python-3.11.3
./configure --with-zlib
make
make install
# python 3.11.3 install
