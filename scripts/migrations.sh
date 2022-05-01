#!/usr/bin/env bash


# shellcheck disable=SC2154
echo "$action $tablename"
#if [[ $environment == "downgrade" ]];
#    then
#        downgrade_db_migrations
#    elif [ $environment == "upgrade" ];
#    then
#        downgrade_db_migrations
#    elif [ $environment == "production" ];
#    then
#        check_db_migrations_history
#    else
#        create_migrations
#     fi
#
#create_migrations() {
#    echo "create a new migration file suffixed with $file_name";
#    flask db migrate -m "$file_name"
#}
#
#upgrade_db_migrations(){
#    do_all_exports;
#    echo "upgrade the database";
#    flask db upgrade;
#}
#
#downgrade_db_migrations(){
#    do_all_exports;
#    echo "downgrade the database";
#    flask db downgrade;
#}
#
#check_db_migrations_history(){
#    do_all_exports;
#    echo "listing the migration history";
#    flask db history;
#}