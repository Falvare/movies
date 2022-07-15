from .settings import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['dj-characters.herokuapp.com', '127.0.0.1']

CSRF_TRUSTED_ORIGINS = [
    'https://dj-characters.herokuapp.com/'
]