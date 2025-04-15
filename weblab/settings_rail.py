from weblab.settings import *
from decouple import config

SECRET_KEY= config('SECRET_KEY')

ALLOWED_HOSTS = ['https://web-production-42e7a.up.railway.app/']