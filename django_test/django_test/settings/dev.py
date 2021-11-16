from .defaults import *
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_test',
        'USER': 'root',
        'PASSWORD': 'Password12@!',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}