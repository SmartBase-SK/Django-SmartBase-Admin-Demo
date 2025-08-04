#!/bin/bash

# elasticsearch settings and run
sudo sysctl -w vm.max_map_count=262144
ulimit -n 65536

sudo /etc/init.d/redis_6379 start
sudo systemctl start elasticsearch.service
# this is not used most of the time and eats RAM
#sudo systemctl start kibana.service
#sudo systemctl start logstash.service
