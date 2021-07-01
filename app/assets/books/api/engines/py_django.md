# Django 

Open source Python Web framework: rapid development and clean, pragmatic design
Focus on writing your app without needing to reinvent the wheel

 To add a bit more to your stack: simple, secure with great performance
 in-built templates that offer performance
 
  - https://www.djangoproject.com
  
  >pip install Django
  >python -m django --version
  > django-admin startproject mysite
  > python manage.py runserver
  > python manage.py runserver 8080
  
  mysite/
    manage.py             cli to interact with this Django project
    mysite/               Python package for your project
        __init__.py       An empty file that tells Python that this directory should be considered a Python package 
        settings.py
        urls.py
        asgi.py           Entry-point for ASGI-compatible web servers to serve your project
        wsgi.py           An entry-point for WSGI-compatible web servers to serve your project.
        
>py manage.py startapp polls        

polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
    
> py manage.py runserver    