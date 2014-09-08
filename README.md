hobototes-data-centric
======================

web apps made for daily operation of hobototes

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

Pre-populate database
Google: django fixture | django initial database

* https://docs.djangoproject.com/en/dev/howto/initial-data/
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
Django bulid a blog
* [Building a Blog with Django 1.7 in 16 mins] (https://www.youtube.com/watch?v=7rgph8en0Jc)
* [Building a Blog in 30 minutes with Django] (https://www.youtube.com/watch?v=srHZoj3ASmk)

Blog example
http://arunrocks.com/recreating-the-building-a-blog-in-django-screencast/
https://www.youtube.com/watch?v=7rgph8en0Jc
https://github.com/django/djangoproject.com/tree/master/blog

* https://django-book.readthedocs.org/en/latest/# (from: http://www.meetup.com/Taipei-py/messages/boards/thread/34933702)
* http://www.barrymorrison.com/2012/10/zero-to-django-in-4-months-what-ive-learned-part-1/

## Dependence / Plugins I use

### Tagging
Google: Django tagging
https://www.djangopackages.com/packages/p/django-taggit/

	sudo pip install django-taggit


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

### Django Admin interface
Google: django admin 2


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

### File and Image Management

https://github.com/stefanfoulis/django-filer (from: http://django-suit.readthedocs.org/en/develop/)

### Django Tutorials

https://code.djangoproject.com/wiki/Tutorials

### Image / Gallery / Media Management

https://www.djangopackages.com/search/?q=image
https://www.djangopackages.com/grids/g/gallery/
https://github.com/stefanfoulis/django-filer (from: http://djangosuit.com)

### Extend models
https://github.com/bconstantin/django_polymorphic