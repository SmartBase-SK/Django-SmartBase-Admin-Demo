#!/usr/bin/env bash

wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
apt-get update
apt-get install -y apt-transport-https
echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
apt-get update
apt-get install -y kibana=7.8.0
echo 'server.host: "0.0.0.0"' >> /etc/kibana/kibana.yml
echo 'server.basePath: "/admin/purchase/purchase/proxy-kibana"' >>  /etc/kibana/kibana.yml
