"""
Django settings for hobototes_data_centric project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7)+-_!9t(4r(#qt^4dc_u((789(4m_hg-drx!a4udgr9@!8r^)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['127.0.0.1', '192.168.0.103', 'aaron213.dlinkddns.com']


# Application definition

INSTALLED_APPS = (
    'autocomplete_light', # pip install 'django-autocomplete-light>=2.0.0a1',
        # http://django-autocomplete-light.readthedocs.org/en/v2/install.html
    'cacheops',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages', # flatpages, use in notice board
        # https://docs.djangoproject.com/en/dev/ref/contrib/flatpages/
    'activity',
    'product', # product depends activity on the marketing campaigns
    'taggit', # pip install django-taggit
    'django.contrib.sites', # use in flatpages,
    # 'django_comments',
)
SITE_ID=1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # for johnny-cache
    # 'johnny.middleware.LocalStoreClearMiddleware',
    # 'johnny.middleware.QueryCacheMiddleware',

    # for setup cache
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware', # for using flatpages
)

ROOT_URLCONF = 'hobototes_data_centric.urls'

WSGI_APPLICATION = 'hobototes_data_centric.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hobototes',
        'USER': 'aaron',
        'PASSWORD': '0858324',
        'HOST': '127.0.0.1',
        'PORT': '3306',

    # https://docs.djangoproject.com/en/dev/ref/databases/
    # -> https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-CONN_MAX_AGE
        'CONN_MAX_AGE' : 600,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us' # https://docs.djangoproject.com/en/dev/ref/settings/

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Google: django set-0-id (2014-08-05)
# https://code.djangoproject.com/ticket/17653
# SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";

# Local-memory caching
# https://docs.djangoproject.com/en/dev/topics/cache/
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-CACHES
# CACHES = {
#     # 'default': {
#     #     'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#     #     'LOCATION': 'unique-snowflake',
#     #     }
#     # 'filebased': {
#     #     'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#     #     'LOCATION': '/var/tmp/django_cache',
#     #     }
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',

#         'TIMEOUT': 'None',
#         'VERSION': 1,
#         'CACHE_MIDDLEWARE_ALIAS': 'default',
#         'CACHE_MIDDLEWARE_SECONDS': 600,
#         'CACHE_MIDDLEWARE_KEY_PREFIX': '',
#     }
# }

CACHEOPS_REDIS = {
    'host': 'localhost', # redis-server is on same machine
    'port': 6379,        # default redis port
    'db': 1,             # SELECT non-default redis database
                         # using separate redis db or redis instance
                         # is highly recommended
    'socket_timeout': 30,
}

CACHEOPS = {
    # Automatically cache any User.objects.get() calls for 15 minutes
    # This includes request.user or post.author access,
    # where Post.author is a foreign key to auth.User
    'auth.user': ('get', 60*15),

    # Automatically cache all gets, queryset fetches and counts
    # to other django.contrib.auth models for an hour
    'auth.*': ('all', 60*60),

    # Enable manual caching on all news models with default timeout of an hour
    # Use News.objects.cache().get(...)
    #  or Tags.objects.filter(...).order_by(...).cache()
    # to cache particular ORM request.
    # Invalidation is still automatic
    'news.*': ('just_enable', 60*60),

    # Automatically cache count requests for all other models for 15 min
    # '*.*': ('count', 60*15),
    '*.*': ('all', 60*15),

    # 'admin.*': ('all', 60*60),
    # 'topic.*': ('all', 60*60),
    # 'source.*': ('all', 60*60),
}

