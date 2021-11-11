sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo gunicorn -c /home/box/web/etc/gunicorn_wsgi.conf hello:app
sudo gunicorn -c /home/box/web/etc/gunicorn_django.conf ask.wsgi:application
