# YAFADEI
Интернет-ресурс для размещения постов и работ, посвященных изобразительному искусству.

## Технологии 

- [Python 3.12](https://www.python.org/)
- [Django 5.0.3](https://www.djangoproject.com/) 

## Установка и запуск 
Создайте и активируйте виртуальное окружение:
* Windows

```sh
python -m venv venv
venv\Scripts\activate
```
* Linux и MacOS

```sh
python3 -m venv venv
source venv/bin/activate
```
Установите основные зависимости проекта:
```sh
pip install --upgrade pip
pip install -r requirements.txt
```
Запуск проекта:
* Windows
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
* Linux и MacOS
```sh
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```