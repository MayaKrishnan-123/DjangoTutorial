from .settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'testproject',
        'USER': 'testproject_user',
        'PASSWORD': 'testproject',
        'HOST': 'localhost',
        'PORT': '',
    }
}


AUTH_USER_MODEL = 'firstapp.User'

DEBUG = True