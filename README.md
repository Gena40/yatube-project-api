# Проект Yatube
## Небольшая соцсеть с возможностью создавать, редактировать и удалять посты с картинками, подписываться на других авторов. В проекте реализовано API v1, документацию в стандарте OpenAPI к которому можно найти на эндпоинте /redoc/.
### Технологии в проекте:
- Django 2.2.16
- djangorestframework
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Gena40/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```