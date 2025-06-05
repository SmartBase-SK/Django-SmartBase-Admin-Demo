#!/bin/bash

PROJECT_NAME=${1:-smartshop}
PROJECT_DIR=/home/vagrant/$PROJECT_NAME
ELASTICSEARCH_OVERRIDE_DIR=$PROJECT_DIR/etc/elasticsearch_override

wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
apt-get update
apt-get install -y apt-transport-https
echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
apt-get update
apt-get install -y elasticsearch=7.17.9

sudo rsync -avzc $ELASTICSEARCH_OVERRIDE_DIR/config/ /etc/elasticsearch
sudo mkdir -p /usr/share/elasticsearch/logs
sudo mkdir -p /usr/share/elasticsearch/data
sudo chmod 777 /usr/share/elasticsearch/logs
sudo chmod 777 /usr/share/elasticsearch/data

sudo sysctl -w vm.max_map_count=262144
echo "vagrant soft     nofile         65536" | sudo tee --append /etc/security/limits.conf
echo "vagrant hard     nofile         65536" | sudo tee --append /etc/security/limits.conf
echo "session required pam_limits.so" | sudo tee --append /etc/pam.d/common-session
sudo -H -u vagrant bash -c 'ulimit -n'
