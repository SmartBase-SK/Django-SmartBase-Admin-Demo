#!/usr/bin/env bash

if ! command redis-server --version; then
    cd /usr/local/src/
    wget http://download.redis.io/releases/redis-7.0.9.tar.gz
    tar xzf redis-7.0.9.tar.gz
    rm redis-7.0.9.tar.gz
    cd redis-7.0.9
    make
    ln -s /usr/local/src/redis-7.0.9/src/redis-server /usr/local/bin/redis-server
    ln -s /usr/local/src/redis-7.0.9/src/redis-server /usr/bin/redis-server
    ln -s /usr/local/src/redis-7.0.9/src/redis-cli /usr/local/bin/redis-cli
    ln -s /usr/local/src/redis-7.0.9/src/redis-cli /usr/bin/redis-cli
    mkdir /etc/redis
    mkdir /var/redis
    cp /usr/local/src/redis-7.0.9/utils/redis_init_script /etc/init.d/redis_6379
    mkdir /var/redis/6379
    update-rc.d redis_6379 defaults
fi
