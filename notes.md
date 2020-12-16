# Notes

Quick reference notes for future Django projects.

## General concepts
- A project is the entire site, data and all components thereof. An app is a part of a project, and can serve a number of funvtions. Both should be created from the command line

## Django CLI commands

Start project:
```shell
django-admin startproject <projectname>
```

Start development server command:
```shell
python manage.py runserver
```

Create app:
```shell
python manage.py startapp articles
```

Built-in app migrations and migrate migration files:
```shell
python manage.py migrate
```

Create migrations file for new/updated model (migrate must be run again after this to update DB):
```shell
python manage.py makemigrations
```

Open interactive shell to interact with database:
```shell
python manage.py shell
```

In shell, to add/query data from a given table:
```shell
>>> from articles.models import Article
>>> article = Article
>>> article.title = "cool title"
>>> Article.objects.all()
```

Create superuser for admin area
```shell
python manage.py createsuperuser
```

## Other

To make models/db stuff appear in the admin area, register them within the admin folder of thier app.