#!/bin/bash

PROJECT_NAME=${1:-smartshop}
PROJECT_DIR=/home/vagrant/$PROJECT_NAME
VIRTUALENV_DIR=/home/vagrant/.virtualenvs/smartshop

# run all services for manage.py to be able to run
sudo $PROJECT_DIR/etc/install/startup.sh

# Set execute permissions on manage.py, as they get lost if we build from a zip file
chmod a+x $PROJECT_DIR/manage.py

echo "Install pg extensions"
su - vagrant -c "$VIRTUALENV_DIR/bin/python3 $PROJECT_DIR/manage.py install_pg_extensions"
