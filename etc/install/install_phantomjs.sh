#!/usr/bin/env bash

if ! command phantomjs -v; then
    cd /usr/local/src
    wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
    tar xjf phantomjs-2.1.1-linux-x86_64.tar.bz2
    rm phantomjs-2.1.1-linux-x86_64.tar.bz2
    ln -s /usr/local/src/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/share/phantomjs
    ln -s /usr/local/src/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs
    ln -s /usr/local/src/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin/phantomjs
fi
