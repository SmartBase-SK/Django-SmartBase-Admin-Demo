#!/usr/bin/env bash

if [ ! -f /usr/local/bin/chromedriver ]; then
    apt-get install -y xvfb
    wget https://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip
    apt-get install -y zip
    unzip chromedriver_linux64.zip
    rm chromedriver_linux64.zip
    mv chromedriver /usr/local/bin/
    apt-get install -y chromium chromium-l10n libnss3 libgconf-2-4
fi
