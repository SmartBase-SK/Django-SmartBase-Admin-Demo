#!/bin/bash

apt-get update -y
# Git (we'd rather avoid people keeping credentials for git commits in the repo, but sometimes we need it for pip requirements that aren't in PyPI)
apt-get install -y git
