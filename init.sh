sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default

mkdir /home/box/etc/
sudo mv /home/box/web/etc/hello.py /home/box/etc/hello.py
sudo ln -s /home/box/etc/hello.py /etc/gunicorn.d/hello.py

sudo /etc/init.d/mysql start
mysql -u 'root' -e 'create database db_qa'
mysql -u 'root' -e 'grant all privileges on db_qa.* to 'box'@'localhost' with grant option'
python3 ~/web/ask/manage.py makemigrations
python3 ~/web/ask/manage.py migrate

cd /home/box/web/ask/
sudo nginx
gunicorn --config /home/box/etc/hello.py ask.wsgi

