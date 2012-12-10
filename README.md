just run setup.sh, this script will do the following

* set apache2 config
* clear /var/www (even if you've got stuff there!)
* change permissions of files in /var/www using `chmodder.sh`
* start mysqld 
* seed mysql using `seed.sh`
* restart apache2
* copy new motd


