from .base import *  # noqa

DEBUG = True

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_learner',
        'USER': 'django_learner',
        'PASSWORD': 'admin',
        'HOST': 'localhost'
    }
}
