import os
from .base import *  # noqa

DEBUG = False

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_learner',
        'USER': 'django_learner',
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': 'localhost'
    }
}
