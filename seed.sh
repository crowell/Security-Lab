#!/bin/bash

MYSQL="mysql -u root --password=toor"
MYSQLD="$MYSQL --database=securelab"
$MYSQL -e "DROP DATABASE IF EXISTS securelab"
$MYSQL -e "CREATE DATABASE securelab"
$MYSQLD -e "CREATE TABLE users (ID MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY, username VARCHAR(60), password VARCHAR(60));"
$MYSQLD -e "INSERT INTO users (username, password) VALUES ('admin', '6ea27872aeabcec0a4d74697e1786225');"
$MYSQLD -e "INSERT INTO users (username, password) VALUES ('James Bond', 'b5117cab4abf1b39ff9a03a3a3f2862c');"

TABLES=(
"products"
"admins"
"offices"
"executives"
"secrets"
"challenges"
"labs"
"hardware"
"software"
"devices"
"vendors"
"partners"
"affiliates"
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



