#!/bin/bash
echo -n "Server IP (for example: prime.sbdev.sk)":
read SERVER_IP

echo -n User:
read USER

echo -n Password:
read -s PASSWORD
echo

echo -n "Project dir (for example: temponabytok)" :
read PROJECT_DIR

HOME_DIR_ON_SERVER="/home/gitlab/${PROJECT_DIR}/"
TMP_PATH=$(mktemp -d)
DUMPS_DIR="${HOME_DIR_ON_SERVER}/db_backups/dumps/"
SERVER=${USER}@${SERVER_IP}

sshpass -v -p $PASSWORD ssh -o PubkeyAuthentication=no -o StrictHostKeyChecking=no $SERVER "
    mkdir ${TMP_PATH}
    cd ${HOME_DIR_ON_SERVER}
    docker-compose exec -T db bash -c 'bash /db_backups/dump_database.sh'
    cd ${HOME_DIR_ON_SERVER}webapp/django_project/
    find . -path '*migrations*' -name '*.py' -not -path '*__init__*' -exec cp --parents \{\} ${TMP_PATH} \;
"

find ./project ./sbcore -path "*migrations*" -name "*.py" -not -path "*__init__*" -not -path "*sb_migrations*"  -not -name "fix_migrations.py" -exec rm {} \;
docker compose stop db
docker compose rm -f db
currentDir="$(basename $PWD)"
docker volume rm -f $currentDir"_db-data"
DUMP_FILE_NAME=$(sshpass -p $PASSWORD ssh -o PubkeyAuthentication=no -o StrictHostKeyChecking=no $SERVER "ls -tp ${DUMPS_DIR} | grep -v / | head -n 1")
sshpass -p $PASSWORD rsync -rtu -e 'ssh -o PubkeyAuthentication=no -o StrictHostKeyChecking=no -p 22' $SERVER:$TMP_PATH/* .
sshpass -p $PASSWORD rsync -rtu -e 'ssh -o PubkeyAuthentication=no -o StrictHostKeyChecking=no -p 22' $SERVER:${HOME_DIR_ON_SERVER}db_backups/dumps/$DUMP_FILE_NAME ./dump.sql.tar
tar -xvkf dump.sql.tar
DUMP_FILE_NAME=${DUMP_FILE_NAME/".tar"/""}
docker compose up -d db
sleep 5
cat "./db_backups/dumps/${DUMP_FILE_NAME}" | docker exec -i $currentDir"-db-1" psql -U smartshop -d smartshop
rm ./dump.sql.tar
rm -rf ./db_backups
sshpass -p $PASSWORD rm -rf $TMP_PATH
rm -rf $TMP_PATH
