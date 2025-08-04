#!/bin/bash

PROJECT_NAME=${1:-smartshop}
DB_NAME=$PROJECT_NAME

sudo apt-get update -y
sudo apt-get install -y vim wget gnupg
# Create the file repository configuration:
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update -y

# Postgresql
if ! command -v psql; then
    sudo apt-get install -y postgresql libpq-dev
    # Create vagrant pgsql superuser
    sudo su postgres bash -c "psql -c \"CREATE USER vagrant WITH PASSWORD 'vagrant';\""
    # user need to be superuser to be able to install extensions
    sudo su postgres bash -c "psql -c \"ALTER USER vagrant WITH SUPERUSER;\""
fi

# postgresql setup for project
sudo su - postgres -c "createdb $DB_NAME"
sudo su postgres bash -c "psql -c \"GRANT ALL PRIVILEGES ON DATABASE $DB_NAME to vagrant;\""
