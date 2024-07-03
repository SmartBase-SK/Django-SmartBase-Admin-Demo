#!/bin/bash

# Script to set up a Django project on Vagrant.

# Installation settings

PROJECT_NAME=${1:-smartshop}
PROJECT_DIR=/home/vagrant/$PROJECT_NAME

find $PROJECT_DIR/etc/install/ -maxdepth 1 -type f -exec bash -c '<<< "$(< {})" tr -d "\r" > {}' \;

echo "install_java"
sudo $PROJECT_DIR/etc/install/install_java.sh

echo "install_postgresql"
sudo $PROJECT_DIR/etc/install/install_postgresql.sh $PROJECT_NAME

echo "install_python"
sudo $PROJECT_DIR/etc/install/install_python.sh

echo "install_git"
sudo $PROJECT_DIR/etc/install/install_git.sh

echo "install_virtualenv"
sudo $PROJECT_DIR/etc/install/install_virtualenv.sh $PROJECT_NAME

echo "install_elasticsearch"
sudo $PROJECT_DIR/etc/install/install_elasticsearch.sh $PROJECT_NAME

echo "install_redis"
sudo $PROJECT_DIR/etc/install/install_redis.sh

echo "install_phantomjs"
sudo $PROJECT_DIR/etc/install/install_phantomjs.sh

echo "install_kibana"
sudo $PROJECT_DIR/etc/install/install_kibana.sh

echo "install_logstash"
sudo $PROJECT_DIR/etc/install/install_logstash.sh

echo "install_selenium"
sudo $PROJECT_DIR/etc/install/install_selenium.sh

echo "install_odbc"
sudo $PROJECT_DIR/etc/install/install_odbc.sh

echo "initial_setup"
sudo $PROJECT_DIR/etc/install/initial_setup.sh
