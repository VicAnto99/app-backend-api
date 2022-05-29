"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 2.2.24.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import mongoengine
from datetime import timedelta

from dotenv import load_dotenv

from pymongo import MongoClient
import certifi

import django_heroku
import dj_database_url

load_dotenv()


DB_SQL = os.getenv('LOCAL_SQL_DB')
USER_SQL = os.getenv('USER_LOCAL_SQL_DB')
PASSWORD_SQL = os.getenv('PASSWORD_LOCAL_SQL_DB')
DB_MONGO = os.getenv('LOCAL_MONGO_DB')
USER_MONGO = os.getenv('USER_LOCAL_MONGO_DB')
PASSWORD_MONGO = os.getenv('PASSWORD_LOCAL_MONGO_DB')
DB_CL='mongodb+srv://manuelortiz:mfkm03162212@newcluster.0vf8b.mongodb.net/reservamedb?retryWrites=true&w=majority'
# # mongoengine.connect(host=DB_CL)
# client = MongoClient("localhost", 27017)
# db = 'reservamedb'
ca = certifi.where()
mongoengine.connect(host=DB_CL, tlsCAFile=ca)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
#'(@r5+6oqd#qpqq0oaolr_-_=45g5s$jh(%yws7lc4*s%$t3%xx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['reservame-appointments.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'djoser',
    'reservame',
    'rest_framework_simplejwt.token_blacklist',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

#os.path.join(BASE_DIR, 'build')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':  [os.path.join(BASE_DIR, 'build')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

""" DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_SQL,
        'USER': USER_SQL,
        'PASSWORD': PASSWORD_SQL,
        'HOST': 'localhost',
        'PORT': '3306',
    },

} """
DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)




# DATABASES = {
#     'default' : {
#         'ENGINE' : 'django_mongodb_engine',
#         'NAME' : 'reservamedb',
#     }
# }



#reservameapp0@gmail.com
#tvxqwioxbfxbgann

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'reservameapp0@gmail.com'
EMAIL_HOST_PASSWORD = 'tvxqwioxbfxbgann'
EMAIL_USE_TLS = True



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'build/static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'https://reservame-appointments.herokuapp.com/'
]




CORS_ALLOW_CREDENTIALS = True

CSRF_COOKIE_DOMAIN = 'http://192.168.56.1:3000' 

CSRF_COOKIE_PATH = 'http://localhost:3000'

SESSION_COOKIE_DOMAIN = 'http://localhost:3000'

SESSION_COOKIE_SECURE = False

REST_FRAMEWORK = {
    'DEFAULT_PERMISSIONS_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
}

DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'SET_USERNAME_RETYPE': True,
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {
        'user_create': 'reservame.serializers.UserCreateSerializer',
        'user': 'reservame.serializers.UserCreateSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    },
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=40),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=360),
}

AUTH_USER_MODEL = 'reservame.UserAccount'

django_heroku.settings(locals())