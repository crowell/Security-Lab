echo_bold () {
        message=${1} 
        echo -e "\033[1m${message}\033[0m"
}
echo_bold "Copying Apache2 config..."
cp apache2.conf /etc/apache2/apache2.conf
echo_bold "Clearing web server files...."
rm -fr /var/www/*
echo_bold "Copying files to web server...."
cp -R lab/* /var/www/
echo_bold "Changing permissions....."
./chmodder.sh

echo_bold "Starting mysql........."
mysql_status=$(service mysql start |grep "already running");
if [ -z "$mysql_status"]
then
        service mysql restart
fi

echo_bold "Seeding the mysql database........."
./seed.sh

echo_bold "Starting apache2..........."
service apache2 restart

