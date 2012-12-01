#!/bin/bash

MYSQL="mysql -u root --password=toor"
MYSQLD="$MYSQL --database=securelab"
$MYSQL -e "DROP DATABASE IF EXISTS securelab"
$MYSQL -e "CREATE DATABASE securelab"
$MYSQLD -e "CREATE TABLE users (ID MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY, username VARCHAR(60), password VARCHAR(60));"
$MYSQLD -e "INSERT INTO users (username, password) VALUES ('admin', '767127cbb24c0291981dd2cb8bad38c9');"
$MYSQLD -e "INSERT INTO users (username, password) VALUES ('James Bond', 'b5117cab4abf1b39ff9a03a3a3f2862c');"
$MYSQLD -e "CREATE TABLE secrets (ID MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY, secret VARCHAR(200));"
$MYSQLD -e "CREATE TABLE challenges (ID MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY, score INT, challenge VARCHAR(60));"
