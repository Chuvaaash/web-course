sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default

mkdir /home/box/etc/
sudo mv /home/box/web/etc/hello.py /home/box/etc/hello.py
sudo ln -s /home/box/etc/hello.py /etc/gunicorn.d/hello.py

cd /home/box/web/ask/
sudo nginx
gunicorn --config /home/box/etc/hello.py ask.wsgi 

