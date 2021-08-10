sudo /etc/init.d/nginx start
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn -c /home/box/web/etc/django.py ask.wsgi:application
#gunicorn -c /home/oliver/web/etc/hello.py hello:app
