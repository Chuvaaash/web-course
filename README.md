## Web-course project
Репозиторий содержит проект простого сайта, созданного на курсе [Web-технологии](https://stepik.org/course/154/syllabus).
### Description
В проекте создан простой сайт с вопросами и ответами (скриншоты ниже).
Backend сайта использует фреймворк Django.
Для запуска сайта используется nginx+gunicorn.
Настройки nginx лежат в файле etc/nginx.conf.
В качестве базы данных используется mysql.
Настройка работы gunicorn с nginx взята из
[статьи](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04-ru#systemd-gunicorn).

### Screenshots
Главная страница

![alt text](https://github.com/Chuvaaash/web-course/blob/main/screenshots/main_page.jpg?raw=true)

Страница с одним вопросом

![alt text](https://github.com/Chuvaaash/web-course/blob/main/screenshots/question_page.jpg?raw=true)

Страница регистрации

![alt text](https://github.com/Chuvaaash/web-course/blob/main/screenshots/signup_page.jpg?raw=true)