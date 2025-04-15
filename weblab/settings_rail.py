from weblab.settings import *
from decouple import config

SECRET_KEY= config('SECRET_KEY')

ALLOWED_HOSTS = ['web-production-42e7a.up.railway.app']