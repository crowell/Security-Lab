cp apache2.conf /etc/apache2/apache2.conf
rm -fr /var/www/*
cp -R lab/* /var/www/
./chmodder.sh

