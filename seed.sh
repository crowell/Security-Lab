#!/bin/bash

MYSQL="mysql -u root --password=toor"
MYSQLD="$MYSQL --database=securelab"
$MYSQL -e "DROP DATABASE IF EXISTS securelab"
$MYSQL -e "CREATE DATABASE securelab"
$MYSQLD -e "CREATE TABLE users (ID MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY, username VARCHAR(60), password VARCHAR(60));"
$MYSQLD -e "INSERT INTO users (username, password) VALUES ('admin', '3d86d1182128f237ee0b378a9b36b8a5');" #ec521thiscannotbecrackedbycrackstation
$MYSQLD -e "INSERT INTO users (username, password) VALUES ('James Bond', 'b5117cab4abf1b39ff9a03a3a3f2862c');"
$MYSQLD -e "INSERT INTO users (username, password) VALUES ('xss', '78a862bb04af562c9d28fb0f3d7e68e2');"


TABLES=(
"products"
"customers"
"answers"
"questions"
"meaningOfLife"
"pokemon"
"patents"
"lawsuits"
"copyrights"
"tradeSecrets"
);

for name in ${TABLES[@]}; do
$MYSQLD -e "CREATE TABLE ${name} (ID MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY, company_id INT, string VARCHAR(30));"
done



