sudo /etc/init.d/mysql start
mysql -uroot -e "create database django;"
mysql -uroot -e "grant all privileges on django.* to 'root'@'localhost' with grant option;"
