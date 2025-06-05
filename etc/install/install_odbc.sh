#!/bin/bash

# Install essential packages from Apt
echo 'deb http://deb.debian.org/debian stretch-backports main' >> /etc/apt/sources.list
apt-get update -y

# Install odbc, FreeTDS
apt-get install -y unixodbc unixodbc-dev
apt-get -y install tdsodbc

# Copy config files for ODBC
# for configuration see ProSpanek project
sudo cp $PROJECT_DIR/etc/odbc.ini /etc/odbc.ini
sudo cp $PROJECT_DIR/etc/odbcinst.ini /etc/odbcinst.ini
sudo mkdir -p /etc/freetds/
sudo cp $PROJECT_DIR/etc/freetds/freetds.conf /etc/freetds/freetds.conf
