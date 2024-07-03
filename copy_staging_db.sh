#!/bin/bash
echo -n "Server IP (for example: prime.sbdev.sk):"
read SERVER_IP

echo -n User:
read USER

echo -n Password:
read -s PASSWORD
echo

echo -n "Project dir (for example: temponabytok):"
read PROJECT_DIR

HOME_DIR_ON_SERVER="/home/gitlab/${PROJECT_DIR}/"
TMP_PATH=$(mktemp -d)
DUMPS_DIR="${HOME_DIR_ON_SERVER}/db_backups/dumps/"
SERVER=${USER}@${SERVER_IP}

sshpass -p $PASSWORD ssh -o PubkeyAuthentication=no -o StrictHostKeyChecking=no $SERVER "
    mkdir ${TMP_PATH}
    cd ${HOME_DIR_ON_SERVER}
    docker-compose exec -T db bash -c 'bash /db_backups/dump_database.sh'
    cd ${HOME_DIR_ON_SERVER}webapp/django_project/
    find . -path '*migrations*' -name '*.py' -not -path '*__init__*' -exec cp --parents \{\} ${TMP_PATH} \;
"

find ./project ./sbcore -path "*migrations*" -name "*.py" -not -path "*__init__*" -not -path "*sb_migrations*"  -not -name "fix_migrations.py" -exec rm {} \;
sudo su - postgres -c "dropdb smartshop"
sudo su - postgres -c "createdb smartshop"
DUMP_FILE_NAME=$(sshpass -p $PASSWORD ssh $SERVER "ls -tp ${DUMPS_DIR} | grep -v / | head -n 1")
sshpass -p $PASSWORD rsync -rtu -e 'ssh -o PubkeyAuthentication=no -o StrictHostKeyChecking=no -p 22' $SERVER:$TMP_PATH/* .
sshpass -p $PASSWORD rsync -rtu -e 'ssh -o PubkeyAuthentication=no -o StrictHostKeyChecking=no -p 22' $SERVER:${HOME_DIR_ON_SERVER}db_backups/dumps/$DUMP_FILE_NAME ./dump.sql.tar
tar -xvkf dump.sql.tar
DUMP_FILE_NAME=${DUMP_FILE_NAME/".tar"/""}
mv "./db_backups/dumps/${DUMP_FILE_NAME}" "./db_backups/dumps/dump.sql"
sudo su - postgres -c "cat /home/vagrant/smartshop/db_backups/dumps/dump.sql | psql -U postgres -d smartshop"
rm ./dump.sql.tar
rm ./db_backups/dumps/dump.sql
sshpass -p $PASSWORD rm -rf $TMP_PATH
rm -rf $TMP_PATH
