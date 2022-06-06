sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
mkdir /home/box/etc/
sudo mv /home/box/web/etc/hello.py /home/box/etc/hello.py
sudo ln -s /home/box/etc/hello.py /etc/gunicorn.d/hello.py

cd /home/box/web/
sudo nginx
sudo gunicorn --config /home/box/etc/hello.py hello:wsgi_application 

