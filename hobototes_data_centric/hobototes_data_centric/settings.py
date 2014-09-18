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

ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['127.0.0.1', '192.168.0.105', 'aaron213.dlinkddns.com']


# Application definition

INSTALLED_APPS = (
    'autocomplete_light', # pip install 'django-autocomplete-light>=2.0.0a1',
        # http://django-autocomplete-light.readthedocs.org/en/v2/install.html
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'product',
    'taggit', # pip install django-taggit
    # 'django.contrib.sites',
    # 'django_comments',
)
# SITE_ID=1

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
CACHES = {
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    #     'LOCATION': 'unique-snowflake',
    #     }
    # 'filebased': {
    #     'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
    #     'LOCATION': '/var/tmp/django_cache',
    #     }
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',

        'TIMEOUT': 'None',
        'VERSION': 1,
        'CACHE_MIDDLEWARE_ALIAS': 'default',
        'CACHE_MIDDLEWARE_SECONDS': 600,
        'CACHE_MIDDLEWARE_KEY_PREFIX': '',
    }
}