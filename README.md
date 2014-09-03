hobototes-data-centric
======================

web apps made for daily operation of hobototes


## Requirement
* virtualenv & virtualenvwrapper
* Python 3.4.1
* Django 1.7rc2

Django==1.7c3
<!-- Markdown==2.4.1 -->
PyYAML==3.11
<!-- django-contrib-comments==1.5
django-markdown==0.6.1
django-taggit==0.12.1
 -->
 mysqlclient==1.3.2


## Usage

	git pull | git pull origin master | git pull origin <branch> | git pull <remote name> <branch># http://ihower.tw/git/remote.html

	./manage.py makemigrations
	./manage.py migrate

	./manage.py createsuperuser

Pre-popular database
Google: django fixture | django initial database
* https://docs.djangoproject.com/en/dev/howto/initial-data/
* https://github.com/alex/django-fixture-generator

## Reference
Django bulid a blog
* [Building a Blog with Django 1.7 in 16 mins] (https://www.youtube.com/watch?v=7rgph8en0Jc)
* [Building a Blog in 30 minutes with Django] (https://www.youtube.com/watch?v=srHZoj3ASmk)

Blog example
http://arunrocks.com/recreating-the-building-a-blog-in-django-screencast/
https://www.youtube.com/watch?v=7rgph8en0Jc
https://github.com/django/djangoproject.com/tree/master/blog

* https://django-book.readthedocs.org/en/latest/# (from: http://www.meetup.com/Taipei-py/messages/boards/thread/34933702)

## Dependence / Plugins in use

### Tagging
Google: Django tagging
https://www.djangopackages.com/packages/p/django-taggit/

	sudo pip install django-taggit


## In planning:
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

### Django Admin interface
Google: django admin 2


Google: django admin demo
django-suit
http://djangosuit.com/

Google: django admin theme
https://www.djangopackages.com/grids/g/admin-styling/
http://grappelliproject.com/
https://github.com/sehmaschine/django-grappelli

### Django frontend
Google: django bootstrap

Google: django Boilerplate 

### File and Image Management

https://github.com/stefanfoulis/django-filer (from: http://django-suit.readthedocs.org/en/develop/)

### Django Tutorials

https://code.djangoproject.com/wiki/Tutorials

### Image / Gallery / Media Management

https://www.djangopackages.com/search/?q=image
https://www.djangopackages.com/grids/g/gallery/