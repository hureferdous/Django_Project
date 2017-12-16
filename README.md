# Gift site is made by Django, Python, Sqlite

## Introduction
Gift site is developed by __Django__. Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Django has an authentication framework which allows user's to login into the the application easily. In this project __user authentication__ is done by user email and password authentication. __Bootstrap__ is used to make it responsive and __Paypal__ payment process is developed by __django-paypal__ to any transaction of products. 

## Structure
The Gift site has one main project is called Gift. __Gift__ project has three Apps called __products__, __user_account__ and __paypal_store__. 
* __products:__ This app contains all the product categories and products details.
* __user_account:__ By using this app user can register, login and logout from the site.
* __paypal_store:__ This app includes all the payments transaction on site.
* __requriments.txt:__ In this text file all the dependency need for the project.


![structure](https://user-images.githubusercontent.com/24476948/34054674-eaabcdd0-e1c3-11e7-88ac-95328db6db09.png)



## Main steps to develop the project
1. __Create Project:__
To start to develop site we need to install python and django in our device by using this comment below:
``` 
python --version
```
```
easy_install --version
```
```
easy_install django
```
Now using django-admin we create our Gift project.
```
django-admin startproject Gift
```
Then we got those file in Gift project:
* __manage.py__: Perfoms admin tasks for our project, such as putting it on the system path, or starting the built-in webserver.
* __settings.py__: This is the settings file for your project, where you define your project’s configuration settings, including database connections, other applications, templates, and more.
* __urls.py__: The url declarations for this Django project. This file contains a list of mappings which connect urls to views.
* __wsgi.py__: An entry-point for WSGI-compatible web servers to serve our project. This file handles our requests/responses to/from Django development server.
* ____init__ __.py__: An empty file that informs Python that this directory should be considered a Python package.

 2. __Create App:__ 
 To create the app we need to use this comment below:
 ```
 django-admin start app products
 ```
 ```
 django-admin start app user_account
 ```
 ```
 django-admin start app paypal_store
 ```
After doinig this we need to Update the INSTALLED_APPS in your settings.py file:

![sett](https://user-images.githubusercontent.com/24476948/34059391-c6571c2e-e1d6-11e7-99bb-6555d9d2c47c.png)

3.__Create Super User:__ 
To manage the admin section we need to create a super user in our site. By using below comment in terminal a super user can create:
```
python manage.py createsuperuser
```


## Content
1.__products:__
The products app is include those file like migrations, static, templates,__init.py__,  admin.py, apps.py, models.py, tests.py, views.py and urls.py.

![product2](https://user-images.githubusercontent.com/24476948/34073338-712453ca-e28f-11e7-99c1-3a9a9579d540.png)

* __models.py:__ First we have to create our database for our products in models.py file. There are two class is created for Product and Category to store in database. Then we apply below comment in terminal:
```
python manage.py makemigrations 
```
```
python manage.py migrate
```

* __admin.py:__ 
To get the all Product and Category in our admin site we need to add this in admin.py:
```
from django.contrib import admin
from .models import Category, Product
```
```
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
```
* __urls.py:__
The url tag helps us to generate links in the templates.At this point urls.py file in products app looks like this:

![urls1](https://user-images.githubusercontent.com/24476948/34073548-f7393008-e293-11e7-81b3-81862c02b3c6.png)

* __views.py:__
Django has the concept of views to encapsulate the logic responsible for processing a user’s request and for returning the response.Add a view function to views.py is connect to our urls.py and show the html pages from the templates.
```
from django.shortcuts import render, get_object_or_404
from .models import Product, Category

```
* __get_object_or_404()__ This pattern is so common that [Django](https://www.djangoproject.com/start/overview/) a provides a shortcurt method called [get_object_or_404()](https://overiq.com/django/1.10/showing-404-errors-in-django). To use get_object_or_404() method with models, queryset and managers. It also shows that when a matching record is not found, get_object_or_404() raises Http404 exception.
* __render()__
To combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.Django does not provide a shortcut function which returns a TemplateResponse because the constructor of TemplateResponse offers the same level of convenience as [render()](https://docs.djangoproject.com/en/2.0/topics/http/shortcuts/).
```
return render(request, "products/products_view/product_list.html",
 {"products": products,"category":category,"categories":categories})
```

## Technology stack

## Instructions
