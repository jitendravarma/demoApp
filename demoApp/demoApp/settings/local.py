import os

from .base import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'demoapp',
        'USER': 'postgres',
        'PASSWORD': 'root#123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
