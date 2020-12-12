# Notes

Start project:
```python
django-admin startproject <projectname>
```

Start development server command:
```python
python manage.py runserver
```

Create app:
```python
python manage.py startapp articles
```

Built-in app migrations and migrate migration files:
```python
python manage.py migrate
```

Create migrations file for new/updated model (migrate must be run again after this to update DB):
```python
python manage.py makemigrations
```

Open interactive shell to interact with database:
```python
python manage.py shell
```

In shell, to add/query data from a given table:
```shell
>>> from articles.models import Article
>>> article = Article
>>> article.title = "cool title"
>>> Article.objects.all()
```