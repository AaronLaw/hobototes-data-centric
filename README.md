hobototes-data-centric
======================

web apps made for daily operation of hobototes.

heavily developed in [Django admin site] (https://docs.djangoproject.com/en/dev/ref/contrib/admin/)

If you find this web apps unstable, I feel sorry about that.
I try to be a pythoner, and am learning Django during I write this web apps.

Please feel free to tell me what you like and don't like on it.

## Requirement
* virtualenv & virtualenvwrapper
* Python 3.4.1
* Django 1.7rc2
* MySQL 5.5

and the following package in the isolated environment (exported by `pip freeze`):

	Django==1.7c3
	mysqlclient==1.3.2
	PyYAML==3.11
	django-taggit==0.12.1
	#django-contrib-comments==1.5
	# Markdown==2.4.1
	# django-markdown==0.6.1


## Usage

	git pull | git pull origin master | git pull origin <branch> | git pull <remote name> <branch># http://ihower.tw/git/remote.html

	./manage.py makemigrations
	./manage.py migrate

	./manage.py createsuperuser

and then go to `http://127.0.0.1:8000/admin`

Product app depends on the activity apps, on the marketing campaign

Pre-populate database
Google: django fixture | django initial database

* https://docs.djangoproject.com/en/dev/howto/initial-data/
* https://code.djangoproject.com/wiki/Fixtures
* https://github.com/alex/django-fixture-generator

## Problems & Error

### In v1.0.0 & v1.0.1 (the resolve version is release as v1.0.2)

When deploy, there maybe a dependency error : `KeyError: "Dependency references nonexistent parent node ('taggit'`.
This is caused by migration dependencies not correctly calculated:
* https://code.djangoproject.com/ticket/23021 -> 
* https://code.djangoproject.com/ticket/23008 ->
* https://code.djangoproject.com/ticket/22970

One possible solution is to delete all the migration files in `product/migrations`, and then run `/.manage.py makemigrations` and `./manage.py migrate` again to resolve it.

## Reference
* RealPython
* [Open Sourcing a Python Project the Right Way - Jeff Knupp] (http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/)
* http://codecondo.com/web-scraping-python/
* http://www.fullstackpython.com/best-python-resources.html
* [Medium - Laravel 4 Tutorials] (http://medium.com/laravel4)
    * from: Google: laravel tutorials. See also "wordpress", "django" in medium.com


Product Source status:

2014-04-16:
	inbox
	rejected
	approved | Watchlist
	bought

Django bulid a blog
* [Building a Blog with Django 1.7 in 16 mins] (https://www.youtube.com/watch?v=7rgph8en0Jc)
* [Building a Blog in 30 minutes with Django] (https://www.youtube.com/watch?v=srHZoj3ASmk)

Blog example
http://arunrocks.com/recreating-the-building-a-blog-in-django-screencast/
https://www.youtube.com/watch?v=7rgph8en0Jc
https://github.com/django/djangoproject.com/tree/master/blog

* http://www.tangowithdjango.com/book/index.html
* https://django-book.readthedocs.org/en/latest/# (from: http://www.meetup.com/Taipei-py/messages/boards/thread/34933702)
* http://www.barrymorrison.com/2012/10/zero-to-django-in-4-months-what-ive-learned-part-1/
* http://djangobook.py3k.cn/2.0/

Modern Django Project Template 
[edge - A Modern Django Project Template ](https://www.youtube.com/watch?v=8cCM18J4Nw4)

## Dependence / Plugins I use

### Tagging
Google: Django tagging
https://www.djangopackages.com/packages/p/django-taggit/

	sudo pip install django-taggit

### Caching

Memcache, redis

### Flatpage

I use it to create the notice board.
https://docs.djangoproject.com/en/dev/ref/contrib/flatpages/

## Plugins in my plan:
### Rating
https://github.com/dcramer/django-ratings

### Markdown
Google: django markdown
django_markdown
https://github.com/klen/django_markdown
[Building a blog with Django1.7 in 16 mins] (https://www.youtube.com/watch?v=7rgph8en0Jc)
http://arunrocks.com/recreating-the-building-a-blog-in-django-screencast/

### Django "excontrib" Comments
Google: Django comment system
https://github.com/django/django-contrib-comments


### Auto complete
django-autocomplete-light
https://www.youtube.com/watch?v=fJIHiqWKUXI
http://django-autocomplete-light.readthedocs.org/en/latest/
https://github.com/yourlabs/django-autocomplete-light/tree/master
https://github.com/yourlabs/django-autocomplete-light/tree/master/test_project/non_admin

### Workflow

> Managing state and transitions, aka workflow.

* https://github.com/kmmbvnr/django-viewflow
* https://www.djangopackages.com/packages/p/django-viewflow/
* https://gist.github.com/Nagyman/9502133 says workflow is a FSM (aka Finite State Machine).
* https://www.ruby-toolbox.com/categories/state_machines

### Address book
https://www.djangopackages.com/packages/p/django-cities-light/

### Django Admin interface
https://code.djangoproject.com/wiki/AdminNext

Google: django admin 2
https://github.com/pydanny/django-admin2 (from: https://code.djangoproject.com/wiki/AdminNext)

Google: django admin demo
django-suit
http://djangosuit.com/

Google: django admin theme
https://www.djangopackages.com/grids/g/admin-styling/
http://grappelliproject.com/
https://github.com/sehmaschine/django-grappelli
https://bitbucket.org/izi/django-admin-tools/wiki/Home (from: http://grappelliproject.com/)

### Django frontend
Google: django bootstrap
https://riccardo.forina.me/bootstrap-your-django-admin-in-3-minutes/

Google: django Boilerplate 

Google: django jquery
http://www.tangowithdjango.com/book/chapters/ajax.html

### File and Image Management

https://github.com/stefanfoulis/django-filer (from: http://django-suit.readthedocs.org/en/develop/)

### Django ROA
Django-ROA (Resource Oriented Architecture)
http://code.larlet.fr/django-roa/wiki/Home (from: https://code.djangoproject.com/wiki/AdminNext)

### Django ERP
https://github.com/django-bmf/django-bmf

### Dashboard
http://code.tutsplus.com/tutorials/adding-charts-to-your-site-with-highcharts--cms-21692

### Django Tutorials

https://code.djangoproject.com/wiki/Tutorials

### Image / Gallery / Media Management

https://www.djangopackages.com/search/?q=image
https://www.djangopackages.com/grids/g/gallery/
https://github.com/stefanfoulis/django-filer (from: http://djangosuit.com)

### Extend models
https://github.com/bconstantin/django_polymorphic

## Code snippet
access from the shell:
https://docs.djangoproject.com/en/dev/topics/db/models/
https://docs.djangoproject.com/en/dev/topics/db/queries/
from django.db import models

from product.models import *
help(Topic)

# get Queryset
t = Topic.objects.all()
type(t)

# get the 1st record
t1 = Topic.objects.get(pk=1)
type(t1)

t1.source_set.count() # -> 16

t1.tags
help(t1.tags)
t1.tags.get_queryset()
t1.tags.all()