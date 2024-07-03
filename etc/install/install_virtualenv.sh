#!/bin/bash

PROJECT_NAME=${1:-smartshop}

PROJECT_DIR=/home/vagrant/$PROJECT_NAME
VIRTUALENV_DIR=/home/vagrant/.virtualenvs/$PROJECT_NAME

# bash environment global setup
cp -p $PROJECT_DIR/etc/install/bashrc /home/vagrant/.bashrc

# virtualenv global setup
if [[ ! -f /usr/local/bin/virtualenv ]]; then
    pip3 install virtualenv virtualenvwrapper stevedore virtualenv-clone
fi
# virtualenv setup for project
su - vagrant -c "/usr/local/bin/virtualenv $VIRTUALENV_DIR --python=/usr/local/bin/python3 && \
    echo $PROJECT_DIR > $VIRTUALENV_DIR/.project && \
    $VIRTUALENV_DIR/bin/pip install -r $PROJECT_DIR/requirements.txt"
