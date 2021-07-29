sudo ln -sf /home/oliver/python_project/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn -c /home/oliver/python_project/box/web/etc/django.py ask.wsgi:application
gunicorn -c /home/oliver/python_project/box/web/etc/hello.py hello:app
