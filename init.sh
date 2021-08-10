sudo ln -sf /home/oliver/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn -c /home/oliver/web/etc/django.py ask.wsgi:application
#gunicorn -c /home/oliver/web/etc/hello.py hello:app
sudo /etc/init.d/mysql restart

#mysql -uroot -e "create database django;"
#mysql -uroot -e "grant all privileges on stepic_web.* to 'root'@'localhost' with grant option;"
